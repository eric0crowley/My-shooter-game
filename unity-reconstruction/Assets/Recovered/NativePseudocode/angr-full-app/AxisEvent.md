# Native pseudocode: AxisEvent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AxisEvent.ctor` — RVA `0xc681f0`

- Decompiled symbol: `AxisEvent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `196` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AxisEvent_Recovered` matched 4 offsets against `AxisEvent` metadata (confidence 1.00).

```c
typedef struct AxisEvent_Recovered {
    char padding_0[32];
    long long axisName;
    unsigned int axisDeadzone;
    char padding_2c[12];
    long long positiveEvent;
    long long negativeEvent;
} AxisEvent_Recovered;

extern long long g_1f0ab18;
extern char g_1fab316;

void AxisEvent_ctor(struct_0 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    struct_0 *p;  // x0
    long long v11;  // x20
    struct_0 *addr;  // x0
    long long v13;  // x0
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
    if (!(g_1fab316 & 1))
    {
        sub_f7d92c("c[");
        sub_f7d92c(&g_1f0ab18);
        g_1fab316 = 1;
    }
    p = ptr;
    p->field_20 = g_1f0ab18;
    sub_f7d8d0((struct AxisEvent_Recovered *)&p->field_20, g_1f0ab18);
    ptr->field_28 = 0x3f000000;
    MonoBehaviour__ctor(ptr, 0);
    v11 = sub_f7db70(g_1ef2110);
    UnityEvent__ctor(v11, 0);
    addr = ptr;
    addr->field_38 = v11;
    sub_f7d8d0((struct AxisEvent_Recovered *)&addr->field_38, v11);
    v13 = sub_f7db70(g_1ef2110);
    UnityEvent__ctor(v13, 0);
    ptr->field_40 = v13;
    sub_f7d8d0();
    return;
}
```

## `AxisEvent.OnEnable` — RVA `0xc682b4`

- Decompiled symbol: `AxisEvent_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    unsigned int field_30;
} struct_0;

struct_0 * AxisEvent_OnEnable(struct_0 *ptr)
{
    ptr->field_30 = 0;
    return ptr;
}
```

## `AxisEvent.Update` — RVA `0xc682bc`

- Decompiled symbol: `AxisEvent_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `292` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10682bc: stp x30, x21, [sp, #-0x20]!
// 0x10682c0: stp x20, x19, [sp, #0x10]
// 0x10682c4: adrp x21, #0x1fab000
// 0x10682c8: adrp x20, #0x1e8c000
// 0x10682cc: ldrb w8, [x21, #0x317]
// 0x10682d0: ldr x20, [x20, #0xe0]
// 0x10682d4: mov x19, x0
// 0x10682d8: tbnz w8, #0, #0x10682f0
// 0x10682dc: adrp x0, #0x1e8c000
// 0x10682e0: ldr x0, [x0, #0xe0]
// 0x10682e4: bl #0xf7d92c
// 0x10682e8: mov w8, #1
// 0x10682ec: strb w8, [x21, #0x317]
// 0x10682f0: ldr x0, [x20]
// 0x10682f4: ldr x21, [x19, #0x20]
// 0x10682f8: add x20, x19, #0x2c
// 0x10682fc: ldr w8, [x0, #0xe0]
// 0x1068300: cbnz w8, #0x1068308
// 0x1068304: bl #0xf7da5c
// 0x1068308: mov x0, x21
// 0x106830c: mov x1, x20
// 0x1068310: mov x2, xzr
// 0x1068314: bl #0x1036220
// 0x1068318: ldr s1, [x19, #0x28]
// 0x106831c: fabs s2, s0
// 0x1068320: fcmp s2, s1
// 0x1068324: b.le #0x1068340
// 0x1068328: mov w9, wzr
// 0x106832c: fcmp s0, #0.0
// 0x1068330: b.le #0x1068350
// 0x1068334: mov w8, #1
// 0x1068338: mov w20, #1
// 0x106833c: b #0x1068358
// 0x1068340: mov w8, wzr
// 0x1068344: mov w20, wzr
// 0x1068348: mov w9, #1
// 0x106834c: b #0x1068358
// 0x1068350: mov w8, wzr
// 0x1068354: mov w20, #-1
// 0x1068358: ldr w10, [x19, #0x34]
// 0x106835c: cmp w10, #2
// 0x1068360: b.eq #0x1068384
// 0x1068364: cmp w10, #1
// 0x1068368: b.eq #0x106839c
// 0x106836c: cbnz w10, #0x10683cc
// 0x1068370: tbnz w9, #0, #0x10683cc
// 0x1068374: ldr w9, [x19, #0x30]
// 0x1068378: cmp w9, w20
// 0x106837c: b.ne #0x1068388
// 0x1068380: b #0x10683cc
// 0x1068384: tbnz w9, #0, #0x10683cc
// 0x1068388: cmp w8, #0
// 0x106838c: mov w8, #0x40
// 0x1068390: mov w9, #0x38
// 0x1068394: csel x8, x9, x8, ne
// 0x1068398: b #0x10683bc
// 0x106839c: ldr w8, [x19, #0x30]
// 0x10683a0: cbz w8, #0x10683cc
// 0x10683a4: cmp w20, w8
// 0x10683a8: b.eq #0x10683cc
// 0x10683ac: cmp w8, #0
// 0x10683b0: mov w8, #0x40
// 0x10683b4: mov w9, #0x38
// 0x10683b8: csel x8, x9, x8, gt
// 0x10683bc: ldr x0, [x19, x8]
// 0x10683c0: cbz x0, #0x10683dc
// 0x10683c4: mov x1, xzr
// 0x10683c8: bl #0x1ba29c8
// 0x10683cc: str w20, [x19, #0x30]
// 0x10683d0: ldp x20, x19, [sp, #0x10]
// 0x10683d4: ldp x30, x21, [sp], #0x20
// 0x10683d8: ret
// 0x10683dc: bl #0xf7db74
```
