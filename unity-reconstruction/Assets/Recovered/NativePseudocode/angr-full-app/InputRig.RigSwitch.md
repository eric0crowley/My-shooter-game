# Native pseudocode: InputRig.RigSwitch

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InputRig.RigSwitch.ctor` — RVA `0xc3f138`

- Decompiled symbol: `InputRig_RigSwitch_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long InputRig_RigSwitch_ctor(void)
{
    long long v0;  // x0

    v0 = Object__ctor();
    return Object__ctor();
}
```

## `InputRig.RigSwitch.ToggleState` — RVA `0xc3f380`

- Decompiled symbol: `InputRig_RigSwitch_ToggleState`
- Metadata signature: `public bool ToggleState() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[25];
    char field_19;
} struct_0;

long long InputRig_RigSwitch_ToggleState(struct_0 *ptr)
{
    unsigned int v0;  // w9
    unsigned int v1;  // w8

    v0 = ptr->field_19;
    if (v0)
        v1 = 0;
    else
        v1 = 1;
    ptr->field_19 = (char)v0 ^ 1;
    return v1;
}
```

## `InputRig.RigSwitch.ctor` — RVA `0xc3f63c`

- Decompiled symbol: `InputRig_RigSwitch_ctor`
- Metadata signature: `public void .ctor(string name) { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

void InputRig_RigSwitch_ctor(struct_0 *ptr, unsigned long a1)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    Object__ctor();
    ptr->field_10 = a1;
    sub_f7d8d0();
    return;
}
```

## `InputRig.RigSwitch.SetState` — RVA `0xc3f66c`

- Decompiled symbol: `InputRig_RigSwitch_SetState`
- Metadata signature: `public void SetState(bool state) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[25];
    char field_19;
} struct_0;

struct_0 * InputRig_RigSwitch_SetState(struct_0 *ptr, char a1)
{
    ptr->field_19 = a1 & 1;
    return ptr;
}
```

## `InputRig.RigSwitch.GetState` — RVA `0xc3f678`

- Decompiled symbol: `InputRig_RigSwitch_GetState`
- Metadata signature: `public bool GetState() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[25];
    char field_19;
} struct_0;

long long InputRig_RigSwitch_GetState(struct_0 *a0)
{
    return a0->field_19;
}
```

## `InputRig.RigSwitch.Reset` — RVA `0xc3f680`

- Decompiled symbol: `InputRig_RigSwitch_Reset`
- Metadata signature: `public override void Reset() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
char [26] InputRig_RigSwitch_Reset(char *ptr)
{
    ptr[25] = ptr[24];
    return ptr;
}
```
