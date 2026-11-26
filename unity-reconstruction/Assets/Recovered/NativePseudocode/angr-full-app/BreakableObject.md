# Native pseudocode: BreakableObject

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BreakableObject.Start` — RVA `0xc95684`

- Decompiled symbol: `BreakableObject_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `128` bytes
- Result: `pseudocode`

```c
extern long long g_1efd040;
extern char g_1fab479;

void BreakableObject_Start(long long *ptr)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    long long v6;  // x0
    long long v7[8];  // x20
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab479 & 1))
    {
        sub_f7d92c(&g_1efd040);
        g_1fab479 = 1;
    }
    v6 = Component__get_transform(ptr, 0);
    ptr[7] = v6;
    v7 = ptr + 7;
    sub_f7d8d0(v7, v6);
    if (v7[0])
    {
        ptr[5] = sub_1231bc8(v7[0], g_1efd040);
        sub_f7d8d0();
        return;
    }
    sub_f7db74(0);
}
```

## `BreakableObject.DetectBroken` — RVA `0xc95704`

- Decompiled symbol: `BreakableObject_DetectBroken`
- Metadata signature: `private IEnumerator DetectBroken() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern char g_1fab47a;

struct_0 * BreakableObject_DetectBroken(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab47a & 1))
    {
        sub_f7d92c("-f");
        g_1fab47a = 1;
    }
    v0 = sub_f7db70(g_1ef2d18);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `BreakableObject.<DetectBroken>d__5.ctor` — RVA `0xc95770`

- Decompiled symbol: `BreakableObject_DetectBroken_d__5_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void BreakableObject_DetectBroken_d__5_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `BreakableObject.ApplyDamage` — RVA `0xc95798`

- Decompiled symbol: `BreakableObject_ApplyDamage`
- Metadata signature: `public void ApplyDamage(float damage) { }`
- Native interval: `744` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1095798: sub sp, sp, #0x80
// 0x109579c: stp d9, d8, [sp, #0x40]
// 0x10957a0: str x30, [sp, #0x50]
// 0x10957a4: stp x22, x21, [sp, #0x60]
// 0x10957a8: stp x20, x19, [sp, #0x70]
// 0x10957ac: adrp x20, #0x1fab000
// 0x10957b0: ldrb w8, [x20, #0x47b]
// 0x10957b4: mov v8.16b, v0.16b
// 0x10957b8: mov x19, x0
// 0x10957bc: tbnz w8, #0, #0x10957f8
// 0x10957c0: adrp x0, #0x1e8d000
// 0x10957c4: ldr x0, [x0, #0x248]
// 0x10957c8: bl #0xf7d92c
// 0x10957cc: adrp x0, #0x1e8e000
// 0x10957d0: ldr x0, [x0, #0x190]
// 0x10957d4: bl #0xf7d92c
// 0x10957d8: adrp x0, #0x1e8e000
// 0x10957dc: ldr x0, [x0, #0x198]
// 0x10957e0: bl #0xf7d92c
// 0x10957e4: adrp x0, #0x1e8c000
// 0x10957e8: ldr x0, [x0, #0xd8]
// 0x10957ec: bl #0xf7d92c
// 0x10957f0: mov w8, #1
// 0x10957f4: strb w8, [x20, #0x47b]
// 0x10957f8: movi v0.2d, #0000000000000000
// 0x10957fc: str xzr, [sp, #0x58]
// 0x1095800: stp q0, q0, [sp, #0x20]
// 0x1095804: ldr s0, [x19, #0x20]
// 0x1095808: fsub s0, s0, s8
// 0x109580c: fcmp s0, #0.0
// 0x1095810: str s0, [x19, #0x20]
// 0x1095814: b.hi #0x1095a64
// 0x1095818: ldrb w8, [x19, #0x30]
// 0x109581c: cbnz w8, #0x1095a64
// 0x1095820: adrp x21, #0x1e8c000
// 0x1095824: ldr x21, [x21, #0xd8]
// 0x1095828: ldr x20, [x19, #0x28]
// 0x109582c: ldr x0, [x21]
// 0x1095830: ldr w8, [x0, #0xe0]
// 0x1095834: cbnz w8, #0x109583c
// 0x1095838: bl #0xf7da5c
// 0x109583c: mov x0, x20
// 0x1095840: mov x1, xzr
// 0x1095844: bl #0x1b98274
// 0x1095848: tbz w0, #0, #0x1095954
// 0x109584c: ldr x20, [x19, #0x28]
// 0x1095850: cbz x20, #0x1095a7c
// 0x1095854: mov x0, x20
// 0x1095858: mov x1, xzr
// 0x109585c: bl #0x1bc9cb4
// 0x1095860: str x0, [sp, #0x58]
// 0x1095864: mov x8, sp
// 0x1095868: add x0, sp, #0x58
// 0x109586c: mov x1, xzr
// 0x1095870: bl #0x1bc9f50
// 0x1095874: ldp q0, q1, [sp]
// 0x1095878: add x0, sp, #0x20
// 0x109587c: mov x1, xzr
// 0x1095880: stp q0, q1, [sp, #0x20]
// 0x1095884: bl #0x1bca508
// 0x1095888: adrp x22, #0x1fab000
// 0x109588c: ldrb w8, [x22, #0x242]
// 0x1095890: mov v8.16b, v0.16b
// 0x1095894: cbnz w8, #0x10958ac
// 0x1095898: adrp x0, #0x1e8c000
// 0x109589c: ldr x0, [x0, #0xa60]
// 0x10958a0: bl #0xf7d92c
// 0x10958a4: mov w8, #1
// 0x10958a8: strb w8, [x22, #0x242]
// 0x10958ac: adrp x8, #0x1e8c000
// 0x10958b0: ldr x8, [x8, #0xa60]
// 0x10958b4: ldr x0, [x8]
// 0x10958b8: ldr w8, [x0, #0xe0]
// 0x10958bc: cbnz w8, #0x10958c4
// 0x10958c0: bl #0xf7da5c
// 0x10958c4: fcvt d9, s8
// 0x10958c8: mov x0, sp
// 0x10958cc: mov v0.16b, v9.16b
// 0x10958d0: bl #0x1db0c60
// 0x10958d4: fcmp s8, #0.0
// 0x10958d8: b.ge #0x10958f4
// 0x10958dc: fmov d1, #-0.50000000
// 0x10958e0: fcmp d0, d1
// 0x10958e4: b.ne #0x109591c
// 0x10958e8: ldr d0, [sp]
// 0x10958ec: fmov d1, #-1.00000000
// 0x10958f0: b #0x1095908
// 0x10958f4: fmov d1, #0.50000000
// 0x10958f8: fcmp d0, d1
// 0x10958fc: b.ne #0x1095928
// 0x1095900: ldr d0, [sp]
// 0x1095904: fmov d1, #1.00000000
// 0x1095908: fcvtzs x8, d0
// 0x109590c: fadd d1, d0, d1
// 0x1095910: tst x8, #1
// 0x1095914: fcsel d0, d0, d1, eq
// 0x1095918: b #0x1095930
// 0x109591c: fadd d0, d9, d1
// 0x1095920: frintp d0, d0
// 0x1095924: b #0x1095930
// 0x1095928: fadd d0, d9, d1
// 0x109592c: frintm d0, d0
// 0x1095930: mov x8, #0x7ff0000000000000
// 0x1095934: fmov d1, x8
// 0x1095938: fcvtzs w9, d0
// 0x109593c: fcmp d0, d1
// 0x1095940: mov w8, #-0x80000000
// 0x1095944: csel w1, w8, w9, eq
// 0x1095948: mov x0, x20
// 0x109594c: mov x2, xzr
// 0x1095950: bl #0x1bc9b7c
// 0x1095954: adrp x22, #0x1e8d000
// 0x1095958: ldr x22, [x22, #0x248]
// 0x109595c: mov x0, x19
// 0x1095960: ldr x1, [x22]
// 0x1095964: bl #0x1231bc8
// 0x1095968: ldr x8, [x21]
// 0x109596c: mov x20, x0
// 0x1095970: ldr w9, [x8, #0xe0]
// 0x1095974: cbnz w9, #0x1095980
// 0x1095978: mov x0, x8
// 0x109597c: bl #0xf7da5c
// 0x1095980: mov x0, x20
// 0x1095984: mov x1, xzr
// 0x1095988: bl #0x1b98274
// 0x109598c: tbz w0, #0, #0x10959f4
// 0x1095990: ldr x1, [x22]
// 0x1095994: mov x0, x19
// 0x1095998: bl #0x1231bc8
// 0x109599c: mov x20, x0
// 0x10959a0: mov x0, xzr
// 0x10959a4: bl #0x1b9ae58
// 0x10959a8: mov x0, xzr
// 0x10959ac: mov v8.16b, v0.16b
// 0x10959b0: bl #0x1b9ae58
// 0x10959b4: adrp x8, #0x832000
// 0x10959b8: mov v1.16b, v0.16b
// 0x10959bc: ldr s0, [x8, #0x400]
// 0x10959c0: mov x0, xzr
// 0x10959c4: fmul s0, s8, s0
// 0x10959c8: bl #0x1b9012c
// 0x10959cc: cbz x20, #0x1095a7c
// 0x10959d0: mov x0, x20
// 0x10959d4: mov x1, xzr
// 0x10959d8: bl #0x1b6a500
// 0x10959dc: ldr x1, [x22]
// 0x10959e0: mov x0, x19
// 0x10959e4: bl #0x1231bc8
// 0x10959e8: cbz x0, #0x1095a7c
// 0x10959ec: mov x1, xzr
// 0x10959f0: bl #0x1b6a5cc
// 0x10959f4: ldr x0, [x19, #0x38]
// 0x10959f8: cbz x0, #0x1095a7c
// 0x10959fc: adrp x8, #0x1e8e000
// 0x1095a00: ldr x8, [x8, #0x198]
// 0x1095a04: ldr x1, [x8]
// 0x1095a08: bl #0x1231bc8
// 0x1095a0c: cbz x0, #0x1095a7c
// 0x1095a10: mov w1, wzr
// 0x1095a14: mov x2, xzr
// 0x1095a18: bl #0x1b799d0
// 0x1095a1c: ldr x0, [x19, #0x38]
// 0x1095a20: cbz x0, #0x1095a7c
// 0x1095a24: adrp x8, #0x1e8e000
// 0x1095a28: ldr x8, [x8, #0x190]
// 0x1095a2c: ldr x1, [x8]
// 0x1095a30: bl #0x1231bc8
// 0x1095a34: cbz x0, #0x1095a7c
// 0x1095a38: mov w1, wzr
// 0x1095a3c: mov x2, xzr
// 0x1095a40: bl #0x1bcf938
// 0x1095a44: mov w8, #1
// 0x1095a48: mov x0, x19
// 0x1095a4c: strb w8, [x19, #0x30]
// 0x1095a50: bl #0x1095704
// 0x1095a54: mov x1, x0
// 0x1095a58: mov x0, x19
// 0x1095a5c: mov x2, xzr
// 0x1095a60: bl #0x1b95d40
// 0x1095a64: ldp x20, x19, [sp, #0x70]
// 0x1095a68: ldp x22, x21, [sp, #0x60]
// 0x1095a6c: ldr x30, [sp, #0x50]
// 0x1095a70: ldp d9, d8, [sp, #0x40]
// 0x1095a74: add sp, sp, #0x80
// 0x1095a78: ret
// 0x1095a7c: bl #0xf7db74
```

## `BreakableObject.ctor` — RVA `0xc95a80`

- Decompiled symbol: `BreakableObject_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned int field_20;
} struct_0;

long long BreakableObject_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_20 = 0x43160000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```

## `BreakableObject.<DetectBroken>d__5.Dispose` — RVA `0xc95a90`

- Decompiled symbol: `BreakableObject_DetectBroken_d__5_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long BreakableObject_DetectBroken_d__5_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `BreakableObject.<DetectBroken>d__5.MoveNext` — RVA `0xc95a94`

- Decompiled symbol: `BreakableObject_DetectBroken_d__5_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `768` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_3 *field_20;
} struct_4;

typedef struct struct_3 {
    char padding_0[40];
    long long field_28;
    char field_30;
    char padding_31[7];
    long long field_38;
} struct_3;

typedef struct struct_5 {
    char padding_0[24];
    int field_18;
} struct_5;

typedef struct struct_6 {
    char padding_0[32];
    unsigned long long field_20;
    char padding_28[9];
    char field_31;
    char padding_32[70];
    unsigned long long field_78;
} struct_6;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

extern struct_2 *g_1ef0c58;
extern long long g_1ef2440;
extern long long g_1efedb0;
extern long long g_1efedb8;
extern char g_1fab47c;

unsigned int BreakableObject_DetectBroken_d__5_MoveNext(struct_4 *ptr)
{
    struct_3 *v0;  // x20
    struct_5 *p;  // x0
    struct_6 *ptr4;  // x22
    long long v11;  // x0
    long long v12;  // x20
    struct_4 *ptr5;  // x19
    unsigned int v2;  // w8
    struct_5 *addr;  // x21
    unsigned int v4;  // w24
    unsigned long long v5[10];  // x22
    unsigned long v6;  // x0
    unsigned int v7;  // w8
    struct_5 *ptr3;  // x21
    unsigned int v9;  // w23

    if (!(g_1fab47c & 1))
    {
        sub_f7d92c("s.");
        sub_f7d92c(&g_1efedb0);
        sub_f7d92c(&g_1efedb8);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c("s%");
        g_1fab47c = 1;
    }
    if (1 < ptr->field_10)
    {
LABEL_1095d74:
        return 0;
    }
    v0 = ptr->field_20;
    ptr->field_10 = 4294967295;
    if (v0)
    {
        if (!v0->field_30)
        {
LABEL_1095d00:
            v12 = sub_f7db70(g_1ef2440);
            WaitForSeconds__ctor(v12, 0);
            ptr->field_18 = v12;
            ptr5 = &ptr->field_18;
            sub_f7d8d0(ptr5, v12);
            *((unsigned int *)&ptr5->padding_0[8]) = 1;
            return 1;
        }
        else if (Component__get_gameObject(v0, 0) && (p = (struct_5 *)(unsigned long long)sub_1249ec4(), p))
        {
            v2 = p->field_18;
            addr = p;
            if (p->field_18 >= 1)
            {
                v4 = 0;
                do
                {
                    if (v2 <= v4)
                        sub_f7db7c(p);
                    v5 = *((long long *)&addr[1].padding_0[4 + 8 * v4]);
                    if (!v5)
                        sub_f7db7c(sub_f7db74());
                    if (!g_1eeea08->field_b8->field_0)
                        sub_f7db7c(sub_f7db74());
                    v6 = Component__get_transform(g_1eeea08->field_b8->field_0, 0);
                    if (!v5[9])
                        sub_f7db7c(sub_f7db74());
                    Transform__set_parent(v5[9], v6, 0);
                    if (!v5[8] || !((GameObject__SetActive(v5[8], 0, 0), Component__get_gameObject(v5, 0))))
                        goto LABEL_1095d8c;
                } while ((p = (struct_5 *)GameObject__SetActive(), v2 = (unsigned int)addr->field_18, v4 += 1, v4 < v2));
            }
            else if (Component__get_gameObject(v0, 0) && (p = (struct_5 *)(unsigned long long)sub_1249ec4(), p))
            {
                v7 = p->field_18;
                ptr3 = p;
                if (v7 >= 1)
                {
                    v9 = 0;
                    do
                    {
                        if (v7 <= v9)
                            sub_f7db7c(p);
                        ptr4 = *((long long *)&ptr3[1].padding_0[4 + 8 * v9]);
                        if (!ptr4)
                            sub_f7db7c(sub_f7db74());
                        if (!Component__get_transform(ptr4, 0))
                            sub_f7db7c(sub_f7db74());
                        Transform__set_parent();
                        if (!ptr4->field_20)
                            sub_f7db7c(sub_f7db74());
                        Rigidbody__set_isKinematic(ptr4->field_20, 0, 0);
                        if (!ptr4->field_78 || !((Collider__set_isTrigger(ptr4->field_78, 0, 0), Component__get_gameObject(ptr4, 0))))
                            goto LABEL_1095d8c;
                    } while ((p = (struct_5 *)(unsigned long long)GameObject__set_tag(), ptr4->field_31 = 1, v7 = (unsigned int)ptr3->field_18, v9 += 1, v9 < v7));
                }
                else
                {
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (!(Object__op_Implicit(v0->field_28, 0) & 1))
                        goto LABEL_1095d00;
                    if (v0->field_28)
                    {
                        if (ParticleSystem__get_particleCount(v0->field_28, 0))
                            goto LABEL_1095d00;
                        if (v0->field_38)
                        {
                            v11 = Component__get_gameObject(v0->field_38, 0);
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            Object__Destroy(v11, 0);
                            goto LABEL_1095d74;
                        }
                    }
                }
            }
        }
    }
LABEL_1095d8c:
    sub_f7db7c(sub_f7db74());
}
```

## `BreakableObject.<DetectBroken>d__5.get_Current` — RVA `0xc95d94`

- Decompiled symbol: `BreakableObject_DetectBroken_d__5_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long BreakableObject_DetectBroken_d__5_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `BreakableObject.<DetectBroken>d__5.Reset` — RVA `0xc95d9c`

- Decompiled symbol: `BreakableObject_DetectBroken_d__5_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04228;

void BreakableObject_DetectBroken_d__5_Reset(void)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = sub_f7db70(sub_f7d940(&g_1ef0bd8));
    NotSupportedException__ctor(v4, 0);
    sub_f7da4c(v4, sub_f7d940(&g_1f04228));
}
```

## `BreakableObject.<DetectBroken>d__5.get_Current` — RVA `0xc95dd4`

- Decompiled symbol: `BreakableObject_DetectBroken_d__5_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long BreakableObject_DetectBroken_d__5_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
