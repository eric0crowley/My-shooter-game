# Native pseudocode: InputRig

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InputRig.OnDisactivateRig` — RVA `0xc35cf8`

- Decompiled symbol: `InputRig_OnDisactivateRig`
- Metadata signature: `public void OnDisactivateRig() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
void InputRig_OnDisactivateRig(char *a0)
{
    if (a0[59])
    {
        if (Component__get_gameObject())
        {
            GameObject__SetActive();
            return;
        }
        sub_f7db74();
    }
    else if (a0[58])
    {
        InputRig__ShowOrHideTouchControls();
        return;
    }
    else
    {
        return;
    }
}
```

## `InputRig.OnActivateRig` — RVA `0xc35d44`

- Decompiled symbol: `InputRig_OnActivateRig`
- Metadata signature: `public void OnActivateRig() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[58];
    char field_3a;
} struct_0;

struct_0 * InputRig_OnActivateRig(struct_0 *a0)
{
    unsigned long long v0;  // x0

    if (!a0->field_3a)
        return a0;
    v0 = InputRig__ShowOrHideTouchControls();
    return InputRig__ShowOrHideTouchControls();
}
```

## `InputRig.ResetInputAxes` — RVA `0xc35e1c`

- Decompiled symbol: `InputRig_ResetInputAxes`
- Metadata signature: `public void ResetInputAxes() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
void InputRig_ResetInputAxes(unsigned long a0)
{
    InputRig__MuteUntilRelease(); /* do not return */
}
```

## `InputRig.GetAxis` — RVA `0xc35ef4`

- Decompiled symbol: `InputRig_GetAxis`
- Metadata signature: `public float GetAxis(string axisName) { }`
- Native interval: `116` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x1035ef4: stp x30, x21, [sp, #-0x20]!
// 0x1035ef8: stp x20, x19, [sp, #0x10]
// 0x1035efc: adrp x21, #0x1fab000
// 0x1035f00: ldrb w8, [x21, #0x1b1]
// 0x1035f04: mov x19, x1
// 0x1035f08: mov x20, x0
// 0x1035f0c: tbnz w8, #0, #0x1035f24
// 0x1035f10: adrp x0, #0x1e8c000
// 0x1035f14: ldr x0, [x0, #0x460]
// 0x1035f18: bl #0xf7d92c
// 0x1035f1c: mov w8, #1
// 0x1035f20: strb w8, [x21, #0x1b1]
// 0x1035f24: ldr x0, [x20, #0x80]
// 0x1035f28: cbz x0, #0x1035f64
// 0x1035f2c: adrp x8, #0x1e8c000
// 0x1035f30: ldr x8, [x8, #0x460]
// 0x1035f34: mov x1, x19
// 0x1035f38: ldr x2, [x8]
// 0x1035f3c: bl #0x1526618
// 0x1035f40: cbz x0, #0x1035f54
// 0x1035f44: ldp x20, x19, [sp, #0x10]
// 0x1035f48: mov x1, xzr
// 0x1035f4c: ldp x30, x21, [sp], #0x20
// 0x1035f50: b #0x1041c48
// 0x1035f54: ldp x20, x19, [sp, #0x10]
// 0x1035f58: fmov s0, wzr
// 0x1035f5c: ldp x30, x21, [sp], #0x20
// 0x1035f60: ret
// 0x1035f64: bl #0xf7db74
```

## `InputRig.GetAxis` — RVA `0xc36050`

- Decompiled symbol: `InputRig_GetAxis`
- Metadata signature: `public float GetAxis(string axisName, ref int cachedId) { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[128];
    long long field_80;
} struct_0;

extern long long g_1ef9858;
extern char g_1fab1b2;

unsigned long long InputRig_GetAxis(struct_0 *a0, long long a1, long long a2)
{
    unsigned long long v0;  // x0

    if (!(g_1fab1b2 & 1))
    {
        sub_f7d92c(&g_1ef9858);
        g_1fab1b2 = 1;
    }
    if (a0->field_80)
    {
        if (sub_15264f8(a0->field_80, a1, a2, g_1ef9858))
        {
            v0 = InputRig_AxisConfig__GetAnalog();
            return InputRig_AxisConfig__GetAnalog();
        }
        return 0;
    }
    sub_f7db74(0);
}
```

## `InputRig.GetAxisRaw` — RVA `0xc361ac`

- Decompiled symbol: `InputRig_GetAxisRaw`
- Metadata signature: `public float GetAxisRaw(string axisName) { }`
- Native interval: `116` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x10361ac: stp x30, x21, [sp, #-0x20]!
// 0x10361b0: stp x20, x19, [sp, #0x10]
// 0x10361b4: adrp x21, #0x1fab000
// 0x10361b8: ldrb w8, [x21, #0x1b3]
// 0x10361bc: mov x19, x1
// 0x10361c0: mov x20, x0
// 0x10361c4: tbnz w8, #0, #0x10361dc
// 0x10361c8: adrp x0, #0x1e8c000
// 0x10361cc: ldr x0, [x0, #0x460]
// 0x10361d0: bl #0xf7d92c
// 0x10361d4: mov w8, #1
// 0x10361d8: strb w8, [x21, #0x1b3]
// 0x10361dc: ldr x0, [x20, #0x80]
// 0x10361e0: cbz x0, #0x103621c
// 0x10361e4: adrp x8, #0x1e8c000
// 0x10361e8: ldr x8, [x8, #0x460]
// 0x10361ec: mov x1, x19
// 0x10361f0: ldr x2, [x8]
// 0x10361f4: bl #0x1526618
// 0x10361f8: cbz x0, #0x103620c
// 0x10361fc: ldp x20, x19, [sp, #0x10]
// 0x1036200: mov x1, xzr
// 0x1036204: ldp x30, x21, [sp], #0x20
// 0x1036208: b #0x1041c64
// 0x103620c: ldp x20, x19, [sp, #0x10]
// 0x1036210: fmov s0, wzr
// 0x1036214: ldp x30, x21, [sp], #0x20
// 0x1036218: ret
// 0x103621c: bl #0xf7db74
```

## `InputRig.GetAxisRaw` — RVA `0xc36308`

- Decompiled symbol: `InputRig_GetAxisRaw`
- Metadata signature: `public float GetAxisRaw(string axisName, ref int cachedId) { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[128];
    long long field_80;
} struct_0;

extern long long g_1ef9858;
extern char g_1fab1b4;

unsigned long long InputRig_GetAxisRaw(struct_0 *a0, long long a1, long long a2)
{
    unsigned long long v0;  // x0

    if (!(g_1fab1b4 & 1))
    {
        sub_f7d92c(&g_1ef9858);
        g_1fab1b4 = 1;
    }
    if (a0->field_80)
    {
        if (sub_15264f8(a0->field_80, a1, a2, g_1ef9858))
        {
            v0 = InputRig_AxisConfig__GetAnalogRaw();
            return InputRig_AxisConfig__GetAnalogRaw();
        }
        return 0;
    }
    sub_f7db74(0);
}
```

## `InputRig.GetButton` — RVA `0xc36464`

- Decompiled symbol: `InputRig_GetButton`
- Metadata signature: `public bool GetButton(string axisName) { }`
- Native interval: `108` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x1036464: stp x30, x21, [sp, #-0x20]!
// 0x1036468: stp x20, x19, [sp, #0x10]
// 0x103646c: adrp x21, #0x1fab000
// 0x1036470: ldrb w8, [x21, #0x1b5]
// 0x1036474: mov x19, x1
// 0x1036478: mov x20, x0
// 0x103647c: tbnz w8, #0, #0x1036494
// 0x1036480: adrp x0, #0x1e8c000
// 0x1036484: ldr x0, [x0, #0x460]
// 0x1036488: bl #0xf7d92c
// 0x103648c: mov w8, #1
// 0x1036490: strb w8, [x21, #0x1b5]
// 0x1036494: ldr x0, [x20, #0x80]
// 0x1036498: cbz x0, #0x10364cc
// 0x103649c: adrp x8, #0x1e8c000
// 0x10364a0: ldr x8, [x8, #0x460]
// 0x10364a4: mov x1, x19
// 0x10364a8: ldr x2, [x8]
// 0x10364ac: bl #0x1526618
// 0x10364b0: cbz x0, #0x10364c0
// 0x10364b4: ldrb w8, [x0, #0x90]
// 0x10364b8: cmp w8, #0
// 0x10364bc: cset w0, ne
// 0x10364c0: ldp x20, x19, [sp, #0x10]
// 0x10364c4: ldp x30, x21, [sp], #0x20
// 0x10364c8: ret
// 0x10364cc: bl #0xf7db74
```

## `InputRig.GetButton` — RVA `0xc365b8`

- Decompiled symbol: `InputRig_GetButton`
- Metadata signature: `public bool GetButton(string axisName, ref int cachedId) { }`
- Native interval: `124` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x10365b8: str x30, [sp, #-0x30]!
// 0x10365bc: stp x22, x21, [sp, #0x10]
// 0x10365c0: stp x20, x19, [sp, #0x20]
// 0x10365c4: adrp x22, #0x1fab000
// 0x10365c8: ldrb w8, [x22, #0x1b6]
// 0x10365cc: mov x19, x2
// 0x10365d0: mov x20, x1
// 0x10365d4: mov x21, x0
// 0x10365d8: tbnz w8, #0, #0x10365f0
// 0x10365dc: adrp x0, #0x1e8c000
// 0x10365e0: ldr x0, [x0, #0x468]
// 0x10365e4: bl #0xf7d92c
// 0x10365e8: mov w8, #1
// 0x10365ec: strb w8, [x22, #0x1b6]
// 0x10365f0: ldr x0, [x21, #0x80]
// 0x10365f4: cbz x0, #0x1036630
// 0x10365f8: adrp x8, #0x1e8c000
// 0x10365fc: ldr x8, [x8, #0x468]
// 0x1036600: mov x1, x20
// 0x1036604: mov x2, x19
// 0x1036608: ldr x3, [x8]
// 0x103660c: bl #0x15264f8
// 0x1036610: cbz x0, #0x1036620
// 0x1036614: ldrb w8, [x0, #0x90]
// 0x1036618: cmp w8, #0
// 0x103661c: cset w0, ne
// 0x1036620: ldp x20, x19, [sp, #0x20]
// 0x1036624: ldp x22, x21, [sp, #0x10]
// 0x1036628: ldr x30, [sp], #0x30
// 0x103662c: ret
// 0x1036630: bl #0xf7db74
```

## `InputRig.GetButtonDown` — RVA `0xc36708`

- Decompiled symbol: `InputRig_GetButtonDown`
- Metadata signature: `public bool GetButtonDown(string axisName) { }`
- Native interval: `112` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x1036708: stp x30, x21, [sp, #-0x20]!
// 0x103670c: stp x20, x19, [sp, #0x10]
// 0x1036710: adrp x21, #0x1fab000
// 0x1036714: ldrb w8, [x21, #0x1b7]
// 0x1036718: mov x19, x1
// 0x103671c: mov x20, x0
// 0x1036720: tbnz w8, #0, #0x1036738
// 0x1036724: adrp x0, #0x1e8c000
// 0x1036728: ldr x0, [x0, #0x460]
// 0x103672c: bl #0xf7d92c
// 0x1036730: mov w8, #1
// 0x1036734: strb w8, [x21, #0x1b7]
// 0x1036738: ldr x0, [x20, #0x80]
// 0x103673c: cbz x0, #0x1036774
// 0x1036740: adrp x8, #0x1e8c000
// 0x1036744: ldr x8, [x8, #0x460]
// 0x1036748: mov x1, x19
// 0x103674c: ldr x2, [x8]
// 0x1036750: bl #0x1526618
// 0x1036754: cbz x0, #0x1036768
// 0x1036758: ldp x20, x19, [sp, #0x10]
// 0x103675c: mov x1, xzr
// 0x1036760: ldp x30, x21, [sp], #0x20
// 0x1036764: b #0x1041d38
// 0x1036768: ldp x20, x19, [sp, #0x10]
// 0x103676c: ldp x30, x21, [sp], #0x20
// 0x1036770: ret
// 0x1036774: bl #0xf7db74
```

## `InputRig.GetButtonDown` — RVA `0xc36860`

- Decompiled symbol: `InputRig_GetButtonDown`
- Metadata signature: `public bool GetButtonDown(string axisName, ref int cachedId) { }`
- Native interval: `132` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x1036860: str x30, [sp, #-0x30]!
// 0x1036864: stp x22, x21, [sp, #0x10]
// 0x1036868: stp x20, x19, [sp, #0x20]
// 0x103686c: adrp x22, #0x1fab000
// 0x1036870: ldrb w8, [x22, #0x1b8]
// 0x1036874: mov x19, x2
// 0x1036878: mov x20, x1
// 0x103687c: mov x21, x0
// 0x1036880: tbnz w8, #0, #0x1036898
// 0x1036884: adrp x0, #0x1e8c000
// 0x1036888: ldr x0, [x0, #0x468]
// 0x103688c: bl #0xf7d92c
// 0x1036890: mov w8, #1
// 0x1036894: strb w8, [x22, #0x1b8]
// 0x1036898: ldr x0, [x21, #0x80]
// 0x103689c: cbz x0, #0x10368e0
// 0x10368a0: adrp x8, #0x1e8c000
// 0x10368a4: ldr x8, [x8, #0x468]
// 0x10368a8: mov x1, x20
// 0x10368ac: mov x2, x19
// 0x10368b0: ldr x3, [x8]
// 0x10368b4: bl #0x15264f8
// 0x10368b8: cbz x0, #0x10368d0
// 0x10368bc: ldp x20, x19, [sp, #0x20]
// 0x10368c0: ldp x22, x21, [sp, #0x10]
// 0x10368c4: mov x1, xzr
// 0x10368c8: ldr x30, [sp], #0x30
// 0x10368cc: b #0x1041d38
// 0x10368d0: ldp x20, x19, [sp, #0x20]
// 0x10368d4: ldp x22, x21, [sp, #0x10]
// 0x10368d8: ldr x30, [sp], #0x30
// 0x10368dc: ret
// 0x10368e0: bl #0xf7db74
```

## `InputRig.GetButtonUp` — RVA `0xc369b8`

- Decompiled symbol: `InputRig_GetButtonUp`
- Metadata signature: `public bool GetButtonUp(string axisName) { }`
- Native interval: `112` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x10369b8: stp x30, x21, [sp, #-0x20]!
// 0x10369bc: stp x20, x19, [sp, #0x10]
// 0x10369c0: adrp x21, #0x1fab000
// 0x10369c4: ldrb w8, [x21, #0x1b9]
// 0x10369c8: mov x19, x1
// 0x10369cc: mov x20, x0
// 0x10369d0: tbnz w8, #0, #0x10369e8
// 0x10369d4: adrp x0, #0x1e8c000
// 0x10369d8: ldr x0, [x0, #0x460]
// 0x10369dc: bl #0xf7d92c
// 0x10369e0: mov w8, #1
// 0x10369e4: strb w8, [x21, #0x1b9]
// 0x10369e8: ldr x0, [x20, #0x80]
// 0x10369ec: cbz x0, #0x1036a24
// 0x10369f0: adrp x8, #0x1e8c000
// 0x10369f4: ldr x8, [x8, #0x460]
// 0x10369f8: mov x1, x19
// 0x10369fc: ldr x2, [x8]
// 0x1036a00: bl #0x1526618
// 0x1036a04: cbz x0, #0x1036a18
// 0x1036a08: ldp x20, x19, [sp, #0x10]
// 0x1036a0c: mov x1, xzr
// 0x1036a10: ldp x30, x21, [sp], #0x20
// 0x1036a14: b #0x1041d58
// 0x1036a18: ldp x20, x19, [sp, #0x10]
// 0x1036a1c: ldp x30, x21, [sp], #0x20
// 0x1036a20: ret
// 0x1036a24: bl #0xf7db74
```

## `InputRig.GetButtonUp` — RVA `0xc36b10`

- Decompiled symbol: `InputRig_GetButtonUp`
- Metadata signature: `public bool GetButtonUp(string axisName, ref int cachedId) { }`
- Native interval: `132` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x1036b10: str x30, [sp, #-0x30]!
// 0x1036b14: stp x22, x21, [sp, #0x10]
// 0x1036b18: stp x20, x19, [sp, #0x20]
// 0x1036b1c: adrp x22, #0x1fab000
// 0x1036b20: ldrb w8, [x22, #0x1ba]
// 0x1036b24: mov x19, x2
// 0x1036b28: mov x20, x1
// 0x1036b2c: mov x21, x0
// 0x1036b30: tbnz w8, #0, #0x1036b48
// 0x1036b34: adrp x0, #0x1e8c000
// 0x1036b38: ldr x0, [x0, #0x468]
// 0x1036b3c: bl #0xf7d92c
// 0x1036b40: mov w8, #1
// 0x1036b44: strb w8, [x22, #0x1ba]
// 0x1036b48: ldr x0, [x21, #0x80]
// 0x1036b4c: cbz x0, #0x1036b90
// 0x1036b50: adrp x8, #0x1e8c000
// 0x1036b54: ldr x8, [x8, #0x468]
// 0x1036b58: mov x1, x20
// 0x1036b5c: mov x2, x19
// 0x1036b60: ldr x3, [x8]
// 0x1036b64: bl #0x15264f8
// 0x1036b68: cbz x0, #0x1036b80
// 0x1036b6c: ldp x20, x19, [sp, #0x20]
// 0x1036b70: ldp x22, x21, [sp, #0x10]
// 0x1036b74: mov x1, xzr
// 0x1036b78: ldr x30, [sp], #0x30
// 0x1036b7c: b #0x1041d58
// 0x1036b80: ldp x20, x19, [sp, #0x20]
// 0x1036b84: ldp x22, x21, [sp, #0x10]
// 0x1036b88: ldr x30, [sp], #0x30
// 0x1036b8c: ret
// 0x1036b90: bl #0xf7db74
```

## `InputRig.GetKey` — RVA `0xc36c68`

- Decompiled symbol: `InputRig_GetKey`
- Metadata signature: `public bool GetKey(KeyCode keyCode) { }`
- Native interval: `204` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed00;
extern char g_1fab1bb;

unsigned int InputRig_GetKey(long long *ptr, unsigned int a1)
{
    unsigned long v0;  // x19
    long long v1;  // x0

    v0 = a1;
    if (!(g_1fab1bb & 1))
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab1bb = 1;
    }
    if (!((char)(v0 >> 31) & 1))
    {
        v1 = ptr[19];
        if (!v1)
        {
            sub_f7db74(v1);
        }
        else if (*((int *)(v1 + 24)) > (unsigned int)v0)
        {
            if (((char)BitArray__Get() & 1))
                return 1;
            v1 = ptr[22];
            if (!v1)
            {
                sub_f7db74(v1);
            }
            else if (!((char)BitArray__get_Item(v1, v0 & 4294967295, 0) & 1))
            {
                if (!g_1eeed00->field_e0)
                    sub_f7da5c(g_1eeed00);
                if (6 < (unsigned int)v0 - 323 || !((char)CF2Input__IsInMobileMode() & 1))
                    return Input__GetKey();
            }
        }
    }
    return 0;
}
```

## `InputRig.GetKeyDown` — RVA `0xc36e08`

- Decompiled symbol: `InputRig_GetKeyDown`
- Metadata signature: `public bool GetKeyDown(KeyCode keyCode) { }`
- Native interval: `236` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed00;
extern char g_1fab1bc;

unsigned int InputRig_GetKeyDown(long long *a0, unsigned int a1)
{
    unsigned long v0;  // x19
    unsigned long long v1;  // x0

    v0 = a1;
    if (!(g_1fab1bc & 1))
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab1bc = 1;
    }
    if (((char)(v0 >> 31) & 1))
        return 0;
    if (a0[19])
    {
        if (*((int *)(a0[19] + 24)) <= (unsigned int)v0)
            return 0;
        if (a0[18])
        {
            if (((char)BitArray__Get(a0[18], v0 & 4294967295, 0) & 1))
            {
LABEL_1036e88:
                if (a0[22])
                {
                    if (!((char)BitArray__get_Item(a0[22], v0 & 4294967295, 0) & 1))
                    {
                        if (!g_1eeed00->field_e0)
                            sub_f7da5c(g_1eeed00);
                        v1 = CF2Input__IsInMobileMode();
                        if (6 < (unsigned int)v0 - 323 || !((char)v1 & 1))
                            return Input__GetKeyDown();
                        return 0;
                        return Input__GetKeyDown();
                    }
                    else
                    {
                        return 0;
                    }
                }
            }
            else if (a0[19])
            {
                if (((char)BitArray__Get(a0[19], v0 & 4294967295, 0) & 1))
                    return 1;
                goto LABEL_1036e88;
            }
        }
    }
    sub_f7db74();
}
```

## `InputRig.GetKeyUp` — RVA `0xc36fc8`

- Decompiled symbol: `InputRig_GetKeyUp`
- Metadata signature: `public bool GetKeyUp(KeyCode keyCode) { }`
- Native interval: `236` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed00;
extern char g_1fab1bd;

unsigned int InputRig_GetKeyUp(long long *a0, unsigned int a1)
{
    unsigned long v0;  // x19
    unsigned long long v1;  // x0

    v0 = a1;
    if (!(g_1fab1bd & 1))
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab1bd = 1;
    }
    if (((char)(v0 >> 31) & 1))
        return 0;
    if (a0[19])
    {
        if (*((int *)(a0[19] + 24)) <= (unsigned int)v0)
            return 0;
        if (a0[18])
        {
            if (!((char)BitArray__Get(a0[18], v0 & 4294967295, 0) & 1))
            {
LABEL_1037040:
                if (a0[22] && !((char)BitArray__get_Item(a0[22], v0 & 4294967295, 0) & 1))
                {
                    if (!g_1eeed00->field_e0)
                        sub_f7da5c(g_1eeed00);
                    v1 = CF2Input__IsInMobileMode();
                }
            }
            else if (a0[19])
            {
                if (!((char)BitArray__Get(a0[19], v0 & 4294967295, 0) & 1))
                    return 1;
                goto LABEL_1037040;
            }
        }
    }
    sub_f7db74();
}
```

## `InputRig.GetKey` — RVA `0xc37194`

- Decompiled symbol: `InputRig_GetKey`
- Metadata signature: `public bool GetKey(string keyName) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned int InputRig_GetKey(long long *a0, long long a1)
{
    return InputRig__GetKey(a0, InputRig__NameToKeyCode(a1));
}
```

## `InputRig.GetKeyDown` — RVA `0xc37294`

- Decompiled symbol: `InputRig_GetKeyDown`
- Metadata signature: `public bool GetKeyDown(string keyName) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned int InputRig_GetKeyDown(long long *a0, long long a1)
{
    return InputRig__GetKeyDown(a0, InputRig__NameToKeyCode(a1));
}
```

## `InputRig.GetKeyUp` — RVA `0xc37394`

- Decompiled symbol: `InputRig_GetKeyUp`
- Metadata signature: `public bool GetKeyUp(string keyName) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned int InputRig_GetKeyUp(long long *a0, long long a1)
{
    return InputRig__GetKeyUp(a0, InputRig__NameToKeyCode(a1));
}
```

## `InputRig.AnyKey` — RVA `0xc37488`

- Decompiled symbol: `InputRig_AnyKey`
- Metadata signature: `public bool AnyKey() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[186];
    char field_ba;
} struct_0;

unsigned int InputRig_AnyKey(struct_0 *a0)
{
    if (a0->field_ba)
        return 1;
}
```

## `InputRig.AnyKeyDown` — RVA `0xc37574`

- Decompiled symbol: `InputRig_AnyKeyDown`
- Metadata signature: `public bool AnyKeyDown() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[187];
    char field_bb;
} struct_0;

unsigned int InputRig_AnyKeyDown(struct_0 *a0)
{
    if (!a0->field_bb)
        return Input__get_anyKeyDown();
    return 1;
}
```

## `InputRig.GetEmuTouchCount` — RVA `0xc37654`

- Decompiled symbol: `InputRig_GetEmuTouchCount`
- Metadata signature: `public int GetEmuTouchCount() { }`
- Native interval: `72` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x1037654: str x30, [sp, #-0x20]!
// 0x1037658: stp x20, x19, [sp, #0x10]
// 0x103765c: adrp x20, #0x1fab000
// 0x1037660: ldrb w8, [x20, #0x1d8]
// 0x1037664: mov x19, x0
// 0x1037668: tbnz w8, #0, #0x1037680
// 0x103766c: adrp x0, #0x1e8c000
// 0x1037670: ldr x0, [x0, #0x470]
// 0x1037674: bl #0xf7d92c
// 0x1037678: mov w8, #1
// 0x103767c: strb w8, [x20, #0x1d8]
// 0x1037680: ldr x8, [x19, #0x168]
// 0x1037684: cbz x8, #0x1037698
// 0x1037688: ldr w0, [x8, #0x18]
// 0x103768c: ldp x20, x19, [sp, #0x10]
// 0x1037690: ldr x30, [sp], #0x20
// 0x1037694: ret
// 0x1037698: bl #0xf7db74
```

## `InputRig.GetEmuTouchArray` — RVA `0xc3779c`

- Decompiled symbol: `InputRig_GetEmuTouchArray`
- Metadata signature: `public InputRig.Touch[] GetEmuTouchArray() { }`
- Native interval: `364` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_Recovered` matched 3 offsets against `InputRig` metadata (confidence 1.00).

```c
typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct InputRig_Recovered {
    char padding_0[360];
    struct struct_0 *emuTouchesOrdered;
    struct struct_1 *emuOutputTouches;
    char emuOutputTouchesDirty;
} InputRig_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

typedef struct struct_4 {
    char padding_0[24];
    unsigned int field_18;
} struct_4;

extern long long g_1ef90f8;
extern long long g_1ef9100;
extern char g_1fab1d7;

struct_3 * InputRig_GetEmuTouchArray(struct_2 *ptr)
{
    struct_1 *v2;  // x8
    struct_2 *p;  // x20
    struct_0 *dst;  // x0, Other Possible Types: struct_4 *
    struct_3 *v5;  // x0
    unsigned long v6;  // x21
    unsigned long long v7;  // x23

    if (!(g_1fab1d7 & 1))
    {
        sub_f7d92c(&g_1ef90f8);
        sub_f7d92c(&g_1ef9100);
        sub_f7d92c("Y*");
        g_1fab1d7 = 1;
    }
    v2 = ptr->field_170;
    if (ptr->field_178)
    {
        p = &ptr->field_170;
        if (!v2)
            goto LABEL_1037824;
        dst = ptr->field_168;
        if (dst->field_18 == v2->field_18)
            goto LABEL_1037858;
LABEL_103782c:
        v5 = sub_f7d9d4(g_1eee528, dst->field_18);
        *((struct_3 **)&p->padding_0[0]) = v5;
        sub_f7d8d0(p, v5);
        dst = ptr->field_168;
LABEL_1037858:
        v6 = 0;
        v7 = 32;
    }
    else
    {
        if (v2)
            return v2;
        p = &ptr->field_170;
LABEL_1037824:
        dst = ptr->field_168;
        if (dst)
            goto LABEL_103782c;
    }
}
```

## `InputRig.GetEmuTouch` — RVA `0xc37a38`

- Decompiled symbol: `InputRig_GetEmuTouch`
- Metadata signature: `public InputRig.Touch GetEmuTouch(int i) { }`
- Native interval: `196` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[360];
    long long field_168;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef3368;
extern long long g_1ef90f8;
extern long long g_1ef9100;
extern char g_1fab1d9;

void InputRig_GetEmuTouch(struct_1 *ptr, unsigned int a1)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    unsigned long v10;  // x20
    long long v11;  // x0
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
    v10 = a1;
    if (!(g_1fab1d9 & 1))
    {
        sub_f7d92c(&g_1ef90f8);
        sub_f7d92c(&g_1ef9100);
        sub_f7d92c(&g_1ef3368);
        g_1fab1d9 = 1;
    }
    if (!((char)(v10 >> 31) & 1))
    {
        v11 = ptr->field_168;
        if (!v11)
        {
LABEL_1037af8:
            sub_f7db74(v11);
        }
        if (*((int *)(v11 + 24)) <= (unsigned int)v10)
            goto LABEL_1037ac0;
        v11 = sub_14a30c0();
        if (!v11)
            goto LABEL_1037af8;
    }
    else
    {
LABEL_1037ac0:
        if (!g_1ef3368->field_e0)
            sub_f7da5c(g_1ef3368);
    }
    memcpy();
    return;
}
```

## `InputRig.GetMouseButton` — RVA `0xc37be8`

- Decompiled symbol: `InputRig_GetMouseButton`
- Metadata signature: `public bool GetMouseButton(int mouseButton) { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
unsigned int InputRig_GetMouseButton(long long *a0, unsigned int a1)
{
    if (6 < a1)
        return 0;
    return InputRig__GetKey(a0, a1 + 323);
}
```

## `InputRig.GetMouseButtonDown` — RVA `0xc37cec`

- Decompiled symbol: `InputRig_GetMouseButtonDown`
- Metadata signature: `public bool GetMouseButtonDown(int mouseButton) { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
unsigned int InputRig_GetMouseButtonDown(long long *a0, unsigned int a1)
{
    if (6 < a1)
        return 0;
    return InputRig__GetKeyDown(a0, a1 + 323);
}
```

## `InputRig.GetMouseButtonUp` — RVA `0xc37df0`

- Decompiled symbol: `InputRig_GetMouseButtonUp`
- Metadata signature: `public bool GetMouseButtonUp(int mouseButton) { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
unsigned int InputRig_GetMouseButtonUp(long long *a0, unsigned int a1)
{
    if (6 < a1)
        return 0;
    return InputRig__GetKeyUp(a0, a1 + 323);
}
```

## `InputRig.CalibrateTilt` — RVA `0xc38274`

- Decompiled symbol: `InputRig_CalibrateTilt`
- Metadata signature: `public void CalibrateTilt() { }`
- Native interval: `36` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x1038274: str x30, [sp, #-0x10]!
// 0x1038278: ldr x8, [x0, #0x110]
// 0x103827c: cbz x8, #0x1038294
// 0x1038280: ldr x0, [x8, #0x18]
// 0x1038284: cbz x0, #0x1038294
// 0x1038288: mov x1, xzr
// 0x103828c: ldr x30, [sp], #0x10
// 0x1038290: b #0x1061838
// 0x1038294: bl #0xf7db74
```

## `InputRig.add_onSwitchesChanged` — RVA `0xc393cc`

- Decompiled symbol: `InputRig_add_onSwitchesChanged`
- Metadata signature: `public void add_onSwitchesChanged(Action value) { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

extern char g_1fab199;

long long InputRig_add_onSwitchesChanged(struct_0 *ptr, long long a1)
{
    long long v0;  // x21
    long long v1;  // x21
    long long v2;  // x8
    long long v3;  // x21

    if (!(g_1fab199 & 1))
    {
        sub_f7d92c("++");
        g_1fab199 = 1;
    }
    v0 = ptr->field_28;
    while (true)
    {
        v1 = v0;
        v2 = Delegate__Combine(v1, a1, 0);
        if (v2 && *((long long *)v2) != g_1eee648)
            sub_f7df10(v2);
        v3 = sub_f60ebc(&ptr->field_28, v2, v1);
        v0 = v3;
        if (v1 == v0)
            return v3;
    }
}
```

## `InputRig.remove_onSwitchesChanged` — RVA `0xc39468`

- Decompiled symbol: `InputRig_remove_onSwitchesChanged`
- Metadata signature: `public void remove_onSwitchesChanged(Action value) { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

extern char g_1fab19a;

long long InputRig_remove_onSwitchesChanged(struct_0 *ptr, long long a1)
{
    long long v0;  // x21
    long long v1;  // x21
    long long v2;  // x8
    long long v3;  // x21

    if (!(g_1fab19a & 1))
    {
        sub_f7d92c("++");
        g_1fab19a = 1;
    }
    v0 = ptr->field_28;
    while (true)
    {
        v1 = v0;
        v2 = Delegate__Remove(v1, a1, 0);
        if (v2 && *((long long *)v2) != g_1eee648)
            sub_f7df10(v2);
        v3 = sub_f60ebc(&ptr->field_28, v2, v1);
        v0 = v3;
        if (v1 == v0)
            return v3;
    }
}
```

## `InputRig.add_onAddExtraInput` — RVA `0xc39504`

- Decompiled symbol: `InputRig_add_onAddExtraInput`
- Metadata signature: `public void add_onAddExtraInput(Action value) { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    long long field_30;
} struct_0;

extern char g_1fab19b;

long long InputRig_add_onAddExtraInput(struct_0 *ptr, long long a1)
{
    long long v0;  // x21
    long long v1;  // x21
    long long v2;  // x8
    long long v3;  // x21

    if (!(g_1fab19b & 1))
    {
        sub_f7d92c("++");
        g_1fab19b = 1;
    }
    v0 = ptr->field_30;
    while (true)
    {
        v1 = v0;
        v2 = Delegate__Combine(v1, a1, 0);
        if (v2 && *((long long *)v2) != g_1eee648)
            sub_f7df10(v2);
        v3 = sub_f60ebc(&ptr->field_30, v2, v1);
        v0 = v3;
        if (v1 == v0)
            return v3;
    }
}
```

## `InputRig.remove_onAddExtraInput` — RVA `0xc395a0`

- Decompiled symbol: `InputRig_remove_onAddExtraInput`
- Metadata signature: `public void remove_onAddExtraInput(Action value) { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    long long field_30;
} struct_0;

extern char g_1fab19c;

long long InputRig_remove_onAddExtraInput(struct_0 *ptr, long long a1)
{
    long long v0;  // x21
    long long v1;  // x21
    long long v2;  // x8
    long long v3;  // x21

    if (!(g_1fab19c & 1))
    {
        sub_f7d92c("++");
        g_1fab19c = 1;
    }
    v0 = ptr->field_30;
    while (true)
    {
        v1 = v0;
        v2 = Delegate__Remove(v1, a1, 0);
        if (v2 && *((long long *)v2) != g_1eee648)
            sub_f7df10(v2);
        v3 = sub_f60ebc(&ptr->field_30, v2, v1);
        v0 = v3;
        if (v1 == v0)
            return v3;
    }
}
```

## `InputRig.add_onAddExtraInputToActiveRig` — RVA `0xc3963c`

- Decompiled symbol: `InputRig_add_onAddExtraInputToActiveRig`
- Metadata signature: `public static void add_onAddExtraInputToActiveRig(Action value) { }`
- Native interval: `184` bytes
- Result: `pseudocode`

```c
extern char g_1fab19d;

long long InputRig_add_onAddExtraInputToActiveRig(long long a0)
{
    long long v0;  // x20
    long long v1;  // x20
    long long v2;  // x8
    long long v3;  // x20

    if (!(g_1fab19d & 1))
    {
        sub_f7d92c("++");
        sub_f7d92c("SB");
        g_1fab19d = 1;
    }
    v0 = g_1ef0428->field_b8->field_0;
    while (true)
    {
        v1 = v0;
        v2 = Delegate__Combine(v1, a0, 0);
        if (v2 && *((long long *)v2) != g_1eee648)
            sub_f7df10(v2);
        v3 = sub_f60ebc(g_1ef0428->field_b8, v2, v1);
        v0 = v3;
        if (v1 == v0)
            return v3;
    }
}
```

## `InputRig.remove_onAddExtraInputToActiveRig` — RVA `0xc396f4`

- Decompiled symbol: `InputRig_remove_onAddExtraInputToActiveRig`
- Metadata signature: `public static void remove_onAddExtraInputToActiveRig(Action value) { }`
- Native interval: `184` bytes
- Result: `pseudocode`

```c
extern char g_1fab19e;

long long InputRig_remove_onAddExtraInputToActiveRig(long long a0)
{
    long long v0;  // x20
    long long v1;  // x20
    long long v2;  // x8
    long long v3;  // x20

    if (!(g_1fab19e & 1))
    {
        sub_f7d92c("++");
        sub_f7d92c("SB");
        g_1fab19e = 1;
    }
    v0 = g_1ef0428->field_b8->field_0;
    while (true)
    {
        v1 = v0;
        v2 = Delegate__Remove(v1, a0, 0);
        if (v2 && *((long long *)v2) != g_1eee648)
            sub_f7df10(v2);
        v3 = sub_f60ebc(g_1ef0428->field_b8, v2, v1);
        v0 = v3;
        if (v1 == v0)
            return v3;
    }
}
```

## `InputRig.ShowOrHideTouchControls` — RVA `0xc397ac`

- Decompiled symbol: `InputRig_ShowOrHideTouchControls`
- Metadata signature: `public void ShowOrHideTouchControls(bool show, bool skipAnim) { }`
- Native interval: `324` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_Recovered` matched 3 offsets against `InputRig` metadata (confidence 1.00).

```c
typedef struct InputRig_Recovered {
    char padding_0[112];
    unsigned int elapsedSinceLastTouch;
    char touchControlsSleeping;
    char padding_75[187];
    char touchControlsHidden;
} InputRig_Recovered;

typedef struct struct_2 {
    char padding_0[136];
    unsigned int field_88;
} struct_2;

typedef struct struct_4 {
    struct struct_2 *field_0;
} struct_4;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_3 {
    char padding_0[184];
    struct struct_4 *field_b8;
} struct_3;

extern struct_3 *g_1eefb00;
extern struct_0 *g_1ef0c58;
extern char g_1fab1ab;
extern char g_1fab1dd;

struct_1 * InputRig_ShowOrHideTouchControls(struct_1 *ptr, unsigned int a1, unsigned int a2)
{
    unsigned long v0;  // x20
    struct_1 *v1;  // x0
    struct_1 *v2;  // x0
    struct_1 *v3;  // x0
    unsigned long v4;  // x22
    struct_1 *v5;  // x0
    unsigned long long v6;  // x0

    v0 = a1;
    v1 = ptr;
    if (!(g_1fab1ab & 1))
    {
        v2 = sub_f7d92c(&g_1ef0c58);
        g_1fab1ab = 1;
        v1 = v2;
    }
    v3 = v1;
    v4 = ~((unsigned int)v0) & 1;
    if (ptr->field_130 == (unsigned int)v4)
        return v3;
    ptr->field_130 = v4;
    InputRig__SyncDisablingConditions(ptr, a2 & 1);
    if (!g_1fab1dd)
    {
        sub_f7d92c(&g_1eefb00);
        g_1fab1dd = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v5 = Object__op_Equality(g_1eefb00->field_b8->field_0, 0, 0);
    if (!((char)v5 & 1))
    {
        if (!g_1fab1dd)
        {
            v5 = sub_f7d92c(&g_1eefb00);
            g_1fab1dd = 1;
        }
        if (!g_1eefb00->field_b8->field_0)
            sub_f7db74();
        if (g_1eefb00->field_b8->field_0->field_88)
            return v5;
        if (((char)v4 & 1))
            return v5;
    }
    else if (!((char)v0 & 1))
    {
        return v5;
    }
    if (ptr->field_74)
    {
        ptr->field_70 = 0;
        ptr->field_74 = 0;
        v6 = InputRig__SyncDisablingConditions();
        return InputRig__SyncDisablingConditions();
    }
    return v5;
}
```

## `InputRig.ctor` — RVA `0xc398f0`

- Decompiled symbol: `InputRig_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `92` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_Recovered` matched 8 offsets against `InputRig` metadata (confidence 1.00).

```c
typedef struct InputRig_Recovered {
    char padding_0[56];
    unsigned short autoActivate;
    char hideWhenDisactivated;
    char padding_3b[1];
    char hideWhenTouchScreenIsUnused;
    char padding_3d[7];
    char hideWhenGamepadIsActivated;
    char padding_45[7];
    unsigned int fingerRadiusInCm;
    char padding_50[4];
    uint128_t controlBaseAlphaAnimDuration;
    unsigned long long ninetyDegTurnAnalogDuration;
    unsigned int scrollStepsPerNinetyDegTurn;
} InputRig_Recovered;

long long InputRig_ctor(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    ptr->field_38 = 257;
    ptr->field_3a = 1;
    ptr->field_3c = 1;
    ptr->field_44 = 1;
    *((uint128_t *)&(&ptr->padding_50)[1]) = 0x4080000043fa00003e4ccccd3f000000;
    ptr->field_4c = 0x3e800000;
    *((unsigned long long *)((char *)&ptr->field_54 + 4)) = 0x408000003f400000;
    *((unsigned int *)((char *)&ptr->field_54 + 12)) = 10;
    ComponentBase__ctor(); /* do not return */
}
```

## `InputRig.BasicConstructor` — RVA `0xc3994c`

- Decompiled symbol: `InputRig_BasicConstructor`
- Metadata signature: `private void BasicConstructor() { }`
- Native interval: `4000` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x103994c: str d8, [sp, #-0x70]!
// 0x1039950: stp x29, x30, [sp, #0x10]
// 0x1039954: stp x28, x27, [sp, #0x20]
// 0x1039958: stp x26, x25, [sp, #0x30]
// 0x103995c: stp x24, x23, [sp, #0x40]
// 0x1039960: stp x22, x21, [sp, #0x50]
// 0x1039964: stp x20, x19, [sp, #0x60]
// 0x1039968: adrp x25, #0x1fab000
// 0x103996c: adrp x20, #0x1e8c000
// 0x1039970: adrp x26, #0x1e8c000
// 0x1039974: adrp x24, #0x1e8c000
// 0x1039978: adrp x23, #0x1e8c000
// 0x103997c: adrp x21, #0x1e8c000
// 0x1039980: adrp x22, #0x1e8c000
// 0x1039984: ldr x20, [x20, #0x4a0]
// 0x1039988: ldrb w8, [x25, #0x19f]
// 0x103998c: ldr x26, [x26, #0x4a8]
// 0x1039990: ldr x24, [x24, #0x4b0]
// 0x1039994: ldr x23, [x23, #0x4b8]
// 0x1039998: ldr x21, [x21, #0x4c0]
// 0x103999c: ldr x22, [x22, #0x3d0]
// 0x10399a0: mov x19, x0
// 0x10399a4: tbnz w8, #0, #0x1039b24
// 0x10399a8: adrp x0, #0x1e8c000
// 0x10399ac: ldr x0, [x0, #0x68]
// 0x10399b0: bl #0xf7d92c
// 0x10399b4: adrp x0, #0x1e8c000
// 0x10399b8: ldr x0, [x0, #0x4c8]
// 0x10399bc: bl #0xf7d92c
// 0x10399c0: adrp x0, #0x1e8c000
// 0x10399c4: ldr x0, [x0, #0x4d0]
// 0x10399c8: bl #0xf7d92c
// 0x10399cc: adrp x0, #0x1e8c000
// 0x10399d0: ldr x0, [x0, #0x4d8]
// 0x10399d4: bl #0xf7d92c
// 0x10399d8: adrp x0, #0x1e8c000
// 0x10399dc: ldr x0, [x0, #0x4a0]
// 0x10399e0: bl #0xf7d92c
// 0x10399e4: adrp x0, #0x1e8c000
// 0x10399e8: ldr x0, [x0, #0x4e0]
// 0x10399ec: bl #0xf7d92c
// 0x10399f0: adrp x0, #0x1e8c000
// 0x10399f4: ldr x0, [x0, #0x4e8]
// 0x10399f8: bl #0xf7d92c
// 0x10399fc: adrp x0, #0x1e8c000
// 0x1039a00: ldr x0, [x0, #0x60]
// 0x1039a04: bl #0xf7d92c
// 0x1039a08: adrp x0, #0x1e8c000
// 0x1039a0c: ldr x0, [x0, #0x4c0]
// 0x1039a10: bl #0xf7d92c
// 0x1039a14: adrp x0, #0x1e8c000
// 0x1039a18: ldr x0, [x0, #0x4f0]
// 0x1039a1c: bl #0xf7d92c
// 0x1039a20: adrp x0, #0x1e8c000
// 0x1039a24: ldr x0, [x0, #0x4f8]
// 0x1039a28: bl #0xf7d92c
// 0x1039a2c: adrp x0, #0x1e8c000
// 0x1039a30: ldr x0, [x0, #0x500]
// 0x1039a34: bl #0xf7d92c
// 0x1039a38: adrp x0, #0x1e8c000
// 0x1039a3c: ldr x0, [x0, #0x4b8]
// 0x1039a40: bl #0xf7d92c
// 0x1039a44: adrp x0, #0x1e8c000
// 0x1039a48: ldr x0, [x0, #0x4b0]
// 0x1039a4c: bl #0xf7d92c
// 0x1039a50: adrp x0, #0x1e8c000
// 0x1039a54: ldr x0, [x0, #0x508]
// 0x1039a58: bl #0xf7d92c
// 0x1039a5c: adrp x0, #0x1e8c000
// 0x1039a60: ldr x0, [x0, #0x510]
// 0x1039a64: bl #0xf7d92c
// 0x1039a68: adrp x0, #0x1e8c000
// 0x1039a6c: ldr x0, [x0, #0x4a8]
// 0x1039a70: bl #0xf7d92c
// 0x1039a74: adrp x0, #0x1e8c000
// 0x1039a78: ldr x0, [x0, #0x518]
// 0x1039a7c: bl #0xf7d92c
// 0x1039a80: adrp x0, #0x1e8c000
// 0x1039a84: ldr x0, [x0, #0x520]
// 0x1039a88: bl #0xf7d92c
// 0x1039a8c: adrp x0, #0x1e8c000
// 0x1039a90: ldr x0, [x0, #0x3d0]
// 0x1039a94: bl #0xf7d92c
// 0x1039a98: adrp x0, #0x1e8c000
// 0x1039a9c: ldr x0, [x0, #0x528]
// 0x1039aa0: bl #0xf7d92c
// 0x1039aa4: adrp x0, #0x1e8c000
// 0x1039aa8: ldr x0, [x0, #0x530]
// 0x1039aac: bl #0xf7d92c
// 0x1039ab0: adrp x0, #0x1e8c000
// 0x1039ab4: ldr x0, [x0, #0x538]
// 0x1039ab8: bl #0xf7d92c
// 0x1039abc: adrp x0, #0x1e8c000
// 0x1039ac0: ldr x0, [x0, #0x540]
// 0x1039ac4: bl #0xf7d92c
// 0x1039ac8: adrp x0, #0x1e8c000
// 0x1039acc: ldr x0, [x0, #0x548]
// 0x1039ad0: bl #0xf7d92c
// 0x1039ad4: adrp x0, #0x1e8c000
// 0x1039ad8: ldr x0, [x0, #0x550]
// 0x1039adc: bl #0xf7d92c
// 0x1039ae0: adrp x0, #0x1e8c000
// 0x1039ae4: ldr x0, [x0, #0x558]
// 0x1039ae8: bl #0xf7d92c
// 0x1039aec: adrp x0, #0x1e8c000
// 0x1039af0: ldr x0, [x0, #0x560]
// 0x1039af4: bl #0xf7d92c
// 0x1039af8: adrp x0, #0x1e8c000
// 0x1039afc: ldr x0, [x0, #0x568]
// 0x1039b00: bl #0xf7d92c
// 0x1039b04: adrp x0, #0x1e8c000
// 0x1039b08: ldr x0, [x0, #0x570]
// 0x1039b0c: bl #0xf7d92c
// 0x1039b10: adrp x0, #0x1e8c000
// 0x1039b14: ldr x0, [x0, #0x578]
// 0x1039b18: bl #0xf7d92c
// 0x1039b1c: mov w8, #1
// 0x1039b20: strb w8, [x25, #0x19f]
// 0x1039b24: ldr x0, [x20]
// 0x1039b28: adrp x28, #0x1e8c000
// 0x1039b2c: adrp x27, #0x1e8c000
// 0x1039b30: adrp x25, #0x1e8c000
// 0x1039b34: ldr x28, [x28, #0x4d8]
// 0x1039b38: ldr x27, [x27, #0x528]
// 0x1039b3c: ldr x25, [x25, #0x4d0]
// 0x1039b40: bl #0xf7db70
// 0x1039b44: mov w1, #0x78
// 0x1039b48: mov x2, xzr
// 0x1039b4c: mov x20, x0
// 0x1039b50: bl #0x105b188
// 0x1039b54: add x0, x19, #0x128
// 0x1039b58: mov x1, x20
// 0x1039b5c: str x20, [x19, #0x128]
// 0x1039b60: bl #0xf7d8d0
// 0x1039b64: adrp x8, #0x832000
// 0x1039b68: ldr q0, [x8, #0xee0]
// 0x1039b6c: mov w9, #1
// 0x1039b70: mov w10, #0x41200000
// 0x1039b74: mov w11, #0x40a00000
// 0x1039b78: strb w9, [x19, #0x3a]
// 0x1039b7c: strb w9, [x19, #0x3c]
// 0x1039b80: str w10, [x19, #0x40]
// 0x1039b84: strb w9, [x19, #0x44]
// 0x1039b88: stur q0, [x19, #0x5c]
// 0x1039b8c: str w11, [x19, #0x48]
// 0x1039b90: ldr x0, [x26]
// 0x1039b94: bl #0xf7db70
// 0x1039b98: mov x1, x19
// 0x1039b9c: mov x2, xzr
// 0x1039ba0: mov x20, x0
// 0x1039ba4: bl #0x103efbc
// 0x1039ba8: mov x0, x19
// 0x1039bac: str x20, [x0, #0xf8]!
// 0x1039bb0: mov x1, x20
// 0x1039bb4: bl #0xf7d8d0
// 0x1039bb8: mov x0, x19
// 0x1039bbc: bl #0x103a8ec
// 0x1039bc0: ldr x0, [x24]
// 0x1039bc4: bl #0xf7db70
// 0x1039bc8: ldr x2, [x23]
// 0x1039bcc: mov w1, #0x20
// 0x1039bd0: mov x20, x0
// 0x1039bd4: bl #0x14a2bd4
// 0x1039bd8: add x0, x19, #0x108
// 0x1039bdc: mov x1, x20
// 0x1039be0: str x20, [x19, #0x108]
// 0x1039be4: bl #0xf7d8d0
// 0x1039be8: ldr x0, [x22]
// 0x1039bec: ldr x20, [x21]
// 0x1039bf0: ldr w8, [x0, #0xe0]
// 0x1039bf4: cbnz w8, #0x1039bfc
// 0x1039bf8: bl #0xf7da5c
// 0x1039bfc: mov x0, x20
// 0x1039c00: mov x1, xzr
// 0x1039c04: bl #0x1956240
// 0x1039c08: mov x1, xzr
// 0x1039c0c: bl #0x1059f08
// 0x1039c10: ldr x8, [x28]
// 0x1039c14: add w20, w0, #1
// 0x1039c18: mov x0, x8
// 0x1039c1c: bl #0xf7db70
// 0x1039c20: mov w1, w20
// 0x1039c24: mov x2, xzr
// 0x1039c28: mov x21, x0
// 0x1039c2c: bl #0x1921ecc
// 0x1039c30: mov x0, x19
// 0x1039c34: str x21, [x0, #0x98]!
// 0x1039c38: mov x1, x21
// 0x1039c3c: bl #0xf7d8d0
// 0x1039c40: ldr x0, [x28]
// 0x1039c44: bl #0xf7db70
// 0x1039c48: mov w1, w20
// 0x1039c4c: mov x2, xzr
// 0x1039c50: mov x21, x0
// 0x1039c54: bl #0x1921ecc
// 0x1039c58: mov x0, x19
// 0x1039c5c: str x21, [x0, #0x90]!
// 0x1039c60: mov x1, x21
// 0x1039c64: bl #0xf7d8d0
// 0x1039c68: ldr x0, [x28]
// 0x1039c6c: bl #0xf7db70
// 0x1039c70: mov w1, w20
// 0x1039c74: mov x2, xzr
// 0x1039c78: mov x21, x0
// 0x1039c7c: bl #0x1921ecc
// 0x1039c80: mov x0, x19
// 0x1039c84: str x21, [x0, #0xa0]!
// 0x1039c88: mov x1, x21
// 0x1039c8c: bl #0xf7d8d0
// 0x1039c90: ldr x0, [x28]
// 0x1039c94: bl #0xf7db70
// 0x1039c98: mov w1, w20
// 0x1039c9c: mov x2, xzr
// 0x1039ca0: mov x21, x0
// 0x1039ca4: bl #0x1921ecc
// 0x1039ca8: mov x0, x19
// 0x1039cac: str x21, [x0, #0xb0]!
// 0x1039cb0: mov x1, x21
// 0x1039cb4: bl #0xf7d8d0
// 0x1039cb8: ldr x0, [x28]
// 0x1039cbc: bl #0xf7db70
// 0x1039cc0: mov w1, w20
// 0x1039cc4: mov x2, xzr
// 0x1039cc8: mov x21, x0
// 0x1039ccc: bl #0x1921ecc
// 0x1039cd0: mov x0, x19
// 0x1039cd4: str x21, [x0, #0xa8]!
// 0x1039cd8: mov x1, x21
// 0x1039cdc: bl #0xf7d8d0
// 0x1039ce0: ldr x0, [x27]
// 0x1039ce4: bl #0xf7db70
// 0x1039ce8: mov w2, #1
// 0x1039cec: mov x1, x19
// 0x1039cf0: mov x3, xzr
// 0x1039cf4: mov x20, x0
// 0x1039cf8: bl #0x1040a54
// 0x1039cfc: mov x0, x19
// 0x1039d00: str x20, [x0, #0x78]!
// 0x1039d04: mov x1, x20
// 0x1039d08: bl #0xf7d8d0
// 0x1039d0c: ldr x0, [x25]
// 0x1039d10: bl #0xf7db70
// 0x1039d14: mov w2, #0x10
// 0x1039d18: mov x1, x19
// 0x1039d1c: mov x3, xzr
// 0x1039d20: mov x21, x0
// 0x1039d24: bl #0x1041ec0
// 0x1039d28: mov x20, x19
// 0x1039d2c: str x21, [x20, #0x80]!
// 0x1039d30: mov x0, x20
// 0x1039d34: mov x1, x21
// 0x1039d38: bl #0xf7d8d0
// 0x1039d3c: ldr x8, [x20]
// 0x1039d40: cbz x8, #0x103a474
// 0x1039d44: ldr x9, [x8, #0x10]
// 0x1039d48: cbz x9, #0x103a474
// 0x1039d4c: ldp w2, w10, [x9, #0x18]
// 0x1039d50: add w10, w10, #1
// 0x1039d54: cmp w2, #1
// 0x1039d58: stp wzr, w10, [x9, #0x18]
// 0x1039d5c: b.lt #0x1039d78
// 0x1039d60: ldr x0, [x9, #0x10]
// 0x1039d64: mov w1, wzr
// 0x1039d68: mov x3, xzr
// 0x1039d6c: bl #0x1968880
// 0x1039d70: ldr x8, [x20]
// 0x1039d74: cbz x8, #0x103a474
// 0x1039d78: adrp x29, #0x1e8c000
// 0x1039d7c: ldr x29, [x29, #0x548]
// 0x1039d80: ldr x21, [x8, #0x10]
// 0x1039d84: mov w1, #0x64
// 0x1039d88: mov w2, #0x61
// 0x1039d8c: ldr x0, [x29]
// 0x1039d90: mov x3, xzr
// 0x1039d94: bl #0x1040ee8
// 0x1039d98: cbz x21, #0x103a474
// 0x1039d9c: adrp x22, #0x1e8c000
// 0x1039da0: ldr x22, [x22, #0x4f0]
// 0x1039da4: ldr w10, [x21, #0x1c]
// 0x1039da8: ldr x8, [x21, #0x10]
// 0x1039dac: ldr x9, [x22]
// 0x1039db0: add w10, w10, #1
// 0x1039db4: str w10, [x21, #0x1c]
// 0x1039db8: cbz x8, #0x103a474
// 0x1039dbc: ldrsw x10, [x21, #0x18]
// 0x1039dc0: ldr w11, [x8, #0x18]
// 0x1039dc4: mov x1, x0
// 0x1039dc8: cmp w10, w11
// 0x1039dcc: b.hs #0x1039de8
// 0x1039dd0: add w9, w10, #1
// 0x1039dd4: add x0, x8, x10, lsl #3
// 0x1039dd8: str w9, [x21, #0x18]
// 0x1039ddc: str x1, [x0, #0x20]!
// 0x1039de0: bl #0xf7d8d0
// 0x1039de4: b #0x1039dfc
// 0x1039de8: ldr x8, [x9, #0x20]
// 0x1039dec: mov x0, x21
// 0x1039df0: ldr x8, [x8, #0xc0]
// 0x1039df4: ldr x2, [x8, #0x70]
// 0x1039df8: bl #0x14a3390
// 0x1039dfc: ldr x8, [x20]
// 0x1039e00: cbz x8, #0x103a474
// 0x1039e04: adrp x25, #0x1e8c000
// 0x1039e08: ldr x25, [x25, #0x538]
// 0x1039e0c: ldr x21, [x8, #0x10]
// 0x1039e10: mov w1, #0x77
// 0x1039e14: mov w2, #0x73
// 0x1039e18: ldr x0, [x25]
// 0x1039e1c: mov x3, xzr
// 0x1039e20: bl #0x1040ee8
// 0x1039e24: cbz x21, #0x103a474
// 0x1039e28: ldr w10, [x21, #0x1c]
// 0x1039e2c: ldr x8, [x21, #0x10]
// 0x1039e30: ldr x9, [x22]
// 0x1039e34: add w10, w10, #1
// 0x1039e38: str w10, [x21, #0x1c]
// 0x1039e3c: cbz x8, #0x103a474
// 0x1039e40: ldrsw x10, [x21, #0x18]
// 0x1039e44: ldr w11, [x8, #0x18]
// 0x1039e48: mov x1, x0
// 0x1039e4c: cmp w10, w11
// 0x1039e50: b.hs #0x1039e6c
// 0x1039e54: add w9, w10, #1
// 0x1039e58: add x0, x8, x10, lsl #3
// 0x1039e5c: str w9, [x21, #0x18]
// 0x1039e60: str x1, [x0, #0x20]!
// 0x1039e64: bl #0xf7d8d0
// 0x1039e68: b #0x1039e80
// 0x1039e6c: ldr x8, [x9, #0x20]
// 0x1039e70: mov x0, x21
// 0x1039e74: ldr x8, [x8, #0xc0]
// 0x1039e78: ldr x2, [x8, #0x70]
// 0x1039e7c: bl #0x14a3390
// 0x1039e80: ldr x8, [x20]
// 0x1039e84: cbz x8, #0x103a474
// 0x1039e88: adrp x9, #0x1e8c000
// 0x1039e8c: ldr x9, [x9, #0x550]
// 0x1039e90: ldr x21, [x8, #0x10]
// 0x1039e94: mov w1, wzr
// 0x1039e98: mov w2, wzr
// 0x1039e9c: ldr x0, [x9]
// 0x1039ea0: mov x3, xzr
// 0x1039ea4: bl #0x1040f74
// 0x1039ea8: cbz x21, #0x103a474
// 0x1039eac: ldr w10, [x21, #0x1c]
// 0x1039eb0: ldr x8, [x21, #0x10]
// 0x1039eb4: ldr x9, [x22]
// 0x1039eb8: add w10, w10, #1
// 0x1039ebc: str w10, [x21, #0x1c]
// 0x1039ec0: cbz x8, #0x103a474
// 0x1039ec4: ldrsw x10, [x21, #0x18]
// 0x1039ec8: ldr w11, [x8, #0x18]
// 0x1039ecc: mov x1, x0
// 0x1039ed0: cmp w10, w11
// 0x1039ed4: b.hs #0x1039ef0
// 0x1039ed8: add w9, w10, #1
// 0x1039edc: add x0, x8, x10, lsl #3
// 0x1039ee0: str w9, [x21, #0x18]
// 0x1039ee4: str x1, [x0, #0x20]!
// 0x1039ee8: bl #0xf7d8d0
// 0x1039eec: b #0x1039f04
// 0x1039ef0: ldr x8, [x9, #0x20]
// 0x1039ef4: mov x0, x21
// 0x1039ef8: ldr x8, [x8, #0xc0]
// 0x1039efc: ldr x2, [x8, #0x70]
// 0x1039f00: bl #0x14a3390
// 0x1039f04: ldr x8, [x20]
// 0x1039f08: cbz x8, #0x103a474
// 0x1039f0c: adrp x9, #0x1e8c000
// 0x1039f10: ldr x9, [x9, #0x530]
// 0x1039f14: ldr x21, [x8, #0x10]
// 0x1039f18: mov w1, wzr
// 0x1039f1c: mov w2, wzr
// 0x1039f20: ldr x0, [x9]
// 0x1039f24: mov x3, xzr
// 0x1039f28: bl #0x1040f74
// 0x1039f2c: cbz x21, #0x103a474
// 0x1039f30: ldr w10, [x21, #0x1c]
// 0x1039f34: ldr x8, [x21, #0x10]
// 0x1039f38: ldr x9, [x22]
// 0x1039f3c: add w10, w10, #1
// 0x1039f40: str w10, [x21, #0x1c]
// 0x1039f44: cbz x8, #0x103a474
// 0x1039f48: ldrsw x10, [x21, #0x18]
// 0x1039f4c: ldr w11, [x8, #0x18]
// 0x1039f50: mov x1, x0
// 0x1039f54: cmp w10, w11
// 0x1039f58: b.hs #0x1039f74
// 0x1039f5c: add w9, w10, #1
// 0x1039f60: add x0, x8, x10, lsl #3
// 0x1039f64: str w9, [x21, #0x18]
// 0x1039f68: str x1, [x0, #0x20]!
// 0x1039f6c: bl #0xf7d8d0
// 0x1039f70: b #0x1039f88
// 0x1039f74: ldr x8, [x9, #0x20]
// 0x1039f78: mov x0, x21
// 0x1039f7c: ldr x8, [x8, #0xc0]
// 0x1039f80: ldr x2, [x8, #0x70]
// 0x1039f84: bl #0x14a3390
// 0x1039f88: ldr x8, [x20]
// 0x1039f8c: cbz x8, #0x103a474
// 0x1039f90: adrp x9, #0x1e8c000
// 0x1039f94: ldr x9, [x9, #0x578]
// 0x1039f98: ldr x21, [x8, #0x10]
// 0x1039f9c: mov w1, wzr
// 0x1039fa0: mov w2, wzr
// 0x1039fa4: ldr x0, [x9]
// 0x1039fa8: mov x3, xzr
// 0x1039fac: bl #0x1040dd8
// 0x1039fb0: cbz x21, #0x103a474
// 0x1039fb4: ldr w10, [x21, #0x1c]
// 0x1039fb8: ldr x8, [x21, #0x10]
// 0x1039fbc: ldr x9, [x22]
// 0x1039fc0: add w10, w10, #1
// 0x1039fc4: str w10, [x21, #0x1c]
// 0x1039fc8: cbz x8, #0x103a474
// 0x1039fcc: ldrsw x10, [x21, #0x18]
// 0x1039fd0: ldr w11, [x8, #0x18]
// 0x1039fd4: mov x1, x0
// 0x1039fd8: cmp w10, w11
// 0x1039fdc: b.hs #0x1039ff8
// 0x1039fe0: add w9, w10, #1
// 0x1039fe4: add x0, x8, x10, lsl #3
// 0x1039fe8: str w9, [x21, #0x18]
// 0x1039fec: str x1, [x0, #0x20]!
// 0x1039ff0: bl #0xf7d8d0
// 0x1039ff4: b #0x103a00c
// 0x1039ff8: ldr x8, [x9, #0x20]
// 0x1039ffc: mov x0, x21
// 0x103a000: ldr x8, [x8, #0xc0]
// 0x103a004: ldr x2, [x8, #0x70]
// 0x103a008: bl #0x14a3390
// 0x103a00c: ldr x8, [x20]
// 0x103a010: cbz x8, #0x103a474
// 0x103a014: adrp x9, #0x1e8c000
// 0x103a018: ldr x9, [x9, #0x568]
// 0x103a01c: ldr x21, [x8, #0x10]
// 0x103a020: mov w1, wzr
// 0x103a024: mov w2, wzr
// 0x103a028: ldr x0, [x9]
// 0x103a02c: mov x3, xzr
// 0x103a030: bl #0x1040dd8
// 0x103a034: cbz x21, #0x103a474
// 0x103a038: ldr w10, [x21, #0x1c]
// 0x103a03c: ldr x8, [x21, #0x10]
// 0x103a040: ldr x9, [x22]
// 0x103a044: add w10, w10, #1
// 0x103a048: str w10, [x21, #0x1c]
// 0x103a04c: cbz x8, #0x103a474
// 0x103a050: ldrsw x10, [x21, #0x18]
// 0x103a054: ldr w11, [x8, #0x18]
// 0x103a058: mov x1, x0
// 0x103a05c: cmp w10, w11
// 0x103a060: b.hs #0x103a07c
// 0x103a064: add w9, w10, #1
// 0x103a068: add x0, x8, x10, lsl #3
// 0x103a06c: str w9, [x21, #0x18]
// 0x103a070: str x1, [x0, #0x20]!
// 0x103a074: bl #0xf7d8d0
// 0x103a078: b #0x103a090
// 0x103a07c: ldr x8, [x9, #0x20]
// 0x103a080: mov x0, x21
// 0x103a084: ldr x8, [x8, #0xc0]
// 0x103a088: ldr x2, [x8, #0x70]
// 0x103a08c: bl #0x14a3390
// 0x103a090: ldr x8, [x20]
// 0x103a094: cbz x8, #0x103a474
// 0x103a098: adrp x26, #0x1e8c000
// 0x103a09c: ldr x26, [x26, #0x570]
// 0x103a0a0: ldr x21, [x8, #0x10]
// 0x103a0a4: mov w1, #0x130
// 0x103a0a8: mov x2, xzr
// 0x103a0ac: ldr x0, [x26]
// 0x103a0b0: bl #0x1040d50
// 0x103a0b4: cbz x21, #0x103a474
// 0x103a0b8: ldr w10, [x21, #0x1c]
// 0x103a0bc: ldr x8, [x21, #0x10]
// 0x103a0c0: ldr x9, [x22]
// 0x103a0c4: add w10, w10, #1
// 0x103a0c8: str w10, [x21, #0x1c]
// 0x103a0cc: cbz x8, #0x103a474
// 0x103a0d0: ldrsw x10, [x21, #0x18]
// 0x103a0d4: ldr w11, [x8, #0x18]
// 0x103a0d8: mov x1, x0
// 0x103a0dc: cmp w10, w11
// 0x103a0e0: b.hs #0x103a0fc
// 0x103a0e4: add w9, w10, #1
// 0x103a0e8: add x0, x8, x10, lsl #3
// 0x103a0ec: str w9, [x21, #0x18]
// 0x103a0f0: str x1, [x0, #0x20]!
// 0x103a0f4: bl #0xf7d8d0
// 0x103a0f8: b #0x103a110
// 0x103a0fc: ldr x8, [x9, #0x20]
// 0x103a100: mov x0, x21
// 0x103a104: ldr x8, [x8, #0xc0]
// 0x103a108: ldr x2, [x8, #0x70]
// 0x103a10c: bl #0x14a3390
// 0x103a110: ldr x8, [x20]
// 0x103a114: cbz x8, #0x103a474
// 0x103a118: adrp x9, #0x1e8c000
// 0x103a11c: ldr x9, [x9, #0x560]
// 0x103a120: ldr x21, [x8, #0x10]
// 0x103a124: mov w1, #0x132
// 0x103a128: mov x2, xzr
// 0x103a12c: ldr x0, [x9]
// 0x103a130: bl #0x1040d50
// 0x103a134: cbz x21, #0x103a474
// 0x103a138: ldr w10, [x21, #0x1c]
// 0x103a13c: ldr x8, [x21, #0x10]
// 0x103a140: ldr x9, [x22]
// 0x103a144: add w10, w10, #1
// 0x103a148: str w10, [x21, #0x1c]
// 0x103a14c: cbz x8, #0x103a474
// 0x103a150: ldrsw x10, [x21, #0x18]
// 0x103a154: ldr w11, [x8, #0x18]
// 0x103a158: mov x1, x0
// 0x103a15c: cmp w10, w11
// 0x103a160: b.hs #0x103a17c
// 0x103a164: add w9, w10, #1
// 0x103a168: add x0, x8, x10, lsl #3
// 0x103a16c: str w9, [x21, #0x18]
// 0x103a170: str x1, [x0, #0x20]!
// 0x103a174: bl #0xf7d8d0
// 0x103a178: b #0x103a190
// 0x103a17c: ldr x8, [x9, #0x20]
// 0x103a180: mov x0, x21
// 0x103a184: ldr x8, [x8, #0xc0]
// 0x103a188: ldr x2, [x8, #0x70]
// 0x103a18c: bl #0x14a3390
// 0x103a190: ldr x8, [x20]
// 0x103a194: cbz x8, #0x103a474
// 0x103a198: adrp x9, #0x1e8c000
// 0x103a19c: ldr x9, [x9, #0x540]
// 0x103a1a0: ldr x20, [x8, #0x10]
// 0x103a1a4: mov w1, #0x20
// 0x103a1a8: mov x2, xzr
// 0x103a1ac: ldr x0, [x9]
// 0x103a1b0: bl #0x1040d50
// 0x103a1b4: cbz x20, #0x103a474
// 0x103a1b8: ldr w10, [x20, #0x1c]
// 0x103a1bc: ldr x8, [x20, #0x10]
// 0x103a1c0: ldr x9, [x22]
// 0x103a1c4: add w10, w10, #1
// 0x103a1c8: str w10, [x20, #0x1c]
// 0x103a1cc: cbz x8, #0x103a474
// 0x103a1d0: ldrsw x10, [x20, #0x18]
// 0x103a1d4: ldr w11, [x8, #0x18]
// 0x103a1d8: adrp x23, #0x1e8c000
// 0x103a1dc: adrp x21, #0x1e8c000
// 0x103a1e0: adrp x22, #0x1e8c000
// 0x103a1e4: ldr x23, [x23, #0x508]
// 0x103a1e8: ldr x21, [x21, #0x500]
// 0x103a1ec: ldr x22, [x22, #0x60]
// 0x103a1f0: mov x1, x0
// 0x103a1f4: cmp w10, w11
// 0x103a1f8: b.hs #0x103a214
// 0x103a1fc: add w9, w10, #1
// 0x103a200: add x0, x8, x10, lsl #3
// 0x103a204: str w9, [x20, #0x18]
// 0x103a208: str x1, [x0, #0x20]!
// 0x103a20c: bl #0xf7d8d0
// 0x103a210: b #0x103a228
// 0x103a214: ldr x8, [x9, #0x20]
// 0x103a218: mov x0, x20
// 0x103a21c: ldr x8, [x8, #0xc0]
// 0x103a220: ldr x2, [x8, #0x70]
// 0x103a224: bl #0x14a3390
// 0x103a228: ldr x0, [x23]
// 0x103a22c: bl #0xf7db70
// 0x103a230: ldr x2, [x21]
// 0x103a234: mov w1, #0x10
// 0x103a238: mov x20, x0
// 0x103a23c: bl #0x1491880
// 0x103a240: mov x0, x19
// 0x103a244: str x20, [x0, #0x88]!
// 0x103a248: mov x1, x20
// 0x103a24c: bl #0xf7d8d0
// 0x103a250: ldr x0, [x22]
// 0x103a254: bl #0xf7db70
// 0x103a258: mov x1, xzr
// 0x103a25c: mov x20, x0
// 0x103a260: bl #0x10609d8
// 0x103a264: mov x21, x19
// 0x103a268: str x20, [x21, #0xc0]!
// 0x103a26c: mov x0, x21
// 0x103a270: mov x1, x20
// 0x103a274: bl #0xf7d8d0
// 0x103a278: ldr x8, [x21]
// 0x103a27c: cbz x8, #0x103a474
// 0x103a280: mov w10, #0x999a
// 0x103a284: mov w9, #2
// 0x103a288: movk w10, #0x3e99, lsl #16
// 0x103a28c: mov x11, #0x100000000
// 0x103a290: str w9, [x8, #0x40]
// 0x103a294: str w10, [x8, #0x10]
// 0x103a298: str x11, [x8, #0x48]
// 0x103a29c: ldr x0, [x22]
// 0x103a2a0: bl #0xf7db70
// 0x103a2a4: mov x1, xzr
// 0x103a2a8: mov x20, x0
// 0x103a2ac: bl #0x10609d8
// 0x103a2b0: mov x21, x19
// 0x103a2b4: str x20, [x21, #0xc8]!
// 0x103a2b8: mov x0, x21
// 0x103a2bc: mov x1, x20
// 0x103a2c0: bl #0xf7d8d0
// 0x103a2c4: ldr x8, [x21]
// 0x103a2c8: cbz x8, #0x103a474
// 0x103a2cc: adrp x9, #0x832000
// 0x103a2d0: ldr d8, [x9, #0xf0]
// 0x103a2d4: mov x23, #0x3f000000
// 0x103a2d8: movk x23, #1, lsl #32
// 0x103a2dc: str wzr, [x8, #0x40]
// 0x103a2e0: str d8, [x8, #0x10]
// 0x103a2e4: str x23, [x8, #0x48]
// 0x103a2e8: ldr x0, [x22]
// 0x103a2ec: bl #0xf7db70
// 0x103a2f0: mov x1, xzr
// 0x103a2f4: mov x20, x0
// 0x103a2f8: bl #0x10609d8
// 0x103a2fc: mov x21, x19
// 0x103a300: str x20, [x21, #0xd0]!
// 0x103a304: mov x0, x21
// 0x103a308: mov x1, x20
// 0x103a30c: bl #0xf7d8d0
// 0x103a310: ldr x8, [x21]
// 0x103a314: cbz x8, #0x103a474
// 0x103a318: adrp x22, #0x1e8c000
// 0x103a31c: ldr x22, [x22, #0x68]
// 0x103a320: str wzr, [x8, #0x40]
// 0x103a324: str d8, [x8, #0x10]
// 0x103a328: str x23, [x8, #0x48]
// 0x103a32c: ldr x0, [x22]
// 0x103a330: bl #0xf7db70
// 0x103a334: mov x1, xzr
// 0x103a338: mov x20, x0
// 0x103a33c: bl #0x1056bb8
// 0x103a340: mov x21, x19
// 0x103a344: str x20, [x21, #0xd8]!
// 0x103a348: mov x0, x21
// 0x103a34c: mov x1, x20
// 0x103a350: bl #0xf7d8d0
// 0x103a354: ldr x8, [x21]
// 0x103a358: cbz x8, #0x103a474
// 0x103a35c: mov w23, #0xcccd
// 0x103a360: movk w23, #0x3e4c, lsl #16
// 0x103a364: str w23, [x8, #0x10]
// 0x103a368: ldr x0, [x22]
// 0x103a36c: bl #0xf7db70
// 0x103a370: mov x1, xzr
// 0x103a374: mov x20, x0
// 0x103a378: bl #0x1056bb8
// 0x103a37c: mov x21, x19
// 0x103a380: str x20, [x21, #0xe0]!
// 0x103a384: mov x0, x21
// 0x103a388: mov x1, x20
// 0x103a38c: bl #0xf7d8d0
// 0x103a390: ldr x8, [x21]
// 0x103a394: cbz x8, #0x103a474
// 0x103a398: adrp x28, #0x1e8c000
// 0x103a39c: ldr x28, [x28, #0x4e8]
// 0x103a3a0: str w23, [x8, #0x10]
// 0x103a3a4: adrp x22, #0x1e8c000
// 0x103a3a8: ldr x0, [x28]
// 0x103a3ac: ldr x22, [x22, #0x4e0]
// 0x103a3b0: bl #0xf7db70
// 0x103a3b4: mov x1, x19
// 0x103a3b8: mov x2, xzr
// 0x103a3bc: mov x21, x0
// 0x103a3c0: bl #0x103f9a4
// 0x103a3c4: mov x20, x19
// 0x103a3c8: str x21, [x20, #0xf0]!
// 0x103a3cc: mov x0, x20
// 0x103a3d0: mov x1, x21
// 0x103a3d4: bl #0xf7d8d0
// 0x103a3d8: ldr x0, [x22]
// 0x103a3dc: mov w1, #4
// 0x103a3e0: bl #0xf7d9d4
// 0x103a3e4: mov x1, x0
// 0x103a3e8: mov x21, x19
// 0x103a3ec: str x1, [x21, #0xe8]!
// 0x103a3f0: mov x0, x21
// 0x103a3f4: bl #0xf7d8d0
// 0x103a3f8: ldr x24, [x21]
// 0x103a3fc: cbz x24, #0x103a474
// 0x103a400: mov x23, xzr
// 0x103a404: mov w27, #0x20
// 0x103a408: ldrsw x8, [x24, #0x18]
// 0x103a40c: cmp x23, x8
// 0x103a410: b.ge #0x103a478
// 0x103a414: ldr x0, [x28]
// 0x103a418: bl #0xf7db70
// 0x103a41c: mov x1, x19
// 0x103a420: mov x2, xzr
// 0x103a424: mov x22, x0
// 0x103a428: bl #0x103f9a4
// 0x103a42c: cbz x22, #0x103a444
// 0x103a430: ldr x8, [x24]
// 0x103a434: mov x0, x22
// 0x103a438: ldr x1, [x8, #0x40]
// 0x103a43c: bl #0xf7da60
// 0x103a440: cbz x0, #0x103a8e0
// 0x103a444: ldr w8, [x24, #0x18]
// 0x103a448: cmp x23, x8
// 0x103a44c: b.hs #0x103a8dc
// 0x103a450: add x8, x24, x23, lsl #3
// 0x103a454: add x0, x24, x27
// 0x103a458: mov x1, x22
// 0x103a45c: str x22, [x8, #0x20]
// 0x103a460: bl #0xf7d8d0
// 0x103a464: ldr x24, [x21]
// 0x103a468: add x23, x23, #1
// 0x103a46c: add x27, x27, #8
// 0x103a470: cbnz x24, #0x103a408
// 0x103a474: bl #0xf7db74
// 0x103a478: ldr x8, [x20]
// 0x103a47c: cbz x8, #0x103a474
// 0x103a480: ldr x9, [x8, #0x88]
// 0x103a484: mov w10, #1
// 0x103a488: strb w10, [x8, #0x10]
// 0x103a48c: cbz x9, #0x103a474
// 0x103a490: ldr x0, [x9, #0x20]
// 0x103a494: cbz x0, #0x103a474
// 0x103a498: mov x1, xzr
// 0x103a49c: bl #0x105b43c
// 0x103a4a0: cbz x0, #0x103a474
// 0x103a4a4: ldr x1, [x29]
// 0x103a4a8: mov w2, wzr
// 0x103a4ac: mov x3, xzr
// 0x103a4b0: bl #0x105b50c
// 0x103a4b4: ldr x8, [x20]
// 0x103a4b8: cbz x8, #0x103a474
// 0x103a4bc: ldr x8, [x8, #0x88]
// 0x103a4c0: cbz x8, #0x103a474
// 0x103a4c4: ldr x0, [x8, #0x28]
// 0x103a4c8: cbz x0, #0x103a474
// 0x103a4cc: mov x1, xzr
// 0x103a4d0: bl #0x105b43c
// 0x103a4d4: cbz x0, #0x103a474
// 0x103a4d8: ldr x1, [x25]
// 0x103a4dc: mov w2, wzr
// 0x103a4e0: mov x3, xzr
// 0x103a4e4: bl #0x105b50c
// 0x103a4e8: ldr x8, [x20]
// 0x103a4ec: cbz x8, #0x103a474
// 0x103a4f0: ldr x9, [x8, #0x88]
// 0x103a4f4: cbz x9, #0x103a474
// 0x103a4f8: ldr x10, [x9, #0x20]
// 0x103a4fc: mov w11, #1
// 0x103a500: strb w11, [x9, #0x10]
// 0x103a504: cbz x10, #0x103a474
// 0x103a508: strb w11, [x10, #0x10]
// 0x103a50c: ldr x9, [x9, #0x28]
// 0x103a510: cbz x9, #0x103a474
// 0x103a514: mov w10, #1
// 0x103a518: strb w10, [x9, #0x10]
// 0x103a51c: ldr x8, [x8, #0x90]
// 0x103a520: cbz x8, #0x103a474
// 0x103a524: ldr x0, [x8, #0x20]
// 0x103a528: cbz x0, #0x103a474
// 0x103a52c: mov x1, xzr
// 0x103a530: bl #0x105b43c
// 0x103a534: cbz x0, #0x103a474
// 0x103a538: adrp x8, #0x1e8c000
// 0x103a53c: ldr x8, [x8, #0x550]
// 0x103a540: mov w2, wzr
// 0x103a544: mov x3, xzr
// 0x103a548: ldr x1, [x8]
// 0x103a54c: bl #0x105b50c
// 0x103a550: ldr x8, [x20]
// 0x103a554: cbz x8, #0x103a474
// 0x103a558: ldr x8, [x8, #0x90]
// 0x103a55c: cbz x8, #0x103a474
// 0x103a560: ldr x0, [x8, #0x28]
// 0x103a564: cbz x0, #0x103a474
// 0x103a568: mov x1, xzr
// 0x103a56c: bl #0x105b43c
// 0x103a570: cbz x0, #0x103a474
// 0x103a574: adrp x8, #0x1e8c000
// 0x103a578: ldr x8, [x8, #0x530]
// 0x103a57c: mov w2, wzr
// 0x103a580: mov x3, xzr
// 0x103a584: ldr x1, [x8]
// 0x103a588: bl #0x105b50c
// 0x103a58c: ldr x8, [x20]
// 0x103a590: cbz x8, #0x103a474
// 0x103a594: ldr x9, [x8, #0x90]
// 0x103a598: cbz x9, #0x103a474
// 0x103a59c: ldr x10, [x9, #0x20]
// 0x103a5a0: mov w11, #1
// 0x103a5a4: strb w11, [x9, #0x10]
// 0x103a5a8: cbz x10, #0x103a474
// 0x103a5ac: strb w11, [x10, #0x10]
// 0x103a5b0: ldr x9, [x9, #0x28]
// 0x103a5b4: cbz x9, #0x103a474
// 0x103a5b8: mov w10, #1
// 0x103a5bc: strb w10, [x9, #0x10]
// 0x103a5c0: ldr x8, [x8, #0x98]
// 0x103a5c4: cbz x8, #0x103a474
// 0x103a5c8: ldr x0, [x8, #0x20]
// 0x103a5cc: cbz x0, #0x103a474
// 0x103a5d0: mov x1, xzr
// 0x103a5d4: bl #0x105b43c
// 0x103a5d8: cbz x0, #0x103a474
// 0x103a5dc: ldr x1, [x29]
// 0x103a5e0: mov w2, wzr
// 0x103a5e4: mov x3, xzr
// 0x103a5e8: bl #0x105b50c
// 0x103a5ec: ldr x8, [x20]
// 0x103a5f0: cbz x8, #0x103a474
// 0x103a5f4: ldr x8, [x8, #0x98]
// 0x103a5f8: cbz x8, #0x103a474
// 0x103a5fc: ldr x0, [x8, #0x28]
// 0x103a600: cbz x0, #0x103a474
// 0x103a604: mov x1, xzr
// 0x103a608: bl #0x105b43c
// 0x103a60c: cbz x0, #0x103a474
// 0x103a610: ldr x1, [x25]
// 0x103a614: mov w2, wzr
// 0x103a618: mov x3, xzr
// 0x103a61c: bl #0x105b50c
// 0x103a620: ldr x8, [x20]
// 0x103a624: cbz x8, #0x103a474
// 0x103a628: adrp x21, #0x1e8c000
// 0x103a62c: ldr x9, [x8, #0x98]
// 0x103a630: ldr x21, [x21, #0x560]
// 0x103a634: cbz x9, #0x103a474
// 0x103a638: ldr x10, [x9, #0x20]
// 0x103a63c: mov w11, #1
// 0x103a640: strb w11, [x9, #0x10]
// 0x103a644: cbz x10, #0x103a474
// 0x103a648: strb w11, [x10, #0x10]
// 0x103a64c: ldr x10, [x9, #0x28]
// 0x103a650: cbz x10, #0x103a474
// 0x103a654: mov w9, #1
// 0x103a658: strb w9, [x10, #0x10]
// 0x103a65c: ldr x0, [x8, #0x18]
// 0x103a660: cbz x0, #0x103a474
// 0x103a664: mov x1, xzr
// 0x103a668: strb w9, [x0, #0x10]
// 0x103a66c: bl #0x105bfec
// 0x103a670: cbz x0, #0x103a474
// 0x103a674: ldr x1, [x26]
// 0x103a678: mov w2, #1
// 0x103a67c: mov x3, xzr
// 0x103a680: bl #0x105c0bc
// 0x103a684: ldr x8, [x20]
// 0x103a688: cbz x8, #0x103a474
// 0x103a68c: ldr x0, [x8, #0x20]
// 0x103a690: cbz x0, #0x103a474
// 0x103a694: mov w8, #1
// 0x103a698: mov x1, xzr
// 0x103a69c: strb w8, [x0, #0x10]
// 0x103a6a0: bl #0x105bfec
// 0x103a6a4: cbz x0, #0x103a474
// 0x103a6a8: adrp x8, #0x1e8c000
// 0x103a6ac: ldr x8, [x8, #0x540]
// 0x103a6b0: mov w2, #1
// 0x103a6b4: mov x3, xzr
// 0x103a6b8: ldr x1, [x8]
// 0x103a6bc: bl #0x105c0bc
// 0x103a6c0: ldr x8, [x20]
// 0x103a6c4: cbz x8, #0x103a474
// 0x103a6c8: ldr x0, [x8, #0x28]
// 0x103a6cc: cbz x0, #0x103a474
// 0x103a6d0: mov w8, #1
// 0x103a6d4: mov x1, xzr
// 0x103a6d8: strb w8, [x0, #0x10]
// 0x103a6dc: bl #0x105bfec
// 0x103a6e0: cbz x0, #0x103a474
// 0x103a6e4: ldr x1, [x21]
// 0x103a6e8: mov w2, #1
// 0x103a6ec: mov x3, xzr
// 0x103a6f0: bl #0x105c0bc
// 0x103a6f4: ldr x8, [x20]
// 0x103a6f8: cbz x8, #0x103a474
// 0x103a6fc: ldr x0, [x8, #0x30]
// 0x103a700: cbz x0, #0x103a474
// 0x103a704: mov w8, #1
// 0x103a708: mov x1, xzr
// 0x103a70c: strb w8, [x0, #0x10]
// 0x103a710: bl #0x105bfec
// 0x103a714: cbz x0, #0x103a474
// 0x103a718: adrp x8, #0x1e8c000
// 0x103a71c: ldr x8, [x8, #0x558]
// 0x103a720: mov w2, #1
// 0x103a724: mov x3, xzr
// 0x103a728: ldr x1, [x8]
// 0x103a72c: bl #0x105c0bc
// 0x103a730: ldr x8, [x20]
// 0x103a734: cbz x8, #0x103a474
// 0x103a738: ldr x0, [x8, #0x50]
// 0x103a73c: cbz x0, #0x103a474
// 0x103a740: mov w8, #1
// 0x103a744: mov x1, xzr
// 0x103a748: strb w8, [x0, #0x10]
// 0x103a74c: bl #0x105bfec
// 0x103a750: cbz x0, #0x103a474
// 0x103a754: ldr x1, [x26]
// 0x103a758: mov w2, #1
// 0x103a75c: mov x3, xzr
// 0x103a760: bl #0x105c0bc
// 0x103a764: ldr x8, [x20]
// 0x103a768: cbz x8, #0x103a474
// 0x103a76c: ldr x0, [x8, #0x60]
// 0x103a770: cbz x0, #0x103a474
// 0x103a774: mov w8, #1
// 0x103a778: mov x1, xzr
// 0x103a77c: strb w8, [x0, #0x10]
// 0x103a780: bl #0x105bfec
// 0x103a784: cbz x0, #0x103a474
// 0x103a788: ldr x1, [x26]
// 0x103a78c: mov w2, #1
// 0x103a790: mov x3, xzr
// 0x103a794: bl #0x105c0bc
// 0x103a798: ldr x8, [x20]
// 0x103a79c: cbz x8, #0x103a474
// 0x103a7a0: ldr x0, [x8, #0x48]
// 0x103a7a4: cbz x0, #0x103a474
// 0x103a7a8: mov w8, #1
// 0x103a7ac: mov x1, xzr
// 0x103a7b0: strb w8, [x0, #0x10]
// 0x103a7b4: bl #0x105bfec
// 0x103a7b8: cbz x0, #0x103a474
// 0x103a7bc: ldr x1, [x21]
// 0x103a7c0: mov w2, #1
// 0x103a7c4: mov x3, xzr
// 0x103a7c8: bl #0x105c0bc
// 0x103a7cc: ldr x8, [x20]
// 0x103a7d0: cbz x8, #0x103a474
// 0x103a7d4: ldr x0, [x8, #0x58]
// 0x103a7d8: cbz x0, #0x103a474
// 0x103a7dc: mov w8, #1
// 0x103a7e0: mov x1, xzr
// 0x103a7e4: strb w8, [x0, #0x10]
// 0x103a7e8: bl #0x105bfec
// 0x103a7ec: cbz x0, #0x103a474
// 0x103a7f0: ldr x1, [x21]
// 0x103a7f4: mov w2, #1
// 0x103a7f8: mov x3, xzr
// 0x103a7fc: bl #0x105c0bc
// 0x103a800: adrp x8, #0x1e8c000
// 0x103a804: ldr x8, [x8, #0x520]
// 0x103a808: ldr x0, [x8]
// 0x103a80c: bl #0xf7db70
// 0x103a810: mov x1, x19
// 0x103a814: mov x2, xzr
// 0x103a818: mov x20, x0
// 0x103a81c: bl #0x10427e0
// 0x103a820: add x0, x19, #0x110
// 0x103a824: mov x1, x20
// 0x103a828: str x20, [x19, #0x110]
// 0x103a82c: bl #0xf7d8d0
// 0x103a830: adrp x8, #0x1e8c000
// 0x103a834: ldr x8, [x8, #0x510]
// 0x103a838: ldr x0, [x8]
// 0x103a83c: bl #0xf7db70
// 0x103a840: mov x1, x19
// 0x103a844: mov x2, xzr
// 0x103a848: mov x20, x0
// 0x103a84c: bl #0x10434c4
// 0x103a850: add x0, x19, #0x118
// 0x103a854: mov x1, x20
// 0x103a858: str x20, [x19, #0x118]
// 0x103a85c: bl #0xf7d8d0
// 0x103a860: adrp x8, #0x1e8c000
// 0x103a864: ldr x8, [x8, #0x518]
// 0x103a868: ldr x0, [x8]
// 0x103a86c: bl #0xf7db70
// 0x103a870: mov x1, x19
// 0x103a874: mov x2, xzr
// 0x103a878: mov x20, x0
// 0x103a87c: bl #0x1042fa0
// 0x103a880: add x0, x19, #0x120
// 0x103a884: mov x1, x20
// 0x103a888: str x20, [x19, #0x120]
// 0x103a88c: bl #0xf7d8d0
// 0x103a890: adrp x8, #0x1e8c000
// 0x103a894: ldr x8, [x8, #0x4c8]
// 0x103a898: ldr x0, [x8]
// 0x103a89c: bl #0xf7db70
// 0x103a8a0: mov x1, x19
// 0x103a8a4: mov x2, xzr
// 0x103a8a8: mov x20, x0
// 0x103a8ac: bl #0x1042560
// 0x103a8b0: add x0, x19, #0x100
// 0x103a8b4: str x20, [x19, #0x100]
// 0x103a8b8: mov x1, x20
// 0x103a8bc: ldp x20, x19, [sp, #0x60]
// 0x103a8c0: ldp x22, x21, [sp, #0x50]
// 0x103a8c4: ldp x24, x23, [sp, #0x40]
// 0x103a8c8: ldp x26, x25, [sp, #0x30]
// 0x103a8cc: ldp x28, x27, [sp, #0x20]
// 0x103a8d0: ldp x29, x30, [sp, #0x10]
// 0x103a8d4: ldr d8, [sp], #0x70
// 0x103a8d8: b #0xf7d8d0
// 0x103a8dc: bl #0xf7db7c
// 0x103a8e0: bl #0xf7db98
// 0x103a8e4: mov x1, xzr
// 0x103a8e8: bl #0xf7da4c
```

## `InputRig.InitEmuTouches` — RVA `0xc3a8ec`

- Decompiled symbol: `InputRig_InitEmuTouches`
- Metadata signature: `private void InitEmuTouches() { }`
- Native interval: `368` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_Recovered` matched 2 offsets against `InputRig` metadata (confidence 1.00).

```c
typedef struct struct_3 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_3;

typedef struct InputRig_Recovered {
    char padding_0[352];
    struct struct_4 *emuTouches;
    long long emuTouchesOrdered;
} InputRig_Recovered;

typedef struct struct_4 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_4;

typedef struct struct_6 {
    char padding_0[32];
    long long field_20;
} struct_6;

typedef struct struct_0 {
    char padding_0[112];
    long long field_70;
} struct_0;

typedef struct struct_1 {
    char padding_0[192];
    struct struct_0 *field_c0;
} struct_1;

typedef struct struct_2 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_2;

extern long long g_1eeda00;
extern long long g_1ef3330;
extern long long g_1ef90e0;
extern struct_2 *g_1ef90e8;
extern char g_1fab1d3;

long long InputRig_InitEmuTouches(struct_5 *p)
{
    struct_3 *v0;  // x21
    struct_5 *addr;  // x19
    long long v2;  // x21
    unsigned int v3;  // w20
    struct_4 *ptr;  // x21
    long long v5;  // x22
    unsigned long long v6;  // x8
    unsigned long v7;  // x10
    struct_6 *ptr3;  // x0
    unsigned long v9;  // x0

    if (!(g_1fab1d3 & 1))
    {
        sub_f7d92c(&g_1ef3330);
        sub_f7d92c(&g_1ef90e8);
        sub_f7d92c(&g_1ef90e0);
        sub_f7d92c(&g_1eeda00);
        g_1fab1d3 = 1;
    }
    v0 = sub_f7db70(g_1eeda00);
    sub_14a2bd4(v0, 8, g_1ef90e0);
    addr = &p->field_160;
    p->field_160 = v0;
    sub_f7d8d0(addr, v0);
    v2 = sub_f7db70(g_1eeda00);
    sub_14a2bd4(v2, 8, g_1ef90e0);
    p->field_168 = v2;
    sub_f7d8d0((struct InputRig_Recovered *)&p->field_168, v2);
    v3 = 0;
    while (true)
    {
        ptr = *((long long *)&addr->padding_0[0]);
        v5 = sub_f7db70(g_1ef3330);
        InputRig_EmulatedTouchState__ctor(v5, v3, 0);
        if (!ptr || !((v6 = ptr->field_10, ptr->field_1c = ptr->field_1c + 1, v6)))
            break;
        v7 = ptr->field_18;
        if (*((int *)(v6 + 24)) > (unsigned int)v7)
        {
            ptr3 = v6 + v7 * 8;
            ptr->field_18 = (unsigned int)v7 + 1;
            ptr3->field_20 = v5;
            v9 = sub_f7d8d0((struct struct_6 *)&ptr3->field_20, v5);
        }
        else
        {
            v9 = sub_14a3390(ptr, v5, g_1ef90e8->field_20->field_c0->field_70);
        }
        v3 += 1;
        if (v3 == 8)
            return v9;
    }
    sub_f7db74();
}
```

## `InputRig.OnInitComponent` — RVA `0xc3aa5c`

- Decompiled symbol: `InputRig_OnInitComponent`
- Metadata signature: `protected override void OnInitComponent() { }`
- Native interval: `64` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[256];
    long long field_100;
} struct_0;

long long InputRig_OnInitComponent(struct_0 *a0)
{
    unsigned long long v0;  // x0

    if (a0->field_100)
    {
        InputRig_AutomaticInputConfigCollection__SetRig(a0->field_100, a0, 0);
        InputRig__ResetState();
        InputRig__ResetAllSwitches(a0, 1);
        v0 = InputRig__InvalidateBlockedKeys(a0);
        return InputRig__InvalidateBlockedKeys(a0);
    }
    sub_f7db74(0);
}
```

## `InputRig.ResetState` — RVA `0xc3aa9c`

- Decompiled symbol: `InputRig_ResetState`
- Metadata signature: `public void ResetState() { }`
- Native interval: `460` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_Recovered` matched 5 offsets against `InputRig` metadata (confidence 0.83).

```c
typedef struct InputRig_Recovered {
    char padding_0[32];
    char field_20;
    char padding_21[87];
    unsigned long long joysticks;
    unsigned long long axes;
    char padding_88[136];
    long long tilt;
    unsigned long long mouseConfig;
    unsigned long long scrollWheel;
} InputRig_Recovered;

extern long long g_1ef0c58;
extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern long long g_1ef9860;
extern long long g_1ef98a0;
extern char g_1fab1a4;

struct_0 * InputRig_ResetState(struct_0 *ptr)
{
    struct_0 *v0;  // x0
    struct_0 *v1;  // x0
    struct_0 *v2;  // x0
    unsigned long v3;  // x0
    unsigned long v4;  // x0

    v0 = ptr;
    if (!(g_1fab1a4 & 1))
    {
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef8a38);
        sub_f7d92c(&g_1ef98a0);
        sub_f7d92c(&g_1ef9860);
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab1a4 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (!ptr->field_20)
        return v2;
    v3 = ptr->field_110;
    if (v3)
    {
        InputRig_TiltConfig__Reset(v3, 0);
        v3 = ptr->field_118;
        if (v3)
        {
            InputRig_MouseConfig__Reset(v3, 0);
            v3 = ptr->field_120;
            if (v3)
            {
                InputRig_ScrollWheelState__Reset(v3, 0);
                InputRig__ResetEmuTouches(ptr);
                v3 = ptr->field_78;
                if (v3)
                {
                    sub_1526400(v3, g_1ef98a0);
                    v3 = ptr->field_80;
                    if (v3)
                    {
                        sub_1526400(v3, g_1ef9860);
                        InputRig__MuteUntilRelease(ptr); /* do not return */
                    }
                }
            }
        }
    }
    v4 = sub_f7db74(v3);
    return sub_f7db74(v3);
}
```

## `InputRig.ResetAllSwitches` — RVA `0xc3ac68`

- Decompiled symbol: `InputRig_ResetAllSwitches`
- Metadata signature: `public void ResetAllSwitches(bool skipAnim) { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[248];
    long long field_f8;
} struct_0;

unsigned long long InputRig_ResetAllSwitches(struct_0 *a0, unsigned int a1)
{
    unsigned long long v0;  // x0
    unsigned long long v1;  // x0

    if (a0->field_f8)
    {
        v0 = InputRig_RigSwitchCollection__Reset(a0->field_f8, 0);
        if (!((char)a1 & 1))
            return v0;
        v1 = InputRig__ApplySwitches(a0, 1);
        return InputRig__ApplySwitches(a0, 1);
    }
    sub_f7db74(0);
}
```

## `InputRig.InvalidateBlockedKeys` — RVA `0xc3acb0`

- Decompiled symbol: `InputRig_InvalidateBlockedKeys`
- Metadata signature: `private void InvalidateBlockedKeys() { }`
- Native interval: `188` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

extern long long g_1ef7f38;
extern long long g_1ef7f40;
extern char g_1fab1a6;

struct_1 * InputRig_InvalidateBlockedKeys(struct_0 **ptr)
{
    struct_1 *v0;  // x0
    int v1;  // w20
    unsigned long long v2;  // x0
    unsigned long v3;  // x0

    if (!(g_1fab1a6 & 1))
    {
        sub_f7d92c(&g_1ef7f38);
        sub_f7d92c(&g_1ef7f40);
        g_1fab1a6 = 1;
    }
    v0 = ptr[22];
    if (v0)
    {
        BitArray__SetAll(v0, 0, 0);
        v0 = ptr[17];
        if (v0)
        {
            v1 = 0;
            do
            {
                if (v0->field_18 <= v1)
                    return v0;
                v2 = sub_1491d6c();
                if ((v2 >> 31 & 1))
                    continue;
                v0 = ptr[22];
                if (!v0)
                    break;
                if (v0->field_18 > (unsigned int)v2)
                    BitArray__set_Item();
            } while ((v0 = (struct_1 *)ptr[17], v1 = (int)(v1 + 1), v0));
        }
    }
    v3 = sub_f7db74(v0);
    return sub_f7db74(v0);
}
```

## `InputRig.OnDestroyComponent` — RVA `0xc3ad6c`

- Decompiled symbol: `InputRig_OnDestroyComponent`
- Metadata signature: `protected override void OnDestroyComponent() { }`
- Native interval: `236` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_2 {
    char padding_0[264];
    struct struct_1 *field_108;
} struct_2;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern char g_1fab1a0;

struct_3 * InputRig_OnDestroyComponent(struct_2 *ptr)
{
    struct_1 *v0;  // x0
    int v1;  // w20
    long long v2;  // x21
    struct_3 *v3;  // x0
    unsigned long v4;  // x0

    if (!(g_1fab1a0 & 1))
    {
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef8a38);
        sub_f7d92c(&g_1ef0c58);
        g_1fab1a0 = 1;
    }
    v0 = ptr->field_108;
    if (!v0)
    {
        return v0;
    }
    else if (v0->field_18 >= 1)
    {
        v1 = 0;
        do
        {
            v2 = sub_14a30c0();
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v3 = Object__op_Inequality(v2, 0, 0);
            if (!(v3 & 1))
                continue;
            if (!v2)
                break;
            v3 = TouchControl__SetRig(v2, 0, 0);
            v1 += 1;
            if (v0->field_18 == v1)
                return v3;
        } while (ptr->field_108);
        v4 = sub_f7db74();
        return sub_f7db74();
    }
    else
    {
        return v0;
    }
}
```

## `InputRig.OnEnableComponent` — RVA `0xc3ae58`

- Decompiled symbol: `InputRig_OnEnableComponent`
- Metadata signature: `protected override void OnEnableComponent() { }`
- Native interval: `852` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_Recovered` matched 3 offsets against `InputRig` metadata (confidence 1.00).

```c
typedef struct InputRig_Recovered {
    char padding_0[56];
    char autoActivate;
    char overrideActiveRig;
    char padding_3a[238];
    long long fixedTimeStep;
} InputRig_Recovered;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct struct_6 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_6;

typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

typedef struct struct_3 {
    char padding_0[304];
    char field_130;
} struct_3;

typedef struct struct_4 {
    char padding_0[224];
    unsigned int field_e0;
} struct_4;

extern struct_1 *g_1eeed00;
extern long long g_1eeed08;
extern struct_2 *g_1eef828;
extern struct_3 *g_1ef0988;
extern struct_4 *g_1ef0c58;
extern long long g_1eff4e8;
extern long long g_1eff4f0;
extern long long g_1f00210;
extern char g_1fab1a1;
extern char g_1fab1df;

long long InputRig_OnEnableComponent(struct_5 *ptr)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long v16;  // x10
    struct_6 **v17;  // x20
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    struct_1 *v12;  // x0
    long long v13;  // x20
    long long v14;  // x0
    struct_6 **v15;  // x0
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]
    unsigned long long v5;  // [bp-0x8]

    v0 = v6;
    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    if (!(g_1fab1a1 & 1))
    {
        sub_f7d92c("++");
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1eeed08);
        sub_f7d92c(&g_1eef828);
        sub_f7d92c(&g_1eff4e8);
        sub_f7d92c(&g_1eff4f0);
        sub_f7d92c(&g_1ef0988);
        sub_f7d92c(&g_1f00210);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("-#");
        g_1fab1a1 = 1;
    }
    if (ptr->field_38)
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        if (!g_1fab1df)
        {
            sub_f7d92c(&g_1eeed00);
            g_1fab1df = 1;
        }
        v12 = g_1eeed00;
        if (!g_1eeed00->field_e0)
        {
            sub_f7da5c(g_1eeed00);
            v12 = g_1eeed00;
        }
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Equality(v12->field_b8->field_18, 0, 0) & 1) || ptr->field_39)
        {
            if (!g_1eeed00->field_e0)
                sub_f7da5c(g_1eeed00);
            CF2Input__set_activeRig(ptr);
        }
    }
    if (!g_1eef828->field_e0)
        sub_f7da5c(g_1eef828);
    v13 = EventSystem__get_current(0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(v13, 0, 0) & 1))
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v13 = sub_1129dbc(g_1f00210);
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v14 = Object__op_Inequality(v13, 0, 0);
    if (((char)v14 & 1))
    {
        if (v13)
        {
            v15 = Component__GetComponent(v13, g_1f0eea8, 0);
            if (!v15 || (v16 = (unsigned long)(unsigned long long)g_1ef0988->field_130, (unsigned int)v16 > (unsigned int)*(v15)->field_130))
            {
                v17 = NULL;
            }
            else if (*((long long *)(*(v15)->field_c8 + v16 * 8 - 8)) == g_1ef0988)
            {
                v17 = v15;
            }
            else
            {
                v17 = NULL;
            }
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v14 = Object__op_Inequality(v17, 0, 0);
            if (((char)v14 & 1))
            {
                if (!v17)
                {
                    sub_f7db74(v14);
                }
                else if (((char)Behaviour__get_enabled(v17, 0) & 1))
                {
                    Behaviour__set_enabled(v17, 0, 0);
                }
            }
        }
        else
        {
            sub_f7db74(v14);
        }
    }
    v14 = ptr->field_128;
    if (v14)
    {
        FixedTimeStepController__Reset(v14, 0);
        InputRig__ResetState(ptr);
        InputRig__MuteUntilRelease(); /* do not return */
    }
    sub_f7db74(v14);
}
```

## `InputRig.MuteUntilRelease` — RVA `0xc3b1ac`

- Decompiled symbol: `InputRig_MuteUntilRelease`
- Metadata signature: `public void MuteUntilRelease() { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
void InputRig_MuteUntilRelease(long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[16];
    if (v4)
    {
        InputRig_AxisConfigCollection__MuteAllUntilRelease(v4, 0);
        v4 = ptr[18];
        if (v4)
        {
            BitArray__SetAll(v4, 0, 0);
            v4 = ptr[19];
            if (v4)
            {
                BitArray__SetAll(v4, 0, 0);
                v4 = ptr[21];
                if (ptr[21])
                {
                    BitArray__SetAll();
                    return;
                }
            }
        }
    }
    sub_f7db74(v4);
}
```

## `InputRig.OnDisableComponent` — RVA `0xc3b208`

- Decompiled symbol: `InputRig_OnDisableComponent`
- Metadata signature: `protected override void OnDisableComponent() { }`
- Native interval: `460` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_Recovered` matched 2 offsets against `InputRig` metadata (confidence 1.00).

```c
typedef struct InputRig_Recovered {
    char padding_0[184];
    struct struct_0 *keysNextSomeDown;
    char padding_c0[32];
    unsigned int rightTriggerAnalogConfig;
} InputRig_Recovered;

typedef struct struct_5 {
    char padding_0[58];
    char field_3a;
} struct_5;

typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

typedef struct struct_3 {
    char padding_0[224];
    unsigned int field_e0;
} struct_3;

extern struct_1 *g_1eeed00;
extern struct_2 *g_1eeed08;
extern struct_3 *g_1ef0c58;
extern long long g_1eff4e8;
extern long long g_1eff4f0;
extern char g_1fab1a2;
extern char g_1fab1df;

long long InputRig_OnDisableComponent(unsigned long a0)
{
    struct_1 *v0;  // x0
    long long v1;  // x0
    long long v2;  // x0
    long long v3;  // x0
    long long v4;  // x0

    if (!(g_1fab1a2 & 1))
    {
        sub_f7d92c("++");
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1eeed08);
        sub_f7d92c(&g_1eff4e8);
        sub_f7d92c(&g_1eff4f0);
        sub_f7d92c(&g_1ef0c58);
        g_1fab1a2 = 1;
    }
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    if (!g_1fab1df)
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab1df = 1;
    }
    v0 = g_1eeed00;
    if (!g_1eeed00->field_e0)
    {
        sub_f7da5c(g_1eeed00);
        v0 = g_1eeed00;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(v0->field_b8->field_18, a0, 0) & 1))
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        CF2Input__set_activeRig(NULL);
    }
    InputRig__ResetState(a0);
    v1 = CFUtils__get_editorStopped(0);
    if (((char)v1 & 1))
        return v1;
    v2 = sub_f7db70(g_1eee648);
    Action__ctor(v2, a0, g_1eff4f0, 0);
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    CF2Input__remove_onMobileModeChange(v2);
    v3 = sub_f7db70(g_1eee648);
    Action__ctor(v3, a0, g_1eff4e8, 0);
    if (!g_1eeed08->field_e0)
        sub_f7da5c(g_1eeed08);
    v4 = CFCursor__remove_onLockStateChange(v3);
    return CFCursor__remove_onLockStateChange(v3);
}
```

## `InputRig.OnMobileModeChange` — RVA `0xc3b3d4`

- Decompiled symbol: `InputRig_OnMobileModeChange`
- Metadata signature: `private void OnMobileModeChange() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long InputRig_OnMobileModeChange(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = InputRig__SyncDisablingConditions();
    return InputRig__SyncDisablingConditions();
}
```

## `InputRig.SyncDisablingConditions` — RVA `0xc3b3dc`

- Decompiled symbol: `InputRig_SyncDisablingConditions`
- Metadata signature: `private void SyncDisablingConditions(bool noAnim) { }`
- Native interval: `276` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern char g_1fab1ac;

long long InputRig_SyncDisablingConditions(struct_1 **ptr, unsigned int a1)
{
    struct_2 *v0;  // x0
    struct_2 *v1;  // x0
    unsigned int v2;  // w20
    long long v3;  // x22
    struct_2 *v4;  // x0
    struct_2 *v5;  // x0
    unsigned long long v6;  // x0

    if (!(g_1fab1ac & 1))
    {
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef8a38);
        sub_f7d92c(&g_1ef0c58);
        g_1fab1ac = 1;
    }
    v0 = ptr[33];
    v1 = v0;
    if (v1)
    {
        if (v0->field_18 >= 1)
        {
            v2 = 0;
            do
            {
                v3 = sub_14a30c0();
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v4 = Object__op_Inequality(v3, 0, 0);
                if (((char)v4 & 1))
                {
                    v1 = v4;
                    if (!v3)
                        break;
                    TouchControl__SyncDisablingConditions(v3, a1 & 1, 0);
                }
                v2 += 1;
                if (v0->field_18 == v2)
                    goto LABEL_103b4bc;
            } while ((v5 = (struct_2 *)ptr[33], v1 = (struct_2 *)ptr[33], v1));
        }
        else
        {
LABEL_103b4bc:
            v1 = ptr[34];
            if (v1)
            {
                InputRig_TiltConfig__OnDisablingConditionsChange(v1, 0);
                v1 = ptr[32];
                if (v1)
                {
                    v6 = InputRig_AutomaticInputConfigCollection__OnDisablingConditionsChange(v1, 0);
                    return InputRig_AutomaticInputConfigCollection__OnDisablingConditionsChange(v1, 0);
                }
            }
        }
    }
    sub_f7db74(v1);
}
```

## `InputRig.OnCursorLockStateChange` — RVA `0xc3b4f0`

- Decompiled symbol: `InputRig_OnCursorLockStateChange`
- Metadata signature: `private void OnCursorLockStateChange() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

long long InputRig_OnCursorLockStateChange(struct_1 **a0)
{
    long long v0;  // x0

    v0 = InputRig__SyncDisablingConditions(a0, 0);
    return InputRig__SyncDisablingConditions(a0, 0);
}
```

## `InputRig.OnApplicationPause` — RVA `0xc3b4f8`

- Decompiled symbol: `InputRig_OnApplicationPause`
- Metadata signature: `private void OnApplicationPause(bool paused) { }`
- Native interval: `240` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_2 {
    char padding_0[264];
    struct struct_1 *field_108;
} struct_2;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

typedef struct struct_4 {
    char padding_0[680];
    struct struct_5 *field_2a8;
    unsigned long long field_2b0;
} struct_4;

typedef struct struct_5 {
    unsigned long long field_0;
} struct_5;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern char g_1fab1a3;

struct_3 * InputRig_OnApplicationPause(struct_2 *ptr)
{
    struct_1 *v0;  // x0
    struct_1 *i;  // x0
    int v2;  // w20
    struct_4 **v3;  // x21
    unsigned long long flag;  // x2
    struct_3 *v5;  // x0
    struct_4 **v7;  // x0
    unsigned long v8;  // x1
    unsigned long v9;  // x0

    if (!(g_1fab1a3 & 1))
    {
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef8a38);
        sub_f7d92c(&g_1ef0c58);
        g_1fab1a3 = 1;
    }
    v0 = ptr->field_108;
    i = v0;
    if (i)
    {
        if (v0->field_18 >= 1)
        {
            v2 = 0;
            do
            {
                v3 = sub_14a30c0();
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                flag = 0;
                v5 = Object__op_Inequality(v3, 0, 0);
                if (((char)v5 & 1))
                {
                    i = v5;
                    if (v3)
                    {
                        v7 = v3;
                        v8 = *(v3)->field_2b0;
                        *(v3)->field_2a8();
                    }
                    break;
                }
                v2 += 1;
                if (v0->field_18 == v2)
                    return v5;
                i = ptr->field_108;
            } while (i);
        }
        else
        {
            return v0;
        }
    }
    v9 = sub_f7db74(i);
    return sub_f7db74(i);
}
```

## `InputRig.Update` — RVA `0xc3b5e8`

- Decompiled symbol: `InputRig_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `80` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_Recovered` matched 2 offsets against `InputRig` metadata (confidence 1.00).

```c
typedef struct struct_2 {
    char padding_0[32];
    char field_20;
    char padding_21[15];
    struct struct_0 *field_30;
    char padding_38[4];
    char field_3c;
    char padding_3d[3];
    unsigned int field_40;
    char field_44;
    char padding_45[3];
    unsigned int field_48;
    char padding_4c[36];
    unsigned int field_70;
    char field_74;
    char padding_75[3];
    long long field_78;
    long long field_80;
    char padding_88[120];
    long long field_100;
    long long field_108;
    long long field_110;
    long long field_118;
    long long field_120;
    long long field_128;
} struct_2;

typedef struct struct_10 {
    char padding_0[136];
    int field_88;
} struct_10;

typedef struct InputRig_Recovered {
    char padding_0[184];
    struct struct_3 *keysNextSomeDown;
    char padding_c0[32];
    unsigned int rightTriggerAnalogConfig;
} InputRig_Recovered;

typedef struct struct_5 {
    char padding_0[24];
    struct struct_6 *field_18;
    char padding_20[8];
    unsigned long long field_28;
    char padding_30[16];
    unsigned long long field_40;
} struct_5;

typedef struct struct_0 {
    char padding_0[24];
    struct struct_1 *field_18;
    char padding_20[8];
    unsigned long long field_28;
    char padding_30[16];
    unsigned long long field_40;
} struct_0;

typedef struct struct_3 {
    char padding_0[24];
    long long field_18;
} struct_3;

typedef struct struct_6 {
    unsigned long long field_0;
} struct_6;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

typedef struct struct_12 {
    struct struct_10 *field_0;
} struct_12;

typedef struct struct_9 {
    char padding_0[224];
    unsigned int field_e0;
} struct_9;

typedef struct struct_11 {
    char padding_0[184];
    struct struct_12 *field_b8;
} struct_11;

extern char g_103b638;
extern struct_4 *g_1eeed00;
extern struct_11 *g_1eefb00;
extern struct_9 *g_1ef0c58;
extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern long long g_1ef9840;
extern long long g_1ef9868;
extern long long g_1ef98a8;
extern char g_1fab1a5;
extern char g_1fab1dd;
extern char g_1fab1df;

unsigned long long InputRig_Update(struct_2 *ptr3)
{
    unsigned long long v11;  // x30
    unsigned long long v12;  // x20
    unsigned long long v21;  // x26
    unsigned long long v22;  // x25
    unsigned long long v23;  // x24
    unsigned long long v24;  // x23
    unsigned long long v25;  // x22
    unsigned long long v26;  // x21
    struct_2 *ptr;  // x19
    unsigned int v28;  // w8
    long long v29;  // x0
    unsigned int v30;  // w8
    struct_2 *v13;  // x19
    unsigned int v31;  // s8
    unsigned int v32;  // s0
    unsigned long v33;  // 4129
    unsigned long v34;  // 4125
    unsigned long v35;  // 4125
    unsigned int v36;  // s0
    unsigned long v37;  // 4142
    int v38;  // w20
    struct_4 *v39;  // x0
    unsigned long long v14;  // x0
    unsigned long long flag;  // x2
    struct_5 *p;  // x8
    unsigned long long v42;  // x0
    unsigned long long v43;  // x1
    struct_0 *addr;  // x8
    unsigned long long v45;  // x0
    unsigned long long v46;  // x1
    unsigned long long v47;  // x0
    unsigned long long v15;  // x20
    struct_2 *v16;  // x19
    struct_2 *v17;  // x0
    unsigned long long v19;  // d9
    unsigned long long v20;  // d8
    unsigned long long v0;  // [bp-0x60]
    unsigned long long v1;  // [bp-0x58]
    unsigned long v2;  // [bp-0x50]
    unsigned long long v3;  // [bp-0x40]
    unsigned long long v4;  // [bp-0x38]
    unsigned long long v5;  // [bp-0x30]
    unsigned long long v6;  // [bp-0x28]
    unsigned long long v7;  // [bp-0x20]
    unsigned long long v8;  // [bp-0x18]
    unsigned long long v9;  // [bp-0x10]
    struct_2 *v10;  // [bp-0x8]

    v7 = v11;
    v12 = ptr3->field_128;
    v13 = ptr3;
    CFUtils__get_realDeltaTimeClamped(0);
    if (v12)
    {
        v14 = FixedTimeStepController__Update(v12, 0);
        if (!v13->field_20)
            return v14;
        v15 = v9;
        v16 = v10;
        v17 = v13;
    }
    else
    {
        vvar_232{r256|8b} = (int)&g_103b638;
        v15 = v12;
        v16 = v13;
        v17 = sub_f7db74();
    }
    v0 = v19;
    v1 = v20;
    v2 = vvar_112{r256|8b};
    v3 = v21;
    v4 = v22;
    v5 = v23;
    v6 = v24;
    v7 = v25;
    v8 = v26;
    v9 = v15;
    v10 = v16;
    ptr = v17;
    if (!(g_1fab1a5 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c("SB");
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef8a38);
        sub_f7d92c(&g_1ef9840);
        sub_f7d92c(&g_1ef98a8);
        sub_f7d92c(&g_1ef9868);
        sub_f7d92c(&g_1ef0c58);
        g_1fab1a5 = 1;
    }
    InputRig__CheckResolution(ptr, 0);
    v28 = ptr->field_3c;
    if (!ptr->field_74)
    {
        if (v28)
            v31 = ptr->field_40;
        else
            v31 = 0xbf800000;
        if (ptr->field_44)
        {
            if (!g_1fab1dd)
            {
                sub_f7d92c(&g_1eefb00);
                g_1fab1dd = 1;
            }
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v29 = Object__op_Inequality(g_1eefb00->field_b8->field_0, 0, 0);
            if (((char)v29 & 1))
            {
                if (!g_1fab1dd)
                {
                    v29 = sub_f7d92c(&g_1eefb00);
                    g_1fab1dd = 1;
                }
                if (!g_1eefb00->field_b8->field_0)
                    sub_f7db74(v29);
                if (g_1eefb00->field_b8->field_0->field_88 >= 1)
                {
                    v32 = ptr->field_48;
                    v33 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v31, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v31, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v31, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v31, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v31, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v31, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if ((char)v33 || (v34 = (unsigned long)arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v32, v31)) >> 5 & 3 | (unsigned long long)(CmpF(v32, v31) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v32, v31)) >> 5 & 3 | (unsigned long long)(CmpF(v32, v31) & 1)) & ((unsigned long long)(char)(CmpF(v32, v31)) >> 5 & 3 | (unsigned long long)(CmpF(v32, v31) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), !((char)v34)))
                        v31 = v32;
                }
            }
        }
        v35 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v31, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v31, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v31, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v31, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v31, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v31, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v35) && (CFUtils__get_realDeltaTimeClamped(0), v36 = ptr->field_70 + v32, ptr->field_70 = v36, v37 = (unsigned long)arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v36, v31)) >> 5 & 3 | (unsigned long long)(CmpF(v36, v31) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v36, v31)) >> 5 & 3 | (unsigned long long)(CmpF(v36, v31) & 1)) & ((unsigned long long)(char)(CmpF(v36, v31)) >> 5 & 3 | (unsigned long long)(CmpF(v36, v31) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), !((char)v37)))
        {
            ptr->field_74 = 1;
            goto LABEL_103b880;
        }
    }
    else if (!v28 && ptr->field_44)
    {
        if (!g_1fab1dd)
        {
            sub_f7d92c(&g_1eefb00);
            g_1fab1dd = 1;
        }
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v29 = Object__op_Inequality(g_1eefb00->field_b8->field_0, 0, 0);
        if (((char)v29 & 1))
        {
            if (!g_1fab1dd)
            {
                v29 = sub_f7d92c(&g_1eefb00);
                g_1fab1dd = 1;
            }
            if (!g_1eefb00->field_b8->field_0)
                sub_f7db74(v29);
            if (!g_1eefb00->field_b8->field_0->field_88 && (v30 = (unsigned int)ptr->field_74, ptr->field_70 = 0, ptr->field_74))
            {
                ptr->field_74 = 0;
LABEL_103b880:
                InputRig__SyncDisablingConditions(ptr, 0);
            }
        }
    }
    InputRig__ApplySwitches(ptr, 0);
    v29 = ptr->field_108;
    if (v29)
    {
        v38 = 0;
        do
        {
            if (*((int *)(v29 + 24)) <= v38)
            {
                v29 = ptr->field_110;
                if (v29 && (InputRig_TiltConfig__Update(v29, 0), v29 = ptr->field_118, v29 && (InputRig_MouseConfig__Update(v29, 0), v29 = ptr->field_120, v29 && (InputRig_ScrollWheelState__Update(v29, 0), v29 = ptr->field_78, v29 && (sub_1526478(v29, ptr, g_1ef98a8), v29 = ptr->field_80, v29)))))
                {
                    InputRig_AxisConfigCollection__ApplyKeyboardInput(v29, 0);
                    if (!g_1eeed00->field_e0)
                        sub_f7da5c(g_1eeed00);
                    if (!g_1fab1df)
                    {
                        sub_f7d92c(&g_1eeed00);
                        g_1fab1df = 1;
                    }
                    v39 = g_1eeed00;
                    if (!g_1eeed00->field_e0)
                    {
                        sub_f7da5c(g_1eeed00);
                        v39 = g_1eeed00;
                    }
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    flag = 0;
                    if (((char)Object__op_Equality(ptr, v39->field_b8->field_18, 0) & 1))
                    {
                        p = g_1ef0428->field_b8->field_0;
                        if (p)
                        {
                            v42 = p->field_40;
                            v43 = p->field_28;
                            p->field_18();
                        }
                    }
                    addr = ptr->field_30;
                    if (addr)
                    {
                        v45 = addr->field_40;
                        v46 = addr->field_28;
                        addr->field_18();
                    }
                    v29 = ptr->field_100;
                    if (v29)
                    {
                        sub_1526478(v29, ptr, g_1ef9840);
                        v29 = ptr->field_80;
                        if (v29)
                        {
                            sub_1526478(v29, ptr, g_1ef9868);
                            InputRig__UpdateKeyCodes(ptr);
                            v47 = InputRig__UpdateEmuTouches(ptr);
                            return InputRig__UpdateEmuTouches(ptr);
                        }
                        break;
                    }
                }
            }
        } while ((v29 = (long long)(unsigned long long)sub_14a30c0(), v29 && (TouchControl__UpdateControl(), v29 = ptr->field_108, v38 = (int)(v38 + 1), v29)));
    }
    sub_f7db74(v29);
}
```

## `InputRig.UpdateConfigs` — RVA `0xc3b638`

- Decompiled symbol: `InputRig_UpdateConfigs`
- Metadata signature: `private void UpdateConfigs() { }`
- Native interval: `1060` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x103b638: stp d9, d8, [sp, #-0x60]!
// 0x103b63c: str x30, [sp, #0x10]
// 0x103b640: stp x26, x25, [sp, #0x20]
// 0x103b644: stp x24, x23, [sp, #0x30]
// 0x103b648: stp x22, x21, [sp, #0x40]
// 0x103b64c: stp x20, x19, [sp, #0x50]
// 0x103b650: adrp x20, #0x1fab000
// 0x103b654: ldrb w8, [x20, #0x1a5]
// 0x103b658: mov x19, x0
// 0x103b65c: tbnz w8, #0, #0x103b6c8
// 0x103b660: adrp x0, #0x1e8c000
// 0x103b664: ldr x0, [x0, #0xe0]
// 0x103b668: bl #0xf7d92c
// 0x103b66c: adrp x0, #0x1e8c000
// 0x103b670: ldr x0, [x0, #0x498]
// 0x103b674: bl #0xf7d92c
// 0x103b678: adrp x0, #0x1e8c000
// 0x103b67c: ldr x0, [x0, #0x5a0]
// 0x103b680: bl #0xf7d92c
// 0x103b684: adrp x0, #0x1e8c000
// 0x103b688: ldr x0, [x0, #0x5a8]
// 0x103b68c: bl #0xf7d92c
// 0x103b690: adrp x0, #0x1e8c000
// 0x103b694: ldr x0, [x0, #0x600]
// 0x103b698: bl #0xf7d92c
// 0x103b69c: adrp x0, #0x1e8c000
// 0x103b6a0: ldr x0, [x0, #0x608]
// 0x103b6a4: bl #0xf7d92c
// 0x103b6a8: adrp x0, #0x1e8c000
// 0x103b6ac: ldr x0, [x0, #0x610]
// 0x103b6b0: bl #0xf7d92c
// 0x103b6b4: adrp x0, #0x1e8c000
// 0x103b6b8: ldr x0, [x0, #0xd8]
// 0x103b6bc: bl #0xf7d92c
// 0x103b6c0: mov w8, #1
// 0x103b6c4: strb w8, [x20, #0x1a5]
// 0x103b6c8: adrp x21, #0x1e8c000
// 0x103b6cc: ldr x21, [x21, #0xd8]
// 0x103b6d0: mov x0, x19
// 0x103b6d4: mov w1, wzr
// 0x103b6d8: bl #0x103bae8
// 0x103b6dc: ldrb w9, [x19, #0x74]
// 0x103b6e0: ldrb w8, [x19, #0x3c]
// 0x103b6e4: cbz w9, #0x103b794
// 0x103b6e8: cbnz w8, #0x103b88c
// 0x103b6ec: ldrb w8, [x19, #0x44]
// 0x103b6f0: cbz w8, #0x103b88c
// 0x103b6f4: adrp x22, #0x1fab000
// 0x103b6f8: ldrb w8, [x22, #0x1dd]
// 0x103b6fc: cbnz w8, #0x103b714
// 0x103b700: adrp x0, #0x1e8c000
// 0x103b704: ldr x0, [x0, #0x28]
// 0x103b708: bl #0xf7d92c
// 0x103b70c: mov w8, #1
// 0x103b710: strb w8, [x22, #0x1dd]
// 0x103b714: adrp x23, #0x1e8c000
// 0x103b718: ldr x23, [x23, #0x28]
// 0x103b71c: ldr x0, [x21]
// 0x103b720: ldr x8, [x23]
// 0x103b724: ldr w9, [x0, #0xe0]
// 0x103b728: ldr x8, [x8, #0xb8]
// 0x103b72c: ldr x20, [x8]
// 0x103b730: cbnz w9, #0x103b738
// 0x103b734: bl #0xf7da5c
// 0x103b738: mov x0, x20
// 0x103b73c: mov x1, xzr
// 0x103b740: mov x2, xzr
// 0x103b744: bl #0x1b94ac8
// 0x103b748: tbz w0, #0, #0x103b88c
// 0x103b74c: ldrb w8, [x22, #0x1dd]
// 0x103b750: cbnz w8, #0x103b768
// 0x103b754: adrp x0, #0x1e8c000
// 0x103b758: ldr x0, [x0, #0x28]
// 0x103b75c: bl #0xf7d92c
// 0x103b760: mov w8, #1
// 0x103b764: strb w8, [x22, #0x1dd]
// 0x103b768: ldr x8, [x23]
// 0x103b76c: ldr x8, [x8, #0xb8]
// 0x103b770: ldr x8, [x8]
// 0x103b774: cbz x8, #0x103ba58
// 0x103b778: ldr w8, [x8, #0x88]
// 0x103b77c: cbnz w8, #0x103b88c
// 0x103b780: ldrb w8, [x19, #0x74]
// 0x103b784: str wzr, [x19, #0x70]
// 0x103b788: cbz w8, #0x103b88c
// 0x103b78c: strb wzr, [x19, #0x74]
// 0x103b790: b #0x103b880
// 0x103b794: cbz w8, #0x103b7a0
// 0x103b798: ldr s8, [x19, #0x40]
// 0x103b79c: b #0x103b7a4
// 0x103b7a0: fmov s8, #-1.00000000
// 0x103b7a4: ldrb w8, [x19, #0x44]
// 0x103b7a8: cbz w8, #0x103b854
// 0x103b7ac: adrp x22, #0x1fab000
// 0x103b7b0: ldrb w8, [x22, #0x1dd]
// 0x103b7b4: cbnz w8, #0x103b7cc
// 0x103b7b8: adrp x0, #0x1e8c000
// 0x103b7bc: ldr x0, [x0, #0x28]
// 0x103b7c0: bl #0xf7d92c
// 0x103b7c4: mov w8, #1
// 0x103b7c8: strb w8, [x22, #0x1dd]
// 0x103b7cc: adrp x23, #0x1e8c000
// 0x103b7d0: ldr x23, [x23, #0x28]
// 0x103b7d4: ldr x0, [x21]
// 0x103b7d8: ldr x8, [x23]
// 0x103b7dc: ldr w9, [x0, #0xe0]
// 0x103b7e0: ldr x8, [x8, #0xb8]
// 0x103b7e4: ldr x20, [x8]
// 0x103b7e8: cbnz w9, #0x103b7f0
// 0x103b7ec: bl #0xf7da5c
// 0x103b7f0: mov x0, x20
// 0x103b7f4: mov x1, xzr
// 0x103b7f8: mov x2, xzr
// 0x103b7fc: bl #0x1b94ac8
// 0x103b800: tbz w0, #0, #0x103b854
// 0x103b804: ldrb w8, [x22, #0x1dd]
// 0x103b808: cbnz w8, #0x103b820
// 0x103b80c: adrp x0, #0x1e8c000
// 0x103b810: ldr x0, [x0, #0x28]
// 0x103b814: bl #0xf7d92c
// 0x103b818: mov w8, #1
// 0x103b81c: strb w8, [x22, #0x1dd]
// 0x103b820: ldr x8, [x23]
// 0x103b824: ldr x8, [x8, #0xb8]
// 0x103b828: ldr x8, [x8]
// 0x103b82c: cbz x8, #0x103ba58
// 0x103b830: ldr w8, [x8, #0x88]
// 0x103b834: cmp w8, #1
// 0x103b838: b.lt #0x103b854
// 0x103b83c: ldr s0, [x19, #0x48]
// 0x103b840: fcmp s8, #0.0
// 0x103b844: b.mi #0x103b850
// 0x103b848: fcmp s0, s8
// 0x103b84c: b.pl #0x103b854
// 0x103b850: mov v8.16b, v0.16b
// 0x103b854: fcmp s8, #0.0
// 0x103b858: b.le #0x103b88c
// 0x103b85c: ldr s9, [x19, #0x70]
// 0x103b860: mov x0, xzr
// 0x103b864: bl #0x105834c
// 0x103b868: fadd s0, s9, s0
// 0x103b86c: fcmp s0, s8
// 0x103b870: str s0, [x19, #0x70]
// 0x103b874: b.le #0x103b88c
// 0x103b878: mov w8, #1
// 0x103b87c: strb w8, [x19, #0x74]
// 0x103b880: mov x0, x19
// 0x103b884: mov w1, wzr
// 0x103b888: bl #0x103b3dc
// 0x103b88c: mov x0, x19
// 0x103b890: mov w1, wzr
// 0x103b894: bl #0x103bcd4
// 0x103b898: ldr x0, [x19, #0x108]
// 0x103b89c: cbz x0, #0x103ba58
// 0x103b8a0: adrp x26, #0x1e8c000
// 0x103b8a4: adrp x25, #0x1e8c000
// 0x103b8a8: adrp x24, #0x1e8c000
// 0x103b8ac: adrp x23, #0x1e8c000
// 0x103b8b0: adrp x22, #0x1e8c000
// 0x103b8b4: ldr x26, [x26, #0x5a8]
// 0x103b8b8: ldr x25, [x25, #0x608]
// 0x103b8bc: ldr x24, [x24, #0xe0]
// 0x103b8c0: ldr x23, [x23, #0x600]
// 0x103b8c4: ldr x22, [x22, #0x610]
// 0x103b8c8: mov w20, wzr
// 0x103b8cc: ldr w8, [x0, #0x18]
// 0x103b8d0: cmp w20, w8
// 0x103b8d4: b.ge #0x103b900
// 0x103b8d8: ldr x2, [x26]
// 0x103b8dc: mov w1, w20
// 0x103b8e0: bl #0x14a30c0
// 0x103b8e4: cbz x0, #0x103ba58
// 0x103b8e8: mov x1, xzr
// 0x103b8ec: bl #0x1052e2c
// 0x103b8f0: ldr x0, [x19, #0x108]
// 0x103b8f4: add w20, w20, #1
// 0x103b8f8: cbnz x0, #0x103b8cc
// 0x103b8fc: b #0x103ba58
// 0x103b900: ldr x0, [x19, #0x110]
// 0x103b904: cbz x0, #0x103ba58
// 0x103b908: mov x1, xzr
// 0x103b90c: bl #0x1042af8
// 0x103b910: ldr x0, [x19, #0x118]
// 0x103b914: cbz x0, #0x103ba58
// 0x103b918: mov x1, xzr
// 0x103b91c: bl #0x1043760
// 0x103b920: ldr x0, [x19, #0x120]
// 0x103b924: cbz x0, #0x103ba58
// 0x103b928: mov x1, xzr
// 0x103b92c: bl #0x1043098
// 0x103b930: ldr x0, [x19, #0x78]
// 0x103b934: cbz x0, #0x103ba58
// 0x103b938: ldr x2, [x25]
// 0x103b93c: mov x1, x19
// 0x103b940: bl #0x1526478
// 0x103b944: ldr x0, [x19, #0x80]
// 0x103b948: cbz x0, #0x103ba58
// 0x103b94c: mov x1, xzr
// 0x103b950: bl #0x1042048
// 0x103b954: ldr x0, [x24]
// 0x103b958: ldr w8, [x0, #0xe0]
// 0x103b95c: cbnz w8, #0x103b964
// 0x103b960: bl #0xf7da5c
// 0x103b964: adrp x20, #0x1fab000
// 0x103b968: ldrb w8, [x20, #0x1df]
// 0x103b96c: cbnz w8, #0x103b984
// 0x103b970: adrp x0, #0x1e8c000
// 0x103b974: ldr x0, [x0, #0xe0]
// 0x103b978: bl #0xf7d92c
// 0x103b97c: mov w8, #1
// 0x103b980: strb w8, [x20, #0x1df]
// 0x103b984: ldr x0, [x24]
// 0x103b988: ldr w8, [x0, #0xe0]
// 0x103b98c: cbnz w8, #0x103b998
// 0x103b990: bl #0xf7da5c
// 0x103b994: ldr x0, [x24]
// 0x103b998: ldr x8, [x21]
// 0x103b99c: ldr x9, [x0, #0xb8]
// 0x103b9a0: ldr w10, [x8, #0xe0]
// 0x103b9a4: ldr x20, [x9, #0x18]
// 0x103b9a8: cbnz w10, #0x103b9b4
// 0x103b9ac: mov x0, x8
// 0x103b9b0: bl #0xf7da5c
// 0x103b9b4: mov x0, x19
// 0x103b9b8: mov x1, x20
// 0x103b9bc: mov x2, xzr
// 0x103b9c0: bl #0x1b9568c
// 0x103b9c4: tbz w0, #0, #0x103b9f0
// 0x103b9c8: adrp x8, #0x1e8c000
// 0x103b9cc: ldr x8, [x8, #0x498]
// 0x103b9d0: ldr x8, [x8]
// 0x103b9d4: ldr x8, [x8, #0xb8]
// 0x103b9d8: ldr x8, [x8]
// 0x103b9dc: cbz x8, #0x103b9f0
// 0x103b9e0: ldr x9, [x8, #0x18]
// 0x103b9e4: ldr x0, [x8, #0x40]
// 0x103b9e8: ldr x1, [x8, #0x28]
// 0x103b9ec: blr x9
// 0x103b9f0: ldr x8, [x19, #0x30]
// 0x103b9f4: cbz x8, #0x103ba08
// 0x103b9f8: ldr x9, [x8, #0x18]
// 0x103b9fc: ldr x0, [x8, #0x40]
// 0x103ba00: ldr x1, [x8, #0x28]
// 0x103ba04: blr x9
// 0x103ba08: ldr x0, [x19, #0x100]
// 0x103ba0c: cbz x0, #0x103ba58
// 0x103ba10: ldr x2, [x23]
// 0x103ba14: mov x1, x19
// 0x103ba18: bl #0x1526478
// 0x103ba1c: ldr x0, [x19, #0x80]
// 0x103ba20: cbz x0, #0x103ba58
// 0x103ba24: ldr x2, [x22]
// 0x103ba28: mov x1, x19
// 0x103ba2c: bl #0x1526478
// 0x103ba30: mov x0, x19
// 0x103ba34: bl #0x103bd28
// 0x103ba38: mov x0, x19
// 0x103ba3c: ldp x20, x19, [sp, #0x50]
// 0x103ba40: ldp x22, x21, [sp, #0x40]
// 0x103ba44: ldp x24, x23, [sp, #0x30]
// 0x103ba48: ldp x26, x25, [sp, #0x20]
// 0x103ba4c: ldr x30, [sp, #0x10]
// 0x103ba50: ldp d9, d8, [sp], #0x60
// 0x103ba54: b #0x103bdf4
// 0x103ba58: bl #0xf7db74
```

## `InputRig.ResetEmuTouches` — RVA `0xc3ba5c`

- Decompiled symbol: `InputRig_ResetEmuTouches`
- Metadata signature: `private void ResetEmuTouches() { }`
- Native interval: `140` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

typedef struct struct_1 {
    char padding_0[352];
    struct struct_0 *field_160;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern long long g_1ef90f8;
extern long long g_1ef9100;
extern char g_1fab1da;

struct_2 * InputRig_ResetEmuTouches(struct_1 *ptr)
{
    struct_0 *v0;  // x0
    int v1;  // w20
    unsigned long v2;  // x0

    if (!(g_1fab1da & 1))
    {
        sub_f7d92c(&g_1ef90f8);
        sub_f7d92c(&g_1ef9100);
        g_1fab1da = 1;
    }
    v0 = ptr->field_160;
    if (v0)
    {
        v1 = 0;
        do
        {
            if (v0->field_18 <= v1)
                return v0;
        } while ((v0 = (struct_0 *)(unsigned long long)sub_14a30c0(), v0 && (InputRig_EmulatedTouchState__Reset(), v0 = (struct_0 *)ptr->field_160, v1 = (int)(v1 + 1), v0)));
    }
    v2 = sub_f7db74(v0);
    return sub_f7db74(v0);
}
```

## `InputRig.CheckResolution` — RVA `0xc3bae8`

- Decompiled symbol: `InputRig_CheckResolution`
- Metadata signature: `private void CheckResolution(bool forceRecalc = false) { }`
- Native interval: `448` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eee870;
extern struct_1 *g_1eeed10;
extern char g_1fab1cd;

void InputRig_CheckResolution(unsigned int *ptr, unsigned long long a1)
{
    struct_1 *v0;  // x0
    unsigned int v1;  // s0
    unsigned int v10;  // s2
    unsigned int v11;  // s0
    unsigned int v12;  // s3
    unsigned long v13;  // 4125
    unsigned int v14;  // s1
    unsigned int v15;  // s3
    unsigned int v16;  // 4103
    unsigned long v17;  // 4135
    unsigned long v18;  // 4129
    unsigned int v19;  // s0
    unsigned int v2;  // s8
    unsigned int v20;  // s4
    unsigned int v21;  // s2
    unsigned int v3;  // w0
    unsigned int v4;  // s0
    unsigned long v5;  // 4129
    unsigned int v6;  // 4098
    unsigned long v7;  // 4111
    unsigned long v9;  // 4125

    if (!(g_1fab1cd & 1))
    {
        sub_f7d92c(&g_1eee870);
        sub_f7d92c(&g_1eeed10);
        g_1fab1cd = 1;
    }
    v0 = g_1eeed10;
    if (!g_1eeed10->field_e0)
        v0 = sub_f7da5c(g_1eeed10);
    CFScreen__get_dpcm(v0, a1);
    v2 = v1;
    if (!((char)a1 & 1) && ptr[85] && ptr[85] == Screen__get_width(0))
    {
        v3 = Screen__get_height(0);
        if (ptr[86] == v3)
        {
            v4 = ptr[87];
            v5 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v4, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v4, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v5))
            {
                v6 = CmpF(v4, v2);
                v7 = (((CmpF(v4, v2) >> 5 & 3 | CmpF(v4, v2) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1;
                if ((char)((v7 - ((CmpF(v4, v2) >> 5 & 3 | CmpF(v4, v2) & 1) & (v6 >> 5 & 3 | CmpF(v4, v2) & 1) >> 1 & 1)) * 0x10000000 >> 30))
                    return;
            }
        }
    }
    ptr[85] = Screen__get_width(0);
    ptr[86] = Screen__get_height(0);
    ptr[87] = v2;
    if (!g_1eee870->field_e0)
        sub_f7da5c(g_1eee870);
    v9 = arm64g_calculate_condition(144, (((((unsigned long long)(char)(CmpF(v2, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v2, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v9 || !((char)Application__get_isMobilePlatform(0) & 1))
    {
        v10 = [D] unsupported_Iop_SqrtF32();
        v2 = v10 / (ptr[26] * 1076006748);
    }
    v11 = 0;
    v12 = 0;
    v13 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v2, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v2, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v13))
        v12 = ptr[23] / (v2 * ptr[24]);
    v14 = ptr[23];
    ptr[83] = v12;
    v15 = 0x3f800000 / v14;
    v16 = CmpF(v14, 0.0);
    v17 = (((CmpF(v14, 0.0) >> 5 & 3 | CmpF(v14, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1;
    if ((char)((v17 - ((CmpF(v14, 0.0) >> 5 & 3 | CmpF(v14, 0.0) & 1) & (v16 >> 5 & 3 | CmpF(v14, 0.0) & 1) >> 1 & 1)) * 0x10000000 >> 30))
        v15 = 0;
    ptr[82] = v15;
    v18 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v2, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v2, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v18))
        v11 = 0x3f800000 / (v2 * ptr[24]);
    ptr[84] = v11;
    v19 = ptr[27];
    v20 = v14 / ptr[25];
    v21 = 0x3f800000 / ptr[25];
    ptr[77] = v20;
    ptr[78] = v21;
    ptr[79] = v20;
    ptr[80] = v14 / v19;
    ptr[81] = 0x3f800000 / v19;
    return;
}
```

## `InputRig.PutTouchControlsToSleep` — RVA `0xc3bca8`

- Decompiled symbol: `InputRig_PutTouchControlsToSleep`
- Metadata signature: `public void PutTouchControlsToSleep() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[116];
    char field_74;
} struct_0;

long long InputRig_PutTouchControlsToSleep(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_74 = 1;
    v0 = InputRig__SyncDisablingConditions(ptr, 0);
    return InputRig__SyncDisablingConditions(ptr, 0);
}
```

## `InputRig.WakeTouchControlsUp` — RVA `0xc3bcb8`

- Decompiled symbol: `InputRig_WakeTouchControlsUp`
- Metadata signature: `public void WakeTouchControlsUp() { }`
- Native interval: `28` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_Recovered` matched 2 offsets against `InputRig` metadata (confidence 1.00).

```c
typedef struct InputRig_Recovered {
    char padding_0[112];
    unsigned int elapsedSinceLastTouch;
    char touchControlsSleeping;
} InputRig_Recovered;

struct_0 * InputRig_WakeTouchControlsUp(struct_0 *ptr)
{
    unsigned int v0;  // w8
    long long v1;  // x0

    v0 = ptr->field_74;
    ptr->field_70 = 0;
    if (!v0)
        return ptr;
    ptr->field_74 = 0;
    v1 = InputRig__SyncDisablingConditions(ptr, 0);
    return InputRig__SyncDisablingConditions(ptr, 0);
}
```

## `InputRig.ApplySwitches` — RVA `0xc3bcd4`

- Decompiled symbol: `InputRig_ApplySwitches`
- Metadata signature: `public void ApplySwitches(bool skipAnim) { }`
- Native interval: `84` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_Recovered` matched 2 offsets against `InputRig` metadata (confidence 1.00).

```c
typedef struct InputRig_Recovered {
    char padding_0[40];
    struct struct_0 *onSwitchesChanged;
    char padding_30[200];
    struct struct_1 *rigSwitches;
} InputRig_Recovered;

typedef struct struct_1 {
    char padding_0[32];
    char field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

struct_2 * InputRig_ApplySwitches(struct_2 *idx, unsigned int a1)
{
    struct_2 *v0;  // x0

    if (idx->field_f8)
    {
        if (idx->field_f8->field_20)
        {
            v0 = InputRig__SyncDisablingConditions(idx, a1 & 1);
            if (idx->field_f8)
            {
                idx->field_f8->field_20 = 0;
                if (!idx->field_28)
                    return v0;
                goto idx->field_28->field_18;
            }
        }
        else
        {
            return idx;
        }
    }
    sub_f7db74();
}
```

## `InputRig.UpdateKeyCodes` — RVA `0xc3bd28`

- Decompiled symbol: `InputRig_UpdateKeyCodes`
- Metadata signature: `private void UpdateKeyCodes() { }`
- Native interval: `204` bytes
- Result: `pseudocode`

```c
unsigned long long InputRig_UpdateKeyCodes(void* ptr)
{
    long long v0;  // x21
    void* ptr3;  // x0
    unsigned long v2;  // x1
    void* p;  // x20
    unsigned long v4;  // x1
    void* addr;  // x22
    unsigned long v6;  // x0
    unsigned long long v7;  // x0
    char v8;  // x8
    char v9;  // x9

    v0 = (long long)ptr[144];
    ptr3 = ptr + 144;
    v2 = (long long)ptr[152];
    p = ptr + 152;
    *((unsigned long *)ptr3) = v2;
    sub_f7d8d0(ptr3, v2);
    v4 = (long long)ptr[160];
    addr = ptr + 160;
    *((unsigned long *)p) = v4;
    sub_f7d8d0(p, v4);
    *((long long *)addr) = v0;
    sub_f7d8d0(addr, v0);
    v6 = *((long long *)addr);
    if (v6)
    {
        BitArray__SetAll(v6, 0, 0);
        v6 = (long long)ptr[168];
        if (v6)
        {
            BitArray__And(v6, (long long)ptr[152], 0);
            v6 = (long long)ptr[168];
            if (v6)
            {
                BitArray__Not(v6, 0);
                v6 = *((long long *)p);
                if (v6)
                {
                    BitArray__And(v6, (long long)ptr[168], 0);
                    v6 = (long long)ptr[168];
                    if (v6)
                    {
                        v7 = BitArray__Not(v6, 0);
                        v8 = (char)ptr[184];
                        v9 = (char)ptr[185];
                        *((unsigned short *)&ptr[184]) = 0;
                        *((char *)&ptr[187]) = v8;
                        *((char *)&ptr[186]) = v9;
                        return v7;
                    }
                }
            }
        }
    }
    sub_f7db74(v6);
}
```

## `InputRig.UpdateEmuTouches` — RVA `0xc3bdf4`

- Decompiled symbol: `InputRig_UpdateEmuTouches`
- Metadata signature: `private void UpdateEmuTouches() { }`
- Native interval: `352` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_Recovered` matched 3 offsets against `InputRig` metadata (confidence 1.00).

```c
typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct InputRig_Recovered {
    char padding_0[352];
    struct struct_0 *emuTouches;
    struct struct_1 *emuTouchesOrdered;
    char padding_170[8];
    char emuOutputTouchesDirty;
} InputRig_Recovered;

typedef struct struct_1 {
    char padding_0[16];
    unsigned long long field_10;
    int field_18;
    unsigned int field_1c;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

typedef struct struct_4 {
    char padding_0[32];
    long long field_20;
} struct_4;

extern long long g_1ef90e8;
extern long long g_1ef90f0;
extern long long g_1ef90f8;
extern long long g_1ef9100;
extern char g_1fab1db;

struct_3 * InputRig_UpdateEmuTouches(struct_2 *ptr)
{
    struct_1 *p;  // x8
    int v1;  // w2
    struct_4 *ptr3;  // x8
    unsigned int v2;  // w9
    struct_0 *v3;  // x0
    int v4;  // w20
    long long v5;  // x0
    long long v6;  // x21
    struct_1 *addr;  // x0
    unsigned long long v8;  // x8
    unsigned long v9;  // x10

    if (!(g_1fab1db & 1))
    {
        sub_f7d92c(&g_1ef90e8);
        sub_f7d92c(&g_1ef90f0);
        sub_f7d92c(&g_1ef90f8);
        sub_f7d92c(&g_1ef9100);
        g_1fab1db = 1;
    }
    p = ptr->field_168;
    if (p)
    {
        v1 = p->field_18;
        v2 = p->field_1c + 1;
        p->field_18 = 0;
        p->field_1c = v2;
        if (v1 >= 1)
            Array__Clear(p->field_10, 0);
        v3 = ptr->field_160;
        if (v3)
        {
            v4 = 0;
            do
            {
                if (v3->field_18 <= v4)
                {
                    ptr->field_178 = 1;
                    return v3;
                }
                v5 = sub_14a30c0();
                if (!v5)
                    break;
                v6 = v5;
                InputRig_EmulatedTouchState__Update();
                if (!(InputRig_EmulatedTouchState__IsActive(v6, 0) & 1))
                    continue;
                addr = ptr->field_168;
                if (!addr || !((v8 = addr->field_10, addr->field_1c = addr->field_1c + 1, v8)))
                    break;
                v9 = addr->field_18;
                if (*((int *)(v8 + 24)) > (unsigned int)v9)
                {
                    ptr3 = v8 + v9 * 8;
                    addr->field_18 = (unsigned int)v9 + 1;
                    ptr3->field_20 = v6;
                    sub_f7d8d0((struct struct_4 *)&ptr3->field_20, v6);
                }
                else
                {
                    sub_14a3390();
                }
            } while ((v3 = (struct_0 *)ptr->field_160, v4 = (int)(v4 + 1), v3));
        }
    }
    v3 = sub_f7db74();
    ptr->field_178 = 1;
    return v3;
}
```

## `InputRig.GetSourceKeyState` — RVA `0xc3bf54`

- Decompiled symbol: `InputRig_GetSourceKeyState`
- Metadata signature: `public static bool GetSourceKeyState(KeyCode key) { }`
- Native interval: `128` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed00;
extern char g_1fab1a7;

unsigned int InputRig_GetSourceKeyState(unsigned int a0)
{
    unsigned long long v0;  // x0

    if (!(g_1fab1a7 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab1a7 = 1;
    }
    if (!a0)
        return 0;
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    v0 = CF2Input__IsInMobileMode();
    if (6 < a0 - 323 || !((char)v0 & 1))
        return Input__GetKey();
    return 0;
    return Input__GetKey();
}
```

## `InputRig.IsMouseKeyCode` — RVA `0xc3bfd4`

- Decompiled symbol: `InputRig_IsMouseKeyCode`
- Metadata signature: `public static bool IsMouseKeyCode(KeyCode key) { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
unsigned long long InputRig_IsMouseKeyCode(unsigned int a0)
{
    if (7 > a0 - 323)
        return 1;
    return 0;
}
```

## `InputRig.AddControl` — RVA `0xc3bfe4`

- Decompiled symbol: `InputRig_AddControl`
- Metadata signature: `public void AddControl(TouchControl c) { }`
- Native interval: `200` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[264];
    struct struct_0 *field_108;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_0;

extern long long g_1ef89f0;
extern char g_1fab1a8;

long long InputRig_AddControl(struct_1 *p, unsigned long a1)
{
    long long v0;  // x0
    struct_0 *ptr;  // x0
    unsigned long long v2;  // x8
    unsigned long v3;  // x10
    long long v4;  // x0
    long long v5;  // x0

    if (!(g_1fab1a8 & 1))
    {
        sub_f7d92c(&g_1ef89f0);
        g_1fab1a8 = 1;
    }
    v0 = ComponentBase__CanBeUsed(p, 0);
    if (!((char)v0 & 1))
        return v0;
    ptr = p->field_108;
    if (ptr)
    {
        v2 = ptr->field_10;
        ptr->field_1c = ptr->field_1c + 1;
        if (v2)
        {
            v3 = ptr->field_18;
            if (*((int *)(v2 + 24)) <= (unsigned int)v3)
            {
                v5 = sub_14a3390();
                return sub_14a3390();
            }
            ptr->field_18 = (unsigned int)v3 + 1;
            *((unsigned long *)(v2 + v3 * 8 + 32)) = a1;
            v4 = sub_f7d8d0();
            return sub_f7d8d0();
        }
    }
    sub_f7db74(ptr);
}
```

## `InputRig.RemoveControl` — RVA `0xc3c0ac`

- Decompiled symbol: `InputRig_RemoveControl`
- Metadata signature: `public void RemoveControl(TouchControl c) { }`
- Native interval: `112` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[264];
    unsigned long long field_108;
} struct_0;

extern long long g_1ef8a20;
extern char g_1fab1a9;

long long InputRig_RemoveControl(struct_0 *a0, unsigned long a1)
{
    long long v0;  // x0

    if (!(g_1fab1a9 & 1))
    {
        sub_f7d92c(&g_1ef8a20);
        g_1fab1a9 = 1;
    }
    v0 = ComponentBase__CanBeUsed(a0, 0);
    if (!((char)v0 & 1))
    {
        return v0;
    }
    else if (!a0->field_108)
    {
        return a0->field_108;
    }
}
```

## `InputRig.GetTouchControls` — RVA `0xc3c11c`

- Decompiled symbol: `InputRig_GetTouchControls`
- Metadata signature: `public List<TouchControl> GetTouchControls() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[264];
    unsigned long long field_108;
} struct_0;

long long InputRig_GetTouchControls(struct_0 *a0)
{
    return a0->field_108;
}
```

## `InputRig.FindTouchControl` — RVA `0xc3c124`

- Decompiled symbol: `InputRig_FindTouchControl`
- Metadata signature: `public TouchControl FindTouchControl(string name) { }`
- Native interval: `228` bytes
- Result: `pseudocode`

```c
extern long long g_1eedbe0;
extern long long g_1ef3308;
extern long long g_1ef8a08;
extern char g_1fab1aa;

long long InputRig_FindTouchControl(unsigned long a0, unsigned long a1)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]
    unsigned long long v5;  // [bp-0x8]

    v0 = v6;
    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    if (!(g_1fab1aa & 1))
    {
        sub_f7d92c(&g_1ef8a08);
        sub_f7d92c(&g_1eedbe0);
        sub_f7d92c("'");
        sub_f7d92c(&g_1ef3308);
        g_1fab1aa = 1;
    }
    InputRig_c__DisplayClass90_0__ctor(sub_f7db70(g_1ef3308), 0); /* do not return */
}
```

## `InputRig.AreTouchControlsHiddenManually` — RVA `0xc3c208`

- Decompiled symbol: `InputRig_AreTouchControlsHiddenManually`
- Metadata signature: `public bool AreTouchControlsHiddenManually() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[304];
    char field_130;
} struct_0;

long long InputRig_AreTouchControlsHiddenManually(struct_0 *a0)
{
    return a0->field_130;
}
```

## `InputRig.AreTouchControlsSleeping` — RVA `0xc3c210`

- Decompiled symbol: `InputRig_AreTouchControlsSleeping`
- Metadata signature: `public bool AreTouchControlsSleeping() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[116];
    char field_74;
} struct_0;

long long InputRig_AreTouchControlsSleeping(struct_0 *a0)
{
    return a0->field_74;
}
```

## `InputRig.AreTouchControlsVisible` — RVA `0xc3c218`

- Decompiled symbol: `InputRig_AreTouchControlsVisible`
- Metadata signature: `public bool AreTouchControlsVisible() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
unsigned long long InputRig_AreTouchControlsVisible(char *a0)
{
    if (a0[116])
    {
        return 0;
    }
    else if (a0[304])
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `InputRig.IsTiltAvailable` — RVA `0xc3c238`

- Decompiled symbol: `InputRig_IsTiltAvailable`
- Metadata signature: `public static bool IsTiltAvailable() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
int InputRig_IsTiltAvailable(void)
{
    return TiltState__IsAvailable(0);
}
```

## `InputRig.IsTiltCalibrated` — RVA `0xc3c240`

- Decompiled symbol: `InputRig_IsTiltCalibrated`
- Metadata signature: `public bool IsTiltCalibrated() { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[272];
    struct struct_1 *field_110;
} struct_2;

typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[88];
    char field_58;
} struct_0;

long long InputRig_IsTiltCalibrated(struct_2 *a0)
{
    if (a0->field_110 && a0->field_110->field_18)
        return a0->field_110->field_18->field_58;
    sub_f7db74();
}
```

## `InputRig.ResetTilt` — RVA `0xc3c264`

- Decompiled symbol: `InputRig_ResetTilt`
- Metadata signature: `public void ResetTilt() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[272];
    long long field_110;
} struct_0;

long long InputRig_ResetTilt(struct_0 *a0)
{
    unsigned long long v0;  // x0

    if (a0->field_110)
    {
        v0 = InputRig_TiltConfig__Reset(a0->field_110, 0);
        return InputRig_TiltConfig__Reset(a0->field_110, 0);
    }
    sub_f7db74(0);
}
```

## `InputRig.GetSwitchState` — RVA `0xc3c280`

- Decompiled symbol: `InputRig_GetSwitchState`
- Metadata signature: `public bool GetSwitchState(string name, ref int cachedId, bool fallbackVal) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[248];
    long long field_f8;
} struct_0;

long long InputRig_GetSwitchState(struct_0 *a0, unsigned long a1, unsigned long a2, unsigned long a3)
{
    unsigned long long v0;  // x0

    if (a0->field_f8)
    {
        v0 = InputRig_RigSwitchCollection__GetSwitchState(a0->field_f8);
        return InputRig_RigSwitchCollection__GetSwitchState(a0->field_f8);
    }
    sub_f7db74(0);
}
```

## `InputRig.GetSwitchState` — RVA `0xc3c2a0`

- Decompiled symbol: `InputRig_GetSwitchState`
- Metadata signature: `public bool GetSwitchState(string name, bool fallbackVal) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[248];
    long long field_f8;
} struct_0;

long long InputRig_GetSwitchState(struct_0 *a0, unsigned long a1, unsigned long a2)
{
    unsigned long long v0;  // x0

    if (a0->field_f8)
    {
        v0 = InputRig_RigSwitchCollection__GetSwitchState(a0->field_f8);
        return InputRig_RigSwitchCollection__GetSwitchState(a0->field_f8);
    }
    sub_f7db74(0);
}
```

## `InputRig.SetSwitchState` — RVA `0xc3c2c0`

- Decompiled symbol: `InputRig_SetSwitchState`
- Metadata signature: `public void SetSwitchState(string name, ref int cachedId, bool state) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[248];
    long long field_f8;
} struct_0;

long long InputRig_SetSwitchState(struct_0 *a0, unsigned long a1, unsigned long a2, unsigned long a3)
{
    unsigned long long v0;  // x0

    if (a0->field_f8)
    {
        v0 = InputRig_RigSwitchCollection__SetSwitchState(a0->field_f8);
        return InputRig_RigSwitchCollection__SetSwitchState(a0->field_f8);
    }
    sub_f7db74(0);
}
```

## `InputRig.SetSwitchState` — RVA `0xc3c2e0`

- Decompiled symbol: `InputRig_SetSwitchState`
- Metadata signature: `public void SetSwitchState(string name, bool state) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[248];
    long long field_f8;
} struct_0;

long long InputRig_SetSwitchState(struct_0 *a0, unsigned long a1, unsigned long a2)
{
    unsigned long long v0;  // x0

    if (a0->field_f8)
    {
        v0 = InputRig_RigSwitchCollection__SetSwitchState(a0->field_f8);
        return InputRig_RigSwitchCollection__SetSwitchState(a0->field_f8);
    }
    sub_f7db74(0);
}
```

## `InputRig.SetAllSwitches` — RVA `0xc3c300`

- Decompiled symbol: `InputRig_SetAllSwitches`
- Metadata signature: `public void SetAllSwitches(bool state) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[248];
    long long field_f8;
} struct_0;

long long InputRig_SetAllSwitches(struct_0 *a0, unsigned int a1)
{
    unsigned long long v0;  // x0

    if (a0->field_f8)
    {
        v0 = InputRig_RigSwitchCollection__SetAll(a0->field_f8, a1 & 1, 0);
        return InputRig_RigSwitchCollection__SetAll(a0->field_f8, a1 & 1, 0);
    }
    sub_f7db74(0);
}
```

## `InputRig.ResetSwitch` — RVA `0xc3c320`

- Decompiled symbol: `InputRig_ResetSwitch`
- Metadata signature: `public void ResetSwitch(string name, ref int cachedId) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[248];
    long long field_f8;
} struct_0;

long long InputRig_ResetSwitch(struct_0 *a0, unsigned long a1, unsigned long a2)
{
    unsigned long long v0;  // x0

    if (a0->field_f8)
    {
        v0 = InputRig_RigSwitchCollection__ResetSwitch(a0->field_f8);
        return InputRig_RigSwitchCollection__ResetSwitch(a0->field_f8);
    }
    sub_f7db74(0);
}
```

## `InputRig.ResetSwitch` — RVA `0xc3c33c`

- Decompiled symbol: `InputRig_ResetSwitch`
- Metadata signature: `public void ResetSwitch(string name) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[248];
    long long field_f8;
} struct_0;

long long InputRig_ResetSwitch(struct_0 *a0, unsigned long a1, unsigned long a2)
{
    unsigned long long v0;  // x0

    if (a0->field_f8)
    {
        v0 = InputRig_RigSwitchCollection__ResetSwitch(a0->field_f8);
        return InputRig_RigSwitchCollection__ResetSwitch(a0->field_f8);
    }
    sub_f7db74(0);
}
```

## `InputRig.IsSwitchDefined` — RVA `0xc3c358`

- Decompiled symbol: `InputRig_IsSwitchDefined`
- Metadata signature: `public bool IsSwitchDefined(string name, ref int cachedId) { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[248];
    long long field_f8;
} struct_0;

extern long long g_1ef9880;
extern char g_1fab1ad;

unsigned long long InputRig_IsSwitchDefined(struct_0 *a0, long long a1, long long a2)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x30]

    v0 = v1;
    if (!(g_1fab1ad & 1))
    {
        sub_f7d92c(&g_1ef9880);
        g_1fab1ad = 1;
    }
    if (a0->field_f8)
    {
        if (!sub_15264f8(a0->field_f8, a1, a2, g_1ef9880))
            return 0;
        return 1;
    }
    sub_f7db74(0);
}
```

## `InputRig.IsSwitchDefined` — RVA `0xc3c3cc`

- Decompiled symbol: `InputRig_IsSwitchDefined`
- Metadata signature: `public bool IsSwitchDefined(string name) { }`
- Native interval: `100` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[248];
    long long field_f8;
} struct_0;

extern long long g_1ef9878;
extern char g_1fab1ae;

unsigned long long InputRig_IsSwitchDefined(struct_0 *a0, long long a1, unsigned long a2)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x21
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]

    v0 = v2;
    v1 = v3;
    if (!(g_1fab1ae & 1))
    {
        sub_f7d92c(&g_1ef9878);
        g_1fab1ae = 1;
    }
    if (a0->field_f8)
    {
        if (!sub_1526618(a0->field_f8, a1, g_1ef9878))
            return 0;
        return 1;
    }
    sub_f7db74(0);
}
```

## `InputRig.IsAxisDefined` — RVA `0xc3c430`

- Decompiled symbol: `InputRig_IsAxisDefined`
- Metadata signature: `public bool IsAxisDefined(string name, ref int cachedId) { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[128];
    long long field_80;
} struct_0;

extern long long g_1ef9858;
extern char g_1fab1af;

unsigned long long InputRig_IsAxisDefined(struct_0 *a0, long long a1, long long a2)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x30]

    v0 = v1;
    if (!(g_1fab1af & 1))
    {
        sub_f7d92c(&g_1ef9858);
        g_1fab1af = 1;
    }
    if (a0->field_80)
    {
        if (!sub_15264f8(a0->field_80, a1, a2, g_1ef9858))
            return 0;
        return 1;
    }
    sub_f7db74(0);
}
```

## `InputRig.IsAxisDefined` — RVA `0xc3c4a4`

- Decompiled symbol: `InputRig_IsAxisDefined`
- Metadata signature: `public bool IsAxisDefined(string name) { }`
- Native interval: `100` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[128];
    long long field_80;
} struct_0;

extern long long g_1ef9850;
extern char g_1fab1b0;

unsigned long long InputRig_IsAxisDefined(struct_0 *a0, long long a1)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x21
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]

    v0 = v2;
    v1 = v3;
    if (!(g_1fab1b0 & 1))
    {
        sub_f7d92c(&g_1ef9850);
        g_1fab1b0 = 1;
    }
    if (a0->field_80)
    {
        if (!sub_1526618(a0->field_80, a1, g_1ef9850))
            return 0;
        return 1;
    }
    sub_f7db74(0);
}
```

## `InputRig.NameToKeyCode` — RVA `0xc3c508`

- Decompiled symbol: `InputRig_NameToKeyCode`
- Metadata signature: `public static KeyCode NameToKeyCode(string keyName) { }`
- Native interval: `4032` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

extern long long g_1f064e0;
extern long long g_1f06bf0;
extern long long g_1f07148;
extern long long g_1f07550;
extern long long g_1f075e0;
extern long long g_1f07db8;
extern long long g_1f09228;
extern long long g_1f09230;
extern long long g_1f09238;
extern long long g_1f09b98;
extern long long g_1f0a1f0;
extern long long g_1f0a1f8;
extern long long g_1f0a200;
extern long long g_1f0a208;
extern long long g_1f0a210;
extern long long g_1f0a218;
extern long long g_1f0a220;
extern long long g_1f0a228;
extern long long g_1f0a230;
extern long long g_1f0a238;
extern long long g_1f0a240;
extern long long g_1f0a248;
extern long long g_1f0bb88;
extern long long g_1f0bb90;
extern long long g_1f0bb98;
extern long long g_1f0bba0;
extern long long g_1f0bbe0;
extern long long g_1f0bc60;
extern long long g_1f0bc78;
extern long long g_1f0bc80;
extern long long g_1f0bc88;
extern long long g_1f0bc90;
extern long long g_1f0bf00;
extern long long g_1f0cd58;
extern long long g_1f0cd60;
extern long long g_1f0cd68;
extern long long g_1f0cd70;
extern long long g_1f0cf08;
extern long long g_1f0cf10;
extern long long g_1f0d198;
extern long long g_1f0d1a0;
extern long long g_1f0d1a8;
extern long long g_1f0d1b0;
extern long long g_1f0d238;
extern long long g_1f0d628;
extern long long g_1f0d640;
extern long long g_1f0d648;
extern long long g_1f0d650;
extern long long g_1f0d658;
extern long long g_1f10078;
extern long long g_1f100b0;
extern long long g_1f11078;
extern long long g_1f11d88;
extern long long g_1f120e0;
extern long long g_1f12408;
extern long long g_1f12468;
extern long long g_1f12470;
extern long long g_1f13c58;
extern long long g_1f13c60;
extern long long g_1f13c68;
extern long long g_1f13c70;
extern long long g_1f13c78;
extern long long g_1f14598;
extern long long g_1f145f0;
extern long long g_1f145f8;
extern long long g_1f14928;
extern long long g_1f14a30;
extern long long g_1f15660;
extern char g_1fab1dc;

unsigned long long InputRig_NameToKeyCode(struct_0 *a0)
{
    unsigned short v0;  // x0
    unsigned long long v1;  // x0
    unsigned long v2;  // 4114
    unsigned long long v3;  // x0

    if (!(g_1fab1dc & 1))
    {
        sub_f7d92c(&g_1f0a1f8);
        sub_f7d92c(&g_1f145f8);
        sub_f7d92c(&g_1f0bc90);
        sub_f7d92c(&g_1f11078);
        sub_f7d92c(&g_1f13c60);
        sub_f7d92c(&g_1f10078);
        sub_f7d92c(&g_1f0cd70);
        sub_f7d92c(&g_1f0cd58);
        sub_f7d92c(&g_1f0d648);
        sub_f7d92c(&g_1f0cf08);
        sub_f7d92c(&g_1f15660);
        sub_f7d92c(&g_1f0d1a0);
        sub_f7d92c(&g_1f0a220);
        sub_f7d92c(&g_1f14a30);
        sub_f7d92c(&g_1f064e0);
        sub_f7d92c(&g_1f0a210);
        sub_f7d92c(&g_1f14598);
        sub_f7d92c("E:");
        sub_f7d92c(&g_1f0bb98);
        sub_f7d92c(&g_1f0bc88);
        sub_f7d92c(&g_1f0a238);
        sub_f7d92c(&g_1f09b98);
        sub_f7d92c(&g_1f06bf0);
        sub_f7d92c("U%");
        sub_f7d92c(&g_1f0bb88);
        sub_f7d92c(&g_1f09228);
        sub_f7d92c("G\t");
        sub_f7d92c(&g_1f120e0);
        sub_f7d92c(&g_1f0d198);
        sub_f7d92c("I\t");
        sub_f7d92c("E\t");
        sub_f7d92c(&g_1f09230);
        sub_f7d92c(&g_1f0a208);
        sub_f7d92c(&g_1f0cd60);
        sub_f7d92c(&g_1f0cf10);
        sub_f7d92c(&g_1f12408);
        sub_f7d92c(&g_1f0d628);
        sub_f7d92c(&g_1f0d658);
        sub_f7d92c(&g_1f0d650);
        sub_f7d92c(&g_1f0bba0);
        sub_f7d92c(&g_1f0bbe0);
        sub_f7d92c(&g_1f0a248);
        sub_f7d92c(&g_1f11d88);
        sub_f7d92c("C\t");
        sub_f7d92c(&g_1f0d1b0);
        sub_f7d92c(&g_1f075e0);
        sub_f7d92c("'5");
        sub_f7d92c("[;");
        sub_f7d92c(&g_1f0cd68);
        sub_f7d92c(&g_1f0d640);
        sub_f7d92c(&g_1f13c58);
        sub_f7d92c(&g_1f07db8);
        sub_f7d92c(&g_1f0bc80);
        sub_f7d92c(&g_1f0bc60);
        sub_f7d92c(&g_1f13c70);
        sub_f7d92c(&g_1f0a230);
        sub_f7d92c(&g_1f0d238);
        sub_f7d92c("5,");
        sub_f7d92c(&g_1f145f0);
        sub_f7d92c(&g_1f0a218);
        sub_f7d92c(&g_1f09238);
        sub_f7d92c(&g_1f0a228);
        sub_f7d92c(&g_1f07148);
        sub_f7d92c(&g_1f0d1a8);
        sub_f7d92c(&g_1f0a1f0);
        sub_f7d92c(&g_1f0a200);
        sub_f7d92c(&g_1f12470);
        sub_f7d92c(&g_1f0a240);
        sub_f7d92c(&g_1f0bf00);
        sub_f7d92c(&g_1f14928);
        sub_f7d92c("3'");
        sub_f7d92c(")5");
        sub_f7d92c("?:");
        sub_f7d92c(&g_1f100b0);
        sub_f7d92c(&g_1f0bc78);
        sub_f7d92c(&g_1f13c78);
        sub_f7d92c(&g_1f13c68);
        sub_f7d92c(&g_1f12468);
        sub_f7d92c(&g_1f07550);
        sub_f7d92c(").");
        sub_f7d92c(&g_1f0bb90);
        g_1fab1dc = 1;
    }
    if (a0)
    {
        if (a0->field_10 == 1)
        {
            v0 = String__get_Chars(a0, 0, 0);
            v1 = v0;
            if (v0 - 97 < 26)
            {
                return v1;
            }
            else if ((unsigned int)v1 - 65 <= 25)
            {
                return (unsigned int)v1 + 32;
            }
            else if ((unsigned int)v1 - 48 < 10)
            {
                return v1;
            }
        }
        if (((char)String__Equals(a0, g_1f12408, 5, 0) & 1) || ((char)String__Equals(a0, g_1f14598, 5, 0) & 1))
            return 13;
        if (((char)String__Equals(a0, g_1f14ae8, 5, 0) & 1) || ((char)String__Equals(a0, g_1f14b00, 5, 0) & 1) || ((char)String__Equals(a0, g_1f064e0, 5, 0) & 1))
            return 32;
        if (((char)String__Equals(a0, g_1f12468, 5, 0) & 1) || ((char)String__Equals(a0, g_1f12470, 5, 0) & 1))
            return 27;
        if (((char)String__Equals(a0, g_1f13688, 5, 0) & 1))
            return 276;
        if (((char)String__Equals(a0, g_1f145f0, 5, 0) & 1))
            return 275;
        if (((char)String__Equals(a0, g_1f15660, 5, 0) & 1))
            return 273;
        if (((char)String__Equals(a0, g_1f120e0, 5, 0) & 1))
            return 274;
        if (((char)String__Equals(a0, g_1f0bc60, 5, 0) & 1))
            return 276;
        if (!((char)String__Equals(a0, g_1f0d628, 5, 0) & 1))
        {
            if (((char)String__Equals(a0, g_1f0f748, 5, 0) & 1))
                return 273;
            if (((char)String__Equals(a0, g_1f09b98, 5, 0) & 1))
                return 274;
            if (((char)String__Equals(a0, g_1f08730, 5, 0) & 1))
                return 276;
            if (!((char)String__Equals(a0, g_1f08738, 5, 0) & 1))
            {
                if (((char)String__Equals(a0, g_1f08740, 5, 0) & 1))
                {
                    return 273;
                }
                else if (((char)String__Equals(a0, g_1f08728, 5, 0) & 1))
                {
                    return 274;
                }
                else if (((char)String__Equals(a0, g_1f0cd58, 5, 0) & 1) || ((char)String__Equals(a0, g_1f0cd68, 5, 0) & 1) || ((char)String__Equals(a0, g_1f0cf08, 5, 0) & 1))
                {
                    return 281;
                }
                goto LABEL_103cc54;
            }
        }
        return 275;
    }
    else
    {
        sub_f7db74();
LABEL_103cc54:
        if (((char)String__Equals(a0, g_1f0cd60, 5, 0) & 1) || ((char)String__Equals(a0, g_1f0cd70, 5, 0) & 1) || ((char)String__Equals(a0, g_1f0cf10, 5, 0) & 1))
            return 280;
        if (((char)String__Equals(a0, g_1f11078, 5, 0) & 1) || ((char)String__Equals(a0, g_1f0bb88, 5, 0) & 1) || ((char)String__Equals(a0, g_1f0bc78, 5, 0) & 1))
            return 308;
        if (((char)String__Equals(a0, g_1f0d198, 5, 0) & 1) || ((char)String__Equals(a0, g_1f0d640, 5, 0) & 1))
            return 307;
        if (((char)String__Equals(a0, g_1f11a90, 5, 0) & 1) || ((char)String__Equals(a0, g_1f0bb90, 5, 0) & 1) || ((char)String__Equals(a0, g_1f0bc80, 5, 0) & 1))
            return 306;
        if (((char)String__Equals(a0, g_1f0d1a0, 5, 0) & 1) || ((char)String__Equals(a0, g_1f0d648, 5, 0) & 1))
            return 305;
        if (((char)String__Equals(a0, g_1f11d88, 5, 0) & 1))
        {
            return 306;
        }
        else if (((char)String__Equals(a0, g_1f0bb98, 5, 0) & 1))
        {
            return 306;
        }
        else if (((char)String__Equals(a0, g_1f0bc88, 5, 0) & 1))
        {
            return 306;
        }
        else if (!((char)String__Equals(a0, g_1f0d1a8, 5, 0) & 1) && !((char)String__Equals(a0, g_1f0d650, 5, 0) & 1))
        {
            if (((char)String__Equals(a0, g_1f14928, 5, 0) & 1) || ((char)String__Equals(a0, g_1f0bba0, 5, 0) & 1) || ((char)String__Equals(a0, g_1f0bc90, 5, 0) & 1))
                return 304;
            if (((char)String__Equals(a0, g_1f0d1b0, 5, 0) & 1) || ((char)String__Equals(a0, g_1f0d658, 5, 0) & 1))
                return 303;
            if (((char)String__Equals(a0, g_1f09230, 5, 0) & 1) || ((char)String__Equals(a0, g_1f09238, 5, 0) & 1) || ((char)String__Equals(a0, g_1f09228, 5, 0) & 1))
                return 301;
            if (((char)String__Equals(a0, g_1f14f58, 5, 0) & 1))
                return 9;
            if (((char)String__Equals(a0, g_1f075e0, 5, 0) & 1) || ((char)String__Equals(a0, g_1f112c0, 5, 0) & 1))
                return 92;
            if (((char)String__Equals(a0, g_1f10078, 5, 0) & 1) || ((char)String__Equals(a0, g_1f14a30, 5, 0) & 1))
                return 47;
            if (((char)String__Equals(a0, g_1f0feb8, 5, 0) & 1))
            {
                return 91;
            }
            else if (((char)String__Equals(a0, g_1f100b0, 5, 0) & 1))
            {
                return 93;
            }
            else if (((char)String__Equals(a0, g_1f07550, 5, 0) & 1))
            {
                return 44;
            }
            else if (((char)String__Equals(a0, g_1f07148, 5, 0) & 1))
            {
                return 58;
            }
            else if (((char)String__Equals(a0, g_1f06bf0, 5, 0) & 1))
            {
                return 39;
            }
            else if (((char)String__Equals(a0, g_1f07db8, 5, 0) & 1))
            {
                return 59;
            }
            else if (((char)String__Equals(a0, g_1f13c58, 5, 0) & 1))
            {
                return 323;
            }
            else
            {
                if (((char)String__Equals(a0, g_1f13c60, 5, 0) & 1))
                    return 324;
                if (((char)String__Equals(a0, g_1f13c68, 5, 0) & 1))
                {
                    return 325;
                }
                else if (((char)String__Equals(a0, g_1f13c70, 5, 0) & 1))
                {
                    return 326;
                }
                else if (((char)String__Equals(a0, g_1f13c78, 5, 0) & 1))
                {
                    return 327;
                }
                else if (((char)String__Equals(a0, g_1f13690, 5, 0) & 1))
                {
                    return 323;
                }
                else if (!((char)String__Equals(a0, g_1f145f8, 5, 0) & 1))
                {
                    if (((char)String__Equals(a0, g_1f0bbe0, 5, 0) & 1))
                    {
                        return 323;
                    }
                    else if (!((char)String__Equals(a0, g_1f0d238, 5, 0) & 1))
                    {
                        if (((char)String__Equals(a0, g_1f0bf00, 5, 0) & 1))
                        {
                            return 325;
                        }
                        else if (((char)String__Equals(a0, g_1f0a1f0, 5, 0) & 1))
                        {
                            return 282;
                        }
                        else if (((char)String__Equals(a0, g_1f0a210, 5, 0) & 1))
                        {
                            return 283;
                        }
                        else if (((char)String__Equals(a0, g_1f0a218, 5, 0) & 1))
                        {
                            return 284;
                        }
                        else if (((char)String__Equals(a0, g_1f0a220, 5, 0) & 1))
                        {
                            return 285;
                        }
                        else if (((char)String__Equals(a0, g_1f0a228, 5, 0) & 1))
                        {
                            return 286;
                        }
                        else if (((char)String__Equals(a0, g_1f0a230, 5, 0) & 1))
                        {
                            return 287;
                        }
                        else if (((char)String__Equals(a0, g_1f0a238, 5, 0) & 1))
                        {
                            return 288;
                        }
                        else if (((char)String__Equals(a0, g_1f0a240, 5, 0) & 1))
                        {
                            return 289;
                        }
                        else if (((char)String__Equals(a0, g_1f0a248, 5, 0) & 1))
                        {
                            return 290;
                        }
                        else if (((char)String__Equals(a0, g_1f0a1f8, 5, 0) & 1))
                        {
                            return 291;
                        }
                        else if (((char)String__Equals(a0, g_1f0a200, 5, 0) & 1))
                        {
                            return 292;
                        }
                        else
                        {
                            v2 = arm64g_calculate_condition(25, (unsigned long long)((unsigned int)(unsigned long long)String__Equals(a0, g_1f0a208, 5, 0) & 1), 0, 0);
                            if ((char)v2)
                                v3 = 293;
                            else
                                v3 = 0;
                            return v3;
                        }
                    }
                }
                return 324;
            }
            return 47;
            return 92;
            return 301;
            return 303;
            return 304;
        }
        return 305;
        return 306;
        return 307;
        return 308;
        return 280;
    }
}
```

## `InputRig.IsAxisAvailableOnMobile` — RVA `0xc3d4c8`

- Decompiled symbol: `InputRig_IsAxisAvailableOnMobile`
- Metadata signature: `public bool IsAxisAvailableOnMobile(string axisName) { }`
- Native interval: `172` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[264];
    struct struct_0 *field_108;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern int g_1fab000;
extern char g_1fab1be;

unsigned long long InputRig_IsAxisAvailableOnMobile(struct_1 *ptr, unsigned long a1)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x23
    int v4;  // w21
    struct_0 *p;  // x0
    unsigned long v6;  // x23
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]

    v0 = v2;
    v1 = v3;
    v4 = (int)&g_1fab000;
    if (!(g_1fab1be & 1))
    {
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef8a38);
        g_1fab1be = 1;
    }
    p = ptr->field_108;
    if (p)
    {
        v4 = 0;
        v6 = p->field_18;
        if ((unsigned int)v6 <= 0)
            goto LABEL_103d55c;
        p = sub_14a30c0();
        if (p)
            TouchControl__IsBoundToAxis(); /* do not return */
    }
    sub_f7db74(p);
LABEL_103d55c:
    if ((unsigned int)v6 > v4)
        return 1;
    return 0;
}
```

## `InputRig.IsKeyAvailableOnMobile` — RVA `0xc3d574`

- Decompiled symbol: `InputRig_IsKeyAvailableOnMobile`
- Metadata signature: `public bool IsKeyAvailableOnMobile(KeyCode keyCode) { }`
- Native interval: `316` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[264];
    struct struct_0 *field_108;
} struct_1;

typedef struct struct_2 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
} struct_2;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern long long g_1ef90d0;
extern long long g_1ef90d8;
extern char g_1fab1bf;

unsigned int InputRig_IsKeyAvailableOnMobile(struct_1 *ptr, unsigned long a1)
{
    struct_2 *p;  // x0
    struct_1 *addr;  // x8
    unsigned int v2;  // w21
    unsigned long v3;  // cc_dep1
    unsigned long v4;  // cc_dep2
    unsigned int v5;  // w22
    unsigned long v6;  // 4102
    unsigned long v7;  // 4102

    if (!(g_1fab1bf & 1))
    {
        sub_f7d92c(&g_1ef90d0);
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef90d8);
        sub_f7d92c(&g_1ef8a38);
        g_1fab1bf = 1;
    }
    p = ptr->field_108;
    if (p)
    {
        if (p->field_18 > 0)
        {
            p = sub_14a30c0();
            if (p)
                TouchControl__IsBoundToKey(); /* do not return */
        }
        else
        {
            addr = *((long long *)&ptr->padding_0[128]);
            if (*((long long *)&ptr->padding_0[128]))
            {
                v2 = 0;
                do
                {
                    p = *((long long *)&addr->padding_0[16]);
                    if (!p)
                        break;
                    v3 = v2;
                    v4 = p->field_18;
                    if (p->field_18 <= v2)
                    {
                        v5 = 0;
                        v6 = arm64g_calculate_condition(163, v3, v4, 0);
                        if ((char)v6)
                            return 0;
                    }
                    else
                    {
                        v5 = 1;
                        v7 = arm64g_calculate_condition(163, v3, v4, 0);
                        if ((char)v7)
                            return 1;
                    }
                    p = sub_14a30c0();
                    if (!p)
                        break;
                    p = InputRig_AxisConfig__DoesAffectKeyCode();
                    if (((char)p & 1))
                    {
                        p = InputRig__IsAxisAvailableOnMobile(ptr, p->field_10);
                        if (((char)p & 1))
                            return v5;
                    }
                    addr = *((long long *)&ptr->padding_0[128]);
                    v2 += 1;
                } while (addr);
            }
        }
    }
    sub_f7db74(p);
    return 1;
}
```

## `InputRig.IsTouchEmulatedOnMobile` — RVA `0xc3d6b0`

- Decompiled symbol: `InputRig_IsTouchEmulatedOnMobile`
- Metadata signature: `public bool IsTouchEmulatedOnMobile() { }`
- Native interval: `160` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[264];
    struct struct_0 *field_108;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern int g_1fab000;
extern char g_1fab1c0;

unsigned long long InputRig_IsTouchEmulatedOnMobile(struct_1 *ptr)
{
    unsigned long long v1;  // x30
    int v2;  // w20
    struct_0 *p;  // x0
    int v4;  // w22
    unsigned long long v0;  // [bp-0x30]

    v0 = v1;
    v2 = (int)&g_1fab000;
    if (!(g_1fab1c0 & 1))
    {
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef8a38);
        g_1fab1c0 = 1;
    }
    p = ptr->field_108;
    if (p)
    {
        v2 = 0;
        v4 = p->field_18;
        if (v4 <= 0)
            goto LABEL_103d738;
        p = sub_14a30c0();
        if (p)
            TouchControl__IsEmulatingTouches(); /* do not return */
    }
    sub_f7db74(p);
LABEL_103d738:
    if (v4 > v2)
        return 1;
    return 0;
}
```

## `InputRig.IsMousePositionEmulatedOnMobile` — RVA `0xc3d750`

- Decompiled symbol: `InputRig_IsMousePositionEmulatedOnMobile`
- Metadata signature: `public bool IsMousePositionEmulatedOnMobile() { }`
- Native interval: `160` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[264];
    struct struct_0 *field_108;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern long long g_1ef8a30;
extern long long g_1ef8a38;
extern int g_1fab000;
extern char g_1fab1c1;

unsigned long long InputRig_IsMousePositionEmulatedOnMobile(struct_1 *ptr)
{
    unsigned long long v1;  // x30
    int v2;  // w20
    struct_0 *p;  // x0
    int v4;  // w22
    unsigned long long v0;  // [bp-0x30]

    v0 = v1;
    v2 = (int)&g_1fab000;
    if (!(g_1fab1c1 & 1))
    {
        sub_f7d92c(&g_1ef8a30);
        sub_f7d92c(&g_1ef8a38);
        g_1fab1c1 = 1;
    }
    p = ptr->field_108;
    if (p)
    {
        v2 = 0;
        v4 = p->field_18;
        if (v4 <= 0)
            goto LABEL_103d7d8;
        p = sub_14a30c0();
        if (p)
            TouchControl__IsEmulatingMousePosition(); /* do not return */
    }
    sub_f7db74(p);
LABEL_103d7d8:
    if (v4 > v2)
        return 1;
    return 0;
}
```

## `InputRig.IsScrollWheelEmulatedOnMobile` — RVA `0xc3d7f0`

- Decompiled symbol: `InputRig_IsScrollWheelEmulatedOnMobile`
- Metadata signature: `public bool IsScrollWheelEmulatedOnMobile() { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[264];
    struct struct_0 *field_108;
} struct_1;

typedef struct struct_4 {
    char padding_0[32];
    struct struct_5 *field_20;
} struct_4;

typedef struct struct_2 {
    char padding_0[32];
    struct struct_3 *field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    unsigned int field_18;
} struct_0;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

typedef struct struct_5 {
    char padding_0[32];
    struct struct_6 *field_20;
} struct_5;

typedef struct struct_3 {
    char padding_0[16];
    char field_10;
} struct_3;

typedef struct struct_6 {
    char padding_0[16];
    char field_10;
} struct_6;

unsigned long long InputRig_IsScrollWheelEmulatedOnMobile(struct_1 *a0, unsigned long a1, unsigned long a2)
{
    struct_0 *v0;  // x0
    unsigned long long v1;  // x0

    if (*((long long *)&a0[1].padding_0[16]) && *((long long *)(*((long long *)&a0[1].padding_0[16]) + 32)) && *((long long *)(*((long long *)(*((long long *)&a0[1].padding_0[16]) + 32)) + 32)))
    {
        if (*((char *)(*((long long *)(*((long long *)(*((long long *)&a0[1].padding_0[16]) + 32)) + 32)) + 16)))
        {
            v0 = AxisBinding__GetTarget();
            if (!v0)
            {
                return 0;
            }
            else if (v0->field_10)
            {
                return 0;
            }
            else
            {
                v1 = InputRig__IsAxisAvailableOnMobile(a0, *((long long *)&v0->field_18));
                return InputRig__IsAxisAvailableOnMobile(a0, *((long long *)&v0->field_18));
            }
        }
        else
        {
            return 0;
        }
    }
    sub_f7db74();
}
```

## `InputRig.IsJoystickDefined` — RVA `0xc3d850`

- Decompiled symbol: `InputRig_IsJoystickDefined`
- Metadata signature: `public bool IsJoystickDefined(string name, ref int cachedId) { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[120];
    long long field_78;
} struct_0;

extern long long g_1ef9898;
extern char g_1fab1c2;

unsigned long long InputRig_IsJoystickDefined(struct_0 *a0, long long a1, long long a2)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x30]

    v0 = v1;
    if (!(g_1fab1c2 & 1))
    {
        sub_f7d92c(&g_1ef9898);
        g_1fab1c2 = 1;
    }
    if (a0->field_78)
    {
        if (!sub_15264f8(a0->field_78, a1, a2, g_1ef9898))
            return 0;
        return 1;
    }
    sub_f7db74(0);
}
```

## `InputRig.IsJoystickDefined` — RVA `0xc3d8c4`

- Decompiled symbol: `InputRig_IsJoystickDefined`
- Metadata signature: `public bool IsJoystickDefined(string name) { }`
- Native interval: `100` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[120];
    long long field_78;
} struct_0;

extern long long g_1ef9890;
extern char g_1fab1c3;

unsigned long long InputRig_IsJoystickDefined(struct_0 *a0, long long a1, unsigned long a2)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x21
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]

    v0 = v2;
    v1 = v3;
    if (!(g_1fab1c3 & 1))
    {
        sub_f7d92c(&g_1ef9890);
        g_1fab1c3 = 1;
    }
    if (a0->field_78)
    {
        if (!sub_1526618(a0->field_78, a1, g_1ef9890))
            return 0;
        return 1;
    }
    sub_f7db74(0);
}
```

## `InputRig.GetJoystickState` — RVA `0xc3d928`

- Decompiled symbol: `InputRig_GetJoystickState`
- Metadata signature: `public JoystickState GetJoystickState(string name, ref int cachedId) { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[40];
    struct struct_1 *field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[120];
    long long field_78;
} struct_0;

extern long long g_1ef9898;
extern char g_1fab1c4;

struct_1 * InputRig_GetJoystickState(struct_0 *a0, long long a1, long long a2)
{
    struct_1 *v0;  // x0

    if (!(g_1fab1c4 & 1))
    {
        sub_f7d92c(&g_1ef9898);
        g_1fab1c4 = 1;
    }
    if (a0->field_78)
    {
        v0 = sub_15264f8(a0->field_78, a1, a2, g_1ef9898);
        if (!v0)
            return v0;
        return v0->field_28;
    }
    sub_f7db74(0);
}
```

## `InputRig.MouseButtonToKey` — RVA `0xc3d99c`

- Decompiled symbol: `InputRig_MouseButtonToKey`
- Metadata signature: `public static KeyCode MouseButtonToKey(int mouseButton) { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
unsigned long long InputRig_MouseButtonToKey(unsigned int a0)
{
    if (a0 >= 7)
        return 323;
    return a0 + 323;
}
```

## `InputRig.get_axisConfigCount` — RVA `0xc3d9b0`

- Decompiled symbol: `InputRig_get_axisConfigCount`
- Metadata signature: `public int get_axisConfigCount() { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[128];
    struct struct_1 *field_80;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

extern long long g_1ef90d0;
extern char g_1fab1c5;

int InputRig_get_axisConfigCount(struct_2 *a0, unsigned long a1)
{
    if (!(g_1fab1c5 & 1))
    {
        sub_f7d92c(&g_1ef90d0);
        g_1fab1c5 = 1;
    }
    if (a0->field_80 && a0->field_80->field_10)
        return a0->field_80->field_10->field_18;
    sub_f7db74();
}
```

## `InputRig.GetAxisConfig` — RVA `0xc3da00`

- Decompiled symbol: `InputRig_GetAxisConfig`
- Metadata signature: `public InputRig.AxisConfig GetAxisConfig(int id) { }`
- Native interval: `140` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[128];
    struct struct_0 *field_80;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

extern long long g_1ef90d0;
extern long long g_1ef90d8;
extern char g_1fab1c6;

unsigned int InputRig_GetAxisConfig(struct_1 *a0, unsigned int a1, unsigned long a2)
{
    unsigned long v0;  // x19

    v0 = a1;
    if (!(g_1fab1c6 & 1))
    {
        sub_f7d92c(&g_1ef90d0);
        sub_f7d92c(&g_1ef90d8);
        g_1fab1c6 = 1;
    }
    if (((char)(v0 >> 31) & 1))
        return 0;
    if (a0->field_80 && a0->field_80->field_10)
    {
        if (*((int *)(a0->field_80->field_10 + 24)) > (unsigned int)v0)
            return sub_14a30c0();
        return 0;
    }
    sub_f7db74();
}
```

## `InputRig.GetAxisConfig` — RVA `0xc3da8c`

- Decompiled symbol: `InputRig_GetAxisConfig`
- Metadata signature: `public InputRig.AxisConfig GetAxisConfig(string name, ref int cachedId) { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[128];
    unsigned long long field_80;
} struct_0;

extern long long g_1ef9858;
extern char g_1fab1c7;

void InputRig_GetAxisConfig(struct_0 *a0, unsigned long a1, unsigned long a2)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
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
    if (!(g_1fab1c7 & 1))
    {
        sub_f7d92c(&g_1ef9858);
        g_1fab1c7 = 1;
    }
    if (a0->field_80)
    {
        sub_15264f8();
        return;
    }
    sub_f7db74(0);
}
```

## `InputRig.GetAxisConfig` — RVA `0xc3daf4`

- Decompiled symbol: `InputRig_GetAxisConfig`
- Metadata signature: `public InputRig.AxisConfig GetAxisConfig(string name) { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[128];
    unsigned long long field_80;
} struct_0;

extern long long g_1ef9850;
extern char g_1fab1c8;

void InputRig_GetAxisConfig(struct_0 *a0, unsigned long a1, unsigned long a2, unsigned long a3)
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
    if (!(g_1fab1c8 & 1))
    {
        sub_f7d92c(&g_1ef9850);
        g_1fab1c8 = 1;
    }
    if (a0->field_80)
    {
        sub_1526618();
        return;
    }
    sub_f7db74(0);
}
```

## `InputRig.SetAxis` — RVA `0xc3db4c`

- Decompiled symbol: `InputRig_SetAxis`
- Metadata signature: `public void SetAxis(string name, ref int cachedId, float v, InputRig.InputSource source) { }`
- Native interval: `160` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[128];
    long long field_80;
} struct_0;

extern long long g_1ef9858;
extern char g_1fab1c9;

unsigned long long InputRig_SetAxis(struct_0 *a0, long long a1, long long a2, unsigned long a3)
{
    unsigned long long v0;  // x0

    if (!(g_1fab1c9 & 1))
    {
        sub_f7d92c(&g_1ef9858);
        g_1fab1c9 = 1;
    }
    if (a0->field_80)
    {
        if (sub_15264f8(a0->field_80, a1, a2, g_1ef9858))
        {
            v0 = InputRig_AxisConfig__Set();
            return InputRig_AxisConfig__Set();
        }
        return 0;
    }
    sub_f7db74(0);
}
```

## `InputRig.SetAxisScroll` — RVA `0xc3dbec`

- Decompiled symbol: `InputRig_SetAxisScroll`
- Metadata signature: `public void SetAxisScroll(string name, ref int cachedId, int v) { }`
- Native interval: `140` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[128];
    long long field_80;
} struct_0;

extern long long g_1ef9858;
extern char g_1fab1ca;

unsigned long long InputRig_SetAxisScroll(struct_0 *a0, long long a1, long long a2, unsigned long a3)
{
    unsigned long long v0;  // x0

    if (!(g_1fab1ca & 1))
    {
        sub_f7d92c(&g_1ef9858);
        g_1fab1ca = 1;
    }
    if (a0->field_80)
    {
        if (sub_15264f8(a0->field_80, a1, a2, g_1ef9858))
        {
            v0 = InputRig_AxisConfig__SetScrollDelta();
            return InputRig_AxisConfig__SetScrollDelta();
        }
        return 0;
    }
    sub_f7db74(0);
}
```

## `InputRig.SetAxisDigital` — RVA `0xc3dc78`

- Decompiled symbol: `InputRig_SetAxisDigital`
- Metadata signature: `public void SetAxisDigital(string name, ref int cachedId, bool negSide) { }`
- Native interval: `144` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[128];
    long long field_80;
} struct_0;

extern long long g_1ef9858;
extern char g_1fab1cb;

unsigned long long InputRig_SetAxisDigital(struct_0 *a0, long long a1, long long a2, unsigned long a3)
{
    unsigned long long v0;  // x0

    if (!(g_1fab1cb & 1))
    {
        sub_f7d92c(&g_1ef9858);
        g_1fab1cb = 1;
    }
    if (a0->field_80)
    {
        if (sub_15264f8(a0->field_80, a1, a2, g_1ef9858))
        {
            v0 = InputRig_AxisConfig__SetSignedDigital();
            return InputRig_AxisConfig__SetSignedDigital();
        }
        return 0;
    }
    sub_f7db74(0);
}
```

## `InputRig.SetJoystickState` — RVA `0xc3dd08`

- Decompiled symbol: `InputRig_SetJoystickState`
- Metadata signature: `public void SetJoystickState(string name, ref int joyId, JoystickState state) { }`
- Native interval: `140` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[120];
    long long field_78;
} struct_0;

extern long long g_1ef9898;
extern char g_1fab1cc;

unsigned long long InputRig_SetJoystickState(struct_0 *a0, long long a1, long long a2, unsigned long a3)
{
    unsigned long long v0;  // x0

    if (!(g_1fab1cc & 1))
    {
        sub_f7d92c(&g_1ef9898);
        g_1fab1cc = 1;
    }
    if (a0->field_78)
    {
        if (sub_15264f8(a0->field_78, a1, a2, g_1ef9898))
        {
            v0 = InputRig_VirtualJoystickConfig__SetState();
            return InputRig_VirtualJoystickConfig__SetState();
        }
        return 0;
    }
    sub_f7db74(0);
}
```

## `InputRig.SetKeyCode` — RVA `0xc3dd94`

- Decompiled symbol: `InputRig_SetKeyCode`
- Metadata signature: `public void SetKeyCode(KeyCode keyCode) { }`
- Native interval: `96` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_Recovered` matched 4 offsets against `InputRig` metadata (confidence 1.00).

```c
typedef struct InputRig_Recovered {
    char padding_0[152];
    unsigned long long keysCur;
    unsigned long long keysNext;
    char padding_a8[16];
    char keysNextSomeDown;
    char keysNextSomeOn;
} InputRig_Recovered;

void InputRig_SetKeyCode(struct_0 *ptr, unsigned int a1)
{
    unsigned long v0;  // x0

    if (!a1)
        return;
    v0 = ptr->field_a0;
    if (v0)
    {
        BitArray__Set(v0);
        v0 = ptr->field_98;
        if (v0)
        {
            if (!((char)BitArray__get_Item(v0, a1, 0) & 1))
                ptr->field_b8 = 1;
            ptr->field_b9 = 1;
            return;
        }
    }
    sub_f7db74(v0);
}
```

## `InputRig.GetNextFrameKeyState` — RVA `0xc3ddf4`

- Decompiled symbol: `InputRig_GetNextFrameKeyState`
- Metadata signature: `public bool GetNextFrameKeyState(KeyCode key) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[160];
    unsigned long long field_a0;
} struct_0;

void InputRig_GetNextFrameKeyState(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a0->field_a0)
    {
        BitArray__get_Item();
        return;
    }
    sub_f7db74(0);
}
```

## `InputRig.RecalcPixelConversionParams` — RVA `0xc3de10`

- Decompiled symbol: `InputRig_RecalcPixelConversionParams`
- Metadata signature: `public void RecalcPixelConversionParams() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long InputRig_RecalcPixelConversionParams(unsigned int *a0)
{
    unsigned long v0;  // x0

    v0 = (unsigned long long)InputRig__CheckResolution(a0, 1);
    return (unsigned long long)InputRig__CheckResolution(a0, 1);
}
```

## `InputRig.TransformMousePointDelta` — RVA `0xc3de18`

- Decompiled symbol: `InputRig_TransformMousePointDelta`
- Metadata signature: `public float TransformMousePointDelta(float mousePoints, InputRig.DeltaTransformMode mode) { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
long long InputRig_TransformMousePointDelta(unsigned long a0, unsigned int a1)
{
    if (!a1)
        return a0;
    return a0;
}
```

## `InputRig.TransformTouchPixelDelta` — RVA `0xc3de2c`

- Decompiled symbol: `InputRig_TransformTouchPixelDelta`
- Metadata signature: `public float TransformTouchPixelDelta(float touchPix, InputRig.DeltaTransformMode mode) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
long long InputRig_TransformTouchPixelDelta(unsigned long a0, unsigned int flag)
{
    if (flag && flag != 1)
        return a0;
    return a0;
}
```

## `InputRig.TransformNormalizedDelta` — RVA `0xc3de4c`

- Decompiled symbol: `InputRig_TransformNormalizedDelta`
- Metadata signature: `public float TransformNormalizedDelta(float normDelta, InputRig.DeltaTransformMode mode) { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
long long InputRig_TransformNormalizedDelta(unsigned long a0, unsigned int a1)
{
    return a0;
}
```

## `InputRig.TransformScrollDelta` — RVA `0xc3de64`

- Decompiled symbol: `InputRig_TransformScrollDelta`
- Metadata signature: `public float TransformScrollDelta(float scrollDelta, InputRig.DeltaTransformMode mode) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
long long InputRig_TransformScrollDelta(unsigned long a0, unsigned int flag)
{
    if (flag && flag != 2 && flag != 1)
        return a0;
    return a0;
}
```

## `InputRig.TransformAnalogDelta` — RVA `0xc3de8c`

- Decompiled symbol: `InputRig_TransformAnalogDelta`
- Metadata signature: `public float TransformAnalogDelta(float analogVal, InputRig.DeltaTransformMode mode) { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
long long InputRig_TransformAnalogDelta(unsigned long a0, unsigned int flag)
{
    if (flag && flag != 2 && flag != 1)
        return a0;
    return a0;
}
```

## `InputRig.GetSubBindingDescriptions` — RVA `0xc3debc`

- Decompiled symbol: `InputRig_GetSubBindingDescriptions`
- Metadata signature: `public void GetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Native interval: `752` bytes
- Result: `pseudocode`

```c
extern long long g_1ef9128;
extern long long g_1ef9130;
extern long long g_1f075e0;
extern long long g_1f0a690;
extern long long g_1f0a698;
extern long long g_1f0c390;
extern long long g_1f0c3b8;
extern long long g_1f0ed60;
extern long long g_1f0fa18;
extern long long g_1f10178;
extern char g_1fab1ce;

long long InputRig_GetSubBindingDescriptions(long long *a0, long long a1, unsigned long a2, long long a3)
{
    long long v1;  // x0
    long long v2;  // x0
    unsigned long v3;  // x0
    unsigned int flag;  // [bp-0x54]

    if (!(g_1fab1ce & 1))
    {
        sub_f7d92c(&g_1ef9128);
        sub_f7d92c(&g_1ef9130);
        sub_f7d92c(&g_1f10178);
        sub_f7d92c(&g_1f0fa18);
        sub_f7d92c(&g_1f0a698);
        sub_f7d92c(&g_1f075e0);
        sub_f7d92c(&g_1f0c390);
        sub_f7d92c(&g_1f0c3b8);
        sub_f7d92c(&g_1f0ed60);
        sub_f7d92c(&g_1f0a690);
        g_1fab1ce = 1;
    }
    flag = 0;
    v1 = String__Concat(a3, g_1f0c3b8, 0);
    if (a0[35])
    {
        InputRig_MouseConfig__GetSubBindingDescriptions(a0[35], a1, a0, v1, 0);
        v2 = String__Concat(a3, g_1f0ed60, 0);
        if (a0[34])
            InputRig_TiltConfig__GetSubBindingDescriptions(a0[34], a1, a0, v2, 0); /* do not return */
    }
    v3 = sub_f7db74();
    return sub_f7db74();
}
```

## `InputRig.IsBoundToKey` — RVA `0xc3e1ac`

- Decompiled symbol: `InputRig_IsBoundToKey`
- Metadata signature: `public bool IsBoundToKey(KeyCode key, InputRig rig) { }`
- Native interval: `392` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_Recovered` matched 6 offsets against `InputRig` metadata (confidence 1.00).

```c
typedef struct InputRig_Recovered {
    char padding_0[120];
    struct struct_1 *joysticks;
    char padding_80[104];
    struct struct_2 *gamepads;
    struct struct_0 *anyGamepad;
    char padding_f8[24];
    struct struct_0 *tilt;
    struct struct_0 *mouseConfig;
    struct struct_0 *scrollWheel;
} InputRig_Recovered;

typedef struct struct_6 {
    char padding_0[24];
    unsigned int field_18;
} struct_6;

typedef struct struct_2 {
    char padding_0[24];
    int field_18;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

extern long long g_1ef9128;
extern long long g_1ef9130;
extern char g_1fab1cf;

unsigned int InputRig_IsBoundToKey(struct_3 *ptr, unsigned int a1, long long a2)
{
    struct_6 *p;  // x0
    struct_2 *i;  // x8
    unsigned long long v2;  // x22
    struct_1 *addr;  // x8
    unsigned int v4;  // w22
    unsigned long v5;  // cc_dep1
    unsigned long v6;  // cc_dep2
    unsigned int v7;  // w23
    unsigned long v8;  // 4102
    unsigned long v9;  // 4102

    if (!(g_1fab1cf & 1))
    {
        sub_f7d92c(&g_1ef9128);
        sub_f7d92c(&g_1ef9130);
        g_1fab1cf = 1;
    }
    p = ptr->field_118;
    if (p)
    {
        if (!((char)InputRig_MouseConfig__IsBoundToKey(p, a1, a2, 0) & 1))
        {
            p = ptr->field_110;
            if (p)
            {
                if (!((char)InputRig_TiltConfig__IsBoundToKey(p, a1, a2, 0) & 1))
                {
                    p = ptr->field_120;
                    if (p)
                    {
                        if (!((char)InputRig_ScrollWheelState__IsBoundToKey(p, a1, a2, 0) & 1))
                        {
                            p = ptr->field_f0;
                            if (p)
                            {
                                p = InputRig_GamepadConfig__IsBoundToKey(p, a1, a2, 0);
                                if (((char)p & 1))
                                    return 1;
                                i = ptr->field_e8;
                                if (ptr->field_e8)
                                {
                                    v2 = 0;
                                    do
                                    {
                                        if (i->field_18 > (unsigned int)v2)
                                        {
                                            if (i->field_18 <= (unsigned int)v2)
                                                sub_f7db7c(p);
                                            p = *((long long *)&i[1].padding_0[4 + 8 * v2]);
                                            if (!p)
                                                break;
                                        }
                                        else
                                        {
                                            addr = ptr->field_78;
                                            if (ptr->field_78)
                                            {
                                                v4 = 0;
                                                do
                                                {
                                                    p = addr->field_10;
                                                    if (!p)
                                                        break;
                                                    v5 = v4;
                                                    v6 = p->field_18;
                                                    if (p->field_18 <= v4)
                                                    {
                                                        v7 = 0;
                                                        v8 = arm64g_calculate_condition(163, v5, v6, 0);
                                                        if ((char)v8)
                                                            return 0;
                                                    }
                                                    else
                                                    {
                                                        v7 = 1;
                                                        v9 = arm64g_calculate_condition(163, v5, v6, 0);
                                                        if ((char)v9)
                                                            return 1;
                                                    }
                                                    if (!sub_14a30c0())
                                                        break;
                                                    if (((char)InputRig_VirtualJoystickConfig__IsBoundToKey() & 1))
                                                        return v7;
                                                    addr = ptr->field_78;
                                                    v4 += 1;
                                                } while (addr);
                                            }
                                        }
                                        p = InputRig_GamepadConfig__IsBoundToKey(p, a1, a2, 0);
                                        if (((char)p & 1))
                                            return 1;
                                        i = ptr->field_e8;
                                        v2 += 1;
                                    } while (i);
                                }
                            }
                        }
                        else
                        {
                            return 1;
                        }
                    }
                }
                else
                {
                    return 1;
                }
            }
        }
        else
        {
            return 1;
        }
    }
    p = sub_f7db74(p);
    sub_f7db7c(p);
}
```

## `InputRig.IsBoundToAxis` — RVA `0xc3e334`

- Decompiled symbol: `InputRig_IsBoundToAxis`
- Metadata signature: `public bool IsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `392` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_Recovered` matched 6 offsets against `InputRig` metadata (confidence 1.00).

```c
typedef struct InputRig_Recovered {
    char padding_0[120];
    struct struct_1 *joysticks;
    char padding_80[104];
    struct struct_2 *gamepads;
    struct struct_0 *anyGamepad;
    char padding_f8[24];
    struct struct_0 *tilt;
    struct struct_0 *mouseConfig;
    struct struct_0 *scrollWheel;
} InputRig_Recovered;

typedef struct struct_4 {
    char padding_0[24];
    unsigned int field_18;
} struct_4;

typedef struct struct_2 {
    char padding_0[24];
    int field_18;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

extern long long g_1ef9128;
extern long long g_1ef9130;
extern char g_1fab1d0;

unsigned int InputRig_IsBoundToAxis(struct_3 *ptr, long long a1, long long a2)
{
    struct_4 *p;  // x0
    struct_2 *i;  // x8
    unsigned long long v2;  // x22
    struct_1 *addr;  // x8
    unsigned int v4;  // w22
    unsigned long v5;  // cc_dep1
    unsigned long v6;  // cc_dep2
    unsigned int v7;  // w23
    unsigned long v8;  // 4102
    unsigned long v9;  // 4102

    if (!(g_1fab1d0 & 1))
    {
        sub_f7d92c(&g_1ef9128);
        sub_f7d92c(&g_1ef9130);
        g_1fab1d0 = 1;
    }
    p = ptr->field_118;
    if (p)
    {
        if (!((char)InputRig_MouseConfig__IsBoundToAxis(p, a1, a2, 0) & 1))
        {
            p = ptr->field_110;
            if (p)
            {
                if (!((char)InputRig_TiltConfig__IsBoundToAxis(p, a1, a2, 0) & 1))
                {
                    p = ptr->field_120;
                    if (p)
                    {
                        if (!((char)InputRig_ScrollWheelState__IsBoundToAxis(p, a1, a2, 0) & 1))
                        {
                            p = ptr->field_f0;
                            if (p)
                            {
                                p = InputRig_GamepadConfig__IsBoundToAxis(p, a1, a2, 0);
                                if (((char)p & 1))
                                    return 1;
                                i = ptr->field_e8;
                                if (ptr->field_e8)
                                {
                                    v2 = 0;
                                    do
                                    {
                                        if (i->field_18 > (unsigned int)v2)
                                        {
                                            if (i->field_18 <= (unsigned int)v2)
                                                sub_f7db7c(p);
                                            p = *((long long *)&i[1].padding_0[4 + 8 * v2]);
                                            if (!p)
                                                break;
                                        }
                                        else
                                        {
                                            addr = ptr->field_78;
                                            if (ptr->field_78)
                                            {
                                                v4 = 0;
                                                do
                                                {
                                                    p = addr->field_10;
                                                    if (!p)
                                                        break;
                                                    v5 = v4;
                                                    v6 = p->field_18;
                                                    if (p->field_18 <= v4)
                                                    {
                                                        v7 = 0;
                                                        v8 = arm64g_calculate_condition(163, v5, v6, 0);
                                                        if ((char)v8)
                                                            return 0;
                                                    }
                                                    else
                                                    {
                                                        v7 = 1;
                                                        v9 = arm64g_calculate_condition(163, v5, v6, 0);
                                                        if ((char)v9)
                                                            return 1;
                                                    }
                                                    if (!sub_14a30c0())
                                                        break;
                                                    if (((char)InputRig_VirtualJoystickConfig__IsBoundToAxis() & 1))
                                                        return v7;
                                                    addr = ptr->field_78;
                                                    v4 += 1;
                                                } while (addr);
                                            }
                                        }
                                        p = InputRig_GamepadConfig__IsBoundToAxis(p, a1, a2, 0);
                                        if (((char)p & 1))
                                            return 1;
                                        i = ptr->field_e8;
                                        v2 += 1;
                                    } while (i);
                                }
                            }
                        }
                        else
                        {
                            return 1;
                        }
                    }
                }
                else
                {
                    return 1;
                }
            }
        }
        else
        {
            return 1;
        }
    }
    p = sub_f7db74(p);
    sub_f7db7c(p);
}
```

## `InputRig.IsEmulatingTouches` — RVA `0xc3e4bc`

- Decompiled symbol: `InputRig_IsEmulatingTouches`
- Metadata signature: `public bool IsEmulatingTouches() { }`
- Native interval: `328` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_Recovered` matched 6 offsets against `InputRig` metadata (confidence 1.00).

```c
typedef struct InputRig_Recovered {
    char padding_0[120];
    struct struct_1 *joysticks;
    char padding_80[104];
    struct struct_2 *gamepads;
    struct struct_0 *anyGamepad;
    char padding_f8[24];
    struct struct_0 *tilt;
    struct struct_0 *mouseConfig;
    struct struct_0 *scrollWheel;
} InputRig_Recovered;

typedef struct struct_5 {
    char padding_0[24];
    unsigned int field_18;
} struct_5;

typedef struct struct_2 {
    char padding_0[24];
    int field_18;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

extern long long g_1ef9128;
extern long long g_1ef9130;
extern char g_1fab1d1;

unsigned int InputRig_IsEmulatingTouches(struct_3 *ptr)
{
    struct_5 *p;  // x0
    struct_2 *i;  // x8
    unsigned long long v2;  // x20
    struct_1 *addr;  // x8
    unsigned int v4;  // w20
    unsigned long v5;  // cc_dep1
    unsigned long v6;  // cc_dep2
    unsigned int v7;  // w21
    unsigned long v8;  // 4102
    unsigned long v9;  // 4102

    if (!(g_1fab1d1 & 1))
    {
        sub_f7d92c(&g_1ef9128);
        sub_f7d92c(&g_1ef9130);
        g_1fab1d1 = 1;
    }
    p = ptr->field_118;
    if (p)
    {
        if (!((char)InputRig_MouseConfig__IsEmulatingTouches(p, 0) & 1))
        {
            p = ptr->field_110;
            if (p)
            {
                if (!((char)InputRig_TiltConfig__IsEmulatingTouches(p, 0) & 1))
                {
                    p = ptr->field_120;
                    if (p)
                    {
                        if (!((char)InputRig_ScrollWheelState__IsEmulatingTouches(p, 0) & 1))
                        {
                            p = ptr->field_f0;
                            if (p)
                            {
                                p = InputRig_GamepadConfig__IsEmulatingTouches(p, 0);
                                if (((char)p & 1))
                                    return 1;
                                i = ptr->field_e8;
                                if (ptr->field_e8)
                                {
                                    v2 = 0;
                                    do
                                    {
                                        if (i->field_18 > (unsigned int)v2)
                                        {
                                            if (i->field_18 <= (unsigned int)v2)
                                                sub_f7db7c(p);
                                            p = *((long long *)&i[1].padding_0[4 + 8 * v2]);
                                            if (!p)
                                                break;
                                        }
                                        else
                                        {
                                            addr = ptr->field_78;
                                            if (ptr->field_78)
                                            {
                                                v4 = 0;
                                                do
                                                {
                                                    p = addr->field_10;
                                                    if (!p)
                                                        break;
                                                    v5 = v4;
                                                    v6 = p->field_18;
                                                    if (p->field_18 <= v4)
                                                    {
                                                        v7 = 0;
                                                        v8 = arm64g_calculate_condition(163, v5, v6, 0);
                                                        if ((char)v8)
                                                            return 0;
                                                    }
                                                    else
                                                    {
                                                        v7 = 1;
                                                        v9 = arm64g_calculate_condition(163, v5, v6, 0);
                                                        if ((char)v9)
                                                            return 1;
                                                    }
                                                    if (!sub_14a30c0())
                                                        break;
                                                    if (((char)InputRig_VirtualJoystickConfig__IsEmulatingTouches() & 1))
                                                        return v7;
                                                    addr = ptr->field_78;
                                                    v4 += 1;
                                                } while (addr);
                                            }
                                        }
                                        p = InputRig_GamepadConfig__IsEmulatingTouches(p, 0);
                                        if (((char)p & 1))
                                            return 1;
                                        i = ptr->field_e8;
                                        v2 += 1;
                                    } while (i);
                                }
                            }
                        }
                        else
                        {
                            return 1;
                        }
                    }
                }
                else
                {
                    return 1;
                }
            }
        }
        else
        {
            return 1;
        }
    }
    p = sub_f7db74(p);
    sub_f7db7c(p);
}
```

## `InputRig.IsEmulatingMousePosition` — RVA `0xc3e604`

- Decompiled symbol: `InputRig_IsEmulatingMousePosition`
- Metadata signature: `public bool IsEmulatingMousePosition() { }`
- Native interval: `328` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_Recovered` matched 6 offsets against `InputRig` metadata (confidence 1.00).

```c
typedef struct InputRig_Recovered {
    char padding_0[120];
    struct struct_1 *joysticks;
    char padding_80[104];
    struct struct_2 *gamepads;
    struct struct_0 *anyGamepad;
    char padding_f8[24];
    struct struct_0 *tilt;
    struct struct_0 *mouseConfig;
    struct struct_0 *scrollWheel;
} InputRig_Recovered;

typedef struct struct_5 {
    char padding_0[24];
    unsigned int field_18;
} struct_5;

typedef struct struct_2 {
    char padding_0[24];
    int field_18;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

extern long long g_1ef9128;
extern long long g_1ef9130;
extern char g_1fab1d2;

unsigned int InputRig_IsEmulatingMousePosition(struct_3 *ptr)
{
    struct_5 *p;  // x0
    struct_2 *i;  // x8
    unsigned long long v2;  // x20
    struct_1 *addr;  // x8
    unsigned int v4;  // w20
    unsigned long v5;  // cc_dep1
    unsigned long v6;  // cc_dep2
    unsigned int v7;  // w21
    unsigned long v8;  // 4102
    unsigned long v9;  // 4102

    if (!(g_1fab1d2 & 1))
    {
        sub_f7d92c(&g_1ef9128);
        sub_f7d92c(&g_1ef9130);
        g_1fab1d2 = 1;
    }
    p = ptr->field_118;
    if (p)
    {
        if (!((char)InputRig_MouseConfig__IsEmulatingMousePosition(p, 0) & 1))
        {
            p = ptr->field_110;
            if (p)
            {
                if (!((char)InputRig_TiltConfig__IsEmulatingMousePosition(p, 0) & 1))
                {
                    p = ptr->field_120;
                    if (p)
                    {
                        if (!((char)InputRig_ScrollWheelState__IsEmulatingMousePosition(p, 0) & 1))
                        {
                            p = ptr->field_f0;
                            if (p)
                            {
                                p = InputRig_GamepadConfig__IsEmulatingMousePosition(p, 0);
                                if (((char)p & 1))
                                    return 1;
                                i = ptr->field_e8;
                                if (ptr->field_e8)
                                {
                                    v2 = 0;
                                    do
                                    {
                                        if (i->field_18 > (unsigned int)v2)
                                        {
                                            if (i->field_18 <= (unsigned int)v2)
                                                sub_f7db7c(p);
                                            p = *((long long *)&i[1].padding_0[4 + 8 * v2]);
                                            if (!p)
                                                break;
                                        }
                                        else
                                        {
                                            addr = ptr->field_78;
                                            if (ptr->field_78)
                                            {
                                                v4 = 0;
                                                do
                                                {
                                                    p = addr->field_10;
                                                    if (!p)
                                                        break;
                                                    v5 = v4;
                                                    v6 = p->field_18;
                                                    if (p->field_18 <= v4)
                                                    {
                                                        v7 = 0;
                                                        v8 = arm64g_calculate_condition(163, v5, v6, 0);
                                                        if ((char)v8)
                                                            return 0;
                                                    }
                                                    else
                                                    {
                                                        v7 = 1;
                                                        v9 = arm64g_calculate_condition(163, v5, v6, 0);
                                                        if ((char)v9)
                                                            return 1;
                                                    }
                                                    if (!sub_14a30c0())
                                                        break;
                                                    if (((char)InputRig_VirtualJoystickConfig__IsEmulatingMousePosition() & 1))
                                                        return v7;
                                                    addr = ptr->field_78;
                                                    v4 += 1;
                                                } while (addr);
                                            }
                                        }
                                        p = InputRig_GamepadConfig__IsEmulatingMousePosition(p, 0);
                                        if (((char)p & 1))
                                            return 1;
                                        i = ptr->field_e8;
                                        v2 += 1;
                                    } while (i);
                                }
                            }
                        }
                        else
                        {
                            return 1;
                        }
                    }
                }
                else
                {
                    return 1;
                }
            }
        }
        else
        {
            return 1;
        }
    }
    p = sub_f7db74(p);
    sub_f7db7c(p);
}
```

## `InputRig.InternalStartEmuTouch` — RVA `0xc3e74c`

- Decompiled symbol: `InputRig_InternalStartEmuTouch`
- Metadata signature: `public int InternalStartEmuTouch(Vector2 pos) { }`
- Native interval: `184` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[352];
    struct struct_0 *field_160;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
    char padding_1c[72];
    char field_64;
} struct_0;

extern long long g_1ef90f8;
extern long long g_1ef9100;
extern char g_1fab1d4;

int InputRig_InternalStartEmuTouch(struct_1 *ptr)
{
    struct_0 *i;  // x0
    int v1;  // w20

    if (!(g_1fab1d4 & 1))
    {
        sub_f7d92c(&g_1ef90f8);
        sub_f7d92c(&g_1ef9100);
        g_1fab1d4 = 1;
    }
    i = ptr->field_160;
    if (i)
    {
        v1 = 0;
        do
        {
            if (i->field_18 <= v1)
                return -1;
            i = sub_14a30c0();
            if (!i)
                break;
            if (!i->field_64)
            {
                InputRig_EmulatedTouchState__Start();
                return v1;
            }
            i = ptr->field_160;
            v1 += 1;
        } while (i);
    }
    sub_f7db74(i);
    return -1;
}
```

## `InputRig.InternalEndEmuTouch` — RVA `0xc3e804`

- Decompiled symbol: `InputRig_InternalEndEmuTouch`
- Metadata signature: `public void InternalEndEmuTouch(int emuTouchId, bool cancel) { }`
- Native interval: `160` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[352];
    struct struct_0 *field_160;
} struct_0;

extern long long g_1ef90f8;
extern long long g_1ef9100;
extern char g_1fab1d5;

struct_0 * InputRig_InternalEndEmuTouch(struct_0 *ptr, unsigned int a1, unsigned long a2)
{
    unsigned long v0;  // x20
    struct_0 *v1;  // x0
    struct_0 *v2;  // x0
    struct_0 *v3;  // x0
    struct_0 *v4;  // x0
    unsigned long long v5;  // x0

    v0 = a1;
    v1 = ptr;
    if (!(g_1fab1d5 & 1))
    {
        sub_f7d92c(&g_1ef90f8);
        v2 = sub_f7d92c(&g_1ef9100);
        g_1fab1d5 = 1;
        v1 = v2;
    }
    v3 = v1;
    if (((char)(v0 >> 31) & 1))
        return v3;
    v4 = ptr->field_160;
    if (v4)
    {
        if (*((int *)&v4->padding_0[24]) > (unsigned int)v0)
        {
            v4 = sub_14a30c0();
            if (v4)
            {
                v5 = InputRig_EmulatedTouchState__EndTouch();
                return InputRig_EmulatedTouchState__EndTouch();
            }
        }
        else
        {
            return v4;
        }
    }
    sub_f7db74(v4);
}
```

## `InputRig.InternalUpdateEmuTouch` — RVA `0xc3e8a4`

- Decompiled symbol: `InputRig_InternalUpdateEmuTouch`
- Metadata signature: `public void InternalUpdateEmuTouch(int emuTouchId, Vector2 pos) { }`
- Native interval: `168` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[352];
    struct struct_0 *field_160;
} struct_0;

extern long long g_1ef90f8;
extern long long g_1ef9100;
extern char g_1fab1d6;

struct_0 * InputRig_InternalUpdateEmuTouch(struct_0 *ptr, unsigned int a1)
{
    unsigned long v0;  // x19
    struct_0 *v1;  // x0
    struct_0 *v2;  // x0
    struct_0 *v3;  // x0
    struct_0 *v4;  // x0
    unsigned long long v5;  // x0

    v0 = a1;
    v1 = ptr;
    if (!(g_1fab1d6 & 1))
    {
        sub_f7d92c(&g_1ef90f8);
        v2 = sub_f7d92c(&g_1ef9100);
        g_1fab1d6 = 1;
        v1 = v2;
    }
    v3 = v1;
    if (((char)(v0 >> 31) & 1))
        return v3;
    v4 = ptr->field_160;
    if (v4)
    {
        if (*((int *)&v4->padding_0[24]) > (unsigned int)v0)
        {
            v4 = sub_14a30c0();
            if (v4)
            {
                v5 = InputRig_EmulatedTouchState__UpdatePos();
                return InputRig_EmulatedTouchState__UpdatePos();
            }
        }
        else
        {
            return v4;
        }
    }
    sub_f7db74(v4);
}
```

## `InputRig.SyncEmuTouch` — RVA `0xc3e94c`

- Decompiled symbol: `InputRig_SyncEmuTouch`
- Metadata signature: `public void SyncEmuTouch(TouchGestureBasicState touch, ref int emuTouchId) { }`
- Native interval: `140` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[28];
    char field_1c;
} struct_0;

void* InputRig_SyncEmuTouch(void* a0, struct_0 *a1, unsigned int *ptr)
{
    void* v0;  // x0
    struct_0 *v1;  // x0

    if (!a1)
        return a0;
    if (((char)TouchGestureBasicState__JustPressedRaw(a1, 0) & 1))
    {
        v0 = InputRig__InternalStartEmuTouch(a0);
    }
    else
    {
        v0 = TouchGestureBasicState__JustReleasedRaw(a1, 0);
        if (!(v0 & 1))
            goto LABEL_103e9ac;
        InputRig__InternalEndEmuTouch(a0, *(ptr), 0);
        v0 = 0xffffffff;
    }
    *(ptr) = (unsigned int)v0;
LABEL_103e9ac:
    if (!a1->field_1c)
        return v0;
    v1 = InputRig__InternalUpdateEmuTouch(a0, *(ptr));
    return InputRig__InternalUpdateEmuTouch(a0, *(ptr));
}
```

## `InputRig.<>c__DisplayClass90_0.ctor` — RVA `0xc439b4`

- Decompiled symbol: `InputRig_c__DisplayClass90_0_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long InputRig_c__DisplayClass90_0_ctor(void)
{
    long long v0;  // x0

    v0 = Object__ctor();
    return Object__ctor();
}
```

## `InputRig.<>c__DisplayClass90_0.<FindTouchControl>b__0` — RVA `0xc439bc`

- Decompiled symbol: `InputRig_c__DisplayClass90_0_FindTouchControl_b__0`
- Metadata signature: `internal bool <FindTouchControl>b__0(TouchControl x) { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
void InputRig_c__DisplayClass90_0_FindTouchControl_b__0(unsigned long a0, long long a1)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    if (a1 && Object__get_name(a1, 0))
    {
        String__Equals();
        return;
    }
    sub_f7db74();
}
```
