# Native pseudocode: PainFade

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `PainFade.Start` — RVA `0xc8ea64`

- Decompiled symbol: `PainFade_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1efcfd0;
extern char g_1fab446;

void PainFade_Start(struct_0 *ptr)
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
    if (!(g_1fab446 & 1))
    {
        sub_f7d92c(&g_1efcfd0);
        g_1fab446 = 1;
    }
    ptr->field_20 = sub_1231bc8(ptr, g_1efcfd0);
    sub_f7d8d0();
    return;
}
```

## `PainFade.FadeIn` — RVA `0xc8eabc`

- Decompiled symbol: `PainFade_FadeIn`
- Metadata signature: `public IEnumerator FadeIn(Color color, float fadeLength) { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    long long field_30;
    unsigned int field_38;
} struct_0;

extern long long g_1ef3660;
extern char g_1fab447;

struct_0 * PainFade_FadeIn(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0
    unsigned int v2;  // s0
    unsigned int v3;  // s1
    unsigned int v4;  // s2
    unsigned int v5;  // s3
    unsigned int v6;  // s4

    if (!(g_1fab447 & 1))
    {
        sub_f7d92c(&g_1ef3660);
        g_1fab447 = 1;
    }
    v0 = sub_f7db70(g_1ef3660);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_30 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_30, a0);
    ptr->field_20 = v2;
    ptr->field_24 = v3;
    ptr->field_28 = v4;
    ptr->field_2c = v5;
    ptr->field_38 = v6;
    return ptr;
}
```

## `PainFade.<FadeIn>d__2.ctor` — RVA `0xc8eb60`

- Decompiled symbol: `PainFade_FadeIn_d__2_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void PainFade_FadeIn_d__2_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `PainFade.ctor` — RVA `0xc8eb88`

- Decompiled symbol: `PainFade_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long PainFade_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```

## `PainFade.<FadeIn>d__2.Dispose` — RVA `0xc8eb90`

- Decompiled symbol: `PainFade_FadeIn_d__2_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long PainFade_FadeIn_d__2_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `PainFade.<FadeIn>d__2.MoveNext` — RVA `0xc8eb94`

- Decompiled symbol: `PainFade_FadeIn_d__2_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `348` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    unsigned long long field_20;
    unsigned int field_28;
    unsigned int field_2c;
    struct struct_2 *field_30;
    unsigned int field_38;
    unsigned long long field_3c;
    unsigned int field_44;
    unsigned int field_48;
    unsigned int field_4c;
} struct_4;

typedef struct struct_2 {
    char padding_0[32];
    struct struct_3 *field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[680];
    struct struct_1 *field_2a8;
    unsigned long long field_2b0;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

unsigned int PainFade_FadeIn_d__2_MoveNext(struct_4 *ptr)
{
    struct_2 *p;  // x20
    unsigned long long v1;  // x8
    unsigned int v10;  // 4106
    unsigned long v11;  // 4146
    unsigned int v12;  // s0
    unsigned long v14;  // 4164
    struct_0 **v15;  // x0
    unsigned long long v16;  // x1
    unsigned int v2;  // w9
    struct_0 **v3;  // x0
    unsigned long long v4;  // x1
    unsigned int v5;  // s8
    unsigned int v6;  // s0
    unsigned long v7;  // 4142
    unsigned int v8;  // s1
    unsigned int v9;  // s0

    p = ptr->field_30;
    if (ptr->field_10 == 1)
    {
        v5 = ptr->field_48;
        ptr->field_10 = 4294967295;
        v6 = ptr->field_38 * 0x40400000;
        v7 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v5, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v6) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v6) & 1)) & ((unsigned long long)(char)(CmpF(v5, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v6) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v7)
            return 0;
        Time__get_deltaTime(0);
        v8 = ptr->field_38;
        v9 = v5 + v6 * 1066611507;
        v10 = CmpF(v8, 0.0);
        v11 = (((CmpF(v8, 0.0) >> 5 & 3 | CmpF(v8, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1;
        ptr->field_48 = v9;
        if (!((char)((v11 - ((CmpF(v8, 0.0) >> 5 & 3 | CmpF(v8, 0.0) & 1) & (v10 >> 5 & 3 | CmpF(v8, 0.0) & 1) >> 1 & 1)) * 0x10000000 >> 30)))
        {
            v12 = 0;
            v14 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF((v9 - v8) / -(v8), 0.0)) >> 5 & 3 | (unsigned long long)(CmpF((v9 - v8) / -(v8), 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((v9 - v8) / -(v8), 0.0)) >> 5 & 3 | (unsigned long long)(CmpF((v9 - v8) / -(v8), 0.0) & 1)) & ((unsigned long long)(char)(CmpF((v9 - v8) / -(v8), 0.0)) >> 5 & 3 | (unsigned long long)(CmpF((v9 - v8) / -(v8), 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v14))
                v12 = [D] unsupported_Iop_ZeroHI96ofV128();
        }
        else
        {
            v12 = 0;
        }
        ptr->field_44 = v12 * ptr->field_2c;
        if (p)
        {
            v15 = p->field_20;
            if (v15)
            {
                v16 = *(v15)->field_2b0;
                *(v15)->field_2a8();
            }
        }
    }
    else if (!ptr->field_10)
    {
        v1 = ptr->field_20;
        v2 = ptr->field_28;
        ptr->field_10 = 4294967295;
        *((unsigned long long *)&(&ptr->field_38)[1]) = v1;
        *((unsigned int *)((char *)&ptr->field_3c + 4)) = v2;
        ptr->field_44 = 0;
        if (p)
        {
            v3 = p->field_20;
            if (v3)
            {
                v4 = *(v3)->field_2b0;
                *(v3)->field_2a8();
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

## `PainFade.<FadeIn>d__2.get_Current` — RVA `0xc8ecf0`

- Decompiled symbol: `PainFade_FadeIn_d__2_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long PainFade_FadeIn_d__2_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `PainFade.<FadeIn>d__2.Reset` — RVA `0xc8ecf8`

- Decompiled symbol: `PainFade_FadeIn_d__2_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04a78;

void PainFade_FadeIn_d__2_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04a78));
}
```

## `PainFade.<FadeIn>d__2.get_Current` — RVA `0xc8ed30`

- Decompiled symbol: `PainFade_FadeIn_d__2_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long PainFade_FadeIn_d__2_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
