# Native pseudocode: GameController

> Metadata source-path string: `Assets/Script/GameController.cs`. This is a path string from the APK metadata, not recovered source text.

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GameController.Awake` — RVA `0xcbfd3c`

- Decompiled symbol: `GameController_Awake`
- Metadata signature: `private void Awake() { }`
- Native interval: `436` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GameController_Recovered` matched 3 offsets against `GameController` metadata (confidence 1.00).

```c
typedef struct GameController_Recovered {
    char padding_0[152];
    long long MainPlayer;
    long long Player;
    char padding_a8[80];
    unsigned long long PlayerPosition;
} GameController_Recovered;

extern long long g_1f0bd20;
extern char g_1fab4fc;

void GameController_Awake(struct_0 *ptr)
{
    unsigned long long v7;  // d9
    unsigned long long v8;  // d8
    long long v17;  // x20
    unsigned long long v18;  // x22
    unsigned long long v19;  // x22
    long long v20;  // x0
    unsigned long long v21;  // x20
    unsigned long long v9;  // x30
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    long long v14;  // x0
    long long v15;  // x0
    unsigned long long v16;  // x22
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x38]
    unsigned long long v2;  // [bp-0x30]
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
    if (!(g_1fab4fc & 1))
    {
        sub_f7d92c(&g_1f0bd20);
        g_1fab4fc = 1;
    }
    v14 = ptr->field_98;
    if (v14)
    {
        v15 = GameObject__get_transform(v14, 0);
        v16 = ptr->field_f8;
        v17 = v15;
        v14 = PlayerPrefs__GetInt(g_1f0bd20, 0);
        if (v16)
        {
            if (*((int *)(v16 + 24)) <= (int)v14)
                goto LABEL_10bfeec;
            v14 = *((long long *)(v16 + (v14 & 4294967295) * 8 + 32));
            if (v14 && !((v14 = GameObject__get_transform(v14, 0), !v14)))
            {
                Transform__get_eulerAngles();
                v18 = ptr->field_f8;
                v14 = PlayerPrefs__GetInt(g_1f0bd20, 0);
                if (v18)
                {
                    if (*((int *)(v18 + 24)) <= (int)v14)
                        goto LABEL_10bfeec;
                    v14 = *((long long *)(v18 + (v14 & 4294967295) * 8 + 32));
                    if (v14 && !((v14 = GameObject__get_transform(v14, 0), !v14)))
                    {
                        Transform__get_eulerAngles();
                        v19 = ptr->field_f8;
                        v14 = PlayerPrefs__GetInt(g_1f0bd20, 0);
                        if (v19)
                        {
                            if (*((int *)(v19 + 24)) <= (int)v14)
                                goto LABEL_10bfeec;
                            v14 = *((long long *)(v19 + (v14 & 4294967295) * 8 + 32));
                            if (v14 && !((v14 = GameObject__get_transform(v14, 0), !v14 || (v14 = (long long)(unsigned long long)Transform__get_eulerAngles(), !v17 || (Transform__set_eulerAngles(v17, 0), v14 = ptr->field_a0, !v14)))))
                            {
                                v20 = GameObject__get_transform(v14, 0);
                                v21 = ptr->field_f8;
                                v14 = PlayerPrefs__GetInt(g_1f0bd20, 0);
                                if (v21)
                                {
                                    if (*((int *)(v21 + 24)) <= (int)v14)
                                        goto LABEL_10bfeec;
                                    v14 = *((long long *)(v21 + (v14 & 4294967295) * 8 + 32));
                                    if (v14)
                                    {
                                        v14 = GameObject__get_transform(v14, 0);
                                        if (v14)
                                        {
                                            v14 = Transform__get_position();
                                            if (v20)
                                            {
                                                Transform__set_position();
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
    v14 = sub_f7db74(v14);
LABEL_10bfeec:
    sub_f7db7c(v14);
}
```

## `GameController.Start` — RVA `0xcbfef0`

- Decompiled symbol: `GameController_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `592` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GameController_Recovered` matched 12 offsets against `GameController` metadata (confidence 1.00).

```c
typedef struct GameController_Recovered {
    char padding_0[32];
    unsigned int LevelNumber;
    char padding_24[76];
    long long Nextbutton;
    char padding_78[152];
    struct struct_3 *LevelCounter;
    unsigned int EnemyCounter;
    char padding_11c[4];
    unsigned long long EnemiesValue;
    char padding_128[16];
    long long EnemyCountText;
    long long SurvivalEnemyCounter;
    char padding_148[96];
    unsigned int Timer;
    char padding_1ac[1];
    unsigned short MusicOnOff;
    char padding_1af[129];
    long long DostHealthBar;
    long long _2ndZoomBtn;
    unsigned long long _gunChangeBtn;
} GameController_Recovered;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_7 {
    char padding_0[32];
    long long field_20;
} struct_7;

typedef struct struct_6 {
    char padding_0[184];
    struct struct_5 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_6;

typedef struct struct_5 {
    char padding_0[12];
    unsigned int field_c;
} struct_5;

typedef struct struct_2 {
    char padding_0[184];
    void* field_b8;
} struct_2;

extern struct_2 *g_1eefae8;
extern struct_6 *g_1ef0750;
extern long long g_1f0bd20;
extern char g_1fab4fd;

void GameController_Start(struct_4 *ptr)
{
    void* p;  // x0
    unsigned long v1;  // x0
    struct_3 *v2;  // x8
    struct_7 *v3;  // x8
    unsigned long v4;  // x8
    unsigned long long v5;  // x9
    struct_6 *v6;  // x0

    if (!(g_1fab4fd & 1))
    {
        sub_f7d92c(&g_1eefae8);
        sub_f7d92c(&g_1ef0750);
        sub_f7d92c(&g_1f0bd20);
        g_1fab4fd = 1;
    }
    p = g_1eefae8->field_b8;
    *((unsigned int *)&p[24]) = 0;
    *((unsigned long *)&p[16]) = 0;
    *((unsigned int *)&p[32]) = 0;
    *((unsigned short *)&(&ptr->padding_1ac)[1]) = 257;
    ptr->field_1a8 = 0x41a00000;
    *((struct_4 **)&p[8]) = ptr;
    sub_f7d8d0(p + 8, ptr);
    *((unsigned int *)&g_1eefae8->field_b8[16]) = 0;
    v1 = PlayerPrefs__GetInt(g_1f0bd20, 0);
    v2 = ptr->field_110;
    ptr->field_20 = v1;
    if (v2)
    {
        if (v2->field_18 <= (unsigned int)v1)
            sub_f7db7c(v1);
        v3 = &v2->padding_0[8 * (v1 & 4294967295)];
        if (v3->field_20)
        {
            GameObject__SetActive(v3->field_20, 1, 0);
            if (1 >= ptr->field_20 - 31)
            {
                if (ptr->field_138 && Component__get_gameObject(ptr->field_138, 0) && (GameObject__SetActive(), ptr->field_140 && Component__get_gameObject(ptr->field_140, 0)))
                {
                    GameObject__SetActive();
                    v4 = ptr->field_20;
                    goto LABEL_10c0084;
                }
            }
            else
            {
                if (ptr->field_140 && Component__get_gameObject(ptr->field_140, 0) && (GameObject__SetActive(), ptr->field_138 && Component__get_gameObject(ptr->field_138, 0) && (v1 = (unsigned long)GameObject__SetActive(), v5 = ptr->field_120, v5)))
                {
                    v4 = ptr->field_20;
                    if (*((int *)(v5 + 24)) <= (unsigned int)v4)
                        sub_f7db7c(GameObject__SetActive());
                    ptr->field_118 = *((int *)(v5 + (v4 * 0x100000000 >> 63 & 0xffffffff00000000 | v4 & 4294967295) * 4 + 32));
LABEL_10c0084:
                    if ((unsigned int)v4 != 30)
                    {
LABEL_10c00a4:
                        if ((unsigned int)v4 != 5 && (unsigned int)v4 != 2)
                            return;
                        v6 = g_1ef0750;
                        if (!g_1ef0750->field_e0)
                        {
                            sub_f7da5c(g_1ef0750);
                            v6 = g_1ef0750;
                        }
                        if (v6->field_b8->field_c == 3)
                        {
                            if (*((long long *)&ptr->padding_1af[128]))
                            {
                                GameObject__SetActive(*((long long *)&ptr->padding_1af[128]), 1, 0);
                                goto LABEL_10c00f4;
                            }
                        }
                        else
                        {
LABEL_10c00f4:
                            if (ptr->field_230)
                            {
                                GameObject__SetActive(ptr->field_230, 1, 0);
                                if (ptr->field_238)
                                {
                                    GameObject__SetActive();
                                    return;
                                }
                            }
                        }
                    }
                    else if (ptr->field_70)
                    {
                        GameObject__SetActive(ptr->field_70, 0, 0);
                        v4 = ptr->field_20;
                        goto LABEL_10c00a4;
                    }
                }
            }
        }
    }
    sub_f7db7c(sub_f7db74());
}
```

## `GameController.Update` — RVA `0xcc0140`

- Decompiled symbol: `GameController_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `1424` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[320];
    struct struct_4 *field_140;
} struct_3;

typedef struct struct_1 {
    char padding_0[1512];
    struct struct_2 *field_5e8;
    unsigned long long field_5f0;
} struct_1;

typedef struct struct_4 {
    struct struct_1 *field_0;
} struct_4;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[184];
    unsigned long long field_b8;
} struct_0;

extern struct_0 *g_1eefae8;
extern long long g_1ef0750;
extern unsigned long long g_1f06220;
extern long long g_1f075e0;
extern long long g_1f0bb80;
extern long long g_1f0bd20;
extern char g_1fab4fe;

void GameController_Update(struct_3 *ptr)
{
    unsigned long long v10;  // d8
    unsigned long long v11;  // x30
    unsigned long v20;  // x0
    unsigned long long v21;  // x2
    unsigned long long v22;  // x1
    struct_1 **v23;  // x0
    unsigned long long v12;  // x25
    unsigned long long v13;  // x24
    unsigned long long v14;  // x23
    unsigned long long v15;  // x22
    unsigned long long v16;  // x21
    unsigned long long v17;  // x20
    unsigned long long v18;  // x19
    struct_1 **v19;  // x20
    unsigned long long v0;  // [bp-0x50]
    unsigned int flag;  // [bp-0x44]
    unsigned long long v2;  // [bp-0x40]
    unsigned long long v3;  // [bp-0x38]
    unsigned long long v4;  // [bp-0x30]
    unsigned long long v5;  // [bp-0x28]
    unsigned long long v6;  // [bp-0x20]
    unsigned long long v7;  // [bp-0x18]
    unsigned long long v8;  // [bp-0x10]
    unsigned long long v9;  // [bp-0x8]

    v0 = v10;
    v2 = v11;
    v3 = v12;
    v4 = v13;
    v5 = v14;
    v6 = v15;
    v7 = v16;
    v8 = v17;
    v9 = v18;
    if (!(g_1fab4fe & 1))
    {
        sub_f7d92c(&g_1eefae8);
        sub_f7d92c(&g_1ef0750);
        sub_f7d92c(&g_1f0bb80);
        sub_f7d92c(&g_1f075e0);
        sub_f7d92c(&g_1f0bd20);
        sub_f7d92c(&g_1f06220);
        sub_f7d92c("%%");
        g_1fab4fe = 1;
    }
    flag = 0;
    v19 = ptr->field_140;
    v20 = Int32__ToString(g_1eefae8->field_b8 + 16, 0);
    if (!v19)
        sub_f7db74();
    v21 = *(v19)->field_5f0;
    if (!v20)
        v22 = g_1f06220;
    else
        v22 = v20;
    v23 = v19;
    *(v19)->field_5e8();
}
```

## `GameController.SurvivalResult` — RVA `0xcc06d0`

- Decompiled symbol: `GameController_SurvivalResult`
- Metadata signature: `public void SurvivalResult() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
void GameController_SurvivalResult(unsigned long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    GameController__SurvivalPanelFunc();
    MonoBehaviour__StartCoroutine();
    return;
}
```

## `GameController.MissionComplete` — RVA `0xcc06f0`

- Decompiled symbol: `GameController_MissionComplete`
- Metadata signature: `private IEnumerator MissionComplete() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern char g_1fab505;

struct_0 * GameController_MissionComplete(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab505 & 1))
    {
        sub_f7d92c("Uj");
        g_1fab505 = 1;
    }
    v0 = sub_f7db70(g_1ef31c8);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```

## `GameController.SHowFail` — RVA `0xcc075c`

- Decompiled symbol: `GameController_SHowFail`
- Metadata signature: `private IEnumerator SHowFail() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern char g_1fab4ff;

struct_0 * GameController_SHowFail(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab4ff & 1))
    {
        sub_f7d92c("Yj");
        g_1fab4ff = 1;
    }
    v0 = sub_f7db70(g_1ef31d8);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```

## `GameController.<SHowFail>d__84.ctor` — RVA `0xcc07c8`

- Decompiled symbol: `GameController_SHowFail_d__84_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void GameController_SHowFail_d__84_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `GameController.ButtonPaused` — RVA `0xcc07f0`

- Decompiled symbol: `GameController_ButtonPaused`
- Metadata signature: `public void ButtonPaused() { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[128];
    long long field_80;
} struct_0;

int GameController_ButtonPaused(struct_0 *a0)
{
    if (a0->field_80)
    {
        GameObject__SetActive(a0->field_80, 1, 0);
        return GameController__ShowIntersititialAd(Time__set_timeScale(0));
    }
    sub_f7db74(0);
}
```

## `GameController.ShowIntersititialAd` — RVA `0xcc0820`

- Decompiled symbol: `GameController_ShowIntersititialAd`
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
extern char g_1fab511;

unsigned long long GameController_ShowIntersititialAd(void)
{
    unsigned long long v0;  // x0
    unsigned long long v1;  // x0

    if (!(g_1fab511 & 1))
    {
        sub_f7d92c(&g_1eee700);
        sub_f7d92c(&g_1f082a0);
        g_1fab511 = 1;
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

## `GameController.ButtonResume` — RVA `0xcc08a8`

- Decompiled symbol: `GameController_ButtonResume`
- Metadata signature: `public void ButtonResume() { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[128];
    long long field_80;
} struct_0;

void GameController_ButtonResume(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a0->field_80)
    {
        GameObject__SetActive(a0->field_80, 0, 0);
        Time__set_timeScale();
        return;
    }
    sub_f7db74(0);
}
```

## `GameController.ButtonNext` — RVA `0xcc08d4`

- Decompiled symbol: `GameController_ButtonNext`
- Metadata signature: `public void ButtonNext() { }`
- Native interval: `172` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef14f0;
extern long long g_1f13e08;
extern char g_1fab500;

unsigned long long GameController_ButtonNext(unsigned long long *ptr)
{
    unsigned long v0;  // x0
    unsigned long long v1;  // x0

    if (!(g_1fab500 & 1))
    {
        sub_f7d92c(&g_1ef14f0);
        sub_f7d92c(&g_1f13e08);
        g_1fab500 = 1;
    }
    PlayerPrefs__SetInt(g_1f13e08, 1, 0);
    v0 = ptr[16];
    if (v0)
    {
        GameObject__SetActive(v0, 0, 0);
        v0 = ptr[15];
        if (v0)
        {
            GameObject__SetActive(v0, 1, 0);
            if (!g_1ef14f0->field_e0)
                sub_f7da5c(g_1ef14f0);
            SceneManager__LoadScene(0, 0);
            v1 = GameController__ShowIntersititialAd();
            return GameController__ShowIntersititialAd();
        }
    }
    sub_f7db74(v0);
}
```

## `GameController.Button_Z_Next` — RVA `0xcc0980`

- Decompiled symbol: `GameController_Button_Z_Next`
- Metadata signature: `public void Button_Z_Next() { }`
- Native interval: `172` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef14f0;
extern char g_1fab501;

unsigned long long GameController_Button_Z_Next(unsigned long long *ptr)
{
    unsigned long v0;  // x0
    unsigned long long v1;  // x0

    if (!(g_1fab501 & 1))
    {
        sub_f7d92c(&g_1ef14f0);
        sub_f7d92c("''");
        g_1fab501 = 1;
    }
    PlayerPrefs__SetInt(g_1f0fe88, 1, 0);
    v0 = ptr[16];
    if (v0)
    {
        GameObject__SetActive(v0, 0, 0);
        v0 = ptr[15];
        if (v0)
        {
            GameObject__SetActive(v0, 1, 0);
            if (!g_1ef14f0->field_e0)
                sub_f7da5c(g_1ef14f0);
            SceneManager__LoadScene(0, 0);
            v1 = GameController__ShowIntersititialAd();
            return GameController__ShowIntersititialAd();
        }
    }
    sub_f7db74(v0);
}
```

## `GameController.ButtonRestart` — RVA `0xcc0a2c`

- Decompiled symbol: `GameController_ButtonRestart`
- Metadata signature: `public void ButtonRestart() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef14f0;
extern char g_1fab502;

long long GameController_ButtonRestart(void)
{
    unsigned long long v1;  // x0
    unsigned int v0;  // [bp-0x18]

    if (!(g_1fab502 & 1))
    {
        sub_f7d92c(&g_1ef14f0);
        g_1fab502 = 1;
    }
    if (!g_1ef14f0->field_e0)
        sub_f7da5c(g_1ef14f0);
    v0 = SceneManager__GetActiveScene(0);
    v1 = SceneManager__LoadScene(Scene__get_buildIndex(&v0, 0), 0);
    return SceneManager__LoadScene(Scene__get_buildIndex(&v0, 0), 0);
}
```

## `GameController.ButtonRestart2` — RVA `0xcc0a98`

- Decompiled symbol: `GameController_ButtonRestart2`
- Metadata signature: `public void ButtonRestart2() { }`
- Native interval: `168` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef14f0;
extern long long g_1f0bd20;
extern char g_1fab503;

long long GameController_ButtonRestart2(void)
{
    unsigned int v1;  // w0
    unsigned long long v2;  // x0
    unsigned int v0;  // [bp-0x28]

    if (!(g_1fab503 & 1))
    {
        sub_f7d92c(&g_1ef14f0);
        sub_f7d92c(&g_1f0bd20);
        g_1fab503 = 1;
    }
    v1 = PlayerPrefs__GetInt(g_1f0bd20, 0);
    PlayerPrefs__SetInt(g_1f0bd20, v1 - 1, 0);
    if (!g_1ef14f0->field_e0)
        sub_f7da5c(g_1ef14f0);
    v0 = SceneManager__GetActiveScene(0);
    v2 = SceneManager__LoadScene(Scene__get_buildIndex(&v0, 0), 0);
    return SceneManager__LoadScene(Scene__get_buildIndex(&v0, 0), 0);
}
```

## `GameController.ButtonHome` — RVA `0xcc0b40`

- Decompiled symbol: `GameController_ButtonHome`
- Metadata signature: `public void ButtonHome() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef14f0;
extern char g_1fab504;

unsigned long long GameController_ButtonHome(unsigned long long *ptr, unsigned long a1)
{
    unsigned long v0;  // x0
    unsigned long long v1;  // x0

    if (!(g_1fab504 & 1))
    {
        sub_f7d92c(&g_1ef14f0);
        g_1fab504 = 1;
    }
    v0 = ptr[16];
    if (v0)
    {
        GameObject__SetActive(v0, 0, 0);
        v0 = ptr[15];
        if (v0)
        {
            GameObject__SetActive(v0, 1, 0);
            if (!g_1ef14f0->field_e0)
                sub_f7da5c(g_1ef14f0);
            SceneManager__LoadScene(0, 0);
            v1 = GameController__ShowIntersititialAd();
            return GameController__ShowIntersititialAd();
        }
    }
    sub_f7db74(v0);
}
```

## `GameController.<MissionComplete>d__92.ctor` — RVA `0xcc0bc8`

- Decompiled symbol: `GameController_MissionComplete_d__92_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void GameController_MissionComplete_d__92_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `GameController.SurvivalPanelFunc` — RVA `0xcc0bf0`

- Decompiled symbol: `GameController_SurvivalPanelFunc`
- Metadata signature: `private IEnumerator SurvivalPanelFunc() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern char g_1fab506;

struct_0 * GameController_SurvivalPanelFunc(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab506 & 1))
    {
        sub_f7d92c("]j");
        g_1fab506 = 1;
    }
    v0 = sub_f7db70(g_1ef31e8);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```

## `GameController.<SurvivalPanelFunc>d__93.ctor` — RVA `0xcc0c5c`

- Decompiled symbol: `GameController_SurvivalPanelFunc_d__93_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void GameController_SurvivalPanelFunc_d__93_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `GameController.EnemySpawnFun` — RVA `0xcc0c84`

- Decompiled symbol: `GameController_EnemySpawnFun`
- Metadata signature: `public void EnemySpawnFun() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
void GameController_EnemySpawnFun(unsigned long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    GameController__SpawnFunc();
    MonoBehaviour__StartCoroutine();
    return;
}
```

## `GameController.SpawnFunc` — RVA `0xcc0ca4`

- Decompiled symbol: `GameController_SpawnFunc`
- Metadata signature: `private IEnumerator SpawnFunc() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern char g_1fab507;

struct_0 * GameController_SpawnFunc(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab507 & 1))
    {
        sub_f7d92c("[j");
        g_1fab507 = 1;
    }
    v0 = sub_f7db70(g_1ef31e0);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```

## `GameController.<SpawnFunc>d__96.ctor` — RVA `0xcc0d10`

- Decompiled symbol: `GameController_SpawnFunc_d__96_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void GameController_SpawnFunc_d__96_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `GameController.SniperEnemySpawnFun` — RVA `0xcc0d38`

- Decompiled symbol: `GameController_SniperEnemySpawnFun`
- Metadata signature: `public void SniperEnemySpawnFun() { }`
- Native interval: `344` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[264];
    struct struct_1 *field_108;
} struct_2;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct struct_3 {
    char padding_0[32];
    long long field_20;
} struct_3;

typedef struct struct_4 {
    char padding_0[32];
    long long field_20;
} struct_4;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1f00260;
extern char g_1fab508;

void GameController_SniperEnemySpawnFun(struct_2 *ptr)
{
    unsigned long long v11;  // d14
    unsigned long long v12;  // d13
    unsigned long long v21;  // x19
    struct_1 *v22;  // x21
    unsigned long v23;  // x0
    struct_3 *v24;  // x8
    struct_1 *v25;  // x20
    struct_4 *v26;  // x8
    unsigned long long v13;  // d12
    unsigned long long v14;  // d11
    unsigned long long v15;  // d10
    unsigned long long v16;  // d9
    unsigned long long v17;  // d8
    unsigned long long v18;  // x30
    unsigned long long v19;  // x21
    unsigned long long v20;  // x20
    unsigned long long v0;  // [bp-0x60]
    unsigned long long v1;  // [bp-0x50]
    unsigned long long v2;  // [bp-0x48]
    unsigned long long v3;  // [bp-0x40]
    unsigned long long v4;  // [bp-0x38]
    unsigned long long v5;  // [bp-0x30]
    unsigned long long v6;  // [bp-0x28]
    unsigned long long v7;  // [bp-0x20]
    unsigned long long v8;  // [bp-0x18]
    unsigned long long v9;  // [bp-0x10]
    unsigned long long v10;  // [bp-0x8]

    v0 = v11;
    v1 = v12;
    v2 = v13;
    v3 = v14;
    v4 = v15;
    v5 = v16;
    v6 = v17;
    v7 = v18;
    v8 = v19;
    v9 = v20;
    v10 = v21;
    if (!(g_1fab508 & 1))
    {
        sub_f7d92c(&g_1f00260);
        sub_f7d92c(&g_1ef0c58);
        g_1fab508 = 1;
    }
    v22 = ptr->field_108;
    if (v22)
    {
        v23 = Random__Range(0, v22->field_18, 0);
        if (v22->field_18 <= (unsigned int)v23)
            goto LABEL_10c0e8c;
        v24 = &v22->padding_0[8 * (v23 & 4294967295)];
        if (v24->field_20 && GameObject__get_transform(v24->field_20, 0) && !((Transform__get_position(), v25 = (struct_1 *)ptr->field_108, !v25)))
        {
            v23 = Random__Range(0, v25->field_18, 0);
            if (v25->field_18 <= (unsigned int)v23)
                goto LABEL_10c0e8c;
            v26 = &v25->padding_0[8 * (v23 & 4294967295)];
            if (v26->field_20 && GameObject__get_transform(v26->field_20, 0))
            {
                Transform__get_rotation();
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                sub_112a1ac();
                return;
            }
        }
    }
    v23 = sub_f7db74();
LABEL_10c0e8c:
    sub_f7db7c(v23);
}
```

## `GameController.MissionFail` — RVA `0xcc0e90`

- Decompiled symbol: `GameController_MissionFail`
- Metadata signature: `private IEnumerator MissionFail() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern char g_1fab509;

struct_0 * GameController_MissionFail(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab509 & 1))
    {
        sub_f7d92c("Wj");
        g_1fab509 = 1;
    }
    v0 = sub_f7db70(g_1ef31d0);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```

## `GameController.<MissionFail>d__98.ctor` — RVA `0xcc0efc`

- Decompiled symbol: `GameController_MissionFail_d__98_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void GameController_MissionFail_d__98_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `GameController.Enemydown` — RVA `0xcc0f24`

- Decompiled symbol: `GameController_Enemydown`
- Metadata signature: `public void Enemydown() { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[456];
    unsigned long long field_1c8;
} struct_0;

void GameController_Enemydown(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a0->field_1c8)
    {
        AudioSource__PlayOneShot();
        return;
    }
    sub_f7db74(0);
}
```

## `GameController.BgMusicFunc` — RVA `0xcc0f48`

- Decompiled symbol: `GameController_BgMusicFunc`
- Metadata signature: `public void BgMusicFunc() { }`
- Native interval: `156` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GameController_Recovered` matched 3 offsets against `GameController` metadata (confidence 1.00).

```c
typedef struct GameController_Recovered {
    char padding_0[56];
    unsigned long long BgMusic;
    char padding_40[365];
    char MusicOnOff;
    char padding_1ae[34];
    unsigned long long MusicButton;
} GameController_Recovered;

struct_0 * GameController_BgMusicFunc(struct_0 *ptr)
{
    unsigned int v0;  // w9
    unsigned int v1;  // w8
    unsigned long v2;  // x0
    struct_0 *v3;  // x0
    long long v4;  // x0

    v0 = ptr->field_1ad;
    v1 = v0 ^ 1;
    ptr->field_1ad = v1;
    if (!v0)
    {
        v2 = ptr->field_1d0;
        if (!v2)
            sub_f7db74(v2);
        v2 = Selectable__get_image(v2, 0);
        if (!v2)
            sub_f7db74(v2);
        Image__set_overrideSprite();
        v2 = ptr->field_38;
        if (!v2)
            sub_f7db74(v2);
        v3 = GameObject__SetActive(v2, 1, 0);
        if (ptr->field_1ad)
            return v3;
    }
    else if (v1)
    {
        return ptr;
    }
    v2 = ptr->field_1d0;
    if (v2)
    {
        v2 = Selectable__get_image(v2, 0);
        if (v2)
        {
            Image__set_overrideSprite();
            v2 = ptr->field_38;
            if (v2)
            {
                v4 = GameObject__SetActive();
                return GameObject__SetActive();
            }
        }
    }
    sub_f7db74(v2);
}
```

## `GameController.BgVoiceFunc` — RVA `0xcc0fe4`

- Decompiled symbol: `GameController_BgVoiceFunc`
- Metadata signature: `public void BgVoiceFunc() { }`
- Native interval: `156` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GameController_Recovered` matched 3 offsets against `GameController` metadata (confidence 1.00).

```c
typedef struct GameController_Recovered {
    char padding_0[104];
    unsigned long long BgVoice;
    char padding_70[318];
    char VoiceOnOff;
    char padding_1af[41];
    unsigned long long VoiceButton;
} GameController_Recovered;

struct_0 * GameController_BgVoiceFunc(struct_0 *ptr)
{
    unsigned int v0;  // w9
    unsigned int v1;  // w8
    unsigned long v2;  // x0
    struct_0 *v3;  // x0
    long long v4;  // x0

    v0 = ptr->field_1ae;
    v1 = v0 ^ 1;
    ptr->field_1ae = v1;
    if (!v0)
    {
        v2 = ptr->field_1d8;
        if (!v2)
            sub_f7db74(v2);
        v2 = Selectable__get_image(v2, 0);
        if (!v2)
            sub_f7db74(v2);
        Image__set_overrideSprite();
        v2 = ptr->field_68;
        if (!v2)
            sub_f7db74(v2);
        v3 = GameObject__SetActive(v2, 1, 0);
        if (ptr->field_1ae)
            return v3;
    }
    else if (v1)
    {
        return ptr;
    }
    v2 = ptr->field_1d8;
    if (v2)
    {
        v2 = Selectable__get_image(v2, 0);
        if (v2)
        {
            Image__set_overrideSprite();
            v2 = ptr->field_68;
            if (v2)
            {
                v4 = GameObject__SetActive();
                return GameObject__SetActive();
            }
        }
    }
    sub_f7db74(v2);
}
```

## `GameController.DoubleRewardAds` — RVA `0xcc1080`

- Decompiled symbol: `GameController_DoubleRewardAds`
- Metadata signature: `public void DoubleRewardAds() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
extern long long g_1f145c0;
extern char g_1fab50a;

void GameController_DoubleRewardAds(void)
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
    if (!(g_1fab50a & 1))
    {
        sub_f7d92c(&g_1f145c0);
        g_1fab50a = 1;
    }
    PlayerPrefs__SetInt();
    return;
}
```

## `GameController.DoubleRewardFunc` — RVA `0xcc10c8`

- Decompiled symbol: `GameController_DoubleRewardFunc`
- Metadata signature: `public void DoubleRewardFunc() { }`
- Native interval: `312` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[400];
    struct struct_5 *field_190;
} struct_4;

typedef struct struct_2 {
    char padding_0[1512];
    struct struct_3 *field_5e8;
    unsigned long long field_5f0;
} struct_2;

typedef struct struct_5 {
    struct struct_2 *field_0;
} struct_5;

typedef struct struct_3 {
    unsigned long long field_0;
} struct_3;

typedef struct struct_1 {
    char padding_0[20];
    unsigned int field_14;
    unsigned int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1eefae8;
extern long long g_1f07140;
extern char g_1fab50b;

void GameController_DoubleRewardFunc(struct_4 *ptr)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x22
    unsigned long long v16;  // x2
    unsigned long long v8;  // x21
    unsigned long long v9;  // x20
    unsigned long long v10;  // x19
    struct_2 **v11;  // x20
    long long v12;  // x0
    unsigned long long v13;  // x0
    unsigned long long v14;  // x1
    struct_2 **v15;  // x0
    unsigned long long v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x24]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]
    unsigned long long v5;  // [bp-0x8]

    v0 = v6;
    v2 = v7;
    v3 = v8;
    v4 = v9;
    v5 = v10;
    if (!(g_1fab50b & 1))
    {
        sub_f7d92c(&g_1eefae8);
        sub_f7d92c(&g_1f07140);
        sub_f7d92c(")#");
        g_1fab50b = 1;
    }
    v11 = ptr->field_190;
    v1 = (((g_1eefae8->field_b8->field_14 + g_1eefae8->field_b8->field_18) * 2 | g_1eefae8->field_b8->field_14 + g_1eefae8->field_b8->field_18 >> 31) & 4294967294) + 1000;
    v12 = Int32__ToString(&v1, 0);
    v13 = String__Concat(g_1f07140, v12, 0);
    if (!v11)
        sub_f7db74();
    v14 = v13;
    v15 = v11;
    v16 = *(v11)->field_5f0;
    *(v11)->field_5e8();
}
```

## `GameController.GrenadeOfferbutton` — RVA `0xcc1200`

- Decompiled symbol: `GameController_GrenadeOfferbutton`
- Metadata signature: `public void GrenadeOfferbutton() { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[64];
    unsigned long long field_40;
} struct_0;

extern long long g_1f0a7f0;
extern char g_1fab50c;

void GameController_GrenadeOfferbutton(struct_0 *a0)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned int v8;  // w0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab50c & 1))
    {
        sub_f7d92c(&g_1f0a7f0);
        g_1fab50c = 1;
    }
    v8 = PlayerPrefs__GetInt(g_1f0a7f0, 0);
    PlayerPrefs__SetInt(g_1f0a7f0, v8 + 1, 0);
    if (a0->field_40)
    {
        GameObject__SetActive();
        return;
    }
    sub_f7db74(0);
}
```

## `GameController.HealthkitOfferbutton` — RVA `0xcc1274`

- Decompiled symbol: `GameController_HealthkitOfferbutton`
- Metadata signature: `public void HealthkitOfferbutton() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[72];
    unsigned long long field_48;
} struct_0;

void GameController_HealthkitOfferbutton(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a0->field_48)
    {
        GameObject__SetActive();
        return;
    }
    sub_f7db74(0);
}
```

## `GameController.CoinOfferbutton` — RVA `0xcc1294`

- Decompiled symbol: `GameController_CoinOfferbutton`
- Metadata signature: `public void CoinOfferbutton() { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[80];
    long long field_50;
} struct_0;

extern char g_1fab50d;

void GameController_CoinOfferbutton(struct_0 *a0)
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
    if (!(g_1fab50d & 1))
    {
        sub_f7d92c(")#");
        g_1fab50d = 1;
    }
    if (a0->field_50)
    {
        GameObject__SetActive(a0->field_50, 0, 0);
        PlayerPrefs__GetInt(g_1f0ee98, 0);
        PlayerPrefs__SetInt();
        return;
    }
    sub_f7db74(0);
}
```

## `GameController.EnemyKill` — RVA `0xcc1308`

- Decompiled symbol: `GameController_EnemyKill`
- Metadata signature: `public void EnemyKill() { }`
- Native interval: `60` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[504];
    long long field_1f8;
} struct_0;

void GameController_EnemyKill(struct_0 *a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    if (a0->field_1f8)
    {
        GameObject__SetActive(a0->field_1f8, 1, 0);
        GameController__Enemy_Kill();
        MonoBehaviour__StartCoroutine();
        return;
    }
    sub_f7db74(0);
}
```

## `GameController.Enemy_Kill` — RVA `0xcc1344`

- Decompiled symbol: `GameController_Enemy_Kill`
- Metadata signature: `private IEnumerator Enemy_Kill() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern char g_1fab50e;

struct_0 * GameController_Enemy_Kill(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab50e & 1))
    {
        sub_f7d92c("Qj");
        g_1fab50e = 1;
    }
    v0 = sub_f7db70(g_1ef31b8);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```

## `GameController.Health_Image` — RVA `0xcc13b0`

- Decompiled symbol: `GameController_Health_Image`
- Metadata signature: `public void Health_Image() { }`
- Native interval: `80` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GameController_Recovered` matched 3 offsets against `GameController` metadata (confidence 1.00).

```c
typedef struct GameController_Recovered {
    char padding_0[440];
    long long breathingclip;
    char padding_1c0[8];
    unsigned long long Enemydownsound;
    char padding_1d0[48];
    unsigned long long HealthImage;
} GameController_Recovered;

void GameController_Health_Image(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr->field_200;
    if (v4)
    {
        GameObject__SetActive(v4, 1, 0);
        v4 = ptr->field_1c8;
        if (v4)
        {
            AudioSource__PlayOneShot(v4, ptr->field_1b8, 0);
            GameController__Health_Imag();
            MonoBehaviour__StartCoroutine();
            return;
        }
    }
    sub_f7db74(v4);
}
```

## `GameController.Health_Imag` — RVA `0xcc1400`

- Decompiled symbol: `GameController_Health_Imag`
- Metadata signature: `private IEnumerator Health_Imag() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern char g_1fab50f;

struct_0 * GameController_Health_Imag(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab50f & 1))
    {
        sub_f7d92c("Sj");
        g_1fab50f = 1;
    }
    v0 = sub_f7db70(g_1ef31c0);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```

## `GameController.<Enemy_Kill>d__109.ctor` — RVA `0xcc146c`

- Decompiled symbol: `GameController_Enemy_Kill_d__109_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void GameController_Enemy_Kill_d__109_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `GameController.<Health_Imag>d__110.ctor` — RVA `0xcc1494`

- Decompiled symbol: `GameController_Health_Imag_d__110_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void GameController_Health_Imag_d__110_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `GameController.Advertisement` — RVA `0xcc14bc`

- Decompiled symbol: `GameController_Advertisement`
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
extern char g_1fab510;

void GameController_Advertisement(void)
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
    if (!(g_1fab510 & 1))
    {
        sub_f7d92c(&g_1eee870);
        sub_f7d92c(&g_1f12e28);
        g_1fab510 = 1;
    }
    if (!g_1eee870->field_e0)
        sub_f7da5c(g_1eee870);
}
```

## `GameController.ctor` — RVA `0xcc1524`

- Decompiled symbol: `GameController_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[424];
    unsigned int field_1a8;
} struct_0;

long long GameController_ctor(struct_0 *ptr)
{
    ptr->field_1a8 = 0x41f00000;
}
```

## `GameController.<Enemy_Kill>d__109.Dispose` — RVA `0xcc1534`

- Decompiled symbol: `GameController_Enemy_Kill_d__109_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long GameController_Enemy_Kill_d__109_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `GameController.<Enemy_Kill>d__109.MoveNext` — RVA `0xcc1538`

- Decompiled symbol: `GameController_Enemy_Kill_d__109_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `184` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[504];
    long long field_1f8;
} struct_0;

extern long long g_1ef2440;
extern char g_1fab512;

unsigned int GameController_Enemy_Kill_d__109_MoveNext(struct_1 *ptr)
{
    long long v0;  // x20
    struct_0 *v1;  // x8

    if (!(g_1fab512 & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab512 = 1;
    }
    if (ptr->field_10 == 1)
    {
        v1 = ptr->field_20;
        ptr->field_10 = 4294967295;
        if (!v1 || !v1->field_1f8)
            sub_f7db74();
        GameObject__SetActive(v1->field_1f8, 0, 0);
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        v0 = sub_f7db70(g_1ef2440);
        WaitForSeconds__ctor(v0, 0);
        ptr->field_18 = v0;
        sub_f7d8d0(&ptr->field_18, v0);
        ptr->field_10 = 1;
        return 1;
    }
    return 0;
}
```

## `GameController.<Enemy_Kill>d__109.get_Current` — RVA `0xcc15f0`

- Decompiled symbol: `GameController_Enemy_Kill_d__109_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GameController_Enemy_Kill_d__109_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `GameController.<Enemy_Kill>d__109.Reset` — RVA `0xcc15f8`

- Decompiled symbol: `GameController_Enemy_Kill_d__109_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04698;

void GameController_Enemy_Kill_d__109_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04698));
}
```

## `GameController.<Enemy_Kill>d__109.get_Current` — RVA `0xcc1630`

- Decompiled symbol: `GameController_Enemy_Kill_d__109_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GameController_Enemy_Kill_d__109_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `GameController.<Health_Imag>d__110.Dispose` — RVA `0xcc1638`

- Decompiled symbol: `GameController_Health_Imag_d__110_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long GameController_Health_Imag_d__110_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `GameController.<Health_Imag>d__110.MoveNext` — RVA `0xcc163c`

- Decompiled symbol: `GameController_Health_Imag_d__110_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `184` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[512];
    long long field_200;
} struct_0;

extern long long g_1ef2440;
extern char g_1fab513;

unsigned int GameController_Health_Imag_d__110_MoveNext(struct_1 *ptr)
{
    long long v0;  // x20
    struct_0 *v1;  // x8

    if (!(g_1fab513 & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab513 = 1;
    }
    if (ptr->field_10 == 1)
    {
        v1 = ptr->field_20;
        ptr->field_10 = 4294967295;
        if (!v1 || !v1->field_200)
            sub_f7db74();
        GameObject__SetActive(v1->field_200, 0, 0);
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        v0 = sub_f7db70(g_1ef2440);
        WaitForSeconds__ctor(v0, 0);
        ptr->field_18 = v0;
        sub_f7d8d0(&ptr->field_18, v0);
        ptr->field_10 = 1;
        return 1;
    }
    return 0;
}
```

## `GameController.<Health_Imag>d__110.get_Current` — RVA `0xcc16f4`

- Decompiled symbol: `GameController_Health_Imag_d__110_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GameController_Health_Imag_d__110_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `GameController.<Health_Imag>d__110.Reset` — RVA `0xcc16fc`

- Decompiled symbol: `GameController_Health_Imag_d__110_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f046a0;

void GameController_Health_Imag_d__110_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f046a0));
}
```

## `GameController.<Health_Imag>d__110.get_Current` — RVA `0xcc1734`

- Decompiled symbol: `GameController_Health_Imag_d__110_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GameController_Health_Imag_d__110_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `GameController.<MissionComplete>d__92.Dispose` — RVA `0xcc173c`

- Decompiled symbol: `GameController_MissionComplete_d__92_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long GameController_MissionComplete_d__92_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `GameController.<MissionComplete>d__92.MoveNext` — RVA `0xcc1740`

- Decompiled symbol: `GameController_MissionComplete_d__92_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `1044` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    struct struct_2 *field_20;
} struct_4;

typedef struct struct_2 {
    char padding_0[32];
    unsigned int field_20;
    char padding_24[28];
    long long field_40;
    long long field_48;
    long long field_50;
    char padding_58[56];
    long long field_90;
    char padding_98[224];
    struct struct_3 *field_178;
} struct_2;

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

extern long long g_1eefae8;
extern long long g_1ef2440;
extern unsigned long long g_1f06220;
extern long long g_1f0bd20;
extern long long g_1f0be88;
extern char g_1fab514;

unsigned int GameController_MissionComplete_d__92_MoveNext(struct_4 *p)
{
    struct_2 *ptr;  // x21
    unsigned int v2;  // w0
    unsigned long v11;  // 4131
    struct_0 **v3;  // x20
    unsigned long v4;  // x0
    unsigned long long v5;  // x2
    unsigned long long v6;  // x1
    struct_0 **v7;  // x0
    unsigned int v8;  // w8
    unsigned long v9;  // 4130
    unsigned long v10;  // 4131
    unsigned int v0;  // [bp-0x34]

    if (!(g_1fab514 & 1))
    {
        sub_f7d92c(&g_1eefae8);
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c(&g_1f0be88);
        sub_f7d92c(&g_1f0bd20);
        sub_f7d92c(")#");
        sub_f7d92c(&g_1f06220);
        sub_f7d92c("%%");
        g_1fab514 = 1;
    }
    ptr = p->field_20;
    if (p->field_10 == 1)
    {
        p->field_10 = 4294967295;
        if (ptr && ptr->field_90)
        {
            GameObject__SetActive(ptr->field_90, 1, 0);
            v8 = ptr->field_20;
            if (30 >= v8 && (v9 = (unsigned long)arm64g_calculate_condition(9, (unsigned long long)(1 << ((char)v8 & 31) & 1227133513), 0, 0), !((char)v9)))
            {
                if (ptr->field_40)
                {
                    GameObject__SetActive(ptr->field_40, 1, 0);
                    v8 = ptr->field_20;
                    goto LABEL_10c1ab8;
                }
            }
            else
            {
LABEL_10c1ab8:
                if (28 >= v8 && !((v10 = (unsigned long)arm64g_calculate_condition(9, (unsigned long long)(1 << ((char)v8 & 31) & 306783378), 0, 0), (char)v10)))
                {
                    if (ptr->field_48)
                    {
                        GameObject__SetActive(ptr->field_48, 1, 0);
                        v8 = ptr->field_20;
                        goto LABEL_10c1af0;
                    }
                }
                else
                {
LABEL_10c1af0:
                    if ((29 < v8 || (v11 = (unsigned long)arm64g_calculate_condition(9, (unsigned long long)(1 << ((char)v8 & 31) & 612516132), 0, 0), (char)v11)) && v8 != 120 && v8 != 111)
                        return 0;
                    if (ptr->field_50)
                    {
                        GameObject__SetActive(ptr->field_50, 1, 0);
                        return 0;
                    }
                }
            }
        }
    }
    else if (!p->field_10)
    {
        p->field_10 = 4294967295;
        v2 = PlayerPrefs__GetInt(g_1f0bd20, 0);
        PlayerPrefs__SetInt(g_1f0bd20, v2 + 1, 0);
        if (ptr)
        {
            v3 = ptr->field_178;
            v0 = 500;
            v4 = Int32__ToString(&v0, 0);
            if (v3)
            {
                v5 = *(v3)->field_5f0;
                if (!v4)
                    v6 = g_1f06220;
                else
                    v6 = v4;
                v7 = v3;
                *(v3)->field_5e8();
            }
        }
    }
    else
    {
        return 0;
    }
    sub_f7db74();
}
```

## `GameController.<MissionComplete>d__92.get_Current` — RVA `0xcc1b54`

- Decompiled symbol: `GameController_MissionComplete_d__92_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GameController_MissionComplete_d__92_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `GameController.<MissionComplete>d__92.Reset` — RVA `0xcc1b5c`

- Decompiled symbol: `GameController_MissionComplete_d__92_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f046a8;

void GameController_MissionComplete_d__92_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f046a8));
}
```

## `GameController.<MissionComplete>d__92.get_Current` — RVA `0xcc1b94`

- Decompiled symbol: `GameController_MissionComplete_d__92_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GameController_MissionComplete_d__92_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `GameController.<MissionFail>d__98.Dispose` — RVA `0xcc1b9c`

- Decompiled symbol: `GameController_MissionFail_d__98_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long GameController_MissionFail_d__98_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `GameController.<MissionFail>d__98.MoveNext` — RVA `0xcc1ba0`

- Decompiled symbol: `GameController_MissionFail_d__98_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `184` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[136];
    long long field_88;
} struct_0;

extern long long g_1ef2440;
extern char g_1fab515;

unsigned int GameController_MissionFail_d__98_MoveNext(struct_1 *ptr)
{
    long long v0;  // x20
    struct_0 *v1;  // x8

    if (!(g_1fab515 & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab515 = 1;
    }
    if (ptr->field_10 == 1)
    {
        v1 = ptr->field_20;
        ptr->field_10 = 4294967295;
        if (!v1 || !v1->field_88)
            sub_f7db74();
        GameObject__SetActive(v1->field_88, 1, 0);
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        v0 = sub_f7db70(g_1ef2440);
        WaitForSeconds__ctor(v0, 0);
        ptr->field_18 = v0;
        sub_f7d8d0(&ptr->field_18, v0);
        ptr->field_10 = 1;
        return 1;
    }
    return 0;
}
```

## `GameController.<MissionFail>d__98.get_Current` — RVA `0xcc1c58`

- Decompiled symbol: `GameController_MissionFail_d__98_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GameController_MissionFail_d__98_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `GameController.<MissionFail>d__98.Reset` — RVA `0xcc1c60`

- Decompiled symbol: `GameController_MissionFail_d__98_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f046b0;

void GameController_MissionFail_d__98_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f046b0));
}
```

## `GameController.<MissionFail>d__98.get_Current` — RVA `0xcc1c98`

- Decompiled symbol: `GameController_MissionFail_d__98_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GameController_MissionFail_d__98_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `GameController.<SHowFail>d__84.Dispose` — RVA `0xcc1ca0`

- Decompiled symbol: `GameController_SHowFail_d__84_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long GameController_SHowFail_d__84_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `GameController.<SHowFail>d__84.MoveNext` — RVA `0xcc1ca4`

- Decompiled symbol: `GameController_SHowFail_d__84_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `300` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_3 *field_20;
} struct_2;

typedef struct struct_3 {
    char padding_0[40];
    long long field_28;
    char padding_30[544];
    long long field_250;
} struct_3;

typedef struct struct_1 {
    char padding_0[20];
    unsigned int field_14;
    unsigned int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1eefae8;
extern long long g_1ef2440;
extern char g_1fab516;

unsigned int GameController_SHowFail_d__84_MoveNext(struct_2 *ptr)
{
    long long v0[75];  // x8
    unsigned long long v1;  // x0
    long long v2;  // x20
    struct_2 *p;  // x19

    if (!(g_1fab516 & 1))
    {
        sub_f7d92c(&g_1eefae8);
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c(")#");
        g_1fab516 = 1;
    }
    v0 = ptr->field_20;
    if (ptr->field_10 == 1)
    {
        ptr->field_10 = 4294967295;
        if (!v0)
            sub_f7db74();
        if (v0[5])
        {
            GameObject__SetActive(v0[5], 1, 0);
            GameController__ShowIntersititialAd();
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
        if (v0[74])
        {
            GameObject__SetActive(v0[74], 0, 0);
            v1 = PlayerPrefs__GetInt(g_1f0ee98, 0);
            PlayerPrefs__SetInt(g_1f0ee98, g_1eefae8->field_b8->field_14 + v1 + g_1eefae8->field_b8->field_18, 0);
            v2 = sub_f7db70(g_1ef2440);
            WaitForSeconds__ctor(v2, 0);
            ptr->field_18 = v2;
            p = &ptr->field_18;
            sub_f7d8d0(p, v2);
            *((unsigned int *)&p->padding_0[8]) = 1;
            return 1;
        }
        sub_f7db74();
    }
    return 0;
}
```

## `GameController.<SHowFail>d__84.get_Current` — RVA `0xcc1dd0`

- Decompiled symbol: `GameController_SHowFail_d__84_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GameController_SHowFail_d__84_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `GameController.<SHowFail>d__84.Reset` — RVA `0xcc1dd8`

- Decompiled symbol: `GameController_SHowFail_d__84_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f046b8;

void GameController_SHowFail_d__84_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f046b8));
}
```

## `GameController.<SHowFail>d__84.get_Current` — RVA `0xcc1e10`

- Decompiled symbol: `GameController_SHowFail_d__84_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GameController_SHowFail_d__84_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `GameController.<SpawnFunc>d__96.Dispose` — RVA `0xcc1e18`

- Decompiled symbol: `GameController_SpawnFunc_d__96_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long GameController_SpawnFunc_d__96_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `GameController.<SpawnFunc>d__96.MoveNext` — RVA `0xcc1e1c`

- Decompiled symbol: `GameController_SpawnFunc_d__96_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `540` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_2 *field_20;
} struct_3;

typedef struct struct_2 {
    char padding_0[256];
    struct struct_1 *field_100;
    char padding_108[32];
    unsigned long long field_128;
} struct_2;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct struct_4 {
    char padding_0[32];
    long long field_20;
} struct_4;

typedef struct struct_5 {
    char padding_0[32];
    long long field_20;
} struct_5;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef2440;
extern long long g_1f00260;
extern long long g_1f06580;
extern char g_1fab517;

unsigned int GameController_SpawnFunc_d__96_MoveNext(struct_3 *ptr)
{
    long long v0;  // x20
    struct_2 *p;  // x20
    struct_5 *v10;  // x8
    unsigned long long v2;  // x19
    unsigned long v3;  // x0
    unsigned long v4;  // x0
    struct_1 *v5;  // x21
    unsigned long v6;  // x0
    struct_4 *v7;  // x8
    struct_1 *v8;  // x20
    unsigned long v9;  // x0

    if (!(g_1fab517 & 1))
    {
        sub_f7d92c(&g_1f00260);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c(&g_1f06580);
        g_1fab517 = 1;
    }
    if (ptr->field_10 != 1)
    {
        if (!ptr->field_10)
        {
            ptr->field_10 = 4294967295;
            MonoBehaviour__print(g_1f06580, 0);
            v0 = sub_f7db70(g_1ef2440);
            WaitForSeconds__ctor(v0, 0);
            ptr->field_18 = v0;
            sub_f7d8d0(&ptr->field_18, v0);
            ptr->field_10 = 1;
            return 1;
        }
        return 0;
    }
    p = ptr->field_20;
    ptr->field_10 = 4294967295;
    if (p)
    {
        v2 = p->field_128;
        if (v2)
        {
            v3 = Random__Range(0, *((int *)(v2 + 24)) - 1, 0);
            v4 = v3;
            if (*((int *)(v2 + 24)) <= (unsigned int)v4)
                sub_f7db7c(v4);
            v5 = p->field_100;
            v6 = Random__Range(0, 3, 0);
            if (v5)
            {
                v4 = v6;
                if (v5->field_18 <= (unsigned int)v4)
                    sub_f7db7c(v4);
                v7 = &v5->padding_0[8 * (v6 & 4294967295)];
                if (v7->field_20 && GameObject__get_transform(v7->field_20, 0))
                {
                    Transform__get_position();
                    v8 = p->field_100;
                    v9 = Random__Range(0, 3, 0);
                    if (v8)
                    {
                        v4 = v9;
                        if (v8->field_18 <= (unsigned int)v4)
                            sub_f7db7c(v4);
                        v10 = &v8->padding_0[8 * (v9 & 4294967295)];
                        if (v10->field_20 && GameObject__get_transform(v10->field_20, 0))
                        {
                            Transform__get_rotation();
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            sub_112a1ac(*((long long *)(v2 + (v3 & 4294967295) * 8 + 32)), g_1f00260);
                            return 0;
                        }
                    }
                }
            }
        }
    }
    sub_f7db7c(sub_f7db74());
}
```

## `GameController.<SpawnFunc>d__96.get_Current` — RVA `0xcc2038`

- Decompiled symbol: `GameController_SpawnFunc_d__96_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GameController_SpawnFunc_d__96_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `GameController.<SpawnFunc>d__96.Reset` — RVA `0xcc2040`

- Decompiled symbol: `GameController_SpawnFunc_d__96_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f046c0;

void GameController_SpawnFunc_d__96_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f046c0));
}
```

## `GameController.<SpawnFunc>d__96.get_Current` — RVA `0xcc2078`

- Decompiled symbol: `GameController_SpawnFunc_d__96_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GameController_SpawnFunc_d__96_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `GameController.<SurvivalPanelFunc>d__93.Dispose` — RVA `0xcc2080`

- Decompiled symbol: `GameController_SurvivalPanelFunc_d__93_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long GameController_SurvivalPanelFunc_d__93_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `GameController.<SurvivalPanelFunc>d__93.MoveNext` — RVA `0xcc2084`

- Decompiled symbol: `GameController_SurvivalPanelFunc_d__93_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `628` bytes
- Result: `pseudocode`

```c
typedef struct struct_5 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    struct struct_3 *field_20;
} struct_5;

typedef struct struct_3 {
    char padding_0[88];
    long long field_58;
    char padding_60[320];
    struct struct_4 *field_1a0;
} struct_3;

typedef struct struct_1 {
    char padding_0[1512];
    struct struct_2 *field_5e8;
    unsigned long long field_5f0;
} struct_1;

typedef struct struct_4 {
    struct struct_1 *field_0;
} struct_4;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[184];
    unsigned long long field_b8;
} struct_0;

extern struct_0 *g_1eefae8;
extern long long g_1ef2440;
extern unsigned long long g_1f06220;
extern char g_1fab518;

unsigned int GameController_SurvivalPanelFunc_d__93_MoveNext(struct_5 *ptr)
{
    struct_3 *p;  // x22
    struct_1 **v1;  // x20
    unsigned long v2;  // x0
    unsigned long long v3;  // x2
    unsigned long long v4;  // x1
    struct_1 **v5;  // x0

    if (!(g_1fab518 & 1))
    {
        sub_f7d92c(&g_1eefae8);
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c(")#");
        sub_f7d92c(&g_1f06220);
        g_1fab518 = 1;
    }
    p = ptr->field_20;
    if (ptr->field_10 == 1)
    {
        ptr->field_10 = 4294967295;
        if (p && p->field_58)
        {
            GameObject__SetActive(p->field_58, 1, 0);
            GameController__ShowIntersititialAd();
            return 0;
        }
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        if (p)
        {
            v1 = p->field_1a0;
            v2 = Int32__ToString(g_1eefae8->field_b8 + 20, 0);
            if (v1)
            {
                v3 = *(v1)->field_5f0;
                if (!v2)
                    v4 = g_1f06220;
                else
                    v4 = v2;
                v5 = v1;
                *(v1)->field_5e8();
            }
        }
    }
    else
    {
        return 0;
    }
    sub_f7db74();
}
```

## `GameController.<SurvivalPanelFunc>d__93.get_Current` — RVA `0xcc22f8`

- Decompiled symbol: `GameController_SurvivalPanelFunc_d__93_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GameController_SurvivalPanelFunc_d__93_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `GameController.<SurvivalPanelFunc>d__93.Reset` — RVA `0xcc2300`

- Decompiled symbol: `GameController_SurvivalPanelFunc_d__93_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f046c8;

void GameController_SurvivalPanelFunc_d__93_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f046c8));
}
```

## `GameController.<SurvivalPanelFunc>d__93.get_Current` — RVA `0xcc2338`

- Decompiled symbol: `GameController_SurvivalPanelFunc_d__93_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long GameController_SurvivalPanelFunc_d__93_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
