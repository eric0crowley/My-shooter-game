# Native pseudocode: MainEnemyPack

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MainEnemyPack.Start` — RVA `0xc6ea48`

- Decompiled symbol: `MainEnemyPack_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `172` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MainEnemyPack_Recovered` matched 3 offsets against `MainEnemyPack` metadata (confidence 1.00).

```c
typedef struct MainEnemyPack_Recovered {
    char padding_0[32];
    struct struct_1 *myEnemy;
    char padding_28[8];
    unsigned int countEnemy;
    char padding_34[4];
    long long FightSound;
} MainEnemyPack_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    unsigned long long field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab353;

unsigned long long MainEnemyPack_Start(struct_2 *ptr)
{
    long long v0;  // x20
    unsigned long long v1;  // x0
    unsigned long long v2;  // x0

    if (!(g_1fab353 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab353 = 1;
    }
    if (ptr->field_20)
    {
        v0 = ptr->field_38;
        ptr->field_30 = ptr->field_20->field_18;
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v1 = Object__op_Inequality(v0, 0, 0);
        if (!((char)v1 & 1))
        {
            return v1;
        }
        else if (ptr->field_38)
        {
            AudioSource__set_volume(ptr->field_38, 0);
            if (ptr->field_38)
            {
                v2 = AudioSource__Play();
                return AudioSource__Play();
            }
        }
    }
    sub_f7db74();
}
```


## `MainEnemyPack.DestroyMe` — RVA `0xc6eaf4`

- Decompiled symbol: `MainEnemyPack_DestroyMe`
- Metadata signature: `private void DestroyMe() { }`
- Native interval: `148` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[40];
    long long field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab354;

void MainEnemyPack_DestroyMe(struct_1 *a0)
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
    if (!(g_1fab354 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab354 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(a0->field_28, 0, 0) & 1))
    {
        if (a0->field_28)
            GameObject__SetActive(a0->field_28, 1, 0);
        else
            sub_f7db74(0);
    }
    MainEnemyPack__fadeOutFightSound(a0);
    MonoBehaviour__StartCoroutine();
    return;
}
```


## `MainEnemyPack.fadeOutFightSound` — RVA `0xc6eb88`

- Decompiled symbol: `MainEnemyPack_fadeOutFightSound`
- Metadata signature: `private IEnumerator fadeOutFightSound() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef3470;
extern char g_1fab355;

struct_0 * MainEnemyPack_fadeOutFightSound(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab355 & 1))
    {
        sub_f7d92c(&g_1ef3470);
        g_1fab355 = 1;
    }
    v0 = sub_f7db70(g_1ef3470);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `MainEnemyPack.<fadeOutFightSound>d__7.ctor` — RVA `0xc6ebf4`

- Decompiled symbol: `MainEnemyPack_fadeOutFightSound_d__7_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void MainEnemyPack_fadeOutFightSound_d__7_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `MainEnemyPack.ctor` — RVA `0xc6ec1c`

- Decompiled symbol: `MainEnemyPack_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long MainEnemyPack_ctor(void)
{
}
```


## `MainEnemyPack.<fadeOutFightSound>d__7.Dispose` — RVA `0xc6ec24`

- Decompiled symbol: `MainEnemyPack_fadeOutFightSound_d__7_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long MainEnemyPack_fadeOutFightSound_d__7_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `MainEnemyPack.<fadeOutFightSound>d__7.MoveNext` — RVA `0xc6ec28`

- Decompiled symbol: `MainEnemyPack_fadeOutFightSound_d__7_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `424` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_1 *field_20;
    int field_28;
} struct_2;

typedef struct struct_1 {
    char padding_0[56];
    long long field_38;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef2440;
extern char g_1fab356;

unsigned int MainEnemyPack_fadeOutFightSound_d__7_MoveNext(struct_2 *ptr)
{
    struct_1 *p;  // x20
    long long v1;  // x21
    int v2;  // w8
    long long v3;  // x0
    unsigned int v4;  // w8
    long long v5;  // x20
    struct_2 *addr;  // x19

    if (!(g_1fab356 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef2440);
        g_1fab356 = 1;
    }
    if (ptr->field_10 != 1)
    {
        if (!ptr->field_10)
        {
            ptr->field_10 = 4294967295;
            ptr->field_28 = 0;
            goto LABEL_106ed78;
        }
        else
        {
            return 0;
        }
    }
    p = ptr->field_20;
    ptr->field_10 = 4294967295;
    if (p)
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Inequality(p->field_38, 0, 0) & 1))
        {
            v1 = p->field_38;
            if (v1)
            {
                AudioSource__get_volume(v1, 0);
                AudioSource__set_volume(v1, 0);
                goto LABEL_106ecf0;
            }
        }
        else
        {
LABEL_106ecf0:
            v2 = ptr->field_28;
            if (ptr->field_28 < 90)
            {
LABEL_106ed68:
                v4 = v2 + 1;
                ptr->field_28 = v4;
                if (90 < v4)
                    return 0;
LABEL_106ed78:
                v5 = sub_f7db70(g_1ef2440);
                WaitForSeconds__ctor(v5, 0);
                ptr->field_18 = v5;
                addr = &ptr->field_18;
                sub_f7d8d0(addr, v5);
                *((unsigned int *)&addr->padding_0[8]) = 1;
                return 1;
            }
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (!((char)Object__op_Inequality(p->field_38, 0, 0) & 1))
            {
LABEL_106ed34:
                v3 = Component__get_gameObject(p, 0);
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                Object__Destroy(v3, 0);
                v2 = ptr->field_28;
                goto LABEL_106ed68;
            }
            else if (p->field_38)
            {
                AudioSource__Stop(p->field_38, 0);
                goto LABEL_106ed34;
            }
        }
    }
    sub_f7db74();
}
```


## `MainEnemyPack.<fadeOutFightSound>d__7.get_Current` — RVA `0xc6edd0`

- Decompiled symbol: `MainEnemyPack_fadeOutFightSound_d__7_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long MainEnemyPack_fadeOutFightSound_d__7_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `MainEnemyPack.<fadeOutFightSound>d__7.Reset` — RVA `0xc6edd8`

- Decompiled symbol: `MainEnemyPack_fadeOutFightSound_d__7_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f048b8;

void MainEnemyPack_fadeOutFightSound_d__7_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f048b8));
}
```


## `MainEnemyPack.<fadeOutFightSound>d__7.get_Current` — RVA `0xc6ee10`

- Decompiled symbol: `MainEnemyPack_fadeOutFightSound_d__7_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long MainEnemyPack_fadeOutFightSound_d__7_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
