# Native pseudocode: NotificationElementGUI

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `NotificationElementGUI.End` — RVA `0xc2ef30`

- Decompiled symbol: `NotificationElementGUI_End`
- Metadata signature: `public void End() { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
void NotificationElementGUI_End(void)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (Component__get_gameObject())
    {
        GameObject__SetActive();
        return;
    }
    sub_f7db74();
}
```

## `NotificationElementGUI.UpdateNotification` — RVA `0xc2f1f4`

- Decompiled symbol: `NotificationElementGUI_UpdateNotification`
- Metadata signature: `public void UpdateNotification(float dt) { }`
- Native interval: `112` bytes
- Result: `pseudocode`
- Heuristic layout hint: `NotificationElementGUI_Recovered` matched 2 offsets against `NotificationElementGUI` metadata (confidence 0.67).

```c
typedef struct NotificationElementGUI_Recovered {
    struct struct_0 *field_0;
    char padding_8[40];
    unsigned int duration;
    unsigned int elapsed;
} NotificationElementGUI_Recovered;

typedef struct struct_0 {
    char padding_0[376];
    unsigned long long field_178;
} struct_0;

void NotificationElementGUI_UpdateNotification(struct_1 *ptr)
{
    unsigned int v0;  // s1
    unsigned int v1;  // s0
    unsigned int v2;  // s0
    unsigned long v3;  // 4150

    if (!((char)NotificationElementGUI__IsActive() & 1))
        return;
    v0 = ptr->field_30;
    v2 = ptr->field_34 + v1;
    ptr->field_34 = v2;
    v3 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v2, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v0) & 1)) & ((unsigned long long)(char)(CmpF(v2, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v3))
    {
        if (Component__get_gameObject(ptr, 0))
            GameObject__SetActive();
        else
            sub_f7db74();
    }
    goto ptr->field_0->field_178;
}
```

## `NotificationElementGUI.IsActive` — RVA `0xc2f6ac`

- Decompiled symbol: `NotificationElementGUI_IsActive`
- Metadata signature: `public bool IsActive() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
void NotificationElementGUI_IsActive(unsigned long a0, unsigned long a1, unsigned long a2, unsigned long a3)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (Component__get_gameObject())
    {
        GameObject__get_activeSelf();
        return;
    }
    sub_f7db74();
}
```

## `NotificationElementGUI.Show` — RVA `0xc2f6cc`

- Decompiled symbol: `NotificationElementGUI_Show`
- Metadata signature: `public void Show(string msg, Sprite icon, RectTransform parent, float duration) { }`
- Native interval: `404` bytes
- Result: `pseudocode`
- Heuristic layout hint: `NotificationElementGUI_Recovered` matched 3 offsets against `NotificationElementGUI` metadata (confidence 1.00).

```c
typedef struct NotificationElementGUI_Recovered {
    char padding_0[32];
    struct struct_3 *targetText;
    char padding_28[8];
    unsigned int duration;
    unsigned int elapsed;
} NotificationElementGUI_Recovered;

typedef struct struct_0 {
    char padding_0[1512];
    struct struct_1 *field_5e8;
    unsigned long long field_5f0;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1ef0c58;
extern unsigned long long g_1ef1170;
extern long long g_1fab000;
extern char g_1fab125;

void NotificationElementGUI_Show(struct_2 *ptr, unsigned long long a1, unsigned long a2, long long a3)
{
    unsigned long long v7;  // d8
    unsigned long long v8;  // x30
    struct_0 **v16;  // x0
    unsigned int v17;  // s0
    unsigned long long v18;  // x1
    unsigned long long v19;  // x2
    long long v20;  // x23
    unsigned long long v9;  // x23
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    long long v14;  // x0
    unsigned long long flag;  // x3
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]
    unsigned long long v5;  // [bp-0x10]
    unsigned long long v6;  // [bp-0x8]

    v0 = v7;
    v1 = v8;
    v2 = v9;
    v3 = v10;
    v4 = v11;
    v5 = v12;
    v6 = v13;
    v20 = &g_1fab000;
    if (!(g_1fab125 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef1170);
        g_1fab125 = 1;
    }
    v14 = Component__get_transform(ptr, 0);
    if (v14)
    {
        v20 = v14;
        if (*((long long *)v14) != g_1ef1170)
            goto LABEL_102f858;
        flag = 0;
        Transform__SetParent(v20, a3, 0, 0);
        Transform__SetSiblingIndex(v20, 0, 0);
        if (Component__get_gameObject(ptr, 0))
        {
            GameObject__SetActive();
            v16 = ptr->field_20;
            ptr->field_30 = v17;
            ptr->field_34 = 0;
            if (v16)
            {
                v18 = a1;
                v19 = *(v16)->field_5f0;
                *(v16)->field_5e8();
            }
        }
    }
    sub_f7db74();
LABEL_102f858:
    sub_f7df10(v20);
}
```

## `NotificationElementGUI.GetTimeElapsed` — RVA `0xc2f904`

- Decompiled symbol: `NotificationElementGUI_GetTimeElapsed`
- Metadata signature: `public float GetTimeElapsed() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long NotificationElementGUI_GetTimeElapsed(unsigned long a0)
{
    return a0;
}
```

## `NotificationElementGUI.OnUpdate` — RVA `0xc2f90c`

- Decompiled symbol: `NotificationElementGUI_OnUpdate`
- Metadata signature: `protected virtual void OnUpdate() { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
extern long long g_1ef22e8;
extern char g_1fab1e1;

void NotificationElementGUI_OnUpdate(unsigned int *ptr)
{
    unsigned long long v4;  // d8
    unsigned long long v5;  // x30
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned int v8;  // s8
    long long v9;  // x0
    unsigned long v11;  // 4159
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    v8 = ptr[13] / ptr[12];
    v9 = Component__get_transform();
    if (!g_1fab1e1)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab1e1 = 1;
    }
    v11 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF((0x3f800000 - v8) * 0x41000000, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF((0x3f800000 - v8) * 0x41000000, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((0x3f800000 - v8) * 0x41000000, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF((0x3f800000 - v8) * 0x41000000, 0.0) & 1)) & ((unsigned long long)(char)(CmpF((0x3f800000 - v8) * 0x41000000, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF((0x3f800000 - v8) * 0x41000000, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (v9)
    {
        Transform__set_localScale();
        return;
    }
    sub_f7db74();
}
```

## `NotificationElementGUI.Compare` — RVA `0xc2f9b0`

- Decompiled symbol: `NotificationElementGUI_Compare`
- Metadata signature: `public static int Compare(NotificationElementGUI a, NotificationElementGUI b) { }`
- Native interval: `264` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[52];
    unsigned int field_34;
} struct_1;

typedef struct struct_2 {
    char padding_0[52];
    unsigned int field_34;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab126;

unsigned int NotificationElementGUI_Compare(struct_1 *ptr, struct_2 *p, unsigned long a2, unsigned int a3)
{
    unsigned int v0;  // w0
    unsigned int v1;  // w0
    unsigned long v2;  // x0
    unsigned long v3;  // 4117
    unsigned int v4;  // w0
    unsigned int v5;  // s0
    unsigned int v6;  // s1
    unsigned int v7;  // 4100
    unsigned long v8;  // 4119
    unsigned long v9;  // 4102

    if (!(g_1fab126 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab126 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(ptr, 0, 0) & 1))
        return 0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Equality(p, 0, 0) & 1))
    {
        if (ptr && (v0 = (unsigned int)(unsigned long long)NotificationElementGUI__IsActive(ptr, 0, 0, a3), p))
        {
            v1 = (unsigned long long)NotificationElementGUI__IsActive(p, 0, 0, a3);
            v2 = (unsigned long long)NotificationElementGUI__IsActive(ptr, 0, 0, a3);
            if (((unsigned int)(unsigned long long)NotificationElementGUI__IsActive(ptr, 0, 0, a3) & 1) != (v1 & 1))
            {
                v3 = arm64g_calculate_condition(25, (unsigned long long)((unsigned int)v2 & 1), 0, 0);
                if ((char)v3)
                    v4 = 4294967295;
                else
                    v4 = 0;
                return v4;
            }
            else if (((char)v2 & 1))
            {
                v5 = ptr->field_34;
                v6 = p->field_34;
                v7 = CmpF(v5, v6);
                v8 = (((CmpF(v5, v6) >> 5 & 3 | CmpF(v5, v6) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1;
                if (!((char)((v8 - ((CmpF(v5, v6) >> 5 & 3 | CmpF(v5, v6) & 1) & (v7 >> 5 & 3 | CmpF(v5, v6) & 1) >> 1 & 1)) * 0x10000000 >> 30)))
                {
                    v9 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v5, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v6) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v6) & 1)) & ((unsigned long long)(char)(CmpF(v5, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v6) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if ((char)v9)
                        return 1;
                    return 4294967295;
                }
            }
        }
        else
        {
            sub_f7db74();
        }
    }
    return 0;
}
```

## `NotificationElementGUI.ctor` — RVA `0xc2fab8`

- Decompiled symbol: `NotificationElementGUI_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long NotificationElementGUI_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
