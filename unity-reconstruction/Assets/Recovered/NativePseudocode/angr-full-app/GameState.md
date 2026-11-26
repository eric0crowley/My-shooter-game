# Native pseudocode: GameState

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GameState.IsRunning` — RVA `0xc34ec0`

- Decompiled symbol: `GameState_IsRunning`
- Metadata signature: `public bool IsRunning() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

long long GameState_IsRunning(struct_0 *a0)
{
    return a0->field_30;
}
```

## `GameState.OnStartState` — RVA `0xc34ec8`

- Decompiled symbol: `GameState_OnStartState`
- Metadata signature: `protected virtual void OnStartState(GameState parentState) { }`
- Native interval: `36` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GameState_Recovered` matched 2 offsets against `GameState` metadata (confidence 1.00).

```c
typedef struct GameState_Recovered {
    char padding_0[32];
    unsigned long long parentState;
    char padding_28[8];
    char isRunning;
} GameState_Recovered;

long long GameState_OnStartState(struct_0 *ptr, unsigned long a1)
{
    struct_0 *p;  // x19
    unsigned long v1;  // x0

    ptr->field_20 = a1;
    p = &ptr->field_20;
    v1 = sub_f7d8d0(p);
    p->padding_0[16] = 1;
    return v1;
}
```

## `GameState.OnExitState` — RVA `0xc34eec`

- Decompiled symbol: `GameState_OnExitState`
- Metadata signature: `protected virtual void OnExitState() { }`
- Native interval: `140` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GameState_Recovered` matched 2 offsets against `GameState` metadata (confidence 1.00).

```c
typedef struct GameState_Recovered {
    char padding_0[40];
    struct struct_3 *subState;
    char isRunning;
} GameState_Recovered;

typedef struct struct_1 {
    char padding_0[392];
    unsigned long long field_188;
} struct_1;

typedef struct struct_3 {
    struct struct_1 *field_0;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab150;

long long GameState_OnExitState(struct_2 *ptr)
{
    long long v0;  // x0

    if (!(g_1fab150 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab150 = 1;
    }
    ptr->field_30 = 0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Inequality(ptr->field_28, 0, 0);
    if (!((char)v0 & 1))
    {
        return v0;
    }
    else if (ptr->field_28)
    {
        goto ptr->field_28->field_0->field_188;
    }
    else
    {
        sub_f7db74(0);
    }
}
```

## `GameState.OnPreSubStateStart` — RVA `0xc34f78`

- Decompiled symbol: `GameState_OnPreSubStateStart`
- Metadata signature: `protected virtual void OnPreSubStateStart(GameState prevState, GameState nextState) { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long GameState_OnPreSubStateStart(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `GameState.OnPostSubStateStart` — RVA `0xc34f7c`

- Decompiled symbol: `GameState_OnPostSubStateStart`
- Metadata signature: `protected virtual void OnPostSubStateStart(GameState prevState, GameState nextState) { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long GameState_OnPostSubStateStart(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `GameState.OnUpdateState` — RVA `0xc34f80`

- Decompiled symbol: `GameState_OnUpdateState`
- Metadata signature: `protected virtual void OnUpdateState() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[40];
    struct struct_3 *field_28;
} struct_2;

typedef struct struct_1 {
    char padding_0[440];
    unsigned long long field_1b8;
} struct_1;

typedef struct struct_3 {
    struct struct_1 *field_0;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab151;

long long GameState_OnUpdateState(struct_2 *a0)
{
    long long v0;  // x0

    if (!(g_1fab151 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab151 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Inequality(a0->field_28, 0, 0);
    if (!((char)v0 & 1))
    {
        return v0;
    }
    else if (a0->field_28)
    {
        goto a0->field_28->field_0->field_1b8;
    }
    else
    {
        sub_f7db74(0);
    }
}
```

## `GameState.OnFixedUpdateState` — RVA `0xc35008`

- Decompiled symbol: `GameState_OnFixedUpdateState`
- Metadata signature: `protected virtual void OnFixedUpdateState() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[40];
    struct struct_3 *field_28;
} struct_2;

typedef struct struct_1 {
    char padding_0[456];
    unsigned long long field_1c8;
} struct_1;

typedef struct struct_3 {
    struct struct_1 *field_0;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab152;

long long GameState_OnFixedUpdateState(struct_2 *a0)
{
    long long v0;  // x0

    if (!(g_1fab152 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab152 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Inequality(a0->field_28, 0, 0);
    if (!((char)v0 & 1))
    {
        return v0;
    }
    else if (a0->field_28)
    {
        goto a0->field_28->field_0->field_1c8;
    }
    else
    {
        sub_f7db74(0);
    }
}
```

## `GameState.StartSubState` — RVA `0xc35090`

- Decompiled symbol: `GameState_StartSubState`
- Metadata signature: `public void StartSubState(GameState state) { }`
- Native interval: `580` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
    char padding_8[32];
    unsigned long long field_28;
} struct_2;

typedef struct struct_0 {
    char padding_0[408];
    struct struct_1 *field_198;
    unsigned long long field_1a0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1eef838;
extern long long g_1ef0c58;
extern long long g_1efede0;
extern long long g_1f070d8;
extern long long g_1f070e0;
extern long long g_1f0a6a0;
extern char g_1fab153;

void GameState_StartSubState(struct_2 *ptr, long long a1)
{
    unsigned long long v7;  // x30
    unsigned long long v8;  // x24
    long long v17;  // x2
    long long v18;  // x21
    long long v20;  // x0
    long long v22;  // x0
    long long v24;  // x0
    long long v25;  // x0
    long long v26;  // x1
    unsigned long long v9;  // x23
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    struct_2 *v14;  // x0
    unsigned long v15;  // x1
    unsigned long v16;  // x3
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]
    unsigned long long v5;  // [bp-0x10]
    unsigned long long v6;  // [bp-0x8]

    v0 = v7;
    v1 = v8;
    v2 = v9;
    v3 = v10;
    v4 = v11;
    v5 = v12;
    v6 = v13;
    if (!(g_1fab153 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab153 = 1;
    }
    if (((char)GameState__FindStateInHierarchy(ptr, a1) & 1))
    {
        v18 = sub_f7d9d4(sub_f7d940("I)"), 5);
        sub_e29564(v18, 5);
        sub_e2999c(v18, 0, sub_f7d940(&g_1f0a6a0));
        v20 = Object__get_name(ptr, 0);
        sub_e29564(v18);
        sub_e2999c(v18, 1, v20);
        sub_e29564(v18);
        sub_e2999c(v18, 2, sub_f7d940(&g_1f070e0));
        sub_e29564(a1);
        v22 = Object__get_name(a1, 0);
        sub_e29564(v18);
        sub_e2999c(v18, 3, v22);
        sub_e29564(v18);
        sub_e2999c(v18, 4, sub_f7d940(&g_1f070d8));
        v24 = String__Concat(v18, 0);
        v25 = sub_f7db70(sub_f7d940(&g_1eef838));
        Exception__ctor(v25, v24, 0);
        v26 = sub_f7d940(&g_1efede0);
        sub_f7db74(sub_f7da4c(v25, v26), v26);
    }
    v14 = ptr;
    v15 = ptr->field_28;
    v16 = ptr->field_0->field_1a0;
    v17 = a1;
    ptr->field_0->field_198();
}
```

## `GameState.FindStateInHierarchy` — RVA `0xc352d4`

- Decompiled symbol: `GameState_FindStateInHierarchy`
- Metadata signature: `protected bool FindStateInHierarchy(GameState state) { }`
- Native interval: `212` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    struct struct_0 *field_20;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_1 *g_1ef0c58;
extern char g_1fab154;

unsigned int GameState_FindStateInHierarchy(struct_0 *a0, long long a1)
{
    struct_0 *cur;  // x20
    unsigned int v1;  // w21
    long long v2;  // x0

    cur = a0;
    if (!(g_1fab154 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab154 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(a1, 0, 0) & 1))
    {
        v1 = 0;
    }
    else
    {
        while (true)
        {
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v2 = Object__op_Inequality(cur, 0, 0);
            v1 = v2;
            if (!((char)v2 & 1))
                break;
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Equality(cur, a1, 0) & 1))
                break;
            if (!cur)
                sub_f7db74();
            cur = cur->field_20;
        }
    }
    return v1 & 1;
}
```

## `GameState.EndState` — RVA `0xc353a8`

- Decompiled symbol: `GameState_EndState`
- Metadata signature: `public void EndState() { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab155;

long long GameState_EndState(void* a0)
{
    unsigned long v0;  // x0
    unsigned long v1;  // x0

    if (!(g_1fab155 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab155 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Inequality((long long)a0[32], 0, 0);
    if (!((char)v0 & 1))
        return v0;
    if ((long long)a0[32])
    {
        v1 = (unsigned long long)GameState__StartSubState((long long)a0[32], 0);
        return (unsigned long long)GameState__StartSubState((long long)a0[32], 0);
    }
    sub_f7db74(0);
}
```

## `GameState.EndSubState` — RVA `0xc3542c`

- Decompiled symbol: `GameState_EndSubState`
- Metadata signature: `public void EndSubState() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
    char padding_8[32];
    unsigned long long field_28;
} struct_2;

typedef struct struct_0 {
    char padding_0[408];
    struct struct_1 *field_198;
    unsigned long long field_1a0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

long long GameState_EndSubState(struct_2 *a0)
{
    unsigned long v0;  // x0

    v0 = (unsigned long long)GameState__StartSubState(a0, 0);
    return (unsigned long long)GameState__StartSubState(a0, 0);
}
```

## `GameState.GetSubState` — RVA `0xc35434`

- Decompiled symbol: `GameState_GetSubState`
- Metadata signature: `public GameState GetSubState() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned long long field_28;
} struct_0;

long long GameState_GetSubState(struct_0 *a0)
{
    return a0->field_28;
}
```

## `GameState.IsSubStateRunning` — RVA `0xc3543c`

- Decompiled symbol: `GameState_IsSubStateRunning`
- Metadata signature: `public bool IsSubStateRunning() { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab156;

void GameState_IsSubStateRunning(unsigned long a0)
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
    if (!(g_1fab156 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab156 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    Object__op_Inequality();
    return;
}
```

## `GameState.ctor` — RVA `0xc3549c`

- Decompiled symbol: `GameState_ctor`
- Metadata signature: `protected void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long GameState_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
