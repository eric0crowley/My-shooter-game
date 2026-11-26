# Native pseudocode: GamepadHardwareTester

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GamepadHardwareTester.GetJoyAxisName` — RVA `0xc699c0`

- Decompiled symbol: `GamepadHardwareTester_GetJoyAxisName`
- Metadata signature: `public static string GetJoyAxisName(int joyId, int axisId) { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
extern long long g_1f11650;
extern char g_1fab323;

long long GamepadHardwareTester_GetJoyAxisName(unsigned int a0, unsigned int a1)
{
    long long v2;  // x0
    long long v3;  // x0
    unsigned long long v4;  // x0
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]

    v0 = a1;
    v1 = a0;
    if (!(g_1fab323 & 1))
    {
        sub_f7d92c(&g_1f11650);
        g_1fab323 = 1;
    }
    v2 = Int32__ToString(&v1, 0);
    v3 = Int32__ToString(&v0, 0);
    v4 = String__Concat(g_1f11650, v2, v3, 0);
    return String__Concat(g_1f11650, v2, v3, 0);
}
```

## `GamepadHardwareTester.GetJoyKeyCode` — RVA `0xc69a34`

- Decompiled symbol: `GamepadHardwareTester_GetJoyKeyCode`
- Metadata signature: `public static KeyCode GetJoyKeyCode(int joyId, int keyId) { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
unsigned long long GamepadHardwareTester_GetJoyKeyCode(unsigned int a0, unsigned long long a1)
{
    if (3 < a0)
    {
        return 0;
    }
    else if (((char)(a1 >> 31) & 1))
    {
        return 0;
    }
    else if ((unsigned int)a1 < 20)
    {
        return (unsigned int)a1 + 20 * a0 + 350;
    }
    else
    {
        return 0;
    }
}
```

## `GamepadHardwareTester.GetAxisCode` — RVA `0xc69a60`

- Decompiled symbol: `GamepadHardwareTester_GetAxisCode`
- Metadata signature: `private string GetAxisCode(int axis, bool positiveSide) { }`
- Native interval: `168` bytes
- Result: `pseudocode`

```c
extern long long g_1f07138;
extern long long g_1f071b8;
extern long long g_1f08948;
extern char g_1fab324;

long long GamepadHardwareTester_GetAxisCode(unsigned long a0, unsigned int a1, unsigned int a2)
{
    unsigned long v1;  // 4116
    unsigned long long v2;  // x0
    unsigned int v0;  // [bp-0x34]

    v0 = a1;
    if (!(g_1fab324 & 1))
    {
        sub_f7d92c(&g_1f07138);
        sub_f7d92c(&g_1f071b8);
        sub_f7d92c(&g_1f08948);
        g_1fab324 = 1;
    }
    Int32__ToString(&v0, 0);
    v1 = arm64g_calculate_condition(25, (unsigned long long)(a2 & 1), 0, 0);
    v2 = String__Concat();
    return String__Concat();
}
```

## `GamepadHardwareTester.GetAxisName` — RVA `0xc69b08`

- Decompiled symbol: `GamepadHardwareTester_GetAxisName`
- Metadata signature: `private string GetAxisName(int axis, bool positiveSide) { }`
- Native interval: `192` bytes
- Result: `pseudocode`

```c
extern long long g_1f07138;
extern long long g_1f071b8;
extern long long g_1f08950;
extern long long g_1f100c8;
extern char g_1fab325;

long long GamepadHardwareTester_GetAxisName(unsigned long a0, unsigned int a1, unsigned int a2)
{
    unsigned long v1;  // 4116
    unsigned long long v2;  // x0
    unsigned int v0;  // [bp-0x34]

    v0 = a1;
    if (!(g_1fab325 & 1))
    {
        sub_f7d92c(&g_1f100c8);
        sub_f7d92c(&g_1f07138);
        sub_f7d92c(&g_1f08950);
        sub_f7d92c(&g_1f071b8);
        g_1fab325 = 1;
    }
    Int32__ToString(&v0, 0);
    v1 = arm64g_calculate_condition(25, (unsigned long long)(a2 & 1), 0, 0);
    v2 = String__Concat();
    return String__Concat();
}
```

## `GamepadHardwareTester.GetAxisState` — RVA `0xc69bc8`

- Decompiled symbol: `GamepadHardwareTester_GetAxisState`
- Metadata signature: `private float GetAxisState(int axis) { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
extern long long g_1f0ba78;
extern char g_1fab326;

long long GamepadHardwareTester_GetAxisState(unsigned long a0, unsigned int a1)
{
    long long v1;  // x0
    unsigned long long v2;  // x0
    unsigned int v0;  // [bp-0x14]

    v0 = a1;
    if (!(g_1fab326 & 1))
    {
        sub_f7d92c(&g_1f0ba78);
        g_1fab326 = 1;
    }
    v1 = Int32__ToString(&v0, 0);
    v2 = Input__GetAxis(String__Concat(g_1f0ba78, v1, 0), 0, 0);
    return Input__GetAxis(String__Concat(g_1f0ba78, v1, 0), 0, 0);
}
```

## `GamepadHardwareTester.GetKeyCode` — RVA `0xc69c30`

- Decompiled symbol: `GamepadHardwareTester_GetKeyCode`
- Metadata signature: `private string GetKeyCode(int key) { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
extern long long g_1f0baf8;
extern char g_1fab327;

long long GamepadHardwareTester_GetKeyCode(unsigned long a0, unsigned int a1)
{
    long long v1;  // x0
    unsigned long long v2;  // x0
    unsigned int v0;  // [bp-0x14]

    v0 = a1;
    if (!(g_1fab327 & 1))
    {
        sub_f7d92c(&g_1f0baf8);
        g_1fab327 = 1;
    }
    v1 = Int32__ToString(&v0, 0);
    v2 = String__Concat(g_1f0baf8, v1, 0);
    return String__Concat(g_1f0baf8, v1, 0);
}
```

## `GamepadHardwareTester.GetKeyState` — RVA `0xc69c90`

- Decompiled symbol: `GamepadHardwareTester_GetKeyState`
- Metadata signature: `private bool GetKeyState(int key) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
void GamepadHardwareTester_GetKeyState(unsigned long a0, unsigned long a1)
{
    Input__GetKey();
    return;
}
```

## `GamepadHardwareTester.OnGUI` — RVA `0xc69c9c`

- Decompiled symbol: `GamepadHardwareTester_OnGUI`
- Metadata signature: `private void OnGUI() { }`
- Native interval: `2160` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1069c9c: sub sp, sp, #0xa0
// 0x1069ca0: str d12, [sp, #0x10]
// 0x1069ca4: stp d11, d10, [sp, #0x20]
// 0x1069ca8: stp d9, d8, [sp, #0x30]
// 0x1069cac: stp x29, x30, [sp, #0x40]
// 0x1069cb0: stp x28, x27, [sp, #0x50]
// 0x1069cb4: stp x26, x25, [sp, #0x60]
// 0x1069cb8: stp x24, x23, [sp, #0x70]
// 0x1069cbc: stp x22, x21, [sp, #0x80]
// 0x1069cc0: stp x20, x19, [sp, #0x90]
// 0x1069cc4: adrp x20, #0x1fab000
// 0x1069cc8: ldrb w8, [x20, #0x328]
// 0x1069ccc: mov x19, x0
// 0x1069cd0: tbnz w8, #0, #0x1069dfc
// 0x1069cd4: adrp x0, #0x1e8c000
// 0x1069cd8: ldr x0, [x0, #0x248]
// 0x1069cdc: bl #0xf7d92c
// 0x1069ce0: adrp x0, #0x1e8c000
// 0x1069ce4: ldr x0, [x0, #0xce0]
// 0x1069ce8: bl #0xf7d92c
// 0x1069cec: adrp x0, #0x1e8c000
// 0x1069cf0: ldr x0, [x0, #0x3a0]
// 0x1069cf4: bl #0xf7d92c
// 0x1069cf8: adrp x0, #0x1e8d000
// 0x1069cfc: ldr x0, [x0, #0x318]
// 0x1069d00: bl #0xf7d92c
// 0x1069d04: adrp x0, #0x1e8d000
// 0x1069d08: ldr x0, [x0, #0x320]
// 0x1069d0c: bl #0xf7d92c
// 0x1069d10: adrp x0, #0x1e8d000
// 0x1069d14: ldr x0, [x0, #0x328]
// 0x1069d18: bl #0xf7d92c
// 0x1069d1c: adrp x0, #0x1e8d000
// 0x1069d20: ldr x0, [x0, #0x330]
// 0x1069d24: bl #0xf7d92c
// 0x1069d28: adrp x0, #0x1e8d000
// 0x1069d2c: ldr x0, [x0, #0x338]
// 0x1069d30: bl #0xf7d92c
// 0x1069d34: adrp x0, #0x1e8d000
// 0x1069d38: ldr x0, [x0, #0x340]
// 0x1069d3c: bl #0xf7d92c
// 0x1069d40: adrp x0, #0x1e8d000
// 0x1069d44: ldr x0, [x0, #0x348]
// 0x1069d48: bl #0xf7d92c
// 0x1069d4c: adrp x0, #0x1e8d000
// 0x1069d50: ldr x0, [x0, #0x350]
// 0x1069d54: bl #0xf7d92c
// 0x1069d58: adrp x0, #0x1e8d000
// 0x1069d5c: ldr x0, [x0, #0x358]
// 0x1069d60: bl #0xf7d92c
// 0x1069d64: adrp x0, #0x1e8d000
// 0x1069d68: ldr x0, [x0, #0x360]
// 0x1069d6c: bl #0xf7d92c
// 0x1069d70: adrp x0, #0x1e8d000
// 0x1069d74: ldr x0, [x0, #0x368]
// 0x1069d78: bl #0xf7d92c
// 0x1069d7c: adrp x0, #0x1e8d000
// 0x1069d80: ldr x0, [x0, #0x370]
// 0x1069d84: bl #0xf7d92c
// 0x1069d88: adrp x0, #0x1e8d000
// 0x1069d8c: ldr x0, [x0, #0x378]
// 0x1069d90: bl #0xf7d92c
// 0x1069d94: adrp x0, #0x1e8d000
// 0x1069d98: ldr x0, [x0, #0x380]
// 0x1069d9c: bl #0xf7d92c
// 0x1069da0: adrp x0, #0x1e8d000
// 0x1069da4: ldr x0, [x0, #0x388]
// 0x1069da8: bl #0xf7d92c
// 0x1069dac: adrp x0, #0x1e8d000
// 0x1069db0: ldr x0, [x0, #0x310]
// 0x1069db4: bl #0xf7d92c
// 0x1069db8: adrp x0, #0x1e8d000
// 0x1069dbc: ldr x0, [x0, #0x390]
// 0x1069dc0: bl #0xf7d92c
// 0x1069dc4: adrp x0, #0x1e8c000
// 0x1069dc8: ldr x0, [x0, #0x230]
// 0x1069dcc: bl #0xf7d92c
// 0x1069dd0: adrp x0, #0x1e8c000
// 0x1069dd4: ldr x0, [x0, #0x8a8]
// 0x1069dd8: bl #0xf7d92c
// 0x1069ddc: adrp x0, #0x1e8d000
// 0x1069de0: ldr x0, [x0, #0x398]
// 0x1069de4: bl #0xf7d92c
// 0x1069de8: adrp x0, #0x1e8d000
// 0x1069dec: ldr x0, [x0, #0x3a0]
// 0x1069df0: bl #0xf7d92c
// 0x1069df4: mov w8, #1
// 0x1069df8: strb w8, [x20, #0x328]
// 0x1069dfc: adrp x8, #0x1e8c000
// 0x1069e00: ldr x8, [x8, #0xce0]
// 0x1069e04: str wzr, [sp, #0x18]
// 0x1069e08: str wzr, [sp, #0xc]
// 0x1069e0c: adrp x29, #0x1e8c000
// 0x1069e10: ldr x0, [x8]
// 0x1069e14: ldr x19, [x19, #0x20]
// 0x1069e18: ldr w8, [x0, #0xe0]
// 0x1069e1c: ldr x29, [x29, #0x230]
// 0x1069e20: cbnz w8, #0x1069e28
// 0x1069e24: bl #0xf7da5c
// 0x1069e28: adrp x28, #0x1e8c000
// 0x1069e2c: adrp x27, #0x1e8d000
// 0x1069e30: adrp x24, #0x1e8d000
// 0x1069e34: adrp x26, #0x1e8d000
// 0x1069e38: adrp x25, #0x1e8d000
// 0x1069e3c: ldr x28, [x28, #0x3a0]
// 0x1069e40: ldr x27, [x27, #0x368]
// 0x1069e44: ldr x24, [x24, #0x338]
// 0x1069e48: ldr x26, [x26, #0x310]
// 0x1069e4c: ldr x25, [x25, #0x318]
// 0x1069e50: mov x0, x19
// 0x1069e54: mov x1, xzr
// 0x1069e58: bl #0x1bb3680
// 0x1069e5c: mov x0, xzr
// 0x1069e60: bl #0x1bc7518
// 0x1069e64: adrp x8, #0x832000
// 0x1069e68: ldr x20, [x29]
// 0x1069e6c: ldr s9, [x8, #0x458]
// 0x1069e70: mov x9, x0
// 0x1069e74: mov w0, wzr
// 0x1069e78: fmov s8, #10.00000000
// 0x1069e7c: fmov s10, #5.00000000
// 0x1069e80: fmov s11, #-5.00000000
// 0x1069e84: mov w19, #0x14
// 0x1069e88: str wzr, [sp, #0x1c]
// 0x1069e8c: str x9, [sp]
// 0x1069e90: cbz x9, #0x1069fc0
// 0x1069e94: ldr w8, [x9, #0x18]
// 0x1069e98: cmp w0, w8
// 0x1069e9c: b.ge #0x1069fc0
// 0x1069ea0: mov w21, wzr
// 0x1069ea4: mov w1, w21
// 0x1069ea8: bl #0x10699c0
// 0x1069eac: mov x1, xzr
// 0x1069eb0: bl #0x1bc71a8
// 0x1069eb4: fabs s1, s0
// 0x1069eb8: fcmp s1, s9
// 0x1069ebc: str s0, [sp, #0x18]
// 0x1069ec0: b.ls #0x1069fac
// 0x1069ec4: ldr x0, [x28]
// 0x1069ec8: mov w1, #5
// 0x1069ecc: bl #0xf7d9d4
// 0x1069ed0: cbz x0, #0x106a508
// 0x1069ed4: ldr w8, [x0, #0x18]
// 0x1069ed8: mov x22, x0
// 0x1069edc: cbz w8, #0x106a504
// 0x1069ee0: mov x23, x22
// 0x1069ee4: str x20, [x23, #0x20]!
// 0x1069ee8: mov x0, x23
// 0x1069eec: mov x1, x20
// 0x1069ef0: bl #0xf7d8d0
// 0x1069ef4: ldr s0, [sp, #0x18]
// 0x1069ef8: mov w1, w21
// 0x1069efc: fcmp s0, #0.0
// 0x1069f00: cset w2, gt
// 0x1069f04: bl #0x1069b08
// 0x1069f08: ldur w8, [x23, #-8]
// 0x1069f0c: cmp w8, #1
// 0x1069f10: b.ls #0x106a504
// 0x1069f14: mov x20, x22
// 0x1069f18: str x0, [x20, #0x28]!
// 0x1069f1c: mov x1, x0
// 0x1069f20: mov x0, x20
// 0x1069f24: bl #0xf7d8d0
// 0x1069f28: ldur w8, [x20, #-0x10]
// 0x1069f2c: cmp w8, #2
// 0x1069f30: b.ls #0x106a504
// 0x1069f34: adrp x8, #0x1e8d000
// 0x1069f38: ldr x8, [x8, #0x398]
// 0x1069f3c: mov x20, x22
// 0x1069f40: ldr x1, [x8]
// 0x1069f44: str x1, [x20, #0x30]!
// 0x1069f48: mov x0, x20
// 0x1069f4c: bl #0xf7d8d0
// 0x1069f50: ldr x1, [x27]
// 0x1069f54: add x0, sp, #0x18
// 0x1069f58: mov x2, xzr
// 0x1069f5c: bl #0x1959570
// 0x1069f60: ldur w8, [x20, #-0x18]
// 0x1069f64: cmp w8, #3
// 0x1069f68: b.ls #0x106a504
// 0x1069f6c: mov x20, x22
// 0x1069f70: str x0, [x20, #0x38]!
// 0x1069f74: mov x1, x0
// 0x1069f78: mov x0, x20
// 0x1069f7c: bl #0xf7d8d0
// 0x1069f80: ldur w8, [x20, #-0x20]
// 0x1069f84: cmp w8, #4
// 0x1069f88: b.ls #0x106a504
// 0x1069f8c: ldr x1, [x24]
// 0x1069f90: mov x0, x22
// 0x1069f94: str x1, [x0, #0x40]!
// 0x1069f98: bl #0xf7d8d0
// 0x1069f9c: mov x0, x22
// 0x1069fa0: mov x1, xzr
// 0x1069fa4: bl #0x17f6a44
// 0x1069fa8: mov x20, x0
// 0x1069fac: cmp w21, #9
// 0x1069fb0: b.eq #0x1069fd0
// 0x1069fb4: ldr w0, [sp, #0x1c]
// 0x1069fb8: add w21, w21, #1
// 0x1069fbc: b #0x1069ea4
// 0x1069fc0: adrp x8, #0x1e8d000
// 0x1069fc4: ldr x8, [x8, #0x388]
// 0x1069fc8: ldr x20, [x8]
// 0x1069fcc: b #0x106a150
// 0x1069fd0: mov w8, wzr
// 0x1069fd4: mov x21, x29
// 0x1069fd8: str wzr, [sp, #0xc]
// 0x1069fdc: ldr w9, [sp, #0x1c]
// 0x1069fe0: cmn w8, #1
// 0x1069fe4: mov x1, xzr
// 0x1069fe8: madd w8, w9, w19, w8
// 0x1069fec: ccmp w9, #4, #2, gt
// 0x1069ff0: add w8, w8, #0x15e
// 0x1069ff4: csel w0, w8, wzr, lo
// 0x1069ff8: bl #0x1bc76bc
// 0x1069ffc: tbz w0, #0, #0x106a028
// 0x106a000: add x0, sp, #0xc
// 0x106a004: mov x1, xzr
// 0x106a008: bl #0x1945824
// 0x106a00c: ldr x1, [x26]
// 0x106a010: ldr x3, [x25]
// 0x106a014: mov x2, x0
// 0x106a018: mov x0, x20
// 0x106a01c: mov x4, xzr
// 0x106a020: bl #0x17f693c
// 0x106a024: mov x20, x0
// 0x106a028: ldr w8, [sp, #0xc]
// 0x106a02c: add w8, w8, #1
// 0x106a030: cmp w8, #0x14
// 0x106a034: str w8, [sp, #0xc]
// 0x106a038: b.lt #0x1069fdc
// 0x106a03c: ldr x1, [x21]
// 0x106a040: mov x0, x20
// 0x106a044: mov x2, xzr
// 0x106a048: bl #0x17f610c
// 0x106a04c: adrp x8, #0x1e8d000
// 0x106a050: ldr x8, [x8, #0x350]
// 0x106a054: tst w0, #1
// 0x106a058: mov w1, #5
// 0x106a05c: ldr x9, [x8]
// 0x106a060: ldr x8, [x28]
// 0x106a064: csel x21, x9, x20, ne
// 0x106a068: mov x0, x8
// 0x106a06c: bl #0xf7d9d4
// 0x106a070: mov x20, x0
// 0x106a074: add x0, sp, #0x1c
// 0x106a078: mov x1, xzr
// 0x106a07c: bl #0x1945824
// 0x106a080: cbz x20, #0x106a508
// 0x106a084: ldr w8, [x20, #0x18]
// 0x106a088: cbz w8, #0x106a504
// 0x106a08c: mov x22, x20
// 0x106a090: str x0, [x22, #0x20]!
// 0x106a094: mov x1, x0
// 0x106a098: mov x0, x22
// 0x106a09c: bl #0xf7d8d0
// 0x106a0a0: ldur w8, [x22, #-8]
// 0x106a0a4: cmp w8, #1
// 0x106a0a8: b.ls #0x106a504
// 0x106a0ac: adrp x8, #0x1e8d000
// 0x106a0b0: ldr x8, [x8, #0x378]
// 0x106a0b4: mov x0, x20
// 0x106a0b8: ldr x1, [x8]
// 0x106a0bc: str x1, [x0, #0x28]!
// 0x106a0c0: bl #0xf7d8d0
// 0x106a0c4: ldr x10, [sp]
// 0x106a0c8: ldrsw x8, [sp, #0x1c]
// 0x106a0cc: ldr w9, [x10, #0x18]
// 0x106a0d0: cmp w8, w9
// 0x106a0d4: b.hs #0x106a504
// 0x106a0d8: ldr w9, [x20, #0x18]
// 0x106a0dc: cmp w9, #2
// 0x106a0e0: b.ls #0x106a504
// 0x106a0e4: add x8, x10, x8, lsl #3
// 0x106a0e8: ldr x1, [x8, #0x20]
// 0x106a0ec: mov x22, x20
// 0x106a0f0: str x1, [x22, #0x30]!
// 0x106a0f4: mov x0, x22
// 0x106a0f8: bl #0xf7d8d0
// 0x106a0fc: ldur w8, [x22, #-0x18]
// 0x106a100: cmp w8, #3
// 0x106a104: b.ls #0x106a504
// 0x106a108: adrp x8, #0x1e8d000
// 0x106a10c: ldr x8, [x8, #0x328]
// 0x106a110: mov x22, x20
// 0x106a114: ldr x1, [x8]
// 0x106a118: str x1, [x22, #0x38]!
// 0x106a11c: mov x0, x22
// 0x106a120: bl #0xf7d8d0
// 0x106a124: ldur w8, [x22, #-0x20]
// 0x106a128: cmp w8, #4
// 0x106a12c: b.ls #0x106a504
// 0x106a130: mov x0, x20
// 0x106a134: str x21, [x0, #0x40]!
// 0x106a138: mov x1, x21
// 0x106a13c: bl #0xf7d8d0
// 0x106a140: mov x0, x20
// 0x106a144: mov x1, xzr
// 0x106a148: bl #0x17f6a44
// 0x106a14c: mov x20, x0
// 0x106a150: mov x0, xzr
// 0x106a154: bl #0x1b77c10
// 0x106a158: ldr s12, [sp, #0x1c]
// 0x106a15c: sub w8, w0, #0x14
// 0x106a160: sub w9, w0, #0x11
// 0x106a164: cmp w8, #0
// 0x106a168: mov x0, xzr
// 0x106a16c: csel w21, w9, w8, lt
// 0x106a170: bl #0x1b77c38
// 0x106a174: adrp x8, #0x1e8c000
// 0x106a178: ldr x8, [x8, #0xce0]
// 0x106a17c: sub w22, w0, #0x82
// 0x106a180: ldr x8, [x8]
// 0x106a184: ldr w9, [x8, #0xe0]
// 0x106a188: cbnz w9, #0x106a194
// 0x106a18c: mov x0, x8
// 0x106a190: bl #0xf7da5c
// 0x106a194: asr w8, w21, #2
// 0x106a198: scvtf s0, s12
// 0x106a19c: scvtf s1, w8
// 0x106a1a0: fmul s0, s0, s1
// 0x106a1a4: fadd s0, s0, s8
// 0x106a1a8: fadd s2, s1, s11
// 0x106a1ac: fadd s0, s0, s10
// 0x106a1b0: scvtf s3, w22
// 0x106a1b4: fmov s1, #10.00000000
// 0x106a1b8: mov x0, x20
// 0x106a1bc: mov x1, xzr
// 0x106a1c0: bl #0x1bb5034
// 0x106a1c4: ldr w8, [sp, #0x1c]
// 0x106a1c8: ldr x20, [x29]
// 0x106a1cc: ldr x9, [sp]
// 0x106a1d0: add w0, w8, #1
// 0x106a1d4: cmp w0, #4
// 0x106a1d8: str w0, [sp, #0x1c]
// 0x106a1dc: b.lt #0x1069e90
// 0x106a1e0: mov w0, #0x1b
// 0x106a1e4: mov x1, xzr
// 0x106a1e8: bl #0x1bc76bc
// 0x106a1ec: tbz w0, #0, #0x106a20c
// 0x106a1f0: adrp x8, #0x1e8d000
// 0x106a1f4: ldr x8, [x8, #0x370]
// 0x106a1f8: mov x0, x20
// 0x106a1fc: mov x2, xzr
// 0x106a200: ldr x1, [x8]
// 0x106a204: bl #0x17ed2c8
// 0x106a208: mov x20, x0
// 0x106a20c: adrp x21, #0x1e8d000
// 0x106a210: adrp x22, #0x1e8c000
// 0x106a214: adrp x23, #0x1e8c000
// 0x106a218: adrp x24, #0x1e8d000
// 0x106a21c: adrp x25, #0x1e8d000
// 0x106a220: ldr x21, [x21, #0x380]
// 0x106a224: ldr x22, [x22, #0x8a8]
// 0x106a228: ldr x23, [x23, #0x248]
// 0x106a22c: ldr x24, [x24, #0x348]
// 0x106a230: ldr x25, [x25, #0x390]
// 0x106a234: mov w0, #0xd
// 0x106a238: mov x1, xzr
// 0x106a23c: bl #0x1bc76bc
// 0x106a240: tbz w0, #0, #0x106a260
// 0x106a244: adrp x8, #0x1e8d000
// 0x106a248: ldr x8, [x8, #0x320]
// 0x106a24c: mov x0, x20
// 0x106a250: mov x2, xzr
// 0x106a254: ldr x1, [x8]
// 0x106a258: bl #0x17ed2c8
// 0x106a25c: mov x20, x0
// 0x106a260: mov w0, #0x130
// 0x106a264: mov x1, xzr
// 0x106a268: bl #0x1bc76bc
// 0x106a26c: tbz w0, #0, #0x106a28c
// 0x106a270: adrp x8, #0x1e8d000
// 0x106a274: ldr x8, [x8, #0x340]
// 0x106a278: mov x0, x20
// 0x106a27c: mov x2, xzr
// 0x106a280: ldr x1, [x8]
// 0x106a284: bl #0x17ed2c8
// 0x106a288: mov x20, x0
// 0x106a28c: mov w0, #0x12f
// 0x106a290: mov x1, xzr
// 0x106a294: bl #0x1bc76bc
// 0x106a298: tbz w0, #0, #0x106a2b8
// 0x106a29c: adrp x8, #0x1e8d000
// 0x106a2a0: ldr x8, [x8, #0x358]
// 0x106a2a4: mov x0, x20
// 0x106a2a8: mov x2, xzr
// 0x106a2ac: ldr x1, [x8]
// 0x106a2b0: bl #0x17ed2c8
// 0x106a2b4: mov x20, x0
// 0x106a2b8: mov w0, #0x132
// 0x106a2bc: mov x1, xzr
// 0x106a2c0: bl #0x1bc76bc
// 0x106a2c4: tbz w0, #0, #0x106a2e4
// 0x106a2c8: adrp x8, #0x1e8d000
// 0x106a2cc: ldr x8, [x8, #0x3a0]
// 0x106a2d0: mov x0, x20
// 0x106a2d4: mov x2, xzr
// 0x106a2d8: ldr x1, [x8]
// 0x106a2dc: bl #0x17ed2c8
// 0x106a2e0: mov x20, x0
// 0x106a2e4: mov w0, #0x131
// 0x106a2e8: mov x1, xzr
// 0x106a2ec: bl #0x1bc76bc
// 0x106a2f0: tbz w0, #0, #0x106a310
// 0x106a2f4: adrp x8, #0x1e8d000
// 0x106a2f8: ldr x8, [x8, #0x360]
// 0x106a2fc: mov x0, x20
// 0x106a300: mov x2, xzr
// 0x106a304: ldr x1, [x8]
// 0x106a308: bl #0x17ed2c8
// 0x106a30c: mov x20, x0
// 0x106a310: mov w0, #0x20
// 0x106a314: mov x1, xzr
// 0x106a318: bl #0x1bc76bc
// 0x106a31c: tbz w0, #0, #0x106a33c
// 0x106a320: adrp x8, #0x1e8d000
// 0x106a324: ldr x8, [x8, #0x330]
// 0x106a328: mov x0, x20
// 0x106a32c: mov x2, xzr
// 0x106a330: ldr x1, [x8]
// 0x106a334: bl #0x17ed2c8
// 0x106a338: mov x20, x0
// 0x106a33c: mov x0, xzr
// 0x106a340: bl #0x1b77c38
// 0x106a344: mov w19, w0
// 0x106a348: mov x0, xzr
// 0x106a34c: bl #0x1b77c10
// 0x106a350: adrp x9, #0x1e8c000
// 0x106a354: ldr x9, [x9, #0xce0]
// 0x106a358: mov w8, w0
// 0x106a35c: sub w10, w19, #0x64
// 0x106a360: sub w8, w8, #0x14
// 0x106a364: ldr x0, [x9]
// 0x106a368: scvtf s8, w10
// 0x106a36c: scvtf s9, w8
// 0x106a370: ldr w9, [x0, #0xe0]
// 0x106a374: cbnz w9, #0x106a37c
// 0x106a378: bl #0xf7da5c
// 0x106a37c: mov w8, #0x42480000
// 0x106a380: fmov s0, #10.00000000
// 0x106a384: fmov s3, w8
// 0x106a388: mov v1.16b, v8.16b
// 0x106a38c: mov v2.16b, v9.16b
// 0x106a390: mov x0, x20
// 0x106a394: mov x1, xzr
// 0x106a398: bl #0x1bb5034
// 0x106a39c: mov x0, xzr
// 0x106a3a0: bl #0x1b77c38
// 0x106a3a4: ldr x8, [x25]
// 0x106a3a8: sub w9, w0, #0x28
// 0x106a3ac: scvtf s1, w9
// 0x106a3b0: mov w9, #0x42c80000
// 0x106a3b4: fmov s0, #10.00000000
// 0x106a3b8: fmov s3, #30.00000000
// 0x106a3bc: fmov s2, w9
// 0x106a3c0: mov x0, x8
// 0x106a3c4: mov x1, xzr
// 0x106a3c8: bl #0x1bb5444
// 0x106a3cc: tbz w0, #0, #0x106a3d8
// 0x106a3d0: mov x0, xzr
// 0x106a3d4: bl #0x1bc74f0
// 0x106a3d8: mov x0, xzr
// 0x106a3dc: bl #0x1b77c38
// 0x106a3e0: adrp x8, #0x1e8c000
// 0x106a3e4: ldr x8, [x8, #0xce0]
// 0x106a3e8: sub w10, w0, #0x28
// 0x106a3ec: scvtf s8, w10
// 0x106a3f0: ldr x8, [x8]
// 0x106a3f4: ldr w9, [x8, #0xe0]
// 0x106a3f8: cbnz w9, #0x106a404
// 0x106a3fc: mov x0, x8
// 0x106a400: bl #0xf7da5c
// 0x106a404: ldr x0, [x24]
// 0x106a408: mov w8, #0x42e60000
// 0x106a40c: mov w9, #0x42c80000
// 0x106a410: fmov s3, #30.00000000
// 0x106a414: fmov s0, w8
// 0x106a418: fmov s2, w9
// 0x106a41c: mov v1.16b, v8.16b
// 0x106a420: mov x1, xzr
// 0x106a424: bl #0x1bb5444
// 0x106a428: tbz w0, #0, #0x106a444
// 0x106a42c: ldr x0, [x23]
// 0x106a430: ldr w8, [x0, #0xe0]
// 0x106a434: cbnz w8, #0x106a43c
// 0x106a438: bl #0xf7da5c
// 0x106a43c: mov x0, xzr
// 0x106a440: bl #0x1b6d458
// 0x106a444: mov x0, xzr
// 0x106a448: bl #0x1b77c38
// 0x106a44c: mov w19, w0
// 0x106a450: mov x0, xzr
// 0x106a454: bl #0x1b77c10
// 0x106a458: ldr x8, [x23]
// 0x106a45c: mov w20, w0
// 0x106a460: ldr w9, [x8, #0xe0]
// 0x106a464: cbnz w9, #0x106a470
// 0x106a468: mov x0, x8
// 0x106a46c: bl #0xf7da5c
// 0x106a470: mov x0, xzr
// 0x106a474: bl #0x1b6d568
// 0x106a478: ldr x8, [x21]
// 0x106a47c: ldr x2, [x22]
// 0x106a480: mov x1, x0
// 0x106a484: mov x3, xzr
// 0x106a488: mov x0, x8
// 0x106a48c: bl #0x17f661c
// 0x106a490: adrp x8, #0x1e8c000
// 0x106a494: ldr x8, [x8, #0xce0]
// 0x106a498: mov x21, x0
// 0x106a49c: ldr x8, [x8]
// 0x106a4a0: ldr w9, [x8, #0xe0]
// 0x106a4a4: cbnz w9, #0x106a4b0
// 0x106a4a8: mov x0, x8
// 0x106a4ac: bl #0xf7da5c
// 0x106a4b0: sub w8, w20, #0xe6
// 0x106a4b4: sub w9, w19, #0x28
// 0x106a4b8: scvtf s2, w8
// 0x106a4bc: mov w8, #0x435c0000
// 0x106a4c0: scvtf s1, w9
// 0x106a4c4: fmov s3, #30.00000000
// 0x106a4c8: fmov s0, w8
// 0x106a4cc: mov x0, x21
// 0x106a4d0: mov x1, xzr
// 0x106a4d4: bl #0x1bb5034
// 0x106a4d8: ldp x20, x19, [sp, #0x90]
// 0x106a4dc: ldp x22, x21, [sp, #0x80]
// 0x106a4e0: ldp x24, x23, [sp, #0x70]
// 0x106a4e4: ldp x26, x25, [sp, #0x60]
// 0x106a4e8: ldp x28, x27, [sp, #0x50]
// 0x106a4ec: ldp x29, x30, [sp, #0x40]
// 0x106a4f0: ldp d9, d8, [sp, #0x30]
// 0x106a4f4: ldp d11, d10, [sp, #0x20]
// 0x106a4f8: ldr d12, [sp, #0x10]
// 0x106a4fc: add sp, sp, #0xa0
// 0x106a500: ret
// 0x106a504: bl #0xf7db7c
// 0x106a508: bl #0xf7db74
```

## `GamepadHardwareTester.ctor` — RVA `0xc6a50c`

- Decompiled symbol: `GamepadHardwareTester_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `424` bytes
- Result: `pseudocode`

```c
long long GamepadHardwareTester_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
