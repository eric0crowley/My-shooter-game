# Native pseudocode: DirectionBinding

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DirectionBinding.ctor` — RVA `0xc5c9ec`

- Decompiled symbol: `DirectionBinding_ctor`
- Metadata signature: `public void .ctor(InputBindingBase parent) { }`
- Native interval: `576` bytes
- Result: `pseudocode`

```c
extern char g_1fab2c5;

long long DirectionBinding_ctor(long long a0, long long a1)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
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
    if (!(g_1fab2c5 & 1))
    {
        sub_f7d92c("y7");
        g_1fab2c5 = 1;
    }
    InputBindingBase__ctor(a0, a1, 0); /* do not return */
}
```

## `DirectionBinding.CopyFrom` — RVA `0xc5cc2c`

- Decompiled symbol: `DirectionBinding_CopyFrom`
- Metadata signature: `public void CopyFrom(DirectionBinding b) { }`
- Native interval: `244` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DirectionBinding_Recovered` matched 12 offsets against `DirectionBinding` metadata (confidence 0.92).

```c
typedef struct struct_1 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    char field_20;
    char padding_21[3];
    unsigned int field_24;
    struct struct_2 *field_28;
    struct struct_2 *field_30;
    struct struct_2 *field_38;
    struct struct_2 *field_40;
    struct struct_2 *field_48;
    struct struct_2 *field_50;
    char padding_58[8];
    struct struct_2 *field_60;
    struct struct_2 *field_68;
    struct struct_2 *field_70;
} struct_1;

typedef struct DirectionBinding_Recovered {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    char bindDiagonals;
    char padding_21[3];
    unsigned int bindMode;
    struct struct_6 *dirBindingU;
    struct struct_6 *dirBindingUR;
    struct struct_6 *dirBindingR;
    struct struct_6 *dirBindingDR;
    struct struct_6 *dirBindingD;
    struct struct_6 *dirBindingDL;
    struct struct_6 *dirBindingL;
    struct struct_6 *dirBindingUL;
    struct struct_6 *dirBindingN;
    struct struct_6 *dirBindingAny;
} DirectionBinding_Recovered;

typedef struct struct_2 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct DirectionBinding_Recovered *field_20;
    struct struct_1 *field_28;
} struct_2;

typedef struct struct_6 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    unsigned long long field_20;
    struct struct_4 *field_28;
} struct_6;

typedef struct DirectionBinding_Recovered {
    char padding_0[16];
    long long field_10;
    int field_18;
    unsigned int field_1c;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
    unsigned int field_1c;
} struct_1;

typedef struct struct_4 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct struct_3 *field_20;
    struct struct_5 *field_28;
} struct_4;

typedef struct struct_3 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_3;

typedef struct struct_5 {
    char padding_0[24];
    unsigned int field_18;
    unsigned int field_1c;
} struct_5;

struct_1 * DirectionBinding_CopyFrom(struct_1 *ptr, struct_0 *p, unsigned long a2, unsigned long a3)
{
    unsigned int v0;  // w8
    unsigned long v1;  // x0
    struct_2 *v2;  // x0

    if (p)
    {
        v0 = p->field_10;
        ptr->field_10 = v0;
        if (!v0)
            return ptr;
        InputBindingBase__Enable(ptr, 0);
        v1 = ptr->field_68;
        ptr->field_20 = p->field_20;
        ptr->field_24 = p->field_24;
        if (v1)
        {
            DigitalBinding__CopyFrom(v1, p->field_68);
            if (ptr->field_70)
            {
                DigitalBinding__CopyFrom(ptr->field_70, p->field_70);
                if (ptr->field_28)
                {
                    DigitalBinding__CopyFrom(ptr->field_28, p->field_28);
                    if (ptr->field_30)
                    {
                        DigitalBinding__CopyFrom(ptr->field_30, p->field_30);
                        if (ptr->field_38)
                        {
                            DigitalBinding__CopyFrom(ptr->field_38, p->field_38);
                            if (ptr->field_40)
                            {
                                DigitalBinding__CopyFrom(ptr->field_40, p->field_40);
                                if (ptr->field_48)
                                {
                                    DigitalBinding__CopyFrom(ptr->field_48, p->field_48);
                                    if (ptr->field_50)
                                    {
                                        DigitalBinding__CopyFrom(ptr->field_50, p->field_50);
                                        if (ptr->field_48)
                                        {
                                            DigitalBinding__CopyFrom(ptr->field_48, p->field_58);
                                            if (ptr->field_60)
                                            {
                                                v2 = DigitalBinding__CopyFrom(ptr->field_60, p->field_60);
                                                return DigitalBinding__CopyFrom(ptr->field_60, p->field_60);
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
    sub_f7db74();
}
```

## `DirectionBinding.OnGetSubBindingDescriptions` — RVA `0xc5cd20`

- Decompiled symbol: `DirectionBinding_OnGetSubBindingDescriptions`
- Metadata signature: `protected override void OnGetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Native interval: `640` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[104];
    long long field_68;
} struct_0;

extern long long g_1f085c0;
extern long long g_1f09b90;
extern long long g_1f09ba0;
extern long long g_1f09ba8;
extern long long g_1f0bc58;
extern long long g_1f0c5b0;
extern long long g_1f0d620;
extern char g_1fab2c6;

long long DirectionBinding_OnGetSubBindingDescriptions(struct_0 *a0, long long a1, long long a2, long long a3)
{
    unsigned long long v8;  // x30
    unsigned long long v9;  // x25
    unsigned long long v10;  // x24
    unsigned long long v11;  // x23
    unsigned long long v12;  // x22
    unsigned long long v13;  // x21
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x38]
    unsigned long long v2;  // [bp-0x30]
    unsigned long long v3;  // [bp-0x28]
    unsigned long long v4;  // [bp-0x20]
    unsigned long long v5;  // [bp-0x18]
    unsigned long long v6;  // [bp-0x10]
    unsigned long long v7;  // [bp-0x8]

    v0 = v8;
    v1 = v9;
    v2 = v10;
    v3 = v11;
    v4 = v12;
    v5 = v13;
    v6 = v14;
    v7 = v15;
    if (!(g_1fab2c6 & 1))
    {
        sub_f7d92c(&g_1f085c0);
        sub_f7d92c(&g_1f0d620);
        sub_f7d92c("Y%");
        sub_f7d92c(&g_1f09ba8);
        sub_f7d92c(&g_1f09b90);
        sub_f7d92c("S%");
        sub_f7d92c(&g_1f09ba0);
        sub_f7d92c(&g_1f0c5b0);
        sub_f7d92c(&g_1f0bc58);
        sub_f7d92c("W%");
        g_1fab2c6 = 1;
    }
    if (a1)
        BindingDescriptionList__Add(a1, a0->field_68, g_1f0c5b0, a3, a2, 0); /* do not return */
    sub_f7db74();
}
```

## `DirectionBinding.SyncDirectionState` — RVA `0xc5cfa0`

- Decompiled symbol: `DirectionBinding_SyncDirectionState`
- Metadata signature: `public void SyncDirectionState(DirectionState dirState, InputRig rig) { }`
- Native interval: `188` bytes
- Result: `pseudocode`

```c
extern char g_852128;

long long DirectionBinding_SyncDirectionState(unsigned long a0)
{
    if (5 < *((int *)(a0 + 36)))
        return a0;
    goto sub_105cfc8 + (&g_852128)[*((int *)(a0 + 36))] * 4;
}
```

## `DirectionBinding.SyncDirRaw` — RVA `0xc5d05c`

- Decompiled symbol: `DirectionBinding_SyncDirRaw`
- Metadata signature: `public void SyncDirRaw(Dir dir, InputRig rig) { }`
- Native interval: `508` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DirectionBinding_Recovered` matched 3 offsets against `DirectionBinding` metadata (confidence 0.75).

```c
typedef struct DirectionBinding_Recovered {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    char bindDiagonals;
    char padding_21[15];
    unsigned long long dirBindingUR;
    char padding_38[56];
    unsigned long long dirBindingAny;
} DirectionBinding_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2c7;
extern char g_85212e;
extern char g_852137;

long long DirectionBinding_SyncDirRaw(struct_1 *ptr, unsigned int a1, long long a2)
{
    unsigned long v0;  // x0
    unsigned long i;  // x0
    struct_1 *v2;  // x0

    if (!(g_1fab2c7 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab2c7 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(a2, 0, 0);
    if (((char)v0 & 1))
    {
        return v0;
    }
    else if (ptr->field_10)
    {
        if (a1)
        {
            i = ptr->field_70;
            if (i)
            {
                v0 = DigitalBinding__Sync(i, 1, a2, 0);
            }
            else
            {
                do
                {
                    sub_f7db74(i);
                    i = ptr->field_30;
                } while (!i);
                v2 = DigitalBinding__Sync(i, 1, a2, 0);
                return DigitalBinding__Sync(i, 1, a2, 0);
            }
        }
        if (ptr->field_20)
        {
            if (8 >= a1)
                goto sub_105d110 + (&g_85212e)[a1] * 4;
            else
                return v0;
        }
        else
        {
            if (7 >= a1 - 1)
                goto sub_105d140 + (&g_852137)[1 + a1] * 4;
            else
                return v0;
        }
    }
    else
    {
        return v0;
    }
}
```

## `DirectionBinding.OnIsBoundToAxis` — RVA `0xc5d258`

- Decompiled symbol: `DirectionBinding_OnIsBoundToAxis`
- Metadata signature: `protected override bool OnIsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `340` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[87];
    long long field_68;
} struct_0;

unsigned long long DirectionBinding_OnIsBoundToAxis(struct_0 *a0, unsigned long a1, unsigned long a2)
{
    if (!a0->field_10)
        return 0;
    if (a0->field_68)
        InputBindingBase__IsBoundToAxis(a0->field_68); /* do not return */
    sub_f7db74(0);
}
```

## `DirectionBinding.OnIsBoundToKey` — RVA `0xc5d3ac`

- Decompiled symbol: `DirectionBinding_OnIsBoundToKey`
- Metadata signature: `protected override bool OnIsBoundToKey(KeyCode keyCode, InputRig rig) { }`
- Native interval: `340` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[87];
    long long field_68;
} struct_0;

unsigned long long DirectionBinding_OnIsBoundToKey(struct_0 *a0, unsigned long a1, unsigned long a2)
{
    if (!a0->field_10)
        return 0;
    if (a0->field_68)
        InputBindingBase__IsBoundToKey(a0->field_68); /* do not return */
    sub_f7db74(0);
}
```
