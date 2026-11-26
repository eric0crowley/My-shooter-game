# Native pseudocode: GamepadManager.Gamepad

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GamepadManager.Gamepad.ctor` — RVA `0xc2af14`

- Decompiled symbol: `GamepadManager_Gamepad_ctor`
- Metadata signature: `public void .ctor(GamepadManager manager) { }`
- Native interval: `960` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_Recovered` matched 7 offsets against `GamepadManager.Gamepad` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Gamepad_Recovered {
    char padding_0[16];
    struct struct_11 *manager;
    char padding_18[32];
    long long leftStick;
    long long rightStick;
    long long dpad;
    struct struct_5 *keys;
    struct struct_7 *internalAxes;
    struct struct_9 *internalKeys;
} GamepadManager_Gamepad_Recovered;

typedef struct struct_1 {
    struct struct_0 *field_0;
    char padding_8[16];
    unsigned int field_18;
} struct_1;

typedef struct struct_3 {
    struct struct_2 *field_0;
    char padding_8[16];
    unsigned int field_18;
} struct_3;

typedef struct struct_14 {
    char padding_0[16];
    unsigned int field_10;
    char field_14;
    char padding_15[1];
    char field_16;
} struct_14;

typedef struct struct_13 {
    struct struct_12 *field_0;
    char padding_8[16];
    unsigned int field_18;
} struct_13;

typedef struct struct_11 {
    char padding_0[64];
    unsigned long long field_40;
    unsigned long long field_48;
    unsigned long long field_50;
} struct_11;

typedef struct struct_5 {
    struct struct_4 *field_0;
    char padding_8[16];
    unsigned int field_18;
} struct_5;

typedef struct struct_7 {
    struct struct_6 *field_0;
    char padding_8[16];
    unsigned int field_18;
} struct_7;

typedef struct struct_9 {
    struct struct_8 *field_0;
    char padding_8[16];
    unsigned int field_18;
} struct_9;

typedef struct struct_0 {
    char padding_0[64];
    unsigned long long field_40;
} struct_0;

typedef struct struct_2 {
    char padding_0[64];
    unsigned long long field_40;
} struct_2;

typedef struct struct_12 {
    char padding_0[64];
    unsigned long long field_40;
} struct_12;

typedef struct struct_4 {
    char padding_0[64];
    long long field_40;
} struct_4;

typedef struct struct_6 {
    char padding_0[64];
    long long field_40;
} struct_6;

typedef struct struct_8 {
    char padding_0[64];
    long long field_40;
} struct_8;

extern long long g_1eee600;
extern long long g_1eee608;
extern long long g_1eee610;
extern char g_1fab117;
extern char g_8322d8;

long long GamepadManager_Gamepad_ctor(struct_10 *a0, long long *a1)
{
    struct_10 *ptr5;  // x0
    struct_1 *v3;  // x0
    long long v12;  // x0
    unsigned long v13;  // x26
    struct_3 *v14;  // x28
    unsigned long j;  // x23
    struct_14 *ptr;  // x22
    unsigned long v17;  // x25
    long long v18;  // x22
    struct_10 *ptr6;  // x0
    long long v20;  // x22
    struct_10 *ptr7;  // x0
    struct_10 *ptr8;  // x22
    long long v22;  // x22
    struct_10 *ptr9;  // x0
    struct_13 *v24;  // x0
    struct_10 *ptr10;  // x21
    struct_10 *p;  // x21
    struct_13 *v27;  // x27
    unsigned long v28;  // x25
    unsigned long long v29;  // x26
    long long v30;  // x22
    long long *ptr4;  // x0
    struct_10 *addr;  // x22
    unsigned long long v32;  // x0
    struct_3 *v6;  // x0
    struct_10 *ptr11;  // x21
    struct_10 *ptr3;  // x21
    struct_1 *i;  // x25
    unsigned long v10;  // x28
    long long v11;  // x23
    char *v0;  // [bp-0x60]
    char v1;  // [bp+0x0]

    v0 = &v1;
    if (!(g_1fab117 & 1))
    {
        sub_f7d92c(&g_1eee600);
        sub_f7d92c("3w");
        sub_f7d92c(&g_1eee608);
        sub_f7d92c("5w");
        sub_f7d92c("7w");
        sub_f7d92c(&g_1eee610);
        sub_f7d92c(";w");
        g_1fab117 = 1;
    }
    Object__ctor(a0, 0);
    ptr5 = a0;
    ptr5->field_10 = a1;
    sub_f7d8d0((struct GamepadManager_Gamepad_Recovered *)&ptr5->field_10, a1);
    v3 = sub_f7d9d4(g_1eee600, 10);
    ptr8 = a0;
    ptr8->field_58 = v3;
    addr = &ptr8->field_58;
    sub_f7d8d0(addr, v3);
    v6 = sub_f7d9d4(g_1eee608, 20);
    ptr11 = a0;
    ptr11->field_60 = v6;
    ptr3 = &ptr11->field_60;
    sub_f7d8d0(ptr3, v6);
    i = *((long long *)&addr->padding_0[0]);
    if (i)
    {
        v10 = 0;
        do
        {
            if (i->field_18 <= v10 && *((long long *)&ptr3->padding_0[0]))
            {
                j = 0;
                while (v14->field_18 > j)
                {
                    ptr = sub_f7db70(g_1ef4230);
                    Object__ctor(ptr, 0);
                    ptr->field_16 = 0;
                    ptr->field_14 = 0;
                    ptr->field_10 = 0;
                    v12 = sub_f7da60(ptr, v14->field_0->field_40);
                    if (!v12)
                        sub_f7da4c(sub_f7db98(v12), 0);
                    if (v14->field_18 <= j)
                        goto LABEL_102b2c4;
                    *((struct_14 **)((char *)&(&v14[1].field_0)[j] + 4)) = ptr;
                    sub_f7d8d0((struct struct_3 *)((char *)v14 + v17), ptr);
                    j += 1;
                    if (!*((long long *)&ptr3->padding_0[0]))
                        goto LABEL_102b2c0;
                }
                if (a1)
                {
                    v18 = sub_f7db70(g_1ef4238);
                    GamepadManager_Gamepad_JoyState__ctor(v18, a0, a1[9]);
                    ptr6 = a0;
                    ptr6->field_38 = v18;
                    sub_f7d8d0((struct GamepadManager_Gamepad_Recovered *)&ptr6->field_38, v18);
                    v20 = sub_f7db70(g_1ef4238);
                    GamepadManager_Gamepad_JoyState__ctor(v20, a0, a1[10]);
                    ptr7 = a0;
                    ptr7->field_40 = v20;
                    sub_f7d8d0((struct GamepadManager_Gamepad_Recovered *)&ptr7->field_40, v20);
                    v22 = sub_f7db70(g_1ef4238);
                    GamepadManager_Gamepad_JoyState__ctor(v22, a0, a1[8]);
                    ptr9 = a0;
                    ptr9->field_48 = v22;
                    sub_f7d8d0((struct GamepadManager_Gamepad_Recovered *)&ptr9->field_48, v22);
                    v24 = sub_f7d9d4(g_1eee610, 12);
                    ptr10 = a0;
                    ptr10->field_50 = v24;
                    p = &ptr10->field_50;
                    sub_f7d8d0(p, v24);
                    v27 = *((long long *)&p->padding_0[0]);
                    if (!v27)
                        break;
                    v28 = 0;
                    v29 = 32;
                    while (true)
                    {
                        if (v27->field_18 <= v28)
                        {
                            v32 = GamepadManager_Gamepad__OnDisconnect(a0);
                            return GamepadManager_Gamepad__OnDisconnect(a0);
                        }
                        if (3 >= (unsigned int)v28 - 6)
                            goto sub_102b214 + (&g_8322d8)[6 + v28] * 4;
                        v30 = sub_f7db70(g_1ef4240);
                        v12 = GamepadManager_Gamepad_KeyState__ctor();
                        if (v30 && (v12 = sub_f7da60(v30, v27->field_0->field_40), !v12))
                            goto LABEL_102b2c8;
                        if (v27->field_18 <= v28)
                            break;
                        ptr4 = (char *)v27 + v29;
                        *(ptr4) = v30;
                        sub_f7d8d0(ptr4, v30);
                        v27 = *((long long *)&p->padding_0[0]);
                        v28 += 1;
                        v29 += 8;
                        if (!v27)
                            goto LABEL_102b2c0;
                    }
                }
                break;
            }
            v11 = sub_f7db70(g_1ef4228);
            v12 = GamepadManager_Gamepad_InternalAxisState__ctor(v11);
            if (v11 && (v12 = sub_f7da60(v11, i->field_0->field_40), !v12))
                goto LABEL_102b2c8;
            if (i->field_18 <= v10)
                goto LABEL_102b2c4;
            *((long long *)((char *)&(&i[1].field_0)[v10] + 4)) = v11;
            sub_f7d8d0((struct struct_1 *)((char *)i + v13), v11);
            i = *((long long *)&addr->padding_0[0]);
            v10 += 1;
        } while (i);
        goto LABEL_102b2c8;
    }
LABEL_102b2c0:
    v12 = sub_f7db74();
LABEL_102b2c4:
    v12 = sub_f7db7c(v12);
LABEL_102b2c8:
    sub_f7da4c(sub_f7db98(v12), 0);
}
```

## `GamepadManager.Gamepad.SetRig` — RVA `0xc2bd0c`

- Decompiled symbol: `GamepadManager_Gamepad_SetRig`
- Metadata signature: `public void SetRig(InputRig rig) { }`
- Native interval: `760` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_Recovered` matched 5 offsets against `GamepadManager.Gamepad` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Gamepad_Recovered {
    char padding_0[16];
    unsigned long long manager;
    char padding_18[32];
    struct struct_2 *leftStick;
    struct struct_4 *rightStick;
    struct struct_6 *dpad;
    struct struct_11 *keys;
} GamepadManager_Gamepad_Recovered;

typedef struct struct_2 {
    char padding_0[24];
    struct struct_1 *field_18;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    long long field_10;
} struct_1;

typedef struct struct_4 {
    char padding_0[24];
    struct struct_3 *field_18;
} struct_4;

typedef struct struct_3 {
    char padding_0[16];
    long long field_10;
} struct_3;

typedef struct struct_6 {
    char padding_0[24];
    struct struct_5 *field_18;
} struct_6;

typedef struct struct_5 {
    char padding_0[16];
    long long field_10;
} struct_5;

typedef struct struct_11 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[52];
    struct struct_7 *field_50;
    struct struct_8 *field_58;
    struct struct_9 *field_60;
    struct struct_10 *field_68;
} struct_11;

typedef struct struct_7 {
    char padding_0[32];
    long long field_20;
} struct_7;

typedef struct struct_9 {
    char padding_0[32];
    long long field_20;
} struct_9;

typedef struct struct_8 {
    char padding_0[32];
    long long field_20;
} struct_8;

typedef struct struct_10 {
    char padding_0[32];
    long long field_20;
} struct_10;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab119;

void GamepadManager_Gamepad_SetRig(struct_12 *ptr, long long *a1)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    long long v15;  // x1
    long long p[29];  // x8
    struct_5 *ptr7;  // x0
    long long v18;  // x1
    unsigned long v19;  // x0
    struct_11 *ptr8;  // x8
    struct_7 *ptr9;  // x21
    long long addr[29];  // x8
    long long v23;  // x1
    struct_11 *ptr10;  // x8
    unsigned long long v7;  // x21
    struct_9 *ptr11;  // x21
    long long ptr3[29];  // x8
    long long v27;  // x1
    struct_11 *ptr12;  // x8
    struct_8 *ptr13;  // x21
    long long ptr4[29];  // x8
    long long v31;  // x1
    struct_11 *idx4;  // x8
    long long v33[29];  // x8
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long ptr5[29];  // x8
    struct_1 *ptr14;  // x0
    long long v12;  // x1
    long long ptr6[29];  // x8
    struct_3 *ptr15;  // x0
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
    if (!(g_1fab119 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab119 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(a1, 0, 0) & 1))
    {
        if (a1)
            ptr5 = a1 + 25;
    }
    else
    {
        if (ptr->field_10 && !((ptr5 = (long long [29])(ptr->field_10 + 72), !ptr->field_38 || (ptr14 = (struct_1 *)ptr->field_38->field_18, !ptr14))))
        {
            v12 = ptr5[0];
            ptr14->field_10 = v12;
            sub_f7d8d0((struct struct_1 *)&ptr14->field_10, v12);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Inequality(a1, 0, 0) & 1))
            {
                if (a1)
                    ptr6 = a1 + 26;
            }
            else
            {
                if (ptr->field_10 && !((ptr6 = (long long [29])(ptr->field_10 + 80), !ptr->field_40 || (ptr15 = (struct_3 *)ptr->field_40->field_18, !ptr15))))
                {
                    v15 = ptr6[0];
                    ptr15->field_10 = v15;
                    sub_f7d8d0((struct struct_3 *)&ptr15->field_10, v15);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (((char)Object__op_Inequality(a1, 0, 0) & 1))
                    {
                        if (a1)
                            p = a1 + 24;
                    }
                    else
                    {
                        if (ptr->field_10 && !((p = (long long [29])(ptr->field_10 + 64), !ptr->field_48 || (ptr7 = (struct_5 *)ptr->field_48->field_18, !ptr7 || (v18 = p[0], ptr7->field_10 = v18, v19 = (unsigned long)sub_f7d8d0(ptr7 + 16, v18), ptr8 = (struct_11 *)ptr->field_50, !ptr8)))))
                        {
                            if (ptr8->field_18 <= 6)
                                goto LABEL_102c000;
                            ptr9 = ptr8->field_50;
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            if (((char)Object__op_Inequality(a1, 0, 0) & 1))
                            {
                                if (a1)
                                    addr = a1 + 27;
                            }
                            else
                            {
                                if (ptr->field_10 && !((addr = (long long [29])(ptr->field_10 + 88), !ptr9 || (v23 = addr[0], ptr9->field_20 = v23, v19 = (unsigned long)sub_f7d8d0(ptr9 + 32, v23), ptr10 = (struct_11 *)ptr->field_50, !ptr10))))
                                {
                                    if (ptr10->field_18 <= 8)
                                        goto LABEL_102c000;
                                    ptr11 = ptr10->field_60;
                                    if (!g_1ef0c58->field_e0)
                                        sub_f7da5c(g_1ef0c58);
                                    if (((char)Object__op_Inequality(a1, 0, 0) & 1))
                                    {
                                        if (a1)
                                            ptr3 = a1 + 27;
                                    }
                                    else
                                    {
                                        if (ptr->field_10 && !((ptr3 = (long long [29])(ptr->field_10 + 88), !ptr11 || (v27 = ptr3[0], ptr11->field_20 = v27, v19 = (unsigned long)sub_f7d8d0(ptr11 + 32, v27), ptr12 = (struct_11 *)ptr->field_50, !ptr12))))
                                        {
                                            if (ptr12->field_18 <= 7)
                                                goto LABEL_102c000;
                                            ptr13 = ptr12->field_58;
                                            if (!g_1ef0c58->field_e0)
                                                sub_f7da5c(g_1ef0c58);
                                            if (((char)Object__op_Inequality(a1, 0, 0) & 1))
                                            {
                                                if (a1)
                                                    ptr4 = a1 + 28;
                                            }
                                            else
                                            {
                                                if (ptr->field_10 && !((ptr4 = (long long [29])(ptr->field_10 + 96), !ptr13 || (v31 = ptr4[0], ptr13->field_20 = v31, v19 = (unsigned long)sub_f7d8d0(ptr13 + 32, v31), idx4 = (struct_11 *)ptr->field_50, !idx4))))
                                                {
                                                    if (idx4->field_18 <= 9)
                                                        goto LABEL_102c000;
                                                    if (!g_1ef0c58->field_e0)
                                                        sub_f7da5c(g_1ef0c58);
                                                    if (((char)Object__op_Inequality(a1, 0, 0) & 1))
                                                    {
                                                        if (a1)
                                                        {
                                                            v33 = a1 + 28;
                                                            goto LABEL_102bfdc;
                                                        }
                                                    }
                                                    else
                                                    {
                                                        if (ptr->field_10)
                                                        {
                                                            v33 = ptr->field_10 + 96;
LABEL_102bfdc:
                                                            if (idx4->field_68)
                                                            {
                                                                idx4->field_68->field_20 = v33[0];
                                                                sub_f7d8d0();
                                                                return;
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    v19 = sub_f7db74();
LABEL_102c000:
    sub_f7db7c(v19);
}
```

## `GamepadManager.Gamepad.Update` — RVA `0xc2c1fc`

- Decompiled symbol: `GamepadManager_Gamepad_Update`
- Metadata signature: `public void Update() { }`
- Native interval: `264` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_Recovered` matched 7 offsets against `GamepadManager.Gamepad` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Gamepad_Recovered {
    char padding_0[33];
    char isConnected;
    char padding_22[22];
    struct GamepadManager_Gamepad_Recovered *leftStick;
    struct GamepadManager_Gamepad_Recovered *rightStick;
    struct GamepadManager_Gamepad_Recovered *dpad;
    struct struct_0 *keys;
    struct struct_1 *internalAxes;
    struct struct_2 *internalKeys;
} GamepadManager_Gamepad_Recovered;

typedef struct struct_4 {
    char padding_0[24];
    unsigned int field_18;
} struct_4;

typedef struct struct_5 {
    char padding_0[24];
    unsigned int field_18;
} struct_5;

typedef struct struct_6 {
    char padding_0[24];
    unsigned int field_18;
} struct_6;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

typedef struct struct_2 {
    char padding_0[24];
    int field_18;
} struct_2;

struct_3 * GamepadManager_Gamepad_Update(struct_3 *ptr, unsigned long a1)
{
    struct_4 *v0;  // x8
    struct_3 *i;  // x0
    struct_3 *v11;  // x0
    struct_3 *v12;  // x0
    struct_3 *v13;  // x0
    struct_3 *v14;  // x0
    struct_6 *v15;  // x8
    unsigned long long v16;  // x20
    struct_3 *v17;  // x0
    unsigned long v18;  // x0
    unsigned long long v2;  // x20
    struct_3 *v3;  // x0
    struct_3 *v4;  // x0
    struct_3 *v5;  // x0
    struct_3 *v6;  // x0
    struct_5 *v7;  // x8
    unsigned long long v8;  // x20

    if (ptr->field_21)
    {
        v0 = ptr->field_60;
        i = ptr;
        if (!i->field_60)
            goto LABEL_102c2f0;
        v2 = 0;
        v3 = ptr;
        while (true)
        {
            v4 = v3;
            if (v0->field_18 <= (unsigned int)v2)
                break;
            if (v0->field_18 <= (unsigned int)v2)
            {
LABEL_102c300:
                sub_f7db7c();
            }
            v5 = *((long long *)&v0[1].padding_0[4 + 8 * v2]);
            if (!v5)
                goto LABEL_102c2f0;
            v6 = GamepadManager_Gamepad_InternalKeyState__Update(v5);
            v0 = ptr->field_60;
            v2 += 1;
            i = v6;
            v3 = v6;
            goto LABEL_102c2f0;
        }
        v7 = ptr->field_58;
        i = v4;
        if (ptr->field_58)
        {
            for (v8 = 0; v7->field_18 > (unsigned int)v8; i = *((long long *)&v7[1].padding_0[4 + 8 * v8]))
            {
                if (v7->field_18 <= (unsigned int)v8)
                    goto LABEL_102c300;
            }
            goto LABEL_102c290;
        }
    }
    else
    {
LABEL_102c290:
        v11 = ptr->field_38;
        i = v11;
        if (i && (GamepadManager_Gamepad_JoyState__Update(v11), v12 = (struct_3 *)ptr->field_40, i = v12, i && (GamepadManager_Gamepad_JoyState__Update(v12), v13 = (struct_3 *)ptr->field_48, i = v13, i && (v14 = (struct_3 *)(unsigned long long)GamepadManager_Gamepad_JoyState__Update(v13), v15 = (struct_6 *)ptr->field_50, i = v14, ptr->field_50))))
        {
            v16 = 0;
            do
            {
                if (v15->field_18 <= (unsigned int)v16)
                    return v14;
                if (v15->field_18 <= (unsigned int)v16)
                    goto LABEL_102c300;
            } while ((v17 = (struct_3 *)*((long long *)&v15[1].padding_0[4 + 8 * v16]), i = v17, i && (v14 = (struct_3 *)GamepadManager_Gamepad_KeyState__Update(v17), v15 = (struct_6 *)ptr->field_50, v16 += 1, i = v14, ptr->field_50)));
        }
    }
LABEL_102c2f0:
    v18 = sub_f7db74(i);
    return sub_f7db74(i);
}
```

## `GamepadManager.Gamepad.ApplyGamepadState` — RVA `0xc2c304`

- Decompiled symbol: `GamepadManager_Gamepad_ApplyGamepadState`
- Metadata signature: `public void ApplyGamepadState(GamepadManager.Gamepad g) { }`
- Native interval: `296` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_Recovered` matched 4 offsets against `GamepadManager.Gamepad` metadata (confidence 1.00).

```c
typedef struct struct_4 {
    char padding_0[56];
    struct struct_0 *field_38;
    struct struct_1 *field_40;
    struct struct_2 *field_48;
    struct struct_3 *field_50;
} struct_4;

typedef struct GamepadManager_Gamepad_Recovered {
    char padding_0[56];
    struct struct_5 *leftStick;
    struct struct_6 *rightStick;
    struct struct_7 *dpad;
    struct struct_8 *keys;
} GamepadManager_Gamepad_Recovered;

typedef struct struct_5 {
    char padding_0[24];
    long long field_18;
} struct_5;

typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

typedef struct struct_6 {
    char padding_0[24];
    long long field_18;
} struct_6;

typedef struct struct_1 {
    char padding_0[24];
    long long field_18;
} struct_1;

typedef struct struct_7 {
    char padding_0[24];
    long long field_18;
} struct_7;

typedef struct struct_2 {
    char padding_0[24];
    long long field_18;
} struct_2;

typedef struct struct_8 {
    char padding_0[24];
    int field_18;
} struct_8;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_11 {
    char padding_0[56];
    unsigned int field_38;
    char field_3c;
} struct_11;

typedef struct struct_10 {
    char padding_0[44];
    unsigned int field_2c;
    char field_30;
} struct_10;

void GamepadManager_Gamepad_ApplyGamepadState(struct_9 *p, struct_4 *addr)
{
    long long v0;  // x0
    struct_8 *ptr3;  // x8
    unsigned long v10;  // 4133
    unsigned int v11;  // s3
    unsigned long v12;  // 4133
    unsigned int v13;  // s2
    int i;  // w9
    struct_3 *v3;  // x10
    unsigned long long v4;  // x12
    unsigned long long v5;  // x12
    struct_11 *ptr4;  // x14
    struct_10 *ptr;  // x13
    unsigned int v8;  // s2
    unsigned int v9;  // s3

    if (!addr)
        return;
    if (p->field_38 && addr->field_38 && p->field_38->field_18 && !((JoystickState__ApplyState(p->field_38->field_18, addr->field_38->field_18, 0), !p->field_40 || !addr->field_40 || !p->field_40->field_18 || (JoystickState__ApplyState(p->field_40->field_18, addr->field_40->field_18, 0), !p->field_48 || !addr->field_48 || !p->field_48->field_18 || (v0 = (long long)(unsigned long long)JoystickState__ApplyState(p->field_48->field_18, addr->field_48->field_18, 0), ptr3 = (struct_8 *)p->field_50, !ptr3)))))
    {
        i = ptr3->field_18;
        if (i < 1)
            return;
        v3 = addr->field_50;
        v4 = 0;
        while (i > (unsigned int)v4)
        {
            if (!v3)
                goto LABEL_102c424;
            v5 = v4 * 0x100000000 >> 63 & 0xffffffff00000000 | v4 & 4294967295;
            if (v3->field_18 <= (unsigned int)v5)
                break;
            ptr4 = *((long long *)&v3[1].padding_0[4 + 8 * v5]);
            if (!ptr4 || !((ptr = (struct_10 *)*((long long *)&ptr3[1].padding_0[4 + 8 * v5]), ptr)))
                goto LABEL_102c424;
            if (ptr4->field_3c)
                ptr->field_30 = 1;
            v8 = ptr4->field_38;
            v9 = ptr->field_2c;
            v10 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v9, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v8) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v9, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v8) & 1)) & ((unsigned long long)(char)(CmpF(v9, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v9, v8) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v10))
            {
                v11 = [D] unsupported_Iop_ZeroHI96ofV128();
                v12 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v8, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v8, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v8, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v12)
                    v13 = v11;
                else
                    v13 = 0;
                ptr->field_2c = v13;
            }
            if ((unsigned int)v5 + 1 >= i)
                return;
        }
        goto LABEL_102c428;
    }
LABEL_102c424:
    v0 = sub_f7db74();
LABEL_102c428:
    sub_f7db7c(v0);
}
```

## `GamepadManager.Gamepad.OnActivate` — RVA `0xc2cd54`

- Decompiled symbol: `GamepadManager_Gamepad_OnActivate`
- Metadata signature: `public void OnActivate(int slot) { }`
- Native interval: `16` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_Recovered` matched 2 offsets against `GamepadManager.Gamepad` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Gamepad_Recovered {
    char padding_0[32];
    char isActivated;
    char padding_21[19];
    unsigned int slot;
} GamepadManager_Gamepad_Recovered;

long long GamepadManager_Gamepad_OnActivate(struct_0 *ptr, unsigned int a1)
{
    unsigned long v0;  // x0

    ptr->field_34 = a1;
    ptr->field_20 = 1;
    v0 = GamepadManager_Gamepad__Reset();
    return GamepadManager_Gamepad__Reset();
}
```

## `GamepadManager.Gamepad.OnDisactivate` — RVA `0xc2cf04`

- Decompiled symbol: `GamepadManager_Gamepad_OnDisactivate`
- Metadata signature: `public void OnDisactivate() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

long long GamepadManager_Gamepad_OnDisactivate(struct_0 *ptr)
{
    unsigned long v0;  // x0

    ptr->field_20 = 0;
    v0 = GamepadManager_Gamepad__Reset();
    return GamepadManager_Gamepad__Reset();
}
```

## `GamepadManager.Gamepad.OnDisconnect` — RVA `0xc2cf0c`

- Decompiled symbol: `GamepadManager_Gamepad_OnDisconnect`
- Metadata signature: `public void OnDisconnect() { }`
- Native interval: `84` bytes
- Result: `pseudocode`

```c
extern char g_1fab11a;

long long GamepadManager_Gamepad_OnDisconnect(long long a0)
{
    unsigned long long v0;  // x0

    if (!(g_1fab11a & 1))
    {
        sub_f7d92c("MT");
        g_1fab11a = 1;
    }
    v0 = GamepadManager_Gamepad__ConnectToJoy(a0, 4294967295, g_1ef18f0->field_b8->field_0);
    return GamepadManager_Gamepad__ConnectToJoy(a0, 4294967295, g_1ef18f0->field_b8->field_0);
}
```

## `GamepadManager.Gamepad.ConnectToJoy` — RVA `0xc2cf60`

- Decompiled symbol: `GamepadManager_Gamepad_ConnectToJoy`
- Metadata signature: `public void ConnectToJoy(int internalJoyId, string joyName) { }`
- Native interval: `324` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_Recovered` matched 8 offsets against `GamepadManager.Gamepad` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Gamepad_Recovered {
    char padding_0[24];
    unsigned long long profile;
    char isActivated;
    char isConnected;
    char isBlocked;
    char padding_23[5];
    long long internalJoyName;
    unsigned int internalJoyId;
    char padding_34[36];
    void* internalAxes;
    struct struct_0 *internalKeys;
} GamepadManager_Gamepad_Recovered;

typedef struct struct_2 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned long long field_18;
    unsigned short field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

typedef struct struct_4 {
    char padding_0[16];
    unsigned int field_10;
    unsigned short field_14;
    char field_16;
} struct_4;

long long GamepadManager_Gamepad_ConnectToJoy(struct_1 *ptr, unsigned int a1, long long a2)
{
    struct_1 *p;  // x22
    unsigned long v1;  // x20
    unsigned long ptr3;  // x22
    struct_0 *ptr4;  // x8
    int v12;  // w9
    int v13;  // w10
    int v14;  // w10
    unsigned long v15;  // cc_dep1
    unsigned long v16;  // cc_dep2
    struct_4 *addr;  // x12
    unsigned long v19;  // 4112
    unsigned long v2;  // x0
    unsigned long v20;  // 4106
    unsigned long v21;  // 4112
    unsigned long v22;  // 4106
    unsigned int v23;  // w13
    unsigned long v24;  // x0
    struct_1 *ptr5;  // x0
    char v4;  // x9
    void* v5;  // x8
    unsigned int i;  // w21
    unsigned long v7;  // 4102
    struct_2 *ptr6;  // x22
    long long v9;  // x0

    ptr->field_18 = 0;
    p = &ptr->field_18;
    v1 = a1;
    sub_f7d8d0(p, 0);
    p->padding_0[8] = 0;
    *((unsigned long long *)&p->padding_0[0]) = 0;
    v2 = sub_f7d8d0(p, 0);
    p->padding_0[10] = 0;
    if (!((char)(v1 >> 31) & 1))
    {
        ptr->field_28 = a2;
        ptr5 = &ptr->field_28;
        *((unsigned int *)&ptr5->padding_0[8]) = v1;
        v2 = sub_f7d8d0(ptr5, a2);
        v4 = 1;
    }
    else
    {
        v4 = 0;
    }
    v5 = ptr->field_58;
    ptr->field_21 = v4;
    if (!v5)
        sub_f7db7c(sub_f7db74());
    i = 0;
    while ((int)v5[24] > i)
    {
        v7 = arm64g_calculate_condition(35, (unsigned long long)i, (unsigned long long)(unsigned int)(int)v5[24], 0);
        if ((char)v7)
            sub_f7db7c(v2);
        ptr6 = *((long long *)(32 + (char *)v5 + 8 * i));
        if (!ptr6)
            sub_f7db7c(sub_f7db74());
        v9 = GamepadManager__GetJoyAxisName(v1, i);
        ptr6->field_10 = v9;
        ptr3 = &ptr6->field_10;
        v2 = sub_f7d8d0(ptr3, v9);
        *((unsigned short *)(ptr3 + 16)) = 0;
        *((unsigned long *)(ptr3 + 8)) = 0;
        i += 1;
        if (!ptr->field_58)
            sub_f7db7c(sub_f7db74());
    }
    ptr4 = ptr->field_60;
    if (ptr4)
    {
        v12 = ptr4->field_18;
        if (v12 >= 1)
        {
            v13 = 0;
            do
            {
                v14 = v13;
                v15 = v14;
                v16 = v12;
                if (v12 <= v14)
                    sub_f7db7c(v2);
                if (!*((long long *)&ptr4[1].padding_0[4 + 8 * v14]))
                    sub_f7db7c(sub_f7db74());
                if (v14 < 20)
                {
                    v19 = arm64g_calculate_condition(51, v15, v16, 0);
                    v20 = arm64g_calculate_condition(51, ((char)v19 ? v1 & 4294967295 : 0x20000000), ((char)v19 ? 4 : 0), 0);
                    if (!((char)v20))
                        goto LABEL_102d072;
                    goto LABEL_102d071;
                }
                else
                {
                    v21 = arm64g_calculate_condition(51, v15, v16, 0);
                    v22 = arm64g_calculate_condition(48, ((char)v21 ? v1 & 4294967295 : 0x20000000), ((char)v21 ? 4 : 0), 0);
                    if ((char)v22)
                    {
LABEL_102d071:
                        v23 = 20 * (unsigned int)v1 + 350 + v14;
                    }
                    else
                    {
LABEL_102d072:
                        v23 = 0;
                    }
                }
            } while ((addr->field_14 = 0, addr->field_10 = v23, addr->field_16 = 0, v13 = (int)(v14 + 1), v13 < v12));
        }
        v24 = GamepadManager_Gamepad__Reset(ptr);
        return GamepadManager_Gamepad__Reset(ptr);
    }
    sub_f7db7c(sub_f7db74());
}
```

## `GamepadManager.Gamepad.SetProfile` — RVA `0xc2d0fc`

- Decompiled symbol: `GamepadManager_Gamepad_SetProfile`
- Metadata signature: `public void SetProfile(GamepadProfile profile) { }`
- Native interval: `304` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_Recovered` matched 5 offsets against `GamepadManager.Gamepad` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Gamepad_Recovered {
    char padding_0[24];
    long long profile;
    char padding_20[24];
    unsigned long long leftStick;
    unsigned long long rightStick;
    unsigned long long dpad;
    struct struct_0 *keys;
} GamepadManager_Gamepad_Recovered;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

typedef struct struct_3 {
    char padding_0[40];
    char field_28;
    char padding_29[3];
    unsigned int field_2c;
    char field_30;
    char padding_31[3];
    char field_34[11];
    char field_3b;
    char padding_3c[4];
    unsigned long long field_40;
    char field_48;
} struct_3;

typedef struct struct_2 {
    char padding_0[24];
    char field_18;
} struct_2;

long long GamepadManager_Gamepad_SetProfile(struct_1 *p, long long a1)
{
    struct_1 *v0;  // x21
    struct_0 *i;  // x8
    unsigned long long v2;  // x21
    struct_3 *ptr;  // x22
    struct_2 *pos;  // x0
    char v5;  // x8
    unsigned long v7;  // x0

    p->field_18 = a1;
    v0 = &p->field_18;
    sub_f7d8d0(v0);
    if (a1)
    {
        if (*((long long *)&v0->padding_20[0]))
            goto LABEL_102d13c;
    }
    else
    {
        if (*((long long *)&v0->padding_20[0]))
        {
LABEL_102d13c:
            GamepadManager_Gamepad_JoyState__ConnectToJoy();
            if (a1)
            {
                if (p->field_40)
                    goto LABEL_102d15c;
            }
            else
            {
                if (p->field_40)
                {
LABEL_102d15c:
                    GamepadManager_Gamepad_JoyState__ConnectToJoy();
                    if (a1)
                    {
                        if (p->field_48)
                            goto LABEL_102d17c;
                    }
                    else
                    {
                        if (p->field_48)
                        {
LABEL_102d17c:
                            GamepadManager_Gamepad_JoyState__ConnectToJoy();
                            i = p->field_50;
                            if (i)
                            {
                                v2 = 0;
                                do
                                {
                                    if (i->field_18 <= (unsigned int)v2)
                                    {
                                        v7 = GamepadManager_Gamepad__Reset(p);
                                        return GamepadManager_Gamepad__Reset(p);
                                    }
                                    if (i->field_18 <= (unsigned int)v2)
                                        sub_f7db7c();
                                    ptr = *((long long *)&i[1].padding_0[4 + 8 * v2]);
                                    if (a1)
                                    {
                                        pos = GamepadProfile__GetKeySource(a1, v2 & 4294967295);
                                        if (!ptr)
                                            break;
                                    }
                                    else
                                    {
                                        pos = NULL;
                                        if (!ptr)
                                            break;
                                    }
                                    if (!pos)
                                        v5 = 0;
                                    else
                                        v5 = 1;
                                    ptr->field_28 = v5;
                                    *((unsigned long long *)&ptr->padding_3c) = 18446744073709551615 CONCAT 18446744073709551615;
                                    if (pos)
                                    {
                                        *((long long *)&ptr->padding_3c) = [D] unsupported_Iop_ZeroHI64ofV128();
                                        *((char *)&ptr->field_40) = pos->field_18;
                                    }
                                    ptr->field_2c = 0;
                                    ptr->field_30 = 0;
                                    *((unsigned long *)&ptr->field_34[0]) = 0;
                                    *((unsigned int *)&ptr->field_34[7]) = 0;
                                    i = p->field_50;
                                    v2 += 1;
                                } while (i);
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74();
    v7 = GamepadManager_Gamepad__Reset(p);
    return GamepadManager_Gamepad__Reset(p);
}
```

## `GamepadManager.Gamepad.IsSupported` — RVA `0xc2d22c`

- Decompiled symbol: `GamepadManager_Gamepad_IsSupported`
- Metadata signature: `public bool IsSupported() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

unsigned long long GamepadManager_Gamepad_IsSupported(struct_0 *a0)
{
    if (a0->field_18)
        return 1;
    return 0;
}
```

## `GamepadManager.Gamepad.AnyInternalKeyOrAxisPressed` — RVA `0xc2d23c`

- Decompiled symbol: `GamepadManager_Gamepad_AnyInternalKeyOrAxisPressed`
- Metadata signature: `public bool AnyInternalKeyOrAxisPressed() { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
long long GamepadManager_Gamepad_AnyInternalKeyOrAxisPressed(long long a0)
{
    unsigned long v0;  // x0

    if (!((char)GamepadManager_Gamepad__AnyInternalKeyPressed() & 1))
    {
        v0 = GamepadManager_Gamepad__AnyInternalAxisPressed(a0);
        return GamepadManager_Gamepad__AnyInternalAxisPressed(a0);
    }
    return 1;
}
```

## `GamepadManager.Gamepad.IsConnected` — RVA `0xc2da80`

- Decompiled symbol: `GamepadManager_Gamepad_IsConnected`
- Metadata signature: `public bool IsConnected() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[33];
    char field_21;
} struct_0;

long long GamepadManager_Gamepad_IsConnected(struct_0 *a0)
{
    return a0->field_21;
}
```

## `GamepadManager.Gamepad.IsActivated` — RVA `0xc2da88`

- Decompiled symbol: `GamepadManager_Gamepad_IsActivated`
- Metadata signature: `public bool IsActivated() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

long long GamepadManager_Gamepad_IsActivated(struct_0 *a0)
{
    return a0->field_20;
}
```

## `GamepadManager.Gamepad.GetSlot` — RVA `0xc2da90`

- Decompiled symbol: `GamepadManager_Gamepad_GetSlot`
- Metadata signature: `public int GetSlot() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[52];
    unsigned int field_34;
} struct_0;

int GamepadManager_Gamepad_GetSlot(struct_0 *a0)
{
    return a0->field_34;
}
```

## `GamepadManager.Gamepad.GetInternalJoyName` — RVA `0xc2da98`

- Decompiled symbol: `GamepadManager_Gamepad_GetInternalJoyName`
- Metadata signature: `public string GetInternalJoyName() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned long long field_28;
} struct_0;

long long GamepadManager_Gamepad_GetInternalJoyName(struct_0 *a0)
{
    return a0->field_28;
}
```

## `GamepadManager.Gamepad.GetInternalJoyId` — RVA `0xc2daa0`

- Decompiled symbol: `GamepadManager_Gamepad_GetInternalJoyId`
- Metadata signature: `public int GetInternalJoyId() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    unsigned int field_30;
} struct_0;

int GamepadManager_Gamepad_GetInternalJoyId(struct_0 *a0)
{
    return a0->field_30;
}
```

## `GamepadManager.Gamepad.GetProfileName` — RVA `0xc2daa8`

- Decompiled symbol: `GamepadManager_Gamepad_GetProfileName`
- Metadata signature: `public string GetProfileName() { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[24];
    struct struct_1 *field_18;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    unsigned long long field_10;
} struct_1;

extern char g_1fab118;

long long GamepadManager_Gamepad_GetProfileName(struct_2 *ptr)
{
    unsigned long v0;  // x8

    if (!(g_1fab118 & 1))
    {
        sub_f7d92c("MT");
        g_1fab118 = 1;
    }
    if (ptr->field_18)
        v0 = &ptr->field_18->field_10;
    else
        v0 = g_1ef18f0->field_b8;
    return *((long long *)v0);
}
```

## `GamepadManager.Gamepad.Block` — RVA `0xc2db04`

- Decompiled symbol: `GamepadManager_Gamepad_Block`
- Metadata signature: `public void Block(bool block) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[34];
    char field_22;
} struct_0;

struct_0 * GamepadManager_Gamepad_Block(struct_0 *ptr, char a1)
{
    ptr->field_22 = a1 & 1;
    return ptr;
}
```

## `GamepadManager.Gamepad.IsBlocked` — RVA `0xc2db10`

- Decompiled symbol: `GamepadManager_Gamepad_IsBlocked`
- Metadata signature: `public bool IsBlocked() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[34];
    char field_22;
} struct_0;

long long GamepadManager_Gamepad_IsBlocked(struct_0 *a0)
{
    return a0->field_22;
}
```

## `GamepadManager.Gamepad.Reset` — RVA `0xc2db9c`

- Decompiled symbol: `GamepadManager_Gamepad_Reset`
- Metadata signature: `public void Reset() { }`
- Native interval: `296` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadManager_Gamepad_Recovered` matched 6 offsets against `GamepadManager.Gamepad` metadata (confidence 1.00).

```c
typedef struct GamepadManager_Gamepad_Recovered {
    char padding_0[56];
    struct struct_0 *leftStick;
    struct struct_1 *rightStick;
    struct struct_2 *dpad;
    struct struct_3 *keys;
    struct struct_4 *internalAxes;
    struct struct_5 *internalKeys;
} GamepadManager_Gamepad_Recovered;

typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    long long field_18;
} struct_1;

typedef struct struct_2 {
    char padding_0[24];
    long long field_18;
} struct_2;

typedef struct struct_3 {
    char padding_0[24];
    int field_18;
} struct_3;

typedef struct struct_8 {
    char padding_0[44];
    unsigned int field_2c;
    char field_30;
    char padding_31[3];
    char field_34[11];
    char field_3b;
} struct_8;

typedef struct struct_4 {
    char padding_0[24];
    int field_18;
} struct_4;

typedef struct struct_10 {
    char padding_0[24];
    unsigned long long field_18;
    unsigned short field_20;
} struct_10;

typedef struct struct_5 {
    char padding_0[24];
    int field_18;
} struct_5;

typedef struct struct_9 {
    char padding_0[20];
    unsigned short field_14;
    char field_16;
} struct_9;

void GamepadManager_Gamepad_Reset(struct_6 *ptr)
{
    long long v0;  // x0
    struct_3 *v1;  // x9
    int v10;  // w9
    int v11;  // w10
    struct_9 *addr;  // x11
    int v2;  // w8
    unsigned long v3;  // 4102
    struct_8 *p;  // x9
    struct_4 *v5;  // x9
    int v6;  // w8
    unsigned long v7;  // 4102
    struct_10 *ptr3;  // x9
    struct_5 *ptr4;  // x8

    if (ptr->field_38 && ptr->field_38->field_18)
    {
        JoystickState__Reset(ptr->field_38->field_18, 0);
        if (ptr->field_40 && ptr->field_40->field_18)
        {
            JoystickState__Reset(ptr->field_40->field_18, 0);
            if (ptr->field_48 && ptr->field_48->field_18)
            {
                v0 = JoystickState__Reset(ptr->field_48->field_18, 0);
                v1 = ptr->field_50;
                if (v1)
                {
                    v2 = 0;
                    do
                    {
                        if (v1->field_18 > v2)
                        {
                            v3 = arm64g_calculate_condition(35, (unsigned long long)(unsigned int)v2, (unsigned long long)(unsigned int)v1->field_18, 0);
                            if ((char)v3)
                                sub_f7db7c(v0);
                            p = *((long long *)&v1[1].padding_0[4 + 8 * v2]);
                            if (!p)
                                break;
                        }
                        else
                        {
                            v5 = ptr->field_58;
                            if (v5)
                            {
                                v6 = 0;
                                do
                                {
                                    if (v5->field_18 <= v6)
                                    {
                                        ptr4 = ptr->field_60;
                                        if (ptr4)
                                        {
                                            v10 = ptr4->field_18;
                                            if (v10 < 1)
                                                return;
                                            v11 = 0;
                                            while (true)
                                            {
                                                if (v10 <= v11)
                                                    sub_f7db7c(v0);
                                                addr = *((long long *)&ptr4[1].padding_0[4 + 8 * v11]);
                                                if (!addr)
                                                    break;
                                                v11 += 1;
                                                addr->field_14 = 0;
                                                addr->field_16 = 0;
                                                if (v11 >= v10)
                                                    return;
                                            }
                                        }
                                    }
                                    v7 = arm64g_calculate_condition(35, (unsigned long long)(unsigned int)v6, (unsigned long long)(unsigned int)v5->field_18, 0);
                                    if ((char)v7)
                                        sub_f7db7c(v0);
                                    ptr3 = *((long long *)&v5[1].padding_0[4 + 8 * v6]);
                                } while (ptr3 && (ptr3->field_20 = 0, ptr3->field_18 = (unsigned long long)0, v5 = (struct_4 *)ptr->field_58, v6 = (int)(v6 + 1), v5));
                            }
                        }
                        p->field_2c = 0;
                        p->field_30 = 0;
                        *((unsigned long *)&p->field_34[0]) = 0;
                        *((unsigned int *)&p->field_34[7]) = 0;
                        v1 = ptr->field_50;
                        v2 += 1;
                    } while (ptr->field_50);
                }
            }
        }
    }
    sub_f7db7c(sub_f7db74());
}
```

## `GamepadManager.Gamepad.GetProfile` — RVA `0xc2dcc4`

- Decompiled symbol: `GamepadManager_Gamepad_GetProfile`
- Metadata signature: `public GamepadProfile GetProfile() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GamepadManager_Gamepad_GetProfile(struct_0 *a0)
{
    return a0->field_18;
}
```

## `GamepadManager.Gamepad.GetKey` — RVA `0xc2dea0`

- Decompiled symbol: `GamepadManager_Gamepad_GetKey`
- Metadata signature: `public bool GetKey(GamepadManager.GamepadKey key) { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[80];
    struct struct_0 *field_50;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

long long GamepadManager_Gamepad_GetKey(struct_1 *ptr, unsigned int a1)
{
    struct_0 *v0;  // x8

    v0 = ptr->field_50;
    if (v0)
    {
        if (v0->field_18 <= a1)
        {
            sub_f7db7c(ptr);
        }
        else if (*((long long *)&v0[1].padding_0[4 + 8 * a1]))
        {
            return *((char *)(*((long long *)&v0[1].padding_0[4 + 8 * a1]) + 61));
        }
    }
    ptr = sub_f7db74();
    sub_f7db7c(ptr);
}
```

## `GamepadManager.Gamepad.GetKeyDown` — RVA `0xc2ded8`

- Decompiled symbol: `GamepadManager_Gamepad_GetKeyDown`
- Metadata signature: `public bool GetKeyDown(GamepadManager.GamepadKey key) { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[80];
    struct struct_0 *field_50;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

unsigned long long GamepadManager_Gamepad_GetKeyDown(struct_1 *ptr, unsigned int a1)
{
    struct_0 *v0;  // x8
    char v1[63];  // x8
    unsigned long long v2;  // x0

    v0 = ptr->field_50;
    if (v0)
    {
        if (v0->field_18 > a1)
        {
            v1 = *((long long *)&v0[1].padding_0[4 + 8 * a1]);
            if (v1)
            {
                if (v1[61])
                {
                    if (v1[62])
                        v2 = 0;
                    else
                        v2 = 1;
                    return v2;
                }
                else
                {
                    return 0;
                }
            }
        }
        else
        {
            sub_f7db7c(ptr);
        }
    }
    ptr = sub_f7db74();
    sub_f7db7c(ptr);
}
```

## `GamepadManager.Gamepad.GetKeyUp` — RVA `0xc2df48`

- Decompiled symbol: `GamepadManager_Gamepad_GetKeyUp`
- Metadata signature: `public bool GetKeyUp(GamepadManager.GamepadKey key) { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[80];
    struct struct_0 *field_50;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

unsigned long long GamepadManager_Gamepad_GetKeyUp(struct_1 *ptr, unsigned int a1)
{
    struct_0 *v0;  // x8
    char v1[63];  // x8

    v0 = ptr->field_50;
    if (v0)
    {
        if (v0->field_18 > a1)
        {
            v1 = *((long long *)&v0[1].padding_0[4 + 8 * a1]);
            if (v1)
            {
                if (v1[61])
                {
                    return 0;
                }
                else if (!v1[62])
                {
                    return 0;
                }
                else
                {
                    return 1;
                }
            }
        }
        else
        {
            sub_f7db7c(ptr);
        }
    }
    ptr = sub_f7db74();
    sub_f7db7c(ptr);
}
```

## `GamepadManager.Gamepad.GetKeyAnalog` — RVA `0xc2dfb8`

- Decompiled symbol: `GamepadManager_Gamepad_GetKeyAnalog`
- Metadata signature: `public float GetKeyAnalog(GamepadManager.GamepadKey key) { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[80];
    struct struct_0 *field_50;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

void GamepadManager_Gamepad_GetKeyAnalog(struct_1 *ptr, unsigned int a1)
{
    struct_0 *v0;  // x8

    v0 = ptr->field_50;
    if (v0)
    {
        if (v0->field_18 <= a1)
        {
            sub_f7db7c(ptr);
        }
        else if (*((long long *)&v0[1].padding_0[4 + 8 * a1]))
        {
            return;
        }
    }
    ptr = sub_f7db74();
    sub_f7db7c(ptr);
}
```

## `GamepadManager.Gamepad.GetStickVec` — RVA `0xc2dff0`

- Decompiled symbol: `GamepadManager_Gamepad_GetStickVec`
- Metadata signature: `public Vector2 GetStickVec(GamepadManager.GamepadStick s) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
void GamepadManager_Gamepad_GetStickVec(unsigned long a0, unsigned long a1)
{
    if (GamepadManager_Gamepad__GetStick())
        return;
    sub_f7db74();
}
```

## `GamepadManager.Gamepad.GetStick` — RVA `0xc2e00c`

- Decompiled symbol: `GamepadManager_Gamepad_GetStick`
- Metadata signature: `public JoystickState GetStick(GamepadManager.GamepadStick s) { }`
- Native interval: `60` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    unsigned long long field_18;
} struct_1;

long long GamepadManager_Gamepad_GetStick(struct_0 **ptr, unsigned int flag)
{
    if (flag != 1)
    {
        if (!flag)
        {
            if (ptr[7])
                return ptr[7]->field_18;
        }
        else
        {
            if (ptr[9])
                return ptr[9]->field_18;
        }
    }
    do
    {
        ptr = sub_f7db74();
    } while (!ptr[8]);
    return ptr[8]->field_18;
}
```

## `GamepadManager.Gamepad.GetStickDir8` — RVA `0xc2e048`

- Decompiled symbol: `GamepadManager_Gamepad_GetStickDir8`
- Metadata signature: `public Dir GetStickDir8(GamepadManager.GamepadStick s) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GamepadManager_Gamepad_GetStickDir8(void)
{
    struct_0 **v0;  // x0
    unsigned int v1;  // w1
    unsigned long long v2;  // x0

    if (GamepadManager_Gamepad__GetStick(v0, v1))
    {
        v2 = JoystickState__GetDir8();
        return JoystickState__GetDir8();
    }
    sub_f7db74();
}
```

## `GamepadManager.Gamepad.GetStickDir4` — RVA `0xc2e064`

- Decompiled symbol: `GamepadManager_Gamepad_GetStickDir4`
- Metadata signature: `public Dir GetStickDir4(GamepadManager.GamepadStick s) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GamepadManager_Gamepad_GetStickDir4(void)
{
    struct_0 **v0;  // x0
    unsigned int v1;  // w1
    unsigned long long v2;  // x0

    if (GamepadManager_Gamepad__GetStick(v0, v1))
    {
        v2 = JoystickState__GetDir4();
        return JoystickState__GetDir4();
    }
    sub_f7db74();
}
```

## `GamepadManager.Gamepad.GetStickDir` — RVA `0xc2e080`

- Decompiled symbol: `GamepadManager_Gamepad_GetStickDir`
- Metadata signature: `public Dir GetStickDir(GamepadManager.GamepadStick s) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GamepadManager_Gamepad_GetStickDir(void)
{
    struct_0 **v0;  // x0
    unsigned int v1;  // w1
    unsigned long long v2;  // x0

    if (GamepadManager_Gamepad__GetStick(v0, v1))
    {
        v2 = JoystickState__GetDir();
        return JoystickState__GetDir();
    }
    sub_f7db74();
}
```

## `GamepadManager.Gamepad.GetInternalKeyState` — RVA `0xc2e09c`

- Decompiled symbol: `GamepadManager_Gamepad_GetInternalKeyState`
- Metadata signature: `public bool GetInternalKeyState(int keyId) { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[96];
    unsigned long long field_60;
} struct_0;

unsigned long long GamepadManager_Gamepad_GetInternalKeyState(struct_0 *ptr, unsigned long long a1)
{
    unsigned long long v0;  // x8
    unsigned long v1;  // 4102
    char v2[23];  // x8
    unsigned long long v3;  // x0

    if (((char)(a1 >> 31) & 1))
        return 0;
    v0 = ptr->field_60;
    if (!v0)
    {
        ptr = sub_f7db74();
        sub_f7db7c(ptr);
    }
    else if (*((int *)(v0 + 24)) > (unsigned int)a1)
    {
        v1 = arm64g_calculate_condition(147, (unsigned long long)(unsigned int)*((int *)(v0 + 24)), a1 & 4294967295, 0);
        if ((char)v1)
            sub_f7db7c(ptr);
        v2 = *((long long *)(v0 + (a1 & 4294967295) * 8 + 32));
        if (!v2)
        {
            sub_f7db74();
            sub_f7db7c(ptr);
        }
        else if (v2[22])
        {
            if (!v2[20])
                v3 = 0;
            else
                v3 = 1;
            return v3;
        }
    }
    return 0;
}
```

## `GamepadManager.Gamepad.GetInternalAxisAnalog` — RVA `0xc2e114`

- Decompiled symbol: `GamepadManager_Gamepad_GetInternalAxisAnalog`
- Metadata signature: `public float GetInternalAxisAnalog(int axisId) { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[88];
    unsigned long long field_58;
} struct_0;

void GamepadManager_Gamepad_GetInternalAxisAnalog(struct_0 *ptr, unsigned long long a1)
{
    unsigned long long v0;  // x8
    unsigned long v1;  // 4102

    if (((char)(a1 >> 31) & 1))
        return;
    v0 = ptr->field_58;
    if (v0)
    {
        if (*((int *)(v0 + 24)) > (unsigned int)a1)
        {
            v1 = arm64g_calculate_condition(147, (unsigned long long)(unsigned int)*((int *)(v0 + 24)), a1 & 4294967295, 0);
            if ((char)v1)
            {
                sub_f7db7c(ptr);
            }
            else if (*((long long *)(v0 + (a1 & 4294967295) * 8 + 32)))
            {
                return;
            }
        }
        else
        {
            return;
        }
    }
    ptr = sub_f7db74();
    sub_f7db7c(ptr);
}
```

## `GamepadManager.Gamepad.GetInternalAxisDigital` — RVA `0xc2e178`

- Decompiled symbol: `GamepadManager_Gamepad_GetInternalAxisDigital`
- Metadata signature: `public int GetInternalAxisDigital(int axisId) { }`
- Native interval: `116` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x102e178: str x30, [sp, #-0x10]!
// 0x102e17c: tbnz w1, #0x1f, #0x102e1d0
// 0x102e180: ldr x8, [x0, #0x58]
// 0x102e184: cbz x8, #0x102e1e4
// 0x102e188: ldr w9, [x8, #0x18]
// 0x102e18c: cmp w9, w1
// 0x102e190: b.le #0x102e1d0
// 0x102e194: b.ls #0x102e1e8
// 0x102e198: add x8, x8, w1, uxtw #3
// 0x102e19c: ldr x8, [x8, #0x20]
// 0x102e1a0: cbz x8, #0x102e1e4
// 0x102e1a4: ldrb w9, [x8, #0x20]
// 0x102e1a8: cbz w9, #0x102e1d0
// 0x102e1ac: ldr s0, [x8, #0x18]
// 0x102e1b0: fmov s2, #0.50000000
// 0x102e1b4: fabs s1, s0
// 0x102e1b8: fcmp s1, s2
// 0x102e1bc: b.le #0x102e1d0
// 0x102e1c0: fcmp s0, #0.0
// 0x102e1c4: b.le #0x102e1dc
// 0x102e1c8: mov w0, #1
// 0x102e1cc: b #0x102e1d4
// 0x102e1d0: mov w0, wzr
// 0x102e1d4: ldr x30, [sp], #0x10
// 0x102e1d8: ret
// 0x102e1dc: mov w0, #-1
// 0x102e1e0: b #0x102e1d4
// 0x102e1e4: bl #0xf7db74
// 0x102e1e8: bl #0xf7db7c
```

## `GamepadManager.Gamepad.IsInternalAxisFullyAnalog` — RVA `0xc2e228`

- Decompiled symbol: `GamepadManager_Gamepad_IsInternalAxisFullyAnalog`
- Metadata signature: `public bool IsInternalAxisFullyAnalog(int axisId) { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[88];
    unsigned long long field_58;
} struct_0;

unsigned long long GamepadManager_Gamepad_IsInternalAxisFullyAnalog(struct_0 *ptr, unsigned long long a1)
{
    unsigned long long v0;  // x8
    unsigned long v1;  // 4102
    unsigned long long v2;  // x0

    if (((char)(a1 >> 31) & 1))
        return 0;
    v0 = ptr->field_58;
    if (v0)
    {
        if (*((int *)(v0 + 24)) > (unsigned int)a1)
        {
            v1 = arm64g_calculate_condition(147, (unsigned long long)(unsigned int)*((int *)(v0 + 24)), a1 & 4294967295, 0);
            if ((char)v1)
            {
                sub_f7db7c(ptr);
            }
            else if (*((long long *)(v0 + (a1 & 4294967295) * 8 + 32)))
            {
                if (!*((char *)(*((long long *)(v0 + (a1 & 4294967295) * 8 + 32)) + 33)))
                    v2 = 0;
                else
                    v2 = 1;
                return v2;
            }
        }
        else
        {
            return 0;
        }
    }
    ptr = sub_f7db74();
    sub_f7db7c(ptr);
}
```

## `GamepadManager.Gamepad.AnyInternalKeyPressed` — RVA `0xc2e278`

- Decompiled symbol: `GamepadManager_Gamepad_AnyInternalKeyPressed`
- Metadata signature: `public bool AnyInternalKeyPressed() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[96];
    struct struct_0 *field_60;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

unsigned int GamepadManager_Gamepad_AnyInternalKeyPressed(struct_1 *ptr)
{
    struct_0 *p;  // x8
    int v1;  // w9
    unsigned int v2;  // w10
    int v3;  // w11
    char v4[23];  // x12
    unsigned long v5;  // cc_dep1
    unsigned long v6;  // cc_dep2
    unsigned long v7;  // 4102
    unsigned long v8;  // 4102

    p = ptr->field_60;
    if (!p)
        sub_f7db74();
    v1 = p->field_18;
    if (v1 <= 0)
        v2 = 0;
    else
        v2 = 1;
    if (v1 < 1)
        return v2 & 1;
    v3 = 0;
    while (true)
    {
        if (v1 <= v3)
        {
            sub_f7db7c();
            sub_f7db74();
        }
        v4 = *((long long *)&p[1].padding_0[4 + 8 * v3]);
        if (!v4)
            sub_f7db74();
        if (v4[22] && v4[20])
            return v2 & 1;
        v3 += 1;
        v5 = v3;
        v6 = v1;
        if (v1 <= v3)
        {
            v2 = 0;
            v7 = arm64g_calculate_condition(179, v5, v6, 0);
            if (!((char)v7))
                return 0;
        }
        else
        {
            v2 = 1;
            v8 = arm64g_calculate_condition(179, v5, v6, 0);
            if (!((char)v8))
                return 1;
        }
    }
}
```

## `GamepadManager.Gamepad.AnyInternalAxisPressed` — RVA `0xc2e2e4`

- Decompiled symbol: `GamepadManager_Gamepad_AnyInternalAxisPressed`
- Metadata signature: `public bool AnyInternalAxisPressed() { }`
- Native interval: `120` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x102e2e4: str x30, [sp, #-0x10]!
// 0x102e2e8: ldr x8, [x0, #0x58]
// 0x102e2ec: cbz x8, #0x102e358
// 0x102e2f0: ldr w9, [x8, #0x18]
// 0x102e2f4: cmp w9, #0
// 0x102e2f8: cset w10, gt
// 0x102e2fc: cmp w9, #1
// 0x102e300: b.lt #0x102e348
// 0x102e304: mov w11, wzr
// 0x102e308: fmov s0, #0.50000000
// 0x102e30c: cmp w11, w9
// 0x102e310: b.hs #0x102e354
// 0x102e314: add x12, x8, w11, sxtw #3
// 0x102e318: ldr x12, [x12, #0x20]
// 0x102e31c: cbz x12, #0x102e358
// 0x102e320: ldrb w13, [x12, #0x20]
// 0x102e324: cbz w13, #0x102e338
// 0x102e328: ldr s1, [x12, #0x18]
// 0x102e32c: fabs s1, s1
// 0x102e330: fcmp s1, s0
// 0x102e334: b.gt #0x102e348
// 0x102e338: add w11, w11, #1
// 0x102e33c: cmp w11, w9
// 0x102e340: cset w10, lt
// 0x102e344: b.lt #0x102e30c
// 0x102e348: and w0, w10, #1
// 0x102e34c: ldr x30, [sp], #0x10
// 0x102e350: ret
// 0x102e354: bl #0xf7db7c
// 0x102e358: bl #0xf7db74
```

## `GamepadManager.Gamepad.GetPressedInternalKey` — RVA `0xc2e35c`

- Decompiled symbol: `GamepadManager_Gamepad_GetPressedInternalKey`
- Metadata signature: `public int GetPressedInternalKey(int start = 0) { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[96];
    struct struct_0 *field_60;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

typedef struct struct_2 {
    char padding_0[32];
    struct struct_3 *field_20;
} struct_2;

typedef struct struct_3 {
    char padding_0[20];
    char field_14;
    char padding_15[1];
    char field_16;
} struct_3;

int GamepadManager_Gamepad_GetPressedInternalKey(struct_1 *ptr, int i)
{
    struct_0 *p;  // x9
    int v1;  // w8
    struct_2 *cur;  // x9
    char v3[23];  // x10

    p = ptr->field_60;
    if (p)
    {
        v1 = p->field_18;
        if (v1 <= i)
            return -1;
        cur = &p->padding_0[8 * i + 32];
        do
        {
            if (v1 <= i)
            {
                sub_f7db7c();
                sub_f7db74();
            }
            v3 = *((long long *)&cur->padding_0[0]);
            if (!v3)
                sub_f7db74();
            if (v3[22] && v3[20])
                return i;
            i += 1;
            cur = &cur->padding_0[8];
        } while (i < v1);
        return -1;
    }
    sub_f7db74();
}
```

## `GamepadManager.Gamepad.GetPressedInternalAxis` — RVA `0xc2e3c4`

- Decompiled symbol: `GamepadManager_Gamepad_GetPressedInternalAxis`
- Metadata signature: `public int GetPressedInternalAxis(out bool positiveSide, int start = 0) { }`
- Native interval: `128` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x102e3c4: str x30, [sp, #-0x10]!
// 0x102e3c8: ldr x8, [x0, #0x58]
// 0x102e3cc: cbz x8, #0x102e440
// 0x102e3d0: ldr w9, [x8, #0x18]
// 0x102e3d4: cmp w9, w2
// 0x102e3d8: b.le #0x102e418
// 0x102e3dc: fmov s0, #0.50000000
// 0x102e3e0: cmp w2, w9
// 0x102e3e4: b.hs #0x102e43c
// 0x102e3e8: add x10, x8, w2, sxtw #3
// 0x102e3ec: ldr x10, [x10, #0x20]
// 0x102e3f0: cbz x10, #0x102e440
// 0x102e3f4: ldrb w11, [x10, #0x20]
// 0x102e3f8: cbz w11, #0x102e40c
// 0x102e3fc: ldr s1, [x10, #0x18]
// 0x102e400: fabs s2, s1
// 0x102e404: fcmp s2, s0
// 0x102e408: b.gt #0x102e430
// 0x102e40c: add w2, w2, #1
// 0x102e410: cmp w2, w9
// 0x102e414: b.lt #0x102e3e0
// 0x102e418: mov w8, wzr
// 0x102e41c: mov w2, #-1
// 0x102e420: strb w8, [x1]
// 0x102e424: mov w0, w2
// 0x102e428: ldr x30, [sp], #0x10
// 0x102e42c: ret
// 0x102e430: fcmp s1, #0.0
// 0x102e434: cset w8, gt
// 0x102e438: b #0x102e420
// 0x102e43c: bl #0xf7db7c
// 0x102e440: bl #0xf7db74
```
