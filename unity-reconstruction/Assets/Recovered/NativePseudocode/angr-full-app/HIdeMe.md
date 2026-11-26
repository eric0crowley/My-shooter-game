# Native pseudocode: HIdeMe

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `HIdeMe.OnEnable` — RVA `0xc6bad8`

- Decompiled symbol: `HIdeMe_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    char field_28;
} struct_0;

void HIdeMe_OnEnable(struct_0 *a0)
{
    if (!a0->field_28)
    {
        HIdeMe__HideMePlease();
        MonoBehaviour__StartCoroutine();
        return;
    }
    return;
}
```

## `HIdeMe.HideMePlease` — RVA `0xc6bb08`

- Decompiled symbol: `HIdeMe_HideMePlease`
- Metadata signature: `private IEnumerator HideMePlease() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef3268;
extern char g_1fab334;

struct_0 * HIdeMe_HideMePlease(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab334 & 1))
    {
        sub_f7d92c(&g_1ef3268);
        g_1fab334 = 1;
    }
    v0 = sub_f7db70(g_1ef3268);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `HIdeMe.Start` — RVA `0xc6bb74`

- Decompiled symbol: `HIdeMe_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    char field_28;
} struct_0;

void HIdeMe_Start(struct_0 *a0)
{
    if (!a0->field_28)
        return;
    HIdeMe__HideMePlease(a0);
    MonoBehaviour__StartCoroutine();
    return;
}
```

## `HIdeMe.<HideMePlease>d__7.ctor` — RVA `0xc6bba4`

- Decompiled symbol: `HIdeMe_HideMePlease_d__7_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void HIdeMe_HideMePlease_d__7_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `HIdeMe.ctor` — RVA `0xc6bbcc`

- Decompiled symbol: `HIdeMe_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[36];
    unsigned int field_24;
} struct_0;

long long HIdeMe_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_24 = 0x3fc00000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```

## `HIdeMe.<HideMePlease>d__7.Dispose` — RVA `0xc6bbdc`

- Decompiled symbol: `HIdeMe_HideMePlease_d__7_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long HIdeMe_HideMePlease_d__7_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `HIdeMe.<HideMePlease>d__7.MoveNext` — RVA `0xc6bbe0`

- Decompiled symbol: `HIdeMe_HideMePlease_d__7_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `288` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_2 *field_20;
} struct_1;

typedef struct struct_2 {
    char padding_0[32];
    char field_20;
    char field_21;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef2440;
extern char g_1fab335;

unsigned int HIdeMe_HideMePlease_d__7_MoveNext(struct_1 *ptr)
{
    char v0[34];  // x0
    long long v1;  // x20
    struct_1 *p;  // x19
    long long v3;  // x0

    if (!(g_1fab335 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef2440);
        g_1fab335 = 1;
    }
    v0 = ptr->field_20;
    if (ptr->field_10 == 1)
    {
        ptr->field_10 = 4294967295;
        if (!v0)
            sub_f7db74();
        if (v0[33])
        {
            if (Component__get_gameObject())
                GameObject__SetActive();
            else
                sub_f7db74();
        }
        else
        {
            if (v0[32])
            {
                v3 = Component__get_gameObject();
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                Object__Destroy(v3, 0);
            }
        }
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

## `HIdeMe.<HideMePlease>d__7.get_Current` — RVA `0xc6bd00`

- Decompiled symbol: `HIdeMe_HideMePlease_d__7_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long HIdeMe_HideMePlease_d__7_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `HIdeMe.<HideMePlease>d__7.Reset` — RVA `0xc6bd08`

- Decompiled symbol: `HIdeMe_HideMePlease_d__7_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04708;

void HIdeMe_HideMePlease_d__7_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04708));
}
```

## `HIdeMe.<HideMePlease>d__7.get_Current` — RVA `0xc6bd40`

- Decompiled symbol: `HIdeMe_HideMePlease_d__7_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long HIdeMe_HideMePlease_d__7_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
