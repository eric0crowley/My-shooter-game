# Native pseudocode: InputRig.AutomaticInputConfigCollection

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InputRig.AutomaticInputConfigCollection.ctor` — RVA `0xc42560`

- Decompiled symbol: `InputRig_AutomaticInputConfigCollection_ctor`
- Metadata signature: `public void .ctor(InputRig rig) { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
extern long long g_1ef9838;
extern char g_1fab206;

void InputRig_AutomaticInputConfigCollection_ctor(unsigned long a0, unsigned long a1)
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
    if (!(g_1fab206 & 1))
    {
        sub_f7d92c(&g_1ef9838);
        g_1fab206 = 1;
    }
}
```

## `InputRig.AutomaticInputConfigCollection.SetRig` — RVA `0xc425bc`

- Decompiled symbol: `InputRig_AutomaticInputConfigCollection_SetRig`
- Metadata signature: `public void SetRig(InputRig rig) { }`
- Native interval: `152` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

extern long long g_1ef90b0;
extern long long g_1ef90b8;
extern char g_1fab207;

long long InputRig_AutomaticInputConfigCollection_SetRig(struct_0 *ptr, unsigned long a1)
{
    unsigned long v0;  // x0, Other Possible Types: unsigned long long
    int v1;  // w21
    unsigned long v2;  // x0

    if (!(g_1fab207 & 1))
    {
        sub_f7d92c(&g_1ef90b0);
        sub_f7d92c(&g_1ef90b8);
        g_1fab207 = 1;
    }
    v0 = ptr->field_10;
    if (v0)
    {
        v1 = 0;
        do
        {
            if (*((int *)(v0 + 24)) <= v1)
                return v0;
        } while ((v0 = (unsigned long long)sub_14a30c0(), v0 && (InputRig_AutomaticInputConfig__SetRig(v0), v0 = ptr->field_10, v1 = (int)(v1 + 1), v0)));
    }
    v2 = sub_f7db74(v0);
    return sub_f7db74(v0);
}
```

## `InputRig.AutomaticInputConfigCollection.Add` — RVA `0xc42654`

- Decompiled symbol: `InputRig_AutomaticInputConfigCollection_Add`
- Metadata signature: `public InputRig.AutomaticInputConfig Add(string name, bool createUndo) { }`
- Native interval: `252` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

typedef struct struct_4 {
    char padding_0[16];
    struct struct_3 *field_10;
} struct_4;

typedef struct struct_3 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_3;

typedef struct struct_2 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    unsigned long long field_10;
} struct_1;

extern long long g_1ef3310;
extern long long g_1ef90a8;
extern char g_1fab208;

struct_0 * InputRig_AutomaticInputConfigCollection_Add(struct_4 *p, long long a1)
{
    struct_0 *v0;  // x19
    struct_0 *addr;  // x0
    struct_3 *ptr;  // x0
    unsigned long long v3;  // x8
    unsigned long v4;  // x10
    struct_2 *ptr3;  // x8

    if (!(g_1fab208 & 1))
    {
        sub_f7d92c(&g_1ef3310);
        sub_f7d92c(&g_1ef90a8);
        g_1fab208 = 1;
    }
    v0 = sub_f7db70(g_1ef3310);
    InputRig_AutomaticInputConfig__ctor(v0);
    if (v0)
    {
        addr = v0;
        addr->field_10 = a1;
        sub_f7d8d0((struct struct_0 *)&addr->field_10, a1);
        InputRig_AutomaticInputConfig__SetRig(v0);
        ptr = p->field_10;
        if (ptr)
        {
            v3 = ptr->field_10;
            ptr->field_1c = ptr->field_1c + 1;
            if (v3)
            {
                v4 = ptr->field_18;
                if (*((int *)(v3 + 24)) <= (unsigned int)v4)
                {
                    sub_14a3390();
                    return v0;
                }
                ptr3 = v3 + v4 * 8;
                ptr->field_18 = (unsigned int)v4 + 1;
                ptr3->field_20 = v0;
                sub_f7d8d0((struct struct_2 *)&ptr3->field_20, v0);
                return v0;
            }
        }
    }
    sub_f7db74();
}
```

## `InputRig.AutomaticInputConfigCollection.OnDisablingConditionsChange` — RVA `0xc42750`

- Decompiled symbol: `InputRig_AutomaticInputConfigCollection_OnDisablingConditionsChange`
- Metadata signature: `public void OnDisablingConditionsChange() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

extern long long g_1ef90b0;
extern long long g_1ef90b8;
extern char g_1fab209;

long long InputRig_AutomaticInputConfigCollection_OnDisablingConditionsChange(struct_0 *ptr)
{
    unsigned long v0;  // x0, Other Possible Types: unsigned long long
    int v1;  // w20
    unsigned long v2;  // x0

    if (!(g_1fab209 & 1))
    {
        sub_f7d92c(&g_1ef90b0);
        sub_f7d92c(&g_1ef90b8);
        g_1fab209 = 1;
    }
    v0 = ptr->field_10;
    if (v0)
    {
        v1 = 0;
        do
        {
            if (*((int *)(v0 + 24)) <= v1)
                return v0;
        } while ((v0 = (unsigned long long)sub_14a30c0(), v0 && (InputRig_AutomaticInputConfig__OnDisablingConditionsChange(v0, (unsigned long long)(unsigned int)v1), v0 = ptr->field_10, v1 = (int)(v1 + 1), v0)));
    }
    v2 = sub_f7db74(v0);
    return sub_f7db74(v0);
}
```
