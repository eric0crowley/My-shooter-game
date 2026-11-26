# Native pseudocode: PressureLevelBinding

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `PressureLevelBinding.ctor` — RVA `0xc686e4`

- Decompiled symbol: `PressureLevelBinding_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `288` bytes
- Result: `pseudocode`

```c
extern long long g_1eeda30;
extern long long g_1eee550;
extern long long g_1ef3790;
extern long long g_1ef91c0;
extern char g_1fab31c;

long long PressureLevelBinding_ctor(long long a0)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]
    unsigned long long v5;  // [bp-0x8]

    v0 = v6;
    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    if (!(g_1fab31c & 1))
    {
        sub_f7d92c(&g_1ef91c0);
        sub_f7d92c(&g_1eeda30);
        sub_f7d92c(&g_1eee550);
        sub_f7d92c(&g_1ef3790);
        g_1fab31c = 1;
    }
    MonoBehaviour__ctor(a0, 0);
    sub_f7d9d4(g_1eee550, 1);
    PressureLevelBinding_RangeConfig__ctor(sub_f7db70(g_1ef3790)); /* do not return */
}
```

## `PressureLevelBinding.OnEnable` — RVA `0xc68870`

- Decompiled symbol: `PressureLevelBinding_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `312` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    long long field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efd170;
extern long long g_1f006a8;
extern char g_1fab31d;

long long PressureLevelBinding_OnEnable(struct_1 *ptr)
{
    struct_1 *v0;  // x20
    long long v1;  // x0
    long long v2;  // x0
    long long v3;  // x0

    if (!(g_1fab31d & 1))
    {
        sub_f7d92c("++");
        sub_f7d92c(&g_1efd170);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f006a8);
        g_1fab31d = 1;
    }
    v0 = &ptr->field_20;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(ptr->field_20, 0, 0) & 1))
    {
        v1 = sub_123204c(ptr, g_1efd170);
        ptr->field_20 = v1;
        sub_f7d8d0(v0, v1);
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v2 = Object__op_Inequality(*((long long *)&v0->padding_0[0]), 0, 0);
    if (!((char)v2 & 1))
        return v2;
    v3 = sub_f7db70(g_1eee648);
    Action__ctor(v3, ptr, g_1f006a8, 0);
    if (!ptr->field_20)
        sub_f7db74();
}
```

## `PressureLevelBinding.OnDisable` — RVA `0xc689a8`

- Decompiled symbol: `PressureLevelBinding_OnDisable`
- Metadata signature: `private void OnDisable() { }`
- Native interval: `208` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    long long field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1f006a8;
extern char g_1fab31e;

long long PressureLevelBinding_OnDisable(struct_1 *a0)
{
    long long v0;  // x0
    long long v1;  // x0

    if (!(g_1fab31e & 1))
    {
        sub_f7d92c("++");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f006a8);
        g_1fab31e = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Inequality(a0->field_20, 0, 0);
    if (!((char)v0 & 1))
        return v0;
    v1 = sub_f7db70(g_1eee648);
    Action__ctor(v1, a0, g_1f006a8, 0);
    if (!a0->field_20)
        sub_f7db74();
}
```

## `PressureLevelBinding.UpdateRanges` — RVA `0xc68a78`

- Decompiled symbol: `PressureLevelBinding_UpdateRanges`
- Metadata signature: `protected void UpdateRanges() { }`
- Native interval: `256` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PressureLevelBinding_Recovered` matched 3 offsets against `PressureLevelBinding` metadata (confidence 1.00).

```c
typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct PressureLevelBinding_Recovered {
    char padding_0[32];
    struct struct_1 *rig;
    long long sourceAxis;
    char padding_30[8];
    struct struct_1 *rangeConfigList;
} PressureLevelBinding_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef91c8;
extern long long g_1ef91d0;
extern char g_1fab31f;

struct_3 * PressureLevelBinding_UpdateRanges(struct_2 *ptr)
{
    struct_3 *v0;  // x0
    struct_3 *v1;  // x0
    struct_1 *v2;  // x0
    int v3;  // w20

    if (!(g_1fab31f & 1))
    {
        sub_f7d92c(&g_1ef91c8);
        sub_f7d92c(&g_1ef91d0);
        sub_f7d92c(&g_1ef0c58);
        g_1fab31f = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(ptr->field_20, 0, 0);
    if (((char)v0 & 1))
        return v0;
    v1 = String__IsNullOrEmpty(ptr->field_28, 0);
    if (((char)v1 & 1))
        return v1;
    v2 = ptr->field_20;
    if (v2)
    {
        InputRig__GetAxisRaw(v2, ptr->field_28, (struct PressureLevelBinding_Recovered *)&ptr->padding_30, 0);
        v2 = ptr->field_38;
        if (v2)
        {
            v3 = 0;
            do
            {
                if (v2->field_18 <= v3)
                    return v2;
            } while ((v2 = (struct_1 *)(unsigned long long)sub_14a30c0(), v2 && (PressureLevelBinding_RangeConfig__Update(), v2 = (struct_1 *)ptr->field_38, v3 = (int)(v3 + 1), v2)));
        }
    }
    sub_f7db74(v2);
}
```
