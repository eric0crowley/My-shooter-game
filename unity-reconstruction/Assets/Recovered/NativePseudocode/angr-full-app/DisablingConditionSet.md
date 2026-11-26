# Native pseudocode: DisablingConditionSet

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DisablingConditionSet.ctor` — RVA `0xc4f5b4`

- Decompiled symbol: `DisablingConditionSet_ctor`
- Metadata signature: `public void .ctor(InputRig rig) { }`
- Native interval: `176` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DisablingConditionSet_Recovered` matched 4 offsets against `DisablingConditionSet` metadata (confidence 1.00).

```c
typedef struct DisablingConditionSet_Recovered {
    char padding_0[16];
    unsigned int mobileModeRelation;
    unsigned short disableWhenTouchScreenInactive;
    char padding_16[2];
    long long switchList;
    long long rig;
} DisablingConditionSet_Recovered;

extern long long g_1eed9c8;
extern long long g_1ef8f98;
extern char g_1fab2a6;

long long DisablingConditionSet_ctor(struct_0 *ptr, long long a1)
{
    long long v0;  // x20
    struct_0 *p;  // x19
    unsigned long v2;  // x0

    if (!(g_1fab2a6 & 1))
    {
        sub_f7d92c(&g_1ef8f98);
        sub_f7d92c(&g_1eed9c8);
        g_1fab2a6 = 1;
    }
    Object__ctor(ptr, 0);
    ptr->field_20 = a1;
    sub_f7d8d0((struct DisablingConditionSet_Recovered *)&ptr->field_20, a1);
    v0 = sub_f7db70(g_1eed9c8);
    sub_14a2bd4(v0, 32, g_1ef8f98);
    ptr->field_18 = v0;
    p = &ptr->field_18;
    v2 = sub_f7d8d0(p, v0);
    *((unsigned int *)&p->padding_0[8]) = 0;
    *((unsigned short *)&p->padding_0[4]) = 1;
    return v2;
}
```

## `DisablingConditionSet.IsInEffect` — RVA `0xc4fd60`

- Decompiled symbol: `DisablingConditionSet_IsInEffect`
- Metadata signature: `public bool IsInEffect() { }`
- Native interval: `304` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DisablingConditionSet_Recovered` matched 4 offsets against `DisablingConditionSet` metadata (confidence 1.00).

```c
typedef struct DisablingConditionSet_Recovered {
    char padding_0[16];
    unsigned int mobileModeRelation;
    char disableWhenTouchScreenInactive;
    char disableWhenCursorIsUnlocked;
    char padding_16[10];
    struct struct_3 *rig;
} DisablingConditionSet_Recovered;

typedef struct struct_3 {
    char padding_0[116];
    char field_74;
} struct_3;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_0 *g_1eeed00;
extern struct_1 *g_1eeed10;
extern struct_2 *g_1ef0c58;
extern char g_1fab2a7;

unsigned long long DisablingConditionSet_IsInEffect(struct_4 *a0)
{
    unsigned int v0;  // w0
    unsigned int v1;  // w9
    unsigned int v2;  // w8
    unsigned long v3;  // 4115
    unsigned long v4;  // x8
    unsigned long long v5;  // x0

    if (!(g_1fab2a7 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1eeed10);
        sub_f7d92c(&g_1ef0c58);
        g_1fab2a7 = 1;
    }
    if (a0->field_10 != 2)
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        v0 = CF2Input__IsInMobileMode();
        if (a0->field_10 != 1)
            v1 = 0;
        else
            v1 = 1;
        if (a0->field_10)
            v2 = 0;
        else
            v2 = 1;
        v3 = arm64g_calculate_condition(25, (unsigned long long)(v0 & 1), 0, 0);
        if ((char)v3)
            v4 = v1;
        else
            v4 = v2;
        if (((char)v4 & 1))
            return 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(a0->field_20, 0, 0) & 1))
        return 0;
    if (a0->field_14)
    {
        if (!a0->field_20)
        {
            sub_f7db74();
        }
        else if (a0->field_20->field_74)
        {
            return 1;
        }
    }
    if (!a0->field_15)
    {
        v5 = DisablingConditionSet__IsDisabledByRigSwitches(a0);
        return DisablingConditionSet__IsDisabledByRigSwitches(a0);
    }
    if (!g_1eeed10->field_e0)
        sub_f7da5c(g_1eeed10);
    if (!((char)CFScreen__get_lockCursor() & 1))
        return 1;
    v5 = DisablingConditionSet__IsDisabledByRigSwitches(a0);
    return DisablingConditionSet__IsDisabledByRigSwitches(a0);
}
```

## `DisablingConditionSet.SetRig` — RVA `0xc5afd4`

- Decompiled symbol: `DisablingConditionSet_SetRig`
- Metadata signature: `public void SetRig(InputRig rig) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

long long DisablingConditionSet_SetRig(struct_0 *ptr, unsigned long a1)
{
    long long v0;  // x0

    ptr->field_20 = a1;
    v0 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `DisablingConditionSet.IsDisabledByRigSwitches` — RVA `0xc5afdc`

- Decompiled symbol: `DisablingConditionSet_IsDisabledByRigSwitches`
- Metadata signature: `public bool IsDisabledByRigSwitches() { }`
- Native interval: `224` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DisablingConditionSet_Recovered` matched 2 offsets against `DisablingConditionSet` metadata (confidence 1.00).

```c
typedef struct DisablingConditionSet_Recovered {
    char padding_0[24];
    struct struct_1 *switchList;
    long long rig;
} DisablingConditionSet_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef8fa0;
extern long long g_1ef8fa8;
extern char g_1fab2a8;

unsigned int DisablingConditionSet_IsDisabledByRigSwitches(struct_2 *ptr)
{
    struct_1 *p;  // x0
    int v1;  // w20
    unsigned long v2;  // cc_dep1
    unsigned long v3;  // cc_dep2
    unsigned int v4;  // w21
    unsigned long v5;  // 4102
    unsigned long v6;  // 4102

    if (!(g_1fab2a8 & 1))
    {
        sub_f7d92c(&g_1ef8fa0);
        sub_f7d92c(&g_1ef8fa8);
        sub_f7d92c(&g_1ef0c58);
        g_1fab2a8 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(ptr->field_20, 0, 0) & 1))
        return 0;
    p = ptr->field_18;
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
            if (((char)DisablingConditionSet_DisablingRigSwitch__IsInEffect() & 1))
                return v4;
            p = ptr->field_18;
            v1 += 1;
        } while (p);
    }
    sub_f7db74(p);
}
```
