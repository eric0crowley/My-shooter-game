# Native pseudocode: BuiltinDebugViewsComponent.ArrowArray

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BuiltinDebugViewsComponent.ArrowArray.ctor` — RVA `0xccffb4`

- Decompiled symbol: `BuiltinDebugViewsComponent_ArrowArray_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long BuiltinDebugViewsComponent_ArrowArray_ctor(void)
{
    long long v0;  // x0

    v0 = Object__ctor();
    return Object__ctor();
}
```

## `BuiltinDebugViewsComponent.ArrowArray.Release` — RVA `0xccffbc`

- Decompiled symbol: `BuiltinDebugViewsComponent_ArrowArray_Release`
- Metadata signature: `public void Release() { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

void BuiltinDebugViewsComponent_ArrowArray_Release(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    GraphicsUtils__Destroy(ptr->field_10, 0);
    ptr->field_10 = 0;
    sub_f7d8d0();
    return;
}
```

## `BuiltinDebugViewsComponent.ArrowArray.BuildMesh` — RVA `0xccffe4`

- Decompiled symbol: `BuiltinDebugViewsComponent_ArrowArray_BuildMesh`
- Metadata signature: `public void BuildMesh(int columns, int rows) { }`
- Native interval: `1080` bytes
- Result: `pseudocode`
- Heuristic layout hint: `BuiltinDebugViewsComponent_ArrowArray_Recovered` matched 3 offsets against `BuiltinDebugViewsComponent.ArrowArray` metadata (confidence 1.00).

```c
typedef struct struct_7 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_7;

typedef struct BuiltinDebugViewsComponent_ArrowArray_Recovered {
    char padding_0[16];
    unsigned long long k__BackingField;
    unsigned int k__BackingField;
    unsigned int k__BackingField;
} BuiltinDebugViewsComponent_ArrowArray_Recovered;

typedef struct struct_6 {
    char padding_0[16];
    long long field_10;
    int field_18;
    int field_1c;
} struct_6;

typedef struct struct_3 {
    char padding_0[112];
    long long field_70;
} struct_3;

typedef struct struct_0 {
    char padding_0[112];
    long long field_70;
} struct_0;

typedef struct struct_4 {
    char padding_0[192];
    struct struct_3 *field_c0;
} struct_4;

typedef struct struct_1 {
    char padding_0[192];
    struct struct_0 *field_c0;
} struct_1;

typedef struct struct_5 {
    char padding_0[32];
    struct struct_4 *field_20;
} struct_5;

typedef struct struct_2 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_2;

extern long long g_1eed938;
extern long long g_1eed940;
extern long long g_1eee410;
extern long long g_1ef0868;
extern long long g_1ef8c68;
extern struct_5 *g_1ef8c70;
extern long long g_1ef8c98;
extern struct_2 *g_1ef8ca0;
extern char g_1fab5b1;

unsigned long long BuiltinDebugViewsComponent_ArrowArray_BuildMesh(struct_6 *ptr4, int a1, int a2)
{
    void* ptr8;  // x0
    unsigned int flag;  // w8
    unsigned int v13;  // s0
    unsigned int v14;  // s1
    unsigned int v15;  // s2
    unsigned long long v16;  // x9
    unsigned long v17;  // x10
    unsigned int ptr5[11];  // x9
    unsigned long long v19;  // x8
    unsigned long v20;  // x10
    unsigned int ptr6[10];  // x8
    void* ptr7;  // x24
    void* ptr;  // x24
    unsigned long v23;  // x9
    unsigned long idx7;  // x8
    long long v25;  // x26
    struct_6 *v26;  // x25
    unsigned long long v27;  // x0
    unsigned int v7;  // w26
    struct_7 *p;  // x22
    struct_8 *addr;  // x23
    int v10;  // w25
    unsigned long i;  // x19
    void* cur;  // x29
    unsigned int v0;  // [bp-0x9c]
    int v1;  // [bp-0x84]
    char *v2;  // [bp-0x60]
    char v3;  // [bp+0x0]

    v2 = &v3;
    if (!(g_1fab5b1 & 1))
    {
        sub_f7d92c("a(");
        sub_f7d92c(&g_1ef8ca0);
        sub_f7d92c(&g_1ef8c70);
        sub_f7d92c(&g_1ef8c68);
        sub_f7d92c(&g_1ef8c98);
        sub_f7d92c(&g_1eed940);
        sub_f7d92c(&g_1eed938);
        sub_f7d92c(&g_1ef0868);
        sub_f7d92c(&g_1eee410);
        g_1fab5b1 = 1;
    }
    ptr8 = sub_f7d9d4(g_1eee410, 6);
    if (ptr8)
    {
        flag = (int)ptr8[24];
        ptr = ptr8;
        if (!flag)
            sub_f7db7c(ptr8);
        *((unsigned long *)&ptr[32]) = 0;
        *((unsigned int *)&ptr[40]) = 0;
        if (flag == 1)
            sub_f7db7c(ptr8);
        *((unsigned int *)&ptr[52]) = 0;
        *((unsigned long *)&ptr[44]) = 0x3f80000000000000;
        if (flag <= 2)
            sub_f7db7c(ptr8);
        *((unsigned long *)&ptr[56]) = 0x3f80000000000000;
        *((unsigned int *)&ptr[64]) = 0;
        if (flag == 3)
            sub_f7db7c(ptr8);
        *((unsigned int *)&ptr[76]) = 0;
        *((unsigned long *)&ptr[68]) = 0x3f800000bf800000;
        if (flag <= 4 || !((*((unsigned long *)&ptr[80]) = 0x3f80000000000000, *((unsigned int *)&ptr[88]) = 0, flag != 5)))
            goto LABEL_10d0418;
        *((unsigned long *)&ptr[92]) = 0x3f8000003f800000;
        *((unsigned int *)&ptr[100]) = 0;
        v7 = (a2 * a1 * 6 | a2 * a1 * 3 >> 31) & 4294967294;
        p = sub_f7db70(g_1eed940);
        sub_14dc484(p, v7, g_1ef8c98);
        addr = sub_f7db70(g_1eed938);
        v0 = v7;
        ptr8 = sub_14d9eb8(addr, v7, g_1ef8c68);
        if (a2 >= 1)
        {
            v1 = 0;
            do
            {
                if (a1 < 1)
                    continue;
                v10 = 0;
                do
                {
                    i = 0;
                    cur = ptr + 40;
                    do
                    {
                        if ((int)ptr[24] <= i)
                            sub_f7db7c(ptr8);
                        if (!p)
                            goto LABEL_10d0414;
                        else
                            goto LABEL_10d0204;
LABEL_10d0204:
                        v13 = (int)cur[8];
                        v14 = (int)cur[4];
                        v15 = *((int *)cur);
                        v16 = p->field_10;
                        p->field_1c = p->field_1c + 1;
                        if (!v16)
                            goto LABEL_10d0414;
                        v17 = p->field_18;
                        if (*((int *)(v16 + 24)) > (unsigned int)v17)
                        {
                            ptr5 = v16 + 12 * v17;
                            p->field_18 = (unsigned int)v17 + 1;
                            ptr5[8] = v13;
                            ptr5[9] = v14;
                            ptr5[10] = v15;
                        }
                        else
                        {
                            ptr8 = sub_14dcca0(p, g_1ef8ca0->field_20->field_c0->field_70);
                        }
                        if (!addr || !((v19 = addr->field_10, addr->field_1c = addr->field_1c + 1, v19)))
                            goto LABEL_10d0414;
                        v20 = addr->field_18;
                        if (*((int *)(v19 + 24)) > (unsigned int)v20)
                        {
                            ptr6 = v19 + v20 * 8;
                            addr->field_18 = (unsigned int)v20 + 1;
                            ptr6[8] = (v10 + 0x3f000000) / a1;
                            ptr6[9] = (v1 + 0x3f000000) / a2;
                        }
                        else
                        {
                            ptr8 = sub_14da6a8(addr, g_1ef8c70->field_20->field_c0->field_70);
                        }
                        i += 1;
                        cur += 12;
                    } while (i != 6);
                } while ((v10 = (int)(v10 + 1), v10 != a1));
            } while ((v1 = (int)(v1 + 1), v1 != a2));
        }
        ptr8 = sub_f7d9d4(g_1eee1f8, v0);
        ptr7 = ptr8;
        if (v0 < 1)
        {
LABEL_10d0340:
            v25 = sub_f7db70(g_1ef0868);
            Mesh__ctor(v25, 0);
            if (v25)
            {
                Object__set_hideFlags(v25, 52, 0);
                ptr4->field_10 = v25;
                v26 = &ptr4->field_10;
                sub_f7d8d0(v26, v25);
                if (*((long long *)&v26->padding_0[0]))
                {
                    Mesh__SetVertices(*((long long *)&v26->padding_0[0]), p, 0);
                    if (*((long long *)&v26->padding_0[0]))
                    {
                        Mesh__SetUVs(*((long long *)&v26->padding_0[0]), 0, addr, 0);
                        if (*((long long *)&v26->padding_0[0]))
                        {
                            Mesh__SetIndices(*((long long *)&v26->padding_0[0]), ptr7, 3, 0, 0);
                            if (*((long long *)&v26->padding_0[0]))
                            {
                                v27 = Mesh__UploadMeshData(*((long long *)&v26->padding_0[0]), 1, 0);
                                ptr4->field_18 = a1;
                                ptr4->field_1c = a2;
                                return v27;
                            }
                        }
                    }
                }
            }
        }
        else if (ptr7)
        {
            v23 = (int)ptr7[24];
            idx7 = 0;
            do
            {
                if (v23 <= idx7)
                    sub_f7db7c(ptr8);
            } while ((*((unsigned int *)(32 + (char *)ptr7 + 4 * idx7)) = (unsigned int)idx7, idx7 = (unsigned long)(idx7 + 1), (unsigned long long)v0 != idx7));
            goto LABEL_10d0340;
        }
    }
LABEL_10d0414:
    ptr8 = sub_f7db74();
LABEL_10d0418:
    sub_f7db7c(ptr8);
}
```

## `BuiltinDebugViewsComponent.ArrowArray.get_mesh` — RVA `0xcd0634`

- Decompiled symbol: `BuiltinDebugViewsComponent_ArrowArray_get_mesh`
- Metadata signature: `public Mesh get_mesh() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

long long BuiltinDebugViewsComponent_ArrowArray_get_mesh(struct_0 *a0)
{
    return a0->field_10;
}
```

## `BuiltinDebugViewsComponent.ArrowArray.set_mesh` — RVA `0xcd063c`

- Decompiled symbol: `BuiltinDebugViewsComponent_ArrowArray_set_mesh`
- Metadata signature: `private void set_mesh(Mesh value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

long long BuiltinDebugViewsComponent_ArrowArray_set_mesh(struct_0 *ptr, unsigned long a1)
{
    long long v0;  // x0

    ptr->field_10 = a1;
    v0 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `BuiltinDebugViewsComponent.ArrowArray.get_columnCount` — RVA `0xcd0644`

- Decompiled symbol: `BuiltinDebugViewsComponent_ArrowArray_get_columnCount`
- Metadata signature: `public int get_columnCount() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

int BuiltinDebugViewsComponent_ArrowArray_get_columnCount(struct_0 *a0)
{
    return a0->field_18;
}
```

## `BuiltinDebugViewsComponent.ArrowArray.set_columnCount` — RVA `0xcd064c`

- Decompiled symbol: `BuiltinDebugViewsComponent_ArrowArray_set_columnCount`
- Metadata signature: `private void set_columnCount(int value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

struct_0 * BuiltinDebugViewsComponent_ArrowArray_set_columnCount(struct_0 *ptr, unsigned int a1)
{
    ptr->field_18 = a1;
    return ptr;
}
```

## `BuiltinDebugViewsComponent.ArrowArray.get_rowCount` — RVA `0xcd0654`

- Decompiled symbol: `BuiltinDebugViewsComponent_ArrowArray_get_rowCount`
- Metadata signature: `public int get_rowCount() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[28];
    unsigned int field_1c;
} struct_0;

int BuiltinDebugViewsComponent_ArrowArray_get_rowCount(struct_0 *a0)
{
    return a0->field_1c;
}
```

## `BuiltinDebugViewsComponent.ArrowArray.set_rowCount` — RVA `0xcd065c`

- Decompiled symbol: `BuiltinDebugViewsComponent_ArrowArray_set_rowCount`
- Metadata signature: `private void set_rowCount(int value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[28];
    unsigned int field_1c;
} struct_0;

struct_0 * BuiltinDebugViewsComponent_ArrowArray_set_rowCount(struct_0 *ptr, unsigned int a1)
{
    ptr->field_1c = a1;
    return ptr;
}
```
