# Native pseudocode: JoystickStateBinding

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `JoystickStateBinding.ctor` — RVA `0xc5de7c`

- Decompiled symbol: `JoystickStateBinding_ctor`
- Metadata signature: `public void .ctor(InputBindingBase parent) { }`
- Native interval: `248` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    long long field_18;
} struct_0;

extern long long g_1eef5a0;
extern char g_1fab2d4;

void JoystickStateBinding_ctor(struct_0 *ptr, long long a1)
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
    if (!(g_1fab2d4 & 1))
    {
        sub_f7d92c("g.");
        sub_f7d92c(&g_1eef5a0);
        g_1fab2d4 = 1;
    }
    Object__ctor(ptr, 0);
    ptr->field_10 = 0;
    ptr->field_18 = a1;
    sub_f7d8d0((struct struct_0 *)&ptr->field_18, a1);
    ptr->field_10 = 0;
    AxisBinding__ctor(sub_f7db70(g_1eee9f8)); /* do not return */
}
```

## `JoystickStateBinding.CopyFrom` — RVA `0xc5df74`

- Decompiled symbol: `JoystickStateBinding_CopyFrom`
- Metadata signature: `public void CopyFrom(JoystickStateBinding b) { }`
- Native interval: `136` bytes
- Result: `pseudocode`
- Heuristic layout hint: `JoystickStateBinding_Recovered` matched 3 offsets against `JoystickStateBinding` metadata (confidence 0.75).

```c
typedef struct struct_2 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct struct_1 *field_20;
} struct_2;

typedef struct JoystickStateBinding_Recovered {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct JoystickStateBinding_Recovered *horzAxisBinding;
    struct JoystickStateBinding_Recovered *vertAxisBinding;
    struct JoystickStateBinding_Recovered *dirBinding;
} JoystickStateBinding_Recovered;

typedef struct struct_1 {
    char padding_0[16];
    long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_1;

typedef struct JoystickStateBinding_Recovered {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    unsigned long long field_20;
} struct_0;

typedef struct JoystickStateBinding_Recovered {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    char field_20;
    char padding_21[3];
    unsigned int field_24;
    struct struct_6 *field_28;
    struct struct_6 *field_30;
    struct struct_6 *field_38;
    struct struct_6 *field_40;
    struct struct_6 *field_48;
    struct struct_6 *field_50;
    struct struct_6 *field_58;
    struct struct_6 *field_60;
    struct struct_6 *field_68;
    struct struct_6 *field_70;
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

struct_2 * JoystickStateBinding_CopyFrom(struct_2 *p, struct_0 *addr, unsigned long a2, unsigned int a3)
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
        if (*((long long *)&v1[1].padding_0[8]))
        {
            DirectionBinding__CopyFrom(*((long long *)&v1[1].padding_0[8]), addr->field_30, 0, a3);
            if (v1->field_20)
            {
                AxisBinding__CopyFrom(v1->field_20, addr->field_20);
                if (*((long long *)&v1[1].padding_0[0]))
                {
                    v4 = AxisBinding__CopyFrom(*((long long *)&v1[1].padding_0[0]), addr->field_28);
                    return AxisBinding__CopyFrom(*((long long *)&v1[1].padding_0[0]), addr->field_28);
                }
            }
        }
    }
    sub_f7db74();
}
```

## `JoystickStateBinding.SyncJoyState` — RVA `0xc5dffc`

- Decompiled symbol: `JoystickStateBinding_SyncJoyState`
- Metadata signature: `public void SyncJoyState(JoystickState state, InputRig rig) { }`
- Native interval: `236` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2d5;

void* JoystickStateBinding_SyncJoyState(void* ptr, unsigned long long a1, long long a2)
{
    void* v0;  // x0
    void* v1;  // x0
    void* v2;  // x0
    void* v3;  // x0
    unsigned long v4;  // x0
    long long v5;  // x0

    v0 = ptr;
    if (!(g_1fab2d5 & 1))
    {
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab2d5 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (!a1)
    {
        return v2;
    }
    else if ((char)ptr[16])
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v3 = Object__op_Equality(a2, 0, 0);
        if (((char)v3 & 1))
            return v3;
        v4 = (long long)ptr[32];
        if (v4)
        {
            AxisBinding__SyncFloat(v4, 1, a2);
            v4 = (long long)ptr[40];
            if (v4)
            {
                AxisBinding__SyncFloat(v4, 1, a2);
                v4 = (long long)ptr[48];
                if (v4)
                {
                    v5 = DirectionBinding__SyncDirectionState(v4);
                    return DirectionBinding__SyncDirectionState(v4);
                }
            }
        }
        sub_f7db74(v4);
    }
    else
    {
        return v2;
    }
}
```

## `JoystickStateBinding.OnIsBoundToAxis` — RVA `0xc5e0e8`

- Decompiled symbol: `JoystickStateBinding_OnIsBoundToAxis`
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

unsigned int JoystickStateBinding_OnIsBoundToAxis(struct_2 *ptr, unsigned long a1, unsigned long a2)
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

## `JoystickStateBinding.OnIsBoundToKey` — RVA `0xc5e17c`

- Decompiled symbol: `JoystickStateBinding_OnIsBoundToKey`
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

unsigned int JoystickStateBinding_OnIsBoundToKey(struct_2 *ptr, unsigned long a1, unsigned long a2, unsigned long a3)
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

## `JoystickStateBinding.OnGetSubBindingDescriptions` — RVA `0xc5e210`

- Decompiled symbol: `JoystickStateBinding_OnGetSubBindingDescriptions`
- Metadata signature: `protected override void OnGetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Native interval: `216` bytes
- Result: `pseudocode`
- Heuristic layout hint: `JoystickStateBinding_Recovered` matched 3 offsets against `JoystickStateBinding` metadata (confidence 1.00).

```c
typedef struct JoystickStateBinding_Recovered {
    char padding_0[32];
    long long horzAxisBinding;
    long long vertAxisBinding;
    struct struct_7 **dirBinding;
} JoystickStateBinding_Recovered;

extern long long g_1f09ae0;
extern long long g_1f0ab18;
extern long long g_1f0f998;
extern char g_1fab2d6;

void JoystickStateBinding_OnGetSubBindingDescriptions(struct_0 *a0, void* a1, unsigned int a2, long long a3)
{
    if (!(g_1fab2d6 & 1))
    {
        sub_f7d92c(&g_1f0f998);
        sub_f7d92c(&g_1f0ab18);
        sub_f7d92c(&g_1f09ae0);
        g_1fab2d6 = 1;
    }
    if (a1)
    {
        BindingDescriptionList__Add(a1, a0->field_20, 1, g_1f0ab18, a3, a2);
        BindingDescriptionList__Add(a1, a0->field_28, 1, g_1f0f998, a3, a2);
        BindingDescriptionList__Add(a1, a0->field_30, g_1f09ae0, a3, a2); /* do not return */
    }
    sub_f7db74();
}
```
