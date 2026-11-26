# Native pseudocode: ScrollDeltaBinding

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ScrollDeltaBinding.ctor` — RVA `0xc5e460`

- Decompiled symbol: `ScrollDeltaBinding_ctor`
- Metadata signature: `public void .ctor(InputBindingBase parent) { }`
- Native interval: `280` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    long long field_18;
    long long field_20;
} struct_0;

extern unsigned int g_1f0c398;
extern char g_1fab2d8;

void ScrollDeltaBinding_ctor(struct_0 *addr, long long a1)
{
    unsigned long long v7;  // x30
    unsigned long long v8;  // x24
    unsigned long long v9;  // x23
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    struct_0 *ptr;  // x0
    long long v15;  // x20
    struct_0 *p;  // x0
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
    if (!(g_1fab2d8 & 1))
    {
        sub_f7d92c("g.");
        sub_f7d92c("y7");
        sub_f7d92c(&g_1f0c398);
        g_1fab2d8 = 1;
    }
    Object__ctor(addr, 0);
    ptr = addr;
    addr->field_10 = 0;
    ptr->field_18 = a1;
    sub_f7d8d0((struct struct_0 *)&ptr->field_18, a1);
    v15 = sub_f7db70(g_1eee9f8);
    AxisBinding__ctor(v15, *((long long *)&g_1f0c398), 0, addr);
    p = addr;
    p->field_20 = v15;
    sub_f7d8d0((struct struct_0 *)&p->field_20, v15);
    DigitalBinding__ctor(sub_f7db70(g_1eef590)); /* do not return */
}
```

## `ScrollDeltaBinding.ctor` — RVA `0xc5e578`

- Decompiled symbol: `ScrollDeltaBinding_ctor`
- Metadata signature: `public void .ctor(string axisName, bool enabled = false, InputBindingBase parent) { }`
- Native interval: `276` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    long long field_18;
    long long field_20;
} struct_0;

extern char g_1fab2d9;

void ScrollDeltaBinding_ctor(struct_0 *ptr, unsigned int a1, unsigned int a2, long long a3)
{
    unsigned long long v8;  // x30
    unsigned long long v9;  // x25
    long long v18;  // x22
    struct_0 *p;  // x0
    unsigned long long v10;  // x24
    unsigned long long v11;  // x23
    unsigned long long v12;  // x22
    unsigned long long v13;  // x21
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
    struct_0 *addr;  // x0
    unsigned int v17;  // w21
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
    if (!(g_1fab2d9 & 1))
    {
        sub_f7d92c("g.");
        sub_f7d92c("y7");
        g_1fab2d9 = 1;
    }
    Object__ctor(ptr, 0);
    addr = ptr;
    ptr->field_10 = 0;
    addr->field_18 = a3;
    sub_f7d8d0((struct struct_0 *)&addr->field_18, a3);
    v17 = a2 & 1;
    ptr->field_10 = v17;
    v18 = sub_f7db70(g_1eee9f8);
    AxisBinding__ctor(v18, a1, v17, ptr);
    p = ptr;
    p->field_20 = v18;
    sub_f7d8d0((struct struct_0 *)&p->field_20, v18);
    DigitalBinding__ctor(sub_f7db70(g_1eef590)); /* do not return */
}
```

## `ScrollDeltaBinding.CopyFrom` — RVA `0xc5e68c`

- Decompiled symbol: `ScrollDeltaBinding_CopyFrom`
- Metadata signature: `public void CopyFrom(ScrollDeltaBinding b) { }`
- Native interval: `136` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ScrollDeltaBinding_Recovered` matched 3 offsets against `ScrollDeltaBinding` metadata (confidence 0.75).

```c
typedef struct struct_2 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct ScrollDeltaBinding_Recovered *field_20;
    struct struct_1 *field_28;
} struct_2;

typedef struct ScrollDeltaBinding_Recovered {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct ScrollDeltaBinding_Recovered *deltaBinding;
    struct struct_6 *positiveDigitalBinding;
    struct struct_6 *negativeDigitalBinding;
} ScrollDeltaBinding_Recovered;

typedef struct ScrollDeltaBinding_Recovered {
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

typedef struct ScrollDeltaBinding_Recovered {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    unsigned long long field_20;
} struct_0;

typedef struct struct_6 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    unsigned long long field_20;
    struct struct_4 *field_28;
} struct_6;

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

struct_2 * ScrollDeltaBinding_CopyFrom(struct_2 *p, struct_0 *addr, unsigned long a2, unsigned long a3)
{
    unsigned int v0;  // w8
    struct_2 *v1;  // x20
    struct_2 *ptr;  // x9
    struct_2 *v4;  // x0

    if (addr)
    {
        v0 = addr->field_10;
        v1 = p;
        p->field_10 = v0;
        if (!v0)
            return p;
        ptr = v1;
        do
        {
            ptr->field_10 = 1;
            ptr = *((long long *)&ptr->padding_11[7]);
        } while (*((long long *)&ptr->padding_11[7]));
        if (v1->field_20)
        {
            AxisBinding__CopyFrom(v1->field_20, addr->field_20);
            if (v1->field_28)
            {
                DigitalBinding__CopyFrom(v1->field_28, addr->field_28);
                if (*((long long *)&v1[1].padding_0[0]))
                {
                    v4 = DigitalBinding__CopyFrom(*((long long *)&v1[1].padding_0[0]), addr->field_30);
                    return DigitalBinding__CopyFrom(*((long long *)&v1[1].padding_0[0]), addr->field_30);
                }
            }
        }
    }
    sub_f7db74();
}
```

## `ScrollDeltaBinding.OnGetSubBindingDescriptions` — RVA `0xc5e714`

- Decompiled symbol: `ScrollDeltaBinding_OnGetSubBindingDescriptions`
- Metadata signature: `protected override void OnGetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Native interval: `212` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ScrollDeltaBinding_Recovered` matched 2 offsets against `ScrollDeltaBinding` metadata (confidence 1.00).

```c
typedef struct ScrollDeltaBinding_Recovered {
    char padding_0[32];
    long long deltaBinding;
    struct struct_7 **positiveDigitalBinding;
} ScrollDeltaBinding_Recovered;

extern long long g_1f09a20;
extern long long g_1f0c570;
extern long long g_1f0cfd0;
extern char g_1fab2da;

void ScrollDeltaBinding_OnGetSubBindingDescriptions(struct_0 *a0, void* a1, unsigned int a2, long long a3)
{
    unsigned long long v7;  // x30
    unsigned long long v8;  // x24
    unsigned long long v9;  // x23
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
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
    if (!(g_1fab2da & 1))
    {
        sub_f7d92c(&g_1f09a20);
        sub_f7d92c(&g_1f0cfd0);
        sub_f7d92c(&g_1f0c570);
        g_1fab2da = 1;
    }
    if (a1)
    {
        BindingDescriptionList__Add(a1, a0->field_20, 5, g_1f09a20, a3, a2);
        BindingDescriptionList__Add(a1, a0->field_28, g_1f0cfd0, a3, a2); /* do not return */
    }
    sub_f7db74();
}
```

## `ScrollDeltaBinding.SyncScrollDelta` — RVA `0xc5e7e8`

- Decompiled symbol: `ScrollDeltaBinding_SyncScrollDelta`
- Metadata signature: `public void SyncScrollDelta(int delta, InputRig rig) { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    int field_18;
    char padding_1c[4];
    void* field_20;
    void* field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2db;

long long ScrollDeltaBinding_SyncScrollDelta(void* ptr, int a1, long long a2)
{
    unsigned long v0;  // x0
    unsigned long v1;  // x0
    unsigned long v2;  // x0
    struct_1 *v3;  // x0

    if (!(g_1fab2db & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab2db = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(a2, 0, 0);
    if (((char)v0 & 1))
    {
        return v0;
    }
    else if ((char)ptr[16])
    {
        v1 = (long long)ptr[32];
        if (v1)
        {
            v2 = AxisBinding__SyncScroll(v1, a1, a2);
            if (!a1)
            {
                return v2;
            }
            else if (a1 >= 1)
            {
                v1 = (long long)ptr[40];
                if (v1)
                {
                    v3 = DigitalBinding__Sync(v1, 1, a2, 0);
                    return DigitalBinding__Sync(v1, 1, a2, 0);
                }
            }
            else
            {
                v1 = (long long)ptr[48];
                if (v1)
                {
                    v3 = DigitalBinding__Sync(v1, 1, a2, 0);
                    return DigitalBinding__Sync(v1, 1, a2, 0);
                }
            }
        }
        sub_f7db74(v1);
    }
    else
    {
        return v0;
    }
}
```

## `ScrollDeltaBinding.OnIsBoundToAxis` — RVA `0xc5e8bc`

- Decompiled symbol: `ScrollDeltaBinding_OnIsBoundToAxis`
- Metadata signature: `protected override bool OnIsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `148` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct struct_3 *field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[488];
    struct struct_1 *field_1e8;
    unsigned long long field_1f0;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

unsigned int ScrollDeltaBinding_OnIsBoundToAxis(struct_2 *ptr, unsigned long a1, unsigned long a2)
{
    struct_0 **v0;  // x0
    unsigned long long v1;  // x3

    if (!ptr->field_10)
        return 0;
    v0 = ptr->field_20;
    if (!ptr->field_20)
        sub_f7db74(0);
    v1 = ptr->field_20->field_0->field_1f0;
    ptr->field_20->field_0->field_1e8();
}
```

## `ScrollDeltaBinding.OnIsBoundToKey` — RVA `0xc5e950`

- Decompiled symbol: `ScrollDeltaBinding_OnIsBoundToKey`
- Metadata signature: `protected override bool OnIsBoundToKey(KeyCode keyCode, InputRig rig) { }`
- Native interval: `148` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct struct_3 *field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[472];
    struct struct_1 *field_1d8;
    unsigned long long field_1e0;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

unsigned int ScrollDeltaBinding_OnIsBoundToKey(struct_2 *ptr, unsigned long a1, unsigned long a2)
{
    struct_0 **v0;  // x0
    unsigned long long v1;  // x3

    if (!ptr->field_10)
        return 0;
    v0 = ptr->field_20;
    if (!ptr->field_20)
        sub_f7db74(0);
    v1 = ptr->field_20->field_0->field_1e0;
    ptr->field_20->field_0->field_1d8();
}
```
