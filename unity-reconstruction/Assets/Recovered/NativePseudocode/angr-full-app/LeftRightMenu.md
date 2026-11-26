# Native pseudocode: LeftRightMenu

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `LeftRightMenu.OnSelect` — RVA `0xc5a654`

- Decompiled symbol: `LeftRightMenu_OnSelect`
- Metadata signature: `public override void OnSelect(BaseEventData data) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long LeftRightMenu_OnSelect(void)
{
}
```

## `LeftRightMenu.OnDeselect` — RVA `0xc5a65c`

- Decompiled symbol: `LeftRightMenu_OnDeselect`
- Metadata signature: `public override void OnDeselect(BaseEventData data) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long LeftRightMenu_OnDeselect(void)
{
}
```

## `LeftRightMenu.OnMove` — RVA `0xc5a664`

- Decompiled symbol: `LeftRightMenu_OnMove`
- Metadata signature: `public override void OnMove(AxisEventData data) { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    char padding_8[32];
    unsigned int field_28;
} struct_1;

typedef struct struct_4 {
    char padding_0[304];
    struct struct_2 *field_130;
} struct_4;

typedef struct struct_2 {
    char padding_0[24];
    struct struct_3 *field_18;
    char padding_20[8];
    unsigned long long field_28;
    char padding_30[16];
    unsigned long long field_40;
} struct_2;

typedef struct struct_0 {
    char padding_0[392];
    unsigned long long field_188;
} struct_0;

typedef struct struct_3 {
    unsigned long long field_0;
} struct_3;

void LeftRightMenu_OnMove(struct_4 *p, struct_1 *a1)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v4;  // x1
    struct_2 *ptr;  // x8
    unsigned long long v6;  // x0
    unsigned long long v7;  // x2
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    if (a1 && (a1->field_28 | 2) == 2)
    {
        if (!a1->field_28)
            v4 = 4294967295;
        else
            v4 = 0;
        if (p)
        {
            ptr = p->field_130;
            if (ptr)
            {
                v6 = ptr->field_40;
                v7 = ptr->field_28;
                ptr->field_18();
            }
            goto a1->field_0->field_188;
        }
    }
    sub_f7db74();
}
```

## `LeftRightMenu.OnSwitch` — RVA `0xc5a6d0`

- Decompiled symbol: `LeftRightMenu_OnSwitch`
- Metadata signature: `private void OnSwitch(int dir) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[304];
    struct struct_0 *field_130;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

void LeftRightMenu_OnSwitch(struct_1 *a0)
{
    if (!a0->field_130)
        return;
    goto a0->field_130->field_18;
}
```

## `LeftRightMenu.GetItemCount` — RVA `0xc5a6ec`

- Decompiled symbol: `LeftRightMenu_GetItemCount`
- Metadata signature: `public int GetItemCount() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[312];
    struct struct_0 *field_138;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

int LeftRightMenu_GetItemCount(struct_1 *a0, unsigned long a1)
{
    if (a0->field_138)
        return a0->field_138->field_18;
    sub_f7db74();
}
```

## `LeftRightMenu.SetItemActive` — RVA `0xc5a708`

- Decompiled symbol: `LeftRightMenu_SetItemActive`
- Metadata signature: `public void SetItemActive(int id) { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[312];
    struct struct_1 *field_138;
} struct_2;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2a0;

struct_2 * LeftRightMenu_SetItemActive(struct_2 *ptr, unsigned int a1)
{
    struct_2 *v0;  // x0
    struct_2 *v1;  // x0
    struct_2 *v2;  // x0
    struct_3 *p;  // x8
    unsigned long long v4;  // x21
    unsigned long v5;  // x9
    unsigned long v6;  // x20
    unsigned long v7;  // x0

    v0 = ptr;
    if (!(g_1fab2a0 & 1))
    {
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab2a0 = 1;
        v0 = v1;
    }
    v2 = v0;
    p = ptr->field_138;
    if (ptr->field_138)
    {
        v4 = 0;
        do
        {
            v5 = p->field_18;
            if ((v5 & 4294967295) <= v4)
                return v2;
            if (v5 <= v4)
                sub_f7db7c();
            v6 = *((long long *)&p[1].padding_0[4 + 8 * v4]);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if ((Object__op_Equality(v6, 0, 0) & 1))
                continue;
            if (!v6 || !Component__get_gameObject(v6, 0))
                break;
            v2 = GameObject__SetActive();
        } while ((p = (struct_3 *)ptr->field_138, v4 += 1, p));
    }
    v7 = sub_f7db74();
    return sub_f7db74();
}
```

## `LeftRightMenu.SetTitle` — RVA `0xc5a7dc`

- Decompiled symbol: `LeftRightMenu_SetTitle`
- Metadata signature: `public void SetTitle(string title) { }`
- Native interval: `160` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[288];
    struct struct_3 *field_120;
} struct_2;

typedef struct struct_1 {
    char padding_0[1512];
    unsigned long long field_5e8;
} struct_1;

typedef struct struct_3 {
    struct struct_1 *field_0;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2a1;

long long LeftRightMenu_SetTitle(struct_2 *a0, unsigned long a1)
{
    long long v0;  // x0

    if (!(g_1fab2a1 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab2a1 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Inequality(a0->field_120, 0, 0);
    if (!((char)v0 & 1))
    {
        return v0;
    }
    else if (a0->field_120)
    {
        goto a0->field_120->field_0->field_5e8;
    }
    else
    {
        sub_f7db74(0);
    }
}
```

## `LeftRightMenu.OnEnable` — RVA `0xc5a87c`

- Decompiled symbol: `LeftRightMenu_OnEnable`
- Metadata signature: `protected override void OnEnable() { }`
- Native interval: `492` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LeftRightMenu_Recovered` matched 5 offsets against `LeftRightMenu` metadata (confidence 1.00).

```c
typedef struct LeftRightMenu_Recovered {
    char padding_0[256];
    struct struct_1 *buttonLeft;
    struct struct_2 *buttonRight;
    struct struct_3 *buttonBack;
    long long contentPlaceholder;
    char padding_120[24];
    struct struct_4 *optionItems;
} LeftRightMenu_Recovered;

typedef struct struct_1 {
    char padding_0[256];
    long long field_100;
} struct_1;

typedef struct struct_2 {
    char padding_0[256];
    long long field_100;
} struct_2;

typedef struct struct_3 {
    char padding_0[256];
    long long field_100;
} struct_3;

typedef struct struct_4 {
    char padding_0[24];
    unsigned int field_18;
} struct_4;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1eff700;
extern long long g_1eff708;
extern long long g_1eff710;
extern char g_1fab2a2;

long long LeftRightMenu_OnEnable(struct_5 *ptr)
{
    long long v0;  // x0
    long long v1;  // x0
    long long v2;  // x0
    unsigned long v3;  // x0
    struct_4 *p;  // x8
    unsigned long long v5;  // x21
    unsigned long v6;  // x9
    unsigned long v7;  // x20
    unsigned long v8;  // x0

    if (!(g_1fab2a2 & 1))
    {
        sub_f7d92c(&g_1eff700);
        sub_f7d92c(&g_1eff708);
        sub_f7d92c(&g_1eff710);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("Q[");
        g_1fab2a2 = 1;
    }
    Selectable__OnEnable(ptr, 0);
    if (ptr->field_100)
    {
        v0 = sub_f7db70(g_1ef2108);
        UnityAction__ctor(v0, ptr, g_1eff708, 0);
        if (ptr->field_100->field_100)
        {
            UnityEvent__AddListener(ptr->field_100->field_100, v0, 0);
            if (ptr->field_108)
            {
                v1 = sub_f7db70(g_1ef2108);
                UnityAction__ctor(v1, ptr, g_1eff710, 0);
                if (ptr->field_108->field_100)
                {
                    UnityEvent__AddListener(ptr->field_108->field_100, v1, 0);
                    if (ptr->field_110)
                    {
                        v2 = sub_f7db70(g_1ef2108);
                        UnityAction__ctor(v2, ptr, g_1eff700, 0);
                        if (ptr->field_110->field_100)
                        {
                            v3 = UnityEvent__AddListener(ptr->field_110->field_100, v2, 0);
                            p = ptr->field_138;
                            if (ptr->field_138)
                            {
                                v5 = 0;
                                do
                                {
                                    v6 = p->field_18;
                                    if ((v6 & 4294967295) <= v5)
                                        return v3;
                                    if (v6 <= v5)
                                        sub_f7db7c();
                                    v7 = *((long long *)&p[1].padding_0[4 + 8 * v5]);
                                    if (!g_1ef0c58->field_e0)
                                        sub_f7da5c(g_1ef0c58);
                                    if ((Object__op_Equality(v7, 0, 0) & 1))
                                        continue;
                                    if (!v7 || !((Transform__SetParent(v7, ptr->field_118, 0, 0), Component__get_gameObject(v7, 0))))
                                        break;
                                    v3 = GameObject__SetActive();
                                } while ((p = (struct_4 *)ptr->field_138, v5 += 1, p));
                            }
                        }
                    }
                }
            }
        }
    }
    v8 = sub_f7db74();
    return sub_f7db74();
}
```

## `LeftRightMenu.OnDisable` — RVA `0xc5aa68`

- Decompiled symbol: `LeftRightMenu_OnDisable`
- Metadata signature: `protected override void OnDisable() { }`
- Native interval: `100` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LeftRightMenu_Recovered` matched 3 offsets against `LeftRightMenu` metadata (confidence 1.00).

```c
typedef struct LeftRightMenu_Recovered {
    char padding_0[256];
    struct struct_0 *buttonLeft;
    struct struct_1 *buttonRight;
    struct struct_2 *buttonBack;
} LeftRightMenu_Recovered;

typedef struct struct_0 {
    char padding_0[256];
    long long field_100;
} struct_0;

typedef struct struct_1 {
    char padding_0[256];
    long long field_100;
} struct_1;

typedef struct struct_2 {
    char padding_0[256];
    long long field_100;
} struct_2;

void LeftRightMenu_OnDisable(struct_3 *a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    if (a0->field_100 && a0->field_100->field_100)
    {
        UnityEventBase__RemoveAllListeners(a0->field_100->field_100, 0);
        if (a0->field_108 && a0->field_108->field_100)
        {
            UnityEventBase__RemoveAllListeners(a0->field_108->field_100, 0);
            if (a0->field_110 && a0->field_110->field_100)
                UnityEventBase__RemoveAllListeners(a0->field_110->field_100, 0);
        }
    }
    sub_f7db74();
}
```

## `LeftRightMenu.OnBackPressed` — RVA `0xc5aacc`

- Decompiled symbol: `LeftRightMenu_OnBackPressed`
- Metadata signature: `private void OnBackPressed() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[296];
    struct struct_0 *field_128;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

void LeftRightMenu_OnBackPressed(struct_1 *a0)
{
    if (!a0->field_128)
        return;
    goto a0->field_128->field_18;
}
```

## `LeftRightMenu.OnLeftPressed` — RVA `0xc5aae8`

- Decompiled symbol: `LeftRightMenu_OnLeftPressed`
- Metadata signature: `private void OnLeftPressed() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[304];
    struct struct_0 *field_130;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

void LeftRightMenu_OnLeftPressed(struct_1 *a0)
{
    if (!a0->field_130)
        return;
    goto a0->field_130->field_18;
}
```

## `LeftRightMenu.OnRightPressed` — RVA `0xc5ab08`

- Decompiled symbol: `LeftRightMenu_OnRightPressed`
- Metadata signature: `private void OnRightPressed() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[304];
    struct struct_0 *field_130;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

void LeftRightMenu_OnRightPressed(struct_1 *a0)
{
    if (!a0->field_130)
        return;
    goto a0->field_130->field_18;
}
```

## `LeftRightMenu.ctor` — RVA `0xc5ab28`

- Decompiled symbol: `LeftRightMenu_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef15b0;
extern char g_1fab2a3;

void LeftRightMenu_ctor(unsigned long a0)
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
    if (!(g_1fab2a3 & 1))
    {
        sub_f7d92c(&g_1ef15b0);
        g_1fab2a3 = 1;
    }
    if (!g_1ef15b0->field_e0)
        sub_f7da5c(g_1ef15b0);
}
```
