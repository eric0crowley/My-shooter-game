# Native pseudocode: MultiDemoManager

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MultiDemoManager.EnterMainMenu` — RVA `0xc648d4`

- Decompiled symbol: `MultiDemoManager_EnterMainMenu`
- Metadata signature: `public void EnterMainMenu() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
long long MultiDemoManager_EnterMainMenu(unsigned long a0)
{
}
```

## `MultiDemoManager.Start` — RVA `0xc64a1c`

- Decompiled symbol: `MultiDemoManager_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[376];
    unsigned long long field_178;
} struct_0;

long long MultiDemoManager_Start(struct_0 **a0)
{
    goto *(a0)->field_178;
}
```

## `MultiDemoManager.Update` — RVA `0xc64a2c`

- Decompiled symbol: `MultiDemoManager_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    char padding_8[40];
    char field_30;
} struct_1;

typedef struct struct_0 {
    char padding_0[440];
    unsigned long long field_1b8;
} struct_0;

struct_1 * MultiDemoManager_Update(struct_1 *a0)
{
    if (!a0->field_30)
        return a0;
    goto a0->field_0->field_1b8;
}
```

## `MultiDemoManager.OnStartState` — RVA `0xc64a44`

- Decompiled symbol: `MultiDemoManager_OnStartState`
- Metadata signature: `protected override void OnStartState(GameState parentState) { }`
- Native interval: `68` bytes
- Result: `pseudocode`

```c
void MultiDemoManager_OnStartState(long long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    GameState__OnStartState();
    if (!Component__get_gameObject(a0, 0))
        sub_f7db74();
    GameObject__SetActive();
}
```

## `MultiDemoManager.OnExitState` — RVA `0xc64a88`

- Decompiled symbol: `MultiDemoManager_OnExitState`
- Metadata signature: `protected override void OnExitState() { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
void MultiDemoManager_OnExitState(long long a0)
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

## `MultiDemoManager.ctor` — RVA `0xc64abc`

- Decompiled symbol: `MultiDemoManager_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long MultiDemoManager_ctor(void)
{
}
```
