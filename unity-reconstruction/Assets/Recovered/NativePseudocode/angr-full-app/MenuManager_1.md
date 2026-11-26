# Native pseudocode: MenuManager_1

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MenuManager_1.ShowInterstitial` — RVA `0xc75c18`

- Decompiled symbol: `MenuManager_1_ShowInterstitial`
- Metadata signature: `public void ShowInterstitial() { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[96];
    long long field_60;
    char padding_68[8];
    unsigned long long field_70;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1eee700;
extern char g_1fab39e;

unsigned long long MenuManager_1_ShowInterstitial(void)
{
    unsigned long long v0;  // x0

    if (!(g_1fab39e & 1))
    {
        sub_f7d92c(&g_1eee700);
        g_1fab39e = 1;
    }
    if (g_1eee700->field_b8->field_0)
    {
        v0 = AdsManager__Show_Interstitial(g_1eee700->field_b8->field_0);
        return AdsManager__Show_Interstitial(g_1eee700->field_b8->field_0);
    }
    sub_f7db74(0);
}
```

## `MenuManager_1.ShowRewarded` — RVA `0xc75c68`

- Decompiled symbol: `MenuManager_1_ShowRewarded`
- Metadata signature: `public void ShowRewarded() { }`
- Native interval: `168` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    long long *field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1eee700;
extern long long g_1effac0;
extern char g_1fab39f;

long long MenuManager_1_ShowRewarded(long long a0)
{
    long long v0;  // x0
    long long v1;  // x0

    if (!(g_1fab39f & 1))
    {
        sub_f7d92c("++");
        sub_f7d92c(&g_1eee700);
        sub_f7d92c(&g_1effac0);
        g_1fab39f = 1;
    }
    v0 = sub_f7db70(g_1eee648);
    Action__ctor(v0, a0, g_1effac0, 0);
    if (g_1eee700->field_b8->field_0)
    {
        v1 = AdsManager__Show_Rewarded(g_1eee700->field_b8->field_0, v0);
        return AdsManager__Show_Rewarded(g_1eee700->field_b8->field_0, v0);
    }
    sub_f7db74();
}
```

## `MenuManager_1.GiveReward` — RVA `0xc75d10`

- Decompiled symbol: `MenuManager_1_GiveReward`
- Metadata signature: `public void GiveReward() { }`
- Native interval: `68` bytes
- Result: `pseudocode`

```c
extern long long g_1f08028;
extern char g_1fab3a0;

void MenuManager_1_GiveReward(void)
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
    if (!(g_1fab3a0 & 1))
    {
        sub_f7d92c(&g_1f08028);
        g_1fab3a0 = 1;
    }
    MonoBehaviour__print();
    return;
}
```

## `MenuManager_1.ReloadAds` — RVA `0xc75d54`

- Decompiled symbol: `MenuManager_1_ReloadAds`
- Metadata signature: `public void ReloadAds() { }`
- Native interval: `84` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eee870;
extern char g_1fab3a1;

void MenuManager_1_ReloadAds(void)
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
    if (!(g_1fab3a1 & 1))
    {
        sub_f7d92c(&g_1eee870);
        g_1fab3a1 = 1;
    }
    if (!g_1eee870->field_e0)
        sub_f7da5c(g_1eee870);
    Application__LoadLevel();
    return;
}
```

## `MenuManager_1.ctor` — RVA `0xc75da8`

- Decompiled symbol: `MenuManager_1_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long MenuManager_1_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
