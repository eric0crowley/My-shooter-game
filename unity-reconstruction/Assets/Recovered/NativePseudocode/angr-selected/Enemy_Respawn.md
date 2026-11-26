# Native pseudocode: Enemy_Respawn

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `Enemy_Respawn.Start` — RVA `0xc6bd48`

- Decompiled symbol: `Enemy_Respawn_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long Enemy_Respawn_Start(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `Enemy_Respawn.Respawn` — RVA `0xc6bd4c`

- Decompiled symbol: `Enemy_Respawn_Respawn`
- Metadata signature: `public void Respawn() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
void Enemy_Respawn_Respawn(unsigned long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    Enemy_Respawn__Respawn_Now();
    MonoBehaviour__StartCoroutine();
    return;
}
```


## `Enemy_Respawn.Respawn_Now` — RVA `0xc6bd6c`

- Decompiled symbol: `Enemy_Respawn_Respawn_Now`
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

extern long long g_1ef3048;
extern char g_1fab336;

struct_0 * Enemy_Respawn_Respawn_Now(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab336 & 1))
    {
        sub_f7d92c(&g_1ef3048);
        g_1fab336 = 1;
    }
    v0 = sub_f7db70(g_1ef3048);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `Enemy_Respawn.<Respawn_Now>d__3.ctor` — RVA `0xc6bdd8`

- Decompiled symbol: `Enemy_Respawn_Respawn_Now_d__3_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void Enemy_Respawn_Respawn_Now_d__3_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `Enemy_Respawn.ctor` — RVA `0xc6be00`

- Decompiled symbol: `Enemy_Respawn_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long Enemy_Respawn_ctor(void)
{
}
```


## `Enemy_Respawn.<Respawn_Now>d__3.Dispose` — RVA `0xc6be08`

- Decompiled symbol: `Enemy_Respawn_Respawn_Now_d__3_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long Enemy_Respawn_Respawn_Now_d__3_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `Enemy_Respawn.<Respawn_Now>d__3.MoveNext` — RVA `0xc6be0c`

- Decompiled symbol: `Enemy_Respawn_Respawn_Now_d__3_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `260` bytes
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
    char padding_0[32];
    struct struct_0 *field_20;
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
extern char g_1fab337;

unsigned int Enemy_Respawn_Respawn_Now_d__3_MoveNext(struct_2 *ptr)
{
    long long v0;  // x20
    struct_1 *p;  // x20
    long long v2;  // x0
    struct_0 *v3;  // x20
    long long v4;  // x19
    long long v5;  // x0
    struct_3 *v6;  // x8

    if (!(g_1fab337 & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab337 = 1;
    }
    if (ptr->field_10 == 1)
    {
        p = ptr->field_20;
        ptr->field_10 = 4294967295;
        if (!p)
        {
            sub_f7db74();
            sub_f7db7c(v5);
        }
        v2 = Component__get_transform(p, 0);
        v3 = p->field_20;
        if (!v3)
        {
            sub_f7db74();
            sub_f7db7c(v5);
        }
        v4 = v2;
        v5 = Random__Range(0, v3->field_18, 0);
        if (v3->field_18 <= (int)v5)
            sub_f7db7c(v5);
        v6 = &v3->padding_0[8 * (v5 & 4294967295)];
        if (!v6->field_20)
        {
            sub_f7db74();
            sub_f7db7c(v5);
        }
        Transform__get_position(v6->field_20, 0);
        if (!v4)
        {
            sub_f7db74();
            sub_f7db7c(v5);
        }
        Transform__set_position(v4, 0);
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


## `Enemy_Respawn.<Respawn_Now>d__3.get_Current` — RVA `0xc6bf10`

- Decompiled symbol: `Enemy_Respawn_Respawn_Now_d__3_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long Enemy_Respawn_Respawn_Now_d__3_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `Enemy_Respawn.<Respawn_Now>d__3.Reset` — RVA `0xc6bf18`

- Decompiled symbol: `Enemy_Respawn_Respawn_Now_d__3_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04538;

void Enemy_Respawn_Respawn_Now_d__3_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04538));
}
```


## `Enemy_Respawn.<Respawn_Now>d__3.get_Current` — RVA `0xc6bf50`

- Decompiled symbol: `Enemy_Respawn_Respawn_Now_d__3_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long Enemy_Respawn_Respawn_Now_d__3_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
