# Native pseudocode: bl_MiniMapDragArea

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_MiniMapDragArea.Awake` — RVA `0xcca4a0`

- Decompiled symbol: `bl_MiniMapDragArea_Awake`
- Metadata signature: `private void Awake() { }`
- Native interval: `200` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MiniMapDragArea_Recovered` matched 4 offsets against `bl_MiniMapDragArea` metadata (confidence 1.00).

```c
typedef struct bl_MiniMapDragArea_Recovered {
    char padding_0[32];
    struct struct_0 *MiniMap;
    char padding_28[8];
    unsigned long long direction;
    char padding_38[8];
    char touched;
    char padding_41[7];
    unsigned long long cursorIcon;
} bl_MiniMapDragArea_Recovered;

typedef struct struct_2 {
    char padding_0[264];
    unsigned long long field_108;
} struct_2;

typedef struct struct_0 {
    char padding_0[264];
    unsigned long long field_108;
} struct_0;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

typedef struct struct_3 {
    char padding_0[184];
    struct struct_4 *field_b8;
} struct_3;

extern struct_3 *g_1ef22b8;
extern long long g_1efd160;
extern char g_1fab1e0;
extern char g_1fab574;

void bl_MiniMapDragArea_Awake(struct_1 *ptr)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_2 *v6;  // x1
    unsigned long long v7;  // d0
    struct_0 *index;  // x8
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab574 & 1))
    {
        sub_f7d92c(&g_1efd160);
        g_1fab574 = 1;
    }
    if (Component__get_transform(ptr, 0) && Transform__get_root())
    {
        v6 = sub_1231e2c();
        ptr->field_20 = v6;
        sub_f7d8d0((struct bl_MiniMapDragArea_Recovered *)&ptr->field_20, v6);
        if (!g_1fab1e0)
        {
            sub_f7d92c(&g_1ef22b8);
            g_1fab1e0 = 1;
        }
        v7 = g_1ef22b8->field_b8->field_0;
        index = ptr->field_20;
        ptr->field_40 = 0;
        ptr->field_30 = v7;
        if (index)
        {
            ptr->field_48 = index->field_108;
            sub_f7d8d0();
            return;
        }
    }
    sub_f7db74();
}
```

## `bl_MiniMapDragArea.OnPointerDown` — RVA `0xcca568`

- Decompiled symbol: `bl_MiniMapDragArea_OnPointerDown`
- Metadata signature: `public void OnPointerDown(PointerEventData data) { }`
- Native interval: `212` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MiniMapDragArea_Recovered` matched 4 offsets against `bl_MiniMapDragArea` metadata (confidence 1.00).

```c
typedef struct bl_MiniMapDragArea_Recovered {
    char padding_0[32];
    struct struct_1 *MiniMap;
    unsigned long long origin;
    char padding_30[16];
    char touched;
    char padding_41[3];
    unsigned int pointerID;
} bl_MiniMapDragArea_Recovered;

typedef struct struct_1 {
    char padding_0[240];
    char field_f0;
} struct_1;

typedef struct struct_3 {
    char padding_0[256];
    unsigned int field_100;
    unsigned long long field_104;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab575;

long long bl_MiniMapDragArea_OnPointerDown(struct_2 *ptr, struct_3 *index)
{
    long long v0;  // x0

    if (!(g_1fab575 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab575 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(ptr->field_20, 0, 0);
    if (((char)v0 & 1))
        return v0;
    if (ptr->field_20)
    {
        if (!ptr->field_20->field_f0)
        {
            return v0;
        }
        else if (ptr->field_40)
        {
            return v0;
        }
        else
        {
            ptr->field_40 = 1;
            if (index)
            {
                ptr->field_44 = index->field_100;
                ptr->field_28 = *((long long *)&(&index->field_100)[1]);
            }
        }
    }
    sub_f7db74();
}
```

## `bl_MiniMapDragArea.OnDrag` — RVA `0xcca63c`

- Decompiled symbol: `bl_MiniMapDragArea_OnDrag`
- Metadata signature: `public void OnDrag(PointerEventData data) { }`
- Native interval: `224` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MiniMapDragArea_Recovered` matched 4 offsets against `bl_MiniMapDragArea` metadata (confidence 1.00).

```c
typedef struct bl_MiniMapDragArea_Recovered {
    char padding_0[32];
    struct struct_1 *MiniMap;
    unsigned long long origin;
    unsigned long long direction;
    char padding_38[12];
    unsigned int pointerID;
} bl_MiniMapDragArea_Recovered;

typedef struct struct_1 {
    char padding_0[240];
    char field_f0;
} struct_1;

typedef struct struct_3 {
    char padding_0[260];
    unsigned long long field_104;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab576;

long long bl_MiniMapDragArea_OnDrag(struct_2 *ptr, struct_3 *index)
{
    unsigned long v0;  // x0
    struct_1 *v1;  // x0
    unsigned long v3;  // x0

    if (!(g_1fab576 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab576 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(ptr->field_20, 0, 0);
    if (((char)v0 & 1))
        return v0;
    if (ptr->field_20)
    {
        if (!ptr->field_20->field_f0)
        {
            return v0;
        }
        else if (index)
        {
            if (*((int *)&index->padding_0[0x100]) == ptr->field_44)
            {
                Time__get_deltaTime(0);
                v1 = ptr->field_20;
                ptr->field_30 = [D] unsupported_Iop_ZeroHI64ofV128();
                if (v1)
                {
                    v3 = (unsigned long long)bl_MiniMap__SetDragPosition(v1);
                    ptr->field_28 = *((long long *)&(&index->padding_0)[1]);
                    return v3;
                }
            }
            else
            {
                return v0;
            }
        }
    }
    sub_f7db74();
}
```

## `bl_MiniMapDragArea.OnPointerUp` — RVA `0xcca71c`

- Decompiled symbol: `bl_MiniMapDragArea_OnPointerUp`
- Metadata signature: `public void OnPointerUp(PointerEventData data) { }`
- Native interval: `252` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MiniMapDragArea_Recovered` matched 4 offsets against `bl_MiniMapDragArea` metadata (confidence 1.00).

```c
typedef struct bl_MiniMapDragArea_Recovered {
    char padding_0[32];
    struct struct_1 *MiniMap;
    char padding_28[8];
    unsigned long long direction;
    char padding_38[8];
    char touched;
    char padding_41[3];
    unsigned int pointerID;
} bl_MiniMapDragArea_Recovered;

typedef struct struct_1 {
    char padding_0[240];
    char field_f0;
} struct_1;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_3 {
    char padding_0[184];
    struct struct_4 *field_b8;
} struct_3;

extern struct_0 *g_1ef0c58;
extern struct_3 *g_1ef22b8;
extern char g_1fab1e0;
extern char g_1fab577;

long long bl_MiniMapDragArea_OnPointerUp(struct_2 *ptr, unsigned long long a1)
{
    long long v0;  // x0
    unsigned long long v1;  // d0

    if (!(g_1fab577 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab577 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(ptr->field_20, 0, 0);
    if (((char)v0 & 1))
        return v0;
    if (ptr->field_20)
    {
        if (!ptr->field_20->field_f0)
        {
            return v0;
        }
        else if (a1)
        {
            if (*((int *)(a1 + 0x100)) == ptr->field_44)
            {
                if (!g_1fab1e0)
                {
                    sub_f7d92c(&g_1ef22b8);
                    g_1fab1e0 = 1;
                }
                v1 = g_1ef22b8->field_b8->field_0;
                ptr->field_40 = 0;
                ptr->field_30 = v1;
            }
            else
            {
                return v0;
            }
        }
    }
    sub_f7db74();
}
```

## `bl_MiniMapDragArea.ctor` — RVA `0xcca818`

- Decompiled symbol: `bl_MiniMapDragArea_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long bl_MiniMapDragArea_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
