# Native pseudocode: DigitalBinding.AxisElem

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DigitalBinding.AxisElem.SetAxis` — RVA `0xc5c0bc`

- Decompiled symbol: `DigitalBinding_AxisElem_SetAxis`
- Metadata signature: `public void SetAxis(string axisName, bool positiveSide) { }`
- Native interval: `44` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DigitalBinding_AxisElem_Recovered` matched 2 offsets against `DigitalBinding.AxisElem` metadata (confidence 1.00).

```c
typedef struct DigitalBinding_AxisElem_Recovered {
    char padding_0[16];
    unsigned long long axisName;
    char axisPositiveSide;
} DigitalBinding_AxisElem_Recovered;

long long DigitalBinding_AxisElem_SetAxis(struct_0 *ptr, unsigned long a1, char a2)
{
    struct_0 *p;  // x19
    unsigned long v1;  // x0

    ptr->field_10 = a1;
    p = &ptr->field_10;
    v1 = sub_f7d8d0(p);
    p->padding_0[8] = a2 & 1;
    return v1;
}
```

## `DigitalBinding.AxisElem.CopyFrom` — RVA `0xc5c434`

- Decompiled symbol: `DigitalBinding_AxisElem_CopyFrom`
- Metadata signature: `public void CopyFrom(DigitalBinding.AxisElem b) { }`
- Native interval: `60` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DigitalBinding_AxisElem_Recovered` matched 2 offsets against `DigitalBinding.AxisElem` metadata (confidence 1.00).

```c
typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
    char field_18;
} struct_0;

typedef struct DigitalBinding_AxisElem_Recovered {
    char padding_0[16];
    long long axisName;
    char axisPositiveSide;
} DigitalBinding_AxisElem_Recovered;

long long DigitalBinding_AxisElem_CopyFrom(struct_1 *ptr, struct_0 *p)
{
    long long v0;  // x1
    struct_1 *addr;  // x20
    unsigned long v2;  // x0

    if (p)
    {
        v0 = p->field_10;
        ptr->field_10 = v0;
        addr = &ptr->field_10;
        v2 = sub_f7d8d0(addr, v0);
        addr->padding_0[8] = p->field_18;
        return v2;
    }
    sub_f7db74();
}
```

## `DigitalBinding.AxisElem.ApplyToRig` — RVA `0xc5c470`

- Decompiled symbol: `DigitalBinding_AxisElem_ApplyToRig`
- Metadata signature: `public void ApplyToRig(InputRig rig, bool skipIfTargetIsMuted) { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[146];
    char field_92;
} struct_1;

typedef struct struct_0 {
    char padding_0[128];
    unsigned long long field_80;
} struct_0;

struct_1 * DigitalBinding_AxisElem_ApplyToRig(struct_0 *a0, struct_0 *a1, unsigned int a2)
{
    struct_1 *v0;  // x0
    char v1[209];  // x0

    if (a1)
    {
        v0 = (unsigned long long)InputRig__GetAxisConfig(a1, *((long long *)&a0->padding_0[16]), &a0->padding_0[28]);
        if (!v0)
            return v0;
        if (((char)a2 & 1) && v0->field_92)
            return v0;
        v1 = InputRig_AxisConfig__SetSignedDigital(v0, a0->padding_0[24]);
        return InputRig_AxisConfig__SetSignedDigital(v0, a0->padding_0[24]);
    }
    sub_f7db74();
}
```

## `DigitalBinding.AxisElem.ctor` — RVA `0xc5c6b0`

- Decompiled symbol: `DigitalBinding_AxisElem_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `104` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DigitalBinding_AxisElem_Recovered` matched 2 offsets against `DigitalBinding.AxisElem` metadata (confidence 1.00).

```c
typedef struct DigitalBinding_AxisElem_Recovered {
    char padding_0[16];
    unsigned long long axisName;
    char axisPositiveSide;
} DigitalBinding_AxisElem_Recovered;

extern char g_1fab2c4;

void DigitalBinding_AxisElem_ctor(struct_2 *ptr)
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
    if (!(g_1fab2c4 & 1))
    {
        sub_f7d92c("MT");
        g_1fab2c4 = 1;
    }
    Object__ctor(ptr, 0);
    ptr->field_18 = 1;
    ptr->field_10 = g_1ef18f0->field_b8->field_0;
    sub_f7d8d0();
    return;
}
```

## `DigitalBinding.AxisElem.OnIsBoundToAxis` — RVA `0xc5c9bc`

- Decompiled symbol: `DigitalBinding_AxisElem_OnIsBoundToAxis`
- Metadata signature: `private bool OnIsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
void DigitalBinding_AxisElem_OnIsBoundToAxis(unsigned long a0)
{
    String__op_Equality();
    return;
}
```
