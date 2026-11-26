# Native pseudocode: SwipeSlasherChara

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SwipeSlasherChara.OnEnable` — RVA `0xc651ac`

- Decompiled symbol: `SwipeSlasherChara_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[160];
    long long field_a0;
} struct_0;

extern long long g_1efcf08;
extern char g_1fab2f4;

void SwipeSlasherChara_OnEnable(struct_0 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab2f4 & 1))
    {
        sub_f7d92c(&g_1efcf08);
        g_1fab2f4 = 1;
    }
    ptr->field_a0 = sub_1231bc8(ptr, g_1efcf08);
    sub_f7d8d0();
    return;
}
```

## `SwipeSlasherChara.Start` — RVA `0xc65204`

- Decompiled symbol: `SwipeSlasherChara_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `196` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[664];
    struct struct_2 *field_298;
    unsigned long long field_2a0;
} struct_1;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2f5;

unsigned long long SwipeSlasherChara_Start(long long a0)
{
    unsigned int v0;  // w20
    struct_1 **v1;  // x21
    unsigned long long flag;  // x2
    unsigned long long v3;  // x0
    struct_1 **v4;  // x0
    unsigned long v5;  // x1

    if (!(g_1fab2f5 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab2f5 = 1;
    }
    v0 = 0;
    while (true)
    {
        v1 = SwipeSlasherChara__GetActionGraphic(a0, v0);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        flag = 0;
        v3 = Object__op_Inequality(v1, 0, 0);
        if (((char)v3 & 1))
            break;
        v0 += 1;
        if (v0 == 12)
            return v3;
    }
    if (!v1)
        sub_f7db74();
    v4 = v1;
    v5 = *(v1)->field_2a0;
    *(v1)->field_298();
}
```

## `SwipeSlasherChara.GetActionGraphic` — RVA `0xc652c8`

- Decompiled symbol: `SwipeSlasherChara_GetActionGraphic`
- Metadata signature: `private Graphic GetActionGraphic(SwipeSlasherChara.ActionType a) { }`
- Native interval: `144` bytes
- Result: `pseudocode`

```c
extern char g_8322dc;

unsigned int SwipeSlasherChara_GetActionGraphic(unsigned long a0, unsigned int a1)
{
    if (11 < a1)
        return 0;
    goto sub_10652ec + (&g_8322dc)[a1] * 4;
}
```

## `SwipeSlasherChara.SetActionTriggerState` — RVA `0xc65358`

- Decompiled symbol: `SwipeSlasherChara_SetActionTriggerState`
- Metadata signature: `private void SetActionTriggerState(SwipeSlasherChara.ActionType action) { }`
- Native interval: `308` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[160];
    long long field_a0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2f6;
extern char g_852240;

unsigned long long SwipeSlasherChara_SetActionTriggerState(struct_1 *a0, unsigned int a1)
{
    unsigned long long v0;  // x0
    unsigned long long v1;  // x0
    unsigned long long v2;  // x0

    if (!(g_1fab2f6 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab2f6 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(a0->field_a0, 0, 0);
    if (((char)v0 & 1))
    {
        return v0;
    }
    else if (11 >= a1)
    {
        goto sub_10653e0 + (&g_852240)[a1] * 4;
    }
    else
    {
        v1 = String__IsNullOrEmpty(0, 0);
        if (((char)v1 & 1))
            return v1;
        if (a0->field_a0)
        {
            v2 = Animator__SetTrigger();
            return Animator__SetTrigger();
        }
        sub_f7db74(0);
    }
}
```

## `SwipeSlasherChara.ExecuteAction` — RVA `0xc6548c`

- Decompiled symbol: `SwipeSlasherChara_ExecuteAction`
- Metadata signature: `public void ExecuteAction(SwipeSlasherChara.ActionType action) { }`
- Native interval: `360` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[160];
    long long field_a0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2f7;

long long SwipeSlasherChara_ExecuteAction(struct_1 *a0, unsigned int a1)
{
    struct_1 **v0;  // x20
    unsigned long long flag;  // x2
    long long v2;  // x0
    struct_1 **v3;  // x0
    unsigned long v4;  // x1

    if (!(g_1fab2f7 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab2f7 = 1;
    }
    v0 = SwipeSlasherChara__GetActionGraphic(a0, a1);
    SwipeSlasherChara__PlaySound();
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(a0->field_a0, 0, 0) & 1))
        SwipeSlasherChara__SetActionTriggerState(a0, a1);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    flag = 0;
    v2 = Object__op_Inequality(v0, 0, 0);
    if (!((char)v2 & 1))
    {
        return v2;
    }
    else if (v0)
    {
        v3 = v0;
        v4 = *((long long *)&(*(v0))[4].padding_0[0]);
        (*(v0))[3].field_a0();
    }
    else
    {
        sub_f7db74();
    }
}
```

## `SwipeSlasherChara.PlaySound` — RVA `0xc655f4`

- Decompiled symbol: `SwipeSlasherChara_PlaySound`
- Metadata signature: `private void PlaySound(AudioClip clip) { }`
- Native interval: `176` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef22e8;
extern char g_1fab2c9;
extern char g_1fab2f8;

long long SwipeSlasherChara_PlaySound(unsigned long a0, long long a1)
{
    long long v0;  // x0

    if (!(g_1fab2f8 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab2f8 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Inequality(a1, 0, 0);
    if (!((char)v0 & 1))
    {
        return v0;
    }
    else if (!g_1fab2c9)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab2c9 = 1;
    }
}
```

## `SwipeSlasherChara.ctor` — RVA `0xc656a4`

- Decompiled symbol: `SwipeSlasherChara_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `524` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SwipeSlasherChara_Recovered` matched 13 offsets against `SwipeSlasherChara` metadata (confidence 1.00).

```c
typedef struct SwipeSlasherChara_Recovered {
    char padding_0[152];
    unsigned int fadeDur;
    char padding_9c[12];
    long long animLeftStab;
    long long animLeftSlashU;
    long long animLeftSlashR;
    long long animLeftSlashD;
    long long animLeftSlashL;
    long long animRightStab;
    long long animRightSlashU;
    long long animRightSlashR;
    long long animRightSlashD;
    long long animRightSlashL;
    long long animDodgeLeft;
    long long animDodgeRight;
} SwipeSlasherChara_Recovered;

extern long long g_1f09b50;
extern long long g_1f09b58;
extern long long g_1f0bc98;
extern long long g_1f0bca0;
extern long long g_1f0bca8;
extern long long g_1f0bcb0;
extern long long g_1f0bcb8;
extern long long g_1f0d660;
extern long long g_1f0d668;
extern long long g_1f0d670;
extern long long g_1f0d678;
extern long long g_1f0d680;
extern char g_1fab2f9;

void SwipeSlasherChara_ctor(struct_0 *ptr)
{
    unsigned long long v13;  // x30
    unsigned long long v14;  // x28
    unsigned long long v23;  // x19
    struct_0 *p;  // x0
    struct_0 *addr;  // x0
    struct_0 *ptr3;  // x0
    struct_0 *ptr4;  // x0
    struct_0 *ptr5;  // x0
    struct_0 *ptr6;  // x0
    struct_0 *ptr7;  // x0
    struct_0 *ptr8;  // x0
    struct_0 *ptr9;  // x0
    unsigned long long v15;  // x27
    struct_0 *ptr10;  // x0
    struct_0 *ptr11;  // x0
    unsigned long long v16;  // x26
    unsigned long long v17;  // x25
    unsigned long long v18;  // x24
    unsigned long long v19;  // x23
    unsigned long long v20;  // x22
    unsigned long long v21;  // x21
    unsigned long long v22;  // x20
    char *v0;  // [bp-0x60]
    unsigned long long v1;  // [bp-0x58]
    unsigned long long v2;  // [bp-0x50]
    unsigned long long v3;  // [bp-0x48]
    unsigned long long v4;  // [bp-0x40]
    unsigned long long v5;  // [bp-0x38]
    unsigned long long v6;  // [bp-0x30]
    unsigned long long v7;  // [bp-0x28]
    unsigned long long v8;  // [bp-0x20]
    unsigned long long v9;  // [bp-0x18]
    unsigned long long v10;  // [bp-0x10]
    unsigned long long v11;  // [bp-0x8]
    char v12;  // [bp+0x0]

    v0 = &v12;
    v1 = v13;
    v2 = v14;
    v3 = v15;
    v4 = v16;
    v5 = v17;
    v6 = v18;
    v7 = v19;
    v8 = v20;
    v9 = v21;
    v10 = v22;
    v11 = v23;
    if (!(g_1fab2f9 & 1))
    {
        sub_f7d92c(&g_1f0bca8);
        sub_f7d92c(&g_1f0d680);
        sub_f7d92c(&g_1f0d660);
        sub_f7d92c(&g_1f09b58);
        sub_f7d92c(&g_1f0bca0);
        sub_f7d92c(&g_1f0d678);
        sub_f7d92c(&g_1f0bc98);
        sub_f7d92c(&g_1f0bcb0);
        sub_f7d92c(&g_1f0d668);
        sub_f7d92c(&g_1f09b50);
        sub_f7d92c(&g_1f0d670);
        sub_f7d92c(&g_1f0bcb8);
        g_1fab2f9 = 1;
    }
    ptr->field_98 = 0x3f000000;
    p = ptr;
    p->field_a8 = g_1f0bcb8;
    sub_f7d8d0((struct SwipeSlasherChara_Recovered *)&p->field_a8, g_1f0bcb8);
    addr = ptr;
    addr->field_b0 = g_1f0bcb0;
    sub_f7d8d0((struct SwipeSlasherChara_Recovered *)&addr->field_b0, g_1f0bcb0);
    ptr3 = ptr;
    ptr3->field_b8 = g_1f0bca8;
    sub_f7d8d0((struct SwipeSlasherChara_Recovered *)&ptr3->field_b8, g_1f0bca8);
    ptr4 = ptr;
    ptr4->field_c0 = g_1f0bc98;
    sub_f7d8d0((struct SwipeSlasherChara_Recovered *)&ptr4->field_c0, g_1f0bc98);
    ptr5 = ptr;
    ptr5->field_c8 = g_1f0bca0;
    sub_f7d8d0((struct SwipeSlasherChara_Recovered *)&ptr5->field_c8, g_1f0bca0);
    ptr6 = ptr;
    ptr6->field_d0 = g_1f0d680;
    sub_f7d8d0((struct SwipeSlasherChara_Recovered *)&ptr6->field_d0, g_1f0d680);
    ptr7 = ptr;
    ptr7->field_d8 = g_1f0d678;
    sub_f7d8d0((struct SwipeSlasherChara_Recovered *)&ptr7->field_d8, g_1f0d678);
    ptr8 = ptr;
    ptr8->field_e0 = g_1f0d670;
    sub_f7d8d0((struct SwipeSlasherChara_Recovered *)&ptr8->field_e0, g_1f0d670);
    ptr9 = ptr;
    ptr9->field_e8 = g_1f0d660;
    sub_f7d8d0((struct SwipeSlasherChara_Recovered *)&ptr9->field_e8, g_1f0d660);
    ptr10 = ptr;
    ptr10->field_f0 = g_1f0d668;
    sub_f7d8d0((struct SwipeSlasherChara_Recovered *)&ptr10->field_f0, g_1f0d668);
    ptr11 = ptr;
    ptr11->field_f8 = g_1f09b50;
    sub_f7d8d0((struct SwipeSlasherChara_Recovered *)&ptr11->field_f8, g_1f09b50);
    ptr->field_100 = g_1f09b58;
    sub_f7d8d0((struct SwipeSlasherChara_Recovered *)&ptr->field_100, g_1f09b58);
    MonoBehaviour__ctor();
    return;
}
```
