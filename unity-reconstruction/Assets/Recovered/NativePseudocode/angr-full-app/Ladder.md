# Native pseudocode: Ladder

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `Ladder.Start` — RVA `0xc9542c`

- Decompiled symbol: `Ladder_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `172` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

extern long long g_1efcf38;
extern long long g_1efec08;
extern char g_1fab476;

void Ladder_Start(long long *ptr, unsigned long a1)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_0 *p;  // x0
    long long v7;  // x1
    long long v8[7];  // x20
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab476 & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efec08);
        g_1fab476 = 1;
    }
    if (Camera__get_main(0) && Component__get_transform())
    {
        p = sub_1231bc8();
        if (p)
        {
            v7 = p->field_28;
            ptr[4] = v7;
            v8 = ptr + 4;
            sub_f7d8d0(v8, v7);
            if (v8[0])
            {
                ptr[6] = sub_1249224(v8[0], g_1efec08);
                sub_f7d8d0();
                return;
            }
        }
    }
    sub_f7db74();
}
```

## `Ladder.OnTriggerStay` — RVA `0xc954d8`

- Decompiled symbol: `Ladder_OnTriggerStay`
- Metadata signature: `private void OnTriggerStay(Collider other) { }`
- Native interval: `220` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10954d8: stp x30, x21, [sp, #-0x20]!
// 0x10954dc: stp x20, x19, [sp, #0x10]
// 0x10954e0: adrp x21, #0x1fab000
// 0x10954e4: ldrb w8, [x21, #0x477]
// 0x10954e8: mov x20, x1
// 0x10954ec: mov x19, x0
// 0x10954f0: tbnz w8, #0, #0x1095514
// 0x10954f4: adrp x0, #0x1e8d000
// 0x10954f8: ldr x0, [x0, #0xd10]
// 0x10954fc: bl #0xf7d92c
// 0x1095500: adrp x0, #0x1e8d000
// 0x1095504: ldr x0, [x0, #0xec0]
// 0x1095508: bl #0xf7d92c
// 0x109550c: mov w8, #1
// 0x1095510: strb w8, [x21, #0x477]
// 0x1095514: cbz x20, #0x10955b0
// 0x1095518: mov x0, x20
// 0x109551c: mov x1, xzr
// 0x1095520: bl #0x1b92190
// 0x1095524: cbz x0, #0x10955b0
// 0x1095528: adrp x20, #0x1e8d000
// 0x109552c: ldr x20, [x20, #0xec0]
// 0x1095530: mov x1, xzr
// 0x1095534: bl #0x1b92774
// 0x1095538: ldr x1, [x20]
// 0x109553c: mov x2, xzr
// 0x1095540: bl #0x17f610c
// 0x1095544: tbz w0, #0, #0x10955a4
// 0x1095548: ldr x0, [x19, #0x20]
// 0x109554c: cbz x0, #0x10955b0
// 0x1095550: adrp x8, #0x1e8d000
// 0x1095554: ldr x8, [x8, #0xd10]
// 0x1095558: ldr x1, [x8]
// 0x109555c: bl #0x1249224
// 0x1095560: cbz x0, #0x10955b0
// 0x1095564: mov w8, #1
// 0x1095568: strb w8, [x0, #0x295]
// 0x109556c: ldrb w9, [x19, #0x28]
// 0x1095570: cbnz w9, #0x1095578
// 0x1095574: strb w8, [x0, #0x296]
// 0x1095578: ldr s0, [x0, #0xc4]
// 0x109557c: adrp x8, #0x832000
// 0x1095580: ldr s1, [x8, #0x3b8]
// 0x1095584: fabs s0, s0
// 0x1095588: fcmp s0, s1
// 0x109558c: b.pl #0x10955a4
// 0x1095590: ldr x8, [x19, #0x30]
// 0x1095594: cbz x8, #0x10955b0
// 0x1095598: ldrb w8, [x8, #0x8f]
// 0x109559c: cbz w8, #0x10955a4
// 0x10955a0: strb wzr, [x0, #0x2d2]
// 0x10955a4: ldp x20, x19, [sp, #0x10]
// 0x10955a8: ldp x30, x21, [sp], #0x20
// 0x10955ac: ret
// 0x10955b0: bl #0xf7db74
```

## `Ladder.OnTriggerExit` — RVA `0xc955b4`

- Decompiled symbol: `Ladder_OnTriggerExit`
- Metadata signature: `private void OnTriggerExit(Collider other2) { }`
- Native interval: `192` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

typedef struct struct_1 {
    char padding_0[661];
    char field_295;
    char field_296;
    char padding_297[18];
    char field_2a9;
    char padding_2aa[2];
    unsigned int field_2ac;
} struct_1;

extern long long g_1efebc0;
extern long long g_1f0cf98;
extern char g_1fab478;

int Ladder_OnTriggerExit(struct_0 *a0, long long a1)
{
    long long v0;  // x0
    unsigned long long v1;  // x0
    struct_1 *p;  // x0
    struct_1 *ptr;  // x19
    unsigned int v4;  // s0

    if (!(g_1fab478 & 1))
    {
        sub_f7d92c(&g_1efebc0);
        sub_f7d92c(&g_1f0cf98);
        g_1fab478 = 1;
    }
    if (!a1)
        sub_f7db74();
    if (Component__get_gameObject(a1, 0))
    {
        v0 = GameObject__get_tag();
        v1 = String__op_Equality(v0, g_1f0cf98, 0);
        if (((char)v1 & 1))
        {
            if (a0->field_20)
            {
                p = sub_1249224(a0->field_20, g_1efebc0);
                if (!p)
                    sub_f7db74();
                ptr = p;
                p->field_295 = 0;
                v1 = Time__get_time(0);
                ptr->field_2a9 = 0;
                ptr->field_2ac = v4 + 0x3e800000;
                ptr->field_296 = 0;
            }
            else
            {
                sub_f7db74();
            }
        }
        return v1;
    }
    sub_f7db74();
}
```

## `Ladder.ctor` — RVA `0xc95674`

- Decompiled symbol: `Ladder_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    char field_28;
} struct_0;

long long Ladder_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_28 = 1;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
