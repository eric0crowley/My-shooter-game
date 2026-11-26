# Native pseudocode: AppOpenAdManager

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AppOpenAdManager.get_Instance` — RVA `0xc72f6c`

- Decompiled symbol: `AppOpenAdManager_get_Instance`
- Metadata signature: `public static AppOpenAdManager get_Instance() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    long long field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1eee850;
extern char g_1fab38c;

long long AppOpenAdManager_get_Instance(void)
{
    long long v0;  // x19

    if (!(g_1fab38c & 1))
    {
        sub_f7d92c(&g_1eee850);
        g_1fab38c = 1;
    }
    if (g_1eee850->field_b8->field_0)
        return g_1eee850->field_b8->field_0;
    v0 = sub_f7db70(g_1eee850);
    Object__ctor(v0, 0);
    g_1eee850->field_b8->field_0 = v0;
    sub_f7d8d0(g_1eee850->field_b8, v0);
    return g_1eee850->field_b8->field_0;
}
```

## `AppOpenAdManager.LoadAppOpenAd` — RVA `0xc72ff4`

- Decompiled symbol: `AppOpenAdManager_LoadAppOpenAd`
- Metadata signature: `public void LoadAppOpenAd() { }`
- Native interval: `324` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[16];
    long long field_10;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern long long g_1eec0e8;
extern struct_0 *g_1eee700;
extern struct_2 *g_1eef458;
extern long long g_1efbd08;
extern long long g_1f0bdd8;
extern char g_1fab390;

void AppOpenAdManager_LoadAppOpenAd(struct_3 *a0)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    struct_3 *ptr;  // x20
    long long v12;  // x0
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
    if (!(g_1fab390 & 1))
    {
        sub_f7d92c(&g_1eec0e8);
        sub_f7d92c("{+");
        sub_f7d92c(&g_1eee700);
        sub_f7d92c(&g_1efbd08);
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f0bdd8);
        g_1fab390 = 1;
    }
    ptr = &a0->field_10;
    if (a0->field_10)
    {
        AppOpenAd__Destroy(a0->field_10, 0);
        *((long long *)&ptr->padding_0[0]) = 0;
        sub_f7d8d0(ptr, 0);
    }
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__Log(g_1f0bdd8, 0);
    AdRequest__ctor(sub_f7db70(g_1eee6c0), 0);
    if (!g_1eee700->field_b8->field_0)
        sub_f7db74();
    v12 = sub_f7db70(g_1eec0e8);
    sub_12633ac(v12, a0, g_1efbd08, 0);
}
```

## `AppOpenAdManager.ctor` — RVA `0xc74d5c`

- Decompiled symbol: `AppOpenAdManager_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long AppOpenAdManager_ctor(void)
{
    long long v0;  // x0

    v0 = Object__ctor();
    return Object__ctor();
}
```

## `AppOpenAdManager.get_IsAdAvailable` — RVA `0xc74d64`

- Decompiled symbol: `AppOpenAdManager_get_IsAdAvailable`
- Metadata signature: `public bool get_IsAdAvailable() { }`
- Native interval: `220` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    long long field_10;
} struct_2;

extern char g_1fab38d;

unsigned int AppOpenAdManager_get_IsAdAvailable(struct_2 *a0)
{
    long long v0;  // x0

    if (!(g_1fab38d & 1))
    {
        sub_f7d92c("O6");
        sub_f7d92c("YX");
        g_1fab38d = 1;
    }
    if (!a0->field_10)
    {
        return 0;
    }
    else if (((char)AppOpenAd__CanShowAd(a0->field_10, 0) & 1))
    {
        if (!g_1eef418->field_e0)
            sub_f7da5c(g_1eef418);
        DateTime__get_Now(0);
        v0 = DateTime__get_Now(0);
        if (!g_1ef1d58->field_e0)
            sub_f7da5c(g_1ef1d58);
        DateTime__op_Addition(v0, TimeSpan__FromHours(0), 0);
    }
    else
    {
        return 0;
    }
}
```

## `AppOpenAdManager.ShowAppOpenAd` — RVA `0xc74e40`

- Decompiled symbol: `AppOpenAdManager_ShowAppOpenAd`
- Metadata signature: `public void ShowAppOpenAd() { }`
- Native interval: `204` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    long long field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1f085f8;
extern long long g_1f0da50;
extern char g_1fab38e;

void AppOpenAdManager_ShowAppOpenAd(struct_1 *a0)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab38e & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f085f8);
        sub_f7d92c(&g_1f0da50);
        g_1fab38e = 1;
    }
    if (a0->field_10 && ((char)AppOpenAd__CanShowAd(a0->field_10, 0) & 1))
    {
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        Debug__Log(g_1f0da50, 0);
        if (!a0->field_10)
            sub_f7db74(0);
    }
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__LogError();
    return;
}
```

## `AppOpenAdManager.RegisterEventHandlers` — RVA `0xc74f0c`

- Decompiled symbol: `AppOpenAdManager_RegisterEventHandlers`
- Metadata signature: `private void RegisterEventHandlers(AppOpenAd ad) { }`
- Native interval: `1000` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    long long field_0;
    long long field_8;
    long long field_10;
    long long field_18;
    long long field_20;
    long long field_28;
    long long field_30;
} struct_1;

extern long long g_1eebf78;
extern long long g_1eebf88;
extern long long g_1f04070;
extern long long g_1f04078;
extern long long g_1f04080;
extern long long g_1f04088;
extern long long g_1f04090;
extern long long g_1f04098;
extern char g_1fab38f;

void AppOpenAdManager_RegisterEventHandlers(unsigned long a0, long long a1, unsigned long a2)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    long long v15;  // x20
    long long v16;  // x0
    long long ptr[7];  // x0
    struct_0 *pos;  // x0
    long long v19;  // x20
    long long v20;  // x0
    long long p[7];  // x0
    struct_0 *off;  // x0
    long long v23;  // x20
    long long v24;  // x0
    unsigned long long v7;  // x21
    long long addr[7];  // x0
    struct_0 *idx4;  // x0
    long long v27;  // x20
    long long v28;  // x0
    long long ptr3[7];  // x0
    struct_0 *v30;  // x0
    long long v31;  // x0
    long long v32;  // x20
    long long ptr4[7];  // x0
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    struct_0 *idx;  // x0
    long long v11;  // x20
    long long v12;  // x0
    long long ptr5[7];  // x0
    struct_0 *index;  // x0
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
    if (!(g_1fab38f & 1))
    {
        sub_f7d92c(&g_1eebf78);
        sub_f7d92c(&g_1eebf88);
        sub_f7d92c("++");
        sub_f7d92c(&g_1f04070);
        sub_f7d92c(&g_1f04078);
        sub_f7d92c(&g_1f04080);
        sub_f7d92c(&g_1f04088);
        sub_f7d92c(&g_1f04090);
        sub_f7d92c(&g_1f04098);
        sub_f7d92c(";e");
        g_1fab38f = 1;
    }
    idx = g_1ef2c00;
    if (!g_1ef2c00->field_e0)
    {
        sub_f7da5c(g_1ef2c00);
        idx = g_1ef2c00;
    }
    v11 = idx->field_b8->field_8;
    if (!v11)
    {
        if (!idx->field_e0)
        {
            sub_f7da5c();
            idx = g_1ef2c00;
        }
        v12 = sub_f7db70(g_1eebf88);
        v11 = v12;
        sub_126041c(v12, idx->field_b8->field_0, g_1f04070, 0);
        ptr5 = g_1ef2c00->field_b8;
        ptr5[1] = v11;
        sub_f7d8d0((long long [7])&ptr5[1], v11);
    }
    if (!a1)
        sub_f7db74();
    AppOpenAd__add_OnAdPaid(a1, v11, 0);
    index = g_1ef2c00;
    if (!g_1ef2c00->field_e0)
    {
        sub_f7da5c(g_1ef2c00);
        index = g_1ef2c00;
    }
    v15 = index->field_b8->field_10;
    if (!v15)
    {
        if (!index->field_e0)
        {
            sub_f7da5c();
            index = g_1ef2c00;
        }
        v16 = sub_f7db70(g_1eee648);
        v15 = v16;
        Action__ctor(v16, index->field_b8->field_0, g_1f04078, 0);
        ptr = g_1ef2c00->field_b8;
        ptr[2] = v15;
        sub_f7d8d0((long long [7])&ptr[2], v15);
    }
    AppOpenAd__add_OnAdImpressionRecorded(a1, v15, 0);
    pos = g_1ef2c00;
    if (!g_1ef2c00->field_e0)
    {
        sub_f7da5c(g_1ef2c00);
        pos = g_1ef2c00;
    }
    v19 = pos->field_b8->field_18;
    if (!v19)
    {
        if (!pos->field_e0)
        {
            sub_f7da5c();
            pos = g_1ef2c00;
        }
        v20 = sub_f7db70(g_1eee648);
        v19 = v20;
        Action__ctor(v20, pos->field_b8->field_0, g_1f04080, 0);
        p = g_1ef2c00->field_b8;
        p[3] = v19;
        sub_f7d8d0((long long [7])&p[3], v19);
    }
    AppOpenAd__add_OnAdClicked(a1, v19, 0);
    off = g_1ef2c00;
    if (!g_1ef2c00->field_e0)
    {
        sub_f7da5c(g_1ef2c00);
        off = g_1ef2c00;
    }
    v23 = off->field_b8->field_20;
    if (!v23)
    {
        if (!off->field_e0)
        {
            sub_f7da5c();
            off = g_1ef2c00;
        }
        v24 = sub_f7db70(g_1eee648);
        v23 = v24;
        Action__ctor(v24, off->field_b8->field_0, g_1f04088, 0);
        addr = g_1ef2c00->field_b8;
        addr[4] = v23;
        sub_f7d8d0((long long [7])&addr[4], v23);
    }
    AppOpenAd__add_OnAdFullScreenContentOpened(a1, v23, 0);
    idx4 = g_1ef2c00;
    if (!g_1ef2c00->field_e0)
    {
        sub_f7da5c(g_1ef2c00);
        idx4 = g_1ef2c00;
    }
    v27 = idx4->field_b8->field_28;
    if (!v27)
    {
        if (!idx4->field_e0)
        {
            sub_f7da5c();
            idx4 = g_1ef2c00;
        }
        v28 = sub_f7db70(g_1eee648);
        v27 = v28;
        Action__ctor(v28, idx4->field_b8->field_0, g_1f04090, 0);
        ptr3 = g_1ef2c00->field_b8;
        ptr3[5] = v27;
        sub_f7d8d0((long long [7])&ptr3[5], v27);
    }
    AppOpenAd__add_OnAdFullScreenContentClosed(a1, v27, 0);
    v30 = g_1ef2c00;
    if (!g_1ef2c00->field_e0)
    {
        sub_f7da5c(g_1ef2c00);
        v30 = g_1ef2c00;
    }
    if (!v30->field_b8->field_30)
    {
        if (!v30->field_e0)
        {
            sub_f7da5c();
            v30 = g_1ef2c00;
        }
        v31 = sub_f7db70(g_1eebf78);
        v32 = v31;
        sub_126041c(v31, v30->field_b8->field_0, g_1f04098, 0);
        ptr4 = g_1ef2c00->field_b8;
        ptr4[6] = v32;
        sub_f7d8d0((long long [7])&ptr4[6], v32);
    }
}
```

## `AppOpenAdManager.<LoadAppOpenAd>b__8_0` — RVA `0xc752f4`

- Decompiled symbol: `AppOpenAdManager_LoadAppOpenAd_b__8_0`
- Metadata signature: `private void <LoadAppOpenAd>b__8_0(AppOpenAd ad, LoadAdError error) { }`
- Native interval: `336` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[360];
    struct struct_5 *field_168;
    unsigned long long field_170;
} struct_4;

typedef struct struct_2 {
    char padding_0[360];
    struct struct_3 *field_168;
    unsigned long long field_170;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    long long field_10;
} struct_1;

typedef struct struct_5 {
    unsigned long long field_0;
} struct_5;

typedef struct struct_3 {
    unsigned long long field_0;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1f08600;
extern long long g_1f11108;
extern char g_1fab391;

void AppOpenAdManager_LoadAppOpenAd_b__8_0(struct_1 *ptr, long long a1, struct_4 **a2)
{
    struct_2 **v0;  // x0
    unsigned long long v1;  // x1
    long long v2;  // x0
    struct_4 **v4;  // x0
    unsigned long v5;  // x1

    if (!(g_1fab391 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f11108);
        sub_f7d92c(&g_1f08600);
        g_1fab391 = 1;
    }
    if (a1 && !a2)
    {
        v0 = AppOpenAd__GetResponseInfo(a1, 0);
        if (v0)
        {
            v1 = *(v0)->field_170;
            *(v0)->field_168();
        }
        v2 = String__Concat(g_1f08600);
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        Debug__Log(v2, 0);
        ptr->field_10 = a1;
        AppOpenAdManager__RegisterEventHandlers(sub_f7d8d0((struct struct_1 *)&ptr->field_10, a1), a1, 0); /* do not return */
    }
    if (a2)
    {
        v4 = a2;
        v5 = *(a2)->field_170;
        *(a2)->field_168();
    }
    String__Concat(g_1f11108);
    if (g_1eef458->field_e0)
    {
        Debug__LogError();
        return;
    }
    sub_f7da5c(g_1eef458);
    Debug__LogError();
    return;
}
```

## `AppOpenAdManager.<>c.cctor` — RVA `0xc75444`

- Decompiled symbol: `AppOpenAdManager_c_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
extern char g_1fab392;

void AppOpenAdManager_c_cctor(void)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    long long v6;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab392 & 1))
    {
        sub_f7d92c(";e");
        g_1fab392 = 1;
    }
    v6 = sub_f7db70(g_1ef2c00);
    Object__ctor(v6, 0);
    g_1ef2c00->field_b8->field_0 = v6;
    sub_f7d8d0();
    return;
}
```

## `AppOpenAdManager.<>c.ctor` — RVA `0xc754ac`

- Decompiled symbol: `AppOpenAdManager_c_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long AppOpenAdManager_c_ctor(void)
{
    long long v0;  // x0

    v0 = Object__ctor();
    return Object__ctor();
}
```

## `AppOpenAdManager.<>c.<RegisterEventHandlers>b__7_0` — RVA `0xc754b4`

- Decompiled symbol: `AppOpenAdManager_c_RegisterEventHandlers_b__7_0`
- Metadata signature: `internal void <RegisterEventHandlers>b__7_0(AdValue adValue) { }`
- Native interval: `200` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    unsigned long long field_18;
    long long field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1ef0458;
extern long long g_1f08608;
extern char g_1fab393;

long long AppOpenAdManager_c_RegisterEventHandlers_b__7_0(unsigned long a0, struct_1 *ptr)
{
    long long v1;  // x0
    long long v2;  // x0
    unsigned long long v3;  // x0
    unsigned long v0;  // [bp-0x28]

    if (!(g_1fab393 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef0458);
        sub_f7d92c(&g_1f08608);
        g_1fab393 = 1;
    }
    if (ptr)
    {
        v0 = ptr->field_18;
        v1 = sub_f7da64(g_1ef0458, &v0);
        v2 = String__Format(g_1f08608, v1, ptr->field_20, 0);
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        v3 = Debug__Log(v2, 0);
        return Debug__Log(v2, 0);
    }
    sub_f7db74();
}
```

## `AppOpenAdManager.<>c.<RegisterEventHandlers>b__7_1` — RVA `0xc7557c`

- Decompiled symbol: `AppOpenAdManager_c_RegisterEventHandlers_b__7_1`
- Metadata signature: `internal void <RegisterEventHandlers>b__7_1() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1f08610;
extern char g_1fab394;

void AppOpenAdManager_c_RegisterEventHandlers_b__7_1(void)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab394 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f08610);
        g_1fab394 = 1;
    }
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__Log();
    return;
}
```

## `AppOpenAdManager.<>c.<RegisterEventHandlers>b__7_2` — RVA `0xc755e4`

- Decompiled symbol: `AppOpenAdManager_c_RegisterEventHandlers_b__7_2`
- Metadata signature: `internal void <RegisterEventHandlers>b__7_2() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1f08618;
extern char g_1fab395;

void AppOpenAdManager_c_RegisterEventHandlers_b__7_2(void)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab395 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f08618);
        g_1fab395 = 1;
    }
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__Log();
    return;
}
```

## `AppOpenAdManager.<>c.<RegisterEventHandlers>b__7_3` — RVA `0xc7564c`

- Decompiled symbol: `AppOpenAdManager_c_RegisterEventHandlers_b__7_3`
- Metadata signature: `internal void <RegisterEventHandlers>b__7_3() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1f085f0;
extern char g_1fab396;

void AppOpenAdManager_c_RegisterEventHandlers_b__7_3(void)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab396 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f085f0);
        g_1fab396 = 1;
    }
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__Log();
    return;
}
```

## `AppOpenAdManager.<>c.<RegisterEventHandlers>b__7_4` — RVA `0xc756b4`

- Decompiled symbol: `AppOpenAdManager_c_RegisterEventHandlers_b__7_4`
- Metadata signature: `internal void <RegisterEventHandlers>b__7_4() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1f085e8;
extern char g_1fab397;

void AppOpenAdManager_c_RegisterEventHandlers_b__7_4(void)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab397 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f085e8);
        g_1fab397 = 1;
    }
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__Log();
    return;
}
```

## `AppOpenAdManager.<>c.<RegisterEventHandlers>b__7_5` — RVA `0xc7571c`

- Decompiled symbol: `AppOpenAdManager_c_RegisterEventHandlers_b__7_5`
- Metadata signature: `internal void <RegisterEventHandlers>b__7_5(AdError error) { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[360];
    struct struct_2 *field_168;
    unsigned long long field_170;
} struct_1;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1f085e0;
extern char g_1fab398;

void AppOpenAdManager_c_RegisterEventHandlers_b__7_5(unsigned long a0, struct_1 **a1)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    struct_1 **v8;  // x0
    unsigned long v9;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab398 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f085e0);
        g_1fab398 = 1;
    }
    if (a1)
    {
        v8 = a1;
        v9 = *(a1)->field_170;
        *(a1)->field_168();
    }
    String__Concat(g_1f085e0);
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__LogError();
    return;
}
```
