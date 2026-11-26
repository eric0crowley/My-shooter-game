# Native pseudocode: Texttyper

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `Texttyper.Start` — RVA `0xcc4870`

- Decompiled symbol: `Texttyper_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
void Texttyper_Start(unsigned long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    Texttyper__texttyperfunc();
    MonoBehaviour__StartCoroutine();
    return;
}
```

## `Texttyper.texttyperfunc` — RVA `0xcc4890`

- Decompiled symbol: `Texttyper_texttyperfunc`
- Metadata signature: `private IEnumerator texttyperfunc() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern char g_1fab535;

struct_0 * Texttyper_texttyperfunc(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab535 & 1))
    {
        sub_f7d92c("er");
        g_1fab535 = 1;
    }
    v0 = sub_f7db70(g_1ef3bd0);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `Texttyper.<texttyperfunc>d__4.ctor` — RVA `0xcc48fc`

- Decompiled symbol: `Texttyper_texttyperfunc_d__4_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void Texttyper_texttyperfunc_d__4_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `Texttyper.ctor` — RVA `0xcc4924`

- Decompiled symbol: `Texttyper_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned int field_20;
} struct_0;

long long Texttyper_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_20 = 1036831949;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```

## `Texttyper.<texttyperfunc>d__4.Dispose` — RVA `0xcc4938`

- Decompiled symbol: `Texttyper_texttyperfunc_d__4_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long Texttyper_texttyperfunc_d__4_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `Texttyper.<texttyperfunc>d__4.MoveNext` — RVA `0xcc493c`

- Decompiled symbol: `Texttyper_texttyperfunc_d__4_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `304` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    struct struct_1 *field_20;
    int field_28;
} struct_2;

typedef struct struct_1 {
    char padding_0[40];
    struct struct_0 *field_28;
    long long field_30;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    int field_10;
} struct_0;

typedef struct struct_3 {
    char padding_0[1512];
    struct struct_4 *field_5e8;
    unsigned long long field_5f0;
} struct_3;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

extern long long g_1ef2440;
extern long long g_1efd0b0;
extern char g_1fab536;

unsigned int Texttyper_texttyperfunc_d__4_MoveNext(struct_2 *ptr)
{
    struct_1 *addr;  // x20
    int v1;  // w2
    int v2;  // w8
    unsigned long long flag;  // x3
    long long v4;  // x1
    struct_1 *p;  // x0
    struct_3 **v6;  // x0
    long long v7;  // x1
    unsigned long long v8;  // x2

    if (!(g_1fab536 & 1))
    {
        sub_f7d92c(&g_1efd0b0);
        sub_f7d92c(&g_1ef2440);
        g_1fab536 = 1;
    }
    addr = ptr->field_20;
    if (ptr->field_10 == 1)
    {
        v2 = ptr->field_28;
        ptr->field_10 = 4294967295;
        v1 = v2 + 1;
        ptr->field_28 = v1;
    }
    else if (!ptr->field_10)
    {
        v1 = 0;
        ptr->field_10 = 4294967295;
        ptr->field_28 = 0;
    }
    else
    {
        return 0;
    }
    if (addr && addr->field_28)
    {
        if (v1 > addr->field_28->field_10)
            return 0;
        flag = 0;
        v4 = String__Substring();
        p = addr;
        p->field_30 = v4;
        sub_f7d8d0((struct struct_1 *)&p->field_30, v4);
        v6 = sub_1231bc8(addr, g_1efd0b0);
        if (v6)
        {
            v7 = addr->field_30;
            v8 = *(v6)->field_5f0;
            *(v6)->field_5e8();
        }
    }
    sub_f7db74();
}
```

## `Texttyper.<texttyperfunc>d__4.get_Current` — RVA `0xcc4a6c`

- Decompiled symbol: `Texttyper_texttyperfunc_d__4_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long Texttyper_texttyperfunc_d__4_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `Texttyper.<texttyperfunc>d__4.Reset` — RVA `0xcc4a74`

- Decompiled symbol: `Texttyper_texttyperfunc_d__4_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05000;

void Texttyper_texttyperfunc_d__4_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f05000));
}
```

## `Texttyper.<texttyperfunc>d__4.get_Current` — RVA `0xcc4aac`

- Decompiled symbol: `Texttyper_texttyperfunc_d__4_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long Texttyper_texttyperfunc_d__4_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
