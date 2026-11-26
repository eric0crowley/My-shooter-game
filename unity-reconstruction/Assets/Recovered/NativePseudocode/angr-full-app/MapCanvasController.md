# Native pseudocode: MapCanvasController

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MapCanvasController.get_Instance` — RVA `0xc7a3fc`

- Decompiled symbol: `MapCanvasController_get_Instance`
- Metadata signature: `public static MapCanvasController get_Instance() { }`
- Native interval: `304` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[24];
    unsigned long long field_18;
    long long field_20;
} struct_2;

typedef struct struct_1 {
    long long field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

typedef struct struct_3 {
    char padding_0[224];
    unsigned int field_e0;
} struct_3;

typedef struct struct_4 {
    char padding_0[224];
    unsigned int field_e0;
} struct_4;

extern struct_3 *g_1eef458;
extern struct_0 *g_1ef0778;
extern struct_4 *g_1ef0c58;
extern long long g_1f00220;
extern long long g_1f0fe38;
extern char g_1fab3d2;

long long MapCanvasController_get_Instance(void)
{
    struct_2 *ptr;  // x0
    long long v1;  // x1

    if (!(g_1fab3d2 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef0778);
        sub_f7d92c(&g_1f00220);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0fe38);
        g_1fab3d2 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Implicit(g_1ef0778->field_b8->field_0, 0) & 1))
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        ptr = sub_1129ea4(g_1f00220);
        if (!ptr)
        {
            sub_f7db74();
        }
        else if (ptr->field_18)
        {
            if ((unsigned int)ptr->field_18 == 1)
            {
                v1 = ptr->field_20;
                g_1ef0778->field_b8->field_0 = v1;
                sub_f7d8d0(g_1ef0778->field_b8, v1);
            }
            else
            {
                if (!g_1eef458->field_e0)
                    sub_f7da5c(g_1eef458);
                Debug__LogError(g_1f0fe38, 0);
            }
        }
    }
    return g_1ef0778->field_b8->field_0;
}
```

## `MapCanvasController.Start` — RVA `0xc7a52c`

- Decompiled symbol: `MapCanvasController_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long MapCanvasController_Start(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `MapCanvasController.get_InnerMapComponent` — RVA `0xc7a530`

- Decompiled symbol: `MapCanvasController_get_InnerMapComponent`
- Metadata signature: `public InnerMap get_InnerMapComponent() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[72];
    unsigned long long field_48;
} struct_0;

long long MapCanvasController_get_InnerMapComponent(struct_0 *a0)
{
    return a0->field_48;
}
```

## `MapCanvasController.get_MarkerGroup` — RVA `0xc7a538`

- Decompiled symbol: `MapCanvasController_get_MarkerGroup`
- Metadata signature: `public MarkerGroup get_MarkerGroup() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[88];
    unsigned long long field_58;
} struct_0;

long long MapCanvasController_get_MarkerGroup(struct_0 *a0)
{
    return a0->field_58;
}
```

## `MapCanvasController.Awake` — RVA `0xc7a540`

- Decompiled symbol: `MapCanvasController_Awake`
- Metadata signature: `private void Awake() { }`
- Native interval: `676` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MapCanvasController_Recovered` matched 6 offsets against `MapCanvasController` metadata (confidence 1.00).

```c
typedef struct MapCanvasController_Recovered {
    char padding_0[32];
    long long playerTransform;
    char padding_28[24];
    long long mapRect;
    long long innerMap;
    long long mapArrow;
    long long markerGroup;
    unsigned int innerMapRadius;
} MapCanvasController_Recovered;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern struct_1 *g_1ef0c58;
extern long long g_1efd060;
extern long long g_1efd120;
extern long long g_1efd128;
extern long long g_1efd130;
extern long long g_1f0aff8;
extern long long g_1f0bfe8;
extern long long g_1f0c128;
extern long long g_1f0fe68;
extern char g_1fab3d3;

void MapCanvasController_Awake(struct_2 *ptr4)
{
    long long v0;  // x1
    struct_2 *ptr;  // x0
    struct_2 *v10;  // x21
    unsigned int v11;  // s0
    long long v2;  // x0
    struct_2 *p;  // x20
    struct_2 *v4;  // x20
    long long v5;  // x0
    struct_2 *addr;  // x21
    struct_2 *v7;  // x21
    long long v8;  // x0
    struct_2 *ptr3;  // x21

    if (!(g_1fab3d3 & 1))
    {
        sub_f7d92c(&g_1efd120);
        sub_f7d92c(&g_1efd128);
        sub_f7d92c(&g_1efd130);
        sub_f7d92c(&g_1efd060);
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0fe68);
        sub_f7d92c(&g_1f0c128);
        sub_f7d92c(&g_1f0aff8);
        sub_f7d92c(&g_1f0bfe8);
        g_1fab3d3 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Implicit(ptr4->field_20, 0) & 1))
    {
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        Debug__LogError(g_1f0fe68, 0);
    }
    v0 = sub_1231bc8(ptr4, g_1efd060);
    ptr = ptr4;
    ptr->field_40 = v0;
    sub_f7d8d0((struct MapCanvasController_Recovered *)&ptr->field_40, v0);
    v2 = sub_1231e2c(ptr4, g_1efd120);
    p = ptr4;
    p->field_48 = v2;
    v4 = &p->field_48;
    sub_f7d8d0(v4, v2);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Implicit(*((long long *)&v4->padding_0[0]), 0) & 1))
    {
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        Debug__LogError(g_1f0aff8, 0);
    }
    v5 = sub_1231e2c(ptr4, g_1efd128);
    addr = ptr4;
    addr->field_50 = v5;
    v7 = &addr->field_50;
    sub_f7d8d0(v7, v5);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Implicit(*((long long *)&v7->padding_0[0]), 0) & 1))
    {
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        Debug__LogError(g_1f0bfe8, 0);
    }
    v8 = sub_1231e2c(ptr4, g_1efd130);
    ptr3 = ptr4;
    ptr3->field_58 = v8;
    v10 = &ptr3->field_58;
    sub_f7d8d0(v10, v8);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Implicit(*((long long *)&v10->padding_0[0]), 0) & 1))
    {
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        Debug__LogError(g_1f0c128, 0);
    }
    if (*((long long *)&v4->padding_0[0]))
    {
        InnerMap__getMapRadius(*((long long *)&v4->padding_0[0]));
        ptr4->field_60 = v11;
        return;
    }
    sub_f7db74(0);
}
```

## `MapCanvasController.Update` — RVA `0xc7a7e4`

- Decompiled symbol: `MapCanvasController_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `312` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MapCanvasController_Recovered` matched 4 offsets against `MapCanvasController` metadata (confidence 1.00).

```c
typedef struct MapCanvasController_Recovered {
    char padding_0[32];
    unsigned long long playerTransform;
    char padding_28[12];
    char rotateMap;
    char padding_35[11];
    long long mapRect;
    char padding_48[8];
    unsigned long long mapArrow;
} MapCanvasController_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2cb;
extern char g_1fab3d4;

long long MapCanvasController_Update(struct_1 *ptr)
{
    long long v0;  // x0
    unsigned long long v1;  // x0
    unsigned long long v2;  // x19

    if (!(g_1fab3d4 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab3d4 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Implicit(ptr->field_20, 0);
    if (!((char)v0 & 1))
        return v0;
    if (ptr->field_34)
    {
        v1 = ptr->field_20;
        if (v1)
        {
            Transform__get_eulerAngles(v1, 0);
            v1 = Quaternion__Internal_FromEulerRad(0);
            if (ptr->field_40)
            {
                v1 = Transform__set_rotation(ptr->field_40, 0);
                v2 = ptr->field_50;
                if (!g_1fab2cb)
                {
                    v1 = sub_f7d92c("-M");
                    g_1fab2cb = 1;
                }
                if (v2)
                {
LABEL_107a8ac:
                    MapArrow__rotate(); /* do not return */
                }
            }
        }
    }
    else
    {
        v1 = ptr->field_20;
        if (v1)
        {
            Transform__get_eulerAngles(v1, 0);
            v1 = Quaternion__Internal_FromEulerRad(0);
            if (ptr->field_50)
                goto LABEL_107a8ac;
        }
    }
    sub_f7db74(v1);
}
```

## `MapCanvasController.checkIn` — RVA `0xc7a91c`

- Decompiled symbol: `MapCanvasController_checkIn`
- Metadata signature: `public void checkIn(MapMarker marker) { }`
- Native interval: `792` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MapCanvasController_Recovered` matched 7 offsets against `MapCanvasController` metadata (confidence 1.00).

```c
typedef struct MapCanvasController_Recovered {
    char padding_0[32];
    long long playerTransform;
    unsigned int radarDistance;
    char hideOutOfRadius;
    char useOpacity;
    char padding_2e[2];
    unsigned int maxRadarDistance;
    char padding_34[4];
    unsigned int scale;
    unsigned int minimalOpacity;
} MapCanvasController_Recovered;

typedef struct struct_3 {
    char padding_0[44];
    char field_2c;
} struct_3;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern struct_1 *g_1ef0c58;
extern long long g_1f0c058;
extern char g_1fab3d5;

long long MapCanvasController_checkIn(struct_2 *ptr, struct_3 *a1)
{
    long long v0;  // x0
    unsigned int v1;  // s0
    unsigned long v10;  // 4172
    unsigned long long v11;  // x0
    unsigned int v2;  // s13
    unsigned long v3;  // 4125
    unsigned int v4;  // s1
    unsigned long v5;  // 4138
    unsigned int v6;  // s1
    unsigned long v7;  // 4138
    unsigned int v8;  // s0
    unsigned int v9;  // s1

    if (!(g_1fab3d5 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0c058);
        g_1fab3d5 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Implicit(ptr->field_20, 0);
    if (!((char)v0 & 1))
        return v0;
    if (a1)
    {
        if (a1->field_2c)
        {
            v1 = ptr->field_28;
            v2 = v1 * ptr->field_38;
            MapMarker__getPosition();
            MapCanvasController__distanceToPlayer(ptr);
            v3 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) & ((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v3))
            {
                if (!ptr->field_2c)
                {
                    v4 = ptr->field_38 * ptr->field_30;
                    v5 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v1, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v4) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v4) & 1)) & ((unsigned long long)(char)(CmpF(v1, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v4) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if (!((char)v5))
                    {
                        MapMarker__isVisible(a1); /* do not return */
                    }
                    else if (ptr->field_2d)
                    {
                        v6 = v4 - v2;
                        v7 = arm64g_calculate_condition(144, (((((unsigned long long)(char)(CmpF(v6, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v6, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v6, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v6, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v6, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v6, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v7))
                        {
                            v8 = ptr->field_3c;
                            v9 = (v1 - v2) / v6;
                            v10 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(0x3f800000 - v9, v8)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 - v9, v8) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(0x3f800000 - (v1 - v2) / v6, v8)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 - (v1 - v2) / v6, v8) & 1)) & ((unsigned long long)(char)(CmpF(0x3f800000 - (v1 - v2) / v6, v8)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 - (v1 - v2) / v6, v8) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        }
                        else
                        {
                            if (!g_1eef458->field_e0)
                                sub_f7da5c(g_1eef458);
                            v11 = Debug__LogError();
                            return Debug__LogError();
                        }
                    }
                }
                else
                {
                    MapMarker__isVisible(a1); /* do not return */
                }
            }
            MapMarker__isVisible(a1); /* do not return */
        }
        else
        {
            MapMarker__isVisible(a1); /* do not return */
        }
    }
    sub_f7db74();
}
```

## `MapCanvasController.distanceToPlayer` — RVA `0xc7ac60`

- Decompiled symbol: `MapCanvasController_distanceToPlayer`
- Metadata signature: `private float distanceToPlayer(Vector3 other) { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern char g_1fab3e4;

struct_2 * MapCanvasController_distanceToPlayer(struct_0 *ptr)
{
    unsigned long long v0;  // x0
    struct_1 *v1;  // x0

    v0 = ptr->field_20;
    if (v0)
    {
        Transform__get_position(v0, 0);
        v0 = ptr->field_20;
        if (v0)
        {
            Transform__get_position(v0, 0);
            if (!g_1fab3e4)
            {
                sub_f7d92c("_F");
                g_1fab3e4 = 1;
            }
            v1 = g_1ef07e8;
            if (!g_1ef07e8->field_e0)
                v1 = sub_f7da5c(g_1ef07e8);
            return v1;
        }
    }
    sub_f7db74(v0);
}
```

## `MapCanvasController.ctor` — RVA `0xc7ae08`

- Decompiled symbol: `MapCanvasController_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `40` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MapCanvasController_Recovered` matched 4 offsets against `MapCanvasController` metadata (confidence 1.00).

```c
typedef struct MapCanvasController_Recovered {
    char padding_0[40];
    unsigned int radarDistance;
    unsigned short hideOutOfRadius;
    char padding_2e[2];
    unsigned int maxRadarDistance;
    char padding_34[4];
    unsigned long long scale;
} MapCanvasController_Recovered;

long long MapCanvasController_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_28 = 0x41200000;
    ptr->field_2c = 257;
    ptr->field_30 = 0x41200000;
    ptr->field_38 = 0x3e99999a3f800000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
