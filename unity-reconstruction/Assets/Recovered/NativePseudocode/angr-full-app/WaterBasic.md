# Native pseudocode: WaterBasic

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `WaterBasic.Update` — RVA `0xce1b24`

- Decompiled symbol: `WaterBasic_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `508` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10e1b24: str d12, [sp, #-0x50]!
// 0x10e1b28: stp d11, d10, [sp, #8]
// 0x10e1b2c: stp d9, d8, [sp, #0x18]
// 0x10e1b30: str x30, [sp, #0x28]
// 0x10e1b34: stp x22, x21, [sp, #0x30]
// 0x10e1b38: stp x20, x19, [sp, #0x40]
// 0x10e1b3c: adrp x21, #0x1fab000
// 0x10e1b40: adrp x22, #0x1e8e000
// 0x10e1b44: adrp x20, #0x1e8c000
// 0x10e1b48: ldrb w8, [x21, #0x63f]
// 0x10e1b4c: ldr x22, [x22, #0x68]
// 0x10e1b50: ldr x20, [x20, #0xd8]
// 0x10e1b54: mov x19, x0
// 0x10e1b58: tbnz w8, #0, #0x10e1ba0
// 0x10e1b5c: adrp x0, #0x1e8e000
// 0x10e1b60: ldr x0, [x0, #0x68]
// 0x10e1b64: bl #0xf7d92c
// 0x10e1b68: adrp x0, #0x1e8c000
// 0x10e1b6c: ldr x0, [x0, #0xd8]
// 0x10e1b70: bl #0xf7d92c
// 0x10e1b74: adrp x0, #0x1e8f000
// 0x10e1b78: ldr x0, [x0, #0x9a8]
// 0x10e1b7c: bl #0xf7d92c
// 0x10e1b80: adrp x0, #0x1e8f000
// 0x10e1b84: ldr x0, [x0, #0x9b0]
// 0x10e1b88: bl #0xf7d92c
// 0x10e1b8c: adrp x0, #0x1e8f000
// 0x10e1b90: ldr x0, [x0, #0x9b8]
// 0x10e1b94: bl #0xf7d92c
// 0x10e1b98: mov w8, #1
// 0x10e1b9c: strb w8, [x21, #0x63f]
// 0x10e1ba0: ldr x1, [x22]
// 0x10e1ba4: mov x0, x19
// 0x10e1ba8: bl #0x1231bc8
// 0x10e1bac: ldr x8, [x20]
// 0x10e1bb0: mov x19, x0
// 0x10e1bb4: ldr w9, [x8, #0xe0]
// 0x10e1bb8: cbnz w9, #0x10e1bc4
// 0x10e1bbc: mov x0, x8
// 0x10e1bc0: bl #0xf7da5c
// 0x10e1bc4: mov x0, x19
// 0x10e1bc8: mov x1, xzr
// 0x10e1bcc: bl #0x1b98274
// 0x10e1bd0: tbz w0, #0, #0x10e1d00
// 0x10e1bd4: cbz x19, #0x10e1d1c
// 0x10e1bd8: mov x0, x19
// 0x10e1bdc: mov x1, xzr
// 0x10e1be0: bl #0x1b79c08
// 0x10e1be4: ldr x8, [x20]
// 0x10e1be8: mov x19, x0
// 0x10e1bec: ldr w9, [x8, #0xe0]
// 0x10e1bf0: cbnz w9, #0x10e1bfc
// 0x10e1bf4: mov x0, x8
// 0x10e1bf8: bl #0xf7da5c
// 0x10e1bfc: mov x0, x19
// 0x10e1c00: mov x1, xzr
// 0x10e1c04: bl #0x1b98274
// 0x10e1c08: tbz w0, #0, #0x10e1d00
// 0x10e1c0c: cbz x19, #0x10e1d1c
// 0x10e1c10: adrp x8, #0x1e8f000
// 0x10e1c14: ldr x8, [x8, #0x9a8]
// 0x10e1c18: mov x0, x19
// 0x10e1c1c: mov x2, xzr
// 0x10e1c20: ldr x1, [x8]
// 0x10e1c24: bl #0x1b7ba20
// 0x10e1c28: adrp x8, #0x1e8f000
// 0x10e1c2c: ldr x8, [x8, #0x9b0]
// 0x10e1c30: mov x0, x19
// 0x10e1c34: mov x2, xzr
// 0x10e1c38: mov v8.16b, v0.16b
// 0x10e1c3c: ldr x1, [x8]
// 0x10e1c40: mov v9.16b, v1.16b
// 0x10e1c44: mov v10.16b, v2.16b
// 0x10e1c48: mov v11.16b, v3.16b
// 0x10e1c4c: bl #0x1b7b96c
// 0x10e1c50: mov x0, xzr
// 0x10e1c54: mov v12.16b, v0.16b
// 0x10e1c58: bl #0x1b9ad30
// 0x10e1c5c: fmov s1, #20.00000000
// 0x10e1c60: fdiv s0, s0, s1
// 0x10e1c64: fmul s0, s12, s0
// 0x10e1c68: fmul s2, s8, s0
// 0x10e1c6c: adrp x8, #0x1e8f000
// 0x10e1c70: fmul s4, s9, s0
// 0x10e1c74: frintm s6, s2
// 0x10e1c78: ldr x8, [x8, #0x9b8]
// 0x10e1c7c: fmul s5, s10, s0
// 0x10e1c80: fsub s2, s2, s6
// 0x10e1c84: frintm s6, s4
// 0x10e1c88: fmul s0, s11, s0
// 0x10e1c8c: fsub s4, s4, s6
// 0x10e1c90: frintm s6, s5
// 0x10e1c94: fmov s1, #1.00000000
// 0x10e1c98: fsub s5, s5, s6
// 0x10e1c9c: frintm s6, s0
// 0x10e1ca0: fmov s3, wzr
// 0x10e1ca4: fsub s6, s0, s6
// 0x10e1ca8: fmin s0, s2, s1
// 0x10e1cac: fcmp s2, #0.0
// 0x10e1cb0: ldr x1, [x8]
// 0x10e1cb4: fmin s2, s4, s1
// 0x10e1cb8: fcsel s0, s0, s3, pl
// 0x10e1cbc: fcmp s4, #0.0
// 0x10e1cc0: mov x0, x19
// 0x10e1cc4: ldp x20, x19, [sp, #0x40]
// 0x10e1cc8: ldp x22, x21, [sp, #0x30]
// 0x10e1ccc: ldr x30, [sp, #0x28]
// 0x10e1cd0: ldp d9, d8, [sp, #0x18]
// 0x10e1cd4: ldp d11, d10, [sp, #8]
// 0x10e1cd8: fmin s4, s5, s1
// 0x10e1cdc: fmin s7, s6, s1
// 0x10e1ce0: fcsel s1, s2, s3, pl
// 0x10e1ce4: fcmp s5, #0.0
// 0x10e1ce8: fcsel s2, s4, s3, pl
// 0x10e1cec: fcmp s6, #0.0
// 0x10e1cf0: fcsel s3, s7, s3, pl
// 0x10e1cf4: mov x2, xzr
// 0x10e1cf8: ldr d12, [sp], #0x50
// 0x10e1cfc: b #0x1b7b76c
// 0x10e1d00: ldp x20, x19, [sp, #0x40]
// 0x10e1d04: ldp x22, x21, [sp, #0x30]
// 0x10e1d08: ldr x30, [sp, #0x28]
// 0x10e1d0c: ldp d9, d8, [sp, #0x18]
// 0x10e1d10: ldp d11, d10, [sp, #8]
// 0x10e1d14: ldr d12, [sp], #0x50
// 0x10e1d18: ret
// 0x10e1d1c: bl #0xf7db74
```

## `WaterBasic.ctor` — RVA `0xce1d20`

- Decompiled symbol: `WaterBasic_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long WaterBasic_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
