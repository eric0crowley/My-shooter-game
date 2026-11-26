# Native pseudocode: ReconfigurePrefab

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ReconfigurePrefab.Start` — RVA `0xcac87c`

- Decompiled symbol: `ReconfigurePrefab_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `296` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ReconfigurePrefab_Recovered` matched 5 offsets against `ReconfigurePrefab` metadata (confidence 1.00).

```c
typedef struct struct_0 {
    char padding_0[48];
    unsigned long long field_30;
} struct_0;

typedef struct ReconfigurePrefab_Recovered {
    char padding_0[40];
    unsigned long long FPSPlayerComponent;
    struct struct_1 *CameraControlComponent;
    char padding_38[8];
    long long MainCamera;
    long long WeaponObj;
    char padding_50[24];
    long long WeaponBehaviorComponents;
} ReconfigurePrefab_Recovered;

typedef struct struct_3 {
    char padding_0[96];
    unsigned long long field_60;
} struct_3;

typedef struct struct_1 {
    char padding_0[48];
    long long field_30;
} struct_1;

extern long long g_1efcf38;
extern long long g_1efeb68;
extern long long g_1efedc0;
extern char g_1fab4c4;

void ReconfigurePrefab_Start(struct_2 *ptr4)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    struct_2 *ptr;  // x20
    struct_2 *v14;  // x20
    long long v15;  // x0
    struct_2 *p;  // x20
    struct_2 *v17;  // x20
    struct_3 *index;  // x0
    unsigned long long v5;  // x19
    struct_0 *v6;  // x0
    struct_2 *addr;  // x20
    struct_2 *v8;  // x20
    long long v9;  // x0
    struct_2 *ptr3;  // x20
    struct_2 *v11;  // x20
    unsigned long v12;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab4c4 & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efeb68);
        sub_f7d92c(&g_1efedc0);
        g_1fab4c4 = 1;
    }
    if (Camera__get_main(0))
    {
        v6 = sub_1231bc8();
        addr = ptr4;
        addr->field_30 = v6;
        v8 = &addr->field_30;
        sub_f7d8d0(v8, v6);
        if (*((long long *)&v8->padding_0[0]) && Component__get_transform(*((long long *)&v8->padding_0[0]), 0))
        {
            v9 = Component__get_gameObject();
            ptr3 = ptr4;
            ptr3->field_40 = v9;
            v11 = &ptr3->field_40;
            sub_f7d8d0(v11, v9);
            if (*((long long *)&v11->padding_0[16]))
            {
                v12 = *((long long *)(*((long long *)&v11->padding_0[16]) + 48));
                ptr = ptr4;
                ptr->field_48 = v12;
                v14 = &ptr->field_48;
                sub_f7d8d0(v14, v12);
                if (*((long long *)&v14->padding_0[0]))
                {
                    v15 = sub_1249ec4(*((long long *)&v14->padding_0[0]), 1, g_1efedc0);
                    p = ptr4;
                    p->field_68 = v15;
                    v17 = &p->field_68;
                    sub_f7d8d0(v17, v15);
                    if (v17->field_28)
                    {
                        index = sub_1249224(v17->field_28, g_1efeb68);
                        if (index)
                        {
                            ptr4->field_28 = index->field_60;
                            sub_f7d8d0();
                            return;
                        }
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `ReconfigurePrefab.Update` — RVA `0xcac9a4`

- Decompiled symbol: `ReconfigurePrefab_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `788` bytes
- Result: `pseudocode`

```c
typedef struct struct_8 {
    char padding_0[96];
    struct struct_6 *field_60;
} struct_8;

typedef struct struct_6 {
    char padding_0[576];
    unsigned long long field_240;
} struct_6;

typedef struct struct_4 {
    char padding_0[24];
    unsigned int field_18;
} struct_4;

typedef struct struct_5 {
    char padding_0[1336];
    char field_538;
    char padding_539[535];
    unsigned long long field_750;
} struct_5;

typedef struct struct_7 {
    char padding_0[1336];
    char field_538;
    char padding_539[535];
    unsigned long long field_750;
} struct_7;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efeb60;
extern char g_1fab4c5;

void* ReconfigurePrefab_Update(void* ptr)
{
    void* v0;  // x0
    void* v1;  // x0
    unsigned long v10;  // x20
    void* v11;  // x0
    long long v12;  // x20
    unsigned int v13;  // w0
    struct_4 *p;  // x21
    unsigned int v15;  // w8
    unsigned int j;  // w22
    struct_7 *ptr4;  // x24
    unsigned long v18;  // x0
    long long v19;  // x0
    void* v2;  // x0
    long long v3;  // x20
    unsigned int v4;  // w0
    unsigned long v5;  // x0
    struct_4 *addr;  // x21
    unsigned int v7;  // w8
    unsigned int i;  // w22
    struct_5 *ptr3;  // x24

    v0 = ptr;
    if (!(g_1fab4c5 & 1))
    {
        sub_f7d92c(&g_1efeb60);
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab4c5 = 1;
        v0 = v1;
    }
    v2 = v0;
    if ((char)ptr[32])
    {
        if (!(char)ptr[120])
        {
            v3 = Camera__get_main(0);
            v4 = LayerMask__op_Implicit((int)ptr[112], 0);
            if (v3)
            {
                Camera__set_cullingMask(v3, v4, 0);
                if (Camera__get_main(0))
                {
                    Camera__set_nearClipPlane();
                    if ((long long)ptr[72] && GameObject__get_transform((long long)ptr[72], 0))
                    {
                        Transform__set_localScale();
                        if ((long long)ptr[40] && *((long long *)((long long)ptr[40] + 96)) && *((long long *)(*((long long *)((long long)ptr[40] + 96)) + 576)))
                        {
                            v5 = Collider__set_enabled(*((long long *)(*((long long *)((long long)ptr[40] + 96)) + 576)), 0, 0);
                            addr = (long long)ptr[104];
                            if (addr)
                            {
                                v7 = addr->field_18;
                                if (v7 >= 1)
                                {
                                    i = 0;
                                    do
                                    {
                                        if (v7 <= i)
                                            sub_f7db7c(v5);
                                        ptr3 = *((long long *)&addr[1].padding_0[4 + 8 * i]);
                                        if (!ptr3)
                                            sub_f7db7c(sub_f7db74());
                                        v10 = ptr3->field_750;
                                        ptr3->field_538 = (char)ptr[100];
                                        if (!g_1ef0c58->field_e0)
                                            sub_f7da5c(g_1ef0c58);
                                        v5 = Object__op_Implicit(v10, 0);
                                        if (((char)v5 & 1))
                                        {
                                            if (ptr3->field_750)
                                                v5 = Light__set_range(ptr3->field_750, 0);
                                            else
                                                sub_f7db7c(sub_f7db74());
                                        }
                                        v7 = addr->field_18;
                                        i += 1;
                                    } while (i < v7);
                                }
                                if ((long long)ptr[56] && sub_1249224((long long)ptr[56], g_1efeb60))
                                {
                                    Camera__set_nearClipPlane();
                                    if ((long long)ptr[56])
                                    {
                                        v11 = GameObject__SetActive((long long)ptr[56], 1, 0);
                                        *((unsigned short *)&ptr[120]) = 1;
                                        return v11;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        else
        {
            return v2;
        }
    }
    else
    {
        if ((char)ptr[121])
            return v2;
        v12 = Camera__get_main(0);
        v13 = LayerMask__op_Implicit((int)ptr[116], 0);
        if (v12)
        {
            Camera__set_cullingMask(v12, v13, 0);
            if (Camera__get_main(0))
            {
                Camera__set_nearClipPlane();
                if ((long long)ptr[72] && GameObject__get_transform((long long)ptr[72], 0))
                {
                    Transform__set_localScale();
                    if ((long long)ptr[40] && *((long long *)((long long)ptr[40] + 96)) && *((long long *)(*((long long *)((long long)ptr[40] + 96)) + 576)))
                    {
                        v5 = Collider__set_enabled(*((long long *)(*((long long *)((long long)ptr[40] + 96)) + 576)), 1, 0);
                        p = (long long)ptr[104];
                        if (p)
                        {
                            v15 = p->field_18;
                            if (v15 >= 1)
                            {
                                j = 0;
                                do
                                {
                                    if (v15 <= j)
                                        sub_f7db7c(v5);
                                    ptr4 = *((long long *)&p[1].padding_0[4 + 8 * j]);
                                    if (!ptr4)
                                        sub_f7db7c(sub_f7db74());
                                    ptr4->field_538 = 0;
                                    if (!g_1ef0c58->field_e0)
                                        sub_f7da5c(g_1ef0c58);
                                    v5 = Object__op_Implicit(ptr4->field_750, 0);
                                    if (((char)v5 & 1))
                                    {
                                        if (ptr4->field_750)
                                            v5 = Light__set_range(ptr4->field_750, 0);
                                        else
                                            sub_f7db7c(sub_f7db74());
                                    }
                                    v15 = p->field_18;
                                    j += 1;
                                } while (j < v15);
                            }
                            v18 = (long long)ptr[56];
                            *((unsigned short *)&ptr[120]) = 0x100;
                            if (v18)
                            {
                                v19 = GameObject__SetActive();
                                return GameObject__SetActive();
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db7c(sub_f7db74());
}
```

## `ReconfigurePrefab.ctor` — RVA `0xcaccb8`

- Decompiled symbol: `ReconfigurePrefab_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `44` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ReconfigurePrefab_Recovered` matched 4 offsets against `ReconfigurePrefab` metadata (confidence 1.00).

```c
typedef struct ReconfigurePrefab_Recovered {
    char padding_0[32];
    char TwoCameraSetup;
    char padding_21[47];
    uint128_t twoCamWeaponScale;
    unsigned int weaponCamNearPlane;
    char shadeWeaponByRaycast;
} ReconfigurePrefab_Recovered;

long long ReconfigurePrefab_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_20 = 1;
    ptr->field_60 = 1055286886;
    ptr->field_50 = 0x3e6147ae3ca3d70a3f80000041a00000;
    ptr->field_64 = 1;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
