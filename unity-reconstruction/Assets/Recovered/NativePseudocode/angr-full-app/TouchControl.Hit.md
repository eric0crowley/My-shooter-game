# Native pseudocode: TouchControl.Hit

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchControl.Hit.Reset` — RVA `0xc52c98`

- Decompiled symbol: `TouchControl_Hit_Reset`
- Metadata signature: `public void Reset() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

long long TouchControl_Hit_Reset(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_10 = 0;
    v0 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `TouchControl.Hit.IsEmpty` — RVA `0xc52f48`

- Decompiled symbol: `TouchControl_Hit_IsEmpty`
- Metadata signature: `public bool IsEmpty() { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab25c;

void TouchControl_Hit_IsEmpty(unsigned long a0)
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
    if (!(g_1fab25c & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab25c = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    Object__op_Equality();
    return;
}
```

## `TouchControl.Hit.CopyFrom` — RVA `0xc52fa8`

- Decompiled symbol: `TouchControl_Hit_CopyFrom`
- Metadata signature: `public void CopyFrom(TouchControl.Hit b) { }`
- Native interval: `108` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControl_Hit_Recovered` matched 8 offsets against `TouchControl.Hit` metadata (confidence 1.00).

```c
typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
    unsigned int field_18;
    char field_1c;
    char padding_1d[3];
    unsigned long long field_20;
    unsigned long long field_28;
    unsigned long long field_30;
    unsigned long long field_38;
    unsigned int field_40;
} struct_0;

typedef struct TouchControl_Hit_Recovered {
    char padding_0[16];
    long long c;
    unsigned int depth;
    char indirectHit;
    char padding_1d[3];
    unsigned long long localPos;
    unsigned long long closestLocalPos;
    unsigned long long screenPos;
    unsigned long long closestScreenPos;
    unsigned int screenDistSqPx;
} TouchControl_Hit_Recovered;

long long TouchControl_Hit_CopyFrom(struct_1 *p, struct_0 *addr)
{
    long long v0;  // x1
    struct_1 *ptr;  // x20
    unsigned long v2;  // x0

    if (addr)
    {
        v0 = addr->field_10;
        p->field_10 = v0;
        ptr = &p->field_10;
        v2 = sub_f7d8d0(ptr, v0);
        *((unsigned int *)&ptr->padding_0[8]) = addr->field_18;
        ptr->padding_0[12] = addr->field_1c;
        ptr->field_10 = addr->field_20;
        *((unsigned long long *)&ptr->field_18) = addr->field_28;
        ptr->field_20 = addr->field_30;
        ptr->field_28 = addr->field_38;
        *((unsigned int *)&ptr->field_30) = addr->field_40;
        return v2;
    }
    sub_f7db74();
}
```

## `TouchControl.Hit.IsHigherThan` — RVA `0xc53014`

- Decompiled symbol: `TouchControl_Hit_IsHigherThan`
- Metadata signature: `public bool IsHigherThan(TouchControl.Hit r) { }`
- Native interval: `1160` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1053014: sub sp, sp, #0x50
// 0x1053018: stp d9, d8, [sp, #0x10]
// 0x105301c: stp x30, x23, [sp, #0x20]
// 0x1053020: stp x22, x21, [sp, #0x30]
// 0x1053024: stp x20, x19, [sp, #0x40]
// 0x1053028: adrp x21, #0x1fab000
// 0x105302c: adrp x22, #0x1e8c000
// 0x1053030: ldrb w8, [x21, #0x25d]
// 0x1053034: ldr x22, [x22, #0xd8]
// 0x1053038: mov x20, x1
// 0x105303c: mov x19, x0
// 0x1053040: tbnz w8, #0, #0x1053064
// 0x1053044: adrp x0, #0x1e8c000
// 0x1053048: ldr x0, [x0, #0xd90]
// 0x105304c: bl #0xf7d92c
// 0x1053050: adrp x0, #0x1e8c000
// 0x1053054: ldr x0, [x0, #0xd8]
// 0x1053058: bl #0xf7d92c
// 0x105305c: mov w8, #1
// 0x1053060: strb w8, [x21, #0x25d]
// 0x1053064: ldr x0, [x22]
// 0x1053068: ldr x21, [x19, #0x10]
// 0x105306c: ldr w8, [x0, #0xe0]
// 0x1053070: cbnz w8, #0x1053078
// 0x1053074: bl #0xf7da5c
// 0x1053078: mov x0, x21
// 0x105307c: mov x1, xzr
// 0x1053080: mov x2, xzr
// 0x1053084: bl #0x1b9568c
// 0x1053088: cbz x20, #0x1053498
// 0x105308c: mov w21, w0
// 0x1053090: ldr x0, [x20, #0x10]
// 0x1053094: mov x1, xzr
// 0x1053098: mov x2, xzr
// 0x105309c: bl #0x1b9568c
// 0x10530a0: and w8, w0, #1
// 0x10530a4: and w9, w21, #1
// 0x10530a8: cmp w9, w8
// 0x10530ac: b.eq #0x10530e8
// 0x10530b0: ldr x0, [x22]
// 0x10530b4: ldr x19, [x19, #0x10]
// 0x10530b8: ldr w8, [x0, #0xe0]
// 0x10530bc: cbnz w8, #0x10530c4
// 0x10530c0: bl #0xf7da5c
// 0x10530c4: mov x0, x19
// 0x10530c8: ldp x20, x19, [sp, #0x40]
// 0x10530cc: ldp x22, x21, [sp, #0x30]
// 0x10530d0: ldp x30, x23, [sp, #0x20]
// 0x10530d4: ldp d9, d8, [sp, #0x10]
// 0x10530d8: mov x1, xzr
// 0x10530dc: mov x2, xzr
// 0x10530e0: add sp, sp, #0x50
// 0x10530e4: b #0x1b94ac8
// 0x10530e8: adrp x21, #0x1fab000
// 0x10530ec: ldrb w8, [x21, #0x242]
// 0x10530f0: ldr s9, [x19, #0x18]
// 0x10530f4: cbnz w8, #0x105310c
// 0x10530f8: adrp x0, #0x1e8c000
// 0x10530fc: ldr x0, [x0, #0xa60]
// 0x1053100: bl #0xf7d92c
// 0x1053104: mov w8, #1
// 0x1053108: strb w8, [x21, #0x242]
// 0x105310c: adrp x22, #0x1e8c000
// 0x1053110: ldr x22, [x22, #0xa60]
// 0x1053114: ldr x0, [x22]
// 0x1053118: ldr w8, [x0, #0xe0]
// 0x105311c: cbnz w8, #0x1053124
// 0x1053120: bl #0xf7da5c
// 0x1053124: fcvt d8, s9
// 0x1053128: add x0, sp, #8
// 0x105312c: mov v0.16b, v8.16b
// 0x1053130: bl #0x1db0c60
// 0x1053134: fcmp s9, #0.0
// 0x1053138: b.ge #0x1053154
// 0x105313c: fmov d1, #-0.50000000
// 0x1053140: fcmp d0, d1
// 0x1053144: b.ne #0x105317c
// 0x1053148: ldr d0, [sp, #8]
// 0x105314c: fmov d1, #-1.00000000
// 0x1053150: b #0x1053168
// 0x1053154: fmov d1, #0.50000000
// 0x1053158: fcmp d0, d1
// 0x105315c: b.ne #0x1053188
// 0x1053160: ldr d0, [sp, #8]
// 0x1053164: fmov d1, #1.00000000
// 0x1053168: fcvtzs x8, d0
// 0x105316c: fadd d1, d0, d1
// 0x1053170: tst x8, #1
// 0x1053174: fcsel d0, d0, d1, eq
// 0x1053178: b #0x1053190
// 0x105317c: fadd d0, d8, d1
// 0x1053180: frintp d0, d0
// 0x1053184: b #0x1053190
// 0x1053188: fadd d0, d8, d1
// 0x105318c: frintm d0, d0
// 0x1053190: mov x9, #0x7ff0000000000000
// 0x1053194: ldrb w10, [x21, #0x242]
// 0x1053198: ldr s9, [x20, #0x18]
// 0x105319c: fmov d1, x9
// 0x10531a0: fcvtzs w8, d0
// 0x10531a4: fcmp d0, d1
// 0x10531a8: mov w9, #-0x80000000
// 0x10531ac: csel w23, w9, w8, eq
// 0x10531b0: cbnz w10, #0x10531c8
// 0x10531b4: adrp x0, #0x1e8c000
// 0x10531b8: ldr x0, [x0, #0xa60]
// 0x10531bc: bl #0xf7d92c
// 0x10531c0: mov w8, #1
// 0x10531c4: strb w8, [x21, #0x242]
// 0x10531c8: ldr x0, [x22]
// 0x10531cc: ldr w8, [x0, #0xe0]
// 0x10531d0: cbnz w8, #0x10531d8
// 0x10531d4: bl #0xf7da5c
// 0x10531d8: fcvt d8, s9
// 0x10531dc: add x0, sp, #8
// 0x10531e0: mov v0.16b, v8.16b
// 0x10531e4: bl #0x1db0c60
// 0x10531e8: fcmp s9, #0.0
// 0x10531ec: b.ge #0x1053208
// 0x10531f0: fmov d1, #-0.50000000
// 0x10531f4: fcmp d0, d1
// 0x10531f8: b.ne #0x1053230
// 0x10531fc: ldr d0, [sp, #8]
// 0x1053200: fmov d1, #-1.00000000
// 0x1053204: b #0x105321c
// 0x1053208: fmov d1, #0.50000000
// 0x105320c: fcmp d0, d1
// 0x1053210: b.ne #0x105323c
// 0x1053214: ldr d0, [sp, #8]
// 0x1053218: fmov d1, #1.00000000
// 0x105321c: fcvtzs x8, d0
// 0x1053220: fadd d1, d0, d1
// 0x1053224: tst x8, #1
// 0x1053228: fcsel d0, d0, d1, eq
// 0x105322c: b #0x1053244
// 0x1053230: fadd d0, d8, d1
// 0x1053234: frintp d0, d0
// 0x1053238: b #0x1053244
// 0x105323c: fadd d0, d8, d1
// 0x1053240: frintm d0, d0
// 0x1053244: mov x8, #0x7ff0000000000000
// 0x1053248: fmov d1, x8
// 0x105324c: fcvtzs w9, d0
// 0x1053250: fcmp d0, d1
// 0x1053254: mov w8, #-0x80000000
// 0x1053258: csel w8, w8, w9, eq
// 0x105325c: cmp w23, w8
// 0x1053260: b.gt #0x10532d0
// 0x1053264: adrp x8, #0x1e8c000
// 0x1053268: ldr x9, [x19, #0x10]
// 0x105326c: ldr x8, [x8, #0xd90]
// 0x1053270: ldr x8, [x8]
// 0x1053274: cbz x9, #0x10532a0
// 0x1053278: ldr x9, [x9]
// 0x105327c: ldrb w10, [x8, #0x130]
// 0x1053280: ldrb w11, [x9, #0x130]
// 0x1053284: cmp w11, w10
// 0x1053288: b.lo #0x10532a0
// 0x105328c: ldr x9, [x9, #0xc8]
// 0x1053290: add x9, x9, x10, lsl #3
// 0x1053294: ldur x9, [x9, #-8]
// 0x1053298: cmp x9, x8
// 0x105329c: b.eq #0x10532d0
// 0x10532a0: ldr x9, [x20, #0x10]
// 0x10532a4: cbz x9, #0x10532d0
// 0x10532a8: ldr x9, [x9]
// 0x10532ac: ldrb w10, [x8, #0x130]
// 0x10532b0: ldrb w11, [x9, #0x130]
// 0x10532b4: cmp w11, w10
// 0x10532b8: b.lo #0x10532d0
// 0x10532bc: ldr x9, [x9, #0xc8]
// 0x10532c0: add x9, x9, x10, lsl #3
// 0x10532c4: ldur x9, [x9, #-8]
// 0x10532c8: cmp x9, x8
// 0x10532cc: b.eq #0x1053490
// 0x10532d0: ldrb w8, [x19, #0x1c]
// 0x10532d4: ldrb w9, [x20, #0x1c]
// 0x10532d8: cmp w8, w9
// 0x10532dc: b.ne #0x1053340
// 0x10532e0: ldrb w8, [x21, #0x242]
// 0x10532e4: ldr s9, [x19, #0x18]
// 0x10532e8: cbnz w8, #0x1053300
// 0x10532ec: adrp x0, #0x1e8c000
// 0x10532f0: ldr x0, [x0, #0xa60]
// 0x10532f4: bl #0xf7d92c
// 0x10532f8: mov w8, #1
// 0x10532fc: strb w8, [x21, #0x242]
// 0x1053300: ldr x0, [x22]
// 0x1053304: ldr w8, [x0, #0xe0]
// 0x1053308: cbnz w8, #0x1053310
// 0x105330c: bl #0xf7da5c
// 0x1053310: fcvt d8, s9
// 0x1053314: add x0, sp, #8
// 0x1053318: mov v0.16b, v8.16b
// 0x105331c: bl #0x1db0c60
// 0x1053320: fcmp s9, #0.0
// 0x1053324: b.ge #0x105334c
// 0x1053328: fmov d1, #-0.50000000
// 0x105332c: fcmp d0, d1
// 0x1053330: b.ne #0x1053374
// 0x1053334: ldr d0, [sp, #8]
// 0x1053338: fmov d1, #-1.00000000
// 0x105333c: b #0x1053360
// 0x1053340: cmp w8, #0
// 0x1053344: cset w0, eq
// 0x1053348: b #0x1053478
// 0x105334c: fmov d1, #0.50000000
// 0x1053350: fcmp d0, d1
// 0x1053354: b.ne #0x1053380
// 0x1053358: ldr d0, [sp, #8]
// 0x105335c: fmov d1, #1.00000000
// 0x1053360: fcvtzs x8, d0
// 0x1053364: fadd d1, d0, d1
// 0x1053368: tst x8, #1
// 0x105336c: fcsel d0, d0, d1, eq
// 0x1053370: b #0x1053388
// 0x1053374: fadd d0, d8, d1
// 0x1053378: frintp d0, d0
// 0x105337c: b #0x1053388
// 0x1053380: fadd d0, d8, d1
// 0x1053384: frintm d0, d0
// 0x1053388: mov x9, #0x7ff0000000000000
// 0x105338c: ldrb w10, [x21, #0x242]
// 0x1053390: ldr s9, [x20, #0x18]
// 0x1053394: fmov d1, x9
// 0x1053398: fcvtzs w8, d0
// 0x105339c: fcmp d0, d1
// 0x10533a0: mov w9, #-0x80000000
// 0x10533a4: csel w23, w9, w8, eq
// 0x10533a8: cbnz w10, #0x10533c0
// 0x10533ac: adrp x0, #0x1e8c000
// 0x10533b0: ldr x0, [x0, #0xa60]
// 0x10533b4: bl #0xf7d92c
// 0x10533b8: mov w8, #1
// 0x10533bc: strb w8, [x21, #0x242]
// 0x10533c0: ldr x0, [x22]
// 0x10533c4: ldr w8, [x0, #0xe0]
// 0x10533c8: cbnz w8, #0x10533d0
// 0x10533cc: bl #0xf7da5c
// 0x10533d0: fcvt d8, s9
// 0x10533d4: add x0, sp, #8
// 0x10533d8: mov v0.16b, v8.16b
// 0x10533dc: bl #0x1db0c60
// 0x10533e0: fcmp s9, #0.0
// 0x10533e4: b.ge #0x1053400
// 0x10533e8: fmov d1, #-0.50000000
// 0x10533ec: fcmp d0, d1
// 0x10533f0: b.ne #0x1053428
// 0x10533f4: ldr d0, [sp, #8]
// 0x10533f8: fmov d1, #-1.00000000
// 0x10533fc: b #0x1053414
// 0x1053400: fmov d1, #0.50000000
// 0x1053404: fcmp d0, d1
// 0x1053408: b.ne #0x1053434
// 0x105340c: ldr d0, [sp, #8]
// 0x1053410: fmov d1, #1.00000000
// 0x1053414: fcvtzs x8, d0
// 0x1053418: fadd d1, d0, d1
// 0x105341c: tst x8, #1
// 0x1053420: fcsel d0, d0, d1, eq
// 0x1053424: b #0x105343c
// 0x1053428: fadd d0, d8, d1
// 0x105342c: frintp d0, d0
// 0x1053430: b #0x105343c
// 0x1053434: fadd d0, d8, d1
// 0x1053438: frintm d0, d0
// 0x105343c: mov x8, #0x7ff0000000000000
// 0x1053440: fmov d1, x8
// 0x1053444: fcvtzs w9, d0
// 0x1053448: fcmp d0, d1
// 0x105344c: mov w8, #-0x80000000
// 0x1053450: csel w8, w8, w9, eq
// 0x1053454: cmp w23, w8
// 0x1053458: b.ne #0x1053468
// 0x105345c: ldr s0, [x19, #0x40]
// 0x1053460: ldr s1, [x20, #0x40]
// 0x1053464: b #0x1053470
// 0x1053468: ldr s0, [x19, #0x18]
// 0x105346c: ldr s1, [x20, #0x18]
// 0x1053470: fcmp s0, s1
// 0x1053474: cset w0, mi
// 0x1053478: ldp x20, x19, [sp, #0x40]
// 0x105347c: ldp x22, x21, [sp, #0x30]
// 0x1053480: ldp x30, x23, [sp, #0x20]
// 0x1053484: ldp d9, d8, [sp, #0x10]
// 0x1053488: add sp, sp, #0x50
// 0x105348c: ret
// 0x1053490: mov w0, #1
// 0x1053494: b #0x1053478
// 0x1053498: bl #0xf7db74
```

## `TouchControl.Hit.ctor` — RVA `0xc5349c`

- Decompiled symbol: `TouchControl_Hit_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TouchControl_Hit_ctor(void)
{
    long long v0;  // x0

    v0 = Object__ctor();
    return Object__ctor();
}
```
