# Native pseudocode: bl_LerpControlledBob

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_LerpControlledBob.Offset` — RVA `0xce04ac`

- Decompiled symbol: `bl_LerpControlledBob_Offset`
- Metadata signature: `public float Offset() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long bl_LerpControlledBob_Offset(unsigned long a0)
{
    return a0;
}
```

## `bl_LerpControlledBob.DoBobCycle` — RVA `0xce04b4`

- Decompiled symbol: `bl_LerpControlledBob_DoBobCycle`
- Metadata signature: `public IEnumerator DoBobCycle() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef4150;
extern char g_1fab637;

struct_0 * bl_LerpControlledBob_DoBobCycle(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab637 & 1))
    {
        sub_f7d92c(&g_1ef4150);
        g_1fab637 = 1;
    }
    v0 = sub_f7db70(g_1ef4150);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `bl_LerpControlledBob.<DoBobCycle>d__4.ctor` — RVA `0xce0520`

- Decompiled symbol: `bl_LerpControlledBob_DoBobCycle_d__4_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void bl_LerpControlledBob_DoBobCycle_d__4_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `bl_LerpControlledBob.ctor` — RVA `0xce0548`

- Decompiled symbol: `bl_LerpControlledBob_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long bl_LerpControlledBob_ctor(void)
{
    long long v0;  // x0

    v0 = Object__ctor();
    return Object__ctor();
}
```

## `bl_LerpControlledBob.<DoBobCycle>d__4.Dispose` — RVA `0xce0550`

- Decompiled symbol: `bl_LerpControlledBob_DoBobCycle_d__4_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long bl_LerpControlledBob_DoBobCycle_d__4_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `bl_LerpControlledBob.<DoBobCycle>d__4.MoveNext` — RVA `0xce0554`

- Decompiled symbol: `bl_LerpControlledBob_DoBobCycle_d__4_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `432` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_1 *field_20;
    unsigned int field_28;
} struct_0;

typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    unsigned int field_14;
    unsigned int field_18;
} struct_1;

extern long long g_1ef2438;
extern char g_1fab638;

unsigned int bl_LerpControlledBob_DoBobCycle_d__4_MoveNext(struct_0 *ptr)
{
    unsigned int flag;  // w9
    unsigned int p[7];  // x8
    unsigned int v10;  // s8
    unsigned int v11;  // s0
    unsigned long v12;  // 4129
    unsigned int v13;  // s2
    unsigned long v14;  // 4150
    unsigned int v15;  // s0
    long long v16;  // x20
    struct_0 *addr;  // x19
    unsigned int v2;  // s8
    unsigned int v3;  // s0
    unsigned long v4;  // 4129
    unsigned int v5;  // s2
    unsigned long v6;  // 4150
    unsigned int v7;  // s0
    long long v8;  // x20
    struct_0 *ptr3;  // x19

    if (!(g_1fab638 & 1))
    {
        sub_f7d92c(&g_1ef2438);
        g_1fab638 = 1;
    }
    flag = ptr->field_10;
    p = ptr->field_20;
    if (flag != 2)
    {
        if (flag == 1)
        {
            v2 = ptr->field_28;
            ptr->field_10 = 4294967295;
        }
        else if (!flag)
        {
            ptr->field_28 = 0;
            ptr->field_10 = 4294967295;
            v2 = 0;
        }
        else
        {
            return 0;
        }
        if (!p)
            sub_f7db74();
        v3 = p[4];
        v4 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v2, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v3) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v3) & 1)) & ((unsigned long long)(char)(CmpF(v2, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v3) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v4))
        {
            v5 = [D] unsupported_Iop_ZeroHI96ofV128();
            v6 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v2 / v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2 / v3, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2 / v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2 / v3, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v2 / v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2 / v3, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v6))
                v5 = 0;
            v7 = v5 * p[5];
            p[6] = v7;
            Time__get_deltaTime();
            ptr->field_28 = v2 + v7;
            v8 = sub_f7db70(g_1ef2438);
            WaitForFixedUpdate__ctor(v8, 0);
            ptr->field_18 = v8;
            ptr3 = &ptr->field_18;
            sub_f7d8d0(ptr3, v8);
            *((unsigned int *)&ptr3->padding_0[8]) = 1;
            return 1;
        }
        ptr->field_28 = 0;
        v10 = 0;
    }
    else
    {
        ptr->field_10 = 4294967295;
        if (!p)
            sub_f7db74();
        v10 = ptr->field_28;
    }
    v11 = p[4];
    v12 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v10, v11)) >> 5 & 3 | (unsigned long long)(CmpF(v10, v11) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v10, v11)) >> 5 & 3 | (unsigned long long)(CmpF(v10, v11) & 1)) & ((unsigned long long)(char)(CmpF(v10, v11)) >> 5 & 3 | (unsigned long long)(CmpF(v10, v11) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v12)
    {
        p[6] = 0;
        return 0;
    }
    v13 = [D] unsupported_Iop_ZeroHI96ofV128();
    v14 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v10 / v11, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10 / v11, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v10 / v11, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10 / v11, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v10 / v11, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10 / v11, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v14))
        v13 = 0;
    v15 = p[5] + v13 * -(p[5]);
    p[6] = v15;
    Time__get_deltaTime();
    ptr->field_28 = v10 + v15;
    v16 = sub_f7db70(g_1ef2438);
    WaitForFixedUpdate__ctor(v16, 0);
    ptr->field_18 = v16;
    addr = &ptr->field_18;
    sub_f7d8d0(addr, v16);
    *((unsigned int *)&addr->padding_0[8]) = 2;
    return 1;
}
```

## `bl_LerpControlledBob.<DoBobCycle>d__4.get_Current` — RVA `0xce0704`

- Decompiled symbol: `bl_LerpControlledBob_DoBobCycle_d__4_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_LerpControlledBob_DoBobCycle_d__4_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_LerpControlledBob.<DoBobCycle>d__4.Reset` — RVA `0xce070c`

- Decompiled symbol: `bl_LerpControlledBob_DoBobCycle_d__4_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f054d0;

void bl_LerpControlledBob_DoBobCycle_d__4_Reset(void)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = sub_f7db70(sub_f7d940(&g_1ef0bd8));
    NotSupportedException__ctor(v4, 0);
    sub_f7da4c(v4, sub_f7d940(&g_1f054d0));
}
```

## `bl_LerpControlledBob.<DoBobCycle>d__4.get_Current` — RVA `0xce0744`

- Decompiled symbol: `bl_LerpControlledBob_DoBobCycle_d__4_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_LerpControlledBob_DoBobCycle_d__4_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
