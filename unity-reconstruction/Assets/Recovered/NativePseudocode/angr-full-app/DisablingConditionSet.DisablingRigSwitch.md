# Native pseudocode: DisablingConditionSet.DisablingRigSwitch

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DisablingConditionSet.DisablingRigSwitch.IsInEffect` — RVA `0xc5b0bc`

- Decompiled symbol: `DisablingConditionSet_DisablingRigSwitch_IsInEffect`
- Metadata signature: `public bool IsInEffect(InputRig rig) { }`
- Native interval: `68` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DisablingConditionSet_DisablingRigSwitch_Recovered` matched 2 offsets against `DisablingConditionSet.DisablingRigSwitch` metadata (confidence 1.00).

```c
typedef struct struct_0 {
    char padding_0[248];
    long long field_f8;
} struct_0;

typedef struct DisablingConditionSet_DisablingRigSwitch_Recovered {
    char padding_0[16];
    long long name;
    char disableWhenSwitchIsOff;
} DisablingConditionSet_DisablingRigSwitch_Recovered;

unsigned long long DisablingConditionSet_DisablingRigSwitch_IsInEffect(struct_1 *a0, struct_0 *a1)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned int v4;  // w0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    if (a1 && a1->field_f8)
    {
        v4 = InputRig_RigSwitchCollection__GetSwitchState(a1->field_f8, a0->field_10, &a0[1].padding_0[3], a0->field_18);
        if (a0->field_18 != (v4 & 1))
            return 1;
        return 0;
    }
    sub_f7db74();
}
```

## `DisablingConditionSet.DisablingRigSwitch.ctor` — RVA `0xc5b100`

- Decompiled symbol: `DisablingConditionSet_DisablingRigSwitch_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

extern unsigned long long g_1f06220;
extern char g_1fab2a9;

void DisablingConditionSet_DisablingRigSwitch_ctor(struct_0 *ptr)
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
    if (!(g_1fab2a9 & 1))
    {
        sub_f7d92c(&g_1f06220);
        g_1fab2a9 = 1;
    }
    Object__ctor(ptr, 0);
    ptr->field_10 = g_1f06220;
    sub_f7d8d0();
    return;
}
```

## `DisablingConditionSet.DisablingRigSwitch.ctor` — RVA `0xc5b158`

- Decompiled symbol: `DisablingConditionSet_DisablingRigSwitch_ctor`
- Metadata signature: `public void .ctor(string name) { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

void DisablingConditionSet_DisablingRigSwitch_ctor(struct_0 *ptr, unsigned long a1)
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
