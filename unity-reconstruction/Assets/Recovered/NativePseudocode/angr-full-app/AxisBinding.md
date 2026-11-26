# Native pseudocode: AxisBinding

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AxisBinding.ctor` — RVA `0xc4eac4`

- Decompiled symbol: `AxisBinding_ctor`
- Metadata signature: `public void .ctor(InputBindingBase parent) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
void AxisBinding_ctor(unsigned long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    InputBindingBase__ctor(); /* do not return */
}
```

## `AxisBinding.SyncFloat` — RVA `0xc4f160`

- Decompiled symbol: `AxisBinding_SyncFloat`
- Metadata signature: `public void SyncFloat(float val, InputRig.InputSource source, InputRig rig) { }`
- Native interval: `240` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_2 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef8ee8;
extern long long g_1ef8ef0;
extern char g_1fab2b1;

struct_3 * AxisBinding_SyncFloat(struct_2 *ptr, unsigned long a1, long long a2)
{
    struct_3 *v0;  // x0
    struct_1 *v1;  // x0
    int v2;  // w22
    unsigned long v3;  // x0

    if (!(g_1fab2b1 & 1))
    {
        sub_f7d92c(&g_1ef8ee8);
        sub_f7d92c(&g_1ef8ef0);
        sub_f7d92c(&g_1ef0c58);
        g_1fab2b1 = 1;
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
        v1 = ptr->field_20;
        if (v1)
        {
            v2 = 0;
            do
            {
                if (v1->field_18 <= v2)
                    return v1;
            } while ((v1 = (struct_1 *)(unsigned long long)sub_14a30c0(), v1 && (AxisBinding_TargetElem__SyncFloat(), v1 = (struct_1 *)ptr->field_20, v2 = (int)(v2 + 1), v1)));
        }
        v3 = sub_f7db74(v1);
        return sub_f7db74(v1);
    }
    else
    {
        return v0;
    }
}
```

## `AxisBinding.ctor` — RVA `0xc56d68`

- Decompiled symbol: `AxisBinding_ctor`
- Metadata signature: `public void .ctor(string singleName, bool enabled, InputBindingBase parent) { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
void AxisBinding_ctor(unsigned long a0, unsigned long a1, unsigned long a2, unsigned long a3)
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
    InputBindingBase__ctor(); /* do not return */
}
```

## `AxisBinding.BasicConstructor` — RVA `0xc5b3b8`

- Decompiled symbol: `AxisBinding_BasicConstructor`
- Metadata signature: `private void BasicConstructor() { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    long long field_20;
} struct_0;

extern long long g_1eed9a0;
extern long long g_1ef8ec8;
extern char g_1fab2ab;

void AxisBinding_BasicConstructor(struct_0 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x0
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
    if (!(g_1fab2ab & 1))
    {
        sub_f7d92c(&g_1ef8ec8);
        sub_f7d92c(&g_1eed9a0);
        g_1fab2ab = 1;
    }
    ptr->field_10 = 0;
    v10 = sub_f7db70(g_1eed9a0);
    sub_14a2bd4(v10, 1, g_1ef8ec8);
    ptr->field_20 = v10;
    sub_f7d8d0();
    return;
}
```

## `AxisBinding.AddTarget` — RVA `0xc5b43c`

- Decompiled symbol: `AxisBinding_AddTarget`
- Metadata signature: `public AxisBinding.TargetElem AddTarget() { }`
- Native interval: `208` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_1;

typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1ef2c58;
extern long long g_1ef8ed0;
extern char g_1fab2ae;

long long AxisBinding_AddTarget(struct_2 *p, unsigned long a1, unsigned long a2)
{
    long long v0;  // x19
    struct_1 *ptr;  // x0
    unsigned long long v2;  // x8
    unsigned long v3;  // x10
    struct_0 *addr;  // x8

    if (!(g_1fab2ae & 1))
    {
        sub_f7d92c(&g_1ef8ed0);
        sub_f7d92c(&g_1ef2c58);
        g_1fab2ae = 1;
    }
    v0 = sub_f7db70(g_1ef2c58);
    AxisBinding_TargetElem__ctor(v0);
    ptr = p->field_20;
    if (ptr)
    {
        v2 = ptr->field_10;
        ptr->field_1c = ptr->field_1c + 1;
        if (v2)
        {
            v3 = ptr->field_18;
            if (*((int *)(v2 + 24)) <= (unsigned int)v3)
            {
                sub_14a3390();
                return v0;
            }
            addr = v2 + v3 * 8;
            ptr->field_18 = (unsigned int)v3 + 1;
            addr->field_20 = v0;
            sub_f7d8d0((struct struct_0 *)&addr->field_20, v0);
            return v0;
        }
    }
    sub_f7db74(ptr);
}
```

## `AxisBinding.CopyFrom` — RVA `0xc5b53c`

- Decompiled symbol: `AxisBinding_CopyFrom`
- Metadata signature: `public void CopyFrom(AxisBinding b) { }`
- Native interval: `340` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    unsigned long long field_20;
} struct_0;

typedef struct struct_3 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_3;

typedef struct struct_1 {
    char padding_0[16];
    long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_1;

extern long long g_1ef8ed8;
extern long long g_1ef8ee8;
extern long long g_1ef8ef0;
extern char g_1fab2ac;

struct_2 * AxisBinding_CopyFrom(struct_2 *addr, struct_0 *ptr)
{
    struct_2 *v0;  // x0
    struct_2 *v1;  // x0
    int v8;  // w21
    unsigned long long v9;  // x8
    struct_2 *v10;  // x0
    unsigned long v11;  // x0
    struct_2 *v2;  // x0
    unsigned int v3;  // w8
    struct_3 *p;  // x9
    unsigned long v5;  // x2
    unsigned int v6;  // w10
    unsigned int v7;  // w21

    v0 = addr;
    if (!(g_1fab2ac & 1))
    {
        sub_f7d92c(&g_1ef8ed8);
        sub_f7d92c(&g_1ef8ee8);
        v1 = sub_f7d92c(&g_1ef8ef0);
        g_1fab2ac = 1;
        v0 = v1;
    }
    v2 = v0;
    if (ptr)
    {
        v3 = ptr->field_10;
        addr->field_10 = v3;
        if (!v3)
            return v2;
        v10 = InputBindingBase__Enable(addr, 0);
        p = addr->field_20;
        if (p)
        {
            v9 = ptr->field_20;
            if (v9)
            {
                v5 = p->field_18;
                if ((unsigned int)v5 == *((int *)(v9 + 24)))
                {
LABEL_105b5c4:
                    v8 = 0;
                    do
                    {
                        if (*((int *)(v9 + 24)) <= v8)
                            return v10;
                    } while (addr->field_20 && (v11 = (unsigned long)sub_14a30c0(addr->field_20, (unsigned long long)(unsigned int)v8, g_1ef8ef0), ptr->field_20 && (sub_14a30c0(ptr->field_20, (unsigned long long)(unsigned int)v8, g_1ef8ef0), v11 && (v10 = (struct_2 *)(unsigned long long)AxisBinding_TargetElem__CopyFrom(), v9 = ptr->field_20, v8 = (int)(v8 + 1), v9))));
                }
                else
                {
                    v6 = p->field_1c + 1;
                    p->field_18 = 0;
                    p->field_1c = v6;
                    if ((unsigned int)v5 < 1 || (v10 = (struct_2 *)(unsigned long long)Array__Clear(p->field_10, 0), v9 = ptr->field_20, v9))
                    {
                        v7 = 4294967295;
                        do
                        {
                            v7 += 1;
                            if (*((int *)(v9 + 24)) <= v7)
                                goto LABEL_105b5c4;
                        } while ((v10 = (struct_2 *)AxisBinding__AddTarget(addr, 0, v5), v9 = ptr->field_20, v9));
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `AxisBinding.Clear` — RVA `0xc5b700`

- Decompiled symbol: `AxisBinding_Clear`
- Metadata signature: `public void Clear() { }`
- Native interval: `112` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
    unsigned int field_1c;
} struct_0;

extern long long g_1ef8ed8;
extern char g_1fab2ad;

void AxisBinding_Clear(struct_1 *p)
{
    struct_0 *ptr;  // x8
    int v1;  // w2
    unsigned int v2;  // w9

    if (!(g_1fab2ad & 1))
    {
        sub_f7d92c(&g_1ef8ed8);
        g_1fab2ad = 1;
    }
    ptr = p->field_20;
    if (ptr)
    {
        v1 = ptr->field_18;
        v2 = ptr->field_1c;
        ptr->field_18 = 0;
        ptr->field_1c = v2 + 1;
        if (v1 < 1)
            return;
        Array__Clear();
        return;
    }
    sub_f7db74();
}
```

## `AxisBinding.RemoveLastTarget` — RVA `0xc5b804`

- Decompiled symbol: `AxisBinding_RemoveLastTarget`
- Metadata signature: `public void RemoveLastTarget() { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

typedef struct struct_1 {
    char padding_0[32];
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern long long g_1ef8ee0;
extern long long g_1ef8ee8;
extern char g_1fab2af;

struct_2 * AxisBinding_RemoveLastTarget(struct_1 *ptr, unsigned long a1)
{
    struct_0 *v0;  // x0
    long long v1;  // x0

    if (!(g_1fab2af & 1))
    {
        sub_f7d92c(&g_1ef8ee0);
        sub_f7d92c(&g_1ef8ee8);
        g_1fab2af = 1;
    }
    v0 = ptr->field_20;
    if (v0)
    {
        if (v0->field_18 >= 1)
        {
            v1 = sub_14a48fc();
            return sub_14a48fc();
        }
        return v0;
    }
    sub_f7db74(0);
}
```

## `AxisBinding.GetTarget` — RVA `0xc5b878`

- Decompiled symbol: `AxisBinding_GetTarget`
- Metadata signature: `public AxisBinding.TargetElem GetTarget(int axisElemId) { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

extern long long g_1ef8ee8;
extern long long g_1ef8ef0;
extern char g_1fab2b0;

unsigned int AxisBinding_GetTarget(struct_0 *a0, unsigned int a1)
{
    unsigned long v0;  // x19

    v0 = a1;
    if (!(g_1fab2b0 & 1))
    {
        sub_f7d92c(&g_1ef8ee8);
        sub_f7d92c(&g_1ef8ef0);
        g_1fab2b0 = 1;
    }
    if (((char)(v0 >> 31) & 1))
        return 0;
    if (a0->field_20)
    {
        if (*((int *)(a0->field_20 + 24)) > (unsigned int)v0)
            return sub_14a30c0();
        return 0;
    }
    sub_f7db74(0);
}
```

## `AxisBinding.SyncScroll` — RVA `0xc5b988`

- Decompiled symbol: `AxisBinding_SyncScroll`
- Metadata signature: `public void SyncScroll(int val, InputRig rig) { }`
- Native interval: `224` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_2 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef8ee8;
extern long long g_1ef8ef0;
extern char g_1fab2b2;

struct_3 * AxisBinding_SyncScroll(struct_2 *ptr, unsigned long a1, long long a2)
{
    struct_3 *v0;  // x0
    struct_1 *v1;  // x0
    int v2;  // w22
    unsigned long v3;  // x0

    if (!(g_1fab2b2 & 1))
    {
        sub_f7d92c(&g_1ef8ee8);
        sub_f7d92c(&g_1ef8ef0);
        sub_f7d92c(&g_1ef0c58);
        g_1fab2b2 = 1;
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
        v1 = ptr->field_20;
        if (v1)
        {
            v2 = 0;
            do
            {
                if (v1->field_18 <= v2)
                    return v1;
            } while ((v1 = (struct_1 *)sub_14a30c0(), v1 && (AxisBinding_TargetElem__SyncScroll(), v1 = (struct_1 *)ptr->field_20, v2 = (int)(v2 + 1), v1)));
        }
        v3 = sub_f7db74(v1);
        return sub_f7db74(v1);
    }
    else
    {
        return v0;
    }
}
```

## `AxisBinding.OnIsBoundToAxis` — RVA `0xc5bab0`

- Decompiled symbol: `AxisBinding_OnIsBoundToAxis`
- Metadata signature: `protected override bool OnIsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `176` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern long long g_1ef8ee8;
extern long long g_1ef8ef0;
extern char g_1fab2b3;

unsigned int AxisBinding_OnIsBoundToAxis(struct_1 *ptr, unsigned long a1)
{
    struct_0 *p;  // x0
    int v1;  // w21
    unsigned long v2;  // cc_dep1
    unsigned long v3;  // cc_dep2
    unsigned int v4;  // w22
    unsigned long v5;  // 4102
    unsigned long v6;  // 4102

    if (!(g_1fab2b3 & 1))
    {
        sub_f7d92c(&g_1ef8ee8);
        sub_f7d92c(&g_1ef8ef0);
        g_1fab2b3 = 1;
    }
    if (!ptr->field_10)
        return 0;
    p = ptr->field_20;
    if (p)
    {
        v1 = 0;
        do
        {
            v2 = v1;
            v3 = p->field_18;
            if (p->field_18 <= v1)
            {
                v4 = 0;
                v5 = arm64g_calculate_condition(163, v2, v3, 0);
                if ((char)v5)
                    return 0;
            }
            else
            {
                v4 = 1;
                v6 = arm64g_calculate_condition(163, v2, v3, 0);
                if ((char)v6)
                    return 1;
            }
            if (!sub_14a30c0())
                break;
            if (((char)AxisBinding_TargetElem__IsBoundToAxis() & 1))
                return v4;
            p = ptr->field_20;
            v1 += 1;
        } while (p);
    }
    sub_f7db74(p);
    return 0;
}
```

## `AxisBinding.OnIsBoundToKey` — RVA `0xc5bbc0`

- Decompiled symbol: `AxisBinding_OnIsBoundToKey`
- Metadata signature: `protected override bool OnIsBoundToKey(KeyCode keycode, InputRig rig) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int AxisBinding_OnIsBoundToKey(void)
{
    return 0;
}
```

## `AxisBinding.GetAxis` — RVA `0xc5bbc8`

- Decompiled symbol: `AxisBinding_GetAxis`
- Metadata signature: `public float GetAxis(InputRig rig) { }`
- Native interval: `344` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    unsigned int field_18;
    char padding_1c[4];
    struct struct_2 *field_20;
} struct_2;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    void* field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_3 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    long long field_18;
    char padding_20[8];
    long long field_28;
    long long field_30;
    char field_38;
    char field_39;
} struct_3;

extern char g_105bd20;
extern struct_0 *g_1eeed00;
extern struct_1 *g_1ef0c58;
extern long long g_1ef8ee8;
extern long long g_1ef8ef0;
extern unsigned long long g_1fab000;
extern char g_1fab1df;
extern char g_1fab2b4;
extern char g_1fab2b6;

struct_2 * AxisBinding_GetAxis(struct_2 *a0, unsigned long a1, unsigned long a2, unsigned long a3)
{
    unsigned long long v6;  // x30
    unsigned long v7;  // x20
    unsigned long long v16;  // d8
    unsigned long v17;  // x19
    struct_3 *v18;  // x20
    struct_2 *v19;  // x0
    unsigned long long v21;  // x0
    struct_2 *ptr;  // x19
    struct_1 **v9;  // x21
    unsigned long long v10;  // x22
    struct_0 *index;  // x0
    struct_2 *v12;  // x0
    struct_2 *v13;  // x0
    unsigned long v14;  // x1
    struct_3 *v15;  // x0
    unsigned long long v0;  // [bp-0x30]
    unsigned long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    struct_1 **v3;  // [bp-0x18]
    unsigned long v4;  // [bp-0x10]
    struct_2 *v5;  // [bp-0x8]

    v0 = v6;
    v7 = a1;
    ptr = a0;
    if (!(g_1fab2b4 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef8ee8);
        sub_f7d92c(&g_1ef8ef0);
        a0 = sub_f7d92c(&g_1ef0c58);
        g_1fab2b4 = 1;
    }
    if (!ptr->field_10)
        return a0;
    v9 = &g_1ef0c58;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(v7, 0, 0) & 1))
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        v10 = &g_1fab000;
        if (!g_1fab1df)
        {
            sub_f7d92c(&g_1eeed00);
            g_1fab1df = 1;
        }
        index = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            index = g_1eeed00;
        }
        v7 = (long long)index->field_b8[24];
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v12 = Object__op_Equality(v7, 0, 0);
    if (((char)v12 & 1))
        return v12;
    v13 = ptr->field_20;
    if (!v13)
    {
        return v13;
    }
    else if (v13->field_18)
    {
        v14 = 0;
        v15 = sub_14a30c0();
        if (v15)
        {
            v14 = v7;
            v7 = v4;
            ptr = v5;
            v10 = v2;
            v9 = v3;
            vvar_77{r256|8b} = v0;
        }
        else
        {
            vvar_205{r256|8b} = (int)&g_105bd20;
            v15 = sub_f7db74();
        }
        v0 = v16;
        v1 = vvar_77{r256|8b};
        v2 = v10;
        v3 = v9;
        v4 = v7;
        v5 = ptr;
        v17 = v14;
        v18 = v15;
        if (!(g_1fab2b6 & 1))
        {
            sub_f7d92c(&g_1ef0c58);
            g_1fab2b6 = 1;
        }
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v19 = Object__op_Equality(v17, 0, 0);
        if (((char)v19 & 1))
            return v19;
        if (v18->field_10)
        {
            if (v17)
            {
                InputRig__GetAxis(v17, v18->field_28, &v18[1].padding_0[6]);
                return InputRig__GetAxis(v17, v18->field_30, &v18[1].padding_0[10]);
            }
        }
        else
        {
            if (v17)
            {
                v21 = InputRig__GetAxis(v17, v18->field_18, &v18[1].padding_0[2]);
                return InputRig__GetAxis(v17, v18->field_18, &v18[1].padding_0[2]);
            }
        }
        sub_f7db74();
    }
    else
    {
        return v13;
    }
}
```
