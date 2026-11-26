# Native pseudocode: RespawnCharacter

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `RespawnCharacter.RespawnNow` — RVA `0xc6de64`

- Decompiled symbol: `RespawnCharacter_RespawnNow`
- Metadata signature: `public void RespawnNow() { }`
- Native interval: `160` bytes
- Result: `pseudocode`
- Heuristic layout hint: `RespawnCharacter_Recovered` matched 2 offsets against `RespawnCharacter` metadata (confidence 1.00).

```c
typedef struct RespawnCharacter_Recovered {
    char padding_0[40];
    long long thisCharacter;
    char padding_30[16];
    char isPlayer;
} RespawnCharacter_Recovered;

extern long long g_1efd038;
extern char g_1fab365;

long long RespawnCharacter_RespawnNow(struct_0 *ptr)
{
    long long v0;  // x0

    if (!(g_1fab365 & 1))
    {
        sub_f7d92c(&g_1efd038);
        g_1fab365 = 1;
    }
    if (ptr->field_40)
        RespawnCharacter__SetPosition_Now(ptr); /* do not return */
    v0 = ptr->field_28;
    if (v0)
    {
        v0 = sub_1231bc8(v0, g_1efd038);
        if (v0)
        {
            Behaviour__set_enabled();
            RespawnCharacter__SetPosition_Now(); /* do not return */
        }
    }
    sub_f7db74(v0);
}
```


## `RespawnCharacter.Start` — RVA `0xc72088`

- Decompiled symbol: `RespawnCharacter_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef1320;
extern char g_1fab363;

void RespawnCharacter_Start(unsigned long a0)
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
    if (!(g_1fab363 & 1))
    {
        sub_f7d92c(&g_1ef1320);
        g_1fab363 = 1;
    }
    g_1ef1320->field_b8->field_0 = a0;
    sub_f7d8d0();
    return;
}
```


## `RespawnCharacter.OnEnable` — RVA `0xc720e0`

- Decompiled symbol: `RespawnCharacter_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
void RespawnCharacter_OnEnable(unsigned long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    RespawnCharacter__SetStartPos();
    MonoBehaviour__StartCoroutine();
    return;
}
```


## `RespawnCharacter.SetStartPos` — RVA `0xc72100`

- Decompiled symbol: `RespawnCharacter_SetStartPos`
- Metadata signature: `private IEnumerator SetStartPos() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef38c8;
extern char g_1fab364;

struct_0 * RespawnCharacter_SetStartPos(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab364 & 1))
    {
        sub_f7d92c(&g_1ef38c8);
        g_1fab364 = 1;
    }
    v0 = sub_f7db70(g_1ef38c8);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `RespawnCharacter.<SetStartPos>d__9.ctor` — RVA `0xc7216c`

- Decompiled symbol: `RespawnCharacter_SetStartPos_d__9_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void RespawnCharacter_SetStartPos_d__9_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `RespawnCharacter.SetPosition_Now` — RVA `0xc72194`

- Decompiled symbol: `RespawnCharacter_SetPosition_Now`
- Metadata signature: `public void SetPosition_Now() { }`
- Native interval: `104` bytes
- Result: `pseudocode`
- Heuristic layout hint: `RespawnCharacter_Recovered` matched 2 offsets against `RespawnCharacter` metadata (confidence 1.00).

```c
typedef struct RespawnCharacter_Recovered {
    char padding_0[40];
    unsigned long long thisCharacter;
    struct struct_0 *pos;
} RespawnCharacter_Recovered;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

typedef struct struct_2 {
    char padding_0[32];
    long long field_20;
} struct_2;

void RespawnCharacter_SetPosition_Now(struct_1 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    struct_0 *v5;  // x8
    struct_2 *v6;  // x8
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    if (ptr->field_30 && !((v4 = (long long)(unsigned long long)Random__Range(0, (unsigned long long)ptr->field_30->field_18, 0), v5 = (struct_0 *)ptr->field_30, !v5)))
    {
        if (v5->field_18 <= (int)v4)
            goto LABEL_10721f8;
        v6 = &v5->padding_0[8 * (v4 & 4294967295)];
        if (v6->field_20)
        {
            Transform__get_position(v6->field_20, 0);
            if (ptr->field_28)
            {
                Transform__set_position();
                return;
            }
        }
    }
    v4 = sub_f7db74();
LABEL_10721f8:
    sub_f7db7c(v4);
}
```


## `RespawnCharacter.Hide_Weapon_Obj` — RVA `0xc721fc`

- Decompiled symbol: `RespawnCharacter_Hide_Weapon_Obj`
- Metadata signature: `public void Hide_Weapon_Obj() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[72];
    unsigned long long field_48;
} struct_0;

void RespawnCharacter_Hide_Weapon_Obj(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a0->field_48)
    {
        GameObject__SetActive();
        return;
    }
    sub_f7db74(0);
}
```


## `RespawnCharacter.Show_Weapon_Obj` — RVA `0xc7221c`

- Decompiled symbol: `RespawnCharacter_Show_Weapon_Obj`
- Metadata signature: `public void Show_Weapon_Obj() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[72];
    unsigned long long field_48;
} struct_0;

void RespawnCharacter_Show_Weapon_Obj(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a0->field_48)
    {
        GameObject__SetActive();
        return;
    }
    sub_f7db74(0);
}
```


## `RespawnCharacter.Update` — RVA `0xc7223c`

- Decompiled symbol: `RespawnCharacter_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[32];
    long long field_20;
} struct_4;

typedef struct struct_1 {
    char padding_0[264];
    char field_108;
} struct_1;

typedef struct struct_3 {
    struct struct_1 *field_0;
} struct_3;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_3 *field_b8;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern struct_2 *g_1ef2ad8;
extern long long g_1f0c038;
extern char g_1fab366;

struct_4 * RespawnCharacter_Update(struct_4 *a0)
{
    struct_4 *v0;  // x0
    struct_4 *v1;  // x0
    struct_4 *v2;  // x0
    struct_4 *v3;  // x0
    unsigned long long v4;  // x0

    v0 = a0;
    if (!(g_1fab366 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef2ad8);
        v1 = sub_f7d92c(&g_1f0c038);
        g_1fab366 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (g_1ef2ad8->field_b8->field_0)
    {
        if (g_1ef2ad8->field_b8->field_0->field_108)
        {
            MonoBehaviour__print(g_1f0c038, 0);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v3 = Object__op_Inequality(a0->field_20, 0, 0);
            if (!((char)v3 & 1))
            {
                return v3;
            }
            else if (a0->field_20)
            {
                v4 = Behaviour__set_enabled();
                return Behaviour__set_enabled();
            }
        }
        else
        {
            return v2;
        }
    }
    sub_f7db74();
}
```


## `RespawnCharacter.ctor` — RVA `0xc72310`

- Decompiled symbol: `RespawnCharacter_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long RespawnCharacter_ctor(void)
{
}
```


## `RespawnCharacter.<SetStartPos>d__9.Dispose` — RVA `0xc72318`

- Decompiled symbol: `RespawnCharacter_SetStartPos_d__9_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long RespawnCharacter_SetStartPos_d__9_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `RespawnCharacter.<SetStartPos>d__9.MoveNext` — RVA `0xc7231c`

- Decompiled symbol: `RespawnCharacter_SetStartPos_d__9_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `280` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
    char padding_30[16];
    char field_40;
} struct_0;

extern long long g_1ef2440;
extern long long g_1efd038;
extern char g_1fab367;

unsigned int RespawnCharacter_SetStartPos_d__9_MoveNext(struct_1 *ptr)
{
    long long v0;  // x20
    struct_0 *v1;  // x20

    if (!(g_1fab367 & 1))
    {
        sub_f7d92c(&g_1efd038);
        sub_f7d92c(&g_1ef2440);
        g_1fab367 = 1;
    }
    if (ptr->field_10 != 1)
    {
        if (!ptr->field_10)
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
    v1 = ptr->field_20;
    ptr->field_10 = 4294967295;
    if (v1)
    {
        if (v1->field_40)
        {
            RespawnCharacter__SetPosition_Now(v1); /* do not return */
        }
        else if (v1->field_28 && sub_1231bc8(v1->field_28, g_1efd038))
        {
            Behaviour__set_enabled();
            RespawnCharacter__SetPosition_Now(v1); /* do not return */
        }
    }
    sub_f7db74();
}
```


## `RespawnCharacter.<SetStartPos>d__9.get_Current` — RVA `0xc72434`

- Decompiled symbol: `RespawnCharacter_SetStartPos_d__9_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long RespawnCharacter_SetStartPos_d__9_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `RespawnCharacter.<SetStartPos>d__9.Reset` — RVA `0xc7243c`

- Decompiled symbol: `RespawnCharacter_SetStartPos_d__9_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04c48;

void RespawnCharacter_SetStartPos_d__9_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04c48));
}
```


## `RespawnCharacter.<SetStartPos>d__9.get_Current` — RVA `0xc72474`

- Decompiled symbol: `RespawnCharacter_SetStartPos_d__9_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long RespawnCharacter_SetStartPos_d__9_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
