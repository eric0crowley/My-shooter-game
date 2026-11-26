# Native pseudocode: DestroyMe

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DestroyMe.OnEnable` — RVA `0xcbfa84`

- Decompiled symbol: `DestroyMe_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
void DestroyMe_OnEnable(unsigned long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    DestroyMe__DestroyObj();
    MonoBehaviour__StartCoroutine();
    return;
}
```

## `DestroyMe.DestroyObj` — RVA `0xcbfaa4`

- Decompiled symbol: `DestroyMe_DestroyObj`
- Metadata signature: `private IEnumerator DestroyObj() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef2f70;
extern char g_1fab4f9;

struct_0 * DestroyMe_DestroyObj(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab4f9 & 1))
    {
        sub_f7d92c(&g_1ef2f70);
        g_1fab4f9 = 1;
    }
    v0 = sub_f7db70(g_1ef2f70);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `DestroyMe.<DestroyObj>d__2.ctor` — RVA `0xcbfb10`

- Decompiled symbol: `DestroyMe_DestroyObj_d__2_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void DestroyMe_DestroyObj_d__2_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `DestroyMe.ctor` — RVA `0xcbfb38`

- Decompiled symbol: `DestroyMe_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned int field_20;
} struct_0;

long long DestroyMe_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_20 = 0x3fc00000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```

## `DestroyMe.<DestroyObj>d__2.Dispose` — RVA `0xcbfb48`

- Decompiled symbol: `DestroyMe_DestroyObj_d__2_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long DestroyMe_DestroyObj_d__2_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `DestroyMe.<DestroyObj>d__2.MoveNext` — RVA `0xcbfb4c`

- Decompiled symbol: `DestroyMe_DestroyObj_d__2_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `244` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    unsigned long long field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef2440;
extern char g_1fab4fa;

unsigned int DestroyMe_DestroyObj_d__2_MoveNext(struct_1 *ptr)
{
    unsigned long long v0;  // x0
    long long v1;  // x20
    struct_1 *p;  // x19
    long long v3;  // x0

    if (!(g_1fab4fa & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef2440);
        g_1fab4fa = 1;
    }
    v0 = ptr->field_20;
    if (ptr->field_10 == 1)
    {
        ptr->field_10 = 4294967295;
        if (!v0)
            sub_f7db74();
        v3 = Component__get_gameObject();
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        Object__Destroy(v3, 0);
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        if (v0)
        {
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

## `DestroyMe.<DestroyObj>d__2.get_Current` — RVA `0xcbfc40`

- Decompiled symbol: `DestroyMe_DestroyObj_d__2_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long DestroyMe_DestroyObj_d__2_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `DestroyMe.<DestroyObj>d__2.Reset` — RVA `0xcbfc48`

- Decompiled symbol: `DestroyMe_DestroyObj_d__2_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f044b8;

void DestroyMe_DestroyObj_d__2_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f044b8));
}
```

## `DestroyMe.<DestroyObj>d__2.get_Current` — RVA `0xcbfc80`

- Decompiled symbol: `DestroyMe_DestroyObj_d__2_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long DestroyMe_DestroyObj_d__2_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
