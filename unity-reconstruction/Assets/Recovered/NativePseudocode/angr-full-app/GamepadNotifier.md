# Native pseudocode: GamepadNotifier

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GamepadNotifier.ctor` — RVA `0xc2ea4c`

- Decompiled symbol: `GamepadNotifier_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `348` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadNotifier_Recovered` matched 7 offsets against `GamepadNotifier` metadata (confidence 1.00).

```c
typedef struct GamepadNotifier_Recovered {
    char padding_0[32];
    unsigned long long maxNotifications;
    char padding_28[16];
    long long notificationList;
    long long msgUnknownGamepadConnected;
    long long msgKnownGamepadConnected;
    long long msgGamepadDisconnected;
    long long msgGamepadActivated;
    long long msgGamepadDisactivated;
} GamepadNotifier_Recovered;

extern long long g_1eed760;
extern long long g_1ef81a0;
extern long long g_1f0a670;
extern long long g_1f0a678;
extern long long g_1f0a680;
extern long long g_1f0a688;
extern long long g_1f0f620;
extern char g_1fab11d;

void GamepadNotifier_ctor(struct_0 *ptr)
{
    unsigned long long v10;  // x30
    unsigned long long v11;  // x27
    struct_0 *p;  // x0
    struct_0 *addr;  // x0
    struct_0 *ptr3;  // x0
    struct_0 *ptr4;  // x0
    struct_0 *ptr5;  // x0
    long long v25;  // x0
    unsigned long long v12;  // x26
    unsigned long long v13;  // x25
    unsigned long long v14;  // x24
    unsigned long long v15;  // x23
    unsigned long long v16;  // x22
    unsigned long long v17;  // x21
    unsigned long long v18;  // x20
    unsigned long long v19;  // x19
    unsigned long long v0;  // [bp-0x50]
    unsigned long long v1;  // [bp-0x48]
    unsigned long long v2;  // [bp-0x40]
    unsigned long long v3;  // [bp-0x38]
    unsigned long long v4;  // [bp-0x30]
    unsigned long long v5;  // [bp-0x28]
    unsigned long long v6;  // [bp-0x20]
    unsigned long long v7;  // [bp-0x18]
    unsigned long long v8;  // [bp-0x10]
    unsigned long long v9;  // [bp-0x8]

    v0 = v10;
    v1 = v11;
    v2 = v12;
    v3 = v13;
    v4 = v14;
    v5 = v15;
    v6 = v16;
    v7 = v17;
    v8 = v18;
    v9 = v19;
    if (!(g_1fab11d & 1))
    {
        sub_f7d92c(&g_1ef81a0);
        sub_f7d92c(&g_1eed760);
        sub_f7d92c(&g_1f0a670);
        sub_f7d92c(&g_1f0a678);
        sub_f7d92c(&g_1f0a688);
        sub_f7d92c(&g_1f0f620);
        sub_f7d92c(&g_1f0a680);
        g_1fab11d = 1;
    }
    ptr->field_20 = 4656722014701092872;
    p = ptr;
    p->field_40 = g_1f0f620;
    sub_f7d8d0((struct GamepadNotifier_Recovered *)&p->field_40, g_1f0f620);
    addr = ptr;
    addr->field_48 = g_1f0a688;
    sub_f7d8d0((struct GamepadNotifier_Recovered *)&addr->field_48, g_1f0a688);
    ptr3 = ptr;
    ptr3->field_50 = g_1f0a678;
    sub_f7d8d0((struct GamepadNotifier_Recovered *)&ptr3->field_50, g_1f0a678);
    ptr4 = ptr;
    ptr4->field_58 = g_1f0a670;
    sub_f7d8d0((struct GamepadNotifier_Recovered *)&ptr4->field_58, g_1f0a670);
    ptr5 = ptr;
    ptr5->field_60 = g_1f0a680;
    sub_f7d8d0((struct GamepadNotifier_Recovered *)&ptr5->field_60, g_1f0a680);
    MonoBehaviour__ctor(ptr, 0);
    v25 = sub_f7db70(g_1eed760);
    sub_14a2bd4(v25, 8, g_1ef81a0);
    ptr->field_38 = v25;
    sub_f7d8d0();
    return;
}
```

## `GamepadNotifier.OnEnable` — RVA `0xc2eba8`

- Decompiled symbol: `GamepadNotifier_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `904` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadNotifier_Recovered` matched 4 offsets against `GamepadNotifier` metadata (confidence 0.67).

```c
typedef struct GamepadNotifier_Recovered {
    char padding_0[16];
    unsigned long long field_10;
    unsigned long long field_18;
    void* maxNotifications;
    struct struct_1 *notificationTemplate;
    char padding_30[16];
    void* msgUnknownGamepadConnected;
    char padding_48[40];
    char iconKnownGamepadConnected;
} GamepadNotifier_Recovered;

typedef struct struct_5 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_5;

typedef struct struct_4 {
    char padding_0[32];
    unsigned long long field_20;
} struct_4;

typedef struct struct_1 {
    char padding_0[8];
    unsigned long long field_8;
    char padding_10[66];
    char field_52;
} struct_1;

typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

typedef struct struct_3 {
    char padding_0[224];
    unsigned int field_e0;
} struct_3;

extern struct_3 *g_1ef0c58;
extern struct_2 *g_1ef81a8;
extern long long g_1ef81b8;
extern long long g_1ef81c0;
extern long long g_1ef81c8;
extern struct_0 *g_1efedf0;
extern struct_0 *g_1efedf8;
extern long long g_1efee00;
extern struct_0 *g_1efee08;
extern long long g_1f00240;
extern char g_1fab11e;

long long GamepadNotifier_OnEnable(struct_2 *ptr)
{
    long long v0;  // x0
    unsigned int v1;  // w8
    long long v9;  // x0
    unsigned long v10;  // x0
    unsigned long v11;  // x0
    struct_2 *v12;  // x0
    struct_5 *v2;  // x20
    struct_4 *v3;  // x8
    long long v4;  // x0
    struct_5 *p;  // x0
    unsigned long v6;  // x9
    struct_4 *addr;  // x8
    unsigned int v8;  // w20

    if (!(g_1fab11e & 1))
    {
        sub_f7d92c(&g_1efedf0);
        sub_f7d92c(&g_1efedf8);
        sub_f7d92c(&g_1efee00);
        sub_f7d92c(&g_1efee08);
        sub_f7d92c(&g_1ef81a8);
        sub_f7d92c(&g_1ef81b8);
        sub_f7d92c(&g_1ef81c0);
        sub_f7d92c(&g_1ef81c8);
        sub_f7d92c(&g_1f00240);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("qj");
        sub_f7d92c("uj");
        g_1fab11e = 1;
    }
    v0 = CFUtils__get_editorStopped(0);
    if (((char)v0 & 1))
        return v0;
    v1 = (int)ptr->field_20;
    v2 = ptr->field_28;
    if (1 >= (int)ptr->field_20)
        v1 = 1;
    *((unsigned int *)&ptr->field_20) = v1;
    v3 = g_1ef0c58->field_e0;
    if (!(unsigned int)v3)
        sub_f7da5c(g_1ef0c58);
    v4 = Object__op_Equality(v2, 0, 0);
    if (((char)v4 & 1))
        return v4;
    p = ptr->field_28;
    if (p)
    {
        p = Component__get_gameObject(p, 0);
        if (p)
        {
            GameObject__SetActive();
            p = *((long long *)&ptr->padding_30[8]);
            if (p)
            {
                do
                {
                    v3 = p->field_18;
                    if ((int)ptr->field_20 <= (unsigned int)v3 || !((v6 = (unsigned long)p->field_10, p->field_1c = p->field_1c + 1, v6)))
                        break;
                    if (*((int *)(v6 + 24)) > (unsigned int)v3)
                    {
                        addr = v6 + v3 * 8;
                        p->field_18 = (unsigned int)v3 + 1;
                        addr->field_20 = 0;
                        v3 = &addr->field_20;
                        sub_f7d8d0(v3, 0);
                    }
                    else
                    {
                        v3 = g_1ef81a8->field_20->field_c0;
                        sub_14a3390();
                    }
                    p = *((long long *)&ptr->padding_30[8]);
                } while (p);
            }
        }
    }
LABEL_102ed68:
    sub_f7db74(p);
    if ((unsigned int)v3 >= 1)
    {
        v8 = 0;
        do
        {
            v9 = sub_14a30c0();
            v3 = g_1ef0c58;
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Equality(v9, 0, 0) & 1))
            {
                v3 = g_1ef0c58->field_e0;
                if (!(unsigned int)v3)
                    sub_f7da5c(g_1ef0c58);
                p = sub_1129f50(ptr->field_28, g_1f00240);
                if (!*((long long *)&ptr->padding_30[8]))
                    goto LABEL_102ed68;
                sub_14a3114(*((long long *)&ptr->padding_30[8]), v8, p, g_1ef81c8);
            }
            p = *((long long *)&ptr->padding_30[8]);
            if (!p || !((p = (struct_5 *)(unsigned long long)sub_14a30c0(p, (unsigned long long)v8, g_1ef81c0), (unsigned long long)sub_14a30c0(p, (unsigned long long)v8, g_1ef81c0) && (NotificationElementGUI__End(), p = (struct_5 *)*((long long *)&ptr->padding_30[8]), p && (p = (struct_5 *)(unsigned long long)sub_14a30c0(p, (unsigned long long)v8, g_1ef81c0), (unsigned long long)sub_14a30c0(p, (unsigned long long)v8, g_1ef81c0) && (p = (struct_5 *)(unsigned long long)Component__get_transform(), (unsigned long long)Component__get_transform() && (Transform__SetParent(), p = (struct_5 *)*((long long *)&ptr->padding_30[8]), *((long long *)&ptr->padding_30[8]))))))))
                goto LABEL_102ed68;
        } while ((v8 += 1, v8 < p->field_18));
    }
    v10 = sub_f7db70(g_1ef3200);
    GamepadManager_OnConnectionChnageCallback__ctor(v10, ptr, g_1efedf0);
    GamepadManager__add_onGamepadActivated(v10);
    v11 = sub_f7db70(g_1ef3200);
    GamepadManager_OnConnectionChnageCallback__ctor(v11, ptr, g_1efedf8);
    GamepadManager__add_onGamepadConnected(v11);
    v12 = sub_f7db70(g_1ef3208);
    GamepadManager_OnDisconnectionCallback__ctor(v12, ptr, g_1efee08);
}
```

## `GamepadNotifier.OnDisable` — RVA `0xc2ef54`

- Decompiled symbol: `GamepadNotifier_OnDisable`
- Metadata signature: `private void OnDisable() { }`
- Native interval: `336` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadNotifier_Recovered` matched 4 offsets against `GamepadNotifier` metadata (confidence 0.67).

```c
typedef struct GamepadNotifier_Recovered {
    char padding_0[16];
    unsigned long long field_10;
    unsigned long long field_18;
    void* maxNotifications;
    struct struct_1 *notificationTemplate;
    char padding_30[16];
    void* msgUnknownGamepadConnected;
    char padding_48[40];
    char iconKnownGamepadConnected;
} GamepadNotifier_Recovered;

typedef struct struct_1 {
    char padding_0[8];
    unsigned long long field_8;
    char padding_10[66];
    char field_52;
} struct_1;

typedef struct struct_0 {
    char padding_0[8];
    unsigned long long field_8;
    char padding_10[66];
    char field_52;
} struct_0;

extern struct_0 *g_1efedf0;
extern struct_0 *g_1efedf8;
extern long long g_1efee00;
extern struct_0 *g_1efee08;
extern char g_1fab11f;

int GamepadNotifier_OnDisable(struct_2 *a0)
{
    unsigned long long v0;  // x0
    unsigned long v1;  // x0
    unsigned long v2;  // x0
    struct_2 *v3;  // x0

    if (!(g_1fab11f & 1))
    {
        sub_f7d92c(&g_1efedf0);
        sub_f7d92c(&g_1efedf8);
        sub_f7d92c(&g_1efee00);
        sub_f7d92c(&g_1efee08);
        sub_f7d92c("qj");
        sub_f7d92c("uj");
        g_1fab11f = 1;
    }
    v0 = CFUtils__get_editorStopped(0);
    if (((char)v0 & 1))
        return v0;
    v1 = sub_f7db70(g_1ef3200);
    GamepadManager_OnConnectionChnageCallback__ctor(v1, a0, g_1efedf0);
    GamepadManager__remove_onGamepadActivated(v1);
    v2 = sub_f7db70(g_1ef3200);
    GamepadManager_OnConnectionChnageCallback__ctor(v2, a0, g_1efedf8);
    GamepadManager__remove_onGamepadConnected(v2);
    v3 = sub_f7db70(g_1ef3208);
    GamepadManager_OnDisconnectionCallback__ctor(v3, a0, g_1efee08);
}
```

## `GamepadNotifier.Update` — RVA `0xc2f0a4`

- Decompiled symbol: `GamepadNotifier_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `336` bytes
- Result: `pseudocode`

```c
typedef struct struct_5 {
    char padding_0[24];
    unsigned int field_18;
} struct_5;

typedef struct struct_4 {
    char padding_0[56];
    struct struct_3 *field_38;
} struct_4;

typedef struct struct_3 {
    char padding_0[24];
    int field_18;
} struct_3;

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

extern struct_1 *g_1eefb00;
extern struct_0 *g_1ef0c58;
extern long long g_1ef81b8;
extern long long g_1ef81c0;
extern char g_1fab120;
extern char g_1fab1dd;

struct_5 * GamepadNotifier_Update(struct_4 *ptr)
{
    struct_3 *v0;  // x0
    int v1;  // w20
    long long v2;  // x0
    unsigned long v3;  // x0

    if (!(g_1fab120 & 1))
    {
        sub_f7d92c(&g_1ef81b8);
        sub_f7d92c(&g_1ef81c0);
        sub_f7d92c(&g_1ef0c58);
        g_1fab120 = 1;
    }
    if (!g_1fab1dd)
    {
        sub_f7d92c(&g_1eefb00);
        g_1fab1dd = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    Object__op_Inequality(g_1eefb00->field_b8->field_0, 0, 0);
    CFUtils__get_realDeltaTimeClamped(0);
    v0 = ptr->field_38;
    if (v0)
    {
        v1 = 0;
        do
        {
            if (v0->field_18 <= v1)
                return v0;
            v2 = sub_14a30c0();
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (!(Object__op_Inequality(v2, 0, 0) & 1))
                continue;
            v0 = ptr->field_38;
            if (!v0 || !((v0 = (struct_3 *)(unsigned long long)sub_14a30c0(v0, (unsigned long long)(unsigned int)v1, g_1ef81c0), (unsigned long long)sub_14a30c0(v0, (unsigned long long)(unsigned int)v1, g_1ef81c0))))
                break;
            NotificationElementGUI__UpdateNotification();
        } while ((v0 = (struct_3 *)ptr->field_38, v1 = (int)(v1 + 1), v0));
    }
    v3 = sub_f7db74(v0);
    return sub_f7db74(v0);
}
```

## `GamepadNotifier.OnGamepadConnected` — RVA `0xc2f264`

- Decompiled symbol: `GamepadNotifier_OnGamepadConnected`
- Metadata signature: `private void OnGamepadConnected(GamepadManager.Gamepad gamepad) { }`
- Native interval: `240` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
    char padding_20[8];
    long long field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

extern char g_1fab118;

long long GamepadNotifier_OnGamepadConnected(long long *p, struct_1 *ptr, unsigned long a2)
{
    unsigned long v0;  // x8
    long long v1;  // x0
    long long v2;  // x21
    unsigned long v3;  // x8
    unsigned long long v4;  // x0

    if (ptr)
    {
        if (!(g_1fab118 & 1))
        {
            sub_f7d92c("MT");
            g_1fab118 = 1;
        }
        if (ptr->field_18)
            v0 = &ptr->field_18->field_10;
        else
            v0 = g_1ef18f0->field_b8;
        if (((char)String__IsNullOrEmpty(*((long long *)v0), 0) & 1))
        {
            v1 = String__Format(p[8], ptr->field_28, 0);
        }
        else
        {
            v2 = p[9];
            if (!(g_1fab118 & 1))
            {
                sub_f7d92c("MT");
                g_1fab118 = 1;
            }
            if (ptr->field_18)
                v3 = &ptr->field_18->field_10;
            else
                v3 = g_1ef18f0->field_b8;
            v1 = String__Format(v2, *((long long *)v3), 0);
        }
        v4 = GamepadNotifier__AddNotification(p, v1);
        return GamepadNotifier__AddNotification(p, v1);
    }
    sub_f7db74();
}
```

## `GamepadNotifier.AddNotification` — RVA `0xc2f354`

- Decompiled symbol: `GamepadNotifier_AddNotification`
- Metadata signature: `private void AddNotification(string msg, Sprite icon) { }`
- Native interval: `428` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GamepadNotifier_Recovered` matched 2 offsets against `GamepadNotifier` metadata (confidence 1.00).

```c
typedef struct GamepadNotifier_Recovered {
    char padding_0[48];
    long long notificationListBox;
    unsigned long long notificationList;
} GamepadNotifier_Recovered;

typedef struct struct_2 {
    char padding_0[52];
    unsigned int field_34;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef81b8;
extern long long g_1ef81c0;
extern char g_1fab123;

unsigned long long GamepadNotifier_AddNotification(struct_1 *ptr, long long a1, long long a2)
{
    unsigned long long v0;  // x0
    unsigned long long v1;  // x0
    struct_2 *p;  // x22
    int v3;  // w23
    struct_2 *addr;  // x24
    unsigned int v5;  // s0
    unsigned int v6;  // s1
    unsigned long v7;  // 4133
    unsigned long long v8;  // x0

    if (!(g_1fab123 & 1))
    {
        sub_f7d92c(&g_1ef81b8);
        sub_f7d92c(&g_1ef81c0);
        sub_f7d92c(&g_1ef0c58);
        g_1fab123 = 1;
    }
    v0 = String__IsNullOrEmpty(a1, 0);
    if (((char)v0 & 1))
        return v0;
    v1 = ptr->field_38;
    if (v1)
    {
        p = NULL;
        v3 = 0;
        do
        {
            if (*((int *)(v1 + 24)) > v3)
            {
                addr = sub_14a30c0();
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                if ((Object__op_Equality(addr, 0, 0) & 1))
                    continue;
                if (!addr)
                    break;
                if (((char)NotificationElementGUI__IsActive(addr) & 1))
                {
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (!((char)Object__op_Equality(p, 0, 0) & 1))
                    {
                        if (!p)
                            break;
                        v5 = addr->field_34;
                        v6 = p->field_34;
                        v7 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v5, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v6) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v6) & 1)) & ((unsigned long long)(char)(CmpF(v5, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v6) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v7)
                            continue;
                    }
                    p = addr;
                }
                else
                {
                    p = addr;
                    goto LABEL_102f480;
                }
            }
            else
            {
LABEL_102f480:
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v1 = Object__op_Equality(p, 0, 0);
                if (((char)v1 & 1))
                    return v1;
                if (p)
                {
                    NotificationElementGUI__End();
                    NotificationElementGUI__Show(p, a1, a2, ptr->field_30);
                    v8 = GamepadNotifier__SortNotifications(ptr);
                    return GamepadNotifier__SortNotifications(ptr);
                }
                break;
            }
        } while ((v1 = ptr->field_38, v3 = (int)(v3 + 1), v1));
    }
    sub_f7db74(v1);
}
```

## `GamepadNotifier.OnGamepadActivated` — RVA `0xc2f500`

- Decompiled symbol: `GamepadNotifier_OnGamepadActivated`
- Metadata signature: `private void OnGamepadActivated(GamepadManager.Gamepad gamepad) { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
    char padding_20[20];
    unsigned int field_34;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

extern long long g_1ef0450;
extern char g_1fab118;
extern char g_1fab121;

unsigned long long GamepadNotifier_OnGamepadActivated(struct_1 *p, struct_1 *ptr)
{
    unsigned long v1;  // x21
    unsigned long v2;  // x9
    long long v3;  // x0
    long long v4;  // x0
    unsigned long long v5;  // x0
    unsigned int v0;  // [bp-0x24]

    if (!(g_1fab121 & 1))
    {
        sub_f7d92c(&g_1ef0450);
        g_1fab121 = 1;
    }
    if (ptr)
    {
        v1 = *((long long *)&p[1].padding_20[0]);
        if (!(g_1fab118 & 1))
        {
            sub_f7d92c("MT");
            g_1fab118 = 1;
        }
        if (ptr->field_18)
            v2 = &ptr->field_18->field_10;
        else
            v2 = g_1ef18f0->field_b8;
        v0 = ptr->field_34;
        v3 = sub_f7da64(g_1ef0450, &v0);
        v4 = String__Format(v1, *((long long *)v2), v3, 0);
        v5 = GamepadNotifier__AddNotification(p, v4, p[2].field_18);
        return GamepadNotifier__AddNotification(p, v4, p[2].field_18);
    }
    sub_f7db74();
}
```

## `GamepadNotifier.OnGamepadDisconnected` — RVA `0xc2f5d4`

- Decompiled symbol: `GamepadNotifier_OnGamepadDisconnected`
- Metadata signature: `private void OnGamepadDisconnected(GamepadManager.Gamepad gamepad, GamepadManager.DisconnectionReason reason) { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
    char padding_20[20];
    unsigned int field_34;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

extern long long g_1ef0450;
extern char g_1fab118;
extern char g_1fab122;

unsigned long long GamepadNotifier_OnGamepadDisconnected(struct_1 *p, struct_1 *ptr)
{
    unsigned long v1;  // x21
    unsigned long v2;  // x9
    long long v3;  // x0
    long long v4;  // x0
    unsigned long long v5;  // x0
    unsigned int v0;  // [bp-0x24]

    if (!(g_1fab122 & 1))
    {
        sub_f7d92c(&g_1ef0450);
        g_1fab122 = 1;
    }
    if (ptr)
    {
        v1 = p[1].field_18;
        if (!(g_1fab118 & 1))
        {
            sub_f7d92c("MT");
            g_1fab118 = 1;
        }
        if (ptr->field_18)
            v2 = &ptr->field_18->field_10;
        else
            v2 = g_1ef18f0->field_b8;
        v0 = ptr->field_34;
        v3 = sub_f7da64(g_1ef0450, &v0);
        v4 = String__Format(v1, *((long long *)v2), v3, 0);
        v5 = GamepadNotifier__AddNotification(p, v4, *((long long *)&p[2].padding_0[8]));
        return GamepadNotifier__AddNotification(p, v4, *((long long *)&p[2].padding_0[8]));
    }
    sub_f7db74();
}
```

## `GamepadNotifier.OnGamepadDisactivated` — RVA `0xc2f6a8`

- Decompiled symbol: `GamepadNotifier_OnGamepadDisactivated`
- Metadata signature: `private void OnGamepadDisactivated(GamepadManager.Gamepad gamepad, GamepadManager.DisconnectionReason reason) { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long GamepadNotifier_OnGamepadDisactivated(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `GamepadNotifier.SortNotifications` — RVA `0xc2f860`

- Decompiled symbol: `GamepadNotifier_SortNotifications`
- Metadata signature: `private void SortNotifications() { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[56];
    unsigned long long field_38;
} struct_0;

extern long long g_1eec368;
extern long long g_1ef81b0;
extern long long g_1f00188;
extern char g_1fab124;

void GamepadNotifier_SortNotifications(struct_0 *a0)
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
    if (!(g_1fab124 & 1))
    {
        sub_f7d92c(&g_1eec368);
        sub_f7d92c(&g_1ef81b0);
        sub_f7d92c(&g_1f00188);
        g_1fab124 = 1;
    }
    v10 = sub_f7db70(g_1eec368);
    sub_1773e0c(v10, 0, g_1f00188, 0);
    if (!a0->field_38)
        sub_f7db74();
}
```
