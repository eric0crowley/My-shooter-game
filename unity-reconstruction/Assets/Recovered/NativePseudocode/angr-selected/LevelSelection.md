# Native pseudocode: LevelSelection

> Metadata source-path string: `Assets/Script/LevelSelection.cs`. This is a path string from the APK metadata, not recovered source text.

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `LevelSelection.OnEnable` — RVA `0xcc272c`

- Decompiled symbol: `LevelSelection_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `368` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LevelSelection_Recovered` matched 4 offsets against `LevelSelection` metadata (confidence 1.00).

```c
typedef struct LevelSelection_Recovered {
    char padding_0[48];
    struct struct_0 *Z_levelButton;
    unsigned long long Z_CompleteImg;
    unsigned int levelNum;
    unsigned int unlockLevelNum;
} LevelSelection_Recovered;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

typedef struct struct_2 {
    char padding_0[32];
    long long field_20;
} struct_2;

typedef struct struct_3 {
    char padding_0[32];
    long long field_20;
} struct_3;

extern long long g_1f0bb80;
extern char g_1fab51e;

long long LevelSelection_OnEnable(struct_1 *ptr)
{
    unsigned int v1;  // w0
    unsigned long v2;  // x8
    struct_3 *v11;  // x8
    unsigned long v12;  // x1
    unsigned long long v13;  // x0
    struct_0 *v3;  // x9
    int v4;  // w8
    long long v5;  // x0
    struct_0 *v6;  // x8
    unsigned long v7;  // x9
    struct_2 *v8;  // x8
    unsigned long long v9;  // x8
    unsigned long v10;  // x9
    int v0;  // [bp-0x24]

    if (!(g_1fab51e & 1))
    {
        sub_f7d92c(&g_1f0bb80);
        sub_f7d92c("%%");
        g_1fab51e = 1;
    }
    v1 = PlayerPrefs__GetInt(g_1f0f688, 0);
    v2 = g_1f0f688;
    if (!v1)
    {
        PlayerPrefs__SetInt(g_1f0f688, 1, 0);
        v2 = g_1f0f688;
    }
    ptr->field_44 = PlayerPrefs__GetInt(v2, 0);
    v0 = 0;
    v3 = ptr->field_30;
    if (ptr->field_30)
    {
        v4 = 0;
        do
        {
            if (v3->field_18 <= v4)
            {
                v12 = ptr->field_44;
                ptr->field_40 = 1;
                v13 = LevelSelection__unlockLevels(ptr, v12);
                return LevelSelection__unlockLevels(ptr, v12);
            }
            v5 = Int32__ToString(&v0, 0);
            if (PlayerPrefs__GetInt(String__Concat(g_1f0bb80, v5, 0), 0, 0) != 1)
                continue;
            v6 = ptr->field_30;
            if (!v6)
                break;
            v7 = v0;
            if (v6->field_18 <= (unsigned int)v7)
                sub_f7db7c();
            v8 = &v6->padding_0[8 * v7];
            if (!v8->field_20 || !((GameObject__SetActive(v8->field_20, 0, 0), v9 = ptr->field_38, v9)))
                break;
            v10 = v0;
            if (*((int *)(v9 + 24)) <= (unsigned int)v10)
                sub_f7db7c();
            v11 = v9 + v10 * 8;
            if (!v11->field_20)
                break;
            GameObject__SetActive(v11->field_20, 1, 0);
        } while ((v4 = (int)(v0 + 1), v0 = v4, v3 = (struct_0 *)ptr->field_30, v3));
    }
    sub_f7db74();
    v12 = ptr->field_44;
    ptr->field_40 = 1;
    v13 = LevelSelection__unlockLevels(ptr, v12);
    return LevelSelection__unlockLevels(ptr, v12);
}
```


## `LevelSelection.unlockLevels` — RVA `0xcc289c`

- Decompiled symbol: `LevelSelection_unlockLevels`
- Metadata signature: `private void unlockLevels(int num) { }`
- Native interval: `196` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

typedef struct struct_1 {
    char padding_0[32];
    long long field_20;
} struct_1;

unsigned long long [6] LevelSelection_unlockLevels(unsigned long long *ptr, int a1)
{
    int v0;  // w21
    unsigned long long v1[6];  // x0
    unsigned long long v2[6];  // x0
    unsigned long v3;  // x8
    struct_0 *v4;  // x8
    unsigned long v5;  // x8
    int v6;  // w9
    struct_1 *v7;  // x8

    if (a1 < 1)
        return ptr;
    v0 = 0;
    v1 = ptr;
    while (true)
    {
        v2 = v1;
        v3 = ptr[4];
        if (v3)
        {
            if (*((int *)(v3 + 24)) <= v0)
                break;
            v4 = v3 + v0 * 8;
            if (!v4->field_20 || !Component__get_transform(v4->field_20, 0) || !Transform__GetChild() || !Component__get_gameObject())
                goto LABEL_10c2958;
            v2 = GameObject__SetActive();
            if (v0)
            {
                v5 = ptr[5];
                if (v5)
                {
                    v6 = v0 - 1;
                    if (*((int *)(v5 + 24)) <= v6)
                        break;
                    v7 = v5 + v6 * 8;
                    if (v7->field_20)
                    {
                        v2 = GameObject__SetActive(v7->field_20, 1, 0);
                        goto LABEL_10c2940;
                    }
                }
            }
            else
            {
LABEL_10c2940:
                v0 += 1;
                v1 = v2;
                if (a1 == v0)
                    return v2;
            }
        }
        else
        {
LABEL_10c2958:
            v2 = sub_f7db74();
            break;
        }
    }
    sub_f7db7c(v2);
}
```


## `LevelSelection.unlock_Zombie_Levels` — RVA `0xcc2960`

- Decompiled symbol: `LevelSelection_unlock_Zombie_Levels`
- Metadata signature: `private void unlock_Zombie_Levels() { }`
- Native interval: `272` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LevelSelection_Recovered` matched 2 offsets against `LevelSelection` metadata (confidence 1.00).

```c
typedef struct LevelSelection_Recovered {
    char padding_0[40];
    struct struct_0 *CompleteImg;
    struct struct_1 *Z_levelButton;
} LevelSelection_Recovered;

typedef struct struct_5 {
    char padding_0[24];
    unsigned int field_18;
} struct_5;

typedef struct struct_3 {
    char padding_0[32];
    long long field_20;
} struct_3;

typedef struct struct_6 {
    char padding_0[24];
    unsigned int field_18;
} struct_6;

typedef struct struct_4 {
    char padding_0[32];
    long long field_20;
} struct_4;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

extern long long g_1f0bb80;
extern char g_1fab51f;

struct_2 * LevelSelection_unlock_Zombie_Levels(struct_2 *ptr)
{
    struct_2 *v1;  // x0
    struct_2 *v2;  // x0
    unsigned int v11;  // w8
    struct_6 *v12;  // x9
    struct_4 *v13;  // x8
    unsigned long v14;  // x0
    struct_2 *v3;  // x0
    struct_5 *v4;  // x9
    int v5;  // w8
    long long v6;  // x0
    struct_5 *v7;  // x8
    unsigned long v8;  // x9
    struct_3 *v9;  // x8
    unsigned int v10;  // w9
    int v0;  // [bp-0x14]

    v1 = ptr;
    if (!(g_1fab51f & 1))
    {
        v2 = sub_f7d92c(&g_1f0bb80);
        g_1fab51f = 1;
        v1 = v2;
    }
    v0 = 0;
    v4 = ptr->field_30;
    if (ptr->field_30)
    {
        v5 = 0;
        do
        {
            if (v4->field_18 <= v5)
                return v3;
            v6 = Int32__ToString(&v0, 0);
            v3 = PlayerPrefs__GetInt(String__Concat(g_1f0bb80, v6, 0), 0, 0);
            if ((unsigned int)v3 == 1)
            {
                v7 = ptr->field_30;
                if (!v7)
                    break;
                v8 = v0;
                if (v7->field_18 <= (unsigned int)v8)
                    sub_f7db7c();
                v9 = &v7->padding_0[8 * v8];
                if (!v9->field_20)
                    break;
                v3 = GameObject__SetActive(v9->field_20, 0, 0);
            }
            v10 = v0;
            v11 = v10 - 1;
            if (v10 < 1)
                continue;
            v12 = ptr->field_28;
            if (!v12)
                break;
            if (v12->field_18 <= v11)
                sub_f7db7c();
            v13 = &v12->padding_0[8 * v11];
            if (!v13->field_20)
                break;
            v3 = GameObject__SetActive(v13->field_20, 1, 0);
            v10 = v0;
        } while ((v5 = (int)(v10 + 1), v0 = v5, v4 = (struct_5 *)ptr->field_30, v4));
    }
    v14 = sub_f7db74();
    return sub_f7db74();
}
```


## `LevelSelection.LevelCounter` — RVA `0xcc2a70`

- Decompiled symbol: `LevelSelection_LevelCounter`
- Metadata signature: `public void LevelCounter(int levelNum) { }`
- Native interval: `152` bytes
- Result: `pseudocode`

```c
extern long long g_1f0bd20;
extern char g_1fab520;

void LevelSelection_LevelCounter(long long *ptr, unsigned int a1)
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
    if (!(g_1fab520 & 1))
    {
        sub_f7d92c(&g_1f0bd20);
        g_1fab520 = 1;
    }
    PlayerPrefs__SetInt(g_1f0bd20, a1, 0);
    v10 = ptr[9];
    if (v10)
    {
        GameObject__SetActive(v10, 1, 0);
        v10 = ptr[10];
        if (v10)
        {
            GameObject__SetActive(v10, 0, 0);
            LevelSelection__WaitforLoading();
            MonoBehaviour__StartCoroutine();
            return;
        }
    }
    sub_f7db74(v10);
}
```


## `LevelSelection.WaitforLoading` — RVA `0xcc2b08`

- Decompiled symbol: `LevelSelection_WaitforLoading`
- Metadata signature: `private IEnumerator WaitforLoading() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

extern char g_1fab521;

struct_0 * LevelSelection_WaitforLoading(void)
{
    struct_0 *ptr;  // x0

    if (!(g_1fab521 & 1))
    {
        sub_f7d92c("Sl");
        g_1fab521 = 1;
    }
    ptr = sub_f7db70(g_1ef3418);
    Object__ctor(ptr, 0);
    ptr->field_10 = 0;
    return ptr;
}
```


## `LevelSelection.<WaitforLoading>d__12.ctor` — RVA `0xcc2b60`

- Decompiled symbol: `LevelSelection_WaitforLoading_d__12_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void LevelSelection_WaitforLoading_d__12_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `LevelSelection.ctor` — RVA `0xcc2b88`

- Decompiled symbol: `LevelSelection_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[64];
    unsigned int field_40;
} struct_0;

long long LevelSelection_ctor(struct_0 *ptr)
{
    ptr->field_40 = 1;
}
```


## `LevelSelection.<WaitforLoading>d__12.Dispose` — RVA `0xcc2b98`

- Decompiled symbol: `LevelSelection_WaitforLoading_d__12_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long LevelSelection_WaitforLoading_d__12_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `LevelSelection.<WaitforLoading>d__12.MoveNext` — RVA `0xcc2b9c`

- Decompiled symbol: `LevelSelection_WaitforLoading_d__12_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `340` bytes
- Result: `pseudocode`

```c
typedef struct struct_5 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
} struct_5;

typedef struct struct_4 {
    char padding_0[184];
    struct struct_3 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_4;

typedef struct struct_3 {
    char padding_0[12];
    unsigned int field_c;
} struct_3;

typedef struct struct_1 {
    long long field_0;
} struct_1;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1eee700;
extern struct_2 *g_1eee870;
extern struct_4 *g_1ef0750;
extern long long g_1ef2440;
extern long long g_1f082a0;
extern char g_1fab522;

unsigned int LevelSelection_WaitforLoading_d__12_MoveNext(struct_5 *ptr)
{
    long long v0;  // x20
    struct_5 *p;  // x19
    struct_4 *v2;  // x0

    if (!(g_1fab522 & 1))
    {
        sub_f7d92c(&g_1eee700);
        sub_f7d92c(&g_1eee870);
        sub_f7d92c(&g_1ef0750);
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c(&g_1f082a0);
        g_1fab522 = 1;
    }
    if (ptr->field_10 == 1)
    {
        ptr->field_10 = 4294967295;
        v2 = g_1ef0750;
        if (!g_1ef0750->field_e0)
        {
            sub_f7da5c(g_1ef0750);
            v2 = g_1ef0750;
        }
        if (!g_1eee870->field_e0)
            sub_f7da5c(g_1eee870);
        Application__LoadLevel(v2->field_b8->field_c, 0);
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        if (PlayerPrefs__GetInt(g_1f082a0, 0) != 1)
        {
            if (g_1eee700->field_b8->field_0)
                AdsManager__Show_Interstitial(g_1eee700->field_b8->field_0, 0);
            else
                sub_f7db74(0);
        }
        v0 = sub_f7db70(g_1ef2440);
        WaitForSeconds__ctor(v0, 0);
        ptr->field_18 = v0;
        p = &ptr->field_18;
        sub_f7d8d0(p, v0);
        *((unsigned int *)&p->padding_0[8]) = 1;
        return 1;
    }
    return 0;
}
```


## `LevelSelection.<WaitforLoading>d__12.get_Current` — RVA `0xcc2cf0`

- Decompiled symbol: `LevelSelection_WaitforLoading_d__12_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long LevelSelection_WaitforLoading_d__12_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `LevelSelection.<WaitforLoading>d__12.Reset` — RVA `0xcc2cf8`

- Decompiled symbol: `LevelSelection_WaitforLoading_d__12_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04870;

void LevelSelection_WaitforLoading_d__12_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04870));
}
```


## `LevelSelection.<WaitforLoading>d__12.get_Current` — RVA `0xcc2d30`

- Decompiled symbol: `LevelSelection_WaitforLoading_d__12_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long LevelSelection_WaitforLoading_d__12_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
