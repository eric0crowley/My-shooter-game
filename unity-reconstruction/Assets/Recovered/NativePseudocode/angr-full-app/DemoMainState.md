# Native pseudocode: DemoMainState

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DemoMainState.OnStartState` — RVA `0xc6466c`

- Decompiled symbol: `DemoMainState_OnStartState`
- Metadata signature: `protected override void OnStartState(GameState parentState) { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
void DemoMainState_OnStartState(long long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    GameState__OnStartState();
    if (Component__get_gameObject(a0, 0))
    {
        GameObject__SetActive();
        return;
    }
    sub_f7db74();
}
```

## `DemoMainState.OnExitState` — RVA `0xc646a0`

- Decompiled symbol: `DemoMainState_OnExitState`
- Metadata signature: `protected override void OnExitState() { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
void DemoMainState_OnExitState(long long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    GameState__OnExitState();
    if (Component__get_gameObject(a0, 0))
    {
        GameObject__SetActive();
        return;
    }
    sub_f7db74();
}
```

## `DemoMainState.OnUpdateState` — RVA `0xc646d4`

- Decompiled symbol: `DemoMainState_OnUpdateState`
- Metadata signature: `protected override void OnUpdateState() { }`
- Native interval: `204` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DemoMainState_Recovered` matched 2 offsets against `DemoMainState` metadata (confidence 1.00).

```c
typedef struct DemoMainState_Recovered {
    char padding_0[64];
    struct struct_2 *helpBox;
    unsigned int helpKey;
} DemoMainState_Recovered;

typedef struct struct_2 {
    char padding_0[48];
    char field_30;
} struct_2;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed00;
extern struct_1 *g_1ef0c58;
extern char g_1fab2ec;

void DemoMainState_OnUpdateState(struct_3 *a0)
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
    if (!(g_1fab2ec & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab2ec = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(a0->field_40, 0, 0) & 1))
    {
        if (!a0->field_40)
        {
            sub_f7db74();
        }
        else if (!a0->field_40->field_30 && a0->field_48)
        {
            if (!g_1eeed00->field_e0)
                sub_f7da5c(g_1eeed00);
            if (((char)CF2Input__GetKeyDown(a0->field_48, 0) & 1))
                DemoMainState__ShowHelpBox();
        }
    }
}
```

## `DemoMainState.ShowHelpBox` — RVA `0xc647a0`

- Decompiled symbol: `DemoMainState_ShowHelpBox`
- Metadata signature: `public void ShowHelpBox() { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[64];
    long long field_40;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2ee;

unsigned long long DemoMainState_ShowHelpBox(struct_1 *a0)
{
    unsigned long long v0;  // x0

    if (!(g_1fab2ee & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab2ee = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Inequality(a0->field_40, 0, 0);
    if (!((char)v0 & 1))
        return v0;
    if (a0->field_40)
        HelpBoxState__ShowHelpBox(a0->field_40, a0); /* do not return */
    sub_f7db74(0);
}
```

## `DemoMainState.ExitToMainMenu` — RVA `0xc64824`

- Decompiled symbol: `DemoMainState_ExitToMainMenu`
- Metadata signature: `public void ExitToMainMenu() { }`
- Native interval: `176` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[56];
    long long field_38;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_0 *g_1eee870;
extern struct_1 *g_1ef0c58;
extern char g_1fab2ed;

void DemoMainState_ExitToMainMenu(struct_2 *a0)
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
    if (!(g_1fab2ed & 1))
    {
        sub_f7d92c(&g_1eee870);
        sub_f7d92c(&g_1ef0c58);
        g_1fab2ed = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(a0->field_38, 0, 0) & 1))
    {
        if (!g_1eee870->field_e0)
            sub_f7da5c(g_1eee870);
        Application__Quit();
        return;
    }
    else if (!a0->field_38)
    {
        sub_f7db74(0);
    }
}
```

## `DemoMainState.ctor` — RVA `0xc6491c`

- Decompiled symbol: `DemoMainState_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[72];
    unsigned int field_48;
} struct_0;

long long DemoMainState_ctor(struct_0 *ptr)
{
    ptr->field_48 = 27;
}
```
