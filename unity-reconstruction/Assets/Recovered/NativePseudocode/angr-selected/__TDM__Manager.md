# Native pseudocode: __TDM__Manager

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `__TDM__Manager.Awake` — RVA `0xc6bf58`

- Decompiled symbol: `TDM__Manager_Awake`
- Metadata signature: `private void Awake() { }`
- Native interval: `204` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TDM__Manager_Recovered` matched 3 offsets against `__TDM__Manager` metadata (confidence 1.00).

```c
typedef struct TDM__Manager_Recovered {
    char padding_0[256];
    struct struct_2 *FreeGunBtn;
    char padding_108[32];
    unsigned int checkAdTime;
    unsigned int checkRewardTime;
} TDM__Manager_Recovered;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

typedef struct struct_0 {
    char padding_0[8];
    char field_8;
} struct_0;

extern struct_1 *g_1ef0750;
extern char g_1fab338;

void TDM__Manager_Awake(struct_3 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned int v8;  // s0
    unsigned int v9;  // s0
    struct_1 *index;  // x0
    struct_2 *v11;  // x19
    long long v12;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab338 & 1))
    {
        sub_f7d92c(&g_1ef0750);
        g_1fab338 = 1;
    }
    Time__get_time(0);
    v9 = v8 + 0x41f00000;
    ptr->field_128 = v9;
    Time__get_time(0);
    ptr->field_12c = v9 + 0x42040000;
    index = g_1ef0750;
    if (!g_1ef0750->field_e0)
    {
        sub_f7da5c(g_1ef0750);
        index = g_1ef0750;
    }
    index->field_b8->field_8 = 1;
    v11 = ptr->field_100;
    if (v11)
    {
        v12 = Random__Range(0, v11->field_18, 0);
        if (v11->field_18 <= (int)v12)
            goto LABEL_106c020;
        if (*((long long *)&v11[1].padding_0[4 + 8 * (v12 & 4294967295)]))
        {
            GameObject__SetActive();
            return;
        }
    }
    v12 = sub_f7db74();
LABEL_106c020:
    sub_f7db7c(v12);
}
```


## `__TDM__Manager.Start` — RVA `0xc6c024`

- Decompiled symbol: `TDM__Manager_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `192` bytes
- Result: `pseudocode`

```c
typedef struct struct_8 {
    char padding_0[240];
    struct struct_9 *field_f0;
} struct_8;

typedef struct struct_6 {
    char padding_0[1064];
    struct struct_7 *field_428;
    unsigned long long field_430;
} struct_6;

typedef struct struct_9 {
    struct struct_6 *field_0;
} struct_9;

typedef struct struct_7 {
    unsigned long long field_0;
} struct_7;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[1064];
    struct struct_1 *field_428;
    unsigned long long field_430;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_2 {
    char padding_0[240];
    struct struct_3 *field_f0;
} struct_2;

typedef struct struct_5 {
    struct struct_2 *field_0;
} struct_5;

typedef struct struct_4 {
    char padding_0[184];
    struct struct_5 *field_b8;
} struct_4;

extern struct_4 *g_1ef2ad8;
extern long long g_1f0d908;
extern char g_1fab339;

void TDM__Manager_Start(struct_8 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    unsigned long long flag;  // x2
    struct_6 **v12;  // x20
    struct_6 **v13;  // x0
    unsigned long long v14;  // x1
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
    if (!(g_1fab339 & 1))
    {
        sub_f7d92c(&g_1ef2ad8);
        sub_f7d92c(&g_1f0d908);
        g_1fab339 = 1;
    }
    g_1ef2ad8->field_b8->field_0 = ptr;
    sub_f7d8d0(g_1ef2ad8->field_b8, ptr);
    flag = 0;
    MonoBehaviour__StartCoroutine(ptr, TDM__Manager__StartCounting(ptr), 0);
    v12 = ptr->field_f0;
    PlayerPrefs__GetFloat(g_1f0d908, 0);
    if (!v12)
        sub_f7db74();
    v13 = v12;
    v14 = *(v12)->field_430;
    *(v12)->field_428();
}
```


## `__TDM__Manager.StartCounting` — RVA `0xc6c0e4`

- Decompiled symbol: `TDM__Manager_StartCounting`
- Metadata signature: `private IEnumerator StartCounting() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef4130;
extern char g_1fab33b;

struct_0 * TDM__Manager_StartCounting(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab33b & 1))
    {
        sub_f7d92c(&g_1ef4130);
        g_1fab33b = 1;
    }
    v0 = sub_f7db70(g_1ef4130);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `__TDM__Manager.Set_Sensitity` — RVA `0xc6c150`

- Decompiled symbol: `TDM__Manager_Set_Sensitity`
- Metadata signature: `public void Set_Sensitity() { }`
- Native interval: `220` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[240];
    struct struct_3 *field_f0;
} struct_2;

typedef struct struct_0 {
    char padding_0[1048];
    struct struct_1 *field_418;
    unsigned long long field_420;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1f0d908;
extern long long g_1f12528;
extern char g_1fab33a;

void TDM__Manager_Set_Sensitity(struct_2 *ptr, unsigned long a1)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    struct_0 **v8;  // x0
    unsigned long long v9;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab33a & 1))
    {
        sub_f7d92c(&g_1f12528);
        sub_f7d92c(&g_1f0d908);
        g_1fab33a = 1;
    }
    v8 = ptr->field_f0;
    if (!ptr->field_f0)
        sub_f7db74(0);
    v9 = ptr->field_f0->field_0->field_420;
    ptr->field_f0->field_0->field_418();
}
```


## `__TDM__Manager.<StartCounting>d__35.ctor` — RVA `0xc6c22c`

- Decompiled symbol: `TDM__Manager_StartCounting_d__35_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void TDM__Manager_StartCounting_d__35_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `__TDM__Manager.Update` — RVA `0xc6c254`

- Decompiled symbol: `TDM__Manager_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `124` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TDM__Manager_Recovered` matched 3 offsets against `__TDM__Manager` metadata (confidence 1.00).

```c
typedef struct TDM__Manager_Recovered {
    char padding_0[96];
    long long Loading_Panel;
    char padding_68[160];
    char isFinished;
    char padding_109[31];
    unsigned int checkAdTime;
} TDM__Manager_Recovered;

long long TDM__Manager_Update(struct_0 *ptr)
{
    unsigned int v0;  // s8
    unsigned long v1;  // x0
    unsigned int v2;  // s0
    unsigned long v3;  // 4125
    unsigned long v4;  // x0

    v0 = ptr->field_128;
    v1 = Time__get_time(0);
    v3 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v0, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v2) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v2) & 1)) & ((unsigned long long)(char)(CmpF(v0, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v2) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v3))
    {
        if (ptr->field_60)
        {
            v1 = GameObject__get_activeSelf(ptr->field_60, 0);
            if (!((char)v1 & 1))
            {
                v1 = Time__get_time(0);
                ptr->field_128 = v2 + 0x40000000;
            }
        }
        else
        {
            sub_f7db74(0);
        }
    }
    if (!ptr->field_108)
        return v1;
    v4 = MonoBehaviour__StartCoroutine(ptr, TDM__Manager__Show_Result_panel(ptr), 0);
    ptr->field_108 = 0;
    return v4;
}
```


## `__TDM__Manager.Show_Result_panel` — RVA `0xc6c2d0`

- Decompiled symbol: `TDM__Manager_Show_Result_panel`
- Metadata signature: `private IEnumerator Show_Result_panel() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef4128;
extern char g_1fab33c;

struct_0 * TDM__Manager_Show_Result_panel(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab33c & 1))
    {
        sub_f7d92c(&g_1ef4128);
        g_1fab33c = 1;
    }
    v0 = sub_f7db70(g_1ef4128);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `__TDM__Manager.<Show_Result_panel>d__44.ctor` — RVA `0xc6c33c`

- Decompiled symbol: `TDM__Manager_Show_Result_panel_d__44_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void TDM__Manager_Show_Result_panel_d__44_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `__TDM__Manager.Rewarded_Video` — RVA `0xc6c364`

- Decompiled symbol: `TDM__Manager_Rewarded_Video`
- Metadata signature: `public void Rewarded_Video() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TDM__Manager_Rewarded_Video(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `__TDM__Manager.GiveReward` — RVA `0xc6c368`

- Decompiled symbol: `TDM__Manager_GiveReward`
- Metadata signature: `public void GiveReward() { }`
- Native interval: `120` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TDM__Manager_Recovered` matched 2 offsets against `__TDM__Manager` metadata (confidence 1.00).

```c
typedef struct TDM__Manager_Recovered {
    char padding_0[304];
    unsigned int TotalReward;
    char padding_134[4];
    unsigned long long CollectedImg;
} TDM__Manager_Recovered;

extern long long g_1f11800;
extern char g_1fab33d;

void TDM__Manager_GiveReward(struct_0 *a0)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v8;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab33d & 1))
    {
        sub_f7d92c(&g_1f11800);
        g_1fab33d = 1;
    }
    v8 = PlayerPrefs__GetInt(g_1f11800, 0);
    PlayerPrefs__SetInt(g_1f11800, a0->field_130 + v8, 0);
    if (a0->field_138)
    {
        GameObject__SetActive();
        return;
    }
    sub_f7db74(0);
}
```


## `__TDM__Manager.myKillCounter_Function` — RVA `0xc6c3e0`

- Decompiled symbol: `TDM__Manager_myKillCounter_Function`
- Metadata signature: `public void myKillCounter_Function() { }`
- Native interval: `64` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TDM__Manager_Recovered` matched 2 offsets against `__TDM__Manager` metadata (confidence 1.00).

```c
typedef struct TDM__Manager_Recovered {
    char padding_0[56];
    struct struct_2 *myKills;
    unsigned int myKillCounter;
} TDM__Manager_Recovered;

typedef struct struct_0 {
    char padding_0[1512];
    unsigned long long field_5e8;
} struct_0;

typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

void TDM__Manager_myKillCounter_Function(struct_1 *idx)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    struct_1 *ptr;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    ptr = &idx->field_40;
    *((unsigned int *)&ptr->padding_0[0]) = idx->field_40 + 1;
    Int32__ToString(ptr, 0);
    if (!*((long long *)&ptr->padding_0[8]))
        sub_f7db74();
    goto *((long long *)(*((long long *)*((long long *)&ptr->padding_0[8])) + 1512));
}
```


## `__TDM__Manager.Respawn` — RVA `0xc6c420`

- Decompiled symbol: `TDM__Manager_Respawn`
- Metadata signature: `public void Respawn() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
void TDM__Manager_Respawn(unsigned long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    TDM__Manager__Respawn_Now();
    MonoBehaviour__StartCoroutine();
    return;
}
```


## `__TDM__Manager.Respawn_Now` — RVA `0xc6c440`

- Decompiled symbol: `TDM__Manager_Respawn_Now`
- Metadata signature: `private IEnumerator Respawn_Now() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef4118;
extern char g_1fab33e;

struct_0 * TDM__Manager_Respawn_Now(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab33e & 1))
    {
        sub_f7d92c(&g_1ef4118);
        g_1fab33e = 1;
    }
    v0 = sub_f7db70(g_1ef4118);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `__TDM__Manager.<Respawn_Now>d__50.ctor` — RVA `0xc6c4ac`

- Decompiled symbol: `TDM__Manager_Respawn_Now_d__50_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void TDM__Manager_Respawn_Now_d__50_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `__TDM__Manager.PauseGame` — RVA `0xc6c4d4`

- Decompiled symbol: `TDM__Manager_PauseGame`
- Metadata signature: `public void PauseGame() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
void TDM__Manager_PauseGame(long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[9];
    if (v4)
    {
        GameObject__SetActive(v4, 0, 0);
        v4 = ptr[10];
        if (v4)
        {
            GameObject__SetActive(v4, 1, 0);
            Time__set_timeScale();
            return;
        }
    }
    sub_f7db74(v4);
}
```


## `__TDM__Manager.Resume_Game` — RVA `0xc6c51c`

- Decompiled symbol: `TDM__Manager_Resume_Game`
- Metadata signature: `public void Resume_Game() { }`
- Native interval: `68` bytes
- Result: `pseudocode`

```c
void TDM__Manager_Resume_Game(long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[9];
    if (v4)
    {
        GameObject__SetActive(v4, 1, 0);
        v4 = ptr[10];
        if (v4)
        {
            GameObject__SetActive(v4, 0, 0);
            Time__set_timeScale();
            return;
        }
    }
    sub_f7db74(v4);
}
```


## `__TDM__Manager._restart` — RVA `0xc6c560`

- Decompiled symbol: `TDM__Manager__restart`
- Metadata signature: `public void _restart() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
void TDM__Manager__restart(unsigned long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    TDM__Manager__Restart_Now();
    MonoBehaviour__StartCoroutine();
    return;
}
```


## `__TDM__Manager.Restart_Now` — RVA `0xc6c580`

- Decompiled symbol: `TDM__Manager_Restart_Now`
- Metadata signature: `private IEnumerator Restart_Now() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef4120;
extern char g_1fab33f;

struct_0 * TDM__Manager_Restart_Now(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab33f & 1))
    {
        sub_f7d92c(&g_1ef4120);
        g_1fab33f = 1;
    }
    v0 = sub_f7db70(g_1ef4120);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `__TDM__Manager.<Restart_Now>d__54.ctor` — RVA `0xc6c5ec`

- Decompiled symbol: `TDM__Manager_Restart_Now_d__54_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void TDM__Manager_Restart_Now_d__54_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `__TDM__Manager._gotoHome` — RVA `0xc6c614`

- Decompiled symbol: `TDM__Manager__gotoHome`
- Metadata signature: `public void _gotoHome() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
void TDM__Manager__gotoHome(unsigned long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    TDM__Manager__GotoHome_Now();
    MonoBehaviour__StartCoroutine();
    return;
}
```


## `__TDM__Manager.GotoHome_Now` — RVA `0xc6c634`

- Decompiled symbol: `TDM__Manager_GotoHome_Now`
- Metadata signature: `private IEnumerator GotoHome_Now() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef4110;
extern char g_1fab340;

struct_0 * TDM__Manager_GotoHome_Now(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab340 & 1))
    {
        sub_f7d92c(&g_1ef4110);
        g_1fab340 = 1;
    }
    v0 = sub_f7db70(g_1ef4110);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `__TDM__Manager.<GotoHome_Now>d__56.ctor` — RVA `0xc6c6a0`

- Decompiled symbol: `TDM__Manager_GotoHome_Now_d__56_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void TDM__Manager_GotoHome_Now_d__56_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `__TDM__Manager.Add_Kill` — RVA `0xc6c6c8`

- Decompiled symbol: `TDM__Manager_Add_Kill`
- Metadata signature: `public void Add_Kill(bool isOur) { }`
- Native interval: `160` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    struct struct_2 *field_0;
} struct_3;

typedef struct struct_2 {
    char padding_0[1512];
    unsigned long long field_5e8;
} struct_2;

typedef struct struct_1 {
    char padding_0[8];
    unsigned int field_8;
    unsigned int field_c;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef2ad8;
extern char g_1fab341;

void TDM__Manager_Add_Kill(struct_3 **p, unsigned int a1)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    unsigned int idx[4];  // x0
    unsigned long ptr;  // x0
    struct_2 **v12;  // x19
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
    if (!(g_1fab341 & 1))
    {
        sub_f7d92c(&g_1ef2ad8);
        g_1fab341 = 1;
    }
    idx = g_1ef2ad8->field_b8;
    if (((char)a1 & 1))
    {
        ptr = &idx[2];
        *((unsigned int *)ptr) = idx[2] + 1;
        v12 = p[5];
    }
    else
    {
        ptr = &idx[3];
        *((unsigned int *)ptr) = idx[3] + 1;
        v12 = p[6];
    }
    Int32__ToString(ptr, 0);
    if (!v12)
        sub_f7db74();
    goto *(v12)->field_5e8;
}
```


## `__TDM__Manager.ctor` — RVA `0xc6c768`

- Decompiled symbol: `TDM__Manager_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    unsigned int field_b8;
} struct_0;

long long TDM__Manager_ctor(struct_0 *ptr)
{
    ptr->field_b8 = 9;
}
```


## `__TDM__Manager.<GotoHome_Now>d__56.Dispose` — RVA `0xc6c778`

- Decompiled symbol: `TDM__Manager_GotoHome_Now_d__56_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TDM__Manager_GotoHome_Now_d__56_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `__TDM__Manager.<GotoHome_Now>d__56.MoveNext` — RVA `0xc6c77c`

- Decompiled symbol: `TDM__Manager_GotoHome_Now_d__56_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `320` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_4 *field_20;
} struct_3;

typedef struct struct_4 {
    char padding_0[80];
    long long field_50;
    long long field_58;
    long long field_60;
} struct_4;

typedef struct struct_1 {
    char padding_0[8];
    unsigned long long field_8;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_2;

extern struct_0 *g_1eee870;
extern long long g_1ef2440;
extern struct_2 *g_1ef2ad8;
extern char g_1fab342;

unsigned int TDM__Manager_GotoHome_Now_d__56_MoveNext(struct_3 *ptr)
{
    long long v0[13];  // x20
    long long v1;  // x21
    struct_3 *p;  // x19

    if (!(g_1fab342 & 1))
    {
        sub_f7d92c(&g_1eee870);
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c(&g_1ef2ad8);
        g_1fab342 = 1;
    }
    if (ptr->field_10 == 1)
    {
        ptr->field_10 = 4294967295;
        if (!g_1eee870->field_e0)
            sub_f7da5c(g_1eee870);
        Application__LoadLevel(2, 0);
    }
    else if (!ptr->field_10)
    {
        v0 = ptr->field_20;
        ptr->field_10 = 4294967295;
        Time__set_timeScale(0);
        if (v0 && v0[11])
        {
            GameObject__SetActive(v0[11], 0, 0);
            if (v0[10])
            {
                GameObject__SetActive(v0[10], 0, 0);
                if (v0[12])
                {
                    GameObject__SetActive(v0[12], 1, 0);
                    g_1ef2ad8->field_b8->field_8 = 0;
                    v1 = sub_f7db70(g_1ef2440);
                    WaitForSeconds__ctor(v1, 0);
                    ptr->field_18 = v1;
                    p = &ptr->field_18;
                    sub_f7d8d0(p, v1);
                    *((unsigned int *)&p->padding_0[8]) = 1;
                    return 1;
                }
            }
        }
        sub_f7db74();
    }
    return 0;
}
```


## `__TDM__Manager.<GotoHome_Now>d__56.get_Current` — RVA `0xc6c8bc`

- Decompiled symbol: `TDM__Manager_GotoHome_Now_d__56_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long TDM__Manager_GotoHome_Now_d__56_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `__TDM__Manager.<GotoHome_Now>d__56.Reset` — RVA `0xc6c8c4`

- Decompiled symbol: `TDM__Manager_GotoHome_Now_d__56_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05490;

void TDM__Manager_GotoHome_Now_d__56_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f05490));
}
```


## `__TDM__Manager.<GotoHome_Now>d__56.get_Current` — RVA `0xc6c8fc`

- Decompiled symbol: `TDM__Manager_GotoHome_Now_d__56_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long TDM__Manager_GotoHome_Now_d__56_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `__TDM__Manager.<Respawn_Now>d__50.Dispose` — RVA `0xc6c904`

- Decompiled symbol: `TDM__Manager_Respawn_Now_d__50_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TDM__Manager_Respawn_Now_d__50_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `__TDM__Manager.<Respawn_Now>d__50.MoveNext` — RVA `0xc6c908`

- Decompiled symbol: `TDM__Manager_Respawn_Now_d__50_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `400` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_1 {
    char padding_0[104];
    long long field_68;
    long long field_70;
    long long field_78;
    char padding_80[8];
    struct struct_0 *field_88;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

typedef struct struct_3 {
    char padding_0[32];
    long long field_20;
} struct_3;

extern long long g_1ef2440;
extern char g_1fab343;

unsigned int TDM__Manager_Respawn_Now_d__50_MoveNext(struct_2 *ptr)
{
    unsigned int flag;  // w8
    struct_1 *p;  // x20
    long long v2;  // x20
    struct_2 *addr;  // x19
    struct_0 *v4;  // x21
    long long v5;  // x0
    struct_3 *v6;  // x8
    long long v7;  // x20
    struct_2 *ptr3;  // x19

    if (!(g_1fab343 & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab343 = 1;
    }
    flag = ptr->field_10;
    p = ptr->field_20;
    if (flag == 2)
    {
        ptr->field_10 = 4294967295;
        if (p && p->field_78)
        {
            Behaviour__set_enabled(p->field_78, 1, 0);
            if (p->field_68)
            {
                Behaviour__set_enabled(p->field_68, 1, 0);
                return 0;
            }
        }
    }
    else if (flag == 1)
    {
        ptr->field_10 = 4294967295;
        if (p)
        {
            v4 = p->field_88;
            if (v4)
            {
                v5 = Random__Range(0, v4->field_18 - 1, 0);
                if (v4->field_18 <= (int)v5)
                    sub_f7db7c(v5);
                v6 = &v4->padding_0[8 * (v5 & 4294967295)];
                if (v6->field_20)
                {
                    Transform__get_position(v6->field_20, 0);
                    if (p->field_70)
                    {
                        Transform__set_position(p->field_70, 0);
                        v7 = sub_f7db70(g_1ef2440);
                        WaitForSeconds__ctor(v7, 0);
                        ptr->field_18 = v7;
                        ptr3 = &ptr->field_18;
                        sub_f7d8d0(ptr3, v7);
                        *((unsigned int *)&ptr3->padding_0[8]) = 2;
                        return 1;
                    }
                }
            }
        }
    }
    else if (!flag)
    {
        ptr->field_10 = 4294967295;
        if (p && p->field_68)
        {
            Behaviour__set_enabled(p->field_68, 0, 0);
            v2 = sub_f7db70(g_1ef2440);
            WaitForSeconds__ctor(v2, 0);
            ptr->field_18 = v2;
            addr = &ptr->field_18;
            sub_f7d8d0(addr, v2);
            *((unsigned int *)&addr->padding_0[8]) = 1;
            return 1;
        }
    }
    else
    {
        return 0;
    }
    v5 = sub_f7db74();
    sub_f7db7c(v5);
}
```


## `__TDM__Manager.<Respawn_Now>d__50.get_Current` — RVA `0xc6ca98`

- Decompiled symbol: `TDM__Manager_Respawn_Now_d__50_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long TDM__Manager_Respawn_Now_d__50_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `__TDM__Manager.<Respawn_Now>d__50.Reset` — RVA `0xc6caa0`

- Decompiled symbol: `TDM__Manager_Respawn_Now_d__50_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05498;

void TDM__Manager_Respawn_Now_d__50_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f05498));
}
```


## `__TDM__Manager.<Respawn_Now>d__50.get_Current` — RVA `0xc6cad8`

- Decompiled symbol: `TDM__Manager_Respawn_Now_d__50_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long TDM__Manager_Respawn_Now_d__50_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `__TDM__Manager.<Restart_Now>d__54.Dispose` — RVA `0xc6cae0`

- Decompiled symbol: `TDM__Manager_Restart_Now_d__54_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TDM__Manager_Restart_Now_d__54_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `__TDM__Manager.<Restart_Now>d__54.MoveNext` — RVA `0xc6cae4`

- Decompiled symbol: `TDM__Manager_Restart_Now_d__54_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `312` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_4 *field_20;
} struct_3;

typedef struct struct_4 {
    char padding_0[80];
    long long field_50;
    long long field_58;
    long long field_60;
} struct_4;

typedef struct struct_1 {
    char padding_0[8];
    unsigned long long field_8;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_2;

extern struct_0 *g_1eee870;
extern long long g_1ef2440;
extern struct_2 *g_1ef2ad8;
extern char g_1fab344;

unsigned int TDM__Manager_Restart_Now_d__54_MoveNext(struct_3 *ptr)
{
    long long v0[13];  // x20
    long long v1;  // x21
    struct_3 *p;  // x19

    if (!(g_1fab344 & 1))
    {
        sub_f7d92c(&g_1eee870);
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c(&g_1ef2ad8);
        g_1fab344 = 1;
    }
    if (ptr->field_10 == 1)
    {
        ptr->field_10 = 4294967295;
        if (!g_1eee870->field_e0)
            sub_f7da5c(g_1eee870);
        Application__LoadLevel(Application__get_loadedLevel(0), 0);
    }
    else if (!ptr->field_10)
    {
        v0 = ptr->field_20;
        ptr->field_10 = 4294967295;
        if (v0 && v0[11])
        {
            GameObject__SetActive(v0[11], 0, 0);
            if (v0[10])
            {
                GameObject__SetActive(v0[10], 0, 0);
                if (v0[12])
                {
                    GameObject__SetActive(v0[12], 1, 0);
                    g_1ef2ad8->field_b8->field_8 = 0;
                    v1 = sub_f7db70(g_1ef2440);
                    WaitForSeconds__ctor(v1, 0);
                    ptr->field_18 = v1;
                    p = &ptr->field_18;
                    sub_f7d8d0(p, v1);
                    *((unsigned int *)&p->padding_0[8]) = 1;
                    return 1;
                }
            }
        }
        sub_f7db74();
    }
    return 0;
}
```


## `__TDM__Manager.<Restart_Now>d__54.get_Current` — RVA `0xc6cc1c`

- Decompiled symbol: `TDM__Manager_Restart_Now_d__54_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long TDM__Manager_Restart_Now_d__54_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `__TDM__Manager.<Restart_Now>d__54.Reset` — RVA `0xc6cc24`

- Decompiled symbol: `TDM__Manager_Restart_Now_d__54_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f054a0;

void TDM__Manager_Restart_Now_d__54_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f054a0));
}
```


## `__TDM__Manager.<Restart_Now>d__54.get_Current` — RVA `0xc6cc5c`

- Decompiled symbol: `TDM__Manager_Restart_Now_d__54_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long TDM__Manager_Restart_Now_d__54_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `__TDM__Manager.<Show_Result_panel>d__44.Dispose` — RVA `0xc6cc64`

- Decompiled symbol: `TDM__Manager_Show_Result_panel_d__44_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TDM__Manager_Show_Result_panel_d__44_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `__TDM__Manager.<Show_Result_panel>d__44.MoveNext` — RVA `0xc6cc68`

- Decompiled symbol: `TDM__Manager_Show_Result_panel_d__44_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `524` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    struct struct_2 *field_20;
} struct_4;

typedef struct struct_2 {
    char padding_0[64];
    unsigned int field_40;
    char padding_44[20];
    long long field_58;
    char padding_60[32];
    char field_80;
    char padding_81[15];
    long long field_90;
    long long field_98;
    struct struct_3 *field_a0;
    char padding_a8[136];
    unsigned int field_130;
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

extern long long g_1ef2440;
extern long long g_1f11800;
extern char g_1fab345;

unsigned int TDM__Manager_Show_Result_panel_d__44_MoveNext(struct_4 *ptr)
{
    struct_2 *p;  // x22
    long long v3;  // x0
    unsigned long long v12;  // x2
    long long v4;  // x1
    unsigned long long v5;  // x0
    unsigned long long v6;  // x8
    long long v7;  // x1
    struct_0 **v8;  // x20
    unsigned long v9;  // x0
    unsigned long v10;  // x1
    struct_0 **v11;  // x0
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]

    if (!(g_1fab345 & 1))
    {
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c(&g_1f11800);
        g_1fab345 = 1;
    }
    p = ptr->field_20;
    if (ptr->field_10 != 1)
    {
        if (ptr->field_10)
            return 0;
        ptr->field_10 = 4294967295;
        if (p && p->field_90 && (GameObject__SetActive(p->field_90, 0, 0), p->field_98))
        {
            GameObject__SetActive(p->field_98, 0, 0);
            if (p->field_80)
            {
                if (p->field_90)
                {
                    GameObject__SetActive(p->field_90, 1, 0);
                    v3 = 1000;
                    v4 = 1500;
                    goto LABEL_106cd58;
                }
            }
            else
            {
                if (p->field_98)
                {
                    GameObject__SetActive(p->field_98, 1, 0);
                    v3 = 300;
                    v4 = 600;
LABEL_106cd58:
                    v5 = Random__Range(v3, v4, 0);
                    v6 = 35 * p->field_40;
                    v7 = v6 + v5;
                    v0 = v6;
                    v1 = v5;
                    p->field_130 = v7;
                    PlayerPrefs__SetInt(g_1f11800, v7, 0);
                    v8 = p->field_a0;
                    v9 = Int32__ToString(&v1, 0);
                    if (v8)
                    {
                        v10 = v9;
                        v11 = v8;
                        v12 = *(v8)->field_5f0;
                        *(v8)->field_5e8();
                    }
                }
            }
        }
    }
    else
    {
        ptr->field_10 = 4294967295;
        if (p && p->field_58)
        {
            GameObject__SetActive(p->field_58, 1, 0);
            return 0;
        }
    }
    sub_f7db74();
}
```


## `__TDM__Manager.<Show_Result_panel>d__44.get_Current` — RVA `0xc6ce74`

- Decompiled symbol: `TDM__Manager_Show_Result_panel_d__44_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long TDM__Manager_Show_Result_panel_d__44_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `__TDM__Manager.<Show_Result_panel>d__44.Reset` — RVA `0xc6ce7c`

- Decompiled symbol: `TDM__Manager_Show_Result_panel_d__44_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f054a8;

void TDM__Manager_Show_Result_panel_d__44_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f054a8));
}
```


## `__TDM__Manager.<Show_Result_panel>d__44.get_Current` — RVA `0xc6ceb4`

- Decompiled symbol: `TDM__Manager_Show_Result_panel_d__44_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long TDM__Manager_Show_Result_panel_d__44_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `__TDM__Manager.<StartCounting>d__35.Dispose` — RVA `0xc6cebc`

- Decompiled symbol: `TDM__Manager_StartCounting_d__35_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TDM__Manager_StartCounting_d__35_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `__TDM__Manager.<StartCounting>d__35.MoveNext` — RVA `0xc6cec0`

- Decompiled symbol: `TDM__Manager_StartCounting_d__35_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `756` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    struct struct_2 *field_20;
} struct_4;

typedef struct struct_2 {
    char padding_0[184];
    int field_b8;
    char padding_bc[4];
    long long field_c0;
    long long field_c8;
    struct struct_3 *field_d0;
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

extern long long g_1ef2440;
extern long long g_1f07670;
extern char g_1fab346;

unsigned int TDM__Manager_StartCounting_d__35_MoveNext(struct_4 *ptr)
{
    unsigned int flag;  // w8
    struct_2 *p;  // x22
    long long v10;  // x0
    unsigned long long v11;  // x0
    unsigned long long v12;  // x1
    struct_0 **v13;  // x0
    unsigned long long v14;  // x2
    struct_0 **v2;  // x21
    long long v3;  // x0
    unsigned long long v4;  // x0
    unsigned long long v5;  // x1
    struct_0 **v6;  // x0
    unsigned long long v7;  // x2
    struct_2 *v8;  // x20
    struct_0 **v9;  // x21

    if (!(g_1fab346 & 1))
    {
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c("58");
        sub_f7d92c(&g_1f07670);
        g_1fab346 = 1;
    }
    flag = ptr->field_10;
    p = ptr->field_20;
    if (flag == 2)
    {
        ptr->field_10 = 4294967295;
        if (p)
        {
            p->field_b8 = p->field_b8 - 1;
LABEL_106d038:
            v8 = p;
            if (v8->field_b8 > 0)
            {
                v9 = p->field_d0;
                v10 = Int32__ToString((struct struct_2 *)&v8->field_b8, 0);
                v11 = String__Concat(g_1f07670, v10, 0);
                if (v9)
                {
                    v12 = v11;
                    v13 = v9;
                    v14 = *(v9)->field_5f0;
                    *(v9)->field_5e8();
                }
            }
            else
            {
                if (p->field_c0)
                {
                    GameObject__SetActive(p->field_c0, 0, 0);
                    if (p->field_c8)
                    {
                        GameObject__SetActive(p->field_c8, 1, 0);
                        if (p->field_c0)
                        {
                            GameObject__SetActive(p->field_c0, 1, 0);
                            if (p->field_d0 && Component__get_gameObject(p->field_d0, 0))
                            {
                                GameObject__SetActive();
                                return 0;
                            }
                        }
                    }
                }
            }
        }
    }
    else if (flag == 1)
    {
        ptr->field_10 = 4294967295;
        if (p)
            goto LABEL_106d038;
    }
    else if (!flag)
    {
        ptr->field_10 = 4294967295;
        if (p && p->field_c8)
        {
            GameObject__SetActive(p->field_c8, 0, 0);
            v2 = p->field_d0;
            v3 = Int32__ToString((struct struct_2 *)&p->field_b8, 0);
            v4 = String__Concat(g_1f07670, v3, 0);
            if (v2)
            {
                v5 = v4;
                v6 = v2;
                v7 = *(v2)->field_5f0;
                *(v2)->field_5e8();
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


## `__TDM__Manager.<StartCounting>d__35.get_Current` — RVA `0xc6d1b4`

- Decompiled symbol: `TDM__Manager_StartCounting_d__35_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long TDM__Manager_StartCounting_d__35_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `__TDM__Manager.<StartCounting>d__35.Reset` — RVA `0xc6d1bc`

- Decompiled symbol: `TDM__Manager_StartCounting_d__35_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f054b0;

void TDM__Manager_StartCounting_d__35_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f054b0));
}
```


## `__TDM__Manager.<StartCounting>d__35.get_Current` — RVA `0xc6d1f4`

- Decompiled symbol: `TDM__Manager_StartCounting_d__35_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long TDM__Manager_StartCounting_d__35_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
