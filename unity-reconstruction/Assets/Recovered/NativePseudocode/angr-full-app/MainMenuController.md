# Native pseudocode: MainMenuController

> Metadata source-path string: `Assets/Script/MainMenuController.cs`. This is a path string from the APK metadata, not recovered source text.

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MainMenuController.Start` — RVA `0xcc2d38`

- Decompiled symbol: `MainMenuController_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `1100` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MainMenuController_Recovered` matched 2 offsets against `MainMenuController` metadata (confidence 1.00).

```c
typedef struct MainMenuController_Recovered {
    char padding_0[184];
    struct struct_5 *QuitPanel;
    char padding_c0[32];
    unsigned int SounOnButton;
} MainMenuController_Recovered;

typedef struct struct_8 {
    char padding_0[424];
    struct struct_9 *field_1a8;
} struct_8;

typedef struct struct_6 {
    char padding_0[1512];
    struct struct_7 *field_5e8;
    unsigned long long field_5f0;
} struct_6;

typedef struct struct_5 {
    struct struct_2 *field_0;
} struct_5;

typedef struct struct_9 {
    struct struct_6 *field_0;
} struct_9;

typedef struct struct_7 {
    unsigned long long field_0;
} struct_7;

typedef struct struct_2 {
    char padding_0[424];
    struct struct_3 *field_1a8;
} struct_2;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_0 {
    char padding_0[1512];
    struct struct_1 *field_5e8;
    unsigned long long field_5f0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern struct_4 *g_1ef0750;
extern unsigned long long g_1f06220;
extern long long g_1f06ae0;
extern long long g_1f07b00;
extern long long g_1f0a7f0;
extern long long g_1f0a9f0;
extern long long g_1f131e0;
extern long long g_1f13e08;
extern long long g_1f14d40;
extern char g_1fab523;

void MainMenuController_Start(struct_8 *ptr)
{
    unsigned long long v7;  // d8
    unsigned long long v8;  // x30
    unsigned long long v17;  // x1
    struct_6 **v18;  // x0
    unsigned long long v9;  // x22
    unsigned long long v10;  // x21
    unsigned long long v11;  // x20
    unsigned long long v12;  // x19
    struct_4 *idx;  // x0
    struct_6 **v14;  // x20
    unsigned long v15;  // x0
    unsigned long long v16;  // x2
    unsigned int v0;  // [bp-0x34]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]
    unsigned long long v5;  // [bp-0x10]
    unsigned long long v6;  // [bp-0x8]

    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    v6 = v12;
    if (!(g_1fab523 & 1))
    {
        sub_f7d92c(&g_1ef0750);
        sub_f7d92c(&g_1f14d40);
        sub_f7d92c(&g_1f0a9f0);
        sub_f7d92c("''");
        sub_f7d92c(&g_1f131e0);
        sub_f7d92c(&g_1f0a7f0);
        sub_f7d92c(&g_1f06ae0);
        sub_f7d92c(&g_1f07b00);
        sub_f7d92c(")#");
        sub_f7d92c(&g_1f13e08);
        sub_f7d92c(&g_1f06220);
        sub_f7d92c("%%");
        g_1fab523 = 1;
    }
    idx = g_1ef0750;
    if (!g_1ef0750->field_e0)
    {
        sub_f7da5c(g_1ef0750);
        idx = g_1ef0750;
    }
    idx->field_b8->field_0 = ptr;
    sub_f7d8d0(g_1ef0750->field_b8, ptr);
    v14 = ptr->field_1a8;
    v0 = PlayerPrefs__GetInt(g_1f14d40, 0);
    v15 = Int32__ToString(&v0, 0);
    if (!v14)
        sub_f7db74();
    v16 = *(v14)->field_5f0;
    if (!v15)
        v17 = g_1f06220;
    else
        v17 = v15;
    v18 = v14;
    *(v14)->field_5e8();
}
```

## `MainMenuController.BuyGrenade` — RVA `0xcc3184`

- Decompiled symbol: `MainMenuController_BuyGrenade`
- Metadata signature: `public void BuyGrenade() { }`
- Native interval: `140` bytes
- Result: `pseudocode`

```c
extern long long g_1f0a7f0;
extern char g_1fab524;

unsigned long long MainMenuController_BuyGrenade(void)
{
    unsigned long long v0;  // x0
    unsigned long long v1;  // x0

    if (!(g_1fab524 & 1))
    {
        sub_f7d92c(&g_1f0a7f0);
        sub_f7d92c(")#");
        g_1fab524 = 1;
    }
    v0 = PlayerPrefs__GetInt(g_1f0ee98, 0);
    if (500 <= (unsigned int)v0)
    {
        PlayerPrefs__GetInt(g_1f0a7f0, 0);
        v1 = PlayerPrefs__SetInt();
        return PlayerPrefs__SetInt();
    }
    return v0;
}
```

## `MainMenuController.Update` — RVA `0xcc3210`

- Decompiled symbol: `MainMenuController_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long MainMenuController_Update(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `MainMenuController.Playbutton` — RVA `0xcc3214`

- Decompiled symbol: `MainMenuController_Playbutton`
- Metadata signature: `public void Playbutton() { }`
- Native interval: `180` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MainMenuController_Recovered` matched 2 offsets against `MainMenuController` metadata (confidence 1.00).

```c
typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct MainMenuController_Recovered {
    char padding_0[184];
    struct struct_2 *QuitPanel;
    char padding_c0[32];
    unsigned int SounOnButton;
} MainMenuController_Recovered;

typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

typedef struct struct_2 {
    char padding_0[12];
    unsigned int field_c;
} struct_2;

extern struct_3 *g_1ef0750;
extern char g_1fab525;

struct_1 * MainMenuController_Playbutton(unsigned long long *ptr)
{
    unsigned long v0;  // x0
    struct_3 *index;  // x0

    if (!(g_1fab525 & 1))
    {
        sub_f7d92c(&g_1ef0750);
        g_1fab525 = 1;
    }
    v0 = ptr[18];
    if (v0)
    {
        GameObject__SetActive(v0, 1, 0);
        v0 = ptr[12];
        if (v0)
        {
            GameObject__SetActive(v0, 0, 0);
            v0 = ptr[6];
            if (v0)
            {
                GameObject__SetActive(v0, 0, 0);
                v0 = ptr[20];
                if (v0)
                {
                    GameObject__SetActive(v0, 0, 0);
                    index = g_1ef0750;
                    if (!g_1ef0750->field_e0)
                    {
                        sub_f7da5c(g_1ef0750);
                        index = g_1ef0750;
                    }
                    index->field_b8->field_c = 2;
                    return index;
                }
            }
        }
    }
    sub_f7db74(v0);
}
```

## `MainMenuController.Play_Zombie_button` — RVA `0xcc32c8`

- Decompiled symbol: `MainMenuController_Play_Zombie_button`
- Metadata signature: `public void Play_Zombie_button() { }`
- Native interval: `140` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MainMenuController_Recovered` matched 2 offsets against `MainMenuController` metadata (confidence 1.00).

```c
typedef struct MainMenuController_Recovered {
    char padding_0[184];
    struct struct_2 *QuitPanel;
    char padding_c0[32];
    unsigned int SounOnButton;
} MainMenuController_Recovered;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct struct_2 {
    char padding_0[12];
    unsigned int field_c;
} struct_2;

typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

extern struct_1 *g_1ef0750;
extern char g_1fab526;

struct_3 * MainMenuController_Play_Zombie_button(unsigned long long *ptr)
{
    unsigned long v0;  // x0
    struct_1 *index;  // x0

    if (!(g_1fab526 & 1))
    {
        sub_f7d92c(&g_1ef0750);
        g_1fab526 = 1;
    }
    v0 = ptr[33];
    if (v0)
    {
        GameObject__SetActive(v0, 1, 0);
        v0 = ptr[12];
        if (v0)
        {
            GameObject__SetActive(v0, 0, 0);
            index = g_1ef0750;
            if (!g_1ef0750->field_e0)
            {
                sub_f7da5c(g_1ef0750);
                index = g_1ef0750;
            }
            index->field_b8->field_c = 3;
            return index;
        }
    }
    sub_f7db74(v0);
}
```

## `MainMenuController.WeaponButton` — RVA `0xcc3354`

- Decompiled symbol: `MainMenuController_WeaponButton`
- Metadata signature: `public void WeaponButton() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
void MainMenuController_WeaponButton(unsigned long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[20];
    if (v4)
    {
        GameObject__SetActive(v4, 1, 0);
        v4 = ptr[12];
        if (v4)
        {
            GameObject__SetActive(v4, 0, 0);
            v4 = ptr[6];
            if (ptr[6])
            {
                GameObject__SetActive();
                return;
            }
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.SettingButton` — RVA `0xcc33a0`

- Decompiled symbol: `MainMenuController_SettingButton`
- Metadata signature: `public void SettingButton() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
void MainMenuController_SettingButton(unsigned long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[22];
    if (v4)
    {
        GameObject__SetActive(v4, 1, 0);
        v4 = ptr[6];
        if (ptr[6])
        {
            GameObject__SetActive();
            return;
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.SettingClose` — RVA `0xcc33d8`

- Decompiled symbol: `MainMenuController_SettingClose`
- Metadata signature: `public void SettingClose() { }`
- Native interval: `60` bytes
- Result: `pseudocode`

```c
long long MainMenuController_SettingClose(unsigned long long *ptr)
{
    unsigned long v0;  // x0
    unsigned long long v1;  // x0

    v0 = ptr[22];
    if (v0)
    {
        GameObject__SetActive(v0, 0, 0);
        v0 = ptr[6];
        if (v0)
        {
            v1 = MainMenuController__ShowIntersititialAd(GameObject__SetActive(v0, 1, 0), 1, 0);
            return MainMenuController__ShowIntersititialAd(GameObject__SetActive(v0, 1, 0), 1, 0);
        }
    }
    sub_f7db74(v0);
}
```

## `MainMenuController.ShowIntersititialAd` — RVA `0xcc3414`

- Decompiled symbol: `MainMenuController_ShowIntersititialAd`
- Metadata signature: `public void ShowIntersititialAd() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1eee700;
extern long long g_1f082a0;
extern char g_1fab52d;

unsigned long long MainMenuController_ShowIntersititialAd(void)
{
    unsigned long long v0;  // x0
    unsigned long long v1;  // x0

    if (!(g_1fab52d & 1))
    {
        sub_f7d92c(&g_1eee700);
        sub_f7d92c(&g_1f082a0);
        g_1fab52d = 1;
    }
    v0 = PlayerPrefs__GetInt(g_1f082a0, 0);
    if ((unsigned int)v0 == 1)
        return v0;
    if (g_1eee700->field_b8->field_0)
    {
        v1 = AdsManager__Show_Interstitial();
        return AdsManager__Show_Interstitial();
    }
    sub_f7db74(0);
}
```

## `MainMenuController.ModeBack` — RVA `0xcc349c`

- Decompiled symbol: `MainMenuController_ModeBack`
- Metadata signature: `public void ModeBack() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
void MainMenuController_ModeBack(unsigned long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[18];
    if (v4)
    {
        GameObject__SetActive(v4, 0, 0);
        v4 = ptr[12];
        if (v4)
        {
            GameObject__SetActive(v4, 1, 0);
            v4 = ptr[6];
            if (ptr[6])
            {
                GameObject__SetActive();
                return;
            }
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.Survival_Back` — RVA `0xcc34e8`

- Decompiled symbol: `MainMenuController_Survival_Back`
- Metadata signature: `public void Survival_Back() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
void MainMenuController_Survival_Back(long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[43];
    if (v4)
    {
        GameObject__SetActive(v4, 1, 0);
        v4 = ptr[45];
        if (v4)
        {
            GameObject__SetActive(v4, 0, 0);
            v4 = ptr[44];
            if (ptr[44])
            {
                GameObject__SetActive();
                return;
            }
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.WeaponBack` — RVA `0xcc3534`

- Decompiled symbol: `MainMenuController_WeaponBack`
- Metadata signature: `public void WeaponBack() { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
unsigned long long MainMenuController_WeaponBack(unsigned long long *ptr)
{
    unsigned long v0;  // x0
    unsigned long long v1;  // x0

    v0 = ptr[20];
    if (v0)
    {
        GameObject__SetActive(v0, 0, 0);
        v0 = ptr[12];
        if (v0)
        {
            GameObject__SetActive(v0, 1, 0);
            v0 = ptr[6];
            if (v0)
            {
                GameObject__SetActive(v0, 1, 0);
                v1 = MainMenuController__ShowIntersititialAd();
                return MainMenuController__ShowIntersititialAd();
            }
        }
    }
    sub_f7db74(v0);
}
```

## `MainMenuController.WeaponBack2` — RVA `0xcc3584`

- Decompiled symbol: `MainMenuController_WeaponBack2`
- Metadata signature: `public void WeaponBack2() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
void MainMenuController_WeaponBack2(long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[19];
    if (v4)
    {
        GameObject__SetActive(v4, 0, 0);
        v4 = ptr[20];
        if (v4)
        {
            GameObject__SetActive(v4, 1, 0);
            v4 = ptr[21];
            if (ptr[21])
            {
                GameObject__SetActive();
                return;
            }
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.MissionMode` — RVA `0xcc35d0`

- Decompiled symbol: `MainMenuController_MissionMode`
- Metadata signature: `public void MissionMode() { }`
- Native interval: `100` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MainMenuController_Recovered` matched 3 offsets against `MainMenuController` metadata (confidence 1.00).

```c
typedef struct MainMenuController_Recovered {
    char padding_0[80];
    long long Unlockall_levels;
    char padding_58[56];
    long long ModeSelection;
    char padding_98[224];
    unsigned int j;
} MainMenuController_Recovered;

void MainMenuController_MissionMode(struct_0 *ptr, unsigned long a1)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x8
    long long v5;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr->field_178 + 1;
    ptr->field_178 = v4;
    if (((char)v4 & 1))
    {
        v5 = ptr->field_50;
        if (!v5)
            goto LABEL_10c3630;
        GameObject__SetActive(v5, 1, 0);
    }
    v5 = ptr->field_90;
    if (v5)
    {
        GameObject__SetActive(v5, 0, 0);
        MainMenuController__ShowInMenu_Loading();
        MonoBehaviour__StartCoroutine();
        return;
    }
LABEL_10c3630:
    sub_f7db74(v5);
}
```

## `MainMenuController.ShowInMenu_Loading` — RVA `0xcc3634`

- Decompiled symbol: `MainMenuController_ShowInMenu_Loading`
- Metadata signature: `private IEnumerator ShowInMenu_Loading(GameObject _panel) { }`
- Native interval: `136` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MainMenuController_Recovered` matched 2 offsets against `MainMenuController` metadata (confidence 0.67).

```c
typedef struct MainMenuController_Recovered {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long loadimage;
    long long loadimage2;
} MainMenuController_Recovered;

extern long long g_1ef3478;
extern char g_1fab527;

struct_0 * MainMenuController_ShowInMenu_Loading(long long a0, long long a1)
{
    struct_0 *v0;  // x21
    struct_0 *ptr;  // x0
    struct_0 *p;  // x0

    if (!(g_1fab527 & 1))
    {
        sub_f7d92c(&g_1ef3478);
        g_1fab527 = 1;
    }
    v0 = sub_f7db70(g_1ef3478);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    p = ptr;
    p->field_28 = a1;
    sub_f7d8d0(&p->field_28, a1);
    return p;
}
```

## `MainMenuController.Survival_Mode` — RVA `0xcc36bc`

- Decompiled symbol: `MainMenuController_Survival_Mode`
- Metadata signature: `public void Survival_Mode() { }`
- Native interval: `84` bytes
- Result: `pseudocode`

```c
void MainMenuController_Survival_Mode(long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[43];
    if (v4)
    {
        GameObject__SetActive(v4, 0, 0);
        v4 = ptr[45];
        if (v4)
        {
            GameObject__SetActive(v4, 0, 0);
            MainMenuController__ShowInMenu_Loading(ptr, ptr[44]);
            MonoBehaviour__StartCoroutine();
            return;
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.Sniper_Mode` — RVA `0xcc3710`

- Decompiled symbol: `MainMenuController_Sniper_Mode`
- Metadata signature: `public void Sniper_Mode() { }`
- Native interval: `84` bytes
- Result: `pseudocode`

```c
void MainMenuController_Sniper_Mode(long long *ptr, unsigned long a1)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[43];
    if (v4)
    {
        GameObject__SetActive(v4, 0, 0);
        v4 = ptr[44];
        if (v4)
        {
            GameObject__SetActive(v4, 0, 0);
            MainMenuController__ShowInMenu_Loading(ptr, ptr[45]);
            MonoBehaviour__StartCoroutine();
            return;
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.<ShowInMenu_Loading>d__71.ctor` — RVA `0xcc3764`

- Decompiled symbol: `MainMenuController_ShowInMenu_Loading_d__71_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void MainMenuController_ShowInMenu_Loading_d__71_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `MainMenuController.LevelSelectionBack` — RVA `0xcc378c`

- Decompiled symbol: `MainMenuController_LevelSelectionBack`
- Metadata signature: `public void LevelSelectionBack() { }`
- Native interval: `60` bytes
- Result: `pseudocode`

```c
unsigned long long MainMenuController_LevelSelectionBack(long long *ptr)
{
    long long v0;  // x0
    unsigned long long v1;  // x0

    v0 = ptr[18];
    if (v0)
    {
        GameObject__SetActive(v0, 1, 0);
        v0 = ptr[24];
        if (v0)
        {
            GameObject__SetActive(v0, 0, 0);
            v1 = MainMenuController__ShowIntersititialAd();
            return MainMenuController__ShowIntersititialAd();
        }
    }
    sub_f7db74(v0);
}
```

## `MainMenuController.MoreGames` — RVA `0xcc37c8`

- Decompiled symbol: `MainMenuController_MoreGames`
- Metadata signature: `public void MoreGames() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eee870;
extern long long g_1f12e38;
extern char g_1fab528;

void MainMenuController_MoreGames(void)
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
    if (!(g_1fab528 & 1))
    {
        sub_f7d92c(&g_1eee870);
        sub_f7d92c(&g_1f12e38);
        g_1fab528 = 1;
    }
    if (!g_1eee870->field_e0)
        sub_f7da5c(g_1eee870);
}
```

## `MainMenuController.Quite` — RVA `0xcc3830`

- Decompiled symbol: `MainMenuController_Quite`
- Metadata signature: `public void Quite() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
void MainMenuController_Quite(unsigned long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[23];
    if (v4)
    {
        GameObject__SetActive(v4, 1, 0);
        v4 = ptr[6];
        if (ptr[6])
        {
            GameObject__SetActive();
            return;
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.QuiteFun` — RVA `0xcc3868`

- Decompiled symbol: `MainMenuController_QuiteFun`
- Metadata signature: `public void QuiteFun() { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eee870;
extern char g_1fab529;

void MainMenuController_QuiteFun(void)
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
    if (!(g_1fab529 & 1))
    {
        sub_f7d92c(&g_1eee870);
        g_1fab529 = 1;
    }
    if (!g_1eee870->field_e0)
        sub_f7da5c(g_1eee870);
}
```

## `MainMenuController.OnMusic` — RVA `0xcc38b8`

- Decompiled symbol: `MainMenuController_OnMusic`
- Metadata signature: `public void OnMusic() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
void MainMenuController_OnMusic(unsigned long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[28];
    if (v4)
    {
        GameObject__SetActive(v4, 1, 0);
        v4 = ptr[29];
        if (v4)
        {
            GameObject__SetActive(v4, 0, 0);
            v4 = ptr[27];
            if (ptr[27])
            {
                GameObject__SetActive();
                return;
            }
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.OffMusic` — RVA `0xcc3904`

- Decompiled symbol: `MainMenuController_OffMusic`
- Metadata signature: `public void OffMusic() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
void MainMenuController_OffMusic(unsigned long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[28];
    if (v4)
    {
        GameObject__SetActive(v4, 0, 0);
        v4 = ptr[29];
        if (v4)
        {
            GameObject__SetActive(v4, 1, 0);
            v4 = ptr[27];
            if (ptr[27])
            {
                GameObject__SetActive();
                return;
            }
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.HighQuality` — RVA `0xcc3950`

- Decompiled symbol: `MainMenuController_HighQuality`
- Metadata signature: `public void HighQuality() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
void MainMenuController_HighQuality(long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    QualitySettings__set_antiAliasing(4, 0);
    v4 = ptr[30];
    if (v4)
    {
        GameObject__SetActive(v4, 1, 0);
        v4 = ptr[31];
        if (v4)
        {
            GameObject__SetActive(v4, 0, 0);
            v4 = ptr[32];
            if (ptr[32])
            {
                GameObject__SetActive();
                return;
            }
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.MediumQuality` — RVA `0xcc39a8`

- Decompiled symbol: `MainMenuController_MediumQuality`
- Metadata signature: `public void MediumQuality() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
void MainMenuController_MediumQuality(long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    QualitySettings__set_antiAliasing(2, 0);
    v4 = ptr[30];
    if (v4)
    {
        GameObject__SetActive(v4, 0, 0);
        v4 = ptr[31];
        if (v4)
        {
            GameObject__SetActive(v4, 1, 0);
            v4 = ptr[32];
            if (ptr[32])
            {
                GameObject__SetActive();
                return;
            }
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.LowQuality` — RVA `0xcc3a00`

- Decompiled symbol: `MainMenuController_LowQuality`
- Metadata signature: `public void LowQuality() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
void MainMenuController_LowQuality(long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    QualitySettings__set_antiAliasing(0, 0);
    v4 = ptr[30];
    if (v4)
    {
        GameObject__SetActive(v4, 0, 0);
        v4 = ptr[31];
        if (v4)
        {
            GameObject__SetActive(v4, 0, 0);
            v4 = ptr[32];
            if (ptr[32])
            {
                GameObject__SetActive();
                return;
            }
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.Simplelevels` — RVA `0xcc3a58`

- Decompiled symbol: `MainMenuController_Simplelevels`
- Metadata signature: `public void Simplelevels() { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
void MainMenuController_Simplelevels(long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[25];
    if (v4)
    {
        GameObject__SetActive(v4, 0, 0);
        v4 = ptr[26];
        if (v4)
        {
            GameObject__SetActive(v4, 1, 0);
            v4 = ptr[38];
            if (v4)
            {
                GameObject__SetActive(v4, 0, 0);
                v4 = ptr[39];
                if (ptr[39])
                {
                    GameObject__SetActive();
                    return;
                }
            }
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.Mediumlevels` — RVA `0xcc3ab8`

- Decompiled symbol: `MainMenuController_Mediumlevels`
- Metadata signature: `public void Mediumlevels() { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
void MainMenuController_Mediumlevels(long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[25];
    if (v4)
    {
        GameObject__SetActive(v4, 1, 0);
        v4 = ptr[26];
        if (v4)
        {
            GameObject__SetActive(v4, 0, 0);
            v4 = ptr[38];
            if (v4)
            {
                GameObject__SetActive(v4, 1, 0);
                v4 = ptr[39];
                if (ptr[39])
                {
                    GameObject__SetActive();
                    return;
                }
            }
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.Hardlevels` — RVA `0xcc3b18`

- Decompiled symbol: `MainMenuController_Hardlevels`
- Metadata signature: `public void Hardlevels() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
void MainMenuController_Hardlevels(long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[25];
    if (v4)
    {
        GameObject__SetActive(v4, 0, 0);
        v4 = ptr[26];
        if (ptr[26])
        {
            GameObject__SetActive();
            return;
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.DifficultyBack` — RVA `0xcc3b50`

- Decompiled symbol: `MainMenuController_DifficultyBack`
- Metadata signature: `public void DifficultyBack() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
void MainMenuController_DifficultyBack(long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[25];
    if (v4)
    {
        GameObject__SetActive(v4, 0, 0);
        v4 = ptr[26];
        if (ptr[26])
        {
            GameObject__SetActive();
            return;
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.DifficultyMenu` — RVA `0xcc3b88`

- Decompiled symbol: `MainMenuController_DifficultyMenu`
- Metadata signature: `public void DifficultyMenu() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
void MainMenuController_DifficultyMenu(unsigned long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[24];
    if (v4)
    {
        GameObject__SetActive(v4, 0, 0);
        v4 = ptr[12];
        if (v4)
        {
            GameObject__SetActive(v4, 1, 0);
            v4 = ptr[6];
            if (ptr[6])
            {
                GameObject__SetActive();
                return;
            }
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.DifficultyWeapons` — RVA `0xcc3bd4`

- Decompiled symbol: `MainMenuController_DifficultyWeapons`
- Metadata signature: `public void DifficultyWeapons() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
void MainMenuController_DifficultyWeapons(unsigned long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[24];
    if (v4)
    {
        GameObject__SetActive(v4, 0, 0);
        v4 = ptr[19];
        if (v4)
        {
            GameObject__SetActive(v4, 1, 0);
            v4 = ptr[21];
            if (ptr[21])
            {
                GameObject__SetActive();
                return;
            }
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.WeaponsNext` — RVA `0xcc3c20`

- Decompiled symbol: `MainMenuController_WeaponsNext`
- Metadata signature: `public void WeaponsNext() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
void MainMenuController_WeaponsNext(unsigned long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[19];
    if (v4)
    {
        GameObject__SetActive(v4, 0, 0);
        v4 = ptr[21];
        if (v4)
        {
            GameObject__SetActive(v4, 0, 0);
            v4 = ptr[18];
            if (ptr[18])
            {
                GameObject__SetActive();
                return;
            }
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.QuitPanelClose` — RVA `0xcc3c6c`

- Decompiled symbol: `MainMenuController_QuitPanelClose`
- Metadata signature: `public void QuitPanelClose() { }`
- Native interval: `60` bytes
- Result: `pseudocode`

```c
unsigned long long MainMenuController_QuitPanelClose(unsigned long long *ptr)
{
    unsigned long v0;  // x0
    unsigned long long v1;  // x0

    v0 = ptr[23];
    if (v0)
    {
        GameObject__SetActive(v0, 0, 0);
        v0 = ptr[6];
        if (v0)
        {
            GameObject__SetActive(v0, 1, 0);
            v1 = MainMenuController__ShowIntersititialAd();
            return MainMenuController__ShowIntersititialAd();
        }
    }
    sub_f7db74(v0);
}
```

## `MainMenuController.ProStorePanelBack` — RVA `0xcc3ca8`

- Decompiled symbol: `MainMenuController_ProStorePanelBack`
- Metadata signature: `public void ProStorePanelBack() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
void MainMenuController_ProStorePanelBack(unsigned long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[34];
    if (v4)
    {
        GameObject__SetActive(v4, 0, 0);
        v4 = ptr[6];
        if (ptr[6])
        {
            GameObject__SetActive();
            return;
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.ProStorePanel` — RVA `0xcc3ce0`

- Decompiled symbol: `MainMenuController_ProStorePanel`
- Metadata signature: `public void ProStorePanel() { }`
- Native interval: `212` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MainMenuController_Recovered` matched 10 offsets against `MainMenuController` metadata (confidence 1.00).

```c
typedef struct MainMenuController_Recovered {
    char padding_0[48];
    unsigned long long Character;
    char padding_38[32];
    unsigned long long Unlock_Everything;
    char padding_60[176];
    unsigned long long ProStore;
    unsigned long long SpecialOffer;
    unsigned long long SpecialPack;
    unsigned long long WeaponPack;
    char padding_130[16];
    unsigned long long Button1;
    unsigned long long Button2;
    unsigned long long Button3;
    char padding_158[36];
    unsigned int k;
} MainMenuController_Recovered;

void MainMenuController_ProStorePanel(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x8
    unsigned long v5;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr->field_17c + 1;
    ptr->field_17c = v4;
    if (((char)v4 & 1))
    {
        v5 = ptr->field_58;
        if (!v5)
            goto LABEL_10c3db0;
        GameObject__SetActive(v5, 1, 0);
    }
    v5 = ptr->field_110;
    if (v5)
    {
        GameObject__SetActive(v5, 1, 0);
        v5 = ptr->field_30;
        if (v5)
        {
            GameObject__SetActive(v5, 0, 0);
            v5 = ptr->field_118;
            if (v5)
            {
                GameObject__SetActive(v5, 1, 0);
                v5 = ptr->field_120;
                if (v5)
                {
                    GameObject__SetActive(v5, 0, 0);
                    v5 = ptr->field_128;
                    if (v5)
                    {
                        GameObject__SetActive(v5, 0, 0);
                        v5 = ptr->field_140;
                        if (v5)
                        {
                            GameObject__SetActive(v5, 1, 0);
                            v5 = ptr->field_148;
                            if (v5)
                            {
                                GameObject__SetActive(v5, 0, 0);
                                v5 = ptr->field_150;
                                if (v5)
                                {
                                    GameObject__SetActive();
                                    return;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
LABEL_10c3db0:
    sub_f7db74(v5);
}
```

## `MainMenuController.Special_Pack` — RVA `0xcc3db4`

- Decompiled symbol: `MainMenuController_Special_Pack`
- Metadata signature: `public void Special_Pack() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
void MainMenuController_Special_Pack(long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[35];
    if (v4)
    {
        GameObject__SetActive(v4, 0, 0);
        v4 = ptr[36];
        if (v4)
        {
            GameObject__SetActive(v4, 1, 0);
            v4 = ptr[37];
            if (v4)
            {
                GameObject__SetActive(v4, 0, 0);
                v4 = ptr[40];
                if (v4)
                {
                    GameObject__SetActive(v4, 0, 0);
                    v4 = ptr[41];
                    if (v4)
                    {
                        GameObject__SetActive(v4, 1, 0);
                        v4 = ptr[42];
                        if (ptr[42])
                        {
                            GameObject__SetActive();
                            return;
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.Weapon_Pack` — RVA `0xcc3e3c`

- Decompiled symbol: `MainMenuController_Weapon_Pack`
- Metadata signature: `public void Weapon_Pack() { }`
- Native interval: `176` bytes
- Result: `pseudocode`

```c
void MainMenuController_Weapon_Pack(unsigned long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[34];
    if (v4)
    {
        GameObject__SetActive(v4, 1, 0);
        v4 = ptr[6];
        if (v4)
        {
            GameObject__SetActive(v4, 0, 0);
            v4 = ptr[35];
            if (v4)
            {
                GameObject__SetActive(v4, 0, 0);
                v4 = ptr[36];
                if (v4)
                {
                    GameObject__SetActive(v4, 0, 0);
                    v4 = ptr[37];
                    if (v4)
                    {
                        GameObject__SetActive(v4, 1, 0);
                        v4 = ptr[40];
                        if (v4)
                        {
                            GameObject__SetActive(v4, 0, 0);
                            v4 = ptr[41];
                            if (v4)
                            {
                                GameObject__SetActive(v4, 0, 0);
                                v4 = ptr[42];
                                if (ptr[42])
                                {
                                    GameObject__SetActive();
                                    return;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.PrimaryWeapon` — RVA `0xcc3eec`

- Decompiled symbol: `MainMenuController_PrimaryWeapon`
- Metadata signature: `public void PrimaryWeapon() { }`
- Native interval: `192` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MainMenuController_Recovered` matched 9 offsets against `MainMenuController` metadata (confidence 1.00).

```c
typedef struct MainMenuController_Recovered {
    char padding_0[72];
    long long GunPanelAdver;
    char padding_50[32];
    long long PrimaryWPanel;
    long long PrimaryGuns;
    long long SecondaryWPanel;
    long long SecondaryGuns;
    char padding_90[8];
    long long WeaponSelection;
    long long Weapon_Selection;
    long long ALLWeapons;
    char padding_b0[196];
    unsigned int i;
} MainMenuController_Recovered;

void MainMenuController_PrimaryWeapon(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x8
    long long v5;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr->field_174 + 1;
    ptr->field_174 = v4;
    if (((char)v4 & 1))
    {
        v5 = ptr->field_48;
        if (!v5)
            goto LABEL_10c3fa8;
        GameObject__SetActive(v5, 1, 0);
    }
    v5 = ptr->field_98;
    if (v5)
    {
        GameObject__SetActive(v5, 1, 0);
        v5 = ptr->field_a0;
        if (v5)
        {
            GameObject__SetActive(v5, 0, 0);
            v5 = ptr->field_a8;
            if (v5)
            {
                GameObject__SetActive(v5, 1, 0);
                v5 = ptr->field_70;
                if (v5)
                {
                    GameObject__SetActive(v5, 1, 0);
                    v5 = ptr->field_78;
                    if (v5)
                    {
                        GameObject__SetActive(v5, 1, 0);
                        v5 = ptr->field_88;
                        if (v5)
                        {
                            GameObject__SetActive(v5, 0, 0);
                            v5 = ptr->field_80;
                            if (v5)
                            {
                                GameObject__SetActive();
                                return;
                            }
                        }
                    }
                }
            }
        }
    }
LABEL_10c3fa8:
    sub_f7db74(v5);
}
```

## `MainMenuController.SecondaryWeapon` — RVA `0xcc3fac`

- Decompiled symbol: `MainMenuController_SecondaryWeapon`
- Metadata signature: `public void SecondaryWeapon() { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
void MainMenuController_SecondaryWeapon(unsigned long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[20];
    if (v4)
    {
        GameObject__SetActive(v4, 0, 0);
        v4 = ptr[19];
        if (v4)
        {
            GameObject__SetActive(v4, 1, 0);
            v4 = ptr[21];
            if (v4)
            {
                GameObject__SetActive(v4, 1, 0);
                v4 = ptr[14];
                if (v4)
                {
                    GameObject__SetActive(v4, 0, 0);
                    v4 = ptr[15];
                    if (v4)
                    {
                        GameObject__SetActive(v4, 0, 0);
                        v4 = ptr[17];
                        if (v4)
                        {
                            GameObject__SetActive(v4, 1, 0);
                            v4 = ptr[16];
                            if (ptr[16])
                            {
                                GameObject__SetActive();
                                return;
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.GetFreeRewards` — RVA `0xcc4048`

- Decompiled symbol: `MainMenuController_GetFreeRewards`
- Metadata signature: `public void GetFreeRewards() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long MainMenuController_GetFreeRewards(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `MainMenuController.PrivacyPolicy` — RVA `0xcc404c`

- Decompiled symbol: `MainMenuController_PrivacyPolicy`
- Metadata signature: `public void PrivacyPolicy() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
void MainMenuController_PrivacyPolicy(unsigned long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[13];
    if (v4)
    {
        GameObject__SetActive(v4, 1, 0);
        v4 = ptr[6];
        if (ptr[6])
        {
            GameObject__SetActive();
            return;
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.PrivacyPolicyClose` — RVA `0xcc4084`

- Decompiled symbol: `MainMenuController_PrivacyPolicyClose`
- Metadata signature: `public void PrivacyPolicyClose() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
void MainMenuController_PrivacyPolicyClose(unsigned long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[13];
    if (v4)
    {
        GameObject__SetActive(v4, 0, 0);
        v4 = ptr[6];
        if (ptr[6])
        {
            GameObject__SetActive();
            return;
        }
    }
    sub_f7db74(v4);
}
```

## `MainMenuController.PrivacyPolicyLink` — RVA `0xcc40bc`

- Decompiled symbol: `MainMenuController_PrivacyPolicyLink`
- Metadata signature: `public void PrivacyPolicyLink() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eee870;
extern char g_1fab52a;

void MainMenuController_PrivacyPolicyLink(void)
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
    if (!(g_1fab52a & 1))
    {
        sub_f7d92c(&g_1eee870);
        sub_f7d92c("\r3");
        g_1fab52a = 1;
    }
    if (!g_1eee870->field_e0)
        sub_f7da5c(g_1eee870);
}
```

## `MainMenuController.Advertisement` — RVA `0xcc4124`

- Decompiled symbol: `MainMenuController_Advertisement`
- Metadata signature: `public void Advertisement() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eee870;
extern long long g_1f12e28;
extern char g_1fab52b;

void MainMenuController_Advertisement(void)
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
    if (!(g_1fab52b & 1))
    {
        sub_f7d92c(&g_1eee870);
        sub_f7d92c(&g_1f12e28);
        g_1fab52b = 1;
    }
    if (!g_1eee870->field_e0)
        sub_f7da5c(g_1eee870);
}
```

## `MainMenuController.RateUs` — RVA `0xcc418c`

- Decompiled symbol: `MainMenuController_RateUs`
- Metadata signature: `public void RateUs() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eee870;
extern long long g_1f12e30;
extern char g_1fab52c;

void MainMenuController_RateUs(void)
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
    if (!(g_1fab52c & 1))
    {
        sub_f7d92c(&g_1eee870);
        sub_f7d92c(&g_1f12e30);
        g_1fab52c = 1;
    }
    if (!g_1eee870->field_e0)
        sub_f7da5c(g_1eee870);
}
```

## `MainMenuController.ctor` — RVA `0xcc41f4`

- Decompiled symbol: `MainMenuController_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long MainMenuController_ctor(void)
{
}
```

## `MainMenuController.cctor` — RVA `0xcc41fc`

- Decompiled symbol: `MainMenuController_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `84` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[8];
    char field_8;
    char padding_9[3];
    unsigned int field_c;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

extern struct_1 *g_1ef0750;
extern char g_1fab52e;

unsigned long long MainMenuController_cctor(void)
{
    unsigned long long v0;  // x0
    struct_0 *ptr;  // x8

    if (!(g_1fab52e & 1))
    {
        v0 = sub_f7d92c(&g_1ef0750);
        g_1fab52e = 1;
    }
    ptr = g_1ef0750->field_b8;
    ptr->field_8 = 1;
    ptr->field_c = 3;
    return v0;
}
```

## `MainMenuController.<ShowInMenu_Loading>d__71.Dispose` — RVA `0xcc4250`

- Decompiled symbol: `MainMenuController_ShowInMenu_Loading_d__71_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long MainMenuController_ShowInMenu_Loading_d__71_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `MainMenuController.<ShowInMenu_Loading>d__71.MoveNext` — RVA `0xcc4254`

- Decompiled symbol: `MainMenuController_ShowInMenu_Loading_d__71_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `232` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_0 *field_20;
    long long field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[432];
    long long field_1b0;
} struct_0;

extern long long g_1ef2440;
extern char g_1fab52f;

unsigned int MainMenuController_ShowInMenu_Loading_d__71_MoveNext(struct_1 *ptr)
{
    struct_0 *v0;  // x8
    long long v1;  // x21
    struct_1 *p;  // x19

    if (!(g_1fab52f & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab52f = 1;
    }
    v0 = ptr->field_20;
    if (ptr->field_10 == 1)
    {
        ptr->field_10 = 4294967295;
        if (!v0)
            sub_f7db74();
        if (v0->field_1b0)
        {
            GameObject__SetActive(v0->field_1b0, 0, 0);
            if (!ptr->field_28)
                sub_f7db74();
            GameObject__SetActive(ptr->field_28, 1, 0);
        }
        else
        {
            sub_f7db74();
        }
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        if (!v0)
            sub_f7db74();
        if (v0->field_1b0)
        {
            GameObject__SetActive(v0->field_1b0, 1, 0);
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

## `MainMenuController.<ShowInMenu_Loading>d__71.get_Current` — RVA `0xcc433c`

- Decompiled symbol: `MainMenuController_ShowInMenu_Loading_d__71_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long MainMenuController_ShowInMenu_Loading_d__71_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `MainMenuController.<ShowInMenu_Loading>d__71.Reset` — RVA `0xcc4344`

- Decompiled symbol: `MainMenuController_ShowInMenu_Loading_d__71_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f048c0;

void MainMenuController_ShowInMenu_Loading_d__71_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f048c0));
}
```

## `MainMenuController.<ShowInMenu_Loading>d__71.get_Current` — RVA `0xcc437c`

- Decompiled symbol: `MainMenuController_ShowInMenu_Loading_d__71_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long MainMenuController_ShowInMenu_Loading_d__71_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
