# Native pseudocode: LevelLoadFade

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `LevelLoadFade.FadeAndLoadLevel` — RVA `0xc8e474`

- Decompiled symbol: `LevelLoadFade_FadeAndLoadLevel`
- Metadata signature: `public void FadeAndLoadLevel(Color color, float fadeLength, bool fadeIn) { }`
- Native interval: `192` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[680];
    struct struct_1 *field_2a8;
    unsigned long long field_2b0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void LevelLoadFade_FadeAndLoadLevel(struct_2 **ptr, unsigned long a1)
{
    unsigned long long v8;  // d12
    unsigned long long v9;  // d11
    unsigned long long v18;  // x1
    unsigned long long v10;  // d10
    unsigned long long v11;  // d9
    unsigned long long v12;  // d8
    unsigned long long v13;  // x30
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
    struct_0 **v16;  // x0
    unsigned long long flag;  // x2
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x38]
    unsigned long long v2;  // [bp-0x30]
    unsigned long long v3;  // [bp-0x28]
    unsigned long long v4;  // [bp-0x20]
    unsigned long long v5;  // [bp-0x18]
    unsigned long long v6;  // [bp-0x10]
    unsigned long long v7;  // [bp-0x8]

    v0 = v8;
    v1 = v9;
    v2 = v10;
    v3 = v11;
    v4 = v12;
    v5 = v13;
    v6 = v14;
    v7 = v15;
    v16 = ptr[4];
    if (v16)
    {
        flag = 0;
        GameObject__set_layer(v16, 14, 0);
        v16 = ptr[5];
        if (v16)
        {
            v18 = *(v16)->field_2b0;
            *(v16)->field_2a8();
        }
    }
    sub_f7db74(v16);
}
```

## `LevelLoadFade.DoFadeIn` — RVA `0xc8e534`

- Decompiled symbol: `LevelLoadFade_DoFadeIn`
- Metadata signature: `private IEnumerator DoFadeIn(float fadeLength) { }`
- Native interval: `124` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LevelLoadFade_Recovered` matched 2 offsets against `LevelLoadFade` metadata (confidence 0.67).

```c
typedef struct LevelLoadFade_Recovered {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long LevelLoadFadeobj;
    unsigned int fadeImage;
} LevelLoadFade_Recovered;

extern char g_1fab443;

struct_0 * LevelLoadFade_DoFadeIn(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0
    unsigned int v2;  // s0

    if (!(g_1fab443 & 1))
    {
        sub_f7d92c("Ol");
        g_1fab443 = 1;
    }
    v0 = sub_f7db70(g_1ef3408);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct LevelLoadFade_Recovered *)&ptr->field_20, a0);
    ptr->field_28 = v2;
    return ptr;
}
```

## `LevelLoadFade.DoFadeOut` — RVA `0xc8e5b0`

- Decompiled symbol: `LevelLoadFade_DoFadeOut`
- Metadata signature: `private IEnumerator DoFadeOut(float fadeLength) { }`
- Native interval: `124` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LevelLoadFade_Recovered` matched 2 offsets against `LevelLoadFade` metadata (confidence 0.67).

```c
typedef struct LevelLoadFade_Recovered {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long LevelLoadFadeobj;
    unsigned int fadeImage;
} LevelLoadFade_Recovered;

extern char g_1fab444;

struct_0 * LevelLoadFade_DoFadeOut(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0
    unsigned int v2;  // s0

    if (!(g_1fab444 & 1))
    {
        sub_f7d92c("Ql");
        g_1fab444 = 1;
    }
    v0 = sub_f7db70(g_1ef3410);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct LevelLoadFade_Recovered *)&ptr->field_20, a0);
    ptr->field_28 = v2;
    return ptr;
}
```

## `LevelLoadFade.<DoFadeIn>d__3.ctor` — RVA `0xc8e62c`

- Decompiled symbol: `LevelLoadFade_DoFadeIn_d__3_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void LevelLoadFade_DoFadeIn_d__3_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `LevelLoadFade.<DoFadeOut>d__4.ctor` — RVA `0xc8e654`

- Decompiled symbol: `LevelLoadFade_DoFadeOut_d__4_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void LevelLoadFade_DoFadeOut_d__4_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `LevelLoadFade.ctor` — RVA `0xc8e67c`

- Decompiled symbol: `LevelLoadFade_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long LevelLoadFade_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```

## `LevelLoadFade.<DoFadeIn>d__3.Dispose` — RVA `0xc8e684`

- Decompiled symbol: `LevelLoadFade_DoFadeIn_d__3_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long LevelLoadFade_DoFadeIn_d__3_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `LevelLoadFade.<DoFadeIn>d__3.MoveNext` — RVA `0xc8e688`

- Decompiled symbol: `LevelLoadFade_DoFadeIn_d__3_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `336` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    unsigned long long field_18;
    struct struct_2 *field_20;
    unsigned int field_28;
    unsigned int field_2c;
} struct_4;

typedef struct struct_2 {
    char padding_0[32];
    long long field_20;
    struct struct_3 *field_28;
} struct_2;

typedef struct struct_0 {
    char padding_0[664];
    struct struct_1 *field_298;
    unsigned long long field_2a0;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

unsigned int LevelLoadFade_DoFadeIn_d__3_MoveNext(struct_4 *ptr)
{
    struct_2 *p;  // x20
    unsigned int v1;  // s0
    unsigned int v2;  // s1
    unsigned long v3;  // 4129
    unsigned long v4;  // 4129
    struct_0 **v5;  // x0
    unsigned long long v6;  // x1
    struct_4 *addr;  // x19

    p = ptr->field_20;
    if (ptr->field_10 == 1)
    {
        v1 = ptr->field_2c;
        ptr->field_10 = 4294967295;
    }
    else if (!ptr->field_10)
    {
        ptr->field_2c = 0;
        ptr->field_10 = 4294967295;
        v1 = 0;
    }
    else
    {
        return 0;
    }
    v2 = ptr->field_28;
    v3 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) & ((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v3))
    {
        Time__get_timeSinceLevelLoad(0);
        v4 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v1, 1061997773)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 1061997773) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 1061997773)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 1061997773) & 1)) & ((unsigned long long)(char)(CmpF(v1, 1061997773)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 1061997773) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v4)
        {
            ptr->field_18 = 0;
            addr = &ptr->field_18;
            sub_f7d8d0(addr, 0);
            *((unsigned int *)&addr->padding_0[8]) = 1;
            return 1;
        }
        if (p)
        {
            v5 = p->field_28;
            if (v5)
            {
                v6 = *(v5)->field_2a0;
                *(v5)->field_298();
            }
        }
    }
    else if (p && p->field_20)
    {
        GameObject__SetActive(p->field_20, 0, 0);
        return 0;
    }
    sub_f7db74();
}
```

## `LevelLoadFade.<DoFadeIn>d__3.get_Current` — RVA `0xc8e7d8`

- Decompiled symbol: `LevelLoadFade_DoFadeIn_d__3_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long LevelLoadFade_DoFadeIn_d__3_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `LevelLoadFade.<DoFadeIn>d__3.Reset` — RVA `0xc8e7e0`

- Decompiled symbol: `LevelLoadFade_DoFadeIn_d__3_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04860;

void LevelLoadFade_DoFadeIn_d__3_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04860));
}
```

## `LevelLoadFade.<DoFadeIn>d__3.get_Current` — RVA `0xc8e818`

- Decompiled symbol: `LevelLoadFade_DoFadeIn_d__3_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long LevelLoadFade_DoFadeIn_d__3_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `LevelLoadFade.<DoFadeOut>d__4.Dispose` — RVA `0xc8e820`

- Decompiled symbol: `LevelLoadFade_DoFadeOut_d__4_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long LevelLoadFade_DoFadeOut_d__4_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `LevelLoadFade.<DoFadeOut>d__4.MoveNext` — RVA `0xc8e824`

- Decompiled symbol: `LevelLoadFade_DoFadeOut_d__4_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `504` bytes
- Result: `pseudocode`

```c
typedef struct struct_6 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_4 *field_20;
    unsigned int field_28;
    char padding_2c[12];
    unsigned int field_38;
    unsigned int field_3c;
} struct_6;

typedef struct struct_4 {
    char padding_0[32];
    long long field_20;
    struct struct_5 *field_28;
} struct_4;

typedef struct struct_1 {
    char padding_0[664];
    struct struct_2 *field_298;
    unsigned long long field_2a0;
    struct struct_3 *field_2a8;
    unsigned long long field_2b0;
} struct_1;

typedef struct struct_5 {
    struct struct_1 *field_0;
} struct_5;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_3 {
    unsigned long long field_0;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef14f0;
extern long long g_1ef2440;
extern char g_1fab445;

unsigned int LevelLoadFade_DoFadeOut_d__4_MoveNext(struct_6 *ptr)
{
    unsigned int flag;  // w8
    struct_4 *p;  // x20
    unsigned int v11;  // 4103
    unsigned long v12;  // 4132
    unsigned long v13;  // 4138
    struct_1 **v14;  // x0
    unsigned long long v15;  // x1
    long long v17;  // x20
    struct_6 *addr;  // x19
    struct_1 **v3;  // x0
    unsigned long long v4;  // x1
    unsigned int v5;  // s8
    unsigned int v6;  // s0
    unsigned long v7;  // 4129
    unsigned int v8;  // s1
    unsigned int v9;  // s0
    unsigned int v10;  // s3
    unsigned int v0;  // [bp-0x28]

    if (!(g_1fab445 & 1))
    {
        sub_f7d92c(&g_1ef14f0);
        sub_f7d92c(&g_1ef2440);
        g_1fab445 = 1;
    }
    flag = ptr->field_10;
    p = ptr->field_20;
    if (flag == 2)
    {
        ptr->field_10 = 4294967295;
        if (p && p->field_20)
        {
            GameObject__SetActive(p->field_20, 0, 0);
            return 0;
        }
    }
    else if (flag == 1)
    {
        v5 = ptr->field_3c;
        ptr->field_10 = 4294967295;
        v6 = ptr->field_28;
        v7 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v5, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v6) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v6) & 1)) & ((unsigned long long)(char)(CmpF(v5, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v6) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v7))
        {
            Time__get_deltaTime(0);
            v8 = ptr->field_28;
            v9 = v5 + v6;
            v10 = 0;
            ptr->field_3c = v9;
            v11 = CmpF(v8, 0.0);
            v12 = (((CmpF(v8, 0.0) >> 5 & 3 | CmpF(v8, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1;
            if (!((char)((v12 - ((CmpF(v8, 0.0) >> 5 & 3 | CmpF(v8, 0.0) & 1) & (v11 >> 5 & 3 | CmpF(v8, 0.0) & 1) >> 1 & 1)) * 0x10000000 >> 30)))
            {
                v13 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v9 / v8, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v9 / v8, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v9 / v8, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v9 / v8, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v9 / v8, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v9 / v8, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if (!((char)v13))
                    v10 = [D] unsupported_Iop_ZeroHI96ofV128();
            }
            ptr->field_38 = v10;
            if (p)
            {
                v14 = p->field_28;
                if (v14)
                {
                    v15 = *(v14)->field_2b0;
                    *(v14)->field_2a8();
                }
            }
        }
        else
        {
            if (!g_1ef14f0->field_e0)
                sub_f7da5c(g_1ef14f0);
            v0 = SceneManager__GetActiveScene(0);
            SceneManager__LoadScene(Scene__get_name(&v0, 0), 0);
            v17 = sub_f7db70(g_1ef2440);
            WaitForSeconds__ctor(v17, 0);
            ptr->field_18 = v17;
            addr = &ptr->field_18;
            sub_f7d8d0(addr, v17);
            *((unsigned int *)&addr->padding_0[8]) = 2;
            return 1;
        }
    }
    else if (!flag)
    {
        ptr->field_10 = 4294967295;
        if (p)
        {
            v3 = p->field_28;
            if (v3)
            {
                v4 = *(v3)->field_2a0;
                *(v3)->field_298();
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

## `LevelLoadFade.<DoFadeOut>d__4.get_Current` — RVA `0xc8ea1c`

- Decompiled symbol: `LevelLoadFade_DoFadeOut_d__4_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long LevelLoadFade_DoFadeOut_d__4_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `LevelLoadFade.<DoFadeOut>d__4.Reset` — RVA `0xc8ea24`

- Decompiled symbol: `LevelLoadFade_DoFadeOut_d__4_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04868;

void LevelLoadFade_DoFadeOut_d__4_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04868));
}
```

## `LevelLoadFade.<DoFadeOut>d__4.get_Current` — RVA `0xc8ea5c`

- Decompiled symbol: `LevelLoadFade_DoFadeOut_d__4_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long LevelLoadFade_DoFadeOut_d__4_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
