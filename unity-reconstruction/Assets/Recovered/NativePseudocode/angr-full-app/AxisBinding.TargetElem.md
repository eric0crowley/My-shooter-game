# Native pseudocode: AxisBinding.TargetElem

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AxisBinding.TargetElem.SetSingleAxis` — RVA `0xc5b50c`

- Decompiled symbol: `AxisBinding_TargetElem_SetSingleAxis`
- Metadata signature: `public void SetSingleAxis(string name, bool flip) { }`
- Native interval: `48` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AxisBinding_TargetElem_Recovered` matched 3 offsets against `AxisBinding.TargetElem` metadata (confidence 1.00).

```c
typedef struct AxisBinding_TargetElem_Recovered {
    char padding_0[16];
    char separateAxes;
    char padding_11[7];
    unsigned long long singleAxis;
    char reverseSingleAxis;
} AxisBinding_TargetElem_Recovered;

long long AxisBinding_TargetElem_SetSingleAxis(struct_0 *p, unsigned long a1, char a2)
{
    struct_0 *ptr;  // x19
    unsigned long v1;  // x0

    p->field_18 = a1;
    ptr = &p->field_18;
    ptr->padding_0[8] = 0;
    v1 = sub_f7d8d0(ptr);
    ptr->padding_0[8] = a2 & 1;
    return v1;
}
```

## `AxisBinding.TargetElem.CopyFrom` — RVA `0xc5b690`

- Decompiled symbol: `AxisBinding_TargetElem_CopyFrom`
- Metadata signature: `public void CopyFrom(AxisBinding.TargetElem elem) { }`
- Native interval: `112` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AxisBinding_TargetElem_Recovered` matched 7 offsets against `AxisBinding.TargetElem` metadata (confidence 1.00).

```c
typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    long long field_18;
    char field_20;
    char padding_21[7];
    long long field_28;
    long long field_30;
    char field_38;
    char field_39;
} struct_0;

typedef struct AxisBinding_TargetElem_Recovered {
    char padding_0[16];
    char separateAxes;
    char padding_11[7];
    long long singleAxis;
    char reverseSingleAxis;
    char padding_21[7];
    long long positiveAxis;
    long long negativeAxis;
    char positiveAxisAsPositive;
    char negativeAxisAsPositive;
} AxisBinding_TargetElem_Recovered;

long long AxisBinding_TargetElem_CopyFrom(struct_1 *ptr, struct_0 *p)
{
    long long v0;  // x1
    long long v1;  // x1
    long long v2;  // x1
    struct_1 *addr;  // x20
    unsigned long v4;  // x0

    if (p)
    {
        ptr->field_10 = p->field_10;
        v0 = p->field_18;
        ptr->field_18 = v0;
        sub_f7d8d0((struct AxisBinding_TargetElem_Recovered *)&ptr->field_18, v0);
        ptr->field_20 = p->field_20;
        v1 = p->field_28;
        ptr->field_28 = v1;
        sub_f7d8d0((struct AxisBinding_TargetElem_Recovered *)&ptr->field_28, v1);
        ptr->field_38 = p->field_38;
        v2 = p->field_30;
        ptr->field_30 = v2;
        addr = &ptr->field_30;
        v4 = sub_f7d8d0(addr, v2);
        addr->padding_0[9] = p->field_39;
        return v4;
    }
    sub_f7db74();
}
```

## `AxisBinding.TargetElem.ctor` — RVA `0xc5b770`

- Decompiled symbol: `AxisBinding_TargetElem_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `148` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AxisBinding_TargetElem_Recovered` matched 8 offsets against `AxisBinding.TargetElem` metadata (confidence 1.00).

```c
typedef struct AxisBinding_TargetElem_Recovered {
    char padding_0[16];
    char separateAxes;
    char padding_11[7];
    long long singleAxis;
    char reverseSingleAxis;
    char padding_21[7];
    long long positiveAxis;
    long long negativeAxis;
    unsigned short positiveAxisAsPositive;
    char padding_3a[2];
    unsigned int singleAxisId;
    unsigned long long positiveAxisId;
} AxisBinding_TargetElem_Recovered;

extern long long g_1f06220;
extern char g_1fab2b5;

long long AxisBinding_TargetElem_ctor(struct_0 *ptr)
{
    struct_0 *addr;  // x0
    struct_0 *ptr3;  // x0
    struct_0 *p;  // x19
    unsigned long v3;  // x0

    if (!(g_1fab2b5 & 1))
    {
        sub_f7d92c(&g_1f06220);
        g_1fab2b5 = 1;
    }
    Object__ctor(ptr, 0);
    ptr->field_10 = 0;
    addr = ptr;
    addr->field_18 = g_1f06220;
    sub_f7d8d0((struct AxisBinding_TargetElem_Recovered *)&addr->field_18, g_1f06220);
    ptr->field_20 = 0;
    ptr3 = ptr;
    ptr3->field_28 = g_1f06220;
    sub_f7d8d0((struct AxisBinding_TargetElem_Recovered *)&ptr3->field_28, g_1f06220);
    ptr->field_30 = g_1f06220;
    p = &ptr->field_30;
    v3 = sub_f7d8d0(p, g_1f06220);
    *((unsigned long *)&p->field_10) = 0;
    *((unsigned int *)&p->padding_0[12]) = 0;
    *((unsigned short *)&p->padding_0[8]) = 257;
    return v3;
}
```

## `AxisBinding.TargetElem.SyncFloat` — RVA `0xc5b8fc`

- Decompiled symbol: `AxisBinding_TargetElem_SyncFloat`
- Metadata signature: `public void SyncFloat(float val, InputRig.InputSource source, InputRig rig) { }`
- Native interval: `140` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AxisBinding_TargetElem_Recovered` matched 7 offsets against `AxisBinding.TargetElem` metadata (confidence 1.00).

```c
typedef struct AxisBinding_TargetElem_Recovered {
    char padding_0[16];
    char separateAxes;
    char padding_11[7];
    unsigned long long singleAxis;
    char reverseSingleAxis;
    char padding_21[7];
    unsigned long long positiveAxis;
    unsigned long long negativeAxis;
    char positiveAxisAsPositive;
    char negativeAxisAsPositive;
} AxisBinding_TargetElem_Recovered;

unsigned long long AxisBinding_TargetElem_SyncFloat(struct_0 *ptr, unsigned int a1, struct_0 *a2)
{
    unsigned int v0;  // s0
    unsigned long v1;  // 4125
    unsigned long v2;  // x1
    struct_0 *v3;  // x8
    unsigned long long v4;  // x0

    if (ptr->field_10)
    {
        v1 = arm64g_calculate_condition(160, (((((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v0, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v1))
        {
            if (a2)
            {
                v2 = ptr->field_30;
                v3 = &ptr[1].padding_0[10];
            }
            else
            {
                sub_f7db74();
            }
        }
        else
        {
            if (a2)
            {
                v2 = ptr->field_28;
                v3 = &ptr[1].padding_0[6];
            }
            else
            {
                sub_f7db74();
            }
        }
    }
    else if (a2)
    {
        v2 = ptr->field_18;
        v3 = &ptr[1].padding_0[2];
    }
    else
    {
        sub_f7db74();
    }
    v4 = InputRig__SetAxis(a2, v2, v3, a1);
    return InputRig__SetAxis(a2, v2, v3, a1);
}
```

## `AxisBinding.TargetElem.SyncScroll` — RVA `0xc5ba68`

- Decompiled symbol: `AxisBinding_TargetElem_SyncScroll`
- Metadata signature: `public void SyncScroll(int val, InputRig rig) { }`
- Native interval: `72` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AxisBinding_TargetElem_Recovered` matched 3 offsets against `AxisBinding.TargetElem` metadata (confidence 1.00).

```c
typedef struct AxisBinding_TargetElem_Recovered {
    char padding_0[16];
    char separateAxes;
    char padding_11[7];
    long long singleAxis;
    char reverseSingleAxis;
} AxisBinding_TargetElem_Recovered;

struct_0 * AxisBinding_TargetElem_SyncScroll(struct_0 *a0, unsigned int a1, struct_0 *a2)
{
    unsigned long v0;  // x3
    unsigned long long v1;  // x0

    if (a0->field_10)
        return a0;
    if (a2)
    {
        if (!a0->field_20)
            v0 = a1;
        else
            v0 = -(a1);
        v1 = InputRig__SetAxisScroll(a2, a0->field_18, (char *)&a0[1].field_18 + 3, v0);
        return InputRig__SetAxisScroll(a2, a0->field_18, (char *)&a0[1].field_18 + 3, v0);
    }
    sub_f7db74();
}
```

## `AxisBinding.TargetElem.IsBoundToAxis` — RVA `0xc5bb60`

- Decompiled symbol: `AxisBinding_TargetElem_IsBoundToAxis`
- Metadata signature: `public bool IsBoundToAxis(string axisName) { }`
- Native interval: `96` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AxisBinding_TargetElem_Recovered` matched 2 offsets against `AxisBinding.TargetElem` metadata (confidence 1.00).

```c
typedef struct AxisBinding_TargetElem_Recovered {
    char padding_0[16];
    char separateAxes;
    char padding_11[23];
    long long positiveAxis;
} AxisBinding_TargetElem_Recovered;

unsigned int AxisBinding_TargetElem_IsBoundToAxis(struct_0 *a0, long long a1)
{
    if (a0->field_10 && ((char)String__op_Equality(a0->field_28, a1, 0) & 1))
        return 1;
    return String__op_Equality();
}
```

## `AxisBinding.TargetElem.GetAxis` — RVA `0xc5bd20`

- Decompiled symbol: `AxisBinding_TargetElem_GetAxis`
- Metadata signature: `public float GetAxis(InputRig rig) { }`
- Native interval: `256` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x105bd20: str d8, [sp, #-0x30]!
// 0x105bd24: str x30, [sp, #8]
// 0x105bd28: stp x22, x21, [sp, #0x10]
// 0x105bd2c: stp x20, x19, [sp, #0x20]
// 0x105bd30: adrp x21, #0x1fab000
// 0x105bd34: adrp x22, #0x1e8c000
// 0x105bd38: ldrb w8, [x21, #0x2b6]
// 0x105bd3c: ldr x22, [x22, #0xd8]
// 0x105bd40: mov x19, x1
// 0x105bd44: mov x20, x0
// 0x105bd48: tbnz w8, #0, #0x105bd60
// 0x105bd4c: adrp x0, #0x1e8c000
// 0x105bd50: ldr x0, [x0, #0xd8]
// 0x105bd54: bl #0xf7d92c
// 0x105bd58: mov w8, #1
// 0x105bd5c: strb w8, [x21, #0x2b6]
// 0x105bd60: ldr x0, [x22]
// 0x105bd64: ldr w8, [x0, #0xe0]
// 0x105bd68: cbnz w8, #0x105bd70
// 0x105bd6c: bl #0xf7da5c
// 0x105bd70: mov x0, x19
// 0x105bd74: mov x1, xzr
// 0x105bd78: mov x2, xzr
// 0x105bd7c: bl #0x1b9568c
// 0x105bd80: fmov s0, wzr
// 0x105bd84: tbnz w0, #0, #0x105bde0
// 0x105bd88: ldrb w8, [x20, #0x10]
// 0x105bd8c: cbz w8, #0x105bdf4
// 0x105bd90: cbz x19, #0x105be1c
// 0x105bd94: ldr x1, [x20, #0x28]
// 0x105bd98: ldrb w21, [x20, #0x38]
// 0x105bd9c: add x2, x20, #0x40
// 0x105bda0: mov x0, x19
// 0x105bda4: mov x3, xzr
// 0x105bda8: bl #0x1036050
// 0x105bdac: ldr x1, [x20, #0x30]
// 0x105bdb0: ldrb w22, [x20, #0x39]
// 0x105bdb4: fneg s1, s0
// 0x105bdb8: cmp w21, #0
// 0x105bdbc: add x2, x20, #0x44
// 0x105bdc0: mov x0, x19
// 0x105bdc4: mov x3, xzr
// 0x105bdc8: fcsel s8, s1, s0, eq
// 0x105bdcc: bl #0x1036050
// 0x105bdd0: fneg s1, s0
// 0x105bdd4: cmp w22, #0
// 0x105bdd8: fcsel s0, s1, s0, eq
// 0x105bddc: fsub s0, s8, s0
// 0x105bde0: ldp x20, x19, [sp, #0x20]
// 0x105bde4: ldp x22, x21, [sp, #0x10]
// 0x105bde8: ldr x30, [sp, #8]
// 0x105bdec: ldr d8, [sp], #0x30
// 0x105bdf0: ret
// 0x105bdf4: cbz x19, #0x105be1c
// 0x105bdf8: ldr x1, [x20, #0x18]
// 0x105bdfc: add x2, x20, #0x3c
// 0x105be00: mov x0, x19
// 0x105be04: ldp x20, x19, [sp, #0x20]
// 0x105be08: ldp x22, x21, [sp, #0x10]
// 0x105be0c: ldr x30, [sp, #8]
// 0x105be10: mov x3, xzr
// 0x105be14: ldr d8, [sp], #0x30
// 0x105be18: b #0x1036050
// 0x105be1c: bl #0xf7db74
```

## `AxisBinding.TargetElem.SetSeparateAxis` — RVA `0xc5be20`

- Decompiled symbol: `AxisBinding_TargetElem_SetSeparateAxis`
- Metadata signature: `public void SetSeparateAxis(string name, bool positiveSide, bool asPositive) { }`
- Native interval: `76` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AxisBinding_TargetElem_Recovered` matched 5 offsets against `AxisBinding.TargetElem` metadata (confidence 1.00).

```c
typedef struct AxisBinding_TargetElem_Recovered {
    char padding_0[16];
    char separateAxes;
    char padding_11[23];
    unsigned long long positiveAxis;
    unsigned long long negativeAxis;
    char positiveAxisAsPositive;
    char negativeAxisAsPositive;
} AxisBinding_TargetElem_Recovered;

long long AxisBinding_TargetElem_SetSeparateAxis(struct_0 *ptr, unsigned long a1, unsigned long a2, char a3)
{
    char v0;  // x20
    struct_0 *p;  // x19
    unsigned long v2;  // x0
    struct_0 *addr;  // x19
    unsigned long v4;  // x0

    v0 = a3 & 1;
    ptr->field_10 = 1;
    if (!((char)a2 & 1))
    {
        ptr->field_30 = a1;
        addr = &ptr->field_30;
        v4 = sub_f7d8d0(addr);
        addr->padding_0[9] = v0;
        return v4;
    }
    ptr->field_28 = a1;
    p = &ptr->field_28;
    v2 = sub_f7d8d0(p);
    p->field_10 = v0;
    return v2;
}
```
