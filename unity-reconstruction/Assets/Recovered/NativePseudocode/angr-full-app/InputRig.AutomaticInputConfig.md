# Native pseudocode: InputRig.AutomaticInputConfig

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InputRig.AutomaticInputConfig.ctor` — RVA `0xc42164`

- Decompiled symbol: `InputRig_AutomaticInputConfig_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `372` bytes
- Result: `pseudocode`

```c
extern long long g_1eedac8;
extern long long g_1eedad0;
extern long long g_1eef5c0;
extern long long g_1ef9548;
extern long long g_1ef9560;
extern char g_1fab203;

long long InputRig_AutomaticInputConfig_ctor(long long a0)
{
    unsigned long long v9;  // x30
    unsigned long long v10;  // x26
    unsigned long long v11;  // x25
    unsigned long long v12;  // x24
    unsigned long long v13;  // x23
    unsigned long long v14;  // x22
    unsigned long long v15;  // x21
    unsigned long long v16;  // x20
    unsigned long long v17;  // x19
    unsigned long long v0;  // [bp-0x50]
    unsigned long long v1;  // [bp-0x40]
    unsigned long long v2;  // [bp-0x38]
    unsigned long long v3;  // [bp-0x30]
    unsigned long long v4;  // [bp-0x28]
    unsigned long long v5;  // [bp-0x20]
    unsigned long long v6;  // [bp-0x18]
    unsigned long long v7;  // [bp-0x10]
    unsigned long long v8;  // [bp-0x8]

    v0 = v9;
    v1 = v10;
    v2 = v11;
    v3 = v12;
    v4 = v13;
    v5 = v14;
    v6 = v15;
    v7 = v16;
    v8 = v17;
    if (!(g_1fab203 & 1))
    {
        sub_f7d92c("y7");
        sub_f7d92c(&g_1eef5c0);
        sub_f7d92c(&g_1ef9548);
        sub_f7d92c(&g_1ef9560);
        sub_f7d92c(&g_1eedad0);
        sub_f7d92c(&g_1eedac8);
        g_1fab203 = 1;
    }
    Object__ctor(a0, 0);
    DigitalBinding__ctor(sub_f7db70(g_1eef590), 0, 0); /* do not return */
}
```

## `InputRig.AutomaticInputConfig.SetRig` — RVA `0xc422d8`

- Decompiled symbol: `InputRig_AutomaticInputConfig_SetRig`
- Metadata signature: `public void SetRig(InputRig rig) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

long long InputRig_AutomaticInputConfig_SetRig(struct_1 *ptr)
{
    struct_0 *p;  // x0
    unsigned long v1;  // x1
    unsigned long long v2;  // x0

    p = ptr->field_20;
    if (p)
    {
        p->field_20 = v1;
        sub_f7d8d0((struct struct_0 *)&p->field_20);
        v2 = InputRig_AutomaticInputConfig__OnDisablingConditionsChange(ptr);
        return InputRig_AutomaticInputConfig__OnDisablingConditionsChange(ptr);
    }
    sub_f7db74(0);
}
```

## `InputRig.AutomaticInputConfig.OnDisablingConditionsChange` — RVA `0xc42300`

- Decompiled symbol: `InputRig_AutomaticInputConfig_OnDisablingConditionsChange`
- Metadata signature: `public void OnDisablingConditionsChange() { }`
- Native interval: `44` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_AutomaticInputConfig_Recovered` matched 2 offsets against `InputRig.AutomaticInputConfig` metadata (confidence 1.00).

```c
typedef struct InputRig_AutomaticInputConfig_Recovered {
    char padding_0[32];
    long long disablingConditions;
    char disabledByConditions;
} InputRig_AutomaticInputConfig_Recovered;

unsigned long long InputRig_AutomaticInputConfig_OnDisablingConditionsChange(struct_0 *ptr, unsigned long a1)
{
    unsigned long long v0;  // x0

    if (ptr->field_20)
    {
        v0 = DisablingConditionSet__IsInEffect(ptr->field_20, 0);
        ptr->field_28 = (char)v0 & 1;
        return v0;
    }
    sub_f7db74(0);
}
```

## `InputRig.AutomaticInputConfig.Update` — RVA `0xc4232c`

- Decompiled symbol: `InputRig_AutomaticInputConfig_Update`
- Metadata signature: `public override void Update(InputRig rig) { }`
- Native interval: `308` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_AutomaticInputConfig_Recovered` matched 4 offsets against `InputRig.AutomaticInputConfig` metadata (confidence 1.00).

```c
typedef struct InputRig_AutomaticInputConfig_Recovered {
    char padding_0[24];
    struct struct_1 *targetBinding;
    char padding_20[8];
    char disabledByConditions;
    char padding_29[7];
    struct struct_2 *relatedAxisList;
    struct struct_3 *relatedKeyList;
} InputRig_AutomaticInputConfig_Recovered;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

typedef struct struct_3 {
    char padding_0[24];
    int field_18;
} struct_3;

extern long long g_1ef9550;
extern long long g_1ef9558;
extern long long g_1ef9568;
extern long long g_1ef9570;
extern char g_1fab204;

struct_4 * InputRig_AutomaticInputConfig_Update(struct_4 *ptr, long long a1)
{
    struct_4 *v0;  // x0
    struct_4 *v1;  // x0
    struct_4 *v2;  // x0
    struct_0 *i;  // x0
    unsigned int v4;  // w21
    struct_4 *v5;  // x0
    int v6;  // w21
    struct_4 *v7;  // x0
    unsigned long long v8;  // x0

    v0 = ptr;
    if (!(g_1fab204 & 1))
    {
        sub_f7d92c(&g_1ef9550);
        sub_f7d92c(&g_1ef9568);
        sub_f7d92c(&g_1ef9570);
        v1 = sub_f7d92c(&g_1ef9558);
        g_1fab204 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (ptr->field_28)
        return v2;
    i = ptr->field_38;
    if (i)
    {
        v4 = 0;
        do
        {
            if (i->field_18 <= v4)
            {
                i = ptr->field_30;
                if (i)
                {
                    v6 = 0;
                    do
                    {
                        if (i->field_18 > v6)
                        {
                            if (!sub_14a30c0())
                                break;
                        }
                        else
                        {
                            i = ptr->field_18;
                            if (i)
                            {
                                v8 = DigitalBinding__Sync(i, 1, a1, 1, 0);
                                return DigitalBinding__Sync(i, 1, a1, 1, 0);
                            }
                            break;
                        }
                        v7 = InputRig_AutomaticInputConfig_RelatedAxis__IsEnabling();
                        if (!((char)v7 & 1))
                            return v7;
                        i = ptr->field_30;
                        v6 += 1;
                    } while (i);
                }
            }
            else if (!sub_14a30c0())
            {
                break;
            }
            v5 = InputRig_AutomaticInputConfig_RelatedKey__IsEnabling();
            if (!((char)v5 & 1))
                return v5;
            i = ptr->field_38;
            v4 += 1;
        } while (i);
    }
    sub_f7db74(i);
}
```
