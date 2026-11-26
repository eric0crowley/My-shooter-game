# Native pseudocode: BindingDescriptionList

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BindingDescriptionList.ctor` — RVA `0xc5d660`

- Decompiled symbol: `BindingDescriptionList_ctor`
- Metadata signature: `public void .ctor(BindingDescription.BindingType typeMask, bool addUnusedBindings, int axisInputSourceMask, BindingDescriptionList.NameFormatter menuNameFormatter) { }`
- Native interval: `180` bytes
- Result: `pseudocode`
- Heuristic layout hint: `BindingDescriptionList_Recovered` matched 4 offsets against `BindingDescriptionList` metadata (confidence 1.00).

```c
typedef struct BindingDescriptionList_Recovered {
    char padding_0[40];
    unsigned int typeMask;
    char addUnusedBindings;
    char padding_2d[3];
    unsigned int axisInputSourceMask;
    char padding_34[4];
    long long menuNameFormatter;
} BindingDescriptionList_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eed568;
extern long long g_1ef7768;
extern char g_1fab2d1;

long long BindingDescriptionList_ctor(struct_1 *p, unsigned int a1, char a2, unsigned int a3, long long a4)
{
    struct_1 *ptr;  // x21
    unsigned long v1;  // x0

    if (!(g_1fab2d1 & 1))
    {
        sub_f7d92c(&g_1ef7768);
        sub_f7d92c(&g_1eed568);
        g_1fab2d1 = 1;
    }
    if (!g_1eed568->field_e0)
        sub_f7da5c(g_1eed568);
    sub_1443a40(p, 16, g_1ef7768);
    p->field_38 = a4;
    ptr = &p->field_38;
    *((unsigned int *)&ptr->padding_0[16]) = a1;
    ptr->padding_0[12] = a2 & 1;
    v1 = sub_f7d8d0(ptr, a4);
    *((unsigned int *)&ptr->padding_0[8]) = a3;
    return v1;
}
```

## `BindingDescriptionList.Setup` — RVA `0xc5d714`

- Decompiled symbol: `BindingDescriptionList_Setup`
- Metadata signature: `public void Setup(BindingDescription.BindingType typeMask, bool addUnusedBindings, int axisInputSourceMask, BindingDescriptionList.NameFormatter menuNameFormatter) { }`
- Native interval: `60` bytes
- Result: `pseudocode`
- Heuristic layout hint: `BindingDescriptionList_Recovered` matched 4 offsets against `BindingDescriptionList` metadata (confidence 1.00).

```c
typedef struct BindingDescriptionList_Recovered {
    char padding_0[40];
    unsigned int typeMask;
    char addUnusedBindings;
    char padding_2d[3];
    unsigned int axisInputSourceMask;
    char padding_34[4];
    long long menuNameFormatter;
} BindingDescriptionList_Recovered;

long long BindingDescriptionList_Setup(struct_0 *p, unsigned int a1, char a2, unsigned int a3, long long a4)
{
    struct_0 *ptr;  // x20
    unsigned long v1;  // x0

    p->field_38 = a4;
    ptr = &p->field_38;
    *((unsigned int *)&ptr->padding_0[16]) = a1;
    ptr->padding_0[12] = a2 & 1;
    v1 = sub_f7d8d0(ptr, a4);
    *((unsigned int *)&ptr->padding_0[8]) = a3;
    return v1;
}
```

## `BindingDescriptionList.Add` — RVA `0xc5d750`

- Decompiled symbol: `BindingDescriptionList_Add`
- Metadata signature: `public void Add(InputBindingBase binding, string name, string menuPath, Object undoObject) { }`
- Native interval: `848` bytes
- Result: `pseudocode`

```c
typedef struct struct_7 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
    char padding_131[151];
    struct struct_8 *field_1c8;
    unsigned long long field_1d0;
} struct_7;

typedef struct struct_13 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
    char padding_131[151];
    struct struct_14 *field_1c8;
    unsigned long long field_1d0;
} struct_13;

typedef struct struct_12 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
    char padding_20[8];
    unsigned int field_28;
    char padding_2c[12];
    struct struct_10 *field_38;
} struct_12;

typedef struct struct_15 {
    char padding_0[24];
    struct struct_16 *field_18;
    char padding_20[8];
    unsigned long long field_28;
    char padding_30[16];
    unsigned long long field_40;
} struct_15;

typedef struct struct_9 {
    char padding_0[32];
    uint128_t field_20;
    uint128_t field_30;
    uint128_t field_40;
    unsigned long long field_50;
} struct_9;

typedef struct struct_8 {
    unsigned long long field_0;
} struct_8;

typedef struct struct_14 {
    unsigned long long field_0;
} struct_14;

typedef struct struct_10 {
    char padding_0[24];
    struct struct_11 *field_18;
    char padding_20[8];
    unsigned long long field_28;
    char padding_30[16];
    unsigned long long field_40;
} struct_10;

typedef struct struct_16 {
    unsigned long long field_0;
} struct_16;

typedef struct struct_11 {
    unsigned long long field_0;
} struct_11;

typedef struct struct_3 {
    char padding_0[112];
    long long field_70;
} struct_3;

typedef struct struct_4 {
    char padding_0[192];
    struct struct_3 *field_c0;
} struct_4;

typedef struct struct_5 {
    char padding_0[32];
    struct struct_4 *field_20;
} struct_5;

typedef struct struct_2 {
    char padding_0[304];
    char field_130;
} struct_2;

extern struct_2 *g_1eef6e0;
extern struct_5 *g_1ef7770;
extern long long g_1f075e0;
extern char g_1fab2d2;

void BindingDescriptionList_Add(struct_12 *ptr, struct_7 **ptr3, long long a2, long long a3, unsigned long a4)
{
    unsigned long long v26;  // x30
    unsigned long long v27;  // x28
    unsigned long long v36;  // x19
    struct_13 *ptr4;  // x8
    unsigned int v38;  // w9
    unsigned long v39;  // x11
    unsigned int v40;  // w25
    unsigned int v41;  // w28
    unsigned long v42;  // x11
    unsigned long v43;  // x11
    unsigned long v44;  // x11
    struct_15 *addr;  // x8
    unsigned long long v28;  // x27
    long long v46;  // x24
    unsigned long v47;  // x0
    unsigned long v48;  // x3
    struct_7 **v49;  // x1
    long long v50;  // x2
    unsigned long v51;  // 4124
    unsigned int v52;  // w8
    unsigned long v53;  // x8
    unsigned long v54;  // x9
    struct_9 *p;  // x8
    unsigned long long v29;  // x26
    unsigned long long v56;  // x0
    unsigned long long v57;  // x3
    struct_7 **v58;  // x0
    struct_12 *v59;  // x1
    unsigned long v60;  // x4
    unsigned long v61;  // x2
    unsigned long long v30;  // x25
    unsigned long long v31;  // x24
    unsigned long long v32;  // x23
    unsigned long long v33;  // x22
    unsigned long long v34;  // x21
    unsigned long long v35;  // x20
    unsigned int v0;  // [bp-0x120], Other Possible Types: uint128_t
    long long v1;  // [bp-0x118]
    int v2;  // [bp-0x110], Other Possible Types: uint128_t
    int v3;  // [bp-0x100], Other Possible Types: uint128_t
    unsigned long v4;  // [bp-0xf0], Other Possible Types: unsigned long long
    int v5;  // [bp-0xe0]
    int v6;  // [bp-0xd0]
    int v7;  // [bp-0xc0]
    unsigned long v8;  // [bp-0xb0]
    char v9;  // [bp-0xa0]
    int v10;  // [bp-0x90]
    int v11;  // [bp-0x80]
    unsigned long v12;  // [bp-0x70]
    char *v13;  // [bp-0x60]
    unsigned long long v14;  // [bp-0x58]
    unsigned long long v15;  // [bp-0x50]
    unsigned long long v16;  // [bp-0x48]
    unsigned long long v17;  // [bp-0x40]
    unsigned long long v18;  // [bp-0x38]
    unsigned long long v19;  // [bp-0x30]
    unsigned long long v20;  // [bp-0x28]
    unsigned long long v21;  // [bp-0x20]
    unsigned long long v22;  // [bp-0x18]
    unsigned long long v23;  // [bp-0x10]
    unsigned long long v24;  // [bp-0x8]
    char v25;  // [bp+0x0]

    v13 = &v25;
    v14 = v26;
    v15 = v27;
    v16 = v28;
    v17 = v29;
    v18 = v30;
    v19 = v31;
    v20 = v32;
    v21 = v33;
    v22 = v34;
    v23 = v35;
    v24 = v36;
    if (!(g_1fab2d2 & 1))
    {
        sub_f7d92c("g.");
        sub_f7d92c("y7");
        sub_f7d92c(&g_1eef6e0);
        sub_f7d92c(&g_1ef7770);
        sub_f7d92c("7H");
        sub_f7d92c(&g_1f075e0);
        g_1fab2d2 = 1;
    }
    v4 = 0;
    v2 = 0;
    v3 = 0;
    v0 = 0;
    if (ptr3)
    {
        ptr4 = *(ptr3);
        v38 = ptr4->field_130;
        v39 = g_1eee9f8->field_130;
        if (v38 < (unsigned int)v39 || *((long long *)(ptr4->field_c8 + v39 * 8 - 8)) != g_1eee9f8)
        {
            v42 = g_1eef590->field_130;
            if (v38 < (unsigned int)v42 || *((long long *)(ptr4->field_c8 + v42 * 8 - 8)) != g_1eef590)
            {
                v43 = g_1eef6e0->field_130;
                if (v38 < (unsigned int)v43 || *((long long *)(ptr4->field_c8 + v43 * 8 - 8)) != g_1eef6e0)
                {
                    v44 = g_1ef0a78->field_130;
                    if (v38 < (unsigned int)v44 || *((long long *)(ptr4->field_c8 + v44 * 8 - 8)) != g_1ef0a78)
                        goto LABEL_105d8a8;
                    v40 = 0;
                    v41 = 64;
                }
                else
                {
                    v40 = 0;
                    v41 = 32;
                }
            }
            else
            {
                v40 = 0;
                v41 = 1;
            }
        }
        else
        {
            v40 = 0;
            v41 = 2;
        }
    }
    else
    {
LABEL_105d8a8:
        v41 = 127;
        v40 = 1;
    }
    addr = ptr->field_38;
    v46 = a2;
    if (addr)
    {
        v47 = addr->field_40;
        v48 = addr->field_28;
        v49 = ptr3;
        v50 = a2;
        addr->field_18();
    }
    v51 = arm64g_calculate_condition(9, (unsigned long long)(v41 & ~(ptr->field_28)), 0, 0);
    if ((char)v51)
        v52 = 0;
    else
        v52 = 1;
    if (!(((char)v40 | (char)v52) & 1))
    {
        v4 = 0;
        v2 = 0;
        v3 = 0;
        v0 = 0;
        v0 = v41;
        v1 = a2;
        sub_f7d8d0(&v0 | 8, a2);
        *((long long *)&v2) = v46;
        sub_f7d8d0(&v2, v46);
        *((long long *)&(&v2)[8]) = a3;
        sub_f7d8d0(&v2 - 8, a3);
        v4 = a4;
        sub_f7d8d0(&v4, a4);
        *((struct_7 ***)&v3) = ptr3;
        sub_f7d8d0(&v3, ptr3);
        memcpy(&v5, &v0, 16);
        v6 = v2;
        v7 = v3;
        v8 = v4;
        v53 = ptr->field_10;
        ptr->field_1c = ptr->field_1c + 1;
        if (!v53)
            goto LABEL_105da9c;
        v54 = ptr->field_18;
        if (*((int *)(v53 + 24)) > (unsigned int)v54)
        {
            ptr->field_18 = (unsigned int)v54 + 1;
            p = v53 + 56 * v54;
            p->field_50 = v8;
            *((void*)&p->field_30) = v6;
            *((void*)&p->field_40) = v7;
            *((void*)&p->field_20) = v5;
            sub_f7d8d0((struct struct_9 *)((char *)&p->field_20 + 8), 0);
        }
        else
        {
            memcpy(&v9, &v5, 16);
            v10 = v6;
            v11 = v7;
            v12 = v8;
            sub_1444334(ptr, &v9, g_1ef7770->field_20->field_c0->field_70);
        }
    }
    v56 = String__Concat(a3, v46, g_1f075e0, 0);
    if (ptr3)
    {
        v57 = v56;
        v58 = ptr3;
        v59 = ptr;
        v60 = *(ptr3)->field_1d0;
        v61 = a4;
        *(ptr3)->field_1c8();
    }
LABEL_105da9c:
    sub_f7db74();
}
```

## `BindingDescriptionList.Add` — RVA `0xc5daac`

- Decompiled symbol: `BindingDescriptionList_Add`
- Metadata signature: `public void Add(AxisBinding binding, InputRig.InputSource sourceType, string name, string menuPath, Object undoObject) { }`
- Native interval: `496` bytes
- Result: `pseudocode`

```c
typedef struct struct_5 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
    char padding_20[8];
    char field_28;
    char padding_29[7];
    unsigned int field_30;
    char padding_34[4];
    struct struct_3 *field_38;
} struct_5;

typedef struct struct_7 {
    char padding_0[24];
    struct struct_8 *field_18;
    char padding_20[8];
    unsigned long long field_28;
    char padding_30[16];
    unsigned long long field_40;
} struct_7;

typedef struct struct_6 {
    char padding_0[32];
    uint128_t field_20;
    uint128_t field_30;
    uint128_t field_40;
    unsigned long long field_50;
} struct_6;

typedef struct struct_3 {
    char padding_0[24];
    struct struct_4 *field_18;
    char padding_20[8];
    unsigned long long field_28;
    char padding_30[16];
    unsigned long long field_40;
} struct_3;

typedef struct struct_8 {
    unsigned long long field_0;
} struct_8;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

typedef struct struct_0 {
    char padding_0[112];
    long long field_70;
} struct_0;

typedef struct struct_1 {
    char padding_0[192];
    struct struct_0 *field_c0;
} struct_1;

typedef struct struct_2 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_2;

extern struct_2 *g_1ef7770;
extern char g_1fab2d3;

struct_5 * BindingDescriptionList_Add(struct_5 *ptr, long long a1, unsigned int a2, long long a3, long long a4, unsigned long a5)
{
    struct_5 *v15;  // x0
    struct_5 *v16;  // x0
    unsigned long v25;  // x9
    struct_6 *p;  // x8
    unsigned long v27;  // x0
    unsigned long v28;  // x0
    struct_5 *v17;  // x0
    struct_7 *addr;  // x8
    long long v19;  // x25
    unsigned long v20;  // x0
    unsigned long v21;  // x3
    long long v22;  // x1
    long long v23;  // x2
    unsigned long v24;  // x8
    unsigned int v0;  // [bp-0x120], Other Possible Types: uint128_t
    long long v1;  // [bp-0x118]
    int v2;  // [bp-0x110], Other Possible Types: uint128_t
    int v3;  // [bp-0x100], Other Possible Types: uint128_t
    unsigned long v4;  // [bp-0xf0], Other Possible Types: unsigned long long
    int v5;  // [bp-0xe0]
    int v6;  // [bp-0xd0]
    int v7;  // [bp-0xc0]
    unsigned long v8;  // [bp-0xb0]
    char v9;  // [bp-0xa0]
    int v10;  // [bp-0x90]
    int v11;  // [bp-0x80]
    unsigned long v12;  // [bp-0x70]
    char *v13;  // [bp-0x60]
    char v14;  // [bp+0x0]

    v13 = &v14;
    v15 = ptr;
    if (!(g_1fab2d3 & 1))
    {
        v16 = sub_f7d92c(&g_1ef7770);
        g_1fab2d3 = 1;
        v15 = v16;
    }
    v17 = v15;
    v4 = 0;
    v2 = 0;
    v3 = 0;
    v0 = 0;
    if (!(ptr->field_28 >> 1 & 1))
    {
        return v17;
    }
    else if (((char)(ptr->field_30 >> ((char)a2 & 31)) & 1))
    {
        addr = ptr->field_38;
        v19 = a3;
        if (addr)
        {
            v20 = addr->field_40;
            v21 = addr->field_28;
            v22 = a1;
            v23 = a3;
            addr->field_18();
        }
        v4 = 0;
        v2 = 0;
        v3 = 0;
        v0 = 0;
        v0 = 2;
        *((unsigned int *)&(&v3)[8]) = a2;
        v1 = a3;
        sub_f7d8d0(&v0 | 8, a3);
        *((long long *)&v2) = v19;
        sub_f7d8d0(&v2, v19);
        *((long long *)&(&v2)[8]) = a4;
        sub_f7d8d0(&v2 - 8, a4);
        v4 = a5;
        sub_f7d8d0(&v4, a5);
        *((long long *)&v3) = a1;
        sub_f7d8d0(&v3, a1);
        memcpy(&v5, &v0, 16);
        v6 = v2;
        v7 = v3;
        v8 = v4;
        v24 = ptr->field_10;
        ptr->field_1c = ptr->field_1c + 1;
        if (v24)
        {
            v25 = ptr->field_18;
            if (*((int *)(v24 + 24)) <= (unsigned int)v25)
            {
                memcpy(&v9, &v5, 16);
                v10 = v6;
                v11 = v7;
                v12 = v8;
                v28 = sub_1444334(ptr, &v9, g_1ef7770->field_20->field_c0->field_70);
                return sub_1444334(ptr, &v9, g_1ef7770->field_20->field_c0->field_70);
            }
            ptr->field_18 = (unsigned int)v25 + 1;
            p = v24 + 56 * v25;
            p->field_50 = v8;
            *((void*)&p->field_30) = v6;
            *((void*)&p->field_40) = v7;
            *((void*)&p->field_20) = v5;
            v27 = sub_f7d8d0((struct struct_6 *)((char *)&p->field_20 + 8), 0);
            return sub_f7d8d0((struct struct_6 *)((char *)&p->field_20 + 8), 0);
        }
        sub_f7db74();
    }
    else
    {
        return v17;
    }
}
```
