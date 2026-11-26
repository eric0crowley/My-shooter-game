# Native pseudocode: LetsMap

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `LetsMap.Start` — RVA `0xc79a8c`

- Decompiled symbol: `LetsMap_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `384` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LetsMap_Recovered` matched 5 offsets against `LetsMap` metadata (confidence 1.00).

```c
typedef struct LetsMap_Recovered {
    char padding_0[32];
    long long ArrowPointerPrefab;
    long long ArrowPointer;
    long long CanvasName;
    unsigned long long Player;
    long long Distance;
} LetsMap_Recovered;

typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
    unsigned long long field_28;
    unsigned long long field_30;
    unsigned long long field_38;
    unsigned long long field_40;
} struct_0;

typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

typedef struct struct_4 {
    char padding_0[224];
    unsigned int field_e0;
} struct_4;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_1;

extern struct_1 *g_1ef0620;
extern struct_4 *g_1ef0c58;
extern long long g_1efd140;
extern long long g_1f00250;
extern long long g_1f0a280;
extern long long g_1f0bff0;
extern char g_1fab3cc;

void LetsMap_Start(struct_3 *ptr3)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    struct_3 *ptr;  // x20
    struct_3 *v16;  // x20
    long long v17;  // x1
    struct_3 *p;  // x0
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x0
    long long v11;  // x1
    struct_3 *addr;  // x20
    struct_3 *v13;  // x20
    long long v14;  // x0
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
    if (!(g_1fab3cc & 1))
    {
        sub_f7d92c(&g_1efd140);
        sub_f7d92c(&g_1ef0620);
        sub_f7d92c(&g_1f00250);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0bff0);
        sub_f7d92c(&g_1f0a280);
        g_1fab3cc = 1;
    }
    g_1ef0620->field_b8->field_0 = ptr3;
    sub_f7d8d0(g_1ef0620->field_b8, ptr3);
    if (GameObject__Find(g_1f0bff0, 0))
    {
        v10 = GameObject__get_transform();
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v11 = sub_112a07c(ptr3->field_20, v10, g_1f00250);
        addr = ptr3;
        addr->field_30 = v11;
        v13 = &addr->field_30;
        sub_f7d8d0(v13, v11);
        if (*((long long *)&v13->padding_0[0]))
        {
            v14 = Component__get_gameObject(*((long long *)&v13->padding_0[0]), 0);
            ptr = ptr3;
            ptr->field_28 = v14;
            v16 = &ptr->field_28;
            sub_f7d8d0(v16, v14);
            if (*((long long *)&v16->padding_0[8]))
            {
                v17 = sub_1231e2c(*((long long *)&v16->padding_0[8]), g_1efd140);
                p = ptr3;
                p->field_40 = v17;
                sub_f7d8d0((struct LetsMap_Recovered *)&p->field_40, v17);
                ptr3->field_38 = GameObject__Find(g_1f0a280, 0);
                sub_f7d8d0();
                return;
            }
        }
    }
    sub_f7db74();
}
```

## `LetsMap.Update` — RVA `0xc79c0c`

- Decompiled symbol: `LetsMap_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `568` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LetsMap_Recovered` matched 4 offsets against `LetsMap` metadata (confidence 0.80).

```c
typedef struct LetsMap_Recovered {
    char padding_0[40];
    unsigned long long ArrowPointer;
    long long CanvasName;
    long long Player;
    struct struct_3 *Distance;
    char padding_48[8];
    unsigned int field_50;
} LetsMap_Recovered;

typedef struct struct_4 {
    char padding_0[64];
    unsigned int field_40;
} struct_4;

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

extern long long g_1efcf68;
extern long long g_1f07670;
extern long long g_1f138a0;
extern char g_1fab3cd;
extern char g_1fab3e0;

void LetsMap_Update(struct_2 *ptr)
{
    unsigned long long v11;  // d13
    unsigned long long v12;  // d12
    long long v21;  // x20
    unsigned int v22;  // s2
    unsigned int v23;  // s8
    struct_4 *p;  // x0
    unsigned int v25;  // s9
    unsigned long long v26;  // 4102
    unsigned long v27;  // 4128
    unsigned long v28;  // 4128
    struct_0 **v29;  // x20
    unsigned long long v13;  // d11
    long long v31;  // x0
    unsigned long long v32;  // x0
    unsigned long long v33;  // x1
    struct_0 **v34;  // x0
    unsigned long long v35;  // x2
    unsigned long long v14;  // d10
    unsigned long long v15;  // d9
    unsigned long long v16;  // d8
    unsigned long long v17;  // x30
    unsigned long long v18;  // x21
    unsigned long long v19;  // x20
    unsigned long long v20;  // x19
    unsigned int v0;  // [bp-0x54]
    unsigned long long v1;  // [bp-0x50]
    unsigned long long v2;  // [bp-0x48]
    unsigned long long v3;  // [bp-0x40]
    unsigned long long v4;  // [bp-0x38]
    unsigned long long v5;  // [bp-0x30]
    unsigned long long v6;  // [bp-0x28]
    unsigned long long v7;  // [bp-0x20]
    unsigned long long v8;  // [bp-0x18]
    unsigned long long v9;  // [bp-0x10]
    unsigned long long v10;  // [bp-0x8]

    v1 = v11;
    v2 = v12;
    v3 = v13;
    v4 = v14;
    v5 = v15;
    v6 = v16;
    v7 = v17;
    v8 = v18;
    v9 = v19;
    v10 = v20;
    if (!(g_1fab3cd & 1))
    {
        sub_f7d92c(&g_1efcf68);
        sub_f7d92c(&g_1f138a0);
        sub_f7d92c(&g_1f07670);
        g_1fab3cd = 1;
    }
    v0 = 0;
    v21 = Camera__get_main(0);
    if (Component__get_transform(ptr, 0) && (Transform__get_position(), v21 && (Camera__WorldToScreenPoint(v21, 0), ptr->field_30)))
    {
        v23 = v22 + ptr->field_50;
        Transform__set_position(ptr->field_30, 0);
        p = sub_1231bc8(ptr, g_1efcf68);
        if (p && ptr->field_30 && (v25 = p->field_40, Component__get_gameObject(ptr->field_30, 0)))
        {
            v26 = (((CmpF(v25, 0.0) >> 5 & 3 | CmpF(v25, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v25, 0.0) >> 5 & 3 | CmpF(v25, 0.0) & 1) & (CmpF(v25, 0.0) >> 5 & 3 | CmpF(v25, 0.0) & 1) >> 1 & 1);
            if ((char)(v26 * 0x10000000 >> 30))
            {
                v27 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v23, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v23, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v23, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v23, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v23, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v23, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                GameObject__SetActive();
                if (ptr->field_28)
                {
LABEL_1079d24:
                    GameObject__SetActive();
                    if (ptr->field_38)
                    {
                        v29 = ptr->field_40;
                        if (GameObject__get_transform(ptr->field_38, 0))
                        {
                            Transform__get_position();
                            if (Component__get_transform(ptr, 0))
                            {
                                Transform__get_position();
                                if (!g_1fab3e0)
                                {
                                    sub_f7d92c("_F");
                                    g_1fab3e0 = 1;
                                }
                                if (!g_1ef07e8->field_e0)
                                    sub_f7da5c(g_1ef07e8);
                                v0 = [D] unsupported_Iop_SqrtF32();
                                v31 = Single__ToString(&v0, g_1f07670, 0);
                                v32 = String__Concat(v31, g_1f138a0, 0);
                                if (v29)
                                {
                                    v33 = v32;
                                    v34 = v29;
                                    v35 = *(v29)->field_5f0;
                                    *(v29)->field_5e8();
                                }
                            }
                        }
                    }
                }
            }
            else
            {
                v28 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v23, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v23, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v23, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v23, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v23, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v23, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v28)
                    goto LABEL_1079d24;
                else
                    goto LABEL_1079d24;
            }
        }
    }
    sub_f7db74();
}
```

## `LetsMap.ctor` — RVA `0xc79e44`

- Decompiled symbol: `LetsMap_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long LetsMap_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
