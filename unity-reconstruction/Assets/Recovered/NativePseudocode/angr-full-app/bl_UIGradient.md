# Native pseudocode: bl_UIGradient

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_UIGradient.get_BlendMode` — RVA `0xce8c44`

- Decompiled symbol: `bl_UIGradient_get_BlendMode`
- Metadata signature: `public bl_UIGradient.Blend get_BlendMode() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[44];
    unsigned int field_2c;
} struct_0;

int bl_UIGradient_get_BlendMode(struct_0 *a0)
{
    return a0->field_2c;
}
```

## `bl_UIGradient.set_BlendMode` — RVA `0xce8c4c`

- Decompiled symbol: `bl_UIGradient_set_BlendMode`
- Metadata signature: `public void set_BlendMode(bl_UIGradient.Blend value) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[44];
    unsigned int field_2c;
} struct_0;

void bl_UIGradient_set_BlendMode(struct_0 *ptr, unsigned int a1)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    ptr->field_2c = a1;
    BaseMeshEffect__get_graphic();
    if (!BaseMeshEffect__get_graphic())
        sub_f7db74();
    goto *((long long *)(*((long long *)BaseMeshEffect__get_graphic()) + 760));
}
```

## `bl_UIGradient.get_EffectGradient` — RVA `0xce8c78`

- Decompiled symbol: `bl_UIGradient_get_EffectGradient`
- Metadata signature: `public Gradient get_EffectGradient() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[64];
    unsigned long long field_40;
} struct_0;

long long bl_UIGradient_get_EffectGradient(struct_0 *a0)
{
    return a0->field_40;
}
```

## `bl_UIGradient.set_EffectGradient` — RVA `0xce8c80`

- Decompiled symbol: `bl_UIGradient_set_EffectGradient`
- Metadata signature: `public void set_EffectGradient(Gradient value) { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[64];
    unsigned long long field_40;
} struct_0;

void bl_UIGradient_set_EffectGradient(struct_0 *ptr, unsigned long a1)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    ptr->field_40 = a1;
    sub_f7d8d0((struct struct_0 *)&ptr->field_40);
    v4 = BaseMeshEffect__get_graphic(ptr, 0);
    if (!BaseMeshEffect__get_graphic(ptr, 0))
        sub_f7db74();
    goto *((long long *)(*((long long *)BaseMeshEffect__get_graphic(ptr, 0)) + 760));
}
```

## `bl_UIGradient.get_GradientType` — RVA `0xce8cb8`

- Decompiled symbol: `bl_UIGradient_get_GradientType`
- Metadata signature: `public bl_UIGradient.Type get_GradientType() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned int field_28;
} struct_0;

int bl_UIGradient_get_GradientType(struct_0 *a0)
{
    return a0->field_28;
}
```

## `bl_UIGradient.set_GradientType` — RVA `0xce8cc0`

- Decompiled symbol: `bl_UIGradient_set_GradientType`
- Metadata signature: `public void set_GradientType(bl_UIGradient.Type value) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned int field_28;
} struct_0;

void bl_UIGradient_set_GradientType(struct_0 *ptr, unsigned int a1)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    ptr->field_28 = a1;
    BaseMeshEffect__get_graphic();
    if (!BaseMeshEffect__get_graphic())
        sub_f7db74();
    goto *((long long *)(*((long long *)BaseMeshEffect__get_graphic()) + 760));
}
```

## `bl_UIGradient.get_ModifyVertices` — RVA `0xce8cec`

- Decompiled symbol: `bl_UIGradient_get_ModifyVertices`
- Metadata signature: `public bool get_ModifyVertices() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

long long bl_UIGradient_get_ModifyVertices(struct_0 *a0)
{
    return a0->field_30;
}
```

## `bl_UIGradient.set_ModifyVertices` — RVA `0xce8cf4`

- Decompiled symbol: `bl_UIGradient_set_ModifyVertices`
- Metadata signature: `public void set_ModifyVertices(bool value) { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

void bl_UIGradient_set_ModifyVertices(struct_0 *ptr, char a1)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    ptr->field_30 = a1 & 1;
    BaseMeshEffect__get_graphic();
    if (!BaseMeshEffect__get_graphic())
        sub_f7db74();
    goto *((long long *)(*((long long *)BaseMeshEffect__get_graphic()) + 760));
}
```

## `bl_UIGradient.get_Offset` — RVA `0xce8d24`

- Decompiled symbol: `bl_UIGradient_get_Offset`
- Metadata signature: `public float get_Offset() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long bl_UIGradient_get_Offset(unsigned long a0)
{
    return a0;
}
```

## `bl_UIGradient.set_Offset` — RVA `0xce8d2c`

- Decompiled symbol: `bl_UIGradient_set_Offset`
- Metadata signature: `public void set_Offset(float value) { }`
- Native interval: `64` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[52];
    unsigned int field_34;
} struct_0;

void bl_UIGradient_set_Offset(struct_0 *ptr)
{
    unsigned long long v1;  // x30
    unsigned int v2;  // s1
    unsigned int v3;  // s0
    unsigned long v4;  // 4138
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    v2 = [D] unsupported_Iop_ZeroHI96ofV128();
    v4 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v3, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0xbf800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0xbf800000) & 1)) & ((unsigned long long)(char)(CmpF(v3, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0xbf800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v4))
        v2 = 0xbf800000;
    ptr->field_34 = v2;
    BaseMeshEffect__get_graphic();
    if (!BaseMeshEffect__get_graphic())
        sub_f7db74();
    goto *((long long *)(*((long long *)BaseMeshEffect__get_graphic()) + 760));
}
```

## `bl_UIGradient.get_Zoom` — RVA `0xce8d6c`

- Decompiled symbol: `bl_UIGradient_get_Zoom`
- Metadata signature: `public float get_Zoom() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long bl_UIGradient_get_Zoom(unsigned long a0)
{
    return a0;
}
```

## `bl_UIGradient.set_Zoom` — RVA `0xce8d74`

- Decompiled symbol: `bl_UIGradient_set_Zoom`
- Metadata signature: `public void set_Zoom(float value) { }`
- Native interval: `68` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[56];
    unsigned int field_38;
} struct_0;

void bl_UIGradient_set_Zoom(struct_0 *ptr)
{
    unsigned long long v1;  // x30
    unsigned int v2;  // s2
    unsigned int v3;  // s0
    unsigned long v4;  // 4146
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    v2 = [D] unsupported_Iop_ZeroHI96ofV128();
    v4 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v3, 1036831949)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 1036831949) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, 1036831949)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 1036831949) & 1)) & ((unsigned long long)(char)(CmpF(v3, 1036831949)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 1036831949) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v4))
        v2 = 1036831949;
    ptr->field_38 = v2;
    BaseMeshEffect__get_graphic();
    if (!BaseMeshEffect__get_graphic())
        sub_f7db74();
    goto *((long long *)(*((long long *)BaseMeshEffect__get_graphic()) + 760));
}
```

## `bl_UIGradient.ModifyMesh` — RVA `0xce8db8`

- Decompiled symbol: `bl_UIGradient_ModifyMesh`
- Metadata signature: `public override void ModifyMesh(VertexHelper helper) { }`
- Native interval: `3756` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[456];
    struct struct_1 *field_1c8;
    unsigned long long field_1d0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1eecff0;
extern long long g_1eed920;
extern long long g_1ef41c0;
extern long long g_1ef8ba0;
extern long long g_1ef8bd8;
extern long long g_1ef8be0;
extern long long g_1f05540;
extern long long g_1f05548;
extern char g_1fab676;

void bl_UIGradient_ModifyMesh(struct_0 **a0, unsigned long a1)
{
    unsigned long long v54;  // d15
    unsigned long long v55;  // d14
    unsigned long long v64;  // x27
    unsigned long long v65;  // x26
    unsigned long long v66;  // x25
    unsigned long long v67;  // x24
    unsigned long long v68;  // x23
    unsigned long long v69;  // x22
    unsigned long long v70;  // x21
    unsigned long long v71;  // x20
    unsigned long long v72;  // x19
    struct_0 **v73;  // x0
    unsigned long long v56;  // d13
    unsigned long v74;  // x1
    unsigned long long v57;  // d12
    unsigned long long v58;  // d11
    unsigned long long v59;  // d10
    unsigned long long v60;  // d9
    unsigned long long v61;  // d8
    unsigned long long v62;  // x30
    unsigned long long v63;  // x28
    uint128_t flag30;  // [bp-0x2f0]
    uint128_t flag31;  // [bp-0x2e0]
    uint128_t flag32;  // [bp-0x2d0]
    unsigned long long flag5;  // [bp-0x2c0]
    unsigned long long flag4;  // [bp-0x2b8]
    uint128_t flag27;  // [bp-0x2b0]
    uint128_t flag28;  // [bp-0x2a0]
    uint128_t flag29;  // [bp-0x290]
    unsigned long long flag3;  // [bp-0x280]
    unsigned long long flag2;  // [bp-0x278]
    unsigned long long choice;  // [bp-0x270]
    unsigned int flag;  // [bp-0x268]
    uint128_t flag25;  // [bp-0x260]
    uint128_t flag26;  // [bp-0x250]
    uint128_t flag23;  // [bp-0x240]
    uint128_t flag24;  // [bp-0x230]
    uint128_t flag21;  // [bp-0x220]
    uint128_t flag22;  // [bp-0x210]
    uint128_t flag20;  // [bp-0x204]
    uint128_t flag18;  // [bp-0x1f0]
    uint128_t flag19;  // [bp-0x1e0]
    uint128_t flag16;  // [bp-0x1d0]
    uint128_t flag17;  // [bp-0x1c0]
    uint128_t flag14;  // [bp-0x1b0]
    uint128_t flag15;  // [bp-0x1a0]
    uint128_t flag13;  // [bp-0x194]
    uint128_t flag11;  // [bp-0x180]
    uint128_t flag12;  // [bp-0x170]
    uint128_t flag9;  // [bp-0x160]
    uint128_t flag10;  // [bp-0x150]
    uint128_t flag7;  // [bp-0x140]
    uint128_t flag8;  // [bp-0x130]
    uint128_t flag6;  // [bp-0x124]
    unsigned long long v33;  // [bp-0xa0]
    unsigned long long v34;  // [bp-0x98]
    unsigned long long v35;  // [bp-0x90]
    unsigned long long v36;  // [bp-0x88]
    unsigned long long v37;  // [bp-0x80]
    unsigned long long v38;  // [bp-0x78]
    unsigned long long v39;  // [bp-0x70]
    unsigned long long v40;  // [bp-0x68]
    char *v41;  // [bp-0x60]
    unsigned long long v42;  // [bp-0x58]
    unsigned long long v43;  // [bp-0x50]
    unsigned long long v44;  // [bp-0x48]
    unsigned long long v45;  // [bp-0x40]
    unsigned long long v46;  // [bp-0x38]
    unsigned long long v47;  // [bp-0x30]
    unsigned long long v48;  // [bp-0x28]
    unsigned long long v49;  // [bp-0x20]
    unsigned long long v50;  // [bp-0x18]
    unsigned long long v51;  // [bp-0x10]
    unsigned long long v52;  // [bp-0x8]
    char v53;  // [bp+0x0]

    v33 = v54;
    v34 = v55;
    v35 = v56;
    v36 = v57;
    v37 = v58;
    v38 = v59;
    v39 = v60;
    v40 = v61;
    v41 = &v53;
    v42 = v62;
    v43 = v63;
    v44 = v64;
    v45 = v65;
    v46 = v66;
    v47 = v67;
    v48 = v68;
    v49 = v69;
    v50 = v70;
    v51 = v71;
    v52 = v72;
    if (!(g_1fab676 & 1))
    {
        sub_f7d92c(&g_1eecff0);
        sub_f7d92c(&g_1ef8ba0);
        sub_f7d92c(&g_1ef8bd8);
        sub_f7d92c(&g_1ef8be0);
        sub_f7d92c(&g_1eed920);
        sub_f7d92c(&g_1f05540);
        sub_f7d92c(&g_1f05548);
        sub_f7d92c(&g_1ef41c0);
        g_1fab676 = 1;
    }
    choice = 0;
    flag = 0;
    flag2 = 0;
    flag3 = 0;
    flag4 = 0;
    flag5 = 0;
    flag6 = 0;
    flag7 = 0;
    flag8 = 0;
    flag9 = 0;
    flag10 = 0;
    flag11 = 0;
    flag12 = 0;
    flag13 = 0;
    flag14 = 0;
    flag15 = 0;
    flag16 = 0;
    flag17 = 0;
    flag18 = 0;
    flag19 = 0;
    flag20 = 0;
    flag21 = 0;
    flag22 = 0;
    flag23 = 0;
    flag24 = 0;
    flag25 = 0;
    flag26 = 0;
    flag27 = 0;
    flag28 = 0;
    flag29 = 0;
    flag30 = 0;
    flag31 = 0;
    flag32 = 0;
    v73 = a0;
    v74 = *(a0)->field_1d0;
    *(a0)->field_1c8();
}
```

## `bl_UIGradient.GetBounds` — RVA `0xce9c64`

- Decompiled symbol: `bl_UIGradient_GetBounds`
- Metadata signature: `private Rect GetBounds(List<UIVertex> vertices) { }`
- Native interval: `336` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

extern long long g_1ef8bd8;
extern long long g_1ef8be0;
extern char g_1fab677;

unsigned long long bl_UIGradient_GetBounds(unsigned long a0, struct_0 *ptr, unsigned long a2)
{
    unsigned int v2;  // s8
    unsigned long long v3;  // x0
    unsigned long v12;  // 4125
    int v13;  // q1
    unsigned long v14;  // 4129
    unsigned long v15;  // 4125
    int v4;  // q11
    unsigned int v5;  // w20
    unsigned int v6;  // s8
    int v7;  // q11
    int v8;  // q11
    unsigned int v9;  // s12
    unsigned long long v10;  // x0
    unsigned long v11;  // 4125
    unsigned int v0;  // [bp-0xc0]
    unsigned int v1;  // [bp-0xbc]

    if (!(g_1fab677 & 1))
    {
        sub_f7d92c(&g_1ef8bd8);
        sub_f7d92c(&g_1ef8be0);
        g_1fab677 = 1;
    }
    if (ptr)
    {
        sub_14d077c(ptr, 0, g_1ef8be0);
        v2 = v0;
        v3 = sub_14d077c(ptr, 0, g_1ef8be0);
        v4 = (int)v1;
        v5 = ptr->field_18 - 1;
        if (v5 < 1)
            return v3;
        v6 = v2;
        v7 = v4;
        do
        {
            v8 = v7;
            sub_14d077c(ptr, v5, g_1ef8be0);
            v9 = v0;
            v10 = sub_14d077c(ptr, v5, g_1ef8be0);
            v11 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v9, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v2) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v9, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v2) & 1)) & ((unsigned long long)(char)(CmpF(v9, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v2) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v11))
            {
                v2 = v9;
            }
            else
            {
                v12 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v9, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v6) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v9, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v6) & 1)) & ((unsigned long long)(char)(CmpF(v9, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v6) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if (!((char)v12))
                    v6 = v9;
            }
            v13 = (int)v1;
            v14 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(*((unsigned int *)(void*)&v13), *((unsigned int *)(void*)&v4))) >> 5 & 3 | (unsigned long long)(CmpF(*((unsigned int *)(void*)&v13), *((unsigned int *)(void*)&v4)) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(*((unsigned int *)(void*)&v13), *((unsigned int *)(void*)&v4))) >> 5 & 3 | (unsigned long long)(CmpF(*((unsigned int *)(void*)&v13), *((unsigned int *)(void*)&v4)) & 1)) & ((unsigned long long)(char)(CmpF(*((unsigned int *)(void*)&v13), *((unsigned int *)(void*)&v4))) >> 5 & 3 | (unsigned long long)(CmpF(*((unsigned int *)(void*)&v13), *((unsigned int *)(void*)&v4)) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v14))
            {
                v4 = v13;
            }
            else
            {
                v15 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(*((unsigned int *)(void*)&v13), *((unsigned int *)(void*)&v8))) >> 5 & 3 | (unsigned long long)(CmpF(*((unsigned int *)(void*)&v13), *((unsigned int *)(void*)&v8)) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(*((unsigned int *)(void*)&v13), *((unsigned int *)(void*)&v8))) >> 5 & 3 | (unsigned long long)(CmpF(*((unsigned int *)(void*)&v13), *((unsigned int *)(void*)&v8)) & 1)) & ((unsigned long long)(char)(CmpF(*((unsigned int *)(void*)&v13), *((unsigned int *)(void*)&v8))) >> 5 & 3 | (unsigned long long)(CmpF(*((unsigned int *)(void*)&v13), *((unsigned int *)(void*)&v8)) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v15)
                    continue;
            }
            v13 = v8;
        } while ((v5 -= 1, v7 = v13, 0 < v5));
        return v10;
    }
    sub_f7db74();
}
```

## `bl_UIGradient.SplitTrianglesAtGradientStops` — RVA `0xce9db4`

- Decompiled symbol: `bl_UIGradient_SplitTrianglesAtGradientStops`
- Metadata signature: `private void SplitTrianglesAtGradientStops(List<UIVertex> _vertexList, Rect bounds, float zoomOffset, VertexHelper helper) { }`
- Native interval: `4344` bytes
- Result: `pseudocode`

```c
typedef struct struct_7 {
    char padding_0[24];
    int field_18;
} struct_7;

typedef struct struct_6 {
    unsigned int field_0;
    char padding_4[20];
    int field_18;
    char padding_1c[4];
    unsigned int field_20;
} struct_6;

typedef struct struct_8 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_8;

typedef struct struct_9 {
    char padding_0[16];
    unsigned long long field_10;
    int field_18;
    unsigned int field_1c;
} struct_9;

typedef struct struct_10 {
    char padding_0[16];
    unsigned long long field_10;
    int field_18;
    unsigned int field_1c;
} struct_10;

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

extern char g_1000000;
extern long long g_1eed6c0;
extern long long g_1eed920;
extern long long g_1ef7e60;
extern struct_2 *g_1ef7e68;
extern long long g_1ef7e88;
extern long long g_1ef7e90;
extern long long g_1ef7ea0;
extern long long g_1ef7ed8;
extern long long g_1ef7ee0;
extern long long g_1ef8580;
extern long long g_1ef8588;
extern long long g_1ef8ba8;
extern struct_5 *g_1ef8bb0;
extern long long g_1ef8bb8;
extern long long g_1ef8bc0;
extern long long g_1ef8bc8;
extern long long g_1ef8bd8;
extern long long g_1ef8be0;
extern char g_1fab678;

struct_7 * bl_UIGradient_SplitTrianglesAtGradientStops(long long a0, struct_6 *a1, long long a2)
{
    long long v56;  // x24
    struct_6 *cur;  // x20
    struct_9 *p;  // x23
    struct_10 *ptr;  // x28
    int i;  // w29
    unsigned int v69;  // w0
    unsigned long idx4;  // x21
    unsigned int v71;  // w24
    unsigned long dst;  // x0
    unsigned int v73;  // s8
    unsigned long v74;  // 4125
    int v58;  // q4
    unsigned int v75;  // s8
    unsigned long v76;  // 4125
    unsigned long long v77;  // x8
    unsigned long v78;  // x10
    unsigned long long v79;  // x8
    unsigned long v80;  // x9
    unsigned int v81;  // w8
    struct_6 *v82;  // x21
    long long v83;  // x23
    int v59;  // q0
    long long v84;  // x24
    unsigned long v85;  // x19
    unsigned int v86;  // s8
    unsigned long v87;  // 4125
    unsigned int v88;  // w8
    unsigned long long v89;  // x9
    unsigned int v90;  // w9
    unsigned long long v91;  // x25
    unsigned long long v92;  // x8
    unsigned long v93;  // x9
    struct_7 *v60;  // x0
    unsigned int v94;  // w0
    unsigned long long v95;  // x0
    unsigned long long v96;  // x25
    unsigned long long v97;  // x8
    unsigned long v98;  // x9
    unsigned int v99;  // w19
    unsigned int v100;  // w20
    unsigned int v101;  // w21
    unsigned int v102;  // w25
    unsigned long v103;  // x2
    struct_7 *v61;  // x22
    long long v104;  // x0
    unsigned long v105;  // x1
    unsigned long v106;  // x3
    unsigned int v107;  // w0
    unsigned int v108;  // w21
    unsigned int v109;  // w8
    unsigned long off;  // x21
    unsigned int v111;  // s8
    unsigned long v112;  // 4125
    unsigned int v113;  // w19
    struct_7 *v62;  // x0
    unsigned int v114;  // s8
    unsigned long v115;  // 4125
    unsigned long long v116;  // x8
    unsigned long v117;  // x9
    struct_7 *v118;  // x0
    long long v119;  // x0
    unsigned int v120;  // w21
    unsigned long long v63;  // x2
    struct_6 *v64;  // x26
    struct_8 *addr;  // x27
    unsigned int v0;  // [bp-0x9d4]
    struct_9 *v1;  // [bp-0x9d0]
    long long v2;  // [bp-0x9c8]
    int v3;  // [bp-0x9bc]
    unsigned int v4;  // [bp-0x9b8]
    unsigned int v5;  // [bp-0x9b4]
    struct_6 *v6;  // [bp-0x9b0]
    struct_6 *v7;  // [bp-0x9a8]
    struct_6 *ptr4;  // [bp-0x998]
    char v9;  // [bp-0x990]
    char v10;  // [bp-0x920]
    char v11;  // [bp-0x8b0]
    char v12;  // [bp-0x840]
    char v13;  // [bp-0x7d0]
    char v14;  // [bp-0x760]
    char v15;  // [bp-0x6f0]
    char v16;  // [bp-0x680]
    char v17;  // [bp-0x610]
    char v18;  // [bp-0x5a0]
    char v19;  // [bp-0x530]
    char v20;  // [bp-0x4c0]
    int v21;  // [bp-0x450]
    unsigned long long v22;  // [bp-0x440]
    char v23;  // [bp-0x3d0]
    int flag21;  // [bp-0x360]
    uint128_t flag20;  // [bp-0x350]
    uint128_t flag19;  // [bp-0x340]
    uint128_t flag18;  // [bp-0x330]
    uint128_t flag17;  // [bp-0x320]
    uint128_t flag16;  // [bp-0x310]
    uint128_t flag15;  // [bp-0x304]
    unsigned long flag23;  // [bp-0x2f0]
    int v32;  // [bp-0x2f0]
    unsigned long long flag22;  // [bp-0x2e8]
    unsigned long long v34;  // [bp-0x2e0]
    int flag14;  // [bp-0x2d0]
    unsigned int flag13;  // [bp-0x2c0]
    uint128_t flag12;  // [bp-0x2b0]
    uint128_t flag11;  // [bp-0x2a0]
    uint128_t flag10;  // [bp-0x290]
    uint128_t flag9;  // [bp-0x280]
    uint128_t flag8;  // [bp-0x270]
    uint128_t flag7;  // [bp-0x260]
    int flag6;  // [bp-0x250]
    uint128_t flag5;  // [bp-0x240]
    uint128_t flag4;  // [bp-0x230]
    uint128_t flag3;  // [bp-0x220]
    uint128_t flag2;  // [bp-0x210]
    uint128_t choice;  // [bp-0x200]
    uint128_t flag;  // [bp-0x1f4]
    char v50;  // [bp-0x1e0]
    char v51;  // [bp-0x170]
    char v52;  // [bp-0x100]
    unsigned long long v53;  // [bp-0x88]
    char *v54;  // [bp-0x60]
    char v55;  // [bp+0x0]

    v54 = &v55;
    v56 = a2;
    cur = a1;
    if (!(g_1fab678 & 1))
    {
        sub_f7d92c("_T");
        sub_f7d92c("9Q");
        sub_f7d92c("aT");
        sub_f7d92c(";Q");
        sub_f7d92c("iT");
        sub_f7d92c("CQ");
        sub_f7d92c(&g_1ef7e68);
        sub_f7d92c(&g_1ef8bb0);
        sub_f7d92c(&g_1ef8bb8);
        sub_f7d92c(&g_1ef7e88);
        sub_f7d92c(&g_1ef7e90);
        sub_f7d92c(&g_1ef8bc0);
        sub_f7d92c(&g_1ef8bc8);
        sub_f7d92c(&g_1ef7ea0);
        sub_f7d92c(&g_1ef7e60);
        sub_f7d92c(&g_1ef8ba8);
        sub_f7d92c(&g_1ef8bd8);
        sub_f7d92c(&g_1ef8580);
        sub_f7d92c(&g_1ef7ed8);
        sub_f7d92c(&g_1ef8be0);
        sub_f7d92c(&g_1ef7ee0);
        sub_f7d92c(&g_1ef8588);
        sub_f7d92c(&g_1eed6c0);
        sub_f7d92c(&g_1eed920);
        g_1fab678 = 1;
    }
    flag = 0;
    choice = 0;
    flag2 = 0;
    flag3 = 0;
    flag4 = 0;
    flag5 = 0;
    flag6 = 0;
    flag7 = 0;
    flag8 = 0;
    flag9 = 0;
    flag10 = 0;
    flag11 = 0;
    flag12 = 0;
    flag13 = 0;
    flag14 = 0;
    flag15 = 0;
    flag16 = 0;
    flag17 = 0;
    flag18 = 0;
    flag19 = 0;
    flag20 = 0;
    flag21 = 0;
    v59 = v58;
    flag22 = 0;
    flag23 = 0;
    v34 = 0;
    v60 = bl_UIGradient__FindStops(a0);
    if (v60)
    {
        v61 = v60;
        if (v60->field_18 < 1)
            return v60;
        if (v56 && !((v62 = (struct_7 *)(unsigned long long)VertexHelper__Clear(v56, 0), !cur)))
        {
            v0 = cur->field_18;
            if (cur->field_18 < 1)
                return VertexHelper__Clear(v56, 0);
            v63 = 0;
            ptr4 = &flag13;
            v7 = cur;
            v2 = v56;
            while (true)
            {
                v53 = v63;
                v64 = bl_UIGradient__GetPositions(a0, cur);
                addr = sub_f7db70(g_1eed6c0);
                sub_148f32c(addr, 3, g_1ef7e60);
                p = sub_f7db70(g_1eed920);
                sub_14d0290(p, 3, g_1ef8ba8);
                ptr = sub_f7db70(g_1eed920);
                sub_14d0290(ptr, 2, g_1ef8ba8);
                if (v61->field_18 >= 1)
                {
                    i = 0;
                    v6 = v64 + 1;
                    v1 = p;
                    do
                    {
                        v69 = VertexHelper__get_currentVertCount(v56, 0);
                        if (!ptr || !addr)
                            goto LABEL_10eade8;
                        idx4 = 0;
                        v71 = 1;
                        cur = 0x1;
                        v4 = v69;
                        v5 = 0;
                        v3 = ptr->field_18;
                        do
                        {
                            if ((sub_148fe20(addr, idx4 & 4294967295, g_1ef7e88) & 1))
                                continue;
                            if (!v64)
                                goto LABEL_10eade8;
                            if (v64->field_18 <= idx4)
                                goto LABEL_10eadec;
                            v73 = (&v64->field_20)[idx4];
                            sub_14afb18(v61, i, g_1ef8588);
                            v74 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v73, *((unsigned int *)(void*)&v59))) >> 5 & 3 | (unsigned long long)(CmpF(v73, *((unsigned int *)(void*)&v59)) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v73, *((unsigned int *)(void*)&v59))) >> 5 & 3 | (unsigned long long)(CmpF(v73, *((unsigned int *)(void*)&v59)) & 1)) & ((unsigned long long)(char)(CmpF(v73, *((unsigned int *)(void*)&v59))) >> 5 & 3 | (unsigned long long)(CmpF(v73, *((unsigned int *)(void*)&v59)) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if ((char)v74)
                                continue;
                            sub_14d077c(v7, v53 + idx4, g_1ef8be0);
                            dst = memcpy(&flag6, &v21, 108);
                            if (v64->field_18 <= (unsigned int)idx4 + (unsigned int)(1 - (__ROL__(v71 * 2863311531, 31) & 2147483647) * 3))
                                goto LABEL_10eadec;
                            v75 = *((int *)((char *)v6 + 18446744073709551604 * (__ROL__(cur * 12297829382473034411 >> 64, 63) & 9223372036854775807) + 4 * idx4));
                            sub_14afb18(v61, i, g_1ef8588);
                            v76 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v75, *((unsigned int *)(void*)&v59))) >> 5 & 3 | (unsigned long long)(CmpF(v75, *((unsigned int *)(void*)&v59)) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v75, *((unsigned int *)(void*)&v59))) >> 5 & 3 | (unsigned long long)(CmpF(v75, *((unsigned int *)(void*)&v59)) & 1)) & ((unsigned long long)(char)(CmpF(v75, *((unsigned int *)(void*)&v59))) >> 5 & 3 | (unsigned long long)(CmpF(v75, *((unsigned int *)(void*)&v59)) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if (!((char)v76))
                            {
                                sub_1490624(addr, 0, idx4 & 4294967295, g_1ef7ea0);
                                memcpy(&v52, &flag6, 108);
                                if (!p)
                                    goto LABEL_10eade8;
                                memcpy(&v21, &v52, 108);
                                sub_14d1a54(p, 0, &v21, g_1ef8bc8);
                                v5 = 1;
                            }
                            else
                            {
                                v77 = addr->field_10;
                                addr->field_1c = addr->field_1c + 1;
                                if (!v77)
                                    goto LABEL_10eade8;
                                v78 = addr->field_18;
                                if (*((int *)(v77 + 24)) > (unsigned int)v78)
                                {
                                    addr->field_18 = (unsigned int)v78 + 1;
                                    *((unsigned int *)(v77 + v78 * 4 + 32)) = idx4;
                                }
                                else
                                {
                                    sub_148fb08(addr, idx4 & 4294967295, g_1ef7e68->field_20->field_c0->field_70);
                                }
                                memcpy(&v23, &flag6, 108);
                                if (!p || !((memcpy(&v52, &v23, 108), v79 = p->field_10, p->field_1c = p->field_1c + 1, v79)))
                                    goto LABEL_10eade8;
                                v80 = p->field_18;
                                if (*((int *)(v79 + 24)) > (unsigned int)v80)
                                {
                                    p->field_18 = (unsigned int)v80 + 1;
                                    memcpy(v79 + 108 * v80 + 32, &v52, 108);
                                }
                                else
                                {
                                    memcpy(&v21, &v52, 108);
                                    sub_14d0b34(p, &v21, g_1ef8bb0->field_20->field_c0->field_70);
                                }
                            }
                        } while ((idx4 = (unsigned long)(idx4 + 1), cur += 1, v71 += 1, idx4 != 3));
                        v56 = v2;
                        if (addr->field_18)
                        {
                            cur = v7;
                            if (addr->field_18 == 3)
                                break;
                            if (p)
                            {
                                sub_14d17b4(p, g_1ef8bc0);
                                memcpy(&flag14, &v21, 128);
                                cur = ptr4;
                                while (((char)sub_1312a40(&flag14, g_1ef64e8) & 1))
                                {
                                    memcpy(&v20, cur, 108);
                                    VertexHelper__AddVert(v56, &v20, 0);
                                }
                                sub_1312a3c(&flag14, g_1ef64e0);
                                v81 = ptr->field_1c;
                                ptr->field_18 = 0;
                                ptr->field_1c = v81 + 1;
                                sub_1490444(addr, g_1ef7e90);
                                v82 = v7;
                                v83 = v56;
                                v32 = v21;
                                v34 = v22;
                                v84 = v56;
                                while (((char)sub_130b79c(&v32, g_1ef6238) & 1))
                                {
                                    if (!v64)
                                    {
                                        sub_f7db74();
                                        sub_1312a3c(&flag14, g_1ef64e0);
                                        if (1)
                                            goto LABEL_10eae98;
                                        cur = sub_f1bd40(0);
                                        goto LABEL_10eae5c;
                                    }
                                    v85 = (unsigned int)v34;
                                    cur = (unsigned int)v85 + 1 - (__ROL__(((unsigned int)v85 + 1) * 1431655766, 32) + (__ROL__(((unsigned int)v85 + 1) * 1431655766, 1) & 1)) * 3;
                                    if (v64->field_18 > (unsigned int)cur)
                                    {
                                        v86 = (&v64->field_20)[cur & 4294967295];
                                        sub_14afb18(v61, i, g_1ef8588);
                                        v87 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v86, *((unsigned int *)(void*)&v59))) >> 5 & 3 | (unsigned long long)(CmpF(v86, *((unsigned int *)(void*)&v59)) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v86, *((unsigned int *)(void*)&v59))) >> 5 & 3 | (unsigned long long)(CmpF(v86, *((unsigned int *)(void*)&v59)) & 1)) & ((unsigned long long)(char)(CmpF(v86, *((unsigned int *)(void*)&v59))) >> 5 & 3 | (unsigned long long)(CmpF(v86, *((unsigned int *)(void*)&v59)) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                        if (!((char)v87))
                                        {
                                            v88 = (unsigned int)cur + 1;
                                            v89 = (v88 * &g_1000000 >> 31 & 0xffffff00 | v88 & 255) * 1431655766;
                                            v90 = ((unsigned int)(__ROL__(v89, 32)) + ((unsigned int)(__ROL__(v89, 1)) & 1)) * 3;
                                            cur = (v88 - v90) * &g_1000000 >> 31 & 0xffffff00 | v88 - v90 & 255;
                                        }
                                        v91 = v53;
                                        sub_14d077c(v82, v85 + v91, g_1ef8be0);
                                        memcpy(&v21, &v52, 108);
                                        sub_14d077c(v82, (char *)cur + v91, g_1ef8be0);
                                        memcpy(&v52, &v23, 108);
                                        sub_14afb18(v61, i, g_1ef8588);
                                        memcpy(&v19, &v21, 108);
                                        memcpy(&v18, &v52, 108);
                                        bl_UIGradient__CreateSplitVertex(a0, &v19, &v18);
                                        memcpy(&v17, &v23, 108);
                                        memcpy(&v50, &v17, 108);
                                        v92 = ptr->field_10;
                                        ptr->field_1c = ptr->field_1c + 1;
                                        if (v92)
                                        {
                                            v93 = ptr->field_18;
                                            if (*((int *)(v92 + 24)) > (unsigned int)v93)
                                            {
                                                ptr->field_18 = (unsigned int)v93 + 1;
                                                memcpy(v92 + 108 * v93 + 32, &v50, 108);
                                                v84 = v83;
                                            }
                                            else
                                            {
                                                memcpy(&v51, &v50, 108);
                                                sub_14d0b34(ptr, &v51, g_1ef8bb0->field_20->field_c0->field_70);
                                                v84 = v83;
                                            }
                                        }
                                        else
                                        {
                                            sub_f7db74();
                                            goto LABEL_10eadf8;
                                        }
                                    }
                                    else
                                    {
                                        sub_f7db7c();
LABEL_10eadf8:
LABEL_10eae5c:
                                        sub_1312a3c(&flag14, g_1ef64e0);
                                        if (1)
                                            goto LABEL_10eae98;
                                        cur = sub_f1bd40(0);
                                        goto LABEL_10eae80;
                                    }
                                }
                                sub_130b798(&v32, g_1ef6230);
                                cur = v7;
                                if (ptr->field_18 == 1)
                                {
                                    v94 = sub_148f818(addr, 0, g_1ef7ee0);
                                    v95 = sub_148f818(addr, 0, g_1ef7ee0);
                                    v96 = v53;
                                    sub_14d077c(cur, v95 + v96, g_1ef8be0);
                                    memcpy(&v16, &v21, 108);
                                    sub_14d077c(cur, v94 + 2 - (__ROL__((v94 + 2) * 1431655766, 32) + (__ROL__((v94 + 2) * 1431655766, 1) & 1)) * 3 + v96, g_1ef8be0);
                                    memcpy(&v15, &v21, 108);
                                    sub_14afb18(v61, i, g_1ef8588);
                                    bl_UIGradient__CreateSplitVertex(a0, &v16, &v15);
                                    memcpy(&v52, &v14, 108);
                                    v97 = ptr->field_10;
                                    ptr->field_1c = ptr->field_1c + 1;
                                    if (v97)
                                    {
                                        v98 = ptr->field_18;
                                        if (*((int *)(v97 + 24)) > (unsigned int)v98)
                                        {
                                            ptr->field_18 = (unsigned int)v98 + 1;
                                            memcpy(v97 + 108 * v98 + 32, &v52, 108);
                                        }
                                        else
                                        {
                                            memcpy(&v21, &v52, 108);
                                            sub_14d0b34(ptr, &v21, g_1ef8bb0->field_20->field_c0->field_70);
                                        }
                                        v56 = v83;
                                        goto LABEL_10ea798;
                                    }
                                    goto LABEL_10eade8;
                                }
                                else
                                {
LABEL_10ea798:
                                    sub_14d17b4(ptr, g_1ef8bc0);
                                    memcpy(&flag14, &v21, 128);
                                    p = v1;
                                    v99 = v4;
                                    while (((char)sub_1312a40(&flag14, g_1ef64e8) & 1))
                                    {
                                        memcpy(&v13, ptr4, 108);
                                        VertexHelper__AddVert(v56, &v13, 0);
                                    }
                                    sub_1312a3c(&flag14, g_1ef64e0);
                                    if (v3 > 0)
                                    {
                                        v100 = v99 - 2;
                                        v101 = v99 + 1;
                                        VertexHelper__AddTriangle(v56, v100, v99, v101, 0);
                                        v102 = v99 - 1;
                                        VertexHelper__AddTriangle(v56, v100, v101, v102, 0);
                                        if (p->field_18 < 1)
                                            goto LABEL_10ea8dc;
                                        v103 = v99 + 3;
                                        if (((char)v5 & 1))
                                        {
                                            v104 = v56;
                                            v105 = v100;
                                            v106 = v99;
                                        }
                                        else
                                        {
                                            v104 = v56;
                                            v105 = v101;
                                            v106 = v102;
                                        }
                                    }
                                    else
                                    {
                                        v107 = VertexHelper__get_currentVertCount(v56, 0);
                                        v108 = v107 - 1;
                                        VertexHelper__AddTriangle(v56, v99, v107 - 2, v108, 0);
                                        if (p->field_18 < 2)
                                            goto LABEL_10ea8dc;
                                        v106 = v99 + 1;
                                        v104 = v56;
                                        v105 = v99;
                                        v103 = v108;
                                    }
                                    VertexHelper__AddTriangle(v104, v105, v103, v106, 0);
LABEL_10ea8dc:
                                    v109 = p->field_1c + 1;
                                    p->field_18 = 0;
                                    p->field_1c = v109;
                                }
                            }
                        }
                        cur = v7;
                        i += 1;
                    } while (i < v61->field_18);
                }
                if (!ptr)
                    break;
                if (ptr->field_18 >= 1)
                {
                    if (!p)
                        break;
                    if (!p->field_18)
                    {
                        if (!addr)
                            break;
                        off = 0;
                        cur = &v64->field_20;
                        do
                        {
                            if (!((char)sub_148fe20(addr, off & 4294967295, g_1ef7e88) & 1))
                            {
                                if (v64)
                                {
                                    if (v64->field_18 <= off)
                                        goto LABEL_10eadec;
                                    v111 = (&cur->field_0)[off];
                                    sub_14afb18(v61, v61->field_18 - 1, g_1ef8588);
                                    v112 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v111, *((unsigned int *)(void*)&v59))) >> 5 & 3 | (unsigned long long)(CmpF(v111, *((unsigned int *)(void*)&v59)) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v111, *((unsigned int *)(void*)&v59))) >> 5 & 3 | (unsigned long long)(CmpF(v111, *((unsigned int *)(void*)&v59)) & 1)) & ((unsigned long long)(char)(CmpF(v111, *((unsigned int *)(void*)&v59))) >> 5 & 3 | (unsigned long long)(CmpF(v111, *((unsigned int *)(void*)&v59)) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                    if ((char)v112)
                                        continue;
                                    if (off == 2)
                                        v113 = 0;
                                    else
                                        v113 = (unsigned int)off + 1;
                                    sub_14d077c();
                                    dst = memcpy(&flag21, &v21, 108);
                                    if (v64->field_18 <= v113)
                                        goto LABEL_10eadec;
                                    v114 = (&v64->field_20)[v113];
                                    sub_14afb18(v61, v61->field_18 - 1, g_1ef8588);
                                    v115 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v114, *((unsigned int *)(void*)&v59))) >> 5 & 3 | (unsigned long long)(CmpF(v114, *((unsigned int *)(void*)&v59)) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v114, *((unsigned int *)(void*)&v59))) >> 5 & 3 | (unsigned long long)(CmpF(v114, *((unsigned int *)(void*)&v59)) & 1)) & ((unsigned long long)(char)(CmpF(v114, *((unsigned int *)(void*)&v59))) >> 5 & 3 | (unsigned long long)(CmpF(v114, *((unsigned int *)(void*)&v59)) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                    if (!((char)v115))
                                    {
                                        memcpy(&v21, &flag21, 108);
                                        sub_14d1a54(p, 0, &v21, g_1ef8bc8);
                                        continue;
                                    }
                                    memcpy(&v52, &flag21, 108);
                                    v116 = p->field_10;
                                    p->field_1c = p->field_1c + 1;
                                    if (!v116)
                                        goto LABEL_10eade8;
                                    v117 = p->field_18;
                                    if (*((int *)(v116 + 24)) > (unsigned int)v117)
                                    {
                                        p->field_18 = (unsigned int)v117 + 1;
                                        memcpy(v116 + 108 * v117 + 32, &v52, 108);
                                        continue;
                                    }
                                    else
                                    {
                                        memcpy(&v21, &v52, 108);
                                        sub_14d0b34(p, &v21, g_1ef8bb0->field_20->field_c0->field_70);
                                    }
                                }
                                goto LABEL_10eade8;
                            }
                        } while ((off = (unsigned long)(off + 1), off != 3));
                    }
                    sub_14d17b4(p, g_1ef8bc0);
                    memcpy(&flag14, &v21, 128);
                    while (((char)sub_1312a40(&flag14, g_1ef64e8) & 1))
                    {
                        memcpy(&v12, ptr4, 108);
                        VertexHelper__AddVert(v56, &v12, 0);
                    }
                    sub_1312a3c(&flag14, g_1ef64e0);
                    v118 = VertexHelper__get_currentVertCount(v56, 0);
                    if (2 > p->field_18)
                    {
                        if (p->field_18 != 1)
                            goto LABEL_10ead60;
                        goto LABEL_10ead20;
                    }
                    else
                    {
                        VertexHelper__AddTriangle(v56, (unsigned int)v118 - 4, (unsigned int)v118 - 2, (unsigned int)v118 - 1, 0);
                        v119 = v56;
LABEL_10ead58:
                        v118 = VertexHelper__AddTriangle(v119);
LABEL_10ead60:
                        cur = v7;
                        v63 = v53 + 3;
                        if ((unsigned int)v63 >= v0)
                            return v118;
                    }
                }
                else
                {
                    v120 = v53;
                    sub_14d077c(cur, v120, g_1ef8be0);
                    memcpy(&v11, &v21, 108);
                    VertexHelper__AddVert(v56, &v11, 0);
                    sub_14d077c(cur, v120 + 1, g_1ef8be0);
                    memcpy(&v10, &v21, 108);
                    VertexHelper__AddVert(v56, &v10, 0);
                    sub_14d077c(cur, v120 + 2, g_1ef8be0);
                    memcpy(&v9, &v21, 108);
                    VertexHelper__AddVert(v56, &v9, 0);
                    VertexHelper__get_currentVertCount(v56, 0);
LABEL_10ead20:
                    v119 = v56;
                    goto LABEL_10ead58;
                }
            }
        }
    }
LABEL_10eade8:
    dst = sub_f7db74();
LABEL_10eadec:
    sub_f7db7c(dst);
LABEL_10eae80:
    sub_130b798(&flag23, g_1ef6230);
    if (false)
        sub_e29990(sub_f1bd40(0));
LABEL_10eae98:
    sub_1026098(cur);
    sub_e29990(sub_f1bd40(0));
}
```

## `bl_UIGradient.BlendColor` — RVA `0xceaeac`

- Decompiled symbol: `bl_UIGradient_BlendColor`
- Metadata signature: `private Color BlendColor(Color colorA, Color colorB) { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[44];
    unsigned int field_2c;
} struct_0;

struct_0 * bl_UIGradient_BlendColor(struct_0 *a0)
{
    if (a0->field_2c == 2)
        return a0;
    return a0;
}
```

## `bl_UIGradient.FindStops` — RVA `0xceaef8`

- Decompiled symbol: `bl_UIGradient_FindStops`
- Metadata signature: `private List<float> FindStops(float zoomOffset, Rect bounds) { }`
- Native interval: `920` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10eaef8: stp d13, d12, [sp, #-0x70]!
// 0x10eaefc: stp d11, d10, [sp, #0x10]
// 0x10eaf00: stp d9, d8, [sp, #0x20]
// 0x10eaf04: stp x30, x25, [sp, #0x30]
// 0x10eaf08: stp x24, x23, [sp, #0x40]
// 0x10eaf0c: stp x22, x21, [sp, #0x50]
// 0x10eaf10: stp x20, x19, [sp, #0x60]
// 0x10eaf14: adrp x21, #0x1fab000
// 0x10eaf18: adrp x22, #0x1e8f000
// 0x10eaf1c: adrp x19, #0x1e8f000
// 0x10eaf20: ldrb w8, [x21, #0x67a]
// 0x10eaf24: ldr x22, [x22, #0xd48]
// 0x10eaf28: ldr x19, [x19, #0xd50]
// 0x10eaf2c: mov v8.16b, v4.16b
// 0x10eaf30: mov v10.16b, v3.16b
// 0x10eaf34: mov v9.16b, v2.16b
// 0x10eaf38: mov v11.16b, v1.16b
// 0x10eaf3c: mov v12.16b, v0.16b
// 0x10eaf40: mov x20, x0
// 0x10eaf44: tbnz w8, #0, #0x10eafbc
// 0x10eaf48: adrp x0, #0x1e8f000
// 0x10eaf4c: ldr x0, [x0, #0xd58]
// 0x10eaf50: bl #0xf7d92c
// 0x10eaf54: adrp x0, #0x1e8f000
// 0x10eaf58: ldr x0, [x0, #0xd60]
// 0x10eaf5c: bl #0xf7d92c
// 0x10eaf60: adrp x0, #0x1e8f000
// 0x10eaf64: ldr x0, [x0, #0xd68]
// 0x10eaf68: bl #0xf7d92c
// 0x10eaf6c: adrp x0, #0x1e8f000
// 0x10eaf70: ldr x0, [x0, #0xd50]
// 0x10eaf74: bl #0xf7d92c
// 0x10eaf78: adrp x0, #0x1e8f000
// 0x10eaf7c: ldr x0, [x0, #0xd20]
// 0x10eaf80: bl #0xf7d92c
// 0x10eaf84: adrp x0, #0x1e8f000
// 0x10eaf88: ldr x0, [x0, #0xd38]
// 0x10eaf8c: bl #0xf7d92c
// 0x10eaf90: adrp x0, #0x1e8f000
// 0x10eaf94: ldr x0, [x0, #0xd70]
// 0x10eaf98: bl #0xf7d92c
// 0x10eaf9c: adrp x0, #0x1e8f000
// 0x10eafa0: ldr x0, [x0, #0xd48]
// 0x10eafa4: bl #0xf7d92c
// 0x10eafa8: adrp x0, #0x1e8c000
// 0x10eafac: ldr x0, [x0, #0xa60]
// 0x10eafb0: bl #0xf7d92c
// 0x10eafb4: mov w8, #1
// 0x10eafb8: strb w8, [x21, #0x67a]
// 0x10eafbc: ldr x0, [x22]
// 0x10eafc0: bl #0xf7db70
// 0x10eafc4: ldr x1, [x19]
// 0x10eafc8: mov x19, x0
// 0x10eafcc: bl #0x14af5bc
// 0x10eafd0: ldr x0, [x20, #0x40]
// 0x10eafd4: cbz x0, #0x10eb288
// 0x10eafd8: ldr s13, [x20, #0x34]
// 0x10eafdc: mov x1, xzr
// 0x10eafe0: bl #0x1b86020
// 0x10eafe4: cbz x0, #0x10eb288
// 0x10eafe8: adrp x22, #0x1e8f000
// 0x10eafec: ldr x22, [x22, #0xd58]
// 0x10eaff0: ldr x8, [x0, #0x18]
// 0x10eaff4: fmov s0, #1.00000000
// 0x10eaff8: fsub s0, s0, s12
// 0x10eaffc: fmul s1, s0, s13
// 0x10eb000: mov x21, x0
// 0x10eb004: fsub s12, s12, s1
// 0x10eb008: cmp w8, #1
// 0x10eb00c: fsub s13, s0, s1
// 0x10eb010: b.lt #0x10eb0b0
// 0x10eb014: mov x23, xzr
// 0x10eb018: and x8, x8, #0xffffffff
// 0x10eb01c: add x24, x21, #0x30
// 0x10eb020: cmp x23, w8, uxtw
// 0x10eb024: b.hs #0x10eb28c
// 0x10eb028: ldr s0, [x24]
// 0x10eb02c: fcmp s0, s13
// 0x10eb030: b.ge #0x10eb0b0
// 0x10eb034: fcmp s0, s12
// 0x10eb038: b.le #0x10eb09c
// 0x10eb03c: cbz x19, #0x10eb288
// 0x10eb040: ldr w10, [x19, #0x1c]
// 0x10eb044: ldr s1, [x20, #0x38]
// 0x10eb048: ldr x8, [x19, #0x10]
// 0x10eb04c: ldr x9, [x22]
// 0x10eb050: add w10, w10, #1
// 0x10eb054: str w10, [x19, #0x1c]
// 0x10eb058: cbz x8, #0x10eb288
// 0x10eb05c: ldrsw x10, [x19, #0x18]
// 0x10eb060: ldr w11, [x8, #0x18]
// 0x10eb064: fsub s0, s0, s12
// 0x10eb068: fmul s0, s0, s1
// 0x10eb06c: cmp w10, w11
// 0x10eb070: b.hs #0x10eb088
// 0x10eb074: add w9, w10, #1
// 0x10eb078: add x8, x8, x10, lsl #2
// 0x10eb07c: str w9, [x19, #0x18]
// 0x10eb080: str s0, [x8, #0x20]
// 0x10eb084: b #0x10eb09c
// 0x10eb088: ldr x8, [x9, #0x20]
// 0x10eb08c: mov x0, x19
// 0x10eb090: ldr x8, [x8, #0xc0]
// 0x10eb094: ldr x1, [x8, #0x70]
// 0x10eb098: bl #0x14afe10
// 0x10eb09c: ldr w8, [x21, #0x18]
// 0x10eb0a0: add x23, x23, #1
// 0x10eb0a4: add x24, x24, #0x14
// 0x10eb0a8: cmp x23, w8, sxtw
// 0x10eb0ac: b.lt #0x10eb020
// 0x10eb0b0: ldr x0, [x20, #0x40]
// 0x10eb0b4: cbz x0, #0x10eb288
// 0x10eb0b8: mov x1, xzr
// 0x10eb0bc: bl #0x1b860a0
// 0x10eb0c0: cbz x0, #0x10eb288
// 0x10eb0c4: ldr x8, [x0, #0x18]
// 0x10eb0c8: mov x21, x0
// 0x10eb0cc: cmp w8, #1
// 0x10eb0d0: b.lt #0x10eb170
// 0x10eb0d4: mov x23, xzr
// 0x10eb0d8: and x8, x8, #0xffffffff
// 0x10eb0dc: add x24, x21, #0x24
// 0x10eb0e0: cmp x23, w8, uxtw
// 0x10eb0e4: b.hs #0x10eb28c
// 0x10eb0e8: ldr s0, [x24]
// 0x10eb0ec: fcmp s0, s13
// 0x10eb0f0: b.ge #0x10eb170
// 0x10eb0f4: fcmp s0, s12
// 0x10eb0f8: b.le #0x10eb15c
// 0x10eb0fc: cbz x19, #0x10eb288
// 0x10eb100: ldr w10, [x19, #0x1c]
// 0x10eb104: ldr s1, [x20, #0x38]
// 0x10eb108: ldr x8, [x19, #0x10]
// 0x10eb10c: ldr x9, [x22]
// 0x10eb110: add w10, w10, #1
// 0x10eb114: str w10, [x19, #0x1c]
// 0x10eb118: cbz x8, #0x10eb288
// 0x10eb11c: ldrsw x10, [x19, #0x18]
// 0x10eb120: ldr w11, [x8, #0x18]
// 0x10eb124: fsub s0, s0, s12
// 0x10eb128: fmul s0, s0, s1
// 0x10eb12c: cmp w10, w11
// 0x10eb130: b.hs #0x10eb148
// 0x10eb134: add w9, w10, #1
// 0x10eb138: add x8, x8, x10, lsl #2
// 0x10eb13c: str w9, [x19, #0x18]
// 0x10eb140: str s0, [x8, #0x20]
// 0x10eb144: b #0x10eb15c
// 0x10eb148: ldr x8, [x9, #0x20]
// 0x10eb14c: mov x0, x19
// 0x10eb150: ldr x8, [x8, #0xc0]
// 0x10eb154: ldr x1, [x8, #0x70]
// 0x10eb158: bl #0x14afe10
// 0x10eb15c: ldr w8, [x21, #0x18]
// 0x10eb160: add x23, x23, #1
// 0x10eb164: add x24, x24, #8
// 0x10eb168: cmp x23, w8, sxtw
// 0x10eb16c: b.lt #0x10eb0e0
// 0x10eb170: ldr w8, [x20, #0x28]
// 0x10eb174: cmp w8, #1
// 0x10eb178: fcsel s10, s8, s10, eq
// 0x10eb17c: fcsel s11, s9, s11, eq
// 0x10eb180: cbz x19, #0x10eb288
// 0x10eb184: adrp x8, #0x1e8f000
// 0x10eb188: ldr x8, [x8, #0xd68]
// 0x10eb18c: mov x0, x19
// 0x10eb190: ldr x1, [x8]
// 0x10eb194: bl #0x14b14ec
// 0x10eb198: ldr w8, [x19, #0x18]
// 0x10eb19c: cmp w8, #1
// 0x10eb1a0: b.lt #0x10eb264
// 0x10eb1a4: adrp x22, #0x1e8f000
// 0x10eb1a8: adrp x23, #0x1e8f000
// 0x10eb1ac: adrp x24, #0x1e8c000
// 0x10eb1b0: adrp x25, #0x1e8f000
// 0x10eb1b4: ldr x22, [x22, #0xd38]
// 0x10eb1b8: ldr x23, [x23, #0xd70]
// 0x10eb1bc: ldr x24, [x24, #0xa60]
// 0x10eb1c0: ldr x25, [x25, #0xd60]
// 0x10eb1c4: mov w20, wzr
// 0x10eb1c8: fmov s12, #2.00000000
// 0x10eb1cc: ldr x2, [x22]
// 0x10eb1d0: mov x0, x19
// 0x10eb1d4: mov w1, w20
// 0x10eb1d8: bl #0x14afb18
// 0x10eb1dc: ldr x2, [x23]
// 0x10eb1e0: fmul s0, s10, s0
// 0x10eb1e4: fadd s0, s11, s0
// 0x10eb1e8: mov x0, x19
// 0x10eb1ec: mov w1, w20
// 0x10eb1f0: bl #0x14afb6c
// 0x10eb1f4: subs w21, w20, #1
// 0x10eb1f8: b.lt #0x10eb254
// 0x10eb1fc: ldr x2, [x22]
// 0x10eb200: mov x0, x19
// 0x10eb204: mov w1, w20
// 0x10eb208: bl #0x14afb18
// 0x10eb20c: ldr x2, [x22]
// 0x10eb210: mov x0, x19
// 0x10eb214: mov w1, w21
// 0x10eb218: mov v8.16b, v0.16b
// 0x10eb21c: bl #0x14afb18
// 0x10eb220: ldr x0, [x24]
// 0x10eb224: mov v9.16b, v0.16b
// 0x10eb228: ldr w8, [x0, #0xe0]
// 0x10eb22c: cbnz w8, #0x10eb234
// 0x10eb230: bl #0xf7da5c
// 0x10eb234: fabd s0, s8, s9
// 0x10eb238: fcmp s0, s12
// 0x10eb23c: b.pl #0x10eb254
// 0x10eb240: ldr x2, [x25]
// 0x10eb244: mov x0, x19
// 0x10eb248: mov w1, w20
// 0x10eb24c: bl #0x14b1328
// 0x10eb250: mov w20, w21
// 0x10eb254: ldr w8, [x19, #0x18]
// 0x10eb258: add w20, w20, #1
// 0x10eb25c: cmp w20, w8
// 0x10eb260: b.lt #0x10eb1cc
// 0x10eb264: mov x0, x19
// 0x10eb268: ldp x20, x19, [sp, #0x60]
// 0x10eb26c: ldp x22, x21, [sp, #0x50]
// 0x10eb270: ldp x24, x23, [sp, #0x40]
// 0x10eb274: ldp x30, x25, [sp, #0x30]
// 0x10eb278: ldp d9, d8, [sp, #0x20]
// 0x10eb27c: ldp d11, d10, [sp, #0x10]
// 0x10eb280: ldp d13, d12, [sp], #0x70
// 0x10eb284: ret
// 0x10eb288: bl #0xf7db74
// 0x10eb28c: bl #0xf7db7c
```

## `bl_UIGradient.GetPositions` — RVA `0xceb290`

- Decompiled symbol: `bl_UIGradient_GetPositions`
- Metadata signature: `private float[] GetPositions(List<UIVertex> _vertexList, int index) { }`
- Native interval: `388` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned int field_28;
} struct_0;

extern long long g_1ef8be0;
extern char g_1fab679;

unsigned int [11] bl_UIGradient_GetPositions(struct_0 *a0, long long a1, unsigned int a2)
{
    unsigned int v2[11];  // x0
    unsigned int ptr[11];  // x20
    unsigned int v4;  // s0
    unsigned int v0;  // [bp-0xa0]
    unsigned int v1;  // [bp-0x9c]

    if (!(g_1fab679 & 1))
    {
        sub_f7d92c(&g_1ef8be0);
        sub_f7d92c("1)");
        g_1fab679 = 1;
    }
    v2 = sub_f7d9d4(g_1eee368, 3);
    if (a1)
    {
        ptr = v2;
        if (a0->field_28)
        {
            sub_14d077c(a1, a2, g_1ef8be0);
            if (ptr)
            {
                if (ptr[6])
                {
                    ptr[8] = v1;
                    sub_14d077c(a1, a2 + 1, g_1ef8be0);
                    if (ptr[6] > 1)
                    {
                        ptr[9] = v1;
                        sub_14d077c(a1, a2 + 2, g_1ef8be0);
                        if (ptr[6] > 2)
                        {
                            ptr[10] = v1;
                            return ptr;
                        }
                    }
                }
                goto LABEL_10eb40c;
            }
        }
        else
        {
            sub_14d077c(a1, a2, g_1ef8be0);
            if (ptr)
            {
                if (ptr[6])
                {
                    ptr[8] = v0;
                    sub_14d077c(a1, a2 + 1, g_1ef8be0);
                    if (ptr[6] > 1)
                    {
                        ptr[9] = v0;
                        sub_14d077c(a1, a2 + 2, g_1ef8be0);
                        if (ptr[6] > 2)
                        {
                            ptr[10] = v4;
                            return ptr;
                        }
                    }
                }
LABEL_10eb40c:
                sub_f7db7c();
            }
        }
    }
    sub_f7db74();
}
```

## `bl_UIGradient.CreateSplitVertex` — RVA `0xceb414`

- Decompiled symbol: `bl_UIGradient_CreateSplitVertex`
- Metadata signature: `private UIVertex CreateSplitVertex(UIVertex vertex1, UIVertex vertex2, float stop) { }`
- Native interval: `340` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned int field_28;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned long long field_c;
    unsigned int field_14;
    char padding_18[16];
    unsigned int field_28;
    unsigned int field_2c;
    unsigned int field_30;
} struct_1;

int bl_UIGradient_CreateSplitVertex(struct_0 *a0, unsigned int *p, unsigned int *addr)
{
    unsigned int v3;  // s12
    unsigned int v4;  // s0
    struct_1 *ptr;  // x8
    unsigned int v5;  // s11
    unsigned int v6;  // s11
    unsigned int v7;  // s9
    unsigned int v8;  // w0
    unsigned int v9;  // s11
    unsigned int v10;  // s15
    char v0;  // [bp-0xc0]
    unsigned long v1;  // [bp-0xb4]
    unsigned int v2;  // [bp-0xac]

    if (a0->field_28)
    {
        v3 = p[2];
        v5 = (p[1] - v4) / (p[1] - addr[1]);
        memcpy(&v0);
        v6 = p[11] - v5 * (p[11] - addr[11]);
        v7 = p[12] - v5 * (p[12] - addr[12]);
        v8 = sub_10eb8d4(0);
        ptr->field_0 = *(p) - v5 * (*(p) - *(addr));
        ptr->field_4 = v4;
    }
    else
    {
        v3 = p[2];
        v9 = (*(p) - v4) / (*(p) - *(addr));
        v10 = p[1] - v9 * (p[1] - addr[1]);
        memcpy(&v0);
        v6 = p[11] - v9 * (p[11] - addr[11]);
        v7 = p[12] - v9 * (p[12] - addr[12]);
        v8 = sub_10eb8d4(0);
        ptr->field_0 = v4;
        ptr->field_4 = v10;
    }
    ptr->field_8 = v3;
    *((unsigned long *)&ptr->field_14) = 0;
    *((unsigned long *)&ptr->padding_18[4]) = 0;
    *((unsigned int *)&ptr->padding_18[12]) = v8;
    ptr->field_28 = v6;
    ptr->field_2c = v7;
    *((void*)&ptr[1].field_4) = 0;
    *((void*)((char *)&ptr[1].field_c + 4)) = 0;
    *((unsigned long *)&(&ptr->field_8)[1]) = v1;
    *((unsigned int *)((char *)&ptr->field_c + 4)) = v2;
    *((void*)&ptr[1].padding_18[8]) = 0;
    ptr->field_30 = 0;
    ptr[1].field_0 = 0;
    return v8;
}
```

## `bl_UIGradient.ctor` — RVA `0xceb568`

- Decompiled symbol: `bl_UIGradient_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `384` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_UIGradient_Recovered` matched 4 offsets against `bl_UIGradient` metadata (confidence 1.00).

```c
typedef struct bl_UIGradient_Recovered {
    char padding_0[44];
    unsigned int _blendMode;
    char _modifyVertices;
    char padding_31[7];
    unsigned int _zoom;
    char padding_3c[4];
    long long _effectGradient;
} bl_UIGradient_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    uint128_t field_20;
    unsigned int field_30;
    uint128_t field_34;
    unsigned int field_44;
} struct_1;

extern char g_1fab67b;

long long bl_UIGradient_ctor(struct_0 *ptr)
{
    long long v9;  // x20
    struct_1 *p;  // x21
    unsigned long v11;  // x0
    unsigned long long v12;  // x0
    int v0;  // [bp-0x90]
    unsigned int v1;  // [bp-0x80]
    int v2;  // [bp-0x78]
    unsigned int flag;  // [bp-0x68]
    int v4;  // [bp-0x60]
    unsigned int v5;  // [bp-0x50]
    unsigned long flag2;  // [bp-0x48]
    unsigned long long flag3;  // [bp-0x40]
    unsigned int choice;  // [bp-0x38]

    if (!(g_1fab67b & 1))
    {
        sub_f7d92c("'(");
        sub_f7d92c("3=");
        g_1fab67b = 1;
    }
    ptr->field_2c = 2;
    ptr->field_30 = 1;
    ptr->field_38 = 0x3f800000;
    v9 = sub_f7db70(g_1eefb70);
    Gradient__ctor(v9, 0);
    p = sub_f7d9d4(g_1eee158, 2);
    flag2 = 0;
    flag3 = 0;
    choice = 0;
    v11 = GradientColorKey__ctor(&flag2, 0);
    if (p)
    {
        memcpy(&v4, &flag2, 16);
        v5 = choice;
        if (p->field_18)
        {
            *((void*)&p->field_20) = v4;
            p->field_30 = v5;
            *((unsigned long long *)&v2) = 0;
            *((unsigned long long *)&(&v2)[8]) = 0;
            flag = 0;
            v11 = GradientColorKey__ctor(&v2, 0);
            v1 = flag;
            v0 = v2;
            if (p->field_18 > 1)
            {
                *((unsigned int *)((char *)&p->field_34 + 4)) = v1;
                *((void*)&(&p->field_30)[1]) = v0;
                if (v9)
                {
                    Gradient__set_colorKeys(v9, p, 0);
                    ptr->field_40 = v9;
                    sub_f7d8d0((struct bl_UIGradient_Recovered *)&ptr->field_40, v9);
                    v12 = BaseMeshEffect__ctor(ptr, 0);
                    return BaseMeshEffect__ctor(ptr, 0);
                }
                goto LABEL_10eb6e0;
            }
        }
    }
    else
    {
LABEL_10eb6e0:
        v11 = sub_f7db74();
    }
    sub_f7db7c(v11);
}
```

## `bl_UIGradient.<>c.cctor` — RVA `0xceb6e8`

- Decompiled symbol: `bl_UIGradient_c_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    long long field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef41c0;
extern char g_1fab67c;

void bl_UIGradient_c_cctor(void)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    long long v6;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab67c & 1))
    {
        sub_f7d92c(&g_1ef41c0);
        g_1fab67c = 1;
    }
    v6 = sub_f7db70(g_1ef41c0);
    Object__ctor(v6, 0);
    g_1ef41c0->field_b8->field_0 = v6;
    sub_f7d8d0();
    return;
}
```

## `bl_UIGradient.<>c.ctor` — RVA `0xceb750`

- Decompiled symbol: `bl_UIGradient_c_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long bl_UIGradient_c_ctor(void)
{
    long long v0;  // x0

    v0 = Object__ctor();
    return Object__ctor();
}
```

## `bl_UIGradient.<>c.<ModifyMesh>b__24_0` — RVA `0xceb758`

- Decompiled symbol: `bl_UIGradient_c_ModifyMesh_b__24_0`
- Metadata signature: `internal float <ModifyMesh>b__24_0(UIVertex v) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long bl_UIGradient_c_ModifyMesh_b__24_0(unsigned long a0, unsigned long a1)
{
    return a0;
}
```

## `bl_UIGradient.<>c.<ModifyMesh>b__24_1` — RVA `0xceb760`

- Decompiled symbol: `bl_UIGradient_c_ModifyMesh_b__24_1`
- Metadata signature: `internal float <ModifyMesh>b__24_1(UIVertex v) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long bl_UIGradient_c_ModifyMesh_b__24_1(unsigned long a0, unsigned long a1)
{
    return a0;
}
```
