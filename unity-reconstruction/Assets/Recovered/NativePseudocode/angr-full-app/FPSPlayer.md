# Native pseudocode: FPSPlayer

> Metadata source-path string: `Assets/RFPSP/Scripts/Player/FPSPlayer.cs`. This is a path string from the APK metadata, not recovered source text.

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `FPSPlayer.Start` — RVA `0xc9cfcc`

- Decompiled symbol: `FPSPlayer_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `3008` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FPSPlayer_Recovered` matched 15 offsets against `FPSPlayer` metadata (confidence 1.00).

```c
typedef struct FPSPlayer_Recovered {
    char padding_0[56];
    unsigned int Healthcounter;
    char padding_3c[20];
    long long IronsightsComponent;
    long long InputComponent;
    long long FPSWalkerComponent;
    long long PlayerWeaponsComponent;
    long long WorldRecenterComponent;
    char padding_78[8];
    long long MouseLookComponent;
    long long WeaponEffectsComponent;
    char padding_90[8];
    struct struct_1 *CameraControlComponent;
    char padding_a0[40];
    long long weaponObj;
    char padding_d0[8];
    long long painFadeObj;
    struct struct_4 *painFadeComponent;
    char padding_e8[280];
    long long mainCamTransform;
    char removePrefabRoot;
    char padding_209[631];
    long long myTransform;
} FPSPlayer_Recovered;

typedef struct struct_7 {
    char padding_0[48];
    unsigned long long field_30;
} struct_7;

typedef struct struct_10 {
    char padding_0[32];
    struct struct_11 *field_20;
} struct_10;

typedef struct struct_12 {
    char padding_0[664];
    struct struct_13 *field_298;
    unsigned long long field_2a0;
} struct_12;

typedef struct struct_1 {
    char padding_0[48];
    long long field_30;
} struct_1;

typedef struct struct_4 {
    char padding_0[32];
    struct struct_5 *field_20;
} struct_4;

typedef struct struct_11 {
    struct struct_8 *field_0;
} struct_11;

typedef struct struct_13 {
    unsigned long long field_0;
} struct_13;

typedef struct struct_5 {
    struct struct_2 *field_0;
} struct_5;

typedef struct struct_8 {
    char padding_0[664];
    struct struct_9 *field_298;
    unsigned long long field_2a0;
} struct_8;

typedef struct struct_2 {
    char padding_0[664];
    struct struct_3 *field_298;
    unsigned long long field_2a0;
} struct_2;

typedef struct struct_9 {
    unsigned long long field_0;
} struct_9;

typedef struct struct_3 {
    unsigned long long field_0;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef0e48;
extern long long g_1efcf38;
extern long long g_1efcfa0;
extern long long g_1efcfd0;
extern long long g_1efcfd8;
extern long long g_1efcfe8;
extern long long g_1efd008;
extern long long g_1efd098;
extern long long g_1efd0b0;
extern long long g_1efd0d8;
extern long long g_1efd178;
extern long long g_1efebe8;
extern long long g_1efebf0;
extern long long g_1efec00;
extern long long g_1efec28;
extern long long g_1efec78;
extern long long g_1efec80;
extern long long g_1efec90;
extern long long g_1efec98;
extern long long g_1efecf0;
extern long long g_1efed20;
extern long long g_1f0a668;
extern long long g_1f0a9f0;
extern long long g_1f0c4b8;
extern char g_1fab4ab;

void FPSPlayer_Start(struct_6 *ptr)
{
    unsigned long long v7;  // x30
    unsigned long long v8;  // x24
    long long v17;  // x0
    long long v18;  // x1
    long long v19;  // x1
    struct_6 *p;  // x0
    long long v21;  // x1
    struct_6 *addr;  // x0
    long long v23;  // x1
    struct_6 *ptr3;  // x0
    long long v25;  // x1
    struct_6 *ptr4;  // x0
    unsigned long long v9;  // x23
    long long v27;  // x0
    struct_6 *ptr5;  // x21
    struct_6 *v29;  // x21
    struct_7 *v30;  // x0
    struct_6 *ptr6;  // x21
    struct_6 *v32;  // x21
    unsigned long v33;  // x1
    struct_6 *ptr7;  // x21
    struct_6 *v35;  // x21
    long long v36;  // x0
    unsigned long long v10;  // x22
    struct_6 *ptr8;  // x21
    struct_6 *v38;  // x21
    long long v39;  // x0
    struct_6 *ptr9;  // x21
    struct_6 *v41;  // x21
    unsigned long long flag;  // x2
    struct_10 *v43;  // x0
    struct_6 *ptr10;  // x21
    struct_6 *ptr11;  // x21
    struct_10 *ptr12;  // x22
    unsigned long long v11;  // x21
    struct_12 **v47;  // x0
    struct_12 **v48;  // x0
    unsigned long v49;  // x1
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    unsigned int v14;  // w0
    unsigned int v15;  // w8
    long long v16;  // x0
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]
    unsigned long long v5;  // [bp-0x10]
    unsigned long long v6;  // [bp-0x8]

    v0 = v7;
    v1 = v8;
    v2 = v9;
    v3 = v10;
    v4 = v11;
    v5 = v12;
    v6 = v13;
    if (!(g_1fab4ab & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efcfa0);
        sub_f7d92c(&g_1efcfd0);
        sub_f7d92c(&g_1efcfd8);
        sub_f7d92c(&g_1efcfe8);
        sub_f7d92c(&g_1efd008);
        sub_f7d92c(&g_1efd098);
        sub_f7d92c(&g_1efd0b0);
        sub_f7d92c(&g_1efd0d8);
        sub_f7d92c(&g_1efd178);
        sub_f7d92c(&g_1efebe8);
        sub_f7d92c(&g_1efebf0);
        sub_f7d92c(&g_1efec00);
        sub_f7d92c(&g_1efec28);
        sub_f7d92c(&g_1efec78);
        sub_f7d92c(&g_1efec80);
        sub_f7d92c(&g_1efec90);
        sub_f7d92c(&g_1efec98);
        sub_f7d92c(&g_1efecf0);
        sub_f7d92c(&g_1efed20);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef0e48);
        sub_f7d92c(&g_1f0a668);
        sub_f7d92c(&g_1f0a9f0);
        sub_f7d92c(&g_1f0c4b8);
        g_1fab4ab = 1;
    }
    v14 = PlayerPrefs__GetInt(g_1f0a9f0, 0);
    v15 = ptr->field_208;
    ptr->field_38 = v14;
    if (v15)
    {
        if (!Component__get_transform(ptr, 0) || !Transform__get_parent() || !Component__get_transform() || !((v16 = Component__get_gameObject(), Component__get_transform(ptr, 0) && (unsigned long long)Transform__get_parent() && Component__get_transform())))
            goto LABEL_109db84;
        Transform__DetachChildren();
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        Object__Destroy(Component__get_gameObject(), 0);
    }
    if (Camera__get_main(0))
    {
        v17 = Component__get_transform();
        ptr->field_200 = v17;
        sub_f7d8d0(&ptr->field_200, v17);
        v18 = Component__get_transform(ptr, 0);
        ptr->field_480 = v18;
        sub_f7d8d0(&ptr->field_480, v18);
        v19 = sub_1231bc8(ptr, g_1efcfe8);
        p = ptr;
        p->field_50 = v19;
        sub_f7d8d0(&p->field_50, v19);
        v21 = sub_1231bc8(ptr, g_1efcfd8);
        addr = ptr;
        addr->field_58 = v21;
        sub_f7d8d0(&addr->field_58, v21);
        v23 = sub_1231bc8(ptr, g_1efcfa0);
        ptr3 = ptr;
        ptr3->field_60 = v23;
        sub_f7d8d0(&ptr3->field_60, v23);
        v25 = sub_1231bc8(ptr, g_1efd0d8);
        ptr4 = ptr;
        ptr4->field_70 = v25;
        sub_f7d8d0(&ptr4->field_70, v25);
        if (ptr->field_200 && Transform__get_parent(ptr->field_200, 0) && Component__get_transform())
        {
            v27 = sub_1231bc8();
            ptr5 = ptr;
            ptr5->field_80 = v27;
            v29 = &ptr5->field_80;
            sub_f7d8d0(v29, v27);
            if (*((long long *)&v29->padding_e8[152]))
            {
                v30 = sub_1231bc8(*((long long *)&v29->padding_e8[152]), g_1efcf38);
                ptr6 = ptr;
                ptr6->field_98 = v30;
                v32 = &ptr6->field_98;
                sub_f7d8d0(v32, v30);
                if (*((long long *)&v32->padding_0[0]))
                {
                    v33 = *((long long *)(*((long long *)&v32->padding_0[0]) + 48));
                    ptr7 = ptr;
                    ptr7->field_c8 = v33;
                    v35 = &ptr7->field_c8;
                    sub_f7d8d0(v35, v33);
                    if (*((long long *)&v35->padding_0[0]))
                    {
                        v36 = sub_1249224(*((long long *)&v35->padding_0[0]), g_1efed20);
                        ptr8 = ptr;
                        ptr8->field_88 = v36;
                        v38 = &ptr8->field_88;
                        sub_f7d8d0(v38, v36);
                        if (*((long long *)&v38->padding_3c[4]))
                        {
                            v39 = sub_1249224(*((long long *)&v38->padding_3c[4]), g_1efec90);
                            ptr9 = ptr;
                            ptr9->field_68 = v39;
                            v41 = &ptr9->field_68;
                            sub_f7d8d0(v41, v39);
                            if (v41->field_70)
                            {
                                flag = 0;
                                GameObject__SetActive(v41->field_70, 1, 0);
                                if (ptr->field_d8)
                                {
                                    v43 = sub_1249224(ptr->field_d8, g_1efec80);
                                    ptr10 = ptr;
                                    ptr10->field_e0 = v43;
                                    ptr11 = &ptr10->field_e0;
                                    sub_f7d8d0(ptr11, v43);
                                    ptr12 = *((long long *)&ptr11->padding_0[0]);
                                    if (ptr12)
                                    {
                                        v47 = sub_1231bc8(ptr12, g_1efcfd0);
                                        ptr12->field_20 = v47;
                                        sub_f7d8d0(&ptr12->field_20, v47);
                                        if (*((long long *)&ptr11->padding_0[0]))
                                        {
                                            v48 = *((long long *)(*((long long *)&ptr11->padding_0[0]) + 32));
                                            if (v48)
                                            {
                                                v49 = *(v48)->field_2a0;
                                                *(v48)->field_298();
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
    }
LABEL_109db84:
    sub_f7db7c(sub_f7db74());
}
```

## `FPSPlayer.LateUpdate` — RVA `0xc9db8c`

- Decompiled symbol: `FPSPlayer_LateUpdate`
- Metadata signature: `private void LateUpdate() { }`
- Native interval: `628` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FPSPlayer_Recovered` matched 12 offsets against `FPSPlayer` metadata (confidence 0.80).

```c
typedef struct FPSPlayer_Recovered {
    char padding_0[48];
    struct struct_5 *imagebar;
    char padding_38[64];
    struct struct_2 *WeaponBehaviorComponent;
    struct struct_3 *MouseLookComponent;
    char padding_88[8];
    struct struct_4 *WeaponPivotComponent;
    char padding_98[232];
    struct struct_5 *crosshairUiRect;
    char padding_188[8];
    struct struct_5 *hitmarkerUiImage;
    struct struct_5 *hitmarkerUiRect;
    char padding_1a0[96];
    struct struct_5 *mainCamTransform;
    char padding_208[4];
    unsigned int hitPoints;
    char padding_210[332];
    unsigned int field_35c;
    unsigned int rayMask;
    char padding_364[92];
    unsigned int camCrosshairPos;
    unsigned int field_3c4;
    unsigned int field_3c8;
    char raycastCrosshair;
} FPSPlayer_Recovered;

typedef struct struct_1 {
    char padding_0[680];
    unsigned long long field_2a8;
} struct_1;

typedef struct struct_3 {
    char padding_0[168];
    char field_a8;
} struct_3;

typedef struct struct_2 {
    char padding_0[501];
    char field_1f5;
    char padding_1f6[514];
    unsigned int field_3f8;
    unsigned int field_3fc;
    unsigned int field_400;
} struct_2;

typedef struct struct_7 {
    char padding_0[680];
    unsigned long long field_2a8;
} struct_7;

typedef struct struct_4 {
    char padding_0[136];
    struct struct_5 *field_88;
} struct_4;

typedef struct struct_5 {
    struct struct_1 *field_0;
} struct_5;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0e48;
extern char g_1fab4ac;

void FPSPlayer_LateUpdate(struct_6 *ptr)
{
    unsigned long long v10;  // d13
    unsigned long long v11;  // d12
    struct_1 **v20;  // x0
    uint128_t v21;  // q0
    struct_2 *v22;  // x8
    struct_6 *v23;  // x20
    unsigned int v24;  // w0
    unsigned int v25;  // s1
    uint128_t v27;  // q2
    struct_7 **v28;  // x21
    struct_7 **v29;  // x0
    unsigned long long v12;  // d11
    struct_2 *p;  // x8
    struct_1 **v31;  // x20
    unsigned long long v13;  // d10
    unsigned long long v14;  // d9
    unsigned long long v15;  // d8
    unsigned long long v16;  // x30
    unsigned long long v17;  // x21
    unsigned long long v18;  // x20
    unsigned long long v19;  // x19
    unsigned long long v0;  // [bp-0x50]
    unsigned long long v1;  // [bp-0x48]
    unsigned long long v2;  // [bp-0x40]
    unsigned long long v3;  // [bp-0x38]
    unsigned long long v4;  // [bp-0x30]
    unsigned long long v5;  // [bp-0x28]
    unsigned long long v6;  // [bp-0x20]
    unsigned long long v7;  // [bp-0x18]
    unsigned long long v8;  // [bp-0x10]
    unsigned long long v9;  // [bp-0x8]

    v0 = v10;
    v1 = v11;
    v2 = v12;
    v3 = v13;
    v4 = v14;
    v5 = v15;
    v6 = v16;
    v7 = v17;
    v8 = v18;
    v9 = v19;
    if (!(g_1fab4ac & 1))
    {
        sub_f7d92c(&g_1ef0e48);
        g_1fab4ac = 1;
    }
    v20 = ptr->field_30;
    if (v20 && (v21 = (uint128_t)(ptr->field_20c / 0x42c80000), v20 = (struct_1 **)Image__set_fillAmount(v20, 0), ptr->field_80))
    {
        if (!ptr->field_80->field_a8 && !ptr->field_3cc)
        {
LABEL_109dcd4:
            v27 = 0;
            v21 = 0x3f000000;
            v25 = 0x3f000000;
            goto LABEL_109dd4c;
        }
        v22 = ptr->field_78;
        if (v22)
        {
            if (!v22->field_1f5)
            {
                v20 = ptr->field_200;
                if (v20 && (v20 = (struct_1 **)Transform__get_position(v20, 0), ptr->field_78))
                {
                    v23 = &ptr->padding_364[4];
                    v24 = LayerMask__op_Implicit(ptr->field_360, 0);
                    if (!g_1ef0e48->field_e0)
                        sub_f7da5c(g_1ef0e48);
                    v25 = 0x42c80000;
                    v20 = Physics__Raycast(v23, v24, 0);
                    if (((char)v20 & 1))
                    {
                        v28 = Camera__get_main(0);
                        v20 = RaycastHit__get_point(v23, 0);
                        if (v28)
                        {
                            v29 = v28;
LABEL_109dd44:
                            Camera__WorldToViewportPoint(v29, 0);
LABEL_109dd4c:
                            v20 = ptr->field_180;
                            ptr->field_3c0 = v21;
                            ptr->field_3c4 = v25;
                            ptr->field_3c8 = v27;
                            if (v20)
                            {
                                RectTransform__set_anchorMax(v20, 0);
                                v20 = ptr->field_180;
                                if (v20)
                                {
                                    RectTransform__set_anchorMin(v20, 0);
                                    v20 = ptr->field_198;
                                    if (v20)
                                    {
                                        RectTransform__set_anchorMax(v20, 0);
                                        v20 = ptr->field_198;
                                        if (v20)
                                        {
                                            RectTransform__set_anchorMin(v20, 0);
                                            v20 = ptr->field_190;
                                            ptr->field_35c = 1060320051;
                                            if (v20)
                                                goto *(v20)->field_2a8;
                                        }
                                    }
                                }
                            }
                        }
                    }
                    else
                    {
                        v22 = ptr->field_78;
                        if (v22)
                            goto LABEL_109dccc;
                    }
                }
            }
            else
            {
LABEL_109dccc:
                if (v22->field_1f5)
                    goto LABEL_109dcd4;
                v20 = Camera__get_main(0);
                p = ptr->field_78;
                if (p && ptr->field_90 && (v31 = v20, v20 = (struct_1 **)ptr->field_90->field_88, v20 && (v20 = (struct_1 **)Transform__get_forward(v20, 0), v31)))
                {
                    v27 = p->field_400 + (unsigned int)v27 * 0x43480000;
                    v25 = p->field_3fc;
                    v21 = p->field_3f8 + (unsigned int)v21 * 0x43480000;
                    v29 = v31;
                    goto LABEL_109dd44;
                }
            }
        }
    }
    sub_f7db74(v20);
}
```

## `FPSPlayer.Update` — RVA `0xc9de00`

- Decompiled symbol: `FPSPlayer_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `5976` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[64];
    struct struct_3 *field_40;
} struct_2;

typedef struct struct_0 {
    char padding_0[1512];
    struct struct_1 *field_5e8;
    unsigned long long field_5f0;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1ef0c58;
extern long long g_1ef0e48;
extern long long g_1efeb10;
extern long long g_1efeb18;
extern long long g_1efebe0;
extern long long g_1efec38;
extern long long g_1efed18;
extern long long g_1efed28;
extern long long g_1f08390;
extern long long g_1f09ab0;
extern long long g_1f0bd20;
extern long long g_1f0cf38;
extern char g_1fab4ad;

void FPSPlayer_Update(struct_2 *ptr)
{
    unsigned long long v14;  // d15
    unsigned long long v15;  // d14
    unsigned long long v24;  // x22
    unsigned long long v25;  // x21
    unsigned long long v26;  // x20
    unsigned long long v27;  // x19
    struct_0 **v28;  // x20
    unsigned long v29;  // x0
    unsigned long v30;  // x1
    struct_0 **v31;  // x0
    unsigned long long v32;  // x2
    unsigned long long v16;  // d13
    unsigned long long v17;  // d12
    unsigned long long v18;  // d11
    unsigned long long v19;  // d10
    unsigned long long v20;  // d9
    unsigned long long v21;  // d8
    unsigned long long v22;  // x30
    unsigned long long v23;  // x23
    unsigned long long v0;  // [bp-0x70]
    unsigned long long v1;  // [bp-0x68]
    unsigned long long v2;  // [bp-0x60]
    unsigned long long v3;  // [bp-0x58]
    unsigned long long v4;  // [bp-0x50]
    unsigned long long v5;  // [bp-0x48]
    unsigned long long v6;  // [bp-0x40]
    unsigned long long v7;  // [bp-0x38]
    unsigned long long v8;  // [bp-0x30]
    unsigned long long v9;  // [bp-0x28]
    unsigned long long v10;  // [bp-0x20]
    unsigned long long v11;  // [bp-0x18]
    unsigned long long v12;  // [bp-0x10]
    unsigned long long v13;  // [bp-0x8]

    v0 = v14;
    v1 = v15;
    v2 = v16;
    v3 = v17;
    v4 = v18;
    v5 = v19;
    v6 = v20;
    v7 = v21;
    v8 = v22;
    v9 = v23;
    v10 = v24;
    v11 = v25;
    v12 = v26;
    v13 = v27;
    if (!(g_1fab4ad & 1))
    {
        sub_f7d92c(&g_1efeb10);
        sub_f7d92c(&g_1efeb18);
        sub_f7d92c(&g_1efebe0);
        sub_f7d92c(&g_1efec38);
        sub_f7d92c(&g_1efed18);
        sub_f7d92c(&g_1efed28);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef0e48);
        sub_f7d92c(&g_1f09ab0);
        sub_f7d92c(&g_1f08390);
        sub_f7d92c("s%");
        sub_f7d92c(&g_1f0cf38);
        sub_f7d92c(&g_1f0bd20);
        g_1fab4ad = 1;
    }
    v28 = ptr->field_40;
    v29 = Int32__ToString((struct struct_2 *)&ptr->padding_0[56], 0);
    if (!v28)
        sub_f7db7c(sub_f7db74());
    v30 = v29;
    v31 = v28;
    v32 = *(v28)->field_5f0;
    *(v28)->field_5e8();
}
```

## `FPSPlayer.HealPlayer` — RVA `0xc9f558`

- Decompiled symbol: `FPSPlayer_HealPlayer`
- Metadata signature: `public void HealPlayer(float healAmt, bool isHungryThirsty = false) { }`
- Native interval: `608` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x109f558: sub sp, sp, #0x30
// 0x109f55c: str d8, [sp, #0x10]
// 0x109f560: str x30, [sp, #0x18]
// 0x109f564: stp x20, x19, [sp, #0x20]
// 0x109f568: ldr s1, [x0, #0x20c]
// 0x109f56c: fcmp s1, #0.0
// 0x109f570: b.ls #0x109f590
// 0x109f574: ldr s8, [x0, #0x210]
// 0x109f578: fadd s1, s1, s0
// 0x109f57c: mov x19, x0
// 0x109f580: fcmp s1, s8
// 0x109f584: b.le #0x109f5a4
// 0x109f588: str s8, [x19, #0x20c]
// 0x109f58c: b #0x109f5d0
// 0x109f590: ldp x20, x19, [sp, #0x20]
// 0x109f594: ldr x30, [sp, #0x18]
// 0x109f598: ldr d8, [sp, #0x10]
// 0x109f59c: add sp, sp, #0x30
// 0x109f5a0: ret
// 0x109f5a4: fcmp s0, #0.0
// 0x109f5a8: b.pl #0x109f5b0
// 0x109f5ac: tbz w1, #0, #0x109f5bc
// 0x109f5b0: mov v8.16b, v1.16b
// 0x109f5b4: str s1, [x19, #0x20c]
// 0x109f5b8: b #0x109f5d0
// 0x109f5bc: mov x0, x19
// 0x109f5c0: mov x1, xzr
// 0x109f5c4: mov w2, wzr
// 0x109f5c8: bl #0x109fed8
// 0x109f5cc: ldr s8, [x19, #0x20c]
// 0x109f5d0: ldr x20, [x19, #0x1a0]
// 0x109f5d4: fcvt d0, s8
// 0x109f5d8: add x0, sp, #8
// 0x109f5dc: bl #0x1db0c60
// 0x109f5e0: fcmp s8, #0.0
// 0x109f5e4: b.ge #0x109f600
// 0x109f5e8: fmov d1, #-0.50000000
// 0x109f5ec: fcmp d0, d1
// 0x109f5f0: b.ne #0x109f62c
// 0x109f5f4: ldr d0, [sp, #8]
// 0x109f5f8: fmov s1, #-1.00000000
// 0x109f5fc: b #0x109f614
// 0x109f600: fmov d1, #0.50000000
// 0x109f604: fcmp d0, d1
// 0x109f608: b.ne #0x109f63c
// 0x109f60c: ldr d0, [sp, #8]
// 0x109f610: fmov s1, #1.00000000
// 0x109f614: fcvtzs x8, d0
// 0x109f618: fcvt s0, d0
// 0x109f61c: fadd s1, s0, s1
// 0x109f620: tst x8, #1
// 0x109f624: fcsel s0, s0, s1, eq
// 0x109f628: b #0x109f648
// 0x109f62c: fmov s0, #-0.50000000
// 0x109f630: fadd s0, s8, s0
// 0x109f634: frintp s0, s0
// 0x109f638: b #0x109f648
// 0x109f63c: fmov s0, #0.50000000
// 0x109f640: fadd s0, s8, s0
// 0x109f644: frintm s0, s0
// 0x109f648: cbz x20, #0x109f7b4
// 0x109f64c: str s0, [x20, #0x20]
// 0x109f650: ldr s8, [x19, #0x20c]
// 0x109f654: ldr x20, [x19, #0x1a8]
// 0x109f658: add x0, sp, #8
// 0x109f65c: fcvt d0, s8
// 0x109f660: bl #0x1db0c60
// 0x109f664: fcmp s8, #0.0
// 0x109f668: b.ge #0x109f684
// 0x109f66c: fmov d1, #-0.50000000
// 0x109f670: fcmp d0, d1
// 0x109f674: b.ne #0x109f6b0
// 0x109f678: ldr d0, [sp, #8]
// 0x109f67c: fmov s1, #-1.00000000
// 0x109f680: b #0x109f698
// 0x109f684: fmov d1, #0.50000000
// 0x109f688: fcmp d0, d1
// 0x109f68c: b.ne #0x109f6c0
// 0x109f690: ldr d0, [sp, #8]
// 0x109f694: fmov s1, #1.00000000
// 0x109f698: fcvtzs x8, d0
// 0x109f69c: fcvt s0, d0
// 0x109f6a0: fadd s1, s0, s1
// 0x109f6a4: tst x8, #1
// 0x109f6a8: fcsel s0, s0, s1, eq
// 0x109f6ac: b #0x109f6cc
// 0x109f6b0: fmov s0, #-0.50000000
// 0x109f6b4: fadd s0, s8, s0
// 0x109f6b8: frintp s0, s0
// 0x109f6bc: b #0x109f6cc
// 0x109f6c0: fmov s0, #0.50000000
// 0x109f6c4: fadd s0, s8, s0
// 0x109f6c8: frintm s0, s0
// 0x109f6cc: cbz x20, #0x109f7b4
// 0x109f6d0: str s0, [x20, #0x20]
// 0x109f6d4: ldr s0, [x19, #0x20c]
// 0x109f6d8: fmov s1, #25.00000000
// 0x109f6dc: fcmp s0, s1
// 0x109f6e0: b.ls #0x109f72c
// 0x109f6e4: ldr x0, [x19, #0x1b0]
// 0x109f6e8: mov w8, #0x42200000
// 0x109f6ec: fmov s1, w8
// 0x109f6f0: fcmp s0, s1
// 0x109f6f4: b.ls #0x109f778
// 0x109f6f8: ldr x8, [x19, #0x1a0]
// 0x109f6fc: cbz x8, #0x109f7b4
// 0x109f700: cbz x0, #0x109f7b4
// 0x109f704: ldr x9, [x0]
// 0x109f708: ldp s2, s3, [x8, #0x30]
// 0x109f70c: ldp s0, s1, [x8, #0x28]
// 0x109f710: ldr x8, [x9, #0x2a8]
// 0x109f714: ldr x1, [x9, #0x2b0]
// 0x109f718: blr x8
// 0x109f71c: ldr x0, [x19, #0x28]
// 0x109f720: cbz x0, #0x109f7b4
// 0x109f724: mov w1, wzr
// 0x109f728: b #0x109f760
// 0x109f72c: ldr x0, [x19, #0x1b0]
// 0x109f730: cbz x0, #0x109f7b4
// 0x109f734: ldr x8, [x0]
// 0x109f738: fmov s0, #1.00000000
// 0x109f73c: fmov s1, wzr
// 0x109f740: fmov s2, wzr
// 0x109f744: ldr x9, [x8, #0x2a8]
// 0x109f748: ldr x1, [x8, #0x2b0]
// 0x109f74c: fmov s3, #1.00000000
// 0x109f750: blr x9
// 0x109f754: ldr x0, [x19, #0x28]
// 0x109f758: cbz x0, #0x109f7b4
// 0x109f75c: mov w1, #1
// 0x109f760: ldp x20, x19, [sp, #0x20]
// 0x109f764: ldr x30, [sp, #0x18]
// 0x109f768: ldr d8, [sp, #0x10]
// 0x109f76c: mov x2, xzr
// 0x109f770: add sp, sp, #0x30
// 0x109f774: b #0x1b94cd0
// 0x109f778: cbz x0, #0x109f7b4
// 0x109f77c: ldr x8, [x0]
// 0x109f780: adrp x9, #0x832000
// 0x109f784: adrp x10, #0x832000
// 0x109f788: ldr s1, [x9, #0x320]
// 0x109f78c: ldr x2, [x8, #0x2a8]
// 0x109f790: ldr x1, [x8, #0x2b0]
// 0x109f794: ldr s2, [x10, #0x37c]
// 0x109f798: ldp x20, x19, [sp, #0x20]
// 0x109f79c: ldr x30, [sp, #0x18]
// 0x109f7a0: ldr d8, [sp, #0x10]
// 0x109f7a4: fmov s0, #1.00000000
// 0x109f7a8: fmov s3, #1.00000000
// 0x109f7ac: add sp, sp, #0x30
// 0x109f7b0: br x2
// 0x109f7b4: bl #0xf7db74
```

## `FPSPlayer.UpdateHunger` — RVA `0xc9f7b8`

- Decompiled symbol: `FPSPlayer_UpdateHunger`
- Metadata signature: `public void UpdateHunger(float hungerAmt) { }`
- Native interval: `520` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x109f7b8: sub sp, sp, #0x30
// 0x109f7bc: str d8, [sp, #0x10]
// 0x109f7c0: str x30, [sp, #0x18]
// 0x109f7c4: stp x20, x19, [sp, #0x20]
// 0x109f7c8: ldr s1, [x0, #0x20c]
// 0x109f7cc: fcmp s1, #0.0
// 0x109f7d0: b.ls #0x109f9a8
// 0x109f7d4: ldr s1, [x0, #0x238]
// 0x109f7d8: ldr s2, [x0, #0x230]
// 0x109f7dc: fmov s3, wzr
// 0x109f7e0: ldr x20, [x0, #0x1b8]
// 0x109f7e4: fadd s0, s1, s0
// 0x109f7e8: fcmp s0, s2
// 0x109f7ec: fcsel s0, s2, s0, gt
// 0x109f7f0: fmax s8, s0, s3
// 0x109f7f4: mov x19, x0
// 0x109f7f8: str s8, [x0, #0x238]
// 0x109f7fc: fcvt d0, s8
// 0x109f800: add x0, sp, #8
// 0x109f804: bl #0x1db0c60
// 0x109f808: fcmp s8, #0.0
// 0x109f80c: b.ge #0x109f828
// 0x109f810: fmov d1, #-0.50000000
// 0x109f814: fcmp d0, d1
// 0x109f818: b.ne #0x109f854
// 0x109f81c: ldr d0, [sp, #8]
// 0x109f820: fmov s1, #-1.00000000
// 0x109f824: b #0x109f83c
// 0x109f828: fmov d1, #0.50000000
// 0x109f82c: fcmp d0, d1
// 0x109f830: b.ne #0x109f864
// 0x109f834: ldr d0, [sp, #8]
// 0x109f838: fmov s1, #1.00000000
// 0x109f83c: fcvtzs x8, d0
// 0x109f840: fcvt s0, d0
// 0x109f844: fadd s1, s0, s1
// 0x109f848: tst x8, #1
// 0x109f84c: fcsel s0, s0, s1, eq
// 0x109f850: b #0x109f870
// 0x109f854: fmov s0, #-0.50000000
// 0x109f858: fadd s0, s8, s0
// 0x109f85c: frintp s0, s0
// 0x109f860: b #0x109f870
// 0x109f864: fmov s0, #0.50000000
// 0x109f868: fadd s0, s8, s0
// 0x109f86c: frintm s0, s0
// 0x109f870: cbz x20, #0x109f9bc
// 0x109f874: str s0, [x20, #0x20]
// 0x109f878: ldr s8, [x19, #0x238]
// 0x109f87c: ldr x20, [x19, #0x1c0]
// 0x109f880: add x0, sp, #8
// 0x109f884: fcvt d0, s8
// 0x109f888: bl #0x1db0c60
// 0x109f88c: fcmp s8, #0.0
// 0x109f890: b.ge #0x109f8ac
// 0x109f894: fmov d1, #-0.50000000
// 0x109f898: fcmp d0, d1
// 0x109f89c: b.ne #0x109f8d8
// 0x109f8a0: ldr d0, [sp, #8]
// 0x109f8a4: fmov s1, #-1.00000000
// 0x109f8a8: b #0x109f8c0
// 0x109f8ac: fmov d1, #0.50000000
// 0x109f8b0: fcmp d0, d1
// 0x109f8b4: b.ne #0x109f8e8
// 0x109f8b8: ldr d0, [sp, #8]
// 0x109f8bc: fmov s1, #1.00000000
// 0x109f8c0: fcvtzs x8, d0
// 0x109f8c4: fcvt s0, d0
// 0x109f8c8: fadd s1, s0, s1
// 0x109f8cc: tst x8, #1
// 0x109f8d0: fcsel s0, s0, s1, eq
// 0x109f8d4: b #0x109f8f4
// 0x109f8d8: fmov s0, #-0.50000000
// 0x109f8dc: fadd s0, s8, s0
// 0x109f8e0: frintp s0, s0
// 0x109f8e4: b #0x109f8f4
// 0x109f8e8: fmov s0, #0.50000000
// 0x109f8ec: fadd s0, s8, s0
// 0x109f8f0: frintm s0, s0
// 0x109f8f4: cbz x20, #0x109f9bc
// 0x109f8f8: str s0, [x20, #0x20]
// 0x109f8fc: ldr s0, [x19, #0x238]
// 0x109f900: mov w8, #0x42820000
// 0x109f904: fmov s1, w8
// 0x109f908: fcmp s0, s1
// 0x109f90c: b.ls #0x109f944
// 0x109f910: ldr x0, [x19, #0x1c8]
// 0x109f914: mov w8, #0x42aa0000
// 0x109f918: fmov s1, w8
// 0x109f91c: fcmp s0, s1
// 0x109f920: b.ls #0x109f970
// 0x109f924: cbz x0, #0x109f9bc
// 0x109f928: ldr x8, [x0]
// 0x109f92c: fmov s0, #1.00000000
// 0x109f930: fmov s1, wzr
// 0x109f934: fmov s2, wzr
// 0x109f938: ldr x9, [x8, #0x2a8]
// 0x109f93c: ldr x1, [x8, #0x2b0]
// 0x109f940: b #0x109f994
// 0x109f944: ldr x8, [x19, #0x1b8]
// 0x109f948: cbz x8, #0x109f9bc
// 0x109f94c: ldr x0, [x19, #0x1c8]
// 0x109f950: cbz x0, #0x109f9bc
// 0x109f954: ldr x9, [x0]
// 0x109f958: ldp s2, s3, [x8, #0x30]
// 0x109f95c: ldp s0, s1, [x8, #0x28]
// 0x109f960: ldr x8, [x9, #0x2a8]
// 0x109f964: ldr x1, [x9, #0x2b0]
// 0x109f968: blr x8
// 0x109f96c: b #0x109f99c
// 0x109f970: cbz x0, #0x109f9bc
// 0x109f974: ldr x8, [x0]
// 0x109f978: adrp x10, #0x832000
// 0x109f97c: ldr s2, [x10, #0x37c]
// 0x109f980: fmov s0, #1.00000000
// 0x109f984: ldr x9, [x8, #0x2a8]
// 0x109f988: ldr x1, [x8, #0x2b0]
// 0x109f98c: adrp x8, #0x832000
// 0x109f990: ldr s1, [x8, #0x320]
// 0x109f994: fmov s3, #1.00000000
// 0x109f998: blr x9
// 0x109f99c: mov x0, xzr
// 0x109f9a0: bl #0x1b9ad30
// 0x109f9a4: str s0, [x19, #0x23c]
// 0x109f9a8: ldp x20, x19, [sp, #0x20]
// 0x109f9ac: ldr x30, [sp, #0x18]
// 0x109f9b0: ldr d8, [sp, #0x10]
// 0x109f9b4: add sp, sp, #0x30
// 0x109f9b8: ret
// 0x109f9bc: bl #0xf7db74
```

## `FPSPlayer.UpdateThirst` — RVA `0xc9f9c0`

- Decompiled symbol: `FPSPlayer_UpdateThirst`
- Metadata signature: `public void UpdateThirst(float thirstAmt) { }`
- Native interval: `520` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x109f9c0: sub sp, sp, #0x30
// 0x109f9c4: str d8, [sp, #0x10]
// 0x109f9c8: str x30, [sp, #0x18]
// 0x109f9cc: stp x20, x19, [sp, #0x20]
// 0x109f9d0: ldr s1, [x0, #0x20c]
// 0x109f9d4: fcmp s1, #0.0
// 0x109f9d8: b.ls #0x109fbb0
// 0x109f9dc: ldr s1, [x0, #0x258]
// 0x109f9e0: ldr s2, [x0, #0x250]
// 0x109f9e4: fmov s3, wzr
// 0x109f9e8: ldr x20, [x0, #0x1d0]
// 0x109f9ec: fadd s0, s1, s0
// 0x109f9f0: fcmp s0, s2
// 0x109f9f4: fcsel s0, s2, s0, gt
// 0x109f9f8: fmax s8, s0, s3
// 0x109f9fc: mov x19, x0
// 0x109fa00: str s8, [x0, #0x258]
// 0x109fa04: fcvt d0, s8
// 0x109fa08: add x0, sp, #8
// 0x109fa0c: bl #0x1db0c60
// 0x109fa10: fcmp s8, #0.0
// 0x109fa14: b.ge #0x109fa30
// 0x109fa18: fmov d1, #-0.50000000
// 0x109fa1c: fcmp d0, d1
// 0x109fa20: b.ne #0x109fa5c
// 0x109fa24: ldr d0, [sp, #8]
// 0x109fa28: fmov s1, #-1.00000000
// 0x109fa2c: b #0x109fa44
// 0x109fa30: fmov d1, #0.50000000
// 0x109fa34: fcmp d0, d1
// 0x109fa38: b.ne #0x109fa6c
// 0x109fa3c: ldr d0, [sp, #8]
// 0x109fa40: fmov s1, #1.00000000
// 0x109fa44: fcvtzs x8, d0
// 0x109fa48: fcvt s0, d0
// 0x109fa4c: fadd s1, s0, s1
// 0x109fa50: tst x8, #1
// 0x109fa54: fcsel s0, s0, s1, eq
// 0x109fa58: b #0x109fa78
// 0x109fa5c: fmov s0, #-0.50000000
// 0x109fa60: fadd s0, s8, s0
// 0x109fa64: frintp s0, s0
// 0x109fa68: b #0x109fa78
// 0x109fa6c: fmov s0, #0.50000000
// 0x109fa70: fadd s0, s8, s0
// 0x109fa74: frintm s0, s0
// 0x109fa78: cbz x20, #0x109fbc4
// 0x109fa7c: str s0, [x20, #0x20]
// 0x109fa80: ldr s8, [x19, #0x258]
// 0x109fa84: ldr x20, [x19, #0x1d8]
// 0x109fa88: add x0, sp, #8
// 0x109fa8c: fcvt d0, s8
// 0x109fa90: bl #0x1db0c60
// 0x109fa94: fcmp s8, #0.0
// 0x109fa98: b.ge #0x109fab4
// 0x109fa9c: fmov d1, #-0.50000000
// 0x109faa0: fcmp d0, d1
// 0x109faa4: b.ne #0x109fae0
// 0x109faa8: ldr d0, [sp, #8]
// 0x109faac: fmov s1, #-1.00000000
// 0x109fab0: b #0x109fac8
// 0x109fab4: fmov d1, #0.50000000
// 0x109fab8: fcmp d0, d1
// 0x109fabc: b.ne #0x109faf0
// 0x109fac0: ldr d0, [sp, #8]
// 0x109fac4: fmov s1, #1.00000000
// 0x109fac8: fcvtzs x8, d0
// 0x109facc: fcvt s0, d0
// 0x109fad0: fadd s1, s0, s1
// 0x109fad4: tst x8, #1
// 0x109fad8: fcsel s0, s0, s1, eq
// 0x109fadc: b #0x109fafc
// 0x109fae0: fmov s0, #-0.50000000
// 0x109fae4: fadd s0, s8, s0
// 0x109fae8: frintp s0, s0
// 0x109faec: b #0x109fafc
// 0x109faf0: fmov s0, #0.50000000
// 0x109faf4: fadd s0, s8, s0
// 0x109faf8: frintm s0, s0
// 0x109fafc: cbz x20, #0x109fbc4
// 0x109fb00: str s0, [x20, #0x20]
// 0x109fb04: ldr s0, [x19, #0x258]
// 0x109fb08: mov w8, #0x42820000
// 0x109fb0c: fmov s1, w8
// 0x109fb10: fcmp s0, s1
// 0x109fb14: b.ls #0x109fb4c
// 0x109fb18: ldr x0, [x19, #0x1e0]
// 0x109fb1c: mov w8, #0x42aa0000
// 0x109fb20: fmov s1, w8
// 0x109fb24: fcmp s0, s1
// 0x109fb28: b.ls #0x109fb78
// 0x109fb2c: cbz x0, #0x109fbc4
// 0x109fb30: ldr x8, [x0]
// 0x109fb34: fmov s0, #1.00000000
// 0x109fb38: fmov s1, wzr
// 0x109fb3c: fmov s2, wzr
// 0x109fb40: ldr x9, [x8, #0x2a8]
// 0x109fb44: ldr x1, [x8, #0x2b0]
// 0x109fb48: b #0x109fb9c
// 0x109fb4c: ldr x8, [x19, #0x1d0]
// 0x109fb50: cbz x8, #0x109fbc4
// 0x109fb54: ldr x0, [x19, #0x1e0]
// 0x109fb58: cbz x0, #0x109fbc4
// 0x109fb5c: ldr x9, [x0]
// 0x109fb60: ldp s2, s3, [x8, #0x30]
// 0x109fb64: ldp s0, s1, [x8, #0x28]
// 0x109fb68: ldr x8, [x9, #0x2a8]
// 0x109fb6c: ldr x1, [x9, #0x2b0]
// 0x109fb70: blr x8
// 0x109fb74: b #0x109fba4
// 0x109fb78: cbz x0, #0x109fbc4
// 0x109fb7c: ldr x8, [x0]
// 0x109fb80: adrp x10, #0x832000
// 0x109fb84: ldr s2, [x10, #0x37c]
// 0x109fb88: fmov s0, #1.00000000
// 0x109fb8c: ldr x9, [x8, #0x2a8]
// 0x109fb90: ldr x1, [x8, #0x2b0]
// 0x109fb94: adrp x8, #0x832000
// 0x109fb98: ldr s1, [x8, #0x320]
// 0x109fb9c: fmov s3, #1.00000000
// 0x109fba0: blr x9
// 0x109fba4: mov x0, xzr
// 0x109fba8: bl #0x1b9ad30
// 0x109fbac: str s0, [x19, #0x25c]
// 0x109fbb0: ldp x20, x19, [sp, #0x20]
// 0x109fbb4: ldr x30, [sp, #0x18]
// 0x109fbb8: ldr d8, [sp, #0x10]
// 0x109fbbc: add sp, sp, #0x30
// 0x109fbc0: ret
// 0x109fbc4: bl #0xf7db74
```

## `FPSPlayer.Die` — RVA `0xc9fbc8`

- Decompiled symbol: `FPSPlayer_Die`
- Metadata signature: `private void Die() { }`
- Native interval: `196` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FPSPlayer_Recovered` matched 4 offsets against `FPSPlayer` metadata (confidence 1.00).

```c
typedef struct FPSPlayer_Recovered {
    char padding_0[96];
    struct struct_0 *FPSWalkerComponent;
    char padding_68[144];
    long long levelLoadFadeRef;
    char padding_100[420];
    char bulletTimeActive;
    char padding_2a5[419];
    long long otherfx;
} FPSPlayer_Recovered;

typedef struct struct_0 {
    char padding_0[192];
    unsigned long long field_c0;
    char padding_c8[416];
    char field_268;
    char padding_269[89];
    char field_2c2;
} struct_0;

void FPSPlayer_Die(struct_1 *ptr)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_0 *v6;  // x8
    long long v7;  // x20
    struct_0 *p;  // x8
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    v6 = ptr->field_60;
    ptr->field_2a4 = 0;
    if (v6)
    {
        if (v6->field_268)
        {
            if (ptr->field_448)
                goto LABEL_109fc00;
        }
        else
        {
            if (ptr->field_448)
            {
LABEL_109fc00:
                AudioSource__set_clip();
                v7 = ptr->field_448;
                if (v7)
                {
                    AudioSource__PlayOneShot(v7, AudioSource__get_clip(v7, 0), 0);
                    p = ptr->field_60;
                    if (p)
                    {
                        p->field_c0 = 0;
                        p->field_2c2 = 1;
                        if (ptr->field_f8)
                        {
                            MonoBehaviour__StopAllCoroutines(ptr->field_f8, 0);
                            if (ptr->field_f8)
                            {
                                LevelLoadFade__FadeAndLoadLevel();
                                return;
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

## `FPSPlayer.UpdateHitmarker` — RVA `0xc9fc8c`

- Decompiled symbol: `FPSPlayer_UpdateHitmarker`
- Metadata signature: `private void UpdateHitmarker() { }`
- Native interval: `236` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FPSPlayer_Recovered` matched 6 offsets against `FPSPlayer` metadata (confidence 1.00).

```c
typedef struct FPSPlayer_Recovered {
    char padding_0[120];
    struct struct_0 *WeaponBehaviorComponent;
    char padding_80[272];
    char hitmarkerUiImage;
    char padding_191[99];
    unsigned int hitTime;
    char hitMarkerState;
    char padding_1f9[551];
    long long hitMarker;
    char padding_428[40];
    char hitmarkfx;
} FPSPlayer_Recovered;

typedef struct struct_0 {
    char padding_0[516];
    unsigned int field_204;
    char padding_208[33];
    char field_229;
} struct_0;

long long FPSPlayer_UpdateHitmarker(struct_1 *ptr, unsigned long a1)
{
    unsigned long v0;  // x0
    unsigned int v1;  // w8
    unsigned long long v10;  // x0
    unsigned int v2;  // s1
    unsigned int v3;  // s0
    unsigned long v4;  // 4148
    struct_0 *p;  // x8
    unsigned int v6;  // s0
    unsigned long long v7;  // 4103
    unsigned long v8;  // x20
    unsigned long v9;  // x0

    v0 = Time__get_time(0);
    v1 = ptr->field_1f8;
    v2 = ptr->field_1f4 + 1050253722;
    v4 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v2, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v3) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v3) & 1)) & ((unsigned long long)(char)(CmpF(v2, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v3) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v4)
    {
        if (v1)
            ptr->field_1f8 = 0;
        v0 = *((long long *)&ptr->field_190);
        if (*((long long *)&ptr->field_190))
        {
            v10 = Behaviour__set_enabled();
            return Behaviour__set_enabled();
        }
    }
    else if (v1)
    {
        return v0;
    }
    else
    {
        p = ptr->field_78;
        if (p)
        {
            v6 = p->field_204;
            v7 = (((CmpF(v6, 0.0) >> 5 & 3 | CmpF(v6, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v6, 0.0) >> 5 & 3 | CmpF(v6, 0.0) & 1) & (CmpF(v6, 0.0) >> 5 & 3 | CmpF(v6, 0.0) & 1) >> 1 & 1);
            if (!((char)(v7 * 0x10000000 >> 30)))
            {
                return v0;
            }
            else if (p->field_229)
            {
                return v0;
            }
            else
            {
                v0 = *((long long *)&ptr->field_190);
                if (v0)
                {
                    Behaviour__set_enabled(v0, 1, 0);
                    v0 = *((long long *)&ptr->field_450);
                    if (v0)
                    {
                        v0 = AudioSource__set_clip(v0, ptr->field_420, 0);
                        v8 = *((long long *)&ptr->field_450);
                        if (v8)
                        {
                            v9 = AudioSource__PlayOneShot(v8, AudioSource__get_clip(v8, 0), 0);
                            ptr->field_1f8 = 1;
                            return v9;
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v0);
}
```

## `FPSPlayer.UpdateReticle` — RVA `0xc9fd78`

- Decompiled symbol: `FPSPlayer_UpdateReticle`
- Metadata signature: `public void UpdateReticle(bool reticleType) { }`
- Native interval: `156` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FPSPlayer_Recovered` matched 2 offsets against `FPSPlayer` metadata (confidence 1.00).

```c
typedef struct struct_2 {
    char padding_0[376];
    struct struct_3 *field_178;
} struct_2;

typedef struct FPSPlayer_Recovered {
    char padding_0[680];
    struct struct_1 *backstabBtTime;
    unsigned long long initialFixedTime;
} FPSPlayer_Recovered;

typedef struct struct_3 {
    struct FPSPlayer_Recovered *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void FPSPlayer_UpdateReticle(struct_2 *ptr, unsigned long a1)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long choice;  // x2
    struct_0 **v5;  // x0
    unsigned long long v6;  // x1
    unsigned long long flag;  // x2
    struct_0 **v8;  // x0
    unsigned long long v9;  // x1
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    if (((char)a1 & 1))
    {
        if (ptr->field_178)
        {
            choice = 0;
            Image__set_sprite();
            v5 = ptr->field_178;
            if (v5)
            {
                v6 = *(v5)->field_2b0;
                *(v5)->field_2a8();
            }
        }
    }
    else
    {
        if (ptr->field_178)
        {
            flag = 0;
            Image__set_sprite();
            v8 = ptr->field_178;
            if (v8)
            {
                v9 = *(v8)->field_2b0;
                *(v8)->field_2a8();
            }
        }
    }
    sub_f7db74();
}
```

## `FPSPlayer.UpdateHitTime` — RVA `0xc9fe14`

- Decompiled symbol: `FPSPlayer_UpdateHitTime`
- Metadata signature: `public void UpdateHitTime() { }`
- Native interval: `32` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FPSPlayer_Recovered` matched 2 offsets against `FPSPlayer` metadata (confidence 1.00).

```c
typedef struct FPSPlayer_Recovered {
    char padding_0[500];
    unsigned int hitTime;
    char hitMarkerState;
} FPSPlayer_Recovered;

int FPSPlayer_UpdateHitTime(struct_0 *ptr)
{
    unsigned int v0;  // w0
    unsigned int v1;  // s0

    v0 = Time__get_time(0);
    ptr->field_1f4 = v1;
    ptr->field_1f8 = 0;
    return v0;
}
```

## `FPSPlayer.ActivateBulletTime` — RVA `0xc9fe34`

- Decompiled symbol: `FPSPlayer_ActivateBulletTime`
- Metadata signature: `public IEnumerator ActivateBulletTime(float duration) { }`
- Native interval: `124` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FPSPlayer_Recovered` matched 2 offsets against `FPSPlayer` metadata (confidence 0.67).

```c
typedef struct FPSPlayer_Recovered {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long MissionFailedPanel;
    unsigned int healthButton;
} FPSPlayer_Recovered;

extern long long g_1ef30e0;
extern char g_1fab4ae;

struct_0 * FPSPlayer_ActivateBulletTime(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0
    unsigned int v2;  // s0

    if (!(g_1fab4ae & 1))
    {
        sub_f7d92c(&g_1ef30e0);
        g_1fab4ae = 1;
    }
    v0 = sub_f7db70(g_1ef30e0);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    ptr->field_28 = v2;
    return ptr;
}
```

## `FPSPlayer.<ActivateBulletTime>d__175.ctor` — RVA `0xc9feb0`

- Decompiled symbol: `FPSPlayer_ActivateBulletTime_d__175_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void FPSPlayer_ActivateBulletTime_d__175_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `FPSPlayer.ApplyDamage` — RVA `0xc9fed8`

- Decompiled symbol: `FPSPlayer_ApplyDamage`
- Metadata signature: `public void ApplyDamage(float damage, Transform attacker, bool isMeleeAttack = false) { }`
- Native interval: `3884` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x109fed8: sub sp, sp, #0x110
// 0x109fedc: stp d15, d14, [sp, #0x70]
// 0x109fee0: stp d13, d12, [sp, #0x80]
// 0x109fee4: stp d11, d10, [sp, #0x90]
// 0x109fee8: stp d9, d8, [sp, #0xa0]
// 0x109feec: stp x29, x30, [sp, #0xb0]
// 0x109fef0: stp x28, x27, [sp, #0xc0]
// 0x109fef4: stp x26, x25, [sp, #0xd0]
// 0x109fef8: stp x24, x23, [sp, #0xe0]
// 0x109fefc: stp x22, x21, [sp, #0xf0]
// 0x109ff00: stp x20, x19, [sp, #0x100]
// 0x109ff04: adrp x22, #0x1fab000
// 0x109ff08: ldrb w8, [x22, #0x4b0]
// 0x109ff0c: mov w21, w2
// 0x109ff10: mov x20, x1
// 0x109ff14: mov v8.16b, v0.16b
// 0x109ff18: mov x19, x0
// 0x109ff1c: tbnz w8, #0, #0x109ff88
// 0x109ff20: adrp x0, #0x1e8e000
// 0x109ff24: ldr x0, [x0, #0xa8]
// 0x109ff28: bl #0xf7d92c
// 0x109ff2c: adrp x0, #0x1e8d000
// 0x109ff30: ldr x0, [x0, #0x230]
// 0x109ff34: bl #0xf7d92c
// 0x109ff38: adrp x0, #0x1e8d000
// 0x109ff3c: ldr x0, [x0, #0xe18]
// 0x109ff40: bl #0xf7d92c
// 0x109ff44: adrp x0, #0x1e8c000
// 0x109ff48: ldr x0, [x0, #0xec8]
// 0x109ff4c: bl #0xf7d92c
// 0x109ff50: adrp x0, #0x1e8c000
// 0x109ff54: ldr x0, [x0, #0xed0]
// 0x109ff58: bl #0xf7d92c
// 0x109ff5c: adrp x0, #0x1e8c000
// 0x109ff60: ldr x0, [x0, #0xd8]
// 0x109ff64: bl #0xf7d92c
// 0x109ff68: adrp x0, #0x1e8d000
// 0x109ff6c: ldr x0, [x0, #0xe68]
// 0x109ff70: bl #0xf7d92c
// 0x109ff74: adrp x0, #0x1e8d000
// 0x109ff78: ldr x0, [x0, #0xe28]
// 0x109ff7c: bl #0xf7d92c
// 0x109ff80: mov w8, #1
// 0x109ff84: strb w8, [x22, #0x4b0]
// 0x109ff88: movi v0.2d, #0000000000000000
// 0x109ff8c: str xzr, [sp, #0x68]
// 0x109ff90: stp q0, q0, [sp, #0x40]
// 0x109ff94: ldr s0, [x19, #0x20c]
// 0x109ff98: fcmp s0, #0.0
// 0x109ff9c: b.ls #0x10a00d0
// 0x109ffa0: adrp x25, #0x1e8c000
// 0x109ffa4: ldr x25, [x25, #0xd8]
// 0x109ffa8: ldr x0, [x25]
// 0x109ffac: ldr w8, [x0, #0xe0]
// 0x109ffb0: cbnz w8, #0x109ffb8
// 0x109ffb4: bl #0xf7da5c
// 0x109ffb8: mov x0, x20
// 0x109ffbc: mov x1, xzr
// 0x109ffc0: mov x2, xzr
// 0x109ffc4: bl #0x1b94ac8
// 0x109ffc8: tbz w0, #0, #0x10a05f4
// 0x109ffcc: ldr x8, [x19, #0x78]
// 0x109ffd0: cbz x8, #0x10a0d04
// 0x109ffd4: ldrb w9, [x8, #0x239]
// 0x109ffd8: cbz w9, #0x10a05f4
// 0x109ffdc: ldr s0, [x8, #0x240]
// 0x109ffe0: fcmp s0, #0.0
// 0x109ffe4: b.le #0x10a05f4
// 0x109ffe8: ldrb w9, [x19, #0x2d0]
// 0x109ffec: cbz w9, #0x10a05f4
// 0x109fff0: ldrb w9, [x8, #0x248]
// 0x109fff4: cbz w9, #0x10a0000
// 0x109fff8: and w9, w21, w9
// 0x109fffc: tbz w9, #0, #0x10a05f4
// 0x10a0000: ldr s9, [x8, #0x1fc]
// 0x10a0004: ldr s10, [x8, #0x150]
// 0x10a0008: mov x0, xzr
// 0x10a000c: bl #0x1b9ad30
// 0x10a0010: fadd s1, s9, s10
// 0x10a0014: fcmp s1, s0
// 0x10a0018: b.pl #0x10a05f4
// 0x10a001c: cbz x20, #0x10a0d04
// 0x10a0020: mov x0, x20
// 0x10a0024: mov x1, xzr
// 0x10a0028: bl #0x1b9d508
// 0x10a002c: ldr x0, [x19, #0x480]
// 0x10a0030: cbz x0, #0x10a0d04
// 0x10a0034: mov x1, xzr
// 0x10a0038: mov v9.16b, v0.16b
// 0x10a003c: mov v10.16b, v1.16b
// 0x10a0040: mov v11.16b, v2.16b
// 0x10a0044: bl #0x1b9d508
// 0x10a0048: adrp x21, #0x1fab000
// 0x10a004c: ldrb w8, [x21, #0x2c8]
// 0x10a0050: mov v12.16b, v0.16b
// 0x10a0054: mov v13.16b, v1.16b
// 0x10a0058: mov v14.16b, v2.16b
// 0x10a005c: cbnz w8, #0x10a0074
// 0x10a0060: adrp x0, #0x1e8c000
// 0x10a0064: ldr x0, [x0, #0xa60]
// 0x10a0068: bl #0xf7d92c
// 0x10a006c: mov w8, #1
// 0x10a0070: strb w8, [x21, #0x2c8]
// 0x10a0074: adrp x8, #0x1e8c000
// 0x10a0078: ldr x8, [x8, #0xa60]
// 0x10a007c: fsub s12, s9, s12
// 0x10a0080: fsub s9, s10, s13
// 0x10a0084: fsub s11, s11, s14
// 0x10a0088: ldr x0, [x8]
// 0x10a008c: ldr w8, [x0, #0xe0]
// 0x10a0090: cbnz w8, #0x10a0098
// 0x10a0094: bl #0xf7da5c
// 0x10a0098: fmul s0, s12, s12
// 0x10a009c: fmul s1, s9, s9
// 0x10a00a0: adrp x8, #0x832000
// 0x10a00a4: fadd s0, s0, s1
// 0x10a00a8: ldr s1, [x8, #0x41c]
// 0x10a00ac: fmul s2, s11, s11
// 0x10a00b0: fadd s0, s2, s0
// 0x10a00b4: fsqrt s0, s0
// 0x10a00b8: fcmp s0, s1
// 0x10a00bc: b.le #0x10a00e0
// 0x10a00c0: fdiv s10, s12, s0
// 0x10a00c4: fdiv s9, s9, s0
// 0x10a00c8: fdiv s11, s11, s0
// 0x10a00cc: b #0x10a0118
// 0x10a00d0: ldrb w8, [x19, #0x216]
// 0x10a00d4: cbnz w8, #0x10a0cc8
// 0x10a00d8: str wzr, [x19, #0x20c]
// 0x10a00dc: b #0x10a0cc8
// 0x10a00e0: adrp x21, #0x1fab000
// 0x10a00e4: ldrb w8, [x21, #0x2c9]
// 0x10a00e8: cbnz w8, #0x10a0100
// 0x10a00ec: adrp x0, #0x1e8c000
// 0x10a00f0: ldr x0, [x0, #0x1e8]
// 0x10a00f4: bl #0xf7d92c
// 0x10a00f8: mov w8, #1
// 0x10a00fc: strb w8, [x21, #0x2c9]
// 0x10a0100: adrp x8, #0x1e8c000
// 0x10a0104: ldr x8, [x8, #0x1e8]
// 0x10a0108: ldr x8, [x8]
// 0x10a010c: ldr x8, [x8, #0xb8]
// 0x10a0110: ldp s10, s9, [x8]
// 0x10a0114: ldr s11, [x8, #8]
// 0x10a0118: ldr x0, [x19, #0x480]
// 0x10a011c: cbz x0, #0x10a0d04
// 0x10a0120: mov x1, xzr
// 0x10a0124: bl #0x1b9d9b8
// 0x10a0128: ldr x0, [x19, #0x480]
// 0x10a012c: fmul s0, s10, s0
// 0x10a0130: fmul s1, s9, s1
// 0x10a0134: fadd s0, s0, s1
// 0x10a0138: fmul s1, s11, s2
// 0x10a013c: fadd s0, s1, s0
// 0x10a0140: str s0, [x19, #0x45c]
// 0x10a0144: cbz x0, #0x10a0d04
// 0x10a0148: mov x1, xzr
// 0x10a014c: bl #0x1b9d9b8
// 0x10a0150: ldr x8, [x19, #0x78]
// 0x10a0154: cbz x8, #0x10a0d04
// 0x10a0158: ldr s3, [x8, #0x244]
// 0x10a015c: fmul s0, s10, s0
// 0x10a0160: fmul s1, s9, s1
// 0x10a0164: fmul s2, s11, s2
// 0x10a0168: fadd s0, s0, s1
// 0x10a016c: fadd s0, s2, s0
// 0x10a0170: fcmp s0, s3
// 0x10a0174: b.le #0x10a05f4
// 0x10a0178: ldr x0, [x19, #0x448]
// 0x10a017c: cbz x0, #0x10a0d04
// 0x10a0180: ldr x1, [x8, #0x6d8]
// 0x10a0184: ldr s15, [x8, #0x240]
// 0x10a0188: mov x2, xzr
// 0x10a018c: bl #0x1b6a588
// 0x10a0190: ldr x22, [x19, #0x448]
// 0x10a0194: cbz x22, #0x10a0d04
// 0x10a0198: mov x0, x22
// 0x10a019c: mov x1, xzr
// 0x10a01a0: bl #0x1b6a54c
// 0x10a01a4: mov x1, x0
// 0x10a01a8: fmov s0, #1.00000000
// 0x10a01ac: mov x0, x22
// 0x10a01b0: mov x2, xzr
// 0x10a01b4: bl #0x1b6a66c
// 0x10a01b8: ldr x0, [x25]
// 0x10a01bc: ldr x22, [x19, #0x428]
// 0x10a01c0: ldr w8, [x0, #0xe0]
// 0x10a01c4: cbnz w8, #0x10a01cc
// 0x10a01c8: bl #0xf7da5c
// 0x10a01cc: mov x0, x22
// 0x10a01d0: mov x1, xzr
// 0x10a01d4: bl #0x1b98274
// 0x10a01d8: tbz w0, #0, #0x10a05e0
// 0x10a01dc: ldr x8, [x19, #0x98]
// 0x10a01e0: cbz x8, #0x10a0d04
// 0x10a01e4: ldr x0, [x19, #0x428]
// 0x10a01e8: cbz x0, #0x10a0d04
// 0x10a01ec: ldrb w21, [x8, #0x106]
// 0x10a01f0: mov x1, xzr
// 0x10a01f4: bl #0x1b94c14
// 0x10a01f8: mov x22, x0
// 0x10a01fc: cbz w21, #0x10a0290
// 0x10a0200: ldr x0, [x19, #0x480]
// 0x10a0204: cbz x0, #0x10a0d04
// 0x10a0208: mov x1, xzr
// 0x10a020c: str s15, [sp, #0x1c]
// 0x10a0210: bl #0x1b9d508
// 0x10a0214: ldr x0, [x19, #0x200]
// 0x10a0218: cbz x0, #0x10a0d04
// 0x10a021c: mov x1, xzr
// 0x10a0220: mov v9.16b, v0.16b
// 0x10a0224: mov v10.16b, v1.16b
// 0x10a0228: mov v11.16b, v2.16b
// 0x10a022c: bl #0x1b9d9b8
// 0x10a0230: ldr s15, [x19, #0x430]
// 0x10a0234: mov x0, x19
// 0x10a0238: mov x1, xzr
// 0x10a023c: mov v12.16b, v0.16b
// 0x10a0240: mov v13.16b, v1.16b
// 0x10a0244: mov v14.16b, v2.16b
// 0x10a0248: bl #0x1b92154
// 0x10a024c: cbz x0, #0x10a0d04
// 0x10a0250: mov x1, xzr
// 0x10a0254: bl #0x1b9d940
// 0x10a0258: cbz x22, #0x10a0d04
// 0x10a025c: fmul s4, s14, s15
// 0x10a0260: fmul s5, s13, s15
// 0x10a0264: fmul s6, s12, s15
// 0x10a0268: ldr s15, [sp, #0x1c]
// 0x10a026c: fmov s3, #0.50000000
// 0x10a0270: fadd s4, s11, s4
// 0x10a0274: fmul s2, s2, s3
// 0x10a0278: fadd s5, s10, s5
// 0x10a027c: fmul s1, s1, s3
// 0x10a0280: fadd s2, s4, s2
// 0x10a0284: fadd s1, s5, s1
// 0x10a0288: fadd s9, s9, s6
// 0x10a028c: b #0x10a02ec
// 0x10a0290: ldr x0, [x19, #0x200]
// 0x10a0294: cbz x0, #0x10a0d04
// 0x10a0298: mov x1, xzr
// 0x10a029c: bl #0x1b9d508
// 0x10a02a0: ldr x0, [x19, #0x200]
// 0x10a02a4: cbz x0, #0x10a0d04
// 0x10a02a8: mov x1, xzr
// 0x10a02ac: mov v9.16b, v0.16b
// 0x10a02b0: mov v10.16b, v1.16b
// 0x10a02b4: mov v11.16b, v2.16b
// 0x10a02b8: bl #0x1b9d9b8
// 0x10a02bc: ldr x8, [x19, #0x98]
// 0x10a02c0: cbz x8, #0x10a0d04
// 0x10a02c4: cbz x22, #0x10a0d04
// 0x10a02c8: ldr s3, [x19, #0x430]
// 0x10a02cc: ldr s4, [x8, #0x1a8]
// 0x10a02d0: ldr s5, [x8, #0x1c4]
// 0x10a02d4: fadd s3, s3, s4
// 0x10a02d8: fadd s3, s3, s5
// 0x10a02dc: fmul s2, s2, s3
// 0x10a02e0: fmul s1, s1, s3
// 0x10a02e4: fadd s2, s11, s2
// 0x10a02e8: fadd s1, s10, s1
// 0x10a02ec: fmul s0, s0, s3
// 0x10a02f0: fadd s0, s9, s0
// 0x10a02f4: mov x0, x22
// 0x10a02f8: mov x1, xzr
// 0x10a02fc: bl #0x1b9d5a8
// 0x10a0300: ldr x0, [x19, #0x428]
// 0x10a0304: cbz x0, #0x10a0d04
// 0x10a0308: mov x1, xzr
// 0x10a030c: bl #0x1b94c14
// 0x10a0310: cbz x0, #0x10a0d04
// 0x10a0314: mov x1, xzr
// 0x10a0318: bl #0x1b9ecd4
// 0x10a031c: mov x22, x0
// 0x10a0320: cbz x0, #0x10a0d14
// 0x10a0324: adrp x26, #0x1e8c000
// 0x10a0328: adrp x29, #0x1e8e000
// 0x10a032c: ldr x26, [x26, #0xed0]
// 0x10a0330: ldr x29, [x29, #0xa8]
// 0x10a0334: add x23, x19, #0x438
// 0x10a0338: adrp x27, #0x1fab000
// 0x10a033c: fmov d11, #-0.50000000
// 0x10a0340: fmov d12, #-1.00000000
// 0x10a0344: mov x21, #0x7ff0000000000000
// 0x10a0348: mov w28, #-0x80000000
// 0x10a034c: fmov d13, #0.50000000
// 0x10a0350: fmov d14, #1.00000000
// 0x10a0354: ldr x8, [x22]
// 0x10a0358: ldr x1, [x26]
// 0x10a035c: ldrh w9, [x8, #0x12e]
// 0x10a0360: cbz x9, #0x10a0384
// 0x10a0364: ldr x10, [x8, #0xb0]
// 0x10a0368: add x10, x10, #8
// 0x10a036c: ldur x11, [x10, #-8]
// 0x10a0370: cmp x11, x1
// 0x10a0374: b.eq #0x10a0394
// 0x10a0378: subs x9, x9, #1
// 0x10a037c: add x10, x10, #0x10
// 0x10a0380: b.ne #0x10a036c
// 0x10a0384: mov x0, x22
// 0x10a0388: mov w2, wzr
// 0x10a038c: bl #0xf80110
// 0x10a0390: b #0x10a03a0
// 0x10a0394: ldrsw x9, [x10]
// 0x10a0398: add x8, x8, x9, lsl #4
// 0x10a039c: add x0, x8, #0x138
// 0x10a03a0: ldp x8, x1, [x0]
// 0x10a03a4: mov x0, x22
// 0x10a03a8: blr x8
// 0x10a03ac: tbz w0, #0, #0x10a0554
// 0x10a03b0: ldr x8, [x22]
// 0x10a03b4: ldr x1, [x26]
// 0x10a03b8: ldrh w9, [x8, #0x12e]
// 0x10a03bc: cbz x9, #0x10a03e0
// 0x10a03c0: ldr x10, [x8, #0xb0]
// 0x10a03c4: add x10, x10, #8
// 0x10a03c8: ldur x11, [x10, #-8]
// 0x10a03cc: cmp x11, x1
// 0x10a03d0: b.eq #0x10a03f0
// 0x10a03d4: subs x9, x9, #1
// 0x10a03d8: add x10, x10, #0x10
// 0x10a03dc: b.ne #0x10a03c8
// 0x10a03e0: mov w2, #1
// 0x10a03e4: mov x0, x22
// 0x10a03e8: bl #0xf80110
// 0x10a03ec: b #0x10a0400
// 0x10a03f0: ldr w9, [x10]
// 0x10a03f4: add w9, w9, #1
// 0x10a03f8: add x8, x8, w9, sxtw #4
// 0x10a03fc: add x0, x8, #0x138
// 0x10a0400: ldp x8, x1, [x0]
// 0x10a0404: mov x0, x22
// 0x10a0408: blr x8
// 0x10a040c: cbz x0, #0x10a0d0c
// 0x10a0410: adrp x9, #0x1e8d000
// 0x10a0414: ldr x8, [x0]
// 0x10a0418: ldr x9, [x9, #0xe68]
// 0x10a041c: ldrb w10, [x8, #0x130]
// 0x10a0420: ldr x1, [x9]
// 0x10a0424: ldrb w9, [x1, #0x130]
// 0x10a0428: cmp w10, w9
// 0x10a042c: b.lo #0x10a0d08
// 0x10a0430: ldr x8, [x8, #0xc8]
// 0x10a0434: add x8, x8, x9, lsl #3
// 0x10a0438: ldur x8, [x8, #-8]
// 0x10a043c: cmp x8, x1
// 0x10a0440: b.ne #0x10a0d08
// 0x10a0444: ldr x1, [x29]
// 0x10a0448: bl #0x1231bc8
// 0x10a044c: mov x1, x0
// 0x10a0450: str x1, [x23]
// 0x10a0454: mov x0, x23
// 0x10a0458: bl #0xf7d8d0
// 0x10a045c: ldr x24, [x23]
// 0x10a0460: cbz x24, #0x10a0d10
// 0x10a0464: mov x0, x24
// 0x10a0468: mov x1, xzr
// 0x10a046c: bl #0x1bc9cb4
// 0x10a0470: str x0, [sp, #0x68]
// 0x10a0474: add x8, sp, #0x20
// 0x10a0478: add x0, sp, #0x68
// 0x10a047c: mov x1, xzr
// 0x10a0480: bl #0x1bc9f50
// 0x10a0484: ldp q0, q1, [sp, #0x20]
// 0x10a0488: stp q0, q1, [sp, #0x40]
// 0x10a048c: add x0, sp, #0x40
// 0x10a0490: mov x1, xzr
// 0x10a0494: bl #0x1bca508
// 0x10a0498: ldrb w8, [x27, #0x242]
// 0x10a049c: mov v9.16b, v0.16b
// 0x10a04a0: cbnz w8, #0x10a04b8
// 0x10a04a4: adrp x0, #0x1e8c000
// 0x10a04a8: ldr x0, [x0, #0xa60]
// 0x10a04ac: bl #0xf7d92c
// 0x10a04b0: mov w8, #1
// 0x10a04b4: strb w8, [x27, #0x242]
// 0x10a04b8: adrp x8, #0x1e8c000
// 0x10a04bc: ldr x8, [x8, #0xa60]
// 0x10a04c0: ldr x0, [x8]
// 0x10a04c4: ldr w8, [x0, #0xe0]
// 0x10a04c8: cbnz w8, #0x10a04d0
// 0x10a04cc: bl #0xf7da5c
// 0x10a04d0: fcvt d10, s9
// 0x10a04d4: add x0, sp, #0x20
// 0x10a04d8: mov v0.16b, v10.16b
// 0x10a04dc: bl #0x1db0c60
// 0x10a04e0: fcmp s9, #0.0
// 0x10a04e4: b.ge #0x10a0500
// 0x10a04e8: fcmp d0, d11
// 0x10a04ec: b.ne #0x10a0520
// 0x10a04f0: ldr d0, [sp, #0x20]
// 0x10a04f4: fcvtzs x8, d0
// 0x10a04f8: fadd d1, d0, d12
// 0x10a04fc: b #0x10a0514
// 0x10a0500: fcmp d0, d13
// 0x10a0504: b.ne #0x10a052c
// 0x10a0508: ldr d0, [sp, #0x20]
// 0x10a050c: fcvtzs x8, d0
// 0x10a0510: fadd d1, d0, d14
// 0x10a0514: tst x8, #1
// 0x10a0518: fcsel d0, d0, d1, eq
// 0x10a051c: b #0x10a0534
// 0x10a0520: fadd d0, d10, d11
// 0x10a0524: frintp d0, d0
// 0x10a0528: b #0x10a0534
// 0x10a052c: fadd d0, d10, d13
// 0x10a0530: frintm d0, d0
// 0x10a0534: fmov d1, x21
// 0x10a0538: fcvtzs w8, d0
// 0x10a053c: fcmp d0, d1
// 0x10a0540: csel w1, w28, w8, eq
// 0x10a0544: mov x0, x24
// 0x10a0548: mov x2, xzr
// 0x10a054c: bl #0x1bc9b7c
// 0x10a0550: b #0x10a0354
// 0x10a0554: mov x21, xzr
// 0x10a0558: mov w23, #6
// 0x10a055c: adrp x24, #0x1e8c000
// 0x10a0560: ldr x24, [x24, #0xec8]
// 0x10a0564: mov x0, x22
// 0x10a0568: ldr x1, [x24]
// 0x10a056c: bl #0xf7da60
// 0x10a0570: cbz x0, #0x10a05d0
// 0x10a0574: ldr x8, [x0]
// 0x10a0578: ldr x1, [x24]
// 0x10a057c: mov x22, x0
// 0x10a0580: ldrh w9, [x8, #0x12e]
// 0x10a0584: cbz x9, #0x10a05a8
// 0x10a0588: ldr x10, [x8, #0xb0]
// 0x10a058c: add x10, x10, #8
// 0x10a0590: ldur x11, [x10, #-8]
// 0x10a0594: cmp x11, x1
// 0x10a0598: b.eq #0x10a05b8
// 0x10a059c: subs x9, x9, #1
// 0x10a05a0: add x10, x10, #0x10
// 0x10a05a4: b.ne #0x10a0590
// 0x10a05a8: mov x0, x22
// 0x10a05ac: mov w2, wzr
// 0x10a05b0: bl #0xf80110
// 0x10a05b4: b #0x10a05c4
// 0x10a05b8: ldrsw x9, [x10]
// 0x10a05bc: add x8, x8, x9, lsl #4
// 0x10a05c0: add x0, x8, #0x138
// 0x10a05c4: ldp x8, x1, [x0]
// 0x10a05c8: mov x0, x22
// 0x10a05cc: blr x8
// 0x10a05d0: cbnz x21, #0x10a0d18
// 0x10a05d4: cmp w23, #6
// 0x10a05d8: b.eq #0x10a05e0
// 0x10a05dc: cbnz w23, #0x10a0cc8
// 0x10a05e0: fmov s0, #1.00000000
// 0x10a05e4: fsub s0, s0, s15
// 0x10a05e8: mov w8, #1
// 0x10a05ec: fmul s8, s0, s8
// 0x10a05f0: strb w8, [x19, #0x459]
// 0x10a05f4: mov x0, x19
// 0x10a05f8: mov x1, x20
// 0x10a05fc: bl #0x10a0e04
// 0x10a0600: mov x0, xzr
// 0x10a0604: bl #0x1b9ad30
// 0x10a0608: ldrb w8, [x19, #0x217]
// 0x10a060c: ldr s9, [x19, #0x20c]
// 0x10a0610: str s0, [x19, #0x228]
// 0x10a0614: cbnz w8, #0x10a0620
// 0x10a0618: fsub s9, s9, s8
// 0x10a061c: str s9, [x19, #0x20c]
// 0x10a0620: ldr x20, [x19, #0x1a0]
// 0x10a0624: fcvt d0, s9
// 0x10a0628: add x0, sp, #0x20
// 0x10a062c: bl #0x1db0c60
// 0x10a0630: fcmp s9, #0.0
// 0x10a0634: b.ge #0x10a0650
// 0x10a0638: fmov d1, #-0.50000000
// 0x10a063c: fcmp d0, d1
// 0x10a0640: b.ne #0x10a067c
// 0x10a0644: ldr d0, [sp, #0x20]
// 0x10a0648: fmov s1, #-1.00000000
// 0x10a064c: b #0x10a0664
// 0x10a0650: fmov d1, #0.50000000
// 0x10a0654: fcmp d0, d1
// 0x10a0658: b.ne #0x10a068c
// 0x10a065c: ldr d0, [sp, #0x20]
// 0x10a0660: fmov s1, #1.00000000
// 0x10a0664: fcvtzs x8, d0
// 0x10a0668: fcvt s0, d0
// 0x10a066c: fadd s1, s0, s1
// 0x10a0670: tst x8, #1
// 0x10a0674: fcsel s0, s0, s1, eq
// 0x10a0678: b #0x10a0698
// 0x10a067c: fmov s0, #-0.50000000
// 0x10a0680: fadd s0, s9, s0
// 0x10a0684: frintp s0, s0
// 0x10a0688: b #0x10a0698
// 0x10a068c: fmov s0, #0.50000000
// 0x10a0690: fadd s0, s9, s0
// 0x10a0694: frintm s0, s0
// 0x10a0698: cbz x20, #0x10a0d04
// 0x10a069c: str s0, [x20, #0x20]
// 0x10a06a0: ldr s9, [x19, #0x20c]
// 0x10a06a4: ldr x20, [x19, #0x1a8]
// 0x10a06a8: add x0, sp, #0x20
// 0x10a06ac: fcvt d0, s9
// 0x10a06b0: bl #0x1db0c60
// 0x10a06b4: fcmp s9, #0.0
// 0x10a06b8: b.ge #0x10a06d4
// 0x10a06bc: fmov d1, #-0.50000000
// 0x10a06c0: fcmp d0, d1
// 0x10a06c4: b.ne #0x10a0700
// 0x10a06c8: ldr d0, [sp, #0x20]
// 0x10a06cc: fmov s1, #-1.00000000
// 0x10a06d0: b #0x10a06e8
// 0x10a06d4: fmov d1, #0.50000000
// 0x10a06d8: fcmp d0, d1
// 0x10a06dc: b.ne #0x10a0710
// 0x10a06e0: ldr d0, [sp, #0x20]
// 0x10a06e4: fmov s1, #1.00000000
// 0x10a06e8: fcvtzs x8, d0
// 0x10a06ec: fcvt s0, d0
// 0x10a06f0: fadd s1, s0, s1
// 0x10a06f4: tst x8, #1
// 0x10a06f8: fcsel s0, s0, s1, eq
// 0x10a06fc: b #0x10a071c
// 0x10a0700: fmov s0, #-0.50000000
// 0x10a0704: fadd s0, s9, s0
// 0x10a0708: frintp s0, s0
// 0x10a070c: b #0x10a071c
// 0x10a0710: fmov s0, #0.50000000
// 0x10a0714: fadd s0, s9, s0
// 0x10a0718: frintm s0, s0
// 0x10a071c: cbz x20, #0x10a0d04
// 0x10a0720: str s0, [x20, #0x20]
// 0x10a0724: ldr s0, [x19, #0x20c]
// 0x10a0728: fmov s1, #25.00000000
// 0x10a072c: fcmp s0, s1
// 0x10a0730: b.pl #0x10a079c
// 0x10a0734: ldr x0, [x19, #0x1b0]
// 0x10a0738: cbz x0, #0x10a0d04
// 0x10a073c: ldr x8, [x0]
// 0x10a0740: fmov s0, #1.00000000
// 0x10a0744: fmov s1, wzr
// 0x10a0748: fmov s2, wzr
// 0x10a074c: ldr x9, [x8, #0x2a8]
// 0x10a0750: ldr x1, [x8, #0x2b0]
// 0x10a0754: fmov s3, #1.00000000
// 0x10a0758: blr x9
// 0x10a075c: ldr x0, [x19, #0x30]
// 0x10a0760: cbz x0, #0x10a0d04
// 0x10a0764: ldr x8, [x0]
// 0x10a0768: fmov s0, #1.00000000
// 0x10a076c: fmov s1, wzr
// 0x10a0770: fmov s2, wzr
// 0x10a0774: ldr x9, [x8, #0x2a8]
// 0x10a0778: ldr x1, [x8, #0x2b0]
// 0x10a077c: fmov s3, #1.00000000
// 0x10a0780: blr x9
// 0x10a0784: ldr x0, [x19, #0x28]
// 0x10a0788: cbz x0, #0x10a0d04
// 0x10a078c: mov w1, #1
// 0x10a0790: mov x2, xzr
// 0x10a0794: bl #0x1b94cd0
// 0x10a0798: b #0x10a0838
// 0x10a079c: mov w8, #0x42200000
// 0x10a07a0: fmov s1, w8
// 0x10a07a4: fcmp s0, s1
// 0x10a07a8: b.pl #0x10a07d8
// 0x10a07ac: ldr x0, [x19, #0x1b0]
// 0x10a07b0: cbz x0, #0x10a0d04
// 0x10a07b4: ldr x8, [x0]
// 0x10a07b8: adrp x10, #0x832000
// 0x10a07bc: ldr s2, [x10, #0x37c]
// 0x10a07c0: fmov s0, #1.00000000
// 0x10a07c4: ldr x9, [x8, #0x2a8]
// 0x10a07c8: ldr x1, [x8, #0x2b0]
// 0x10a07cc: adrp x8, #0x832000
// 0x10a07d0: ldr s1, [x8, #0x320]
// 0x10a07d4: b #0x10a0830
// 0x10a07d8: mov w8, #0x42200000
// 0x10a07dc: fmov s1, w8
// 0x10a07e0: fcmp s0, s1
// 0x10a07e4: b.le #0x10a0b00
// 0x10a07e8: ldr x0, [x19, #0x1b0]
// 0x10a07ec: cbz x0, #0x10a0d04
// 0x10a07f0: ldr x8, [x0]
// 0x10a07f4: fmov s0, #1.00000000
// 0x10a07f8: fmov s1, #1.00000000
// 0x10a07fc: fmov s2, #1.00000000
// 0x10a0800: ldr x9, [x8, #0x2a8]
// 0x10a0804: ldr x1, [x8, #0x2b0]
// 0x10a0808: fmov s3, #1.00000000
// 0x10a080c: blr x9
// 0x10a0810: ldr x0, [x19, #0x30]
// 0x10a0814: cbz x0, #0x10a0d04
// 0x10a0818: ldr x8, [x0]
// 0x10a081c: fmov s0, wzr
// 0x10a0820: fmov s1, #1.00000000
// 0x10a0824: fmov s2, wzr
// 0x10a0828: ldr x9, [x8, #0x2a8]
// 0x10a082c: ldr x1, [x8, #0x2b0]
// 0x10a0830: fmov s3, #1.00000000
// 0x10a0834: blr x9
// 0x10a0838: ldrb w8, [x19, #0x459]
// 0x10a083c: cbnz w8, #0x10a08bc
// 0x10a0840: add x8, x19, #0x274
// 0x10a0844: ldr q0, [x8]
// 0x10a0848: add x8, x19, #0x284
// 0x10a084c: mov x0, xzr
// 0x10a0850: str q0, [x8]
// 0x10a0854: ldr s9, [x19, #0x280]
// 0x10a0858: bl #0x1b901f4
// 0x10a085c: adrp x8, #0x832000
// 0x10a0860: ldr s1, [x8, #0x3b8]
// 0x10a0864: ldr x0, [x19, #0xd8]
// 0x10a0868: fmul s0, s0, s1
// 0x10a086c: fadd s0, s9, s0
// 0x10a0870: str s0, [x19, #0x290]
// 0x10a0874: cbz x0, #0x10a0d04
// 0x10a0878: mov w1, #1
// 0x10a087c: mov x2, xzr
// 0x10a0880: bl #0x1b94cd0
// 0x10a0884: ldr x20, [x19, #0xe0]
// 0x10a0888: cbz x20, #0x10a0d04
// 0x10a088c: ldr s3, [x19, #0x290]
// 0x10a0890: ldr s2, [x19, #0x28c]
// 0x10a0894: ldr s1, [x19, #0x288]
// 0x10a0898: ldr s0, [x19, #0x284]
// 0x10a089c: fmov s4, #0.75000000
// 0x10a08a0: mov x0, x20
// 0x10a08a4: mov x1, xzr
// 0x10a08a8: bl #0x108eabc
// 0x10a08ac: mov x1, x0
// 0x10a08b0: mov x0, x20
// 0x10a08b4: mov x2, xzr
// 0x10a08b8: bl #0x1b95d40
// 0x10a08bc: ldr x8, [x19, #0x60]
// 0x10a08c0: cbz x8, #0x10a0d04
// 0x10a08c4: ldrb w8, [x8, #0x256]
// 0x10a08c8: cbz w8, #0x10a0968
// 0x10a08cc: mov x0, xzr
// 0x10a08d0: bl #0x1b9ad30
// 0x10a08d4: ldr s1, [x19, #0x270]
// 0x10a08d8: fcmp s0, s1
// 0x10a08dc: b.le #0x10a09fc
// 0x10a08e0: ldr x0, [x25]
// 0x10a08e4: ldr x20, [x19, #0x3e0]
// 0x10a08e8: ldr w8, [x0, #0xe0]
// 0x10a08ec: cbnz w8, #0x10a08f4
// 0x10a08f0: bl #0xf7da5c
// 0x10a08f4: mov x0, x20
// 0x10a08f8: mov x1, xzr
// 0x10a08fc: bl #0x1b98274
// 0x10a0900: tbz w0, #0, #0x10a09fc
// 0x10a0904: ldr x0, [x19, #0x448]
// 0x10a0908: cbz x0, #0x10a0d04
// 0x10a090c: ldr x1, [x19, #0x3e0]
// 0x10a0910: mov x2, xzr
// 0x10a0914: bl #0x1b6a588
// 0x10a0918: ldr x20, [x19, #0x448]
// 0x10a091c: cbz x20, #0x10a0d04
// 0x10a0920: mov x0, x20
// 0x10a0924: mov x1, xzr
// 0x10a0928: bl #0x1b6a54c
// 0x10a092c: mov x1, x0
// 0x10a0930: fmov s0, #1.00000000
// 0x10a0934: mov x0, x20
// 0x10a0938: mov x2, xzr
// 0x10a093c: bl #0x1b6a66c
// 0x10a0940: mov x0, xzr
// 0x10a0944: bl #0x1b9ad30
// 0x10a0948: mov v9.16b, v0.16b
// 0x10a094c: fmov s0, #0.50000000
// 0x10a0950: fmov s1, #0.75000000
// 0x10a0954: mov x0, xzr
// 0x10a0958: bl #0x1b9012c
// 0x10a095c: fadd s0, s9, s0
// 0x10a0960: str s0, [x19, #0x270]
// 0x10a0964: b #0x10a09fc
// 0x10a0968: ldrb w8, [x19, #0x459]
// 0x10a096c: cbnz w8, #0x10a09fc
// 0x10a0970: mov x0, xzr
// 0x10a0974: bl #0x1b9ad30
// 0x10a0978: ldr s1, [x19, #0x270]
// 0x10a097c: fcmp s0, s1
// 0x10a0980: b.le #0x10a09fc
// 0x10a0984: ldr x0, [x25]
// 0x10a0988: ldr x20, [x19, #0x3d8]
// 0x10a098c: ldr w8, [x0, #0xe0]
// 0x10a0990: cbnz w8, #0x10a0998
// 0x10a0994: bl #0xf7da5c
// 0x10a0998: mov x0, x20
// 0x10a099c: mov x1, xzr
// 0x10a09a0: bl #0x1b98274
// 0x10a09a4: tbz w0, #0, #0x10a09fc
// 0x10a09a8: ldr x0, [x25]
// 0x10a09ac: ldr x20, [x19, #0x3d0]
// 0x10a09b0: ldr w8, [x0, #0xe0]
// 0x10a09b4: cbnz w8, #0x10a09bc
// 0x10a09b8: bl #0xf7da5c
// 0x10a09bc: mov x0, x20
// 0x10a09c0: mov x1, xzr
// 0x10a09c4: bl #0x1b98274
// 0x10a09c8: tbz w0, #0, #0x10a09fc
// 0x10a09cc: ldr x0, [x19, #0x448]
// 0x10a09d0: fmov s0, #30.00000000
// 0x10a09d4: fcmp s8, s0
// 0x10a09d8: b.gt #0x10a0cf8
// 0x10a09dc: ldr s0, [x19, #0x20c]
// 0x10a09e0: mov w8, #0x42200000
// 0x10a09e4: fmov s1, w8
// 0x10a09e8: fcmp s0, s1
// 0x10a09ec: b.mi #0x10a0cf8
// 0x10a09f0: cbz x0, #0x10a0d04
// 0x10a09f4: ldr x1, [x19, #0x3d0]
// 0x10a09f8: b #0x10a0910
// 0x10a09fc: ldr x8, [x19, #0x98]
// 0x10a0a00: cbz x8, #0x10a0d04
// 0x10a0a04: ldrb w8, [x8, #0x106]
// 0x10a0a08: cbnz w8, #0x10a0be0
// 0x10a0a0c: mov w0, #0x64
// 0x10a0a10: mov w1, #-0x64
// 0x10a0a14: mov x2, xzr
// 0x10a0a18: bl #0x1b9016c
// 0x10a0a1c: mov w20, w0
// 0x10a0a20: mov w0, #0x64
// 0x10a0a24: mov w1, #-0x64
// 0x10a0a28: mov x2, xzr
// 0x10a0a2c: bl #0x1b9016c
// 0x10a0a30: ldr x8, [x19, #0x200]
// 0x10a0a34: cbz x8, #0x10a0d04
// 0x10a0a38: fmov s0, w20
// 0x10a0a3c: movi v1.2d, #0xffffffffffffffff
// 0x10a0a40: mov v0.s[1], w0
// 0x10a0a44: movi v2.2s, #0x30
// 0x10a0a48: add v1.2s, v0.2s, v1.2s
// 0x10a0a4c: movi v3.2s, #0x32
// 0x10a0a50: cmhi v1.2s, v1.2s, v2.2s
// 0x10a0a54: bif v0.8b, v3.8b, v1.8b
// 0x10a0a58: mvni v1.2s, #0x31
// 0x10a0a5c: mov x0, x8
// 0x10a0a60: mov x1, xzr
// 0x10a0a64: umin v9.2s, v0.2s, v1.2s
// 0x10a0a68: bl #0x1b9d7f0
// 0x10a0a6c: mov x0, xzr
// 0x10a0a70: bl #0x1b8b1c4
// 0x10a0a74: adrp x8, #0x832000
// 0x10a0a78: ldr s3, [x8, #0x554]
// 0x10a0a7c: mov x0, xzr
// 0x10a0a80: fmul s0, s0, s3
// 0x10a0a84: fmul s1, s1, s3
// 0x10a0a88: fmul s2, s2, s3
// 0x10a0a8c: bl #0x1b8b63c
// 0x10a0a90: adrp x9, #0x832000
// 0x10a0a94: mov w8, #0xfa35
// 0x10a0a98: mov v0.s[1], v1.s[0]
// 0x10a0a9c: ldr s1, [x9, #0x3e4]
// 0x10a0aa0: scvtf v3.2s, v9.2s
// 0x10a0aa4: movk w8, #0x3c8e, lsl #16
// 0x10a0aa8: dup v4.2s, w8
// 0x10a0aac: fsub v0.2s, v0.2s, v3.2s
// 0x10a0ab0: fmul v0.2s, v0.2s, v4.2s
// 0x10a0ab4: fmul s2, s2, s1
// 0x10a0ab8: mov s1, v0.s[1]
// 0x10a0abc: mov x0, xzr
// 0x10a0ac0: bl #0x1b8b12c
// 0x10a0ac4: ldrb w8, [x19, #0x2d0]
// 0x10a0ac8: mov v9.16b, v0.16b
// 0x10a0acc: mov v10.16b, v1.16b
// 0x10a0ad0: mov v11.16b, v2.16b
// 0x10a0ad4: mov v12.16b, v3.16b
// 0x10a0ad8: cbz w8, #0x10a0aec
// 0x10a0adc: ldr x8, [x19, #0x78]
// 0x10a0ae0: cbz x8, #0x10a0d04
// 0x10a0ae4: ldrb w8, [x8, #0x239]
// 0x10a0ae8: cbz w8, #0x10a0b60
// 0x10a0aec: ldr s0, [x19, #0x294]
// 0x10a0af0: fmov s1, #10.00000000
// 0x10a0af4: fmul s0, s0, s1
// 0x10a0af8: fdiv s0, s8, s0
// 0x10a0afc: b #0x10a0b78
// 0x10a0b00: ldr x0, [x19, #0x30]
// 0x10a0b04: cbz x0, #0x10a0d04
// 0x10a0b08: ldr x8, [x0]
// 0x10a0b0c: fmov s0, wzr
// 0x10a0b10: fmov s1, #1.00000000
// 0x10a0b14: fmov s2, wzr
// 0x10a0b18: ldr x9, [x8, #0x2a8]
// 0x10a0b1c: ldr x1, [x8, #0x2b0]
// 0x10a0b20: fmov s3, #1.00000000
// 0x10a0b24: blr x9
// 0x10a0b28: ldr x8, [x19, #0x1a0]
// 0x10a0b2c: cbz x8, #0x10a0d04
// 0x10a0b30: ldr x0, [x19, #0x1b0]
// 0x10a0b34: cbz x0, #0x10a0d04
// 0x10a0b38: ldr x9, [x0]
// 0x10a0b3c: ldp s2, s3, [x8, #0x30]
// 0x10a0b40: ldp s0, s1, [x8, #0x28]
// 0x10a0b44: ldr x8, [x9, #0x2a8]
// 0x10a0b48: ldr x1, [x9, #0x2b0]
// 0x10a0b4c: blr x8
// 0x10a0b50: ldr x0, [x19, #0x28]
// 0x10a0b54: cbz x0, #0x10a0d04
// 0x10a0b58: mov w1, wzr
// 0x10a0b5c: b #0x10a0790
// 0x10a0b60: ldr s0, [x19, #0x294]
// 0x10a0b64: fmov s1, #10.00000000
// 0x10a0b68: fmul s0, s0, s1
// 0x10a0b6c: fdiv s0, s8, s0
// 0x10a0b70: fmov s1, #3.00000000
// 0x10a0b74: fdiv s0, s0, s1
// 0x10a0b78: ldrb w8, [x19, #0x459]
// 0x10a0b7c: adrp x9, #0x832000
// 0x10a0b80: ldr s1, [x9, #0x304]
// 0x10a0b84: ldr x20, [x19, #0x200]
// 0x10a0b88: cmp w8, #0
// 0x10a0b8c: fcsel s0, s0, s1, eq
// 0x10a0b90: cbz x20, #0x10a0d04
// 0x10a0b94: adrp x8, #0x832000
// 0x10a0b98: ldr s1, [x8, #0x2f8]
// 0x10a0b9c: fcmp s0, #0.0
// 0x10a0ba0: mov x0, x20
// 0x10a0ba4: mov x1, xzr
// 0x10a0ba8: fmin s0, s0, s1
// 0x10a0bac: fmov s1, wzr
// 0x10a0bb0: fcsel s8, s0, s1, pl
// 0x10a0bb4: bl #0x1b9d7f0
// 0x10a0bb8: mov v4.16b, v9.16b
// 0x10a0bbc: mov v5.16b, v10.16b
// 0x10a0bc0: mov v6.16b, v11.16b
// 0x10a0bc4: mov v7.16b, v12.16b
// 0x10a0bc8: mov x0, xzr
// 0x10a0bcc: str s8, [sp]
// 0x10a0bd0: bl #0x1b8af84
// 0x10a0bd4: mov x0, x20
// 0x10a0bd8: mov x1, xzr
// 0x10a0bdc: bl #0x1b9d874
// 0x10a0be0: ldr x8, [x19, #0x78]
// 0x10a0be4: cbz x8, #0x10a0d04
// 0x10a0be8: ldrb w9, [x8, #0x239]
// 0x10a0bec: cbz w9, #0x10a0c04
// 0x10a0bf0: ldrb w8, [x8, #0x23b]
// 0x10a0bf4: cbz w8, #0x10a0c00
// 0x10a0bf8: strb wzr, [x19, #0x2d0]
// 0x10a0bfc: b #0x10a0c04
// 0x10a0c00: strb wzr, [x19, #0x459]
// 0x10a0c04: ldr s0, [x19, #0x20c]
// 0x10a0c08: fcmp s0, #0.0
// 0x10a0c0c: b.ls #0x10a0c2c
// 0x10a0c10: ldr x0, [x19, #0x48]
// 0x10a0c14: cbz x0, #0x10a0d04
// 0x10a0c18: mov x1, xzr
// 0x10a0c1c: bl #0x1b92190
// 0x10a0c20: cbz x0, #0x10a0d04
// 0x10a0c24: mov w1, #1
// 0x10a0c28: b #0x10a0cc0
// 0x10a0c2c: adrp x8, #0x1e8d000
// 0x10a0c30: ldr x8, [x8, #0x230]
// 0x10a0c34: mov x0, x19
// 0x10a0c38: ldr x1, [x8]
// 0x10a0c3c: bl #0x1231bc8
// 0x10a0c40: cbz x0, #0x10a0d04
// 0x10a0c44: mov w1, #1
// 0x10a0c48: mov x2, xzr
// 0x10a0c4c: bl #0x1bcf2d0
// 0x10a0c50: ldr x0, [x19, #0x68]
// 0x10a0c54: cbz x0, #0x10a0d04
// 0x10a0c58: mov x1, xzr
// 0x10a0c5c: bl #0x10b3d4c
// 0x10a0c60: adrp x8, #0x1e8d000
// 0x10a0c64: ldr x8, [x8, #0xe28]
// 0x10a0c68: mov x1, xzr
// 0x10a0c6c: ldr x0, [x8]
// 0x10a0c70: bl #0x1b8fab8
// 0x10a0c74: adrp x8, #0x1e8d000
// 0x10a0c78: ldr x8, [x8, #0xe18]
// 0x10a0c7c: cmp w0, #0x1f
// 0x10a0c80: ldr x8, [x8]
// 0x10a0c84: ldr x8, [x8, #0xb8]
// 0x10a0c88: b.ne #0x10a0ca0
// 0x10a0c8c: ldr x0, [x8, #8]
// 0x10a0c90: cbz x0, #0x10a0d04
// 0x10a0c94: mov x1, xzr
// 0x10a0c98: bl #0x10c06d0
// 0x10a0c9c: b #0x10a0ca8
// 0x10a0ca0: mov w9, #2
// 0x10a0ca4: str w9, [x8]
// 0x10a0ca8: ldr x0, [x19, #0x48]
// 0x10a0cac: cbz x0, #0x10a0d04
// 0x10a0cb0: mov x1, xzr
// 0x10a0cb4: bl #0x1b92190
// 0x10a0cb8: cbz x0, #0x10a0d04
// 0x10a0cbc: mov w1, wzr
// 0x10a0cc0: mov x2, xzr
// 0x10a0cc4: bl #0x1b94cd0
// 0x10a0cc8: ldp x20, x19, [sp, #0x100]
// 0x10a0ccc: ldp x22, x21, [sp, #0xf0]
// 0x10a0cd0: ldp x24, x23, [sp, #0xe0]
// 0x10a0cd4: ldp x26, x25, [sp, #0xd0]
// 0x10a0cd8: ldp x28, x27, [sp, #0xc0]
// 0x10a0cdc: ldp x29, x30, [sp, #0xb0]
// 0x10a0ce0: ldp d9, d8, [sp, #0xa0]
// 0x10a0ce4: ldp d11, d10, [sp, #0x90]
// 0x10a0ce8: ldp d13, d12, [sp, #0x80]
// 0x10a0cec: ldp d15, d14, [sp, #0x70]
// 0x10a0cf0: add sp, sp, #0x110
// 0x10a0cf4: ret
// 0x10a0cf8: cbz x0, #0x10a0d04
// 0x10a0cfc: ldr x1, [x19, #0x3d8]
// 0x10a0d00: b #0x10a0910
// 0x10a0d04: bl #0xf7db74
// 0x10a0d08: bl #0xf7df10
// 0x10a0d0c: bl #0xf7db74
// 0x10a0d10: bl #0xf7db74
// 0x10a0d14: bl #0xf7db74
// 0x10a0d18: mov x0, x21
// 0x10a0d1c: bl #0xf1bd40
// 0x10a0d20: b #0x10a0d48
// 0x10a0d24: b #0x10a0d48
// 0x10a0d28: b #0x10a0d48
// 0x10a0d2c: b #0x10a0d48
// 0x10a0d30: b #0x10a0d48
// 0x10a0d34: b #0x10a0d48
// 0x10a0d38: b #0x10a0d48
// 0x10a0d3c: b #0x10a0d48
// 0x10a0d40: b #0x10a0d48
// 0x10a0d44: b #0x10a0d48
// 0x10a0d48: mov x23, x0
// 0x10a0d4c: cmp w1, #1
// 0x10a0d50: b.ne #0x10a0d6c
// 0x10a0d54: mov x0, x23
// 0x10a0d58: bl #0x1db0c00
// 0x10a0d5c: ldr x21, [x0]
// 0x10a0d60: bl #0x1db0c10
// 0x10a0d64: mov w23, wzr
// 0x10a0d68: b #0x10a055c
// 0x10a0d6c: mov x21, xzr
// 0x10a0d70: b #0x10a0d78
// 0x10a0d74: mov x23, x0
// 0x10a0d78: adrp x20, #0x1e8c000
// 0x10a0d7c: ldr x20, [x20, #0xec8]
// 0x10a0d80: ldr x1, [x20]
// 0x10a0d84: mov x0, x22
// 0x10a0d88: bl #0xf7da60
// 0x10a0d8c: mov x19, x0
// 0x10a0d90: cbz x0, #0x10a0dec
// 0x10a0d94: ldr x8, [x19]
// 0x10a0d98: ldr x1, [x20]
// 0x10a0d9c: ldrh w9, [x8, #0x12e]
// 0x10a0da0: cbz x9, #0x10a0dc4
// 0x10a0da4: ldr x10, [x8, #0xb0]
// 0x10a0da8: add x10, x10, #8
// 0x10a0dac: ldur x11, [x10, #-8]
// 0x10a0db0: cmp x11, x1
// 0x10a0db4: b.eq #0x10a0dd4
// 0x10a0db8: subs x9, x9, #1
// 0x10a0dbc: add x10, x10, #0x10
// 0x10a0dc0: b.ne #0x10a0dac
// 0x10a0dc4: mov x0, x19
// 0x10a0dc8: mov w2, wzr
// 0x10a0dcc: bl #0xf80110
// 0x10a0dd0: b #0x10a0de0
// 0x10a0dd4: ldrsw x9, [x10]
// 0x10a0dd8: add x8, x8, x9, lsl #4
// 0x10a0ddc: add x0, x8, #0x138
// 0x10a0de0: ldp x8, x1, [x0]
// 0x10a0de4: mov x0, x19
// 0x10a0de8: blr x8
// 0x10a0dec: cbnz x21, #0x10a0df8
// 0x10a0df0: mov x0, x23
// 0x10a0df4: bl #0x1026098
// 0x10a0df8: mov x0, x21
// 0x10a0dfc: bl #0xf1bd40
// 0x10a0e00: bl #0xe29990
```

## `FPSPlayer.ApplyHitDirection` — RVA `0xca0e04`

- Decompiled symbol: `FPSPlayer_ApplyHitDirection`
- Metadata signature: `public void ApplyHitDirection(Transform hitTransform) { }`
- Native interval: `484` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1f00260;
extern char g_1fab4af;

long long FPSPlayer_ApplyHitDirection(long long *a0, long long a1)
{
    long long v3;  // x0
    unsigned int v4;  // s1
    unsigned int v5;  // s2
    unsigned int v6;  // s0
    unsigned long v7;  // x0
    unsigned int v0;  // [bp-0x70]
    unsigned int v1;  // [bp-0x6c]
    unsigned int v2;  // [bp-0x68]

    if (!(g_1fab4af & 1))
    {
        sub_f7d92c(&g_1f00260);
        sub_f7d92c(&g_1ef0c58);
        g_1fab4af = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v3 = Object__op_Implicit(a1, 0);
    if (!((char)v3 & 1))
        return v3;
    if (Component__get_transform(a0, 0))
    {
        Transform__get_forward();
        if (a1)
        {
            Transform__get_forward(a1, 0);
            if (Component__get_transform(a0, 0))
            {
                Transform__get_up();
                v1 = v4;
                v2 = v5;
                v0 = v6;
                sub_10a61f0(0);
                Quaternion__Internal_FromEulerRad(0);
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if (sub_112a1ac(a0[145], g_1f00260))
                {
                    v7 = GameObject__get_transform();
                    if (a0[146])
                        GameObject__get_transform(a0[146], 0);
                }
            }
        }
    }
    sub_f7db74();
}
```

## `FPSPlayer.ApplyDamageEmerald` — RVA `0xca0fe8`

- Decompiled symbol: `FPSPlayer_ApplyDamageEmerald`
- Metadata signature: `public void ApplyDamageEmerald(object[] DamageArray) { }`
- Native interval: `304` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FPSPlayer_Recovered` matched 2 offsets against `FPSPlayer` metadata (confidence 1.00).

```c
typedef struct FPSPlayer_Recovered {
    char padding_0[200];
    unsigned long long weaponObj;
    char padding_d0[96];
    char thirstUiObj;
} FPSPlayer_Recovered;

typedef struct struct_4 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_5 *field_20;
    struct struct_5 *field_28;
    struct struct_5 *field_30;
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

typedef struct struct_0 {
    char padding_0[64];
    unsigned long long field_40;
} struct_0;

typedef struct struct_1 {
    char padding_0[64];
    unsigned long long field_40;
} struct_1;

extern struct_0 *g_1eeebf0;
extern struct_1 *g_1ef1720;
extern struct_6 *g_1fab000;
extern char g_1fab4b1;

void FPSPlayer_ApplyDamageEmerald(void* a0, struct_4 *ptr)
{
    struct_6 **v0;  // x21
    struct_3 **v2;  // x0
    struct_6 **v3;  // x20
    unsigned long v4;  // x9
    char *v5;  // x0

    v0 = &g_1fab000;
    if (!(g_1fab4b1 & 1))
    {
        sub_f7d92c(&g_1eeebf0);
        sub_f7d92c(&g_1ef1720);
        sub_f7d92c("cY");
        g_1fab4b1 = 1;
    }
    if (ptr)
    {
        if (ptr->field_18 && ptr->field_18 != 1 && ptr->field_18 > 2)
        {
            v2 = ptr->field_20;
            if (v2)
            {
                if (*((long long *)&*(v2)->padding_0[64]) != g_1ef1720->field_40)
                    sub_f7df10(v2);
                v0 = ptr->field_28;
                v3 = ptr->field_30;
                sub_f7da68();
                if (v0 && !((v4 = (unsigned long)(unsigned long long)g_1ef1e78->field_130, (unsigned int)*(v0)->field_130 >= (unsigned int)v4 && *((long long *)(*(v0)->field_c8 + v4 * 8 - 8)) == g_1ef1e78)))
                    goto LABEL_10a1110;
                if (v3)
                {
                    v2 = v3;
                    if (*((long long *)&*(v3)->padding_0[64]) == g_1eeebf0->field_40)
                    {
                        v5 = sub_f7da68(v2, g_1eeebf0);
                        FPSPlayer__ApplyDamage(a0, v0, *(v5));
                        return;
                    }
                    sub_f7df10(v2);
                }
            }
        }
        else
        {
            sub_f7db7c();
        }
    }
    sub_f7db74();
LABEL_10a1110:
    sub_f7df10(v0);
}
```

## `FPSPlayer.RestartMap` — RVA `0xca1118`

- Decompiled symbol: `FPSPlayer_RestartMap`
- Metadata signature: `public void RestartMap() { }`
- Native interval: `128` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FPSPlayer_Recovered` matched 4 offsets against `FPSPlayer` metadata (confidence 1.00).

```c
typedef struct FPSPlayer_Recovered {
    char padding_0[96];
    struct struct_0 *FPSWalkerComponent;
    char padding_68[16];
    struct struct_1 *WeaponBehaviorComponent;
    char padding_80[120];
    unsigned long long levelLoadFadeRef;
    char padding_100[718];
    char restarting;
} FPSPlayer_Recovered;

typedef struct struct_0 {
    char padding_0[192];
    unsigned long long field_c0;
    char padding_c8[506];
    char field_2c2;
} struct_0;

typedef struct struct_1 {
    char padding_0[933];
    char field_3a5;
} struct_1;

void FPSPlayer_RestartMap(struct_2 *ptr)
{
    unsigned long long v0;  // x0
    struct_0 *p;  // x8

    Time__set_timeScale(0);
    v0 = ptr->field_f8;
    if (v0)
    {
        MonoBehaviour__StopAllCoroutines(v0, 0);
        v0 = ptr->field_f8;
        if (v0)
        {
            v0 = LevelLoadFade__FadeAndLoadLevel(v0, 0, 0);
            p = ptr->field_60;
            ptr->field_3ce = 1;
            if (p)
            {
                p->field_c0 = 0;
                p->field_2c2 = 1;
                if (ptr->field_78)
                {
                    ptr->field_78->field_3a5 = 0;
                    return;
                }
            }
        }
    }
    sub_f7db74(v0);
}
```

## `FPSPlayer.Missionfailed` — RVA `0xca1198`

- Decompiled symbol: `FPSPlayer_Missionfailed`
- Metadata signature: `private IEnumerator Missionfailed() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef30e8;
extern char g_1fab4b2;

struct_0 * FPSPlayer_Missionfailed(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab4b2 & 1))
    {
        sub_f7d92c(&g_1ef30e8);
        g_1fab4b2 = 1;
    }
    v0 = sub_f7db70(g_1ef30e8);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```

## `FPSPlayer.<Missionfailed>d__186.ctor` — RVA `0xca1204`

- Decompiled symbol: `FPSPlayer_Missionfailed_d__186_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void FPSPlayer_Missionfailed_d__186_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `FPSPlayer.HealthCounterfunc` — RVA `0xca122c`

- Decompiled symbol: `FPSPlayer_HealthCounterfunc`
- Metadata signature: `public void HealthCounterfunc() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[56];
    int field_38;
} struct_0;

extern long long g_1f0a9f0;
extern char g_1fab4b3;

struct_0 * FPSPlayer_HealthCounterfunc(struct_0 *ptr)
{
    struct_0 *v0;  // x0
    struct_0 *v1;  // x0
    struct_0 *v2;  // x0
    unsigned long long v3;  // x0

    v0 = ptr;
    if (!(g_1fab4b3 & 1))
    {
        v1 = sub_f7d92c(&g_1f0a9f0);
        g_1fab4b3 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (ptr->field_38 <= 9)
    {
        ptr->field_38 = ptr->field_38 + 1;
        v3 = PlayerPrefs__SetInt();
        return PlayerPrefs__SetInt();
    }
    return v2;
}
```

## `FPSPlayer.HealthAdd` — RVA `0xca1294`

- Decompiled symbol: `FPSPlayer_HealthAdd`
- Metadata signature: `public void HealthAdd() { }`
- Native interval: `260` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FPSPlayer_Recovered` matched 3 offsets against `FPSPlayer` metadata (confidence 1.00).

```c
typedef struct FPSPlayer_Recovered {
    char padding_0[56];
    int Healthcounter;
    char padding_3c[464];
    unsigned int hitPoints;
    unsigned int maximumHitPoints;
} FPSPlayer_Recovered;

typedef struct struct_0 {
    char padding_0[8];
    long long field_8;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

extern struct_1 *g_1eefae8;
extern long long g_1f06220;
extern long long g_1f0a9f0;
extern char g_1fab4b4;

struct_2 * FPSPlayer_HealthAdd(struct_2 *ptr)
{
    struct_2 *v0;  // x0
    struct_2 *v1;  // x0
    struct_2 *v2;  // x0
    unsigned int v3;  // s0
    unsigned int v4;  // s1
    unsigned long v5;  // 4133

    v0 = ptr;
    if (!(g_1fab4b4 & 1))
    {
        sub_f7d92c(&g_1eefae8);
        sub_f7d92c(&g_1f0a9f0);
        v1 = sub_f7d92c(&g_1f06220);
        g_1fab4b4 = 1;
        v0 = v1;
    }
    v2 = v0;
    v3 = ptr->field_20c;
    v4 = ptr->field_210;
    v5 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v3, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v4) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v4) & 1)) & ((unsigned long long)(char)(CmpF(v3, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v4) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v5)
    {
        return v2;
    }
    else if (ptr->field_38 >= 1)
    {
        if (g_1eefae8->field_b8->field_8)
            GameController__Health_Image(g_1eefae8->field_b8->field_8, 0); /* do not return */
        sub_f7db74(0);
    }
    else
    {
        return v2;
    }
}
```

## `FPSPlayer.ctor` — RVA `0xca1398`

- Decompiled symbol: `FPSPlayer_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `208` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FPSPlayer_Recovered` matched 26 offsets against `FPSPlayer` metadata (confidence 0.96).

```c
typedef struct FPSPlayer_Recovered {
    char padding_0[500];
    unsigned int hitTime;
    char padding_1f8[16];
    char removePrefabRoot;
    char padding_209[3];
    unsigned long long hitPoints;
    unsigned short showHealth;
    char showHpUnderZero;
    char padding_217[5];
    unsigned long long maxRegenHealth;
    unsigned int healthRegenRate;
    char padding_228[8];
    unsigned long long maxHungerPoints;
    char padding_238[12];
    unsigned long long starveInterval;
    char padding_24c[4];
    unsigned long long maxThirstPoints;
    char padding_258[12];
    unsigned long long thirstDmgInterval;
    unsigned short allowBulletTime;
    char pauseHidesCursor;
    char padding_26f[1];
    uint128_t gotHitTimer;
    unsigned int field_280;
    char padding_284[16];
    unsigned long long painScreenKickAmt;
    unsigned int sloMoMoveSpeed;
    char padding_2a0[40];
    char zoomBtnState;
    char padding_2c9[11];
    unsigned int zoomStart;
    char padding_2d8[12];
    unsigned int zoomDelay;
    char padding_2e8[1];
    unsigned short crosshairEnabled;
    char padding_2eb[1];
    char useSwapReticle;
    char padding_2ed[51];
    uint128_t pickupReticleColor;
    uint128_t reticleColor;
    char padding_340[16];
    uint128_t hitmarkerColor;
    char padding_360[4];
    unsigned int reachDistance;
    char padding_368[101];
    char pickUpBtnState;
} FPSPlayer_Recovered;

long long FPSPlayer_ctor(struct_0 *ptr)
{
    struct_0 *p;  // x8
    int v1;  // q0

    p = &(&ptr->padding_209)[1];
    ptr->field_1f4 = 0xc1200000;
    ptr->field_208 = 1;
    *((unsigned long long *)&p->padding_0[0]) = 0x4348000042c80000;
    *((unsigned short *)((char *)&ptr->field_20c + 4)) = 257;
    *((char *)&ptr->field_20c + 6) = 1;
    *((unsigned long long *)&p->padding_0[16]) = 0x40e0000042c80000;
    *((unsigned int *)((char *)&ptr->field_21c + 4)) = 0x41c80000;
    *((unsigned long long *)&ptr->padding_228[4]) = 0x40e0000042c80000;
    *((unsigned long long *)&p->padding_0[56]) = 0xc0a0000040400000;
    ptr->field_244 = 0x40e0000042c80000;
    *((unsigned long long *)&p->padding_0[88]) = 0xc0a0000040400000;
    *((unsigned int *)&ptr->field_26c) = 0x3f800000;
    *((unsigned short *)&ptr->padding_258[4]) = 257;
    ptr->padding_258[6] = 1;
    *((uint128_t *)&ptr->padding_258[8]) = 0x3f8000003f8000003f800000bf800000;
    *((unsigned long long *)&p->padding_0[136]) = 4518011146334311023;
    *((unsigned int *)((char *)&ptr->field_270 + 12)) = 0x40000000;
    *((unsigned int *)&ptr->padding_2a0[32]) = 1053609165;
    *((unsigned int *)&ptr->padding_2a0[16]) = 0xc0000000;
    v1 = (int)(0x3f8000003f800000 CONCAT 0x3f8000003f800000);
    ptr->padding_2a0[4] = 1;
    *((unsigned short *)&ptr->padding_2a0[37]) = 257;
    ptr->field_2c8 = 1;
    *((void*)&ptr->padding_2ed[14]) = v1;
    *((void*)&ptr->padding_2ed[30]) = v1;
    *((void*)&ptr->field_320) = v1;
    *((unsigned int *)((char *)&ptr->field_330 + 4)) = 1074161254;
    ptr->padding_368[53] = 1;
}
```

## `FPSPlayer.<ActivateBulletTime>d__175.Dispose` — RVA `0xca1468`

- Decompiled symbol: `FPSPlayer_ActivateBulletTime_d__175_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long FPSPlayer_ActivateBulletTime_d__175_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `FPSPlayer.<ActivateBulletTime>d__175.MoveNext` — RVA `0xca146c`

- Decompiled symbol: `FPSPlayer_ActivateBulletTime_d__175_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `256` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_0 *field_20;
    unsigned int field_28;
    unsigned int field_2c;
} struct_1;

typedef struct struct_0 {
    char padding_0[676];
    char field_2a4;
} struct_0;

extern long long g_1ef2440;
extern char g_1fab4b5;

unsigned int FPSPlayer_ActivateBulletTime_d__175_MoveNext(struct_1 *ptr)
{
    struct_0 *p;  // x20
    unsigned int v1;  // s0
    unsigned int v2;  // s8
    unsigned int v3;  // s1
    unsigned long v4;  // 4138
    long long v5;  // x20
    struct_1 *addr;  // x19

    if (!(g_1fab4b5 & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab4b5 = 1;
    }
    p = ptr->field_20;
    if (ptr->field_10 == 1)
    {
        v2 = ptr->field_2c;
        ptr->field_10 = 4294967295;
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        if (!p)
            sub_f7db74();
        if (p->field_2a4)
            return 0;
        p->field_2a4 = 1;
        Time__get_time(0);
        v2 = v1;
        ptr->field_2c = v1;
    }
    else
    {
        return 0;
    }
    Time__get_time(0);
    v3 = v2 + ptr->field_28;
    v4 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v3, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v1) & 1)) & ((unsigned long long)(char)(CmpF(v3, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v4)
    {
        v5 = sub_f7db70(g_1ef2440);
        WaitForSeconds__ctor(v5, 0);
        ptr->field_18 = v5;
        addr = &ptr->field_18;
        sub_f7d8d0(addr, v5);
        *((unsigned int *)&addr->padding_0[8]) = 1;
        return 1;
    }
    if (p)
    {
        p->field_2a4 = 0;
        return 0;
    }
    sub_f7db74();
}
```

## `FPSPlayer.<ActivateBulletTime>d__175.get_Current` — RVA `0xca156c`

- Decompiled symbol: `FPSPlayer_ActivateBulletTime_d__175_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long FPSPlayer_ActivateBulletTime_d__175_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `FPSPlayer.<ActivateBulletTime>d__175.Reset` — RVA `0xca1574`

- Decompiled symbol: `FPSPlayer_ActivateBulletTime_d__175_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f045d8;

void FPSPlayer_ActivateBulletTime_d__175_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f045d8));
}
```

## `FPSPlayer.<ActivateBulletTime>d__175.get_Current` — RVA `0xca15ac`

- Decompiled symbol: `FPSPlayer_ActivateBulletTime_d__175_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long FPSPlayer_ActivateBulletTime_d__175_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `FPSPlayer.<Missionfailed>d__186.Dispose` — RVA `0xca15b4`

- Decompiled symbol: `FPSPlayer_Missionfailed_d__186_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long FPSPlayer_Missionfailed_d__186_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `FPSPlayer.<Missionfailed>d__186.MoveNext` — RVA `0xca15b8`

- Decompiled symbol: `FPSPlayer_Missionfailed_d__186_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `356` bytes
- Result: `pseudocode`

```c
typedef struct struct_5 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_4 *field_20;
} struct_5;

typedef struct struct_4 {
    char padding_0[32];
    long long field_20;
} struct_4;

typedef struct struct_3 {
    char padding_0[20];
    unsigned int field_14;
    unsigned int field_18;
} struct_3;

typedef struct struct_1 {
    long long field_0;
} struct_1;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_3 *field_b8;
} struct_2;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1eee700;
extern struct_2 *g_1eefae8;
extern long long g_1ef2440;
extern long long g_1f082a0;
extern char g_1fab4b6;

unsigned int FPSPlayer_Missionfailed_d__186_MoveNext(struct_5 *ptr)
{
    long long v0;  // x20
    struct_4 *v1;  // x8
    unsigned long long v2;  // x0

    if (!(g_1fab4b6 & 1))
    {
        sub_f7d92c(&g_1eee700);
        sub_f7d92c(&g_1eefae8);
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c(&g_1f082a0);
        sub_f7d92c(")#");
        g_1fab4b6 = 1;
    }
    if (ptr->field_10 == 1)
    {
        v1 = ptr->field_20;
        ptr->field_10 = 4294967295;
        if (!v1)
            sub_f7db74();
        if (v1->field_20)
        {
            GameObject__SetActive(v1->field_20, 1, 0);
            v2 = PlayerPrefs__GetInt(g_1f0ee98, 0);
            PlayerPrefs__SetInt(g_1f0ee98, g_1eefae8->field_b8->field_14 + v2 + g_1eefae8->field_b8->field_18, 0);
            if (PlayerPrefs__GetInt(g_1f082a0, 0) != 1)
            {
                if (g_1eee700->field_b8->field_0)
                    AdsManager__Show_Interstitial(g_1eee700->field_b8->field_0, 0);
                else
                    sub_f7db74();
            }
        }
        else
        {
            sub_f7db74();
        }
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        v0 = sub_f7db70(g_1ef2440);
        WaitForSeconds__ctor(v0, 0);
        ptr->field_18 = v0;
        sub_f7d8d0(&ptr->field_18, v0);
        ptr->field_10 = 1;
        return 1;
    }
    return 0;
}
```

## `FPSPlayer.<Missionfailed>d__186.get_Current` — RVA `0xca171c`

- Decompiled symbol: `FPSPlayer_Missionfailed_d__186_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long FPSPlayer_Missionfailed_d__186_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `FPSPlayer.<Missionfailed>d__186.Reset` — RVA `0xca1724`

- Decompiled symbol: `FPSPlayer_Missionfailed_d__186_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f045e0;

void FPSPlayer_Missionfailed_d__186_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f045e0));
}
```

## `FPSPlayer.<Missionfailed>d__186.get_Current` — RVA `0xca175c`

- Decompiled symbol: `FPSPlayer_Missionfailed_d__186_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long FPSPlayer_Missionfailed_d__186_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
