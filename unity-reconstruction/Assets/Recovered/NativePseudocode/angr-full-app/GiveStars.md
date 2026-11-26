# Native pseudocode: GiveStars

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GiveStars.Start` — RVA `0xc6b704`

- Decompiled symbol: `GiveStars_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `136` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GiveStars_Recovered` matched 3 offsets against `GiveStars` metadata (confidence 1.00).

```c
typedef struct GiveStars_Recovered {
    char padding_0[32];
    struct struct_0 *Stars;
    unsigned long long OkBtnLock;
    long long ThankPanel;
} GiveStars_Recovered;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_2 {
    char padding_0[32];
    long long field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

void GiveStars_Start(struct_1 *p, unsigned long a1)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_3 *v6;  // x8
    struct_1 *ptr;  // x19
    unsigned long long v8;  // x20
    struct_2 *v9;  // x8
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    v6 = p->field_20;
    if (p->field_20)
    {
        ptr = p;
        v8 = 0;
        do
        {
            if (v6->field_18 <= (unsigned int)v8)
                goto LABEL_0x106b758;
            if (v6->field_18 <= (unsigned int)v8)
                sub_f7db7c();
            v9 = &v6->padding_0[8 * v8];
        } while (v9->field_20 && !((GameObject__SetActive(v9->field_20, 0, 0), v6 = (struct_3 *)ptr->field_20, v8 += 1, !ptr->field_20)));
    }
    do
    {
        do
        {
            sub_f7db74();
        } while (!ptr->field_30);
    } while ((GameObject__SetActive(ptr->field_30, 0, 0), !ptr->field_28));
    GameObject__SetActive();
    return;
}
```

## `GiveStars.ShowStars` — RVA `0xc6b78c`

- Decompiled symbol: `GiveStars_ShowStars`
- Metadata signature: `public void ShowStars(int n) { }`
- Native interval: `204` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GiveStars_Recovered` matched 3 offsets against `GiveStars` metadata (confidence 1.00).

```c
typedef struct GiveStars_Recovered {
    char padding_0[32];
    struct struct_0 *Stars;
    unsigned long long OkBtnLock;
    char padding_30[16];
    unsigned int CountStar;
} GiveStars_Recovered;

typedef struct struct_4 {
    char padding_0[24];
    unsigned int field_18;
} struct_4;

typedef struct struct_2 {
    char padding_0[32];
    long long field_20;
} struct_2;

typedef struct struct_3 {
    char padding_0[32];
    long long field_20;
} struct_3;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

void GiveStars_ShowStars(struct_1 *ptr, unsigned int a1)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned int v14;  // w21
    struct_3 *v15;  // x8
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    struct_4 *i;  // x8
    unsigned long long v9;  // x21
    struct_1 *v10;  // x0
    struct_1 *v11;  // x0
    struct_2 *v12;  // x8
    struct_1 *v13;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    i = ptr->field_20;
    ptr->field_40 = a1;
    if (i)
    {
        v9 = 0;
        v10 = ptr;
        while (true)
        {
            v11 = v10;
            if (i->field_18 <= (unsigned int)v9)
                break;
            if (i->field_18 <= (unsigned int)v9)
                goto LABEL_106b854;
            v12 = &i->padding_0[8 * v9];
            if (!v12->field_20 || !((v13 = (struct_1 *)(unsigned long long)GameObject__SetActive(v12->field_20, 0, 0), i = (struct_4 *)ptr->field_20, v9 += 1, v10 = (struct_1 *)(unsigned long long)GameObject__SetActive(v12->field_20, 0, 0), i)))
                goto LABEL_106b850;
        }
        if (a1 < 1)
        {
LABEL_106b834:
            if (ptr->field_28)
            {
                GameObject__SetActive();
                return;
            }
            goto LABEL_106b850;
        }
        if (i)
        {
            for (v14 = 0; i->field_18 > v14; i = ptr->field_20)
            {
                v15 = &i->padding_0[8 * v14];
                if (!v15->field_20)
                    goto LABEL_106b850;
                v11 = GameObject__SetActive(v15->field_20, 1, 0);
                if (a1 == v14 + 1)
                    goto LABEL_106b834;
            }
            goto LABEL_106b854;
        }
    }
LABEL_106b850:
    v11 = sub_f7db74();
LABEL_106b854:
    sub_f7db7c(v11);
}
```

## `GiveStars.RateFun` — RVA `0xc6b858`

- Decompiled symbol: `GiveStars_RateFun`
- Metadata signature: `public void RateFun(string AdLink) { }`
- Native interval: `196` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GiveStars_Recovered` matched 2 offsets against `GiveStars` metadata (confidence 1.00).

```c
typedef struct GiveStars_Recovered {
    char padding_0[56];
    long long RatePanel;
    int CountStar;
} GiveStars_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eee870;
extern long long g_1f0d290;
extern char g_1fab331;

void GiveStars_RateFun(struct_1 *a0, long long a1)
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
    if (!(g_1fab331 & 1))
    {
        sub_f7d92c(&g_1eee870);
        sub_f7d92c(&g_1f0d290);
        g_1fab331 = 1;
    }
    if (a0->field_40 <= 3)
    {
        GiveStars__HideRatePanel(a0);
        MonoBehaviour__StartCoroutine();
        return;
    }
    if (!g_1eee870->field_e0)
        sub_f7da5c(g_1eee870);
    Application__OpenURL(a1, 0);
    if (a0->field_38)
    {
        GameObject__SetActive(a0->field_38, 0, 0);
        PlayerPrefs__SetInt();
        return;
    }
    sub_f7db74(0);
}
```

## `GiveStars.HideRatePanel` — RVA `0xc6b91c`

- Decompiled symbol: `GiveStars_HideRatePanel`
- Metadata signature: `private IEnumerator HideRatePanel() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef3238;
extern char g_1fab332;

struct_0 * GiveStars_HideRatePanel(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab332 & 1))
    {
        sub_f7d92c(&g_1ef3238);
        g_1fab332 = 1;
    }
    v0 = sub_f7db70(g_1ef3238);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `GiveStars.<HideRatePanel>d__8.ctor` — RVA `0xc6b988`

- Decompiled symbol: `GiveStars_HideRatePanel_d__8_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void GiveStars_HideRatePanel_d__8_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `GiveStars.ctor` — RVA `0xc6b9b0`

- Decompiled symbol: `GiveStars_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long GiveStars_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```

## `GiveStars.<HideRatePanel>d__8.Dispose` — RVA `0xc6b9b8`

- Decompiled symbol: `GiveStars_HideRatePanel_d__8_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long GiveStars_HideRatePanel_d__8_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `GiveStars.<HideRatePanel>d__8.MoveNext` — RVA `0xc6b9bc`

- Decompiled symbol: `GiveStars_HideRatePanel_d__8_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_1 *field_20;
} struct_0;

typedef struct struct_1 {
    char padding_0[48];
    long long field_30;
    long long field_38;
} struct_1;

extern long long g_1ef2440;
extern char g_1fab333;

unsigned int GiveStars_HideRatePanel_d__8_MoveNext(struct_0 *ptr)
{
    long long v0[8];  // x8
    long long v1;  // x21
    struct_0 *p;  // x19

    if (!(g_1fab333 & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab333 = 1;
    }
    v0 = ptr->field_20;
    if (ptr->field_10 == 1)
    {
        ptr->field_10 = 4294967295;
        if (!v0)
            sub_f7db74();
        if (v0[7])
            GameObject__SetActive(v0[7], 0, 0);
        else
            sub_f7db74();
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        if (!v0)
            sub_f7db74();
        if (v0[6])
        {
            GameObject__SetActive(v0[6], 1, 0);
            v1 = sub_f7db70(g_1ef2440);
            WaitForSeconds__ctor(v1, 0);
            ptr->field_18 = v1;
            p = &ptr->field_18;
            sub_f7d8d0(p, v1);
            *((unsigned int *)&p->padding_0[8]) = 1;
            return 1;
        }
        sub_f7db74();
    }
    return 0;
}
```

## `GiveStars.<HideRatePanel>d__8.get_Current` — RVA `0xc6ba90`

- Decompiled symbol: `GiveStars_HideRatePanel_d__8_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GiveStars_HideRatePanel_d__8_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `GiveStars.<HideRatePanel>d__8.Reset` — RVA `0xc6ba98`

- Decompiled symbol: `GiveStars_HideRatePanel_d__8_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f046d8;

void GiveStars_HideRatePanel_d__8_Reset(void)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = sub_f7db70(sub_f7d940(&g_1ef0bd8));
    NotSupportedException__ctor(v4, 0);
    sub_f7da4c(v4, sub_f7d940(&g_1f046d8));
}
```

## `GiveStars.<HideRatePanel>d__8.get_Current` — RVA `0xc6bad0`

- Decompiled symbol: `GiveStars_HideRatePanel_d__8_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GiveStars_HideRatePanel_d__8_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
