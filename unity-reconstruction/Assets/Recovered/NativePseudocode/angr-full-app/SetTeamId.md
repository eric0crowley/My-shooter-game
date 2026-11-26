# Native pseudocode: SetTeamId

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SetTeamId.CountKill` — RVA `0xc6dd54`

- Decompiled symbol: `SetTeamId_CountKill`
- Metadata signature: `public void CountKill() { }`
- Native interval: `268` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SetTeamId_Recovered` matched 3 offsets against `SetTeamId` metadata (confidence 1.00).

```c
typedef struct SetTeamId_Recovered {
    char padding_0[32];
    unsigned int myID;
    char padding_24[4];
    struct struct_8 *RedCounter_Txt;
    struct struct_8 *BlueCounter_Txt;
} SetTeamId_Recovered;

typedef struct struct_9 {
    char padding_0[1512];
    struct struct_10 *field_5e8;
    unsigned long long field_5f0;
} struct_9;

typedef struct struct_8 {
    struct struct_5 *field_0;
} struct_8;

typedef struct struct_10 {
    unsigned long long field_0;
} struct_10;

typedef struct struct_5 {
    char padding_0[1512];
    struct struct_6 *field_5e8;
    unsigned long long field_5f0;
} struct_5;

typedef struct struct_6 {
    unsigned long long field_0;
} struct_6;

typedef struct struct_2 {
    char padding_0[128];
    char field_80;
    char padding_81[135];
    char field_108;
} struct_2;

typedef struct struct_4 {
    struct struct_2 *field_0;
} struct_4;

typedef struct struct_3 {
    char padding_0[184];
    struct struct_4 *field_b8;
} struct_3;

extern struct_3 *g_1ef2ad8;
extern char g_1fab36a;

void SetTeamId_CountKill(struct_7 *addr)
{
    unsigned long p;  // x0
    struct_9 **v1;  // x19
    char ptr[265];  // x8
    unsigned int v3;  // w10
    char v4;  // x10
    unsigned long v5;  // x0
    unsigned long v6;  // x1
    struct_9 **v7;  // x0
    unsigned long v8;  // x2

    if (!(g_1fab36a & 1))
    {
        sub_f7d92c("-R");
        sub_f7d92c(&g_1ef2ad8);
        g_1fab36a = 1;
    }
    if (addr->field_20 != 2)
    {
        if (addr->field_20 == 1)
        {
            p = &g_1ef16b0->field_b8->field_c;
            *((unsigned int *)p) = g_1ef16b0->field_b8->field_c + 1;
            v1 = addr->field_30;
LABEL_106dddc:
            v5 = Int32__ToString(p, 0);
            if (v1)
            {
                v6 = v5;
                v7 = v1;
                v8 = *(v1)->field_5f0;
                *(v1)->field_5e8();
            }
        }
        else
        {
            ptr = g_1ef2ad8->field_b8->field_0;
            if (ptr)
            {
                v3 = g_1ef16b0->field_b8->field_8;
                if (g_1ef16b0->field_b8->field_c != *((int *)&ptr[32]))
                {
                    v3 = *((int *)&ptr[32]);
                    if (g_1ef16b0->field_b8->field_8 != v3)
                        return;
                }
                if (g_1ef16b0->field_b8->field_c <= v3)
                    v4 = 0;
                else
                    v4 = 1;
                ptr[128] = v4;
                ptr[264] = 1;
                return;
            }
        }
        sub_f7db74();
    }
    else
    {
        p = &g_1ef16b0->field_b8->field_8;
        *((unsigned int *)p) = g_1ef16b0->field_b8->field_8 + 1;
        v1 = addr->field_28;
        goto LABEL_106dddc;
    }
}
```

## `SetTeamId.DropGun` — RVA `0xc6de60`

- Decompiled symbol: `SetTeamId_DropGun`
- Metadata signature: `public void DropGun() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long SetTeamId_DropGun(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `SetTeamId.Start` — RVA `0xc7247c`

- Decompiled symbol: `SetTeamId_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `160` bytes
- Result: `pseudocode`

```c
extern long long g_1efd088;
extern char g_1fab368;

void SetTeamId_Start(long long a0)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x1
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
    if (!(g_1fab368 & 1))
    {
        sub_f7d92c(&g_1efd088);
        sub_f7d92c("-R");
        g_1fab368 = 1;
    }
    g_1ef16b0->field_b8->field_8 = 0;
    v10 = sub_1231bc8(a0, g_1efd088);
    g_1ef16b0->field_b8->field_0 = v10;
    SetTeamId__SetIds(sub_f7d8d0(g_1ef16b0->field_b8, v10), v10);
    MonoBehaviour__StartCoroutine();
    return;
}
```

## `SetTeamId.SetIds` — RVA `0xc7251c`

- Decompiled symbol: `SetTeamId_SetIds`
- Metadata signature: `private IEnumerator SetIds() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

extern long long g_1ef3998;
extern char g_1fab369;

struct_0 * SetTeamId_SetIds(void)
{
    struct_0 *ptr;  // x0

    if (!(g_1fab369 & 1))
    {
        sub_f7d92c(&g_1ef3998);
        g_1fab369 = 1;
    }
    ptr = sub_f7db70(g_1ef3998);
    Object__ctor(ptr, 0);
    ptr->field_10 = 0;
    return ptr;
}
```

## `SetTeamId.<SetIds>d__8.ctor` — RVA `0xc72574`

- Decompiled symbol: `SetTeamId_SetIds_d__8_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void SetTeamId_SetIds_d__8_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `SetTeamId.ctor` — RVA `0xc7259c`

- Decompiled symbol: `SetTeamId_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long SetTeamId_ctor(void)
{
}
```

## `SetTeamId.<SetIds>d__8.Dispose` — RVA `0xc725a4`

- Decompiled symbol: `SetTeamId_SetIds_d__8_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long SetTeamId_SetIds_d__8_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `SetTeamId.<SetIds>d__8.MoveNext` — RVA `0xc725a8`

- Decompiled symbol: `SetTeamId_SetIds_d__8_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `152` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
} struct_0;

extern long long g_1ef2440;
extern char g_1fab36b;

unsigned int SetTeamId_SetIds_d__8_MoveNext(struct_0 *ptr)
{
    unsigned int v0;  // w0
    long long v1;  // x20
    unsigned int v2;  // w8

    if (!(g_1fab36b & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab36b = 1;
    }
    v0 = 0;
    if (ptr->field_10 == 1)
    {
        v2 = 4294967295;
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        v1 = sub_f7db70(g_1ef2440);
        WaitForSeconds__ctor(v1, 0);
        ptr->field_18 = v1;
        sub_f7d8d0(&ptr->field_18, v1);
        v2 = 1;
        v0 = 1;
    }
    else
    {
        return 0;
    }
    ptr->field_10 = v2;
    return v0;
}
```

## `SetTeamId.<SetIds>d__8.get_Current` — RVA `0xc72640`

- Decompiled symbol: `SetTeamId_SetIds_d__8_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long SetTeamId_SetIds_d__8_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `SetTeamId.<SetIds>d__8.Reset` — RVA `0xc72648`

- Decompiled symbol: `SetTeamId_SetIds_d__8_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04ce0;

void SetTeamId_SetIds_d__8_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04ce0));
}
```

## `SetTeamId.<SetIds>d__8.get_Current` — RVA `0xc72680`

- Decompiled symbol: `SetTeamId_SetIds_d__8_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long SetTeamId_SetIds_d__8_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
