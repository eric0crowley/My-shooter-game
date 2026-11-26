# Native pseudocode: GamepadInputModule

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GamepadInputModule.IsModuleSupported` — RVA `0xc33f8c`

- Decompiled symbol: `GamepadInputModule_IsModuleSupported`
- Metadata signature: `public override bool IsModuleSupported() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int GamepadInputModule_IsModuleSupported(void)
{
    return 1;
}
```

## `GamepadInputModule.JustPressedSubmitButton` — RVA `0xc33f94`

- Decompiled symbol: `GamepadInputModule_JustPressedSubmitButton`
- Metadata signature: `private bool JustPressedSubmitButton() { }`
- Native interval: `228` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[128];
    struct struct_1 *field_80;
} struct_1;

typedef struct struct_1 {
    char padding_0[80];
    struct struct_0 *field_50;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

typedef struct struct_3 {
    struct struct_1 *field_0;
} struct_3;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_3 *field_b8;
} struct_2;

extern struct_2 *g_1eefb00;
extern struct_0 *g_1ef0c58;
extern char g_1fab148;
extern char g_1fab1dd;

unsigned int GamepadInputModule_JustPressedSubmitButton(unsigned int *a0)
{
    struct_1 *v0;  // x20

    if (!(g_1fab148 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab148 = 1;
    }
    if (((char)Input__GetKeyDown(13, 0) & 1))
        return 1;
    if (!g_1fab1dd)
    {
        sub_f7d92c(&g_1eefb00);
        g_1fab1dd = 1;
    }
    v0 = g_1eefb00->field_b8->field_0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(v0, 0, 0) & 1))
    {
        return 0;
    }
    else if (!v0)
    {
        sub_f7db74();
    }
    else if (!v0->field_80)
    {
        sub_f7db74();
    }
    else if (!((char)GamepadManager_Gamepad__GetKeyDown(v0->field_80, a0[22]) & 1))
    {
        if (!v0->field_80)
        {
            sub_f7db74();
        }
        else if (!((char)GamepadManager_Gamepad__GetKeyDown(v0->field_80, a0[23]) & 1))
        {
            return 0;
        }
    }
    return 1;
}
```

## `GamepadInputModule.JustPressedCancelButton` — RVA `0xc34078`

- Decompiled symbol: `GamepadInputModule_JustPressedCancelButton`
- Metadata signature: `private bool JustPressedCancelButton() { }`
- Native interval: `228` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[128];
    struct struct_1 *field_80;
} struct_1;

typedef struct struct_1 {
    char padding_0[80];
    struct struct_0 *field_50;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

typedef struct struct_3 {
    struct struct_1 *field_0;
} struct_3;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_3 *field_b8;
} struct_2;

extern struct_2 *g_1eefb00;
extern struct_0 *g_1ef0c58;
extern char g_1fab149;
extern char g_1fab1dd;

unsigned int GamepadInputModule_JustPressedCancelButton(unsigned int *a0)
{
    struct_1 *v0;  // x20

    if (!(g_1fab149 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab149 = 1;
    }
    if (((char)Input__GetKeyDown(27, 0) & 1))
        return 1;
    if (!g_1fab1dd)
    {
        sub_f7d92c(&g_1eefb00);
        g_1fab1dd = 1;
    }
    v0 = g_1eefb00->field_b8->field_0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(v0, 0, 0) & 1))
    {
        return 0;
    }
    else if (!v0)
    {
        sub_f7db74();
    }
    else if (!v0->field_80)
    {
        sub_f7db74();
    }
    else if (!((char)GamepadManager_Gamepad__GetKeyDown(v0->field_80, a0[24]) & 1))
    {
        if (!v0->field_80)
        {
            sub_f7db74();
        }
        else if (!((char)GamepadManager_Gamepad__GetKeyDown(v0->field_80, a0[25]) & 1))
        {
            return 0;
        }
    }
    return 1;
}
```

## `GamepadInputModule.JustPressedDirectionKey` — RVA `0xc3415c`

- Decompiled symbol: `GamepadInputModule_JustPressedDirectionKey`
- Metadata signature: `private MoveDirection JustPressedDirectionKey() { }`
- Native interval: `728` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[128];
    struct struct_3 *field_80;
} struct_4;

typedef struct struct_3 {
    char padding_0[56];
    struct struct_1 *field_38;
    char padding_40[8];
    struct struct_2 *field_48;
} struct_3;

typedef struct struct_1 {
    char padding_0[24];
    long long field_18;
} struct_1;

typedef struct struct_2 {
    char padding_0[24];
    long long field_18;
} struct_2;

typedef struct struct_6 {
    struct struct_4 *field_0;
} struct_6;

typedef struct struct_5 {
    char padding_0[184];
    struct struct_6 *field_b8;
} struct_5;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_5 *g_1eefb00;
extern struct_0 *g_1ef0c58;
extern char g_1fab14a;
extern char g_1fab1dd;

unsigned int GamepadInputModule_JustPressedDirectionKey(void)
{
    unsigned int v0;  // w19
    unsigned int v1;  // w20
    unsigned int v10;  // w8
    unsigned long v11;  // 4124
    unsigned int v12;  // w0
    unsigned int v13;  // w8
    unsigned long v14;  // 4126
    unsigned int v2;  // w21
    unsigned int v3;  // w22
    struct_4 *v4;  // x23
    unsigned int v5;  // w8
    unsigned int v6;  // w8
    unsigned int v7;  // w24
    unsigned int v8;  // w8
    unsigned int v9;  // w8

    if (!(g_1fab14a & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab14a = 1;
    }
    v0 = Input__GetKeyDown(276, 0);
    v1 = Input__GetKeyDown(275, 0);
    v2 = Input__GetKeyDown(273, 0);
    v3 = Input__GetKeyDown(274, 0);
    if (!g_1fab1dd)
    {
        sub_f7d92c(&g_1eefb00);
        g_1fab1dd = 1;
    }
    v4 = g_1eefb00->field_b8->field_0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(v4, 0, 0) & 1))
    {
LABEL_10343cc:
        v9 = v3 & v2;
        if ((v2 & 1) != (v9 & 1))
            return 1;
        v10 = v3 ^ v9;
        v11 = arm64g_calculate_condition(25, (unsigned long long)(v10 & 1), 0, 0);
        if ((char)v11)
            v12 = 3;
        else
            v12 = 0;
        if (((char)v10 & 1))
            return v12;
        v13 = v1 & v0;
        if ((((char)v0 ^ (char)v13) & 1))
            return v12;
        v14 = arm64g_calculate_condition(25, (unsigned long long)((v1 ^ v13) & 1), 0, 0);
        if (!((char)v14))
            return 4;
        return 2;
    }
    if (v4 && v4->field_80 && v4->field_80->field_38 && v4->field_80->field_38->field_18)
    {
        if (((char)JoystickState__JustPressedDir4(v4->field_80->field_38->field_18, 7, 0) & 1))
        {
            v5 = 1;
            goto LABEL_1034288;
        }
        if (v4->field_80 && v4->field_80->field_48 && v4->field_80->field_48->field_18)
        {
            v5 = JoystickState__JustPressedDir4(v4->field_80->field_48->field_18, 7, 0) & 1;
LABEL_1034288:
            if (!v5 && !((char)v0 & 1))
                v0 = 0;
            else
                v0 = 1;
            if (v4->field_80 && v4->field_80->field_38 && v4->field_80->field_38->field_18)
            {
                if (((char)JoystickState__JustPressedDir4(v4->field_80->field_38->field_18, 3, 0) & 1))
                {
                    v6 = 1;
                    goto LABEL_10342f0;
                }
                else if (v4->field_80 && v4->field_80->field_48 && v4->field_80->field_48->field_18)
                {
                    v6 = JoystickState__JustPressedDir4(v4->field_80->field_48->field_18, 3, 0) & 1;
LABEL_10342f0:
                    if (!v6 && !((char)v1 & 1))
                        v1 = 0;
                    else
                        v1 = 1;
                    if (v4->field_80 && v4->field_80->field_38 && v4->field_80->field_38->field_18)
                    {
                        v7 = 1;
                        if (((char)JoystickState__JustPressedDir4(v4->field_80->field_38->field_18, 1, 0) & 1))
                        {
LABEL_1034354:
                            if (!v7 && !((char)v2 & 1))
                                v2 = 0;
                            else
                                v2 = 1;
                            if (v4->field_80 && v4->field_80->field_38 && v4->field_80->field_38->field_18)
                            {
                                if (((char)JoystickState__JustPressedDir4(v4->field_80->field_38->field_18, 5, 0) & 1))
                                {
                                    v8 = 1;
                                    goto LABEL_10343bc;
                                }
                                else
                                {
                                    if (v4->field_80 && v4->field_80->field_48 && v4->field_80->field_48->field_18)
                                    {
                                        v8 = JoystickState__JustPressedDir4(v4->field_80->field_48->field_18, 5, 0) & 1;
LABEL_10343bc:
                                        if (!v8 && !((char)v3 & 1))
                                        {
                                            v3 = 0;
                                            goto LABEL_10343cc;
                                        }
                                        else
                                        {
                                            v3 = 1;
                                            goto LABEL_10343cc;
                                        }
                                    }
                                }
                            }
                        }
                        else if (v4->field_80 && v4->field_80->field_48 && v4->field_80->field_48->field_18)
                        {
                            v7 = JoystickState__JustPressedDir4(v4->field_80->field_48->field_18, 1, 0) & 1;
                            goto LABEL_1034354;
                        }
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `GamepadInputModule.ShouldActivateModule` — RVA `0xc34434`

- Decompiled symbol: `GamepadInputModule_ShouldActivateModule`
- Metadata signature: `public override bool ShouldActivateModule() { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
unsigned long long GamepadInputModule_ShouldActivateModule(unsigned int *a0)
{
    if (!((char)BaseInputModule__ShouldActivateModule() & 1))
        return 0;
    if (((char)GamepadInputModule__JustPressedCancelButton(a0) & 1) || ((char)GamepadInputModule__JustPressedSubmitButton(a0) & 1))
        return 1;
    if (GamepadInputModule__JustPressedDirectionKey() == 4)
        return 0;
    return 1;
    return 1;
}
```

## `GamepadInputModule.ActivateModule` — RVA `0xc34484`

- Decompiled symbol: `GamepadInputModule_ActivateModule`
- Metadata signature: `public override void ActivateModule() { }`
- Native interval: `440` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    struct struct_1 *field_0;
    char padding_8[48];
    struct struct_4 *field_38;
} struct_3;

typedef struct struct_1 {
    char padding_0[616];
    struct struct_2 *field_268;
    unsigned long long field_270;
} struct_1;

typedef struct struct_4 {
    char padding_0[48];
    long long field_30;
    char padding_38[8];
    long long field_40;
} struct_4;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab14b;

long long GamepadInputModule_ActivateModule(struct_3 *idx)
{
    unsigned long long choice;  // x2
    struct_3 *v1;  // x0
    unsigned long v2;  // x1
    unsigned long v3;  // x20
    unsigned long long flag;  // x2
    long long v5;  // x0
    struct_3 *v6;  // x0
    unsigned long v7;  // x1

    if (!(g_1fab14b & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab14b = 1;
    }
    BaseInputModule__ActivateModule(idx, 0);
    if (!idx->field_38)
        sub_f7db74();
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    choice = 0;
    if (((char)Object__op_Inequality(idx->field_38->field_40, 0, 0) & 1))
    {
        v1 = idx;
        v2 = idx->field_0->field_270;
        idx->field_0->field_268();
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Equality(idx->field_38->field_40, 0, 0) & 1))
    {
        v3 = GamepadInputModule__FindFirstSelectableInScene();
    }
    else if (idx->field_38)
    {
        v3 = idx->field_38->field_30;
    }
    else
    {
        sub_f7db74();
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    flag = 0;
    v5 = Object__op_Inequality(v3, 0, 0);
    if (!((char)v5 & 1))
        return v5;
    v6 = idx;
    v7 = idx->field_0->field_270;
    idx->field_0->field_268();
}
```

## `GamepadInputModule.SendMoveEventToSelectedObject` — RVA `0xc3463c`

- Decompiled symbol: `GamepadInputModule_SendMoveEventToSelectedObject`
- Metadata signature: `protected bool SendMoveEventToSelectedObject() { }`
- Native interval: `800` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[128];
    struct struct_3 *field_80;
} struct_4;

typedef struct struct_3 {
    char padding_0[56];
    struct struct_1 *field_38;
    char padding_40[8];
    struct struct_2 *field_48;
} struct_3;

typedef struct struct_1 {
    char padding_0[24];
    long long field_18;
} struct_1;

typedef struct struct_2 {
    char padding_0[24];
    long long field_18;
} struct_2;

typedef struct struct_7 {
    char padding_0[600];
    struct struct_8 *field_258;
    unsigned long long field_260;
} struct_7;

typedef struct struct_8 {
    unsigned long long field_0;
} struct_8;

typedef struct struct_6 {
    struct struct_4 *field_0;
} struct_6;

typedef struct struct_5 {
    char padding_0[184];
    struct struct_6 *field_b8;
} struct_5;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eef870;
extern struct_5 *g_1eefb00;
extern struct_0 *g_1ef0c58;
extern long long g_1efe558;
extern char g_1fab14e;
extern char g_1fab1dd;

int GamepadInputModule_SendMoveEventToSelectedObject(struct_7 **a0)
{
    unsigned long long v12;  // d11
    unsigned long long v13;  // d10
    unsigned long long v22;  // x19
    struct_4 *addr;  // x20
    struct_3 *idx;  // x8
    long long v25;  // x21
    unsigned long v26;  // x20
    long long v27;  // x0
    unsigned long long flag;  // x2
    unsigned int v29;  // s11
    unsigned int v30;  // s10
    unsigned long v31;  // 4113
    unsigned long long v14;  // d9
    unsigned int v32;  // w0
    unsigned int *ptr;  // x8
    unsigned long v34;  // 4115
    unsigned int *v35;  // x21
    unsigned int *p;  // x20
    unsigned int v37;  // s0
    unsigned int v38;  // s1
    unsigned long v40;  // 4172
    struct_7 **v41;  // x0
    unsigned long long v15;  // d8
    unsigned long v42;  // x1
    unsigned long long v16;  // x30
    unsigned long long v17;  // x24
    unsigned long long v18;  // x23
    unsigned long long v19;  // x22
    unsigned long long v20;  // x21
    unsigned long long v21;  // x20
    unsigned long long v0;  // [bp-0x60]
    unsigned long long v1;  // [bp-0x58]
    unsigned long long v2;  // [bp-0x50]
    unsigned long long v3;  // [bp-0x48]
    unsigned long long v4;  // [bp-0x40]
    unsigned int choice;  // [bp-0x38]
    unsigned long long v6;  // [bp-0x30]
    unsigned long long v7;  // [bp-0x28]
    unsigned long long v8;  // [bp-0x20]
    unsigned long long v9;  // [bp-0x18]
    unsigned long long v10;  // [bp-0x10]
    unsigned long long v11;  // [bp-0x8]

    v0 = v12;
    v1 = v13;
    v2 = v14;
    v3 = v15;
    v4 = v16;
    v6 = v17;
    v7 = v18;
    v8 = v19;
    v9 = v20;
    v10 = v21;
    v11 = v22;
    if (!(g_1fab14e & 1))
    {
        sub_f7d92c(&g_1efe558);
        sub_f7d92c(&g_1eef870);
        sub_f7d92c(&g_1ef0c58);
        g_1fab14e = 1;
    }
    choice = 0;
    if (!g_1fab1dd)
    {
        sub_f7d92c(&g_1eefb00);
        g_1fab1dd = 1;
    }
    addr = g_1eefb00->field_b8->field_0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(addr, 0, 0) & 1))
        return sub_1034938();
    if (!addr || !((idx = (struct_3 *)addr->field_80, idx && idx->field_38 && idx->field_48 && (v25 = idx->field_38->field_18, v25))))
        sub_f7db74();
    v26 = idx->field_48->field_18;
    if (!((char)JoystickState__JustReleasedDir4(v25, 0, 0) & 1))
    {
        if (!v26)
            sub_f7db74();
        v27 = 0;
        v25 = v26;
        if (!(JoystickState__JustReleasedDir4(v26, 0, 0) & 4294967295 & 1))
            goto LABEL_1034760;
    }
    v27 = JoystickState__GetDir4(v25, 0);
LABEL_1034760:
    flag = 0;
    CFUtils__DirToVector(v27, 0, 0);
    v29 = 0x3f800000;
    v30 = 0x3f800000;
    if (!((char)Input__GetKeyDown(275, 0) & 1))
    {
        v31 = arm64g_calculate_condition(25, (unsigned long long)((unsigned int)(unsigned long long)Input__GetKeyDown(276, 0) & 1), 0, 0);
        if ((char)v31)
            v30 = 0xbf800000;
        else
            v30 = 0;
    }
    v32 = Input__GetKeyDown(273, 0);
    ptr = &choice;
    v34 = arm64g_calculate_condition(25, (unsigned long long)(v32 & 1), 0, 0);
    if ((char)v34)
        v35 = NULL;
    else
        v35 = &choice;
    p = &choice | 4;
    if (!((char)v32 & 1))
    {
        if (((char)Input__GetKeyDown(274, 0) & 1))
        {
            v29 = 0xbf800000;
            ptr = &choice;
        }
        else
        {
            p = v35 + 1;
            v29 = 0;
            ptr = v35;
        }
    }
    *(ptr) = v30;
    *(p) = v29;
    CFUtils__ApplyDeltaInput(0);
    CFUtils__ApplyDeltaInput(0);
    v40 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v37 * v37 + v38 * v38, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v37 * v37 + v38 * v38, 925353388) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v37 * v37 + v38 * v38, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v37 * v37 + v38 * v38, 925353388) & 1)) & ((unsigned long long)(char)(CmpF(v37 * v37 + v38 * v38, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v37 * v37 + v38 * v38, 925353388) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v40))
    {
        v41 = a0;
        v42 = *(a0)->field_260;
        *(a0)->field_258();
    }
    return sub_1034938();
}
```

## `GamepadInputModule.FindFirstSelectableInScene` — RVA `0xc3495c`

- Decompiled symbol: `GamepadInputModule_FindFirstSelectableInScene`
- Metadata signature: `private GameObject FindFirstSelectableInScene() { }`
- Native interval: `368` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[224];
    unsigned int field_e0;
} struct_3;

typedef struct struct_4 {
    char padding_0[40];
    unsigned int field_28;
} struct_4;

typedef struct struct_5 {
    char padding_0[24];
    int field_18;
} struct_5;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eeb950;
extern struct_0 *g_1ef0c58;
extern struct_3 *g_1ef1f08;
extern char g_1fab14c;

unsigned int GamepadInputModule_FindFirstSelectableInScene(void)
{
    struct_3 **v0;  // x20
    struct_4 *v1;  // x19
    struct_4 *v2;  // x0
    struct_5 *ptr;  // x0
    int i;  // w8
    int v5;  // w9
    struct_4 *v6;  // x10

    v0 = &g_1ef1f08;
    if (!(g_1fab14c & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("-)");
        sub_f7d92c(&g_1eeb950);
        sub_f7d92c(&g_1ef1f08);
        g_1fab14c = 1;
    }
    if (!g_1ef1f08->field_e0)
        sub_f7da5c(g_1ef1f08);
    v1 = Type__GetTypeFromHandle(g_1eeb950, 0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v2 = Object__FindObjectsOfType(v1, 0);
    if (v2)
    {
        v0 = g_1eee360;
        ptr = sub_f7da60();
        if (!ptr)
            sub_f7df10(v2, g_1eee360);
        i = ptr->field_18;
        if (i >= 1)
        {
            v5 = 0;
            v1 = NULL;
            do
            {
                if (i <= v5)
                {
                    sub_f7db7c(ptr);
                    sub_f7df10(v1, v0);
                }
                v6 = *((long long *)&ptr[1].padding_0[4 + 8 * v5]);
                if (!v6)
                    goto LABEL_1034ab8;
                else
                    goto LABEL_1034a4c;
LABEL_1034a4c:
                v5 += 1;
                if (v6->field_28)
                    v1 = v6;
            } while (i != v5);
            goto LABEL_1034a6c;
        }
        else
        {
            v1 = NULL;
LABEL_1034a6c:
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (!((char)Object__op_Inequality(v1, 0, 0) & 1))
            {
                return 0;
            }
            else if (v1)
            {
                return Component__get_gameObject();
            }
        }
    }
LABEL_1034ab8:
    ptr = sub_f7db74();
    sub_f7db7c(ptr);
    sub_f7df10(v1, v0);
}
```

## `GamepadInputModule.DeactivateModule` — RVA `0xc34acc`

- Decompiled symbol: `GamepadInputModule_DeactivateModule`
- Metadata signature: `public override void DeactivateModule() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long GamepadInputModule_DeactivateModule(void)
{
}
```

## `GamepadInputModule.Process` — RVA `0xc34ad4`

- Decompiled symbol: `GamepadInputModule_Process`
- Metadata signature: `public override void Process() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[56];
    struct struct_0 *field_38;
} struct_1;

typedef struct struct_0 {
    char padding_0[56];
    char field_38;
} struct_0;

unsigned long long GamepadInputModule_Process(struct_1 *a0)
{
    unsigned long long v0;  // x0
    unsigned int v1;  // w8
    unsigned long long v2;  // x0
    unsigned long long v3;  // x0

    v0 = GamepadInputModule__SendUpdateEventToSelectedObject();
    if (a0->field_38)
    {
        if (a0->field_38->field_38)
            v1 = 0;
        else
            v1 = 1;
        if ((((char)v0 | (char)v1) & 1))
            return v0;
        v2 = GamepadInputModule__SendMoveEventToSelectedObject(a0);
        if (!((char)v2 & 1))
        {
            v3 = GamepadInputModule__SendSubmitEventToSelectedObject(a0);
            return GamepadInputModule__SendSubmitEventToSelectedObject(a0);
        }
        return v2;
    }
    sub_f7db74();
}
```

## `GamepadInputModule.SendUpdateEventToSelectedObject` — RVA `0xc34b20`

- Decompiled symbol: `GamepadInputModule_SendUpdateEventToSelectedObject`
- Metadata signature: `protected bool SendUpdateEventToSelectedObject() { }`
- Native interval: `328` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    struct struct_1 *field_0;
    char padding_8[48];
    struct struct_3 *field_38;
} struct_4;

typedef struct struct_5 {
    char padding_0[64];
    unsigned long long field_40;
} struct_5;

typedef struct struct_1 {
    char padding_0[616];
    struct struct_2 *field_268;
    unsigned long long field_270;
} struct_1;

typedef struct struct_3 {
    char padding_0[64];
    long long field_40;
} struct_3;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eef870;
extern struct_0 *g_1ef0c58;
extern long long g_1efe598;
extern char g_1fab14f;

unsigned int GamepadInputModule_SendUpdateEventToSelectedObject(struct_4 *a0)
{
    unsigned long long flag;  // x2
    struct_4 *v1;  // x0
    unsigned long v2;  // x1

    if (!(g_1fab14f & 1))
    {
        sub_f7d92c(&g_1efe598);
        sub_f7d92c(&g_1eef870);
        sub_f7d92c(&g_1ef0c58);
        g_1fab14f = 1;
    }
    if (!a0->field_38)
        sub_f7db74();
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    flag = 0;
    if (((char)Object__op_Equality(a0->field_38->field_40, 0, 0) & 1))
        return 0;
    v1 = a0;
    v2 = a0->field_0->field_270;
    a0->field_0->field_268();
}
```

## `GamepadInputModule.SendSubmitEventToSelectedObject` — RVA `0xc34c68`

- Decompiled symbol: `GamepadInputModule_SendSubmitEventToSelectedObject`
- Metadata signature: `protected bool SendSubmitEventToSelectedObject() { }`
- Native interval: `572` bytes
- Result: `pseudocode`

```c
typedef struct struct_6 {
    struct struct_3 *field_0;
    char padding_8[48];
    struct struct_5 *field_38;
} struct_6;

typedef struct struct_7 {
    char padding_0[64];
    unsigned long long field_40;
} struct_7;

typedef struct struct_3 {
    char padding_0[616];
    struct struct_4 *field_268;
    unsigned long long field_270;
} struct_3;

typedef struct struct_5 {
    char padding_0[64];
    long long field_40;
} struct_5;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

typedef struct struct_2 {
    long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_1;

extern long long g_1eef870;
extern struct_1 *g_1eefb00;
extern struct_0 *g_1ef0c58;
extern long long g_1efe530;
extern long long g_1efe590;
extern char g_1fab14d;
extern char g_1fab1dd;

unsigned int GamepadInputModule_SendSubmitEventToSelectedObject(struct_6 *a0)
{
    unsigned long long flag;  // x2
    struct_6 *v1;  // x0
    unsigned long v2;  // x1

    if (!(g_1fab14d & 1))
    {
        sub_f7d92c(&g_1efe530);
        sub_f7d92c(&g_1efe590);
        sub_f7d92c(&g_1eef870);
        sub_f7d92c(&g_1ef0c58);
        g_1fab14d = 1;
    }
    if (!a0->field_38)
        sub_f7db74();
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(a0->field_38->field_40, 0, 0) & 1))
        return 0;
    if (!g_1fab1dd)
    {
        sub_f7d92c(&g_1eefb00);
        g_1fab1dd = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    flag = 0;
    if (((char)Object__op_Equality(g_1eefb00->field_b8->field_0, 0, 0) & 1))
        return 0;
    v1 = a0;
    v2 = a0->field_0->field_270;
    a0->field_0->field_268();
}
```

## `GamepadInputModule.ctor` — RVA `0xc34ea4`

- Decompiled symbol: `GamepadInputModule_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `28` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadInputModule_Recovered` matched 2 offsets against `GamepadInputModule` metadata (confidence 1.00).

```c
typedef struct GamepadInputModule_Recovered {
    char padding_0[92];
    unsigned long long submitGamepadButtonAlt;
    unsigned int cancelGamepadButtonAlt;
} GamepadInputModule_Recovered;

long long GamepadInputModule_ctor(struct_0 *ptr)
{
    *((unsigned int *)((char *)&ptr->field_5c + 4)) = 5;
    *((unsigned long long *)&(&ptr->padding_0)[1]) = 4294967300;
}
```
