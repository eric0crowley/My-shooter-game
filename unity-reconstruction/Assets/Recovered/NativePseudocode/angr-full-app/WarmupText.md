# Native pseudocode: WarmupText

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `WarmupText.OnEnable` — RVA `0xc9281c`

- Decompiled symbol: `WarmupText_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `100` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WarmupText_Recovered` matched 2 offsets against `WarmupText` metadata (confidence 1.00).

```c
typedef struct WarmupText_Recovered {
    char padding_0[36];
    unsigned int oldWarmup;
    char padding_28[24];
    long long uiTextComponent;
} WarmupText_Recovered;

extern long long g_1efd0b0;
extern char g_1fab459;

long long WarmupText_OnEnable(struct_0 *ptr)
{
    long long v0;  // x0
    struct_0 *p;  // x19
    unsigned long v2;  // x0

    if (!(g_1fab459 & 1))
    {
        sub_f7d92c(&g_1efd0b0);
        g_1fab459 = 1;
    }
    v0 = sub_1231bc8(ptr, g_1efd0b0);
    ptr->field_40 = v0;
    p = &ptr->field_40;
    v2 = sub_f7d8d0(p, v0);
    *((unsigned int *)&p->padding_0[28]) = 0xc4000000;
    return v2;
}
```

## `WarmupText.Update` — RVA `0xc92880`

- Decompiled symbol: `WarmupText_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `424` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1092880: sub sp, sp, #0x30
// 0x1092884: str d8, [sp, #0x10]
// 0x1092888: str x30, [sp, #0x18]
// 0x109288c: stp x20, x19, [sp, #0x20]
// 0x1092890: adrp x20, #0x1fab000
// 0x1092894: ldrb w8, [x20, #0x45a]
// 0x1092898: mov x19, x0
// 0x109289c: tbnz w8, #0, #0x10928cc
// 0x10928a0: adrp x0, #0x1e8e000
// 0x10928a4: ldr x0, [x0, #0x130]
// 0x10928a8: bl #0xf7d92c
// 0x10928ac: adrp x0, #0x1e8e000
// 0x10928b0: ldr x0, [x0, #0x138]
// 0x10928b4: bl #0xf7d92c
// 0x10928b8: adrp x0, #0x1e8e000
// 0x10928bc: ldr x0, [x0, #0x140]
// 0x10928c0: bl #0xf7d92c
// 0x10928c4: mov w8, #1
// 0x10928c8: strb w8, [x20, #0x45a]
// 0x10928cc: str wzr, [sp, #4]
// 0x10928d0: ldp s8, s0, [x19, #0x20]
// 0x10928d4: fcmp s8, s0
// 0x10928d8: b.eq #0x1092a10
// 0x10928dc: ldrb w8, [x19, #0x39]
// 0x10928e0: cbz w8, #0x1092908
// 0x10928e4: ldr x0, [x19, #0x40]
// 0x10928e8: cbz x0, #0x1092a24
// 0x10928ec: adrp x9, #0x1e8e000
// 0x10928f0: ldr x8, [x0]
// 0x10928f4: ldr x9, [x9, #0x138]
// 0x10928f8: ldr x2, [x8, #0x5f0]
// 0x10928fc: ldr x1, [x9]
// 0x1092900: ldr x9, [x8, #0x5e8]
// 0x1092904: b #0x10929e4
// 0x1092908: ldrb w8, [x19, #0x38]
// 0x109290c: ldr x20, [x19, #0x40]
// 0x1092910: cbz w8, #0x109292c
// 0x1092914: cbz x20, #0x1092a24
// 0x1092918: adrp x9, #0x1e8e000
// 0x109291c: ldr x8, [x20]
// 0x1092920: ldr x9, [x9, #0x130]
// 0x1092924: ldr x1, [x9]
// 0x1092928: b #0x10929d8
// 0x109292c: fcvt d0, s8
// 0x1092930: add x0, sp, #8
// 0x1092934: bl #0x1db0c60
// 0x1092938: fcmp s8, #0.0
// 0x109293c: b.ge #0x1092958
// 0x1092940: fmov d1, #-0.50000000
// 0x1092944: fcmp d0, d1
// 0x1092948: b.ne #0x1092984
// 0x109294c: ldr d0, [sp, #8]
// 0x1092950: fmov s1, #-1.00000000
// 0x1092954: b #0x109296c
// 0x1092958: fmov d1, #0.50000000
// 0x109295c: fcmp d0, d1
// 0x1092960: b.ne #0x1092994
// 0x1092964: ldr d0, [sp, #8]
// 0x1092968: fmov s1, #1.00000000
// 0x109296c: fcvtzs x8, d0
// 0x1092970: fcvt s0, d0
// 0x1092974: fadd s1, s0, s1
// 0x1092978: tst x8, #1
// 0x109297c: fcsel s0, s0, s1, eq
// 0x1092980: b #0x10929a0
// 0x1092984: fmov s0, #-0.50000000
// 0x1092988: fadd s0, s8, s0
// 0x109298c: frintp s0, s0
// 0x1092990: b #0x10929a0
// 0x1092994: fmov s0, #0.50000000
// 0x1092998: fadd s0, s8, s0
// 0x109299c: frintm s0, s0
// 0x10929a0: add x0, sp, #4
// 0x10929a4: mov x1, xzr
// 0x10929a8: str s0, [sp, #4]
// 0x10929ac: bl #0x1959468
// 0x10929b0: adrp x8, #0x1e8e000
// 0x10929b4: ldr x8, [x8, #0x140]
// 0x10929b8: mov x1, x0
// 0x10929bc: mov x2, xzr
// 0x10929c0: ldr x8, [x8]
// 0x10929c4: mov x0, x8
// 0x10929c8: bl #0x17ed2c8
// 0x10929cc: cbz x20, #0x1092a24
// 0x10929d0: ldr x8, [x20]
// 0x10929d4: mov x1, x0
// 0x10929d8: ldr x9, [x8, #0x5e8]
// 0x10929dc: ldr x2, [x8, #0x5f0]
// 0x10929e0: mov x0, x20
// 0x10929e4: blr x9
// 0x10929e8: ldr x0, [x19, #0x40]
// 0x10929ec: cbz x0, #0x1092a24
// 0x10929f0: ldr x8, [x0]
// 0x10929f4: ldp s2, s3, [x19, #0x30]
// 0x10929f8: ldp s0, s1, [x19, #0x28]
// 0x10929fc: ldr x9, [x8, #0x2a8]
// 0x1092a00: ldr x1, [x8, #0x2b0]
// 0x1092a04: blr x9
// 0x1092a08: ldr s0, [x19, #0x20]
// 0x1092a0c: str s0, [x19, #0x24]
// 0x1092a10: ldp x20, x19, [sp, #0x20]
// 0x1092a14: ldr x30, [sp, #0x18]
// 0x1092a18: ldr d8, [sp, #0x10]
// 0x1092a1c: add sp, sp, #0x30
// 0x1092a20: ret
// 0x1092a24: bl #0xf7db74
```

## `WarmupText.ctor` — RVA `0xc92a28`

- Decompiled symbol: `WarmupText_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[36];
    unsigned int field_24;
} struct_0;

long long WarmupText_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_24 = 0xc4000000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
