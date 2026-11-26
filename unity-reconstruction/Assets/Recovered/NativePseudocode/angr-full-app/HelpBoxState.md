# Native pseudocode: HelpBoxState

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `HelpBoxState.ShowHelpBox` — RVA `0xc648e0`

- Decompiled symbol: `HelpBoxState_ShowHelpBox`
- Metadata signature: `public void ShowHelpBox(DemoMainState parentDemoState) { }`
- Native interval: `60` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[56];
    unsigned long long field_38;
} struct_0;

void HelpBoxState_ShowHelpBox(struct_0 *ptr, unsigned long long a1)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_0 *v6;  // x20
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    ptr->field_38 = a1;
    v6 = &ptr->field_38;
    sub_f7d8d0(v6);
    if (!*((long long *)&v6->padding_0[0]))
        sub_f7db74(0);
}
```

## `HelpBoxState.OnStartState` — RVA `0xc6492c`

- Decompiled symbol: `HelpBoxState_OnStartState`
- Metadata signature: `protected override void OnStartState(GameState parentState) { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
void HelpBoxState_OnStartState(long long a0)
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

## `HelpBoxState.OnExitState` — RVA `0xc64960`

- Decompiled symbol: `HelpBoxState_OnExitState`
- Metadata signature: `protected override void OnExitState() { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
void HelpBoxState_OnExitState(long long a0)
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

## `HelpBoxState.ExitToMainMenu` — RVA `0xc64994`

- Decompiled symbol: `HelpBoxState_ExitToMainMenu`
- Metadata signature: `public void ExitToMainMenu() { }`
- Native interval: `128` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2ef;

unsigned long long HelpBoxState_ExitToMainMenu(void* a0)
{
    unsigned long long v0;  // x0

    if (!(g_1fab2ef & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab2ef = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Inequality((long long)a0[56], 0, 0);
    if (!((char)v0 & 1))
        return v0;
    if ((long long)a0[56])
        DemoMainState__ExitToMainMenu((long long)a0[56]); /* do not return */
    sub_f7db74(0);
}
```

## `HelpBoxState.ctor` — RVA `0xc64a14`

- Decompiled symbol: `HelpBoxState_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long HelpBoxState_ctor(void)
{
}
```
