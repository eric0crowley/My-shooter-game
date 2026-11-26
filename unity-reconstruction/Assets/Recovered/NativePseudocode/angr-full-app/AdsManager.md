# Native pseudocode: AdsManager

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AdsManager.Start` — RVA `0xc72a08`

- Decompiled symbol: `AdsManager_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `780` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AdsManager_Recovered` matched 6 offsets against `AdsManager` metadata (confidence 1.00).

```c
typedef struct AdsManager_Recovered {
    char padding_0[32];
    char isTest;
    char padding_21[7];
    long long AppOpen_ID;
    long long Banner_ID;
    long long Big_Banner_ID;
    long long interstitial_ID;
    long long Rewarded_ID;
} AdsManager_Recovered;

typedef struct struct_6 {
    char padding_0[184];
    struct struct_7 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_6;

typedef struct struct_7 {
    long long field_0;
    long long field_8;
} struct_7;

typedef struct struct_0 {
    char padding_0[32];
    char field_20;
    char padding_21[7];
    unsigned long long field_28;
    unsigned long long field_30;
    unsigned long long field_38;
    unsigned long long field_40;
    unsigned long long field_48;
} struct_0;

typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

typedef struct struct_5 {
    char padding_0[224];
    unsigned int field_e0;
} struct_5;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_1;

extern struct_1 *g_1eee700;
extern struct_5 *g_1ef0c58;
extern struct_6 *g_1ef2b90;
extern long long g_1f04000;
extern long long g_1f082a0;
extern long long g_1f092a0;
extern long long g_1f0bdb8;
extern long long g_1f115a0;
extern long long g_1f115a8;
extern long long g_1f115b0;
extern long long g_1f115b8;
extern char g_1fab36c;

void AdsManager_Start(struct_3 *a0)
{
    unsigned long long v7;  // x30
    unsigned long long v8;  // x24
    struct_3 *ptr;  // x0
    struct_3 *p;  // x0
    struct_6 *idx;  // x0
    long long v20;  // x20
    long long v21;  // x0
    long long addr[2];  // x0
    long long v25;  // x0
    unsigned long long v9;  // x23
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    struct_3 *ptr3;  // x0
    struct_3 *ptr4;  // x0
    struct_3 *ptr5;  // x0
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
    if (!(g_1fab36c & 1))
    {
        sub_f7d92c("9\t");
        sub_f7d92c(&g_1eee700);
        sub_f7d92c("[G");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f04000);
        sub_f7d92c(&g_1ef2b90);
        sub_f7d92c(&g_1f092a0);
        sub_f7d92c(&g_1f115a8);
        sub_f7d92c(&g_1f082a0);
        sub_f7d92c(&g_1f115b8);
        sub_f7d92c(&g_1f0bdb8);
        sub_f7d92c(&g_1f115a0);
        sub_f7d92c(&g_1f115b0);
        g_1fab36c = 1;
    }
    Time__set_timeScale(0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(g_1eee700->field_b8->field_0, 0, 0) & 1))
    {
        MonoBehaviour__print(g_1f092a0, 0);
        g_1eee700->field_b8->field_0 = a0;
        sub_f7d8d0(g_1eee700->field_b8, a0);
        if (a0->field_20)
        {
            ptr3 = a0;
            ptr3->field_28 = g_1f115b8;
            sub_f7d8d0((struct AdsManager_Recovered *)&ptr3->field_28, g_1f115b8);
            ptr4 = a0;
            ptr4->field_30 = g_1f115b0;
            sub_f7d8d0((struct AdsManager_Recovered *)&ptr4->field_30, g_1f115b0);
            ptr5 = a0;
            ptr5->field_38 = g_1f115b0;
            sub_f7d8d0((struct AdsManager_Recovered *)&ptr5->field_38, g_1f115b0);
            ptr = a0;
            ptr->field_40 = g_1f115a0;
            sub_f7d8d0((struct AdsManager_Recovered *)&ptr->field_40, g_1f115a0);
            p = a0;
            p->field_48 = g_1f115a8;
            sub_f7d8d0((struct AdsManager_Recovered *)&p->field_48, g_1f115a8);
        }
        idx = g_1ef2b90;
        if (!g_1ef2b90->field_e0)
        {
            sub_f7da5c(g_1ef2b90);
            idx = g_1ef2b90;
        }
        v20 = idx->field_b8->field_8;
        if (!v20)
        {
            if (!idx->field_e0)
            {
                sub_f7da5c();
                idx = g_1ef2b90;
            }
            v21 = sub_f7db70(g_1eec028);
            v20 = v21;
            sub_126041c(v21, idx->field_b8->field_0, g_1f04000, 0);
            addr = g_1ef2b90->field_b8;
            addr[1] = v20;
            sub_f7d8d0((long long [2])&addr[1], v20);
        }
        if (!g_1ef0948->field_e0)
            sub_f7da5c(g_1ef0948);
        MobileAds__Initialize(v20, 0);
        if (PlayerPrefs__GetInt(g_1f082a0, 0) != 1)
            AdsManager__RequestBanner(a0);
        MonoBehaviour__StartCoroutine(a0, AdsManager__LoadInter(a0), 0);
        MonoBehaviour__StartCoroutine(a0, AdsManager__LoadRewarded(a0), 0);
        v25 = Component__get_gameObject(a0, 0);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        Object__DontDestroyOnLoad(v25, 0);
    }
}
```

## `AdsManager.RequestBanner` — RVA `0xc72d14`

- Decompiled symbol: `AdsManager_RequestBanner`
- Metadata signature: `private void RequestBanner() { }`
- Native interval: `284` bytes
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
} struct_1;

extern long long g_1eeea58;
extern long long g_1ef2b88;
extern long long g_1f07218;
extern char g_1fab371;

void AdsManager_RequestBanner(long long *ptr)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    long long v16;  // x20
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    struct_0 *v12;  // x0
    long long v13;  // x0
    long long v14;  // x22
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
    if (!(g_1fab371 & 1))
    {
        sub_f7d92c("}+");
        sub_f7d92c(&g_1eeea58);
        sub_f7d92c(&g_1ef2b88);
        sub_f7d92c(&g_1f07218);
        g_1fab371 = 1;
    }
    MonoBehaviour__print(g_1f07218, 0);
    v12 = g_1eee6c8;
    if (!g_1eee6c8->field_e0)
    {
        sub_f7da5c(g_1eee6c8);
        v12 = g_1eee6c8;
    }
    v13 = sub_f7db70(g_1eeea58);
    v14 = v13;
    BannerView__ctor(v13, ptr[6], v12->field_b8->field_0, 3, 0);
    ptr[10] = v14;
    sub_f7d8d0(ptr + 10, v14);
    v16 = sub_f7db70(g_1ef2b88);
    AdRequest_Builder__ctor(v16, 0);
    if (v16)
        AdRequest_Builder__Build(v16, 0);
    sub_f7db74();
}
```

## `AdsManager.LoadInter` — RVA `0xc72e30`

- Decompiled symbol: `AdsManager_LoadInter`
- Metadata signature: `private IEnumerator LoadInter() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef2b98;
extern char g_1fab36f;

struct_0 * AdsManager_LoadInter(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab36f & 1))
    {
        sub_f7d92c(&g_1ef2b98);
        g_1fab36f = 1;
    }
    v0 = sub_f7db70(g_1ef2b98);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `AdsManager.LoadRewarded` — RVA `0xc72e9c`

- Decompiled symbol: `AdsManager_LoadRewarded`
- Metadata signature: `private IEnumerator LoadRewarded() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef2ba0;
extern char g_1fab370;

struct_0 * AdsManager_LoadRewarded(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab370 & 1))
    {
        sub_f7d92c(&g_1ef2ba0);
        g_1fab370 = 1;
    }
    v0 = sub_f7db70(g_1ef2ba0);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `AdsManager.LoadApOpen` — RVA `0xc72f08`

- Decompiled symbol: `AdsManager_LoadApOpen`
- Metadata signature: `public void LoadApOpen() { }`
- Native interval: `100` bytes
- Result: `pseudocode`

```c
extern long long g_1f0d458;
extern char g_1fab36d;

unsigned long long AdsManager_LoadApOpen(void)
{
    unsigned long long v0;  // x0
    unsigned long long v1;  // x0

    if (!(g_1fab36d & 1))
    {
        sub_f7d92c(&g_1f0d458);
        g_1fab36d = 1;
    }
    v0 = PlayerPrefs__GetInt(g_1f0d458, 0);
    if ((unsigned int)v0 == 149)
        return v0;
    v1 = AppOpenAdManager__get_Instance();
    if (!v1)
        return v1;
    AppOpenAdManager__LoadAppOpenAd(); /* do not return */
}
```

## `AdsManager.loading_Screen` — RVA `0xc73138`

- Decompiled symbol: `AdsManager_loading_Screen`
- Metadata signature: `private IEnumerator loading_Screen() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

extern long long g_1ef2ba8;
extern char g_1fab36e;

struct_0 * AdsManager_loading_Screen(void)
{
    struct_0 *ptr;  // x0

    if (!(g_1fab36e & 1))
    {
        sub_f7d92c(&g_1ef2ba8);
        g_1fab36e = 1;
    }
    ptr = sub_f7db70(g_1ef2ba8);
    Object__ctor(ptr, 0);
    ptr->field_10 = 0;
    return ptr;
}
```

## `AdsManager.<loading_Screen>d__13.ctor` — RVA `0xc73190`

- Decompiled symbol: `AdsManager_loading_Screen_d__13_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void AdsManager_loading_Screen_d__13_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `AdsManager.Call_Load_Interstitial` — RVA `0xc731b8`

- Decompiled symbol: `AdsManager_Call_Load_Interstitial`
- Metadata signature: `public void Call_Load_Interstitial() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
void AdsManager_Call_Load_Interstitial(long long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    AdsManager__LoadInter(a0);
    MonoBehaviour__StartCoroutine();
    return;
}
```

## `AdsManager.Call_Load_Rewarded` — RVA `0xc731d8`

- Decompiled symbol: `AdsManager_Call_Load_Rewarded`
- Metadata signature: `public void Call_Load_Rewarded() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
void AdsManager_Call_Load_Rewarded(long long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    AdsManager__LoadRewarded(a0);
    MonoBehaviour__StartCoroutine();
    return;
}
```

## `AdsManager.<LoadInter>d__16.ctor` — RVA `0xc731f8`

- Decompiled symbol: `AdsManager_LoadInter_d__16_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void AdsManager_LoadInter_d__16_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `AdsManager.<LoadRewarded>d__17.ctor` — RVA `0xc73220`

- Decompiled symbol: `AdsManager_LoadRewarded_d__17_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void AdsManager_LoadRewarded_d__17_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `AdsManager.ShowBanner` — RVA `0xc73248`

- Decompiled symbol: `AdsManager_ShowBanner`
- Metadata signature: `public void ShowBanner() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long AdsManager_ShowBanner(long long *a0)
{
    unsigned long v0;  // x0

    v0 = (unsigned long long)AdsManager__RequestBanner(a0);
    return (unsigned long long)AdsManager__RequestBanner(a0);
}
```

## `AdsManager.DestroyBanner` — RVA `0xc7324c`

- Decompiled symbol: `AdsManager_DestroyBanner`
- Metadata signature: `public void DestroyBanner() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[80];
    unsigned long long field_50;
} struct_0;

void AdsManager_DestroyBanner(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (!a0->field_50)
        sub_f7db74(0);
}
```

## `AdsManager.Request_Big_Banner` — RVA `0xc73268`

- Decompiled symbol: `AdsManager_Request_Big_Banner`
- Metadata signature: `private void Request_Big_Banner() { }`
- Native interval: `252` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[8];
    long long field_8;
} struct_0;

extern long long g_1eeea58;
extern long long g_1ef2b88;
extern char g_1fab372;

void AdsManager_Request_Big_Banner(long long *ptr)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    long long v16;  // x20
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    struct_1 *v12;  // x0
    long long v13;  // x0
    long long v14;  // x22
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
    if (!(g_1fab372 & 1))
    {
        sub_f7d92c("}+");
        sub_f7d92c(&g_1eeea58);
        sub_f7d92c(&g_1ef2b88);
        g_1fab372 = 1;
    }
    v12 = g_1eee6c8;
    if (!g_1eee6c8->field_e0)
    {
        sub_f7da5c(g_1eee6c8);
        v12 = g_1eee6c8;
    }
    v13 = sub_f7db70(g_1eeea58);
    v14 = v13;
    BannerView__ctor(v13, ptr[7], v12->field_b8->field_8, 5, 0);
    ptr[11] = v14;
    sub_f7d8d0(ptr + 11, v14);
    v16 = sub_f7db70(g_1ef2b88);
    AdRequest_Builder__ctor(v16, 0);
    if (v16)
        AdRequest_Builder__Build(v16, 0);
    sub_f7db74();
}
```

## `AdsManager.Show_Big_Banner` — RVA `0xc73364`

- Decompiled symbol: `AdsManager_Show_Big_Banner`
- Metadata signature: `public void Show_Big_Banner() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long AdsManager_Show_Big_Banner(long long *a0)
{
    AdsManager__Request_Big_Banner(a0); /* do not return */
}
```

## `AdsManager.Destroy_Big_Banner` — RVA `0xc73368`

- Decompiled symbol: `AdsManager_Destroy_Big_Banner`
- Metadata signature: `public void Destroy_Big_Banner() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[88];
    unsigned long long field_58;
} struct_0;

void AdsManager_Destroy_Big_Banner(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (!a0->field_58)
        sub_f7db74(0);
}
```

## `AdsManager.RequestInterstitial` — RVA `0xc73384`

- Decompiled symbol: `AdsManager_RequestInterstitial`
- Metadata signature: `private void RequestInterstitial() { }`
- Native interval: `360` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AdsManager_Recovered` matched 2 offsets against `AdsManager` metadata (confidence 1.00).

```c
typedef struct struct_2 {
    char padding_0[16];
    long long field_10;
} struct_2;

typedef struct AdsManager_Recovered {
    char padding_0[64];
    unsigned long long interstitial_ID;
    char padding_48[24];
    long long interstitialAd;
} AdsManager_Recovered;

typedef struct struct_3 {
    char padding_0[184];
    struct struct_4 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_3;

typedef struct struct_4 {
    long long field_0;
    char padding_8[8];
    long long field_10;
    long long field_18;
    long long field_20;
    long long field_28;
    long long field_30;
    long long field_38;
} struct_4;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern char g_10734ec;
extern long long g_1eebf78;
extern long long g_1eebf88;
extern long long g_1eec120;
extern struct_0 *g_1eef458;
extern struct_3 *g_1ef2b90;
extern long long g_1ef6e68;
extern long long g_1efbae0;
extern long long g_1f03fa0;
extern long long g_1f03fa8;
extern long long g_1f03fb0;
extern long long g_1f03fb8;
extern long long g_1f03fc0;
extern long long g_1f03fc8;
extern long long g_1f0bde0;
extern char g_1fab373;
extern char g_1fab374;

void AdsManager_RequestInterstitial(struct_1 *a0)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    long long *v16;  // x22
    long long v17;  // x1
    struct_2 *v18;  // x21
    long long v19;  // x0
    long long v20;  // x19
    struct_3 *index;  // x0
    long long v22;  // x20
    long long v23;  // x0
    long long p[8];  // x0
    struct_3 *pos;  // x0
    long long *v8;  // x22
    long long v26;  // x20
    long long v27;  // x0
    long long addr[8];  // x0
    struct_3 *off;  // x0
    long long v30;  // x20
    long long v31;  // x0
    long long ptr3[8];  // x0
    struct_3 *idx4;  // x0
    long long v34;  // x20
    long long v35;  // x0
    struct_2 *v9;  // x21
    long long ptr4[8];  // x0
    struct_3 *idx5;  // x0
    long long v38;  // x20
    long long v39;  // x0
    long long ptr5[8];  // x0
    struct_3 *v41;  // x0
    long long v42;  // x0
    long long v43;  // x20
    long long ptr6[8];  // x0
    unsigned long v10;  // x20
    struct_1 *v11;  // x19
    struct_1 *ptr7;  // x19
    struct_1 *v13;  // x21
    struct_1 *ptr;  // x21
    unsigned long v15;  // x20
    unsigned long v0;  // [bp-0x30], Other Possible Types: unsigned long long
    unsigned long long v1;  // [bp-0x28]
    long long *v2;  // [bp-0x20]
    struct_2 *v3;  // [bp-0x18]
    unsigned long v4;  // [bp-0x10]
    struct_1 *v5;  // [bp-0x8]

    v0 = v6;
    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    ptr7 = a0;
    if (!(g_1fab373 & 1))
    {
        sub_f7d92c(&g_1eec120);
        sub_f7d92c("{+");
        sub_f7d92c(&g_1efbae0);
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef6e68);
        sub_f7d92c("A<");
        sub_f7d92c(&g_1f0bde0);
        g_1fab373 = 1;
    }
    v13 = ptr7;
    ptr = &v13->field_60;
    v15 = *((long long *)&ptr->padding_0[32]);
    if (v13->field_60)
    {
        InterstitialAd__Destroy(v13->field_60, 0);
        *((long long *)&ptr->padding_0[0]) = 0;
        sub_f7d8d0(ptr, 0);
    }
    v16 = &g_1f0bde0;
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__Log(g_1f0bde0, 0);
    v17 = 0;
    v18 = sub_f7db70(g_1eee6c0);
    AdRequest__ctor(v18, 0);
    if (v18 && v18->field_10)
    {
        sub_13d6008(v18->field_10, g_1f152f0, g_1ef6e68);
        v19 = sub_f7db70(g_1eec120);
        sub_12633ac(v19, ptr7, g_1efbae0, 0);
        InterstitialAd__Load(v15, v18, v19, 0);
        v17 = ptr7->field_60;
        v15 = v4;
        ptr7 = v5;
        v16 = v2;
        v18 = v3;
        vvar_111{r256|8b} = v0;
    }
    else
    {
        vvar_280{r256|8b} = (int)&g_10734ec;
        sub_f7db74();
    }
    v0 = vvar_111{r256|8b};
    v2 = v16;
    v3 = v18;
    v4 = v15;
    v5 = ptr7;
    v20 = v17;
    if (!(g_1fab374 & 1))
    {
        sub_f7d92c(&g_1eebf78);
        sub_f7d92c(&g_1eebf88);
        sub_f7d92c("++");
        sub_f7d92c(&g_1f03fa0);
        sub_f7d92c(&g_1f03fa8);
        sub_f7d92c(&g_1f03fb0);
        sub_f7d92c(&g_1f03fb8);
        sub_f7d92c(&g_1f03fc0);
        sub_f7d92c(&g_1f03fc8);
        sub_f7d92c(&g_1ef2b90);
        g_1fab374 = 1;
    }
    index = g_1ef2b90;
    if (!g_1ef2b90->field_e0)
    {
        sub_f7da5c(g_1ef2b90);
        index = g_1ef2b90;
    }
    v22 = index->field_b8->field_10;
    if (!v22)
    {
        if (!index->field_e0)
        {
            sub_f7da5c();
            index = g_1ef2b90;
        }
        v23 = sub_f7db70(g_1eebf88);
        v22 = v23;
        sub_126041c(v23, index->field_b8->field_0, g_1f03fa0, 0);
        p = g_1ef2b90->field_b8;
        p[2] = v22;
        sub_f7d8d0((long long [8])&p[2], v22);
    }
    if (!v20)
        sub_f7db74();
    InterstitialAd__add_OnAdPaid(v20, v22, 0);
    pos = g_1ef2b90;
    if (!g_1ef2b90->field_e0)
    {
        sub_f7da5c(g_1ef2b90);
        pos = g_1ef2b90;
    }
    v26 = pos->field_b8->field_18;
    if (!v26)
    {
        if (!pos->field_e0)
        {
            sub_f7da5c();
            pos = g_1ef2b90;
        }
        v27 = sub_f7db70(g_1eee648);
        v26 = v27;
        Action__ctor(v27, pos->field_b8->field_0, g_1f03fa8, 0);
        addr = g_1ef2b90->field_b8;
        addr[3] = v26;
        sub_f7d8d0((long long [8])&addr[3], v26);
    }
    InterstitialAd__add_OnAdImpressionRecorded(v20, v26, 0);
    off = g_1ef2b90;
    if (!g_1ef2b90->field_e0)
    {
        sub_f7da5c(g_1ef2b90);
        off = g_1ef2b90;
    }
    v30 = off->field_b8->field_20;
    if (!v30)
    {
        if (!off->field_e0)
        {
            sub_f7da5c();
            off = g_1ef2b90;
        }
        v31 = sub_f7db70(g_1eee648);
        v30 = v31;
        Action__ctor(v31, off->field_b8->field_0, g_1f03fb0, 0);
        ptr3 = g_1ef2b90->field_b8;
        ptr3[4] = v30;
        sub_f7d8d0((long long [8])&ptr3[4], v30);
    }
    InterstitialAd__add_OnAdClicked(v20, v30, 0);
    idx4 = g_1ef2b90;
    if (!g_1ef2b90->field_e0)
    {
        sub_f7da5c(g_1ef2b90);
        idx4 = g_1ef2b90;
    }
    v34 = idx4->field_b8->field_28;
    if (!v34)
    {
        if (!idx4->field_e0)
        {
            sub_f7da5c();
            idx4 = g_1ef2b90;
        }
        v35 = sub_f7db70(g_1eee648);
        v34 = v35;
        Action__ctor(v35, idx4->field_b8->field_0, g_1f03fb8, 0);
        ptr4 = g_1ef2b90->field_b8;
        ptr4[5] = v34;
        sub_f7d8d0((long long [8])&ptr4[5], v34);
    }
    InterstitialAd__add_OnAdFullScreenContentOpened(v20, v34, 0);
    idx5 = g_1ef2b90;
    if (!g_1ef2b90->field_e0)
    {
        sub_f7da5c(g_1ef2b90);
        idx5 = g_1ef2b90;
    }
    v38 = idx5->field_b8->field_30;
    if (!v38)
    {
        if (!idx5->field_e0)
        {
            sub_f7da5c();
            idx5 = g_1ef2b90;
        }
        v39 = sub_f7db70(g_1eee648);
        v38 = v39;
        Action__ctor(v39, idx5->field_b8->field_0, g_1f03fc0, 0);
        ptr5 = g_1ef2b90->field_b8;
        ptr5[6] = v38;
        sub_f7d8d0((long long [8])&ptr5[6], v38);
    }
    InterstitialAd__add_OnAdFullScreenContentClosed(v20, v38, 0);
    v41 = g_1ef2b90;
    if (!g_1ef2b90->field_e0)
    {
        sub_f7da5c(g_1ef2b90);
        v41 = g_1ef2b90;
    }
    if (!v41->field_b8->field_38)
    {
        if (!v41->field_e0)
        {
            sub_f7da5c();
            v41 = g_1ef2b90;
        }
        v42 = sub_f7db70(g_1eebf78);
        v43 = v42;
        sub_126041c(v42, v41->field_b8->field_0, g_1f03fc8, 0);
        ptr6 = g_1ef2b90->field_b8;
        ptr6[7] = v43;
        sub_f7d8d0((long long [8])&ptr6[7], v43);
    }
}
```

## `AdsManager.RegisterEventHandlers` — RVA `0xc734ec`

- Decompiled symbol: `AdsManager_RegisterEventHandlers`
- Metadata signature: `private void RegisterEventHandlers(InterstitialAd ad) { }`
- Native interval: `1000` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x10734ec: str x30, [sp, #-0x30]!
// 0x10734f0: stp x22, x21, [sp, #0x10]
// 0x10734f4: stp x20, x19, [sp, #0x20]
// 0x10734f8: adrp x20, #0x1fab000
// 0x10734fc: adrp x22, #0x1e8d000
// 0x1073500: ldrb w8, [x20, #0x374]
// 0x1073504: ldr x22, [x22, #0x698]
// 0x1073508: mov x19, x1
// 0x107350c: tbnz w8, #0, #0x1073590
// 0x1073510: adrp x0, #0x1e8d000
// 0x1073514: ldr x0, [x0, #0x768]
// 0x1073518: bl #0xf7d92c
// 0x107351c: adrp x0, #0x1e8d000
// 0x1073520: ldr x0, [x0, #0x770]
// 0x1073524: bl #0xf7d92c
// 0x1073528: adrp x0, #0x1e8c000
// 0x107352c: ldr x0, [x0, #0x40]
// 0x1073530: bl #0xf7d92c
// 0x1073534: adrp x0, #0x1e8d000
// 0x1073538: ldr x0, [x0, #0x778]
// 0x107353c: bl #0xf7d92c
// 0x1073540: adrp x0, #0x1e8d000
// 0x1073544: ldr x0, [x0, #0x780]
// 0x1073548: bl #0xf7d92c
// 0x107354c: adrp x0, #0x1e8d000
// 0x1073550: ldr x0, [x0, #0x788]
// 0x1073554: bl #0xf7d92c
// 0x1073558: adrp x0, #0x1e8d000
// 0x107355c: ldr x0, [x0, #0x790]
// 0x1073560: bl #0xf7d92c
// 0x1073564: adrp x0, #0x1e8d000
// 0x1073568: ldr x0, [x0, #0x798]
// 0x107356c: bl #0xf7d92c
// 0x1073570: adrp x0, #0x1e8d000
// 0x1073574: ldr x0, [x0, #0x7a0]
// 0x1073578: bl #0xf7d92c
// 0x107357c: adrp x0, #0x1e8d000
// 0x1073580: ldr x0, [x0, #0x698]
// 0x1073584: bl #0xf7d92c
// 0x1073588: mov w8, #1
// 0x107358c: strb w8, [x20, #0x374]
// 0x1073590: ldr x0, [x22]
// 0x1073594: ldr w8, [x0, #0xe0]
// 0x1073598: cbnz w8, #0x10735a4
// 0x107359c: bl #0xf7da5c
// 0x10735a0: ldr x0, [x22]
// 0x10735a4: ldr x8, [x0, #0xb8]
// 0x10735a8: ldr x20, [x8, #0x10]
// 0x10735ac: cbnz x20, #0x1073608
// 0x10735b0: ldr w8, [x0, #0xe0]
// 0x10735b4: cbnz w8, #0x10735c0
// 0x10735b8: bl #0xf7da5c
// 0x10735bc: ldr x0, [x22]
// 0x10735c0: adrp x9, #0x1e8d000
// 0x10735c4: ldr x8, [x0, #0xb8]
// 0x10735c8: ldr x9, [x9, #0x770]
// 0x10735cc: ldr x21, [x8]
// 0x10735d0: ldr x0, [x9]
// 0x10735d4: bl #0xf7db70
// 0x10735d8: adrp x8, #0x1e8d000
// 0x10735dc: ldr x8, [x8, #0x778]
// 0x10735e0: mov x1, x21
// 0x10735e4: mov x3, xzr
// 0x10735e8: mov x20, x0
// 0x10735ec: ldr x2, [x8]
// 0x10735f0: bl #0x126041c
// 0x10735f4: ldr x8, [x22]
// 0x10735f8: mov x1, x20
// 0x10735fc: ldr x0, [x8, #0xb8]
// 0x1073600: str x20, [x0, #0x10]!
// 0x1073604: bl #0xf7d8d0
// 0x1073608: cbz x19, #0x10738d0
// 0x107360c: mov x0, x19
// 0x1073610: mov x1, x20
// 0x1073614: mov x2, xzr
// 0x1073618: bl #0x17aa944
// 0x107361c: ldr x0, [x22]
// 0x1073620: ldr w8, [x0, #0xe0]
// 0x1073624: cbnz w8, #0x1073630
// 0x1073628: bl #0xf7da5c
// 0x107362c: ldr x0, [x22]
// 0x1073630: ldr x8, [x0, #0xb8]
// 0x1073634: ldr x20, [x8, #0x18]
// 0x1073638: cbnz x20, #0x1073694
// 0x107363c: ldr w8, [x0, #0xe0]
// 0x1073640: cbnz w8, #0x107364c
// 0x1073644: bl #0xf7da5c
// 0x1073648: ldr x0, [x22]
// 0x107364c: adrp x9, #0x1e8c000
// 0x1073650: ldr x8, [x0, #0xb8]
// 0x1073654: ldr x9, [x9, #0x40]
// 0x1073658: ldr x21, [x8]
// 0x107365c: ldr x0, [x9]
// 0x1073660: bl #0xf7db70
// 0x1073664: adrp x8, #0x1e8d000
// 0x1073668: ldr x8, [x8, #0x780]
// 0x107366c: mov x1, x21
// 0x1073670: mov x3, xzr
// 0x1073674: mov x20, x0
// 0x1073678: ldr x2, [x8]
// 0x107367c: bl #0x18e3eac
// 0x1073680: ldr x8, [x22]
// 0x1073684: mov x1, x20
// 0x1073688: ldr x0, [x8, #0xb8]
// 0x107368c: str x20, [x0, #0x18]!
// 0x1073690: bl #0xf7d8d0
// 0x1073694: mov x0, x19
// 0x1073698: mov x1, x20
// 0x107369c: mov x2, xzr
// 0x10736a0: bl #0x17aabdc
// 0x10736a4: ldr x0, [x22]
// 0x10736a8: ldr w8, [x0, #0xe0]
// 0x10736ac: cbnz w8, #0x10736b8
// 0x10736b0: bl #0xf7da5c
// 0x10736b4: ldr x0, [x22]
// 0x10736b8: ldr x8, [x0, #0xb8]
// 0x10736bc: ldr x20, [x8, #0x20]
// 0x10736c0: cbnz x20, #0x107371c
// 0x10736c4: ldr w8, [x0, #0xe0]
// 0x10736c8: cbnz w8, #0x10736d4
// 0x10736cc: bl #0xf7da5c
// 0x10736d0: ldr x0, [x22]
// 0x10736d4: adrp x9, #0x1e8c000
// 0x10736d8: ldr x8, [x0, #0xb8]
// 0x10736dc: ldr x9, [x9, #0x40]
// 0x10736e0: ldr x21, [x8]
// 0x10736e4: ldr x0, [x9]
// 0x10736e8: bl #0xf7db70
// 0x10736ec: adrp x8, #0x1e8d000
// 0x10736f0: ldr x8, [x8, #0x788]
// 0x10736f4: mov x1, x21
// 0x10736f8: mov x3, xzr
// 0x10736fc: mov x20, x0
// 0x1073700: ldr x2, [x8]
// 0x1073704: bl #0x18e3eac
// 0x1073708: ldr x8, [x22]
// 0x107370c: mov x1, x20
// 0x1073710: ldr x0, [x8, #0xb8]
// 0x1073714: str x20, [x0, #0x20]!
// 0x1073718: bl #0xf7d8d0
// 0x107371c: mov x0, x19
// 0x1073720: mov x1, x20
// 0x1073724: mov x2, xzr
// 0x1073728: bl #0x17aaaa4
// 0x107372c: ldr x0, [x22]
// 0x1073730: ldr w8, [x0, #0xe0]
// 0x1073734: cbnz w8, #0x1073740
// 0x1073738: bl #0xf7da5c
// 0x107373c: ldr x0, [x22]
// 0x1073740: ldr x8, [x0, #0xb8]
// 0x1073744: ldr x20, [x8, #0x28]
// 0x1073748: cbnz x20, #0x10737a4
// 0x107374c: ldr w8, [x0, #0xe0]
// 0x1073750: cbnz w8, #0x107375c
// 0x1073754: bl #0xf7da5c
// 0x1073758: ldr x0, [x22]
// 0x107375c: adrp x9, #0x1e8c000
// 0x1073760: ldr x8, [x0, #0xb8]
// 0x1073764: ldr x9, [x9, #0x40]
// 0x1073768: ldr x21, [x8]
// 0x107376c: ldr x0, [x9]
// 0x1073770: bl #0xf7db70
// 0x1073774: adrp x8, #0x1e8d000
// 0x1073778: ldr x8, [x8, #0x790]
// 0x107377c: mov x1, x21
// 0x1073780: mov x3, xzr
// 0x1073784: mov x20, x0
// 0x1073788: ldr x2, [x8]
// 0x107378c: bl #0x18e3eac
// 0x1073790: ldr x8, [x22]
// 0x1073794: mov x1, x20
// 0x1073798: ldr x0, [x8, #0xb8]
// 0x107379c: str x20, [x0, #0x28]!
// 0x10737a0: bl #0xf7d8d0
// 0x10737a4: mov x0, x19
// 0x10737a8: mov x1, x20
// 0x10737ac: mov x2, xzr
// 0x10737b0: bl #0x17aad14
// 0x10737b4: ldr x0, [x22]
// 0x10737b8: ldr w8, [x0, #0xe0]
// 0x10737bc: cbnz w8, #0x10737c8
// 0x10737c0: bl #0xf7da5c
// 0x10737c4: ldr x0, [x22]
// 0x10737c8: ldr x8, [x0, #0xb8]
// 0x10737cc: ldr x20, [x8, #0x30]
// 0x10737d0: cbnz x20, #0x107382c
// 0x10737d4: ldr w8, [x0, #0xe0]
// 0x10737d8: cbnz w8, #0x10737e4
// 0x10737dc: bl #0xf7da5c
// 0x10737e0: ldr x0, [x22]
// 0x10737e4: adrp x9, #0x1e8c000
// 0x10737e8: ldr x8, [x0, #0xb8]
// 0x10737ec: ldr x9, [x9, #0x40]
// 0x10737f0: ldr x21, [x8]
// 0x10737f4: ldr x0, [x9]
// 0x10737f8: bl #0xf7db70
// 0x10737fc: adrp x8, #0x1e8d000
// 0x1073800: ldr x8, [x8, #0x798]
// 0x1073804: mov x1, x21
// 0x1073808: mov x3, xzr
// 0x107380c: mov x20, x0
// 0x1073810: ldr x2, [x8]
// 0x1073814: bl #0x18e3eac
// 0x1073818: ldr x8, [x22]
// 0x107381c: mov x1, x20
// 0x1073820: ldr x0, [x8, #0xb8]
// 0x1073824: str x20, [x0, #0x30]!
// 0x1073828: bl #0xf7d8d0
// 0x107382c: mov x0, x19
// 0x1073830: mov x1, x20
// 0x1073834: mov x2, xzr
// 0x1073838: bl #0x17aae4c
// 0x107383c: ldr x0, [x22]
// 0x1073840: ldr w8, [x0, #0xe0]
// 0x1073844: cbnz w8, #0x1073850
// 0x1073848: bl #0xf7da5c
// 0x107384c: ldr x0, [x22]
// 0x1073850: ldr x8, [x0, #0xb8]
// 0x1073854: ldr x20, [x8, #0x38]
// 0x1073858: cbnz x20, #0x10738b4
// 0x107385c: ldr w8, [x0, #0xe0]
// 0x1073860: cbnz w8, #0x107386c
// 0x1073864: bl #0xf7da5c
// 0x1073868: ldr x0, [x22]
// 0x107386c: adrp x9, #0x1e8d000
// 0x1073870: ldr x8, [x0, #0xb8]
// 0x1073874: ldr x9, [x9, #0x768]
// 0x1073878: ldr x21, [x8]
// 0x107387c: ldr x0, [x9]
// 0x1073880: bl #0xf7db70
// 0x1073884: adrp x8, #0x1e8d000
// 0x1073888: ldr x8, [x8, #0x7a0]
// 0x107388c: mov x1, x21
// 0x1073890: mov x3, xzr
// 0x1073894: mov x20, x0
// 0x1073898: ldr x2, [x8]
// 0x107389c: bl #0x126041c
// 0x10738a0: ldr x8, [x22]
// 0x10738a4: mov x1, x20
// 0x10738a8: ldr x0, [x8, #0xb8]
// 0x10738ac: str x20, [x0, #0x38]!
// 0x10738b0: bl #0xf7d8d0
// 0x10738b4: mov x0, x19
// 0x10738b8: mov x1, x20
// 0x10738bc: ldp x20, x19, [sp, #0x20]
// 0x10738c0: ldp x22, x21, [sp, #0x10]
// 0x10738c4: mov x2, xzr
// 0x10738c8: ldr x30, [sp], #0x30
// 0x10738cc: b #0x17aaf84
// 0x10738d0: bl #0xf7db74
```

## `AdsManager.Request_Rewarded` — RVA `0xc738d4`

- Decompiled symbol: `AdsManager_Request_Rewarded`
- Metadata signature: `private void Request_Rewarded() { }`
- Native interval: `360` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AdsManager_Recovered` matched 2 offsets against `AdsManager` metadata (confidence 1.00).

```c
typedef struct struct_2 {
    char padding_0[16];
    long long field_10;
} struct_2;

typedef struct AdsManager_Recovered {
    char padding_0[72];
    unsigned long long Rewarded_ID;
    char padding_50[24];
    long long rewardedAd;
} AdsManager_Recovered;

typedef struct struct_3 {
    char padding_0[184];
    struct struct_4 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_3;

typedef struct struct_4 {
    long long field_0;
    char padding_8[56];
    long long field_40;
    long long field_48;
    long long field_50;
    long long field_58;
    long long field_60;
    long long field_68;
} struct_4;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern char g_1073a3c;
extern long long g_1eebf78;
extern long long g_1eebf88;
extern long long g_1eec130;
extern struct_0 *g_1eef458;
extern struct_3 *g_1ef2b90;
extern long long g_1ef6e68;
extern long long g_1efbae8;
extern long long g_1f03fd0;
extern long long g_1f03fd8;
extern long long g_1f03fe0;
extern long long g_1f03fe8;
extern long long g_1f03ff0;
extern long long g_1f03ff8;
extern long long g_1f0bde8;
extern char g_1fab375;
extern char g_1fab376;

void AdsManager_Request_Rewarded(struct_1 *a0)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    long long *v16;  // x22
    long long v17;  // x1
    struct_2 *v18;  // x21
    long long v19;  // x0
    long long v20;  // x19
    struct_3 *index;  // x0
    long long v22;  // x20
    long long v23;  // x0
    long long p[14];  // x0
    struct_3 *pos;  // x0
    long long *v8;  // x22
    long long v26;  // x20
    long long v27;  // x0
    long long addr[14];  // x0
    struct_3 *off;  // x0
    long long v30;  // x20
    long long v31;  // x0
    long long ptr3[14];  // x0
    struct_3 *idx4;  // x0
    long long v34;  // x20
    long long v35;  // x0
    struct_2 *v9;  // x21
    long long ptr4[14];  // x0
    struct_3 *idx5;  // x0
    long long v38;  // x20
    long long v39;  // x0
    long long ptr5[14];  // x0
    struct_3 *v41;  // x0
    long long v42;  // x0
    long long v43;  // x20
    long long ptr6[14];  // x0
    unsigned long v10;  // x20
    struct_1 *v11;  // x19
    struct_1 *ptr7;  // x19
    struct_1 *v13;  // x21
    struct_1 *ptr;  // x21
    unsigned long v15;  // x20
    unsigned long v0;  // [bp-0x30], Other Possible Types: unsigned long long
    unsigned long long v1;  // [bp-0x28]
    long long *v2;  // [bp-0x20]
    struct_2 *v3;  // [bp-0x18]
    unsigned long v4;  // [bp-0x10]
    struct_1 *v5;  // [bp-0x8]

    v0 = v6;
    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    ptr7 = a0;
    if (!(g_1fab375 & 1))
    {
        sub_f7d92c(&g_1eec130);
        sub_f7d92c("{+");
        sub_f7d92c(&g_1efbae8);
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef6e68);
        sub_f7d92c("A<");
        sub_f7d92c(&g_1f0bde8);
        g_1fab375 = 1;
    }
    v13 = ptr7;
    ptr = &v13->field_68;
    v15 = *((long long *)&ptr->padding_0[32]);
    if (v13->field_68)
    {
        RewardedAd__Destroy(v13->field_68, 0);
        *((long long *)&ptr->padding_0[0]) = 0;
        sub_f7d8d0(ptr, 0);
    }
    v16 = &g_1f0bde8;
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__Log(g_1f0bde8, 0);
    v17 = 0;
    v18 = sub_f7db70(g_1eee6c0);
    AdRequest__ctor(v18, 0);
    if (v18 && v18->field_10)
    {
        sub_13d6008(v18->field_10, g_1f152f0, g_1ef6e68);
        v19 = sub_f7db70(g_1eec130);
        sub_12633ac(v19, ptr7, g_1efbae8, 0);
        RewardedAd__Load(v15, v18, v19, 0);
        v17 = ptr7->field_68;
        v15 = v4;
        ptr7 = v5;
        v16 = v2;
        v18 = v3;
        vvar_111{r256|8b} = v0;
    }
    else
    {
        vvar_280{r256|8b} = (int)&g_1073a3c;
        sub_f7db74();
    }
    v0 = vvar_111{r256|8b};
    v2 = v16;
    v3 = v18;
    v4 = v15;
    v5 = ptr7;
    v20 = v17;
    if (!(g_1fab376 & 1))
    {
        sub_f7d92c(&g_1eebf78);
        sub_f7d92c(&g_1eebf88);
        sub_f7d92c("++");
        sub_f7d92c(&g_1f03fd0);
        sub_f7d92c(&g_1f03fd8);
        sub_f7d92c(&g_1f03fe0);
        sub_f7d92c(&g_1f03fe8);
        sub_f7d92c(&g_1f03ff0);
        sub_f7d92c(&g_1f03ff8);
        sub_f7d92c(&g_1ef2b90);
        g_1fab376 = 1;
    }
    index = g_1ef2b90;
    if (!g_1ef2b90->field_e0)
    {
        sub_f7da5c(g_1ef2b90);
        index = g_1ef2b90;
    }
    v22 = index->field_b8->field_40;
    if (!v22)
    {
        if (!index->field_e0)
        {
            sub_f7da5c();
            index = g_1ef2b90;
        }
        v23 = sub_f7db70(g_1eebf88);
        v22 = v23;
        sub_126041c(v23, index->field_b8->field_0, g_1f03fd0, 0);
        p = g_1ef2b90->field_b8;
        p[8] = v22;
        sub_f7d8d0((long long [14])&p[8], v22);
    }
    if (!v20)
        sub_f7db74();
    RewardedAd__add_OnAdPaid(v20, v22, 0);
    pos = g_1ef2b90;
    if (!g_1ef2b90->field_e0)
    {
        sub_f7da5c(g_1ef2b90);
        pos = g_1ef2b90;
    }
    v26 = pos->field_b8->field_48;
    if (!v26)
    {
        if (!pos->field_e0)
        {
            sub_f7da5c();
            pos = g_1ef2b90;
        }
        v27 = sub_f7db70(g_1eee648);
        v26 = v27;
        Action__ctor(v27, pos->field_b8->field_0, g_1f03fd8, 0);
        addr = g_1ef2b90->field_b8;
        addr[9] = v26;
        sub_f7d8d0((long long [14])&addr[9], v26);
    }
    RewardedAd__add_OnAdImpressionRecorded(v20, v26, 0);
    off = g_1ef2b90;
    if (!g_1ef2b90->field_e0)
    {
        sub_f7da5c(g_1ef2b90);
        off = g_1ef2b90;
    }
    v30 = off->field_b8->field_50;
    if (!v30)
    {
        if (!off->field_e0)
        {
            sub_f7da5c();
            off = g_1ef2b90;
        }
        v31 = sub_f7db70(g_1eee648);
        v30 = v31;
        Action__ctor(v31, off->field_b8->field_0, g_1f03fe0, 0);
        ptr3 = g_1ef2b90->field_b8;
        ptr3[10] = v30;
        sub_f7d8d0((long long [14])&ptr3[10], v30);
    }
    RewardedAd__add_OnAdClicked(v20, v30, 0);
    idx4 = g_1ef2b90;
    if (!g_1ef2b90->field_e0)
    {
        sub_f7da5c(g_1ef2b90);
        idx4 = g_1ef2b90;
    }
    v34 = idx4->field_b8->field_58;
    if (!v34)
    {
        if (!idx4->field_e0)
        {
            sub_f7da5c();
            idx4 = g_1ef2b90;
        }
        v35 = sub_f7db70(g_1eee648);
        v34 = v35;
        Action__ctor(v35, idx4->field_b8->field_0, g_1f03fe8, 0);
        ptr4 = g_1ef2b90->field_b8;
        ptr4[11] = v34;
        sub_f7d8d0((long long [14])&ptr4[11], v34);
    }
    RewardedAd__add_OnAdFullScreenContentOpened(v20, v34, 0);
    idx5 = g_1ef2b90;
    if (!g_1ef2b90->field_e0)
    {
        sub_f7da5c(g_1ef2b90);
        idx5 = g_1ef2b90;
    }
    v38 = idx5->field_b8->field_60;
    if (!v38)
    {
        if (!idx5->field_e0)
        {
            sub_f7da5c();
            idx5 = g_1ef2b90;
        }
        v39 = sub_f7db70(g_1eee648);
        v38 = v39;
        Action__ctor(v39, idx5->field_b8->field_0, g_1f03ff0, 0);
        ptr5 = g_1ef2b90->field_b8;
        ptr5[12] = v38;
        sub_f7d8d0((long long [14])&ptr5[12], v38);
    }
    RewardedAd__add_OnAdFullScreenContentClosed(v20, v38, 0);
    v41 = g_1ef2b90;
    if (!g_1ef2b90->field_e0)
    {
        sub_f7da5c(g_1ef2b90);
        v41 = g_1ef2b90;
    }
    if (!v41->field_b8->field_68)
    {
        if (!v41->field_e0)
        {
            sub_f7da5c();
            v41 = g_1ef2b90;
        }
        v42 = sub_f7db70(g_1eebf78);
        v43 = v42;
        sub_126041c(v42, v41->field_b8->field_0, g_1f03ff8, 0);
        ptr6 = g_1ef2b90->field_b8;
        ptr6[13] = v43;
        sub_f7d8d0((long long [14])&ptr6[13], v43);
    }
}
```

## `AdsManager.RegisterEventHandlers` — RVA `0xc73a3c`

- Decompiled symbol: `AdsManager_RegisterEventHandlers`
- Metadata signature: `private void RegisterEventHandlers(RewardedAd ad) { }`
- Native interval: `1000` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x1073a3c: str x30, [sp, #-0x30]!
// 0x1073a40: stp x22, x21, [sp, #0x10]
// 0x1073a44: stp x20, x19, [sp, #0x20]
// 0x1073a48: adrp x20, #0x1fab000
// 0x1073a4c: adrp x22, #0x1e8d000
// 0x1073a50: ldrb w8, [x20, #0x376]
// 0x1073a54: ldr x22, [x22, #0x698]
// 0x1073a58: mov x19, x1
// 0x1073a5c: tbnz w8, #0, #0x1073ae0
// 0x1073a60: adrp x0, #0x1e8d000
// 0x1073a64: ldr x0, [x0, #0x768]
// 0x1073a68: bl #0xf7d92c
// 0x1073a6c: adrp x0, #0x1e8d000
// 0x1073a70: ldr x0, [x0, #0x770]
// 0x1073a74: bl #0xf7d92c
// 0x1073a78: adrp x0, #0x1e8c000
// 0x1073a7c: ldr x0, [x0, #0x40]
// 0x1073a80: bl #0xf7d92c
// 0x1073a84: adrp x0, #0x1e8d000
// 0x1073a88: ldr x0, [x0, #0x7c0]
// 0x1073a8c: bl #0xf7d92c
// 0x1073a90: adrp x0, #0x1e8d000
// 0x1073a94: ldr x0, [x0, #0x7c8]
// 0x1073a98: bl #0xf7d92c
// 0x1073a9c: adrp x0, #0x1e8d000
// 0x1073aa0: ldr x0, [x0, #0x7d0]
// 0x1073aa4: bl #0xf7d92c
// 0x1073aa8: adrp x0, #0x1e8d000
// 0x1073aac: ldr x0, [x0, #0x7d8]
// 0x1073ab0: bl #0xf7d92c
// 0x1073ab4: adrp x0, #0x1e8d000
// 0x1073ab8: ldr x0, [x0, #0x7e0]
// 0x1073abc: bl #0xf7d92c
// 0x1073ac0: adrp x0, #0x1e8d000
// 0x1073ac4: ldr x0, [x0, #0x7e8]
// 0x1073ac8: bl #0xf7d92c
// 0x1073acc: adrp x0, #0x1e8d000
// 0x1073ad0: ldr x0, [x0, #0x698]
// 0x1073ad4: bl #0xf7d92c
// 0x1073ad8: mov w8, #1
// 0x1073adc: strb w8, [x20, #0x376]
// 0x1073ae0: ldr x0, [x22]
// 0x1073ae4: ldr w8, [x0, #0xe0]
// 0x1073ae8: cbnz w8, #0x1073af4
// 0x1073aec: bl #0xf7da5c
// 0x1073af0: ldr x0, [x22]
// 0x1073af4: ldr x8, [x0, #0xb8]
// 0x1073af8: ldr x20, [x8, #0x40]
// 0x1073afc: cbnz x20, #0x1073b58
// 0x1073b00: ldr w8, [x0, #0xe0]
// 0x1073b04: cbnz w8, #0x1073b10
// 0x1073b08: bl #0xf7da5c
// 0x1073b0c: ldr x0, [x22]
// 0x1073b10: adrp x9, #0x1e8d000
// 0x1073b14: ldr x8, [x0, #0xb8]
// 0x1073b18: ldr x9, [x9, #0x770]
// 0x1073b1c: ldr x21, [x8]
// 0x1073b20: ldr x0, [x9]
// 0x1073b24: bl #0xf7db70
// 0x1073b28: adrp x8, #0x1e8d000
// 0x1073b2c: ldr x8, [x8, #0x7c0]
// 0x1073b30: mov x1, x21
// 0x1073b34: mov x3, xzr
// 0x1073b38: mov x20, x0
// 0x1073b3c: ldr x2, [x8]
// 0x1073b40: bl #0x126041c
// 0x1073b44: ldr x8, [x22]
// 0x1073b48: mov x1, x20
// 0x1073b4c: ldr x0, [x8, #0xb8]
// 0x1073b50: str x20, [x0, #0x40]!
// 0x1073b54: bl #0xf7d8d0
// 0x1073b58: cbz x19, #0x1073e20
// 0x1073b5c: mov x0, x19
// 0x1073b60: mov x1, x20
// 0x1073b64: mov x2, xzr
// 0x1073b68: bl #0x17adb80
// 0x1073b6c: ldr x0, [x22]
// 0x1073b70: ldr w8, [x0, #0xe0]
// 0x1073b74: cbnz w8, #0x1073b80
// 0x1073b78: bl #0xf7da5c
// 0x1073b7c: ldr x0, [x22]
// 0x1073b80: ldr x8, [x0, #0xb8]
// 0x1073b84: ldr x20, [x8, #0x48]
// 0x1073b88: cbnz x20, #0x1073be4
// 0x1073b8c: ldr w8, [x0, #0xe0]
// 0x1073b90: cbnz w8, #0x1073b9c
// 0x1073b94: bl #0xf7da5c
// 0x1073b98: ldr x0, [x22]
// 0x1073b9c: adrp x9, #0x1e8c000
// 0x1073ba0: ldr x8, [x0, #0xb8]
// 0x1073ba4: ldr x9, [x9, #0x40]
// 0x1073ba8: ldr x21, [x8]
// 0x1073bac: ldr x0, [x9]
// 0x1073bb0: bl #0xf7db70
// 0x1073bb4: adrp x8, #0x1e8d000
// 0x1073bb8: ldr x8, [x8, #0x7c8]
// 0x1073bbc: mov x1, x21
// 0x1073bc0: mov x3, xzr
// 0x1073bc4: mov x20, x0
// 0x1073bc8: ldr x2, [x8]
// 0x1073bcc: bl #0x18e3eac
// 0x1073bd0: ldr x8, [x22]
// 0x1073bd4: mov x1, x20
// 0x1073bd8: ldr x0, [x8, #0xb8]
// 0x1073bdc: str x20, [x0, #0x48]!
// 0x1073be0: bl #0xf7d8d0
// 0x1073be4: mov x0, x19
// 0x1073be8: mov x1, x20
// 0x1073bec: mov x2, xzr
// 0x1073bf0: bl #0x17ade18
// 0x1073bf4: ldr x0, [x22]
// 0x1073bf8: ldr w8, [x0, #0xe0]
// 0x1073bfc: cbnz w8, #0x1073c08
// 0x1073c00: bl #0xf7da5c
// 0x1073c04: ldr x0, [x22]
// 0x1073c08: ldr x8, [x0, #0xb8]
// 0x1073c0c: ldr x20, [x8, #0x50]
// 0x1073c10: cbnz x20, #0x1073c6c
// 0x1073c14: ldr w8, [x0, #0xe0]
// 0x1073c18: cbnz w8, #0x1073c24
// 0x1073c1c: bl #0xf7da5c
// 0x1073c20: ldr x0, [x22]
// 0x1073c24: adrp x9, #0x1e8c000
// 0x1073c28: ldr x8, [x0, #0xb8]
// 0x1073c2c: ldr x9, [x9, #0x40]
// 0x1073c30: ldr x21, [x8]
// 0x1073c34: ldr x0, [x9]
// 0x1073c38: bl #0xf7db70
// 0x1073c3c: adrp x8, #0x1e8d000
// 0x1073c40: ldr x8, [x8, #0x7d0]
// 0x1073c44: mov x1, x21
// 0x1073c48: mov x3, xzr
// 0x1073c4c: mov x20, x0
// 0x1073c50: ldr x2, [x8]
// 0x1073c54: bl #0x18e3eac
// 0x1073c58: ldr x8, [x22]
// 0x1073c5c: mov x1, x20
// 0x1073c60: ldr x0, [x8, #0xb8]
// 0x1073c64: str x20, [x0, #0x50]!
// 0x1073c68: bl #0xf7d8d0
// 0x1073c6c: mov x0, x19
// 0x1073c70: mov x1, x20
// 0x1073c74: mov x2, xzr
// 0x1073c78: bl #0x17adce0
// 0x1073c7c: ldr x0, [x22]
// 0x1073c80: ldr w8, [x0, #0xe0]
// 0x1073c84: cbnz w8, #0x1073c90
// 0x1073c88: bl #0xf7da5c
// 0x1073c8c: ldr x0, [x22]
// 0x1073c90: ldr x8, [x0, #0xb8]
// 0x1073c94: ldr x20, [x8, #0x58]
// 0x1073c98: cbnz x20, #0x1073cf4
// 0x1073c9c: ldr w8, [x0, #0xe0]
// 0x1073ca0: cbnz w8, #0x1073cac
// 0x1073ca4: bl #0xf7da5c
// 0x1073ca8: ldr x0, [x22]
// 0x1073cac: adrp x9, #0x1e8c000
// 0x1073cb0: ldr x8, [x0, #0xb8]
// 0x1073cb4: ldr x9, [x9, #0x40]
// 0x1073cb8: ldr x21, [x8]
// 0x1073cbc: ldr x0, [x9]
// 0x1073cc0: bl #0xf7db70
// 0x1073cc4: adrp x8, #0x1e8d000
// 0x1073cc8: ldr x8, [x8, #0x7d8]
// 0x1073ccc: mov x1, x21
// 0x1073cd0: mov x3, xzr
// 0x1073cd4: mov x20, x0
// 0x1073cd8: ldr x2, [x8]
// 0x1073cdc: bl #0x18e3eac
// 0x1073ce0: ldr x8, [x22]
// 0x1073ce4: mov x1, x20
// 0x1073ce8: ldr x0, [x8, #0xb8]
// 0x1073cec: str x20, [x0, #0x58]!
// 0x1073cf0: bl #0xf7d8d0
// 0x1073cf4: mov x0, x19
// 0x1073cf8: mov x1, x20
// 0x1073cfc: mov x2, xzr
// 0x1073d00: bl #0x17adf50
// 0x1073d04: ldr x0, [x22]
// 0x1073d08: ldr w8, [x0, #0xe0]
// 0x1073d0c: cbnz w8, #0x1073d18
// 0x1073d10: bl #0xf7da5c
// 0x1073d14: ldr x0, [x22]
// 0x1073d18: ldr x8, [x0, #0xb8]
// 0x1073d1c: ldr x20, [x8, #0x60]
// 0x1073d20: cbnz x20, #0x1073d7c
// 0x1073d24: ldr w8, [x0, #0xe0]
// 0x1073d28: cbnz w8, #0x1073d34
// 0x1073d2c: bl #0xf7da5c
// 0x1073d30: ldr x0, [x22]
// 0x1073d34: adrp x9, #0x1e8c000
// 0x1073d38: ldr x8, [x0, #0xb8]
// 0x1073d3c: ldr x9, [x9, #0x40]
// 0x1073d40: ldr x21, [x8]
// 0x1073d44: ldr x0, [x9]
// 0x1073d48: bl #0xf7db70
// 0x1073d4c: adrp x8, #0x1e8d000
// 0x1073d50: ldr x8, [x8, #0x7e0]
// 0x1073d54: mov x1, x21
// 0x1073d58: mov x3, xzr
// 0x1073d5c: mov x20, x0
// 0x1073d60: ldr x2, [x8]
// 0x1073d64: bl #0x18e3eac
// 0x1073d68: ldr x8, [x22]
// 0x1073d6c: mov x1, x20
// 0x1073d70: ldr x0, [x8, #0xb8]
// 0x1073d74: str x20, [x0, #0x60]!
// 0x1073d78: bl #0xf7d8d0
// 0x1073d7c: mov x0, x19
// 0x1073d80: mov x1, x20
// 0x1073d84: mov x2, xzr
// 0x1073d88: bl #0x17ae088
// 0x1073d8c: ldr x0, [x22]
// 0x1073d90: ldr w8, [x0, #0xe0]
// 0x1073d94: cbnz w8, #0x1073da0
// 0x1073d98: bl #0xf7da5c
// 0x1073d9c: ldr x0, [x22]
// 0x1073da0: ldr x8, [x0, #0xb8]
// 0x1073da4: ldr x20, [x8, #0x68]
// 0x1073da8: cbnz x20, #0x1073e04
// 0x1073dac: ldr w8, [x0, #0xe0]
// 0x1073db0: cbnz w8, #0x1073dbc
// 0x1073db4: bl #0xf7da5c
// 0x1073db8: ldr x0, [x22]
// 0x1073dbc: adrp x9, #0x1e8d000
// 0x1073dc0: ldr x8, [x0, #0xb8]
// 0x1073dc4: ldr x9, [x9, #0x768]
// 0x1073dc8: ldr x21, [x8]
// 0x1073dcc: ldr x0, [x9]
// 0x1073dd0: bl #0xf7db70
// 0x1073dd4: adrp x8, #0x1e8d000
// 0x1073dd8: ldr x8, [x8, #0x7e8]
// 0x1073ddc: mov x1, x21
// 0x1073de0: mov x3, xzr
// 0x1073de4: mov x20, x0
// 0x1073de8: ldr x2, [x8]
// 0x1073dec: bl #0x126041c
// 0x1073df0: ldr x8, [x22]
// 0x1073df4: mov x1, x20
// 0x1073df8: ldr x0, [x8, #0xb8]
// 0x1073dfc: str x20, [x0, #0x68]!
// 0x1073e00: bl #0xf7d8d0
// 0x1073e04: mov x0, x19
// 0x1073e08: mov x1, x20
// 0x1073e0c: ldp x20, x19, [sp, #0x20]
// 0x1073e10: ldp x22, x21, [sp, #0x10]
// 0x1073e14: mov x2, xzr
// 0x1073e18: ldr x30, [sp], #0x30
// 0x1073e1c: b #0x17ae1c0
// 0x1073e20: bl #0xf7db74
```

## `AdsManager.Show_Interstitial` — RVA `0xc73e24`

- Decompiled symbol: `AdsManager_Show_Interstitial`
- Metadata signature: `public void Show_Interstitial() { }`
- Native interval: `344` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AdsManager_Recovered` matched 2 offsets against `AdsManager` metadata (confidence 1.00).

```c
typedef struct AdsManager_Recovered {
    char padding_0[96];
    long long interstitialAd;
    char padding_68[8];
    unsigned long long Successfunction;
} AdsManager_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1f082a0;
extern long long g_1f0b168;
extern long long g_1f0d458;
extern long long g_1f0da58;
extern char g_1fab377;

unsigned long long AdsManager_Show_Interstitial(struct_1 *ptr)
{
    unsigned long long v0;  // x0
    unsigned long long v1;  // x0
    unsigned long long v2;  // x0
    unsigned long long v3;  // x0

    if (!(g_1fab377 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f0d458);
        sub_f7d92c(&g_1f082a0);
        sub_f7d92c(&g_1f0b168);
        sub_f7d92c(&g_1f0da58);
        g_1fab377 = 1;
    }
    v0 = PlayerPrefs__GetInt(g_1f0d458, 0);
    if ((unsigned int)v0 == 149)
        return v0;
    ptr->field_70 = 0;
    sub_f7d8d0((struct AdsManager_Recovered *)&ptr->field_70, 0);
    v1 = PlayerPrefs__GetInt(g_1f082a0, 0);
    if ((unsigned int)v1 == 1)
        return v1;
    if (ptr->field_60 && ((char)InterstitialAd__CanShowAd(ptr->field_60, 0) & 1))
    {
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        Debug__Log(g_1f0da58, 0);
        if (ptr->field_60)
        {
            InterstitialAd__Show(ptr->field_60, 0);
            AdsManager__LoadInter(ptr);
            v2 = MonoBehaviour__StartCoroutine();
            return MonoBehaviour__StartCoroutine();
        }
        sub_f7db74(0);
    }
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    v3 = Debug__LogError();
    return Debug__LogError();
}
```

## `AdsManager.Show_Rewarded` — RVA `0xc73f7c`

- Decompiled symbol: `AdsManager_Show_Rewarded`
- Metadata signature: `public void Show_Rewarded(Action RewardedFunction) { }`
- Native interval: `192` bytes
- Result: `pseudocode`

```c
extern long long g_1efbaf0;
extern char g_1fab378;

long long AdsManager_Show_Rewarded(long long *ptr, long long a1)
{
    long long p[15];  // x21
    long long v1;  // x0
    long long v2;  // x0
    long long v3;  // x0

    if (!(g_1fab378 & 1))
    {
        sub_f7d92c("q\t");
        sub_f7d92c(&g_1efbaf0);
        g_1fab378 = 1;
    }
    ptr[14] = a1;
    p = ptr + 14;
    sub_f7d8d0(p, a1);
    v1 = p[1];
    if (!v1)
        return v1;
    v2 = RewardedAd__CanShowAd(v1, 0);
    if (!((char)v2 & 1))
        return v2;
    v3 = sub_f7db70(g_1eec080);
    sub_126041c(v3, ptr, g_1efbaf0, 0);
    if (!ptr[13])
        sub_f7db74();
}
```

## `AdsManager.ctor` — RVA `0xc7403c`

- Decompiled symbol: `AdsManager_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long AdsManager_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```

## `AdsManager.<RequestInterstitial>b__24_0` — RVA `0xc74044`

- Decompiled symbol: `AdsManager_RequestInterstitial_b__24_0`
- Metadata signature: `private void <RequestInterstitial>b__24_0(InterstitialAd ad, LoadAdError error) { }`
- Native interval: `328` bytes
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
    char padding_0[96];
    long long field_60;
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
extern long long g_1f0b170;
extern long long g_1f130b8;
extern char g_1fab379;

void AdsManager_RequestInterstitial_b__24_0(struct_1 *ptr, long long a1, struct_4 **a2)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    struct_2 **v10;  // x0
    unsigned long long v11;  // x1
    long long v12;  // x0
    struct_4 **v13;  // x0
    unsigned long v14;  // x1
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
    if (!(g_1fab379 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f130b8);
        sub_f7d92c(&g_1f0b170);
        g_1fab379 = 1;
    }
    if (a1 && !a2)
    {
        v10 = InterstitialAd__GetResponseInfo(a1, 0);
        if (v10)
        {
            v11 = *(v10)->field_170;
            *(v10)->field_168();
        }
        v12 = String__Concat(g_1f0b170);
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        Debug__Log(v12, 0);
        ptr->field_60 = a1;
        sub_f7d8d0();
        return;
    }
    if (a2)
    {
        v13 = a2;
        v14 = *(a2)->field_170;
        *(a2)->field_168();
    }
    String__Concat(g_1f130b8);
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__LogError();
    return;
}
```

## `AdsManager.<Request_Rewarded>b__26_0` — RVA `0xc7418c`

- Decompiled symbol: `AdsManager_Request_Rewarded_b__26_0`
- Metadata signature: `private void <Request_Rewarded>b__26_0(RewardedAd ad, LoadAdError error) { }`
- Native interval: `328` bytes
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
    char padding_0[104];
    long long field_68;
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
extern long long g_1f0d5d0;
extern long long g_1f0d5f0;
extern char g_1fab37a;

void AdsManager_Request_Rewarded_b__26_0(struct_1 *ptr, long long a1, struct_4 **a2)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    struct_2 **v10;  // x0
    unsigned long long v11;  // x1
    long long v12;  // x0
    struct_4 **v13;  // x0
    unsigned long v14;  // x1
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
    if (!(g_1fab37a & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f0d5d0);
        sub_f7d92c(&g_1f0d5f0);
        g_1fab37a = 1;
    }
    if (a1 && !a2)
    {
        v10 = RewardedAd__GetResponseInfo(a1, 0);
        if (v10)
        {
            v11 = *(v10)->field_170;
            *(v10)->field_168();
        }
        v12 = String__Concat(g_1f0d5f0);
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        Debug__Log(v12, 0);
        ptr->field_68 = a1;
        sub_f7d8d0();
        return;
    }
    if (a2)
    {
        v13 = a2;
        v14 = *(a2)->field_170;
        *(a2)->field_168();
    }
    String__Concat(g_1f0d5d0);
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__LogError();
    return;
}
```

## `AdsManager.<Show_Rewarded>b__30_0` — RVA `0xc742d4`

- Decompiled symbol: `AdsManager_Show_Rewarded_b__30_0`
- Metadata signature: `private void <Show_Rewarded>b__30_0(Reward reward) { }`
- Native interval: `256` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AdsManager_Recovered` matched 2 offsets against `AdsManager` metadata (confidence 0.67).

```c
typedef struct struct_3 {
    char padding_0[112];
    struct AdsManager_Recovered *field_70;
} struct_3;

typedef struct AdsManager_Recovered {
    char padding_0[24];
    struct struct_2 *field_18;
    char padding_20[8];
    unsigned long long AppOpen_ID;
    char padding_30[16];
    unsigned long long interstitial_ID;
} AdsManager_Recovered;

typedef struct struct_4 {
    char padding_0[16];
    long long field_10;
    unsigned long long field_18;
} struct_4;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1eef608;
extern long long g_1f0d608;
extern char g_1fab37b;

long long AdsManager_Show_Rewarded_b__30_0(struct_3 *p, struct_4 *addr)
{
    struct_1 *ptr;  // x8
    unsigned long long v2;  // x0
    unsigned long long v3;  // x1
    long long v5;  // x0
    long long v6;  // x0
    unsigned long long v7;  // x0
    unsigned long v0;  // [bp-0x28]

    if (!(g_1fab37b & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1eef608);
        sub_f7d92c(&g_1f0d608);
        g_1fab37b = 1;
    }
    ptr = p->field_70;
    if (ptr)
    {
        v2 = ptr->field_40;
        v3 = ptr->field_28;
        ptr->field_18();
    }
    MonoBehaviour__StartCoroutine(p, AdsManager__LoadRewarded(p), 0);
    if (addr)
    {
        v0 = addr->field_18;
        v5 = sub_f7da64(g_1eef608, &v0);
        v6 = String__Format(g_1f0d608, addr->field_10, v5, 0);
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        v7 = Debug__Log(v6, 0);
        return Debug__Log(v6, 0);
    }
    sub_f7db74();
}
```

## `AdsManager.<>c.cctor` — RVA `0xc743d4`

- Decompiled symbol: `AdsManager_c_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    long long field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef2b90;
extern char g_1fab37c;

void AdsManager_c_cctor(void)
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
    if (!(g_1fab37c & 1))
    {
        sub_f7d92c(&g_1ef2b90);
        g_1fab37c = 1;
    }
    v6 = sub_f7db70(g_1ef2b90);
    Object__ctor(v6, 0);
    g_1ef2b90->field_b8->field_0 = v6;
    sub_f7d8d0();
    return;
}
```

## `AdsManager.<>c.ctor` — RVA `0xc7443c`

- Decompiled symbol: `AdsManager_c_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long AdsManager_c_ctor(void)
{
    long long v0;  // x0

    v0 = Object__ctor();
    return Object__ctor();
}
```

## `AdsManager.<>c.<Start>b__11_0` — RVA `0xc74444`

- Decompiled symbol: `AdsManager_c_Start_b__11_0`
- Metadata signature: `internal void <Start>b__11_0(InitializationStatus initStatus) { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long AdsManager_c_Start_b__11_0(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `AdsManager.<>c.<RegisterEventHandlers>b__25_0` — RVA `0xc74448`

- Decompiled symbol: `AdsManager_c_RegisterEventHandlers_b__25_0`
- Metadata signature: `internal void <RegisterEventHandlers>b__25_0(AdValue adValue) { }`
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
extern long long g_1f0b178;
extern char g_1fab37d;

long long AdsManager_c_RegisterEventHandlers_b__25_0(unsigned long a0, struct_1 *ptr)
{
    long long v1;  // x0
    long long v2;  // x0
    unsigned long long v3;  // x0
    unsigned long v0;  // [bp-0x28]

    if (!(g_1fab37d & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef0458);
        sub_f7d92c(&g_1f0b178);
        g_1fab37d = 1;
    }
    if (ptr)
    {
        v0 = ptr->field_18;
        v1 = sub_f7da64(g_1ef0458, &v0);
        v2 = String__Format(g_1f0b178, v1, ptr->field_20, 0);
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        v3 = Debug__Log(v2, 0);
        return Debug__Log(v2, 0);
    }
    sub_f7db74();
}
```

## `AdsManager.<>c.<RegisterEventHandlers>b__25_1` — RVA `0xc74510`

- Decompiled symbol: `AdsManager_c_RegisterEventHandlers_b__25_1`
- Metadata signature: `internal void <RegisterEventHandlers>b__25_1() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1f0b180;
extern char g_1fab37e;

void AdsManager_c_RegisterEventHandlers_b__25_1(void)
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
    if (!(g_1fab37e & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f0b180);
        g_1fab37e = 1;
    }
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__Log();
    return;
}
```

## `AdsManager.<>c.<RegisterEventHandlers>b__25_2` — RVA `0xc74578`

- Decompiled symbol: `AdsManager_c_RegisterEventHandlers_b__25_2`
- Metadata signature: `internal void <RegisterEventHandlers>b__25_2() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1f0b188;
extern char g_1fab37f;

void AdsManager_c_RegisterEventHandlers_b__25_2(void)
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
    if (!(g_1fab37f & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f0b188);
        g_1fab37f = 1;
    }
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__Log();
    return;
}
```

## `AdsManager.<>c.<RegisterEventHandlers>b__25_3` — RVA `0xc745e0`

- Decompiled symbol: `AdsManager_c_RegisterEventHandlers_b__25_3`
- Metadata signature: `internal void <RegisterEventHandlers>b__25_3() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1f07240;
extern char g_1fab380;

void AdsManager_c_RegisterEventHandlers_b__25_3(void)
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
    if (!(g_1fab380 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f07240);
        g_1fab380 = 1;
    }
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__Log();
    return;
}
```

## `AdsManager.<>c.<RegisterEventHandlers>b__25_4` — RVA `0xc74648`

- Decompiled symbol: `AdsManager_c_RegisterEventHandlers_b__25_4`
- Metadata signature: `internal void <RegisterEventHandlers>b__25_4() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1f0b160;
extern char g_1fab381;

void AdsManager_c_RegisterEventHandlers_b__25_4(void)
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
    if (!(g_1fab381 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f0b160);
        g_1fab381 = 1;
    }
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__Log();
    return;
}
```

## `AdsManager.<>c.<RegisterEventHandlers>b__25_5` — RVA `0xc746b0`

- Decompiled symbol: `AdsManager_c_RegisterEventHandlers_b__25_5`
- Metadata signature: `internal void <RegisterEventHandlers>b__25_5(AdError error) { }`
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
extern long long g_1f0b158;
extern char g_1fab382;

void AdsManager_c_RegisterEventHandlers_b__25_5(unsigned long a0, struct_1 **a1)
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
    if (!(g_1fab382 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f0b158);
        g_1fab382 = 1;
    }
    if (a1)
    {
        v8 = a1;
        v9 = *(a1)->field_170;
        *(a1)->field_168();
    }
    String__Concat(g_1f0b158);
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__LogError();
    return;
}
```

## `AdsManager.<>c.<RegisterEventHandlers>b__27_0` — RVA `0xc74754`

- Decompiled symbol: `AdsManager_c_RegisterEventHandlers_b__27_0`
- Metadata signature: `internal void <RegisterEventHandlers>b__27_0(AdValue adValue) { }`
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
extern long long g_1f0d5f8;
extern char g_1fab383;

long long AdsManager_c_RegisterEventHandlers_b__27_0(unsigned long a0, struct_1 *ptr)
{
    long long v1;  // x0
    long long v2;  // x0
    unsigned long long v3;  // x0
    unsigned long v0;  // [bp-0x28]

    if (!(g_1fab383 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef0458);
        sub_f7d92c(&g_1f0d5f8);
        g_1fab383 = 1;
    }
    if (ptr)
    {
        v0 = ptr->field_18;
        v1 = sub_f7da64(g_1ef0458, &v0);
        v2 = String__Format(g_1f0d5f8, v1, ptr->field_20, 0);
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        v3 = Debug__Log(v2, 0);
        return Debug__Log(v2, 0);
    }
    sub_f7db74();
}
```

## `AdsManager.<>c.<RegisterEventHandlers>b__27_1` — RVA `0xc7481c`

- Decompiled symbol: `AdsManager_c_RegisterEventHandlers_b__27_1`
- Metadata signature: `internal void <RegisterEventHandlers>b__27_1() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1f0d600;
extern char g_1fab384;

void AdsManager_c_RegisterEventHandlers_b__27_1(void)
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
    if (!(g_1fab384 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f0d600);
        g_1fab384 = 1;
    }
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__Log();
    return;
}
```

## `AdsManager.<>c.<RegisterEventHandlers>b__27_2` — RVA `0xc74884`

- Decompiled symbol: `AdsManager_c_RegisterEventHandlers_b__27_2`
- Metadata signature: `internal void <RegisterEventHandlers>b__27_2() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1f0d610;
extern char g_1fab385;

void AdsManager_c_RegisterEventHandlers_b__27_2(void)
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
    if (!(g_1fab385 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f0d610);
        g_1fab385 = 1;
    }
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__Log();
    return;
}
```

## `AdsManager.<>c.<RegisterEventHandlers>b__27_3` — RVA `0xc748ec`

- Decompiled symbol: `AdsManager_c_RegisterEventHandlers_b__27_3`
- Metadata signature: `internal void <RegisterEventHandlers>b__27_3() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1f0d5e8;
extern char g_1fab386;

void AdsManager_c_RegisterEventHandlers_b__27_3(void)
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
    if (!(g_1fab386 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f0d5e8);
        g_1fab386 = 1;
    }
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__Log();
    return;
}
```

## `AdsManager.<>c.<RegisterEventHandlers>b__27_4` — RVA `0xc74954`

- Decompiled symbol: `AdsManager_c_RegisterEventHandlers_b__27_4`
- Metadata signature: `internal void <RegisterEventHandlers>b__27_4() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1f0d5e0;
extern char g_1fab387;

void AdsManager_c_RegisterEventHandlers_b__27_4(void)
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
    if (!(g_1fab387 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f0d5e0);
        g_1fab387 = 1;
    }
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__Log();
    return;
}
```

## `AdsManager.<>c.<RegisterEventHandlers>b__27_5` — RVA `0xc749bc`

- Decompiled symbol: `AdsManager_c_RegisterEventHandlers_b__27_5`
- Metadata signature: `internal void <RegisterEventHandlers>b__27_5(AdError error) { }`
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
extern long long g_1f0d5d8;
extern char g_1fab388;

void AdsManager_c_RegisterEventHandlers_b__27_5(unsigned long a0, struct_1 **a1)
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
    if (!(g_1fab388 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f0d5d8);
        g_1fab388 = 1;
    }
    if (a1)
    {
        v8 = a1;
        v9 = *(a1)->field_170;
        *(a1)->field_168();
    }
    String__Concat(g_1f0d5d8);
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__LogError();
    return;
}
```

## `AdsManager.<LoadInter>d__16.Dispose` — RVA `0xc74a60`

- Decompiled symbol: `AdsManager_LoadInter_d__16_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long AdsManager_LoadInter_d__16_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `AdsManager.<LoadInter>d__16.MoveNext` — RVA `0xc74a64`

- Decompiled symbol: `AdsManager_LoadInter_d__16_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `168` bytes
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
    char padding_0[64];
    unsigned long long field_40;
    char padding_48[24];
    long long field_60;
} struct_1;

extern long long g_1ef2440;
extern char g_1fab389;

unsigned int AdsManager_LoadInter_d__16_MoveNext(struct_0 *ptr)
{
    long long v0;  // x20
    struct_1 *v1;  // x0

    if (!(g_1fab389 & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab389 = 1;
    }
    if (ptr->field_10 != 1)
    {
        if (!ptr->field_10)
        {
            ptr->field_10 = 4294967295;
            v0 = sub_f7db70(g_1ef2440);
            WaitForSeconds__ctor(v0, 0);
            ptr->field_18 = v0;
            sub_f7d8d0((struct struct_0 *)&ptr->field_18, v0);
            ptr->field_10 = 1;
            return 1;
        }
        return 0;
    }
    v1 = ptr->field_20;
    ptr->field_10 = 4294967295;
    if (v1)
        AdsManager__RequestInterstitial(v1); /* do not return */
    sub_f7db74(0);
}
```

## `AdsManager.<LoadInter>d__16.get_Current` — RVA `0xc74b0c`

- Decompiled symbol: `AdsManager_LoadInter_d__16_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AdsManager_LoadInter_d__16_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `AdsManager.<LoadInter>d__16.Reset` — RVA `0xc74b14`

- Decompiled symbol: `AdsManager_LoadInter_d__16_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04008;

void AdsManager_LoadInter_d__16_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04008));
}
```

## `AdsManager.<LoadInter>d__16.get_Current` — RVA `0xc74b4c`

- Decompiled symbol: `AdsManager_LoadInter_d__16_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AdsManager_LoadInter_d__16_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `AdsManager.<LoadRewarded>d__17.Dispose` — RVA `0xc74b54`

- Decompiled symbol: `AdsManager_LoadRewarded_d__17_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long AdsManager_LoadRewarded_d__17_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `AdsManager.<LoadRewarded>d__17.MoveNext` — RVA `0xc74b58`

- Decompiled symbol: `AdsManager_LoadRewarded_d__17_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `168` bytes
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
    char padding_0[72];
    unsigned long long field_48;
    char padding_50[24];
    long long field_68;
} struct_1;

extern long long g_1ef2440;
extern char g_1fab38a;

unsigned int AdsManager_LoadRewarded_d__17_MoveNext(struct_0 *ptr)
{
    long long v0;  // x20
    struct_1 *v1;  // x0

    if (!(g_1fab38a & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab38a = 1;
    }
    if (ptr->field_10 == 1)
    {
        v1 = ptr->field_20;
        ptr->field_10 = 4294967295;
        if (!v1)
            sub_f7db74(0);
        AdsManager__Request_Rewarded(v1);
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        v0 = sub_f7db70(g_1ef2440);
        WaitForSeconds__ctor(v0, 0);
        ptr->field_18 = v0;
        sub_f7d8d0((struct struct_0 *)&ptr->field_18, v0);
        ptr->field_10 = 1;
        return 1;
    }
    return 0;
}
```

## `AdsManager.<LoadRewarded>d__17.get_Current` — RVA `0xc74c00`

- Decompiled symbol: `AdsManager_LoadRewarded_d__17_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AdsManager_LoadRewarded_d__17_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `AdsManager.<LoadRewarded>d__17.Reset` — RVA `0xc74c08`

- Decompiled symbol: `AdsManager_LoadRewarded_d__17_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04010;

void AdsManager_LoadRewarded_d__17_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04010));
}
```

## `AdsManager.<LoadRewarded>d__17.get_Current` — RVA `0xc74c40`

- Decompiled symbol: `AdsManager_LoadRewarded_d__17_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AdsManager_LoadRewarded_d__17_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `AdsManager.<loading_Screen>d__13.Dispose` — RVA `0xc74c48`

- Decompiled symbol: `AdsManager_loading_Screen_d__13_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long AdsManager_loading_Screen_d__13_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `AdsManager.<loading_Screen>d__13.MoveNext` — RVA `0xc74c4c`

- Decompiled symbol: `AdsManager_loading_Screen_d__13_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `200` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eee870;
extern long long g_1ef2440;
extern char g_1fab38b;

unsigned int AdsManager_loading_Screen_d__13_MoveNext(struct_1 *ptr)
{
    long long v0;  // x20

    if (!(g_1fab38b & 1))
    {
        sub_f7d92c(&g_1eee870);
        sub_f7d92c(&g_1ef2440);
        g_1fab38b = 1;
    }
    if (ptr->field_10 == 1)
    {
        ptr->field_10 = 4294967295;
        if (!g_1eee870->field_e0)
            sub_f7da5c(g_1eee870);
        Application__LoadLevel(1, 0);
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        v0 = sub_f7db70(g_1ef2440);
        WaitForSeconds__ctor(v0, 0);
        ptr->field_18 = v0;
        sub_f7d8d0((struct struct_1 *)&ptr->field_18, v0);
        ptr->field_10 = 1;
        return 1;
    }
    return 0;
}
```

## `AdsManager.<loading_Screen>d__13.get_Current` — RVA `0xc74d14`

- Decompiled symbol: `AdsManager_loading_Screen_d__13_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AdsManager_loading_Screen_d__13_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `AdsManager.<loading_Screen>d__13.Reset` — RVA `0xc74d1c`

- Decompiled symbol: `AdsManager_loading_Screen_d__13_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04018;

void AdsManager_loading_Screen_d__13_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04018));
}
```

## `AdsManager.<loading_Screen>d__13.get_Current` — RVA `0xc74d54`

- Decompiled symbol: `AdsManager_loading_Screen_d__13_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long AdsManager_loading_Screen_d__13_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
