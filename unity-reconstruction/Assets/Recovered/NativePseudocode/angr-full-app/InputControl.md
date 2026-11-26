# Native pseudocode: InputControl

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InputControl.Start` — RVA `0xca6368`

- Decompiled symbol: `InputControl_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1efcf98;
extern char g_1fab4bd;

void InputControl_Start(struct_0 *ptr)
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
    if (!(g_1fab4bd & 1))
    {
        sub_f7d92c(&g_1efcf98);
        g_1fab4bd = 1;
    }
    ptr->field_20 = sub_1231bc8(ptr, g_1efcf98);
    sub_f7d8d0();
    return;
}
```

## `InputControl.Update` — RVA `0xca63c0`

- Decompiled symbol: `InputControl_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `4664` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10a63c0: sub sp, sp, #0xe0
// 0x10a63c4: str d14, [sp, #0x50]
// 0x10a63c8: stp d13, d12, [sp, #0x58]
// 0x10a63cc: stp d11, d10, [sp, #0x68]
// 0x10a63d0: stp d9, d8, [sp, #0x78]
// 0x10a63d4: str x30, [sp, #0x88]
// 0x10a63d8: stp x28, x27, [sp, #0x90]
// 0x10a63dc: stp x26, x25, [sp, #0xa0]
// 0x10a63e0: stp x24, x23, [sp, #0xb0]
// 0x10a63e4: stp x22, x21, [sp, #0xc0]
// 0x10a63e8: stp x20, x19, [sp, #0xd0]
// 0x10a63ec: adrp x20, #0x1fab000
// 0x10a63f0: ldrb w8, [x20, #0x4be]
// 0x10a63f4: mov x19, x0
// 0x10a63f8: tbnz w8, #0, #0x10a6698
// 0x10a63fc: adrp x0, #0x1e8c000
// 0x10a6400: ldr x0, [x0, #0xe0]
// 0x10a6404: bl #0xf7d92c
// 0x10a6408: adrp x0, #0x1e8c000
// 0x10a640c: ldr x0, [x0, #0xd8]
// 0x10a6410: bl #0xf7d92c
// 0x10a6414: adrp x0, #0x1e8d000
// 0x10a6418: ldr x0, [x0, #0x4a8]
// 0x10a641c: bl #0xf7d92c
// 0x10a6420: adrp x0, #0x1e8e000
// 0x10a6424: ldr x0, [x0, #0x3a0]
// 0x10a6428: bl #0xf7d92c
// 0x10a642c: adrp x0, #0x1e8e000
// 0x10a6430: ldr x0, [x0, #0x3a8]
// 0x10a6434: bl #0xf7d92c
// 0x10a6438: adrp x0, #0x1e8c000
// 0x10a643c: ldr x0, [x0, #0xfd0]
// 0x10a6440: bl #0xf7d92c
// 0x10a6444: adrp x0, #0x1e8c000
// 0x10a6448: ldr x0, [x0, #0x530]
// 0x10a644c: bl #0xf7d92c
// 0x10a6450: adrp x0, #0x1e8e000
// 0x10a6454: ldr x0, [x0, #0x3b0]
// 0x10a6458: bl #0xf7d92c
// 0x10a645c: adrp x0, #0x1e8e000
// 0x10a6460: ldr x0, [x0, #0x3b8]
// 0x10a6464: bl #0xf7d92c
// 0x10a6468: adrp x0, #0x1e8e000
// 0x10a646c: ldr x0, [x0, #0x3c0]
// 0x10a6470: bl #0xf7d92c
// 0x10a6474: adrp x0, #0x1e8d000
// 0x10a6478: ldr x0, [x0, #0x620]
// 0x10a647c: bl #0xf7d92c
// 0x10a6480: adrp x0, #0x1e8e000
// 0x10a6484: ldr x0, [x0, #0x3c8]
// 0x10a6488: bl #0xf7d92c
// 0x10a648c: adrp x0, #0x1e8e000
// 0x10a6490: ldr x0, [x0, #0x3d0]
// 0x10a6494: bl #0xf7d92c
// 0x10a6498: adrp x0, #0x1e8e000
// 0x10a649c: ldr x0, [x0, #0x3d8]
// 0x10a64a0: bl #0xf7d92c
// 0x10a64a4: adrp x0, #0x1e8e000
// 0x10a64a8: ldr x0, [x0, #0x3e0]
// 0x10a64ac: bl #0xf7d92c
// 0x10a64b0: adrp x0, #0x1e8e000
// 0x10a64b4: ldr x0, [x0, #0x3e8]
// 0x10a64b8: bl #0xf7d92c
// 0x10a64bc: adrp x0, #0x1e8e000
// 0x10a64c0: ldr x0, [x0, #0x3f0]
// 0x10a64c4: bl #0xf7d92c
// 0x10a64c8: adrp x0, #0x1e8e000
// 0x10a64cc: ldr x0, [x0, #0x3f8]
// 0x10a64d0: bl #0xf7d92c
// 0x10a64d4: adrp x0, #0x1e8e000
// 0x10a64d8: ldr x0, [x0, #0x400]
// 0x10a64dc: bl #0xf7d92c
// 0x10a64e0: adrp x0, #0x1e8e000
// 0x10a64e4: ldr x0, [x0, #0x408]
// 0x10a64e8: bl #0xf7d92c
// 0x10a64ec: adrp x0, #0x1e8e000
// 0x10a64f0: ldr x0, [x0, #0xb8]
// 0x10a64f4: bl #0xf7d92c
// 0x10a64f8: adrp x0, #0x1e8e000
// 0x10a64fc: ldr x0, [x0, #0x410]
// 0x10a6500: bl #0xf7d92c
// 0x10a6504: adrp x0, #0x1e8c000
// 0x10a6508: ldr x0, [x0, #0x540]
// 0x10a650c: bl #0xf7d92c
// 0x10a6510: adrp x0, #0x1e8e000
// 0x10a6514: ldr x0, [x0, #0x418]
// 0x10a6518: bl #0xf7d92c
// 0x10a651c: adrp x0, #0x1e8e000
// 0x10a6520: ldr x0, [x0, #0x420]
// 0x10a6524: bl #0xf7d92c
// 0x10a6528: adrp x0, #0x1e8e000
// 0x10a652c: ldr x0, [x0, #0x428]
// 0x10a6530: bl #0xf7d92c
// 0x10a6534: adrp x0, #0x1e8e000
// 0x10a6538: ldr x0, [x0, #0x430]
// 0x10a653c: bl #0xf7d92c
// 0x10a6540: adrp x0, #0x1e8e000
// 0x10a6544: ldr x0, [x0, #0x438]
// 0x10a6548: bl #0xf7d92c
// 0x10a654c: adrp x0, #0x1e8e000
// 0x10a6550: ldr x0, [x0, #0x440]
// 0x10a6554: bl #0xf7d92c
// 0x10a6558: adrp x0, #0x1e8c000
// 0x10a655c: ldr x0, [x0, #0x550]
// 0x10a6560: bl #0xf7d92c
// 0x10a6564: adrp x0, #0x1e8e000
// 0x10a6568: ldr x0, [x0, #0x448]
// 0x10a656c: bl #0xf7d92c
// 0x10a6570: adrp x0, #0x1e8e000
// 0x10a6574: ldr x0, [x0, #0x450]
// 0x10a6578: bl #0xf7d92c
// 0x10a657c: adrp x0, #0x1e8e000
// 0x10a6580: ldr x0, [x0, #0x458]
// 0x10a6584: bl #0xf7d92c
// 0x10a6588: adrp x0, #0x1e8e000
// 0x10a658c: ldr x0, [x0, #0x460]
// 0x10a6590: bl #0xf7d92c
// 0x10a6594: adrp x0, #0x1e8e000
// 0x10a6598: ldr x0, [x0, #0x468]
// 0x10a659c: bl #0xf7d92c
// 0x10a65a0: adrp x0, #0x1e8e000
// 0x10a65a4: ldr x0, [x0, #0x470]
// 0x10a65a8: bl #0xf7d92c
// 0x10a65ac: adrp x0, #0x1e8e000
// 0x10a65b0: ldr x0, [x0, #0x478]
// 0x10a65b4: bl #0xf7d92c
// 0x10a65b8: adrp x0, #0x1e8e000
// 0x10a65bc: ldr x0, [x0, #0x480]
// 0x10a65c0: bl #0xf7d92c
// 0x10a65c4: adrp x0, #0x1e8d000
// 0x10a65c8: ldr x0, [x0, #8]
// 0x10a65cc: bl #0xf7d92c
// 0x10a65d0: adrp x0, #0x1e8e000
// 0x10a65d4: ldr x0, [x0, #0x488]
// 0x10a65d8: bl #0xf7d92c
// 0x10a65dc: adrp x0, #0x1e8e000
// 0x10a65e0: ldr x0, [x0, #0x490]
// 0x10a65e4: bl #0xf7d92c
// 0x10a65e8: adrp x0, #0x1e8e000
// 0x10a65ec: ldr x0, [x0, #0x498]
// 0x10a65f0: bl #0xf7d92c
// 0x10a65f4: adrp x0, #0x1e8e000
// 0x10a65f8: ldr x0, [x0, #0x4a0]
// 0x10a65fc: bl #0xf7d92c
// 0x10a6600: adrp x0, #0x1e8e000
// 0x10a6604: ldr x0, [x0, #0x4a8]
// 0x10a6608: bl #0xf7d92c
// 0x10a660c: adrp x0, #0x1e8e000
// 0x10a6610: ldr x0, [x0, #0x4b0]
// 0x10a6614: bl #0xf7d92c
// 0x10a6618: adrp x0, #0x1e8d000
// 0x10a661c: ldr x0, [x0, #0xfd0]
// 0x10a6620: bl #0xf7d92c
// 0x10a6624: adrp x0, #0x1e8e000
// 0x10a6628: ldr x0, [x0, #0x4b8]
// 0x10a662c: bl #0xf7d92c
// 0x10a6630: adrp x0, #0x1e8e000
// 0x10a6634: ldr x0, [x0, #0x4c0]
// 0x10a6638: bl #0xf7d92c
// 0x10a663c: adrp x0, #0x1e8e000
// 0x10a6640: ldr x0, [x0, #0x4c8]
// 0x10a6644: bl #0xf7d92c
// 0x10a6648: adrp x0, #0x1e8e000
// 0x10a664c: ldr x0, [x0, #0x4d0]
// 0x10a6650: bl #0xf7d92c
// 0x10a6654: adrp x0, #0x1e8e000
// 0x10a6658: ldr x0, [x0, #0x4d8]
// 0x10a665c: bl #0xf7d92c
// 0x10a6660: adrp x0, #0x1e8e000
// 0x10a6664: ldr x0, [x0, #0x4e0]
// 0x10a6668: bl #0xf7d92c
// 0x10a666c: adrp x0, #0x1e8e000
// 0x10a6670: ldr x0, [x0, #0x4e8]
// 0x10a6674: bl #0xf7d92c
// 0x10a6678: adrp x0, #0x1e8e000
// 0x10a667c: ldr x0, [x0, #0x4f0]
// 0x10a6680: bl #0xf7d92c
// 0x10a6684: adrp x0, #0x1e8e000
// 0x10a6688: ldr x0, [x0, #0x4f8]
// 0x10a668c: bl #0xf7d92c
// 0x10a6690: mov w8, #1
// 0x10a6694: strb w8, [x20, #0x4be]
// 0x10a6698: movi v0.2d, #0000000000000000
// 0x10a669c: stur q0, [sp, #0x3c]
// 0x10a66a0: stp q0, q0, [sp, #0x20]
// 0x10a66a4: ldr x0, [x19, #0x30]
// 0x10a66a8: cbz x0, #0x10a75f4
// 0x10a66ac: mov x1, xzr
// 0x10a66b0: bl #0x1b94c14
// 0x10a66b4: cbz x0, #0x10a75f4
// 0x10a66b8: mov x1, xzr
// 0x10a66bc: bl #0x1b9d508
// 0x10a66c0: ldr x0, [x19, #0x30]
// 0x10a66c4: cbz x0, #0x10a75f4
// 0x10a66c8: mov x1, xzr
// 0x10a66cc: mov v8.16b, v0.16b
// 0x10a66d0: mov v9.16b, v1.16b
// 0x10a66d4: mov v10.16b, v2.16b
// 0x10a66d8: bl #0x1b94c14
// 0x10a66dc: adrp x23, #0x1fab000
// 0x10a66e0: ldrb w8, [x23, #0x3e3]
// 0x10a66e4: mov x20, x0
// 0x10a66e8: cbnz w8, #0x10a6700
// 0x10a66ec: adrp x0, #0x1e8c000
// 0x10a66f0: ldr x0, [x0, #0x1e8]
// 0x10a66f4: bl #0xf7d92c
// 0x10a66f8: mov w8, #1
// 0x10a66fc: strb w8, [x23, #0x3e3]
// 0x10a6700: cbz x20, #0x10a75f4
// 0x10a6704: adrp x24, #0x1e8c000
// 0x10a6708: ldr x24, [x24, #0x1e8]
// 0x10a670c: adrp x22, #0x1e8d000
// 0x10a6710: mov x0, x20
// 0x10a6714: mov x1, xzr
// 0x10a6718: ldr x8, [x24]
// 0x10a671c: ldr x8, [x8, #0xb8]
// 0x10a6720: ldp s1, s2, [x8, #0x4c]
// 0x10a6724: ldr s0, [x8, #0x48]
// 0x10a6728: ldr x22, [x22, #0x4a8]
// 0x10a672c: bl #0x1b9e01c
// 0x10a6730: ldr x0, [x22]
// 0x10a6734: mov v11.16b, v0.16b
// 0x10a6738: mov v12.16b, v1.16b
// 0x10a673c: mov v13.16b, v2.16b
// 0x10a6740: ldr w8, [x0, #0xe0]
// 0x10a6744: cbnz w8, #0x10a674c
// 0x10a6748: bl #0xf7da5c
// 0x10a674c: add x0, sp, #0x20
// 0x10a6750: mov v0.16b, v8.16b
// 0x10a6754: mov v1.16b, v9.16b
// 0x10a6758: mov v2.16b, v10.16b
// 0x10a675c: mov v3.16b, v11.16b
// 0x10a6760: mov v4.16b, v12.16b
// 0x10a6764: mov v5.16b, v13.16b
// 0x10a6768: mov x1, xzr
// 0x10a676c: bl #0x1bcbdec
// 0x10a6770: tbz w0, #0, #0x10a6824
// 0x10a6774: add x0, sp, #0x20
// 0x10a6778: mov x1, xzr
// 0x10a677c: bl #0x1bcec58
// 0x10a6780: cbz x0, #0x10a75f4
// 0x10a6784: mov x1, xzr
// 0x10a6788: bl #0x1b92704
// 0x10a678c: adrp x8, #0x1e8e000
// 0x10a6790: ldr x8, [x8, #0xb8]
// 0x10a6794: mov x2, xzr
// 0x10a6798: ldr x1, [x8]
// 0x10a679c: bl #0x17f610c
// 0x10a67a0: tbnz w0, #0, #0x10a67d4
// 0x10a67a4: add x0, sp, #0x20
// 0x10a67a8: mov x1, xzr
// 0x10a67ac: bl #0x1bcec58
// 0x10a67b0: cbz x0, #0x10a75f4
// 0x10a67b4: mov x1, xzr
// 0x10a67b8: bl #0x1b92704
// 0x10a67bc: adrp x8, #0x1e8e000
// 0x10a67c0: ldr x8, [x8, #0x3c8]
// 0x10a67c4: mov x2, xzr
// 0x10a67c8: ldr x1, [x8]
// 0x10a67cc: bl #0x17f610c
// 0x10a67d0: tbz w0, #0, #0x10a6810
// 0x10a67d4: ldr x0, [x19, #0x28]
// 0x10a67d8: cbz x0, #0x10a75f4
// 0x10a67dc: mov w1, #1
// 0x10a67e0: mov x2, xzr
// 0x10a67e4: bl #0x1b94cd0
// 0x10a67e8: ldrb w8, [x19, #0x88]
// 0x10a67ec: cbnz w8, #0x10a6824
// 0x10a67f0: ldr x0, [x19, #0x80]
// 0x10a67f4: cbz x0, #0x10a75f4
// 0x10a67f8: ldr x1, [x19, #0x78]
// 0x10a67fc: mov x2, xzr
// 0x10a6800: bl #0x1b6a664
// 0x10a6804: mov w8, #1
// 0x10a6808: strb w8, [x19, #0x88]
// 0x10a680c: b #0x10a6824
// 0x10a6810: ldr x0, [x19, #0x28]
// 0x10a6814: cbz x0, #0x10a75f4
// 0x10a6818: mov w1, wzr
// 0x10a681c: mov x2, xzr
// 0x10a6820: bl #0x1b94cd0
// 0x10a6824: adrp x26, #0x1e8c000
// 0x10a6828: ldr x26, [x26, #0xd8]
// 0x10a682c: ldr x20, [x19, #0x20]
// 0x10a6830: ldr x0, [x26]
// 0x10a6834: ldr w8, [x0, #0xe0]
// 0x10a6838: cbnz w8, #0x10a6840
// 0x10a683c: bl #0xf7da5c
// 0x10a6840: mov x0, x20
// 0x10a6844: mov x1, xzr
// 0x10a6848: bl #0x1b98274
// 0x10a684c: tbz w0, #0, #0x10a6860
// 0x10a6850: ldr x8, [x19, #0x20]
// 0x10a6854: cbz x8, #0x10a75f4
// 0x10a6858: ldrb w8, [x8, #0x3ce]
// 0x10a685c: cbz w8, #0x10a6894
// 0x10a6860: strb wzr, [x19, #0x89]
// 0x10a6864: ldp x20, x19, [sp, #0xd0]
// 0x10a6868: ldp x22, x21, [sp, #0xc0]
// 0x10a686c: ldp x24, x23, [sp, #0xb0]
// 0x10a6870: ldp x26, x25, [sp, #0xa0]
// 0x10a6874: ldp x28, x27, [sp, #0x90]
// 0x10a6878: ldr x30, [sp, #0x88]
// 0x10a687c: ldp d9, d8, [sp, #0x78]
// 0x10a6880: ldp d11, d10, [sp, #0x68]
// 0x10a6884: ldp d13, d12, [sp, #0x58]
// 0x10a6888: ldr d14, [sp, #0x50]
// 0x10a688c: add sp, sp, #0xe0
// 0x10a6890: ret
// 0x10a6894: adrp x21, #0x1e8c000
// 0x10a6898: ldr x21, [x21, #0xe0]
// 0x10a689c: ldr x0, [x21]
// 0x10a68a0: ldr w8, [x0, #0xe0]
// 0x10a68a4: cbnz w8, #0x10a68ac
// 0x10a68a8: bl #0xf7da5c
// 0x10a68ac: adrp x8, #0x1e8d000
// 0x10a68b0: ldr x8, [x8, #8]
// 0x10a68b4: mov x1, xzr
// 0x10a68b8: ldr x0, [x8]
// 0x10a68bc: bl #0x1036390
// 0x10a68c0: and w8, w0, #1
// 0x10a68c4: strb w8, [x19, #0xbc]
// 0x10a68c8: adrp x8, #0x1e8c000
// 0x10a68cc: ldr x8, [x8, #0xfd0]
// 0x10a68d0: mov x1, xzr
// 0x10a68d4: ldr x0, [x8]
// 0x10a68d8: bl #0x1036390
// 0x10a68dc: and w8, w0, #1
// 0x10a68e0: strb w8, [x19, #0xbd]
// 0x10a68e4: adrp x8, #0x1e8e000
// 0x10a68e8: ldr x8, [x8, #0x418]
// 0x10a68ec: mov x1, xzr
// 0x10a68f0: ldr x0, [x8]
// 0x10a68f4: bl #0x1036390
// 0x10a68f8: and w8, w0, #1
// 0x10a68fc: strb w8, [x19, #0xbe]
// 0x10a6900: adrp x8, #0x1e8e000
// 0x10a6904: ldr x8, [x8, #0x3e8]
// 0x10a6908: mov x1, xzr
// 0x10a690c: ldr x0, [x8]
// 0x10a6910: bl #0x1036390
// 0x10a6914: ldrb w9, [x19, #0xbc]
// 0x10a6918: ldrb w8, [x19, #0xbd]
// 0x10a691c: and w10, w0, #1
// 0x10a6920: strb w10, [x19, #0xbf]
// 0x10a6924: cbz w9, #0x10a6934
// 0x10a6928: cbnz w8, #0x10a693c
// 0x10a692c: fmov s0, #-1.00000000
// 0x10a6930: b #0x10a6940
// 0x10a6934: fmov s0, #1.00000000
// 0x10a6938: cbnz w8, #0x10a6940
// 0x10a693c: fmov s0, wzr
// 0x10a6940: ldrb w8, [x19, #0xbe]
// 0x10a6944: str s0, [x19, #0xc0]
// 0x10a6948: cbz w8, #0x10a69b0
// 0x10a694c: fmov s0, #1.00000000
// 0x10a6950: tbz w0, #0, #0x10a6958
// 0x10a6954: fmov s0, wzr
// 0x10a6958: str s0, [x19, #0xc4]
// 0x10a695c: ldr x0, [x21]
// 0x10a6960: ldr w8, [x0, #0xe0]
// 0x10a6964: cbnz w8, #0x10a696c
// 0x10a6968: bl #0xf7da5c
// 0x10a696c: adrp x8, #0x1e8e000
// 0x10a6970: ldr x8, [x8, #0x4e8]
// 0x10a6974: mov x1, xzr
// 0x10a6978: ldr x0, [x8]
// 0x10a697c: bl #0x1035e20
// 0x10a6980: adrp x8, #0x1e8e000
// 0x10a6984: ldr x8, [x8, #0x428]
// 0x10a6988: mov x1, xzr
// 0x10a698c: mov v8.16b, v0.16b
// 0x10a6990: ldr x0, [x8]
// 0x10a6994: bl #0x1035e20
// 0x10a6998: stp s8, s0, [x19, #0xcc]
// 0x10a699c: adrp x20, #0x1fab000
// 0x10a69a0: ldrb w8, [x20, #0x243]
// 0x10a69a4: cbz w8, #0x10a69bc
// 0x10a69a8: mov v9.16b, v0.16b
// 0x10a69ac: b #0x10a69d4
// 0x10a69b0: fmov s0, #-1.00000000
// 0x10a69b4: tbz w0, #0, #0x10a6954
// 0x10a69b8: b #0x10a6958
// 0x10a69bc: adrp x0, #0x1e8c000
// 0x10a69c0: ldr x0, [x0, #0xa60]
// 0x10a69c4: bl #0xf7d92c
// 0x10a69c8: mov w8, #1
// 0x10a69cc: strb w8, [x20, #0x243]
// 0x10a69d0: ldp s8, s9, [x19, #0xcc]
// 0x10a69d4: adrp x25, #0x1e8c000
// 0x10a69d8: ldr x25, [x25, #0xa60]
// 0x10a69dc: ldr x0, [x25]
// 0x10a69e0: ldr w8, [x0, #0xe0]
// 0x10a69e4: cbnz w8, #0x10a69ec
// 0x10a69e8: bl #0xf7da5c
// 0x10a69ec: ldr s1, [x19, #0xc8]
// 0x10a69f0: fmul s0, s8, s8
// 0x10a69f4: fmul s2, s9, s9
// 0x10a69f8: fadd s0, s0, s2
// 0x10a69fc: fsqrt s0, s0
// 0x10a6a00: fcmp s0, s1
// 0x10a6a04: adrp x27, #0x832000
// 0x10a6a08: b.pl #0x10a6a44
// 0x10a6a0c: adrp x28, #0x1fab000
// 0x10a6a10: ldrb w8, [x28, #0x1e0]
// 0x10a6a14: cbnz w8, #0x10a6a2c
// 0x10a6a18: adrp x0, #0x1e8c000
// 0x10a6a1c: ldr x0, [x0, #0x138]
// 0x10a6a20: bl #0xf7d92c
// 0x10a6a24: mov w8, #1
// 0x10a6a28: strb w8, [x28, #0x1e0]
// 0x10a6a2c: adrp x8, #0x1e8c000
// 0x10a6a30: ldr x8, [x8, #0x138]
// 0x10a6a34: ldr x8, [x8]
// 0x10a6a38: ldr x8, [x8, #0xb8]
// 0x10a6a3c: ldr d0, [x8]
// 0x10a6a40: b #0x10a6b24
// 0x10a6a44: ldrb w8, [x20, #0x243]
// 0x10a6a48: ldur d8, [x19, #0xcc]
// 0x10a6a4c: cbnz w8, #0x10a6a64
// 0x10a6a50: adrp x0, #0x1e8c000
// 0x10a6a54: ldr x0, [x0, #0xa60]
// 0x10a6a58: bl #0xf7d92c
// 0x10a6a5c: mov w8, #1
// 0x10a6a60: strb w8, [x20, #0x243]
// 0x10a6a64: ldr x0, [x25]
// 0x10a6a68: ldr w8, [x0, #0xe0]
// 0x10a6a6c: cbnz w8, #0x10a6a74
// 0x10a6a70: bl #0xf7da5c
// 0x10a6a74: ldr s1, [x27, #0x41c]
// 0x10a6a78: fmul v0.2s, v8.2s, v8.2s
// 0x10a6a7c: faddp s0, v0.2s
// 0x10a6a80: fsqrt s0, s0
// 0x10a6a84: fcmp s0, s1
// 0x10a6a88: b.le #0x10a6a98
// 0x10a6a8c: dup v0.2s, v0.s[0]
// 0x10a6a90: fdiv v8.2s, v8.2s, v0.2s
// 0x10a6a94: b #0x10a6acc
// 0x10a6a98: adrp x28, #0x1fab000
// 0x10a6a9c: ldrb w8, [x28, #0x1e0]
// 0x10a6aa0: cbnz w8, #0x10a6ab8
// 0x10a6aa4: adrp x0, #0x1e8c000
// 0x10a6aa8: ldr x0, [x0, #0x138]
// 0x10a6aac: bl #0xf7d92c
// 0x10a6ab0: mov w8, #1
// 0x10a6ab4: strb w8, [x28, #0x1e0]
// 0x10a6ab8: adrp x8, #0x1e8c000
// 0x10a6abc: ldr x8, [x8, #0x138]
// 0x10a6ac0: ldr x8, [x8]
// 0x10a6ac4: ldr x8, [x8, #0xb8]
// 0x10a6ac8: ldr d8, [x8]
// 0x10a6acc: ldrb w8, [x20, #0x243]
// 0x10a6ad0: cbnz w8, #0x10a6ae8
// 0x10a6ad4: adrp x0, #0x1e8c000
// 0x10a6ad8: ldr x0, [x0, #0xa60]
// 0x10a6adc: bl #0xf7d92c
// 0x10a6ae0: mov w8, #1
// 0x10a6ae4: strb w8, [x20, #0x243]
// 0x10a6ae8: ldr x0, [x25]
// 0x10a6aec: ldp s10, s9, [x19, #0xcc]
// 0x10a6af0: ldr w8, [x0, #0xe0]
// 0x10a6af4: cbnz w8, #0x10a6afc
// 0x10a6af8: bl #0xf7da5c
// 0x10a6afc: ldr s2, [x19, #0xc8]
// 0x10a6b00: fmul s0, s10, s10
// 0x10a6b04: fmul s1, s9, s9
// 0x10a6b08: fadd s0, s0, s1
// 0x10a6b0c: fmov s3, #1.00000000
// 0x10a6b10: fsqrt s0, s0
// 0x10a6b14: fsub s0, s0, s2
// 0x10a6b18: fsub s1, s3, s2
// 0x10a6b1c: fdiv s0, s0, s1
// 0x10a6b20: fmul v0.2s, v8.2s, v0.s[0]
// 0x10a6b24: stur d0, [x19, #0xcc]
// 0x10a6b28: ldr x0, [x21]
// 0x10a6b2c: ldr w8, [x0, #0xe0]
// 0x10a6b30: cbnz w8, #0x10a6b38
// 0x10a6b34: bl #0xf7da5c
// 0x10a6b38: adrp x8, #0x1e8e000
// 0x10a6b3c: ldr x8, [x8, #0x410]
// 0x10a6b40: mov x1, xzr
// 0x10a6b44: ldr x0, [x8]
// 0x10a6b48: bl #0x1035e20
// 0x10a6b4c: mov x0, xzr
// 0x10a6b50: str d0, [sp, #0x10]
// 0x10a6b54: bl #0x1b9ae30
// 0x10a6b58: adrp x8, #0x1e8e000
// 0x10a6b5c: ldr x8, [x8, #0x4f0]
// 0x10a6b60: mov x1, xzr
// 0x10a6b64: str d0, [sp]
// 0x10a6b68: ldr x0, [x8]
// 0x10a6b6c: bl #0x1035e20
// 0x10a6b70: ldr q1, [sp, #0x10]
// 0x10a6b74: mov x0, xzr
// 0x10a6b78: mov v1.s[1], v0.s[0]
// 0x10a6b7c: str q1, [sp, #0x10]
// 0x10a6b80: fabs v8.2s, v1.2s
// 0x10a6b84: bl #0x1b9ae30
// 0x10a6b88: ldr q3, [sp]
// 0x10a6b8c: movi v1.2s, #0x3e, lsl #24
// 0x10a6b90: movi v2.2s, #0x41, lsl #24
// 0x10a6b94: mov w8, #0x42700000
// 0x10a6b98: mov v3.s[1], v0.s[0]
// 0x10a6b9c: ldr q0, [sp, #0x10]
// 0x10a6ba0: fmul v0.2s, v0.2s, v1.2s
// 0x10a6ba4: fmul v1.2s, v8.2s, v2.2s
// 0x10a6ba8: fmul v0.2s, v0.2s, v1.2s
// 0x10a6bac: fmul v0.2s, v3.2s, v0.2s
// 0x10a6bb0: dup v1.2s, w8
// 0x10a6bb4: fmul v8.2s, v0.2s, v1.2s
// 0x10a6bb8: stur d8, [x19, #0xd4]
// 0x10a6bbc: ldrb w8, [x20, #0x243]
// 0x10a6bc0: cbnz w8, #0x10a6bdc
// 0x10a6bc4: adrp x0, #0x1e8c000
// 0x10a6bc8: ldr x0, [x0, #0xa60]
// 0x10a6bcc: bl #0xf7d92c
// 0x10a6bd0: mov w8, #1
// 0x10a6bd4: strb w8, [x20, #0x243]
// 0x10a6bd8: ldur d8, [x19, #0xd4]
// 0x10a6bdc: ldr x0, [x25]
// 0x10a6be0: ldr w8, [x0, #0xe0]
// 0x10a6be4: cbnz w8, #0x10a6bec
// 0x10a6be8: bl #0xf7da5c
// 0x10a6bec: ldr s0, [x19, #0xc8]
// 0x10a6bf0: fmul v1.2s, v8.2s, v8.2s
// 0x10a6bf4: faddp s1, v1.2s
// 0x10a6bf8: fsqrt s1, s1
// 0x10a6bfc: fcmp s1, s0
// 0x10a6c00: b.pl #0x10a6c3c
// 0x10a6c04: adrp x20, #0x1fab000
// 0x10a6c08: ldrb w8, [x20, #0x1e0]
// 0x10a6c0c: cbnz w8, #0x10a6c24
// 0x10a6c10: adrp x0, #0x1e8c000
// 0x10a6c14: ldr x0, [x0, #0x138]
// 0x10a6c18: bl #0xf7d92c
// 0x10a6c1c: mov w8, #1
// 0x10a6c20: strb w8, [x20, #0x1e0]
// 0x10a6c24: adrp x8, #0x1e8c000
// 0x10a6c28: ldr x8, [x8, #0x138]
// 0x10a6c2c: ldr x8, [x8]
// 0x10a6c30: ldr x8, [x8, #0xb8]
// 0x10a6c34: ldr d0, [x8]
// 0x10a6c38: b #0x10a6d1c
// 0x10a6c3c: ldrb w8, [x20, #0x243]
// 0x10a6c40: ldur d8, [x19, #0xd4]
// 0x10a6c44: cbnz w8, #0x10a6c5c
// 0x10a6c48: adrp x0, #0x1e8c000
// 0x10a6c4c: ldr x0, [x0, #0xa60]
// 0x10a6c50: bl #0xf7d92c
// 0x10a6c54: mov w8, #1
// 0x10a6c58: strb w8, [x20, #0x243]
// 0x10a6c5c: ldr x0, [x25]
// 0x10a6c60: ldr w8, [x0, #0xe0]
// 0x10a6c64: cbnz w8, #0x10a6c6c
// 0x10a6c68: bl #0xf7da5c
// 0x10a6c6c: ldr s1, [x27, #0x41c]
// 0x10a6c70: fmul v0.2s, v8.2s, v8.2s
// 0x10a6c74: faddp s0, v0.2s
// 0x10a6c78: fsqrt s0, s0
// 0x10a6c7c: fcmp s0, s1
// 0x10a6c80: b.le #0x10a6c90
// 0x10a6c84: dup v0.2s, v0.s[0]
// 0x10a6c88: fdiv v8.2s, v8.2s, v0.2s
// 0x10a6c8c: b #0x10a6cc4
// 0x10a6c90: adrp x27, #0x1fab000
// 0x10a6c94: ldrb w8, [x27, #0x1e0]
// 0x10a6c98: cbnz w8, #0x10a6cb0
// 0x10a6c9c: adrp x0, #0x1e8c000
// 0x10a6ca0: ldr x0, [x0, #0x138]
// 0x10a6ca4: bl #0xf7d92c
// 0x10a6ca8: mov w8, #1
// 0x10a6cac: strb w8, [x27, #0x1e0]
// 0x10a6cb0: adrp x8, #0x1e8c000
// 0x10a6cb4: ldr x8, [x8, #0x138]
// 0x10a6cb8: ldr x8, [x8]
// 0x10a6cbc: ldr x8, [x8, #0xb8]
// 0x10a6cc0: ldr d8, [x8]
// 0x10a6cc4: ldrb w8, [x20, #0x243]
// 0x10a6cc8: cbnz w8, #0x10a6ce0
// 0x10a6ccc: adrp x0, #0x1e8c000
// 0x10a6cd0: ldr x0, [x0, #0xa60]
// 0x10a6cd4: bl #0xf7d92c
// 0x10a6cd8: mov w8, #1
// 0x10a6cdc: strb w8, [x20, #0x243]
// 0x10a6ce0: ldr x0, [x25]
// 0x10a6ce4: ldp s10, s9, [x19, #0xd4]
// 0x10a6ce8: ldr w8, [x0, #0xe0]
// 0x10a6cec: cbnz w8, #0x10a6cf4
// 0x10a6cf0: bl #0xf7da5c
// 0x10a6cf4: ldr s2, [x19, #0xc8]
// 0x10a6cf8: fmul s0, s10, s10
// 0x10a6cfc: fmul s1, s9, s9
// 0x10a6d00: fadd s0, s0, s1
// 0x10a6d04: fmov s3, #1.00000000
// 0x10a6d08: fsqrt s0, s0
// 0x10a6d0c: fsub s0, s0, s2
// 0x10a6d10: fsub s1, s3, s2
// 0x10a6d14: fdiv s0, s0, s1
// 0x10a6d18: fmul v0.2s, v8.2s, v0.s[0]
// 0x10a6d1c: ldr d1, [x19, #0xc0]
// 0x10a6d20: ldur d2, [x19, #0xcc]
// 0x10a6d24: stur d0, [x19, #0xd4]
// 0x10a6d28: fmov v0.2s, #-1.00000000
// 0x10a6d2c: fmov v3.2s, #1.00000000
// 0x10a6d30: fadd v1.2s, v1.2s, v2.2s
// 0x10a6d34: fcmgt v2.2s, v0.2s, v1.2s
// 0x10a6d38: fmin v1.2s, v1.2s, v3.2s
// 0x10a6d3c: bif v0.8b, v1.8b, v2.8b
// 0x10a6d40: stur d0, [x19, #0xdc]
// 0x10a6d44: ldr x0, [x21]
// 0x10a6d48: ldr w8, [x0, #0xe0]
// 0x10a6d4c: cbnz w8, #0x10a6d54
// 0x10a6d50: bl #0xf7da5c
// 0x10a6d54: adrp x8, #0x1e8c000
// 0x10a6d58: ldr x8, [x8, #0x550]
// 0x10a6d5c: mov x1, xzr
// 0x10a6d60: ldr x0, [x8]
// 0x10a6d64: bl #0x10360d8
// 0x10a6d68: ldr s1, [x19, #0xd4]
// 0x10a6d6c: adrp x8, #0x1e8c000
// 0x10a6d70: mov x1, xzr
// 0x10a6d74: fadd s0, s0, s1
// 0x10a6d78: str s0, [x19, #0xe4]
// 0x10a6d7c: ldr x8, [x8, #0x530]
// 0x10a6d80: ldr x0, [x8]
// 0x10a6d84: bl #0x10360d8
// 0x10a6d88: ldr s1, [x19, #0xd8]
// 0x10a6d8c: adrp x8, #0x1e8e000
// 0x10a6d90: mov x1, xzr
// 0x10a6d94: fadd s0, s0, s1
// 0x10a6d98: str s0, [x19, #0xe8]
// 0x10a6d9c: ldr x8, [x8, #0x440]
// 0x10a6da0: ldr x0, [x8]
// 0x10a6da4: bl #0x10360d8
// 0x10a6da8: adrp x8, #0x832000
// 0x10a6dac: ldr s14, [x8, #0x3b8]
// 0x10a6db0: fcmp s0, s14
// 0x10a6db4: b.gt #0x10a6de0
// 0x10a6db8: ldr x0, [x21]
// 0x10a6dbc: ldr w8, [x0, #0xe0]
// 0x10a6dc0: cbnz w8, #0x10a6dc8
// 0x10a6dc4: bl #0xf7da5c
// 0x10a6dc8: adrp x8, #0x1e8e000
// 0x10a6dcc: ldr x8, [x8, #0x4b8]
// 0x10a6dd0: mov x1, xzr
// 0x10a6dd4: ldr x0, [x8]
// 0x10a6dd8: bl #0x1036390
// 0x10a6ddc: tbz w0, #0, #0x10a6dec
// 0x10a6de0: mov w8, #1
// 0x10a6de4: strb w8, [x19, #0x89]
// 0x10a6de8: b #0x10a6fe0
// 0x10a6dec: ldr x0, [x26]
// 0x10a6df0: ldr x20, [x19, #0x58]
// 0x10a6df4: ldr w8, [x0, #0xe0]
// 0x10a6df8: cbnz w8, #0x10a6e00
// 0x10a6dfc: bl #0xf7da5c
// 0x10a6e00: mov x0, x20
// 0x10a6e04: mov x1, xzr
// 0x10a6e08: bl #0x1b98274
// 0x10a6e0c: tbz w0, #0, #0x10a6fdc
// 0x10a6e10: ldr x0, [x19, #0x30]
// 0x10a6e14: cbz x0, #0x10a75f4
// 0x10a6e18: mov x1, xzr
// 0x10a6e1c: bl #0x1b94c14
// 0x10a6e20: cbz x0, #0x10a75f4
// 0x10a6e24: mov x1, xzr
// 0x10a6e28: bl #0x1b9d508
// 0x10a6e2c: ldr x0, [x19, #0x30]
// 0x10a6e30: cbz x0, #0x10a75f4
// 0x10a6e34: mov x1, xzr
// 0x10a6e38: mov v8.16b, v0.16b
// 0x10a6e3c: mov v9.16b, v1.16b
// 0x10a6e40: mov v10.16b, v2.16b
// 0x10a6e44: bl #0x1b94c14
// 0x10a6e48: ldrb w8, [x23, #0x3e3]
// 0x10a6e4c: mov x20, x0
// 0x10a6e50: cbnz w8, #0x10a6e68
// 0x10a6e54: adrp x0, #0x1e8c000
// 0x10a6e58: ldr x0, [x0, #0x1e8]
// 0x10a6e5c: bl #0xf7d92c
// 0x10a6e60: mov w8, #1
// 0x10a6e64: strb w8, [x23, #0x3e3]
// 0x10a6e68: cbz x20, #0x10a75f4
// 0x10a6e6c: ldr x8, [x24]
// 0x10a6e70: mov x0, x20
// 0x10a6e74: mov x1, xzr
// 0x10a6e78: ldr x8, [x8, #0xb8]
// 0x10a6e7c: ldp s1, s2, [x8, #0x4c]
// 0x10a6e80: ldr s0, [x8, #0x48]
// 0x10a6e84: bl #0x1b9e01c
// 0x10a6e88: ldr x0, [x22]
// 0x10a6e8c: mov v11.16b, v0.16b
// 0x10a6e90: mov v12.16b, v1.16b
// 0x10a6e94: mov v13.16b, v2.16b
// 0x10a6e98: ldr w8, [x0, #0xe0]
// 0x10a6e9c: cbnz w8, #0x10a6ea4
// 0x10a6ea0: bl #0xf7da5c
// 0x10a6ea4: add x0, sp, #0x20
// 0x10a6ea8: mov v0.16b, v8.16b
// 0x10a6eac: mov v1.16b, v9.16b
// 0x10a6eb0: mov v2.16b, v10.16b
// 0x10a6eb4: mov v3.16b, v11.16b
// 0x10a6eb8: mov v4.16b, v12.16b
// 0x10a6ebc: mov v5.16b, v13.16b
// 0x10a6ec0: mov x1, xzr
// 0x10a6ec4: bl #0x1bcbdec
// 0x10a6ec8: tbz w0, #0, #0x10a6fdc
// 0x10a6ecc: add x0, sp, #0x20
// 0x10a6ed0: mov x1, xzr
// 0x10a6ed4: bl #0x1bcec58
// 0x10a6ed8: cbz x0, #0x10a75f4
// 0x10a6edc: mov x1, xzr
// 0x10a6ee0: bl #0x1b92704
// 0x10a6ee4: adrp x8, #0x1e8e000
// 0x10a6ee8: ldr x8, [x8, #0xb8]
// 0x10a6eec: mov x2, xzr
// 0x10a6ef0: ldr x1, [x8]
// 0x10a6ef4: bl #0x17f610c
// 0x10a6ef8: tbnz w0, #0, #0x10a6f2c
// 0x10a6efc: add x0, sp, #0x20
// 0x10a6f00: mov x1, xzr
// 0x10a6f04: bl #0x1bcec58
// 0x10a6f08: cbz x0, #0x10a75f4
// 0x10a6f0c: mov x1, xzr
// 0x10a6f10: bl #0x1b92704
// 0x10a6f14: adrp x8, #0x1e8e000
// 0x10a6f18: ldr x8, [x8, #0x3c8]
// 0x10a6f1c: mov x2, xzr
// 0x10a6f20: ldr x1, [x8]
// 0x10a6f24: bl #0x17f610c
// 0x10a6f28: tbz w0, #0, #0x10a6fdc
// 0x10a6f2c: mov x0, x19
// 0x10a6f30: mov x1, xzr
// 0x10a6f34: bl #0x1b92154
// 0x10a6f38: cbz x0, #0x10a75f4
// 0x10a6f3c: mov x1, xzr
// 0x10a6f40: bl #0x1b9d508
// 0x10a6f44: add x0, sp, #0x20
// 0x10a6f48: mov x1, xzr
// 0x10a6f4c: mov v8.16b, v0.16b
// 0x10a6f50: mov v9.16b, v1.16b
// 0x10a6f54: mov v10.16b, v2.16b
// 0x10a6f58: bl #0x1bced24
// 0x10a6f5c: cbz x0, #0x10a75f4
// 0x10a6f60: mov x1, xzr
// 0x10a6f64: bl #0x1b9d508
// 0x10a6f68: adrp x20, #0x1fab000
// 0x10a6f6c: ldrb w8, [x20, #0x3e0]
// 0x10a6f70: mov v11.16b, v0.16b
// 0x10a6f74: mov v12.16b, v1.16b
// 0x10a6f78: mov v13.16b, v2.16b
// 0x10a6f7c: cbnz w8, #0x10a6f94
// 0x10a6f80: adrp x0, #0x1e8c000
// 0x10a6f84: ldr x0, [x0, #0xa60]
// 0x10a6f88: bl #0xf7d92c
// 0x10a6f8c: mov w8, #1
// 0x10a6f90: strb w8, [x20, #0x3e0]
// 0x10a6f94: ldr x0, [x25]
// 0x10a6f98: fsub s11, s8, s11
// 0x10a6f9c: fsub s9, s9, s12
// 0x10a6fa0: fsub s8, s10, s13
// 0x10a6fa4: ldr w8, [x0, #0xe0]
// 0x10a6fa8: cbnz w8, #0x10a6fb0
// 0x10a6fac: bl #0xf7da5c
// 0x10a6fb0: fmul s0, s11, s11
// 0x10a6fb4: fmul s1, s9, s9
// 0x10a6fb8: fmul s2, s8, s8
// 0x10a6fbc: fadd s0, s0, s1
// 0x10a6fc0: fadd s0, s2, s0
// 0x10a6fc4: fsqrt s0, s0
// 0x10a6fc8: fmov s1, #30.00000000
// 0x10a6fcc: fcmp s0, s1
// 0x10a6fd0: b.hi #0x10a6fe0
// 0x10a6fd4: ldrb w8, [x19, #0x70]
// 0x10a6fd8: cbnz w8, #0x10a6de0
// 0x10a6fdc: strb wzr, [x19, #0x89]
// 0x10a6fe0: ldr x0, [x21]
// 0x10a6fe4: ldr w8, [x0, #0xe0]
// 0x10a6fe8: cbnz w8, #0x10a6ff0
// 0x10a6fec: bl #0xf7da5c
// 0x10a6ff0: adrp x8, #0x1e8e000
// 0x10a6ff4: ldr x8, [x8, #0x4a0]
// 0x10a6ff8: mov x1, xzr
// 0x10a6ffc: ldr x0, [x8]
// 0x10a7000: bl #0x10360d8
// 0x10a7004: fcmp s0, s14
// 0x10a7008: b.le #0x10a7014
// 0x10a700c: mov w8, #1
// 0x10a7010: b #0x10a703c
// 0x10a7014: ldr x0, [x21]
// 0x10a7018: ldr w8, [x0, #0xe0]
// 0x10a701c: cbnz w8, #0x10a7024
// 0x10a7020: bl #0xf7da5c
// 0x10a7024: adrp x8, #0x1e8e000
// 0x10a7028: ldr x8, [x8, #0x3b0]
// 0x10a702c: mov x1, xzr
// 0x10a7030: ldr x0, [x8]
// 0x10a7034: bl #0x1036390
// 0x10a7038: and w8, w0, #1
// 0x10a703c: strb w8, [x19, #0x92]
// 0x10a7040: ldr x0, [x21]
// 0x10a7044: ldr w8, [x0, #0xe0]
// 0x10a7048: cbnz w8, #0x10a7050
// 0x10a704c: bl #0xf7da5c
// 0x10a7050: adrp x20, #0x1e8e000
// 0x10a7054: ldr x20, [x20, #0x4e0]
// 0x10a7058: mov x1, xzr
// 0x10a705c: ldr x0, [x20]
// 0x10a7060: bl #0x1035e20
// 0x10a7064: fcmp s0, #0.0
// 0x10a7068: b.le #0x10a7088
// 0x10a706c: ldrb w8, [x19, #0xf5]
// 0x10a7070: mov w9, #0x100
// 0x10a7074: strh w9, [x19, #0xec]
// 0x10a7078: strb wzr, [x19, #0xf4]
// 0x10a707c: cbz w8, #0x10a70dc
// 0x10a7080: strb wzr, [x19, #0xf1]
// 0x10a7084: b #0x10a70f4
// 0x10a7088: ldr x0, [x21]
// 0x10a708c: ldr w8, [x0, #0xe0]
// 0x10a7090: cbnz w8, #0x10a7098
// 0x10a7094: bl #0xf7da5c
// 0x10a7098: ldr x0, [x20]
// 0x10a709c: mov x1, xzr
// 0x10a70a0: bl #0x1035e20
// 0x10a70a4: fcmp s0, #0.0
// 0x10a70a8: strb wzr, [x19, #0xed]
// 0x10a70ac: b.pl #0x10a70cc
// 0x10a70b0: ldrb w9, [x19, #0xf4]
// 0x10a70b4: mov w8, #1
// 0x10a70b8: strb w8, [x19, #0xec]
// 0x10a70bc: strb wzr, [x19, #0xf5]
// 0x10a70c0: cbz w9, #0x10a70ec
// 0x10a70c4: strb wzr, [x19, #0xf0]
// 0x10a70c8: b #0x10a70f4
// 0x10a70cc: strb wzr, [x19, #0xec]
// 0x10a70d0: strh wzr, [x19, #0xf0]
// 0x10a70d4: strh wzr, [x19, #0xf4]
// 0x10a70d8: b #0x10a70f4
// 0x10a70dc: mov w8, #1
// 0x10a70e0: strb w8, [x19, #0xf1]
// 0x10a70e4: strb w8, [x19, #0xf5]
// 0x10a70e8: b #0x10a70f4
// 0x10a70ec: strb w8, [x19, #0xf0]
// 0x10a70f0: strb w8, [x19, #0xf4]
// 0x10a70f4: ldr x0, [x21]
// 0x10a70f8: ldr w8, [x0, #0xe0]
// 0x10a70fc: cbnz w8, #0x10a7104
// 0x10a7100: bl #0xf7da5c
// 0x10a7104: adrp x20, #0x1e8e000
// 0x10a7108: ldr x20, [x20, #0x3d8]
// 0x10a710c: mov x1, xzr
// 0x10a7110: ldr x0, [x20]
// 0x10a7114: bl #0x1035e20
// 0x10a7118: fcmp s0, #0.0
// 0x10a711c: b.le #0x10a713c
// 0x10a7120: ldrb w9, [x19, #0xf6]
// 0x10a7124: mov w8, #1
// 0x10a7128: strh w8, [x19, #0xee]
// 0x10a712c: strb wzr, [x19, #0xf7]
// 0x10a7130: cbz w9, #0x10a7190
// 0x10a7134: strb wzr, [x19, #0xf2]
// 0x10a7138: b #0x10a71a4
// 0x10a713c: ldr x0, [x21]
// 0x10a7140: ldr w8, [x0, #0xe0]
// 0x10a7144: cbnz w8, #0x10a714c
// 0x10a7148: bl #0xf7da5c
// 0x10a714c: ldr x0, [x20]
// 0x10a7150: mov x1, xzr
// 0x10a7154: bl #0x1035e20
// 0x10a7158: fcmp s0, #0.0
// 0x10a715c: strb wzr, [x19, #0xee]
// 0x10a7160: b.pl #0x10a7180
// 0x10a7164: ldrb w9, [x19, #0xf7]
// 0x10a7168: mov w8, #1
// 0x10a716c: strb w8, [x19, #0xef]
// 0x10a7170: strb wzr, [x19, #0xf6]
// 0x10a7174: cbz w9, #0x10a719c
// 0x10a7178: strb wzr, [x19, #0xf3]
// 0x10a717c: b #0x10a71a4
// 0x10a7180: strb wzr, [x19, #0xef]
// 0x10a7184: strh wzr, [x19, #0xf2]
// 0x10a7188: strh wzr, [x19, #0xf6]
// 0x10a718c: b #0x10a71a4
// 0x10a7190: strb w8, [x19, #0xf2]
// 0x10a7194: strb w8, [x19, #0xf6]
// 0x10a7198: b #0x10a71a4
// 0x10a719c: strb w8, [x19, #0xf3]
// 0x10a71a0: strb w8, [x19, #0xf7]
// 0x10a71a4: ldr x0, [x21]
// 0x10a71a8: ldr w8, [x0, #0xe0]
// 0x10a71ac: cbnz w8, #0x10a71b4
// 0x10a71b0: bl #0xf7da5c
// 0x10a71b4: adrp x8, #0x1e8d000
// 0x10a71b8: ldr x8, [x8, #0xfd0]
// 0x10a71bc: mov x1, xzr
// 0x10a71c0: ldr x0, [x8]
// 0x10a71c4: bl #0x1035e20
// 0x10a71c8: str s0, [x19, #0xb8]
// 0x10a71cc: adrp x8, #0x1e8e000
// 0x10a71d0: ldr x8, [x8, #0x4b8]
// 0x10a71d4: mov x1, xzr
// 0x10a71d8: ldr x0, [x8]
// 0x10a71dc: bl #0x1036634
// 0x10a71e0: and w8, w0, #1
// 0x10a71e4: strb w8, [x19, #0x8a]
// 0x10a71e8: adrp x8, #0x1e8e000
// 0x10a71ec: ldr x8, [x8, #0x3b0]
// 0x10a71f0: mov x1, xzr
// 0x10a71f4: ldr x0, [x8]
// 0x10a71f8: bl #0x1036634
// 0x10a71fc: and w8, w0, #1
// 0x10a7200: strb w8, [x19, #0x93]
// 0x10a7204: adrp x8, #0x1e8e000
// 0x10a7208: ldr x8, [x8, #0x498]
// 0x10a720c: mov x1, xzr
// 0x10a7210: ldr x0, [x8]
// 0x10a7214: bl #0x1036634
// 0x10a7218: and w8, w0, #1
// 0x10a721c: strb w8, [x19, #0x8b]
// 0x10a7220: adrp x8, #0x1e8e000
// 0x10a7224: ldr x8, [x8, #0x3a0]
// 0x10a7228: mov x1, xzr
// 0x10a722c: ldr x0, [x8]
// 0x10a7230: bl #0x1036634
// 0x10a7234: and w8, w0, #1
// 0x10a7238: strb w8, [x19, #0x8c]
// 0x10a723c: adrp x20, #0x1e8c000
// 0x10a7240: ldr x20, [x20, #0x540]
// 0x10a7244: mov x1, xzr
// 0x10a7248: ldr x0, [x20]
// 0x10a724c: bl #0x1036390
// 0x10a7250: and w8, w0, #1
// 0x10a7254: strb w8, [x19, #0x8d]
// 0x10a7258: ldr x0, [x20]
// 0x10a725c: mov x1, xzr
// 0x10a7260: bl #0x1036634
// 0x10a7264: and w8, w0, #1
// 0x10a7268: strb w8, [x19, #0x8e]
// 0x10a726c: adrp x8, #0x1e8d000
// 0x10a7270: ldr x8, [x8, #0x620]
// 0x10a7274: mov x1, xzr
// 0x10a7278: ldr x0, [x8]
// 0x10a727c: bl #0x1036390
// 0x10a7280: and w8, w0, #1
// 0x10a7284: strb w8, [x19, #0x8f]
// 0x10a7288: adrp x8, #0x1e8e000
// 0x10a728c: ldr x8, [x8, #0x3b8]
// 0x10a7290: mov x1, xzr
// 0x10a7294: ldr x0, [x8]
// 0x10a7298: bl #0x1036390
// 0x10a729c: and w8, w0, #1
// 0x10a72a0: strb w8, [x19, #0x90]
// 0x10a72a4: adrp x8, #0x1e8e000
// 0x10a72a8: ldr x8, [x8, #0x3a8]
// 0x10a72ac: mov x1, xzr
// 0x10a72b0: ldr x0, [x8]
// 0x10a72b4: bl #0x1036390
// 0x10a72b8: and w8, w0, #1
// 0x10a72bc: strb w8, [x19, #0x91]
// 0x10a72c0: adrp x8, #0x1e8e000
// 0x10a72c4: ldr x8, [x8, #0x470]
// 0x10a72c8: mov x1, xzr
// 0x10a72cc: ldr x0, [x8]
// 0x10a72d0: bl #0x1036390
// 0x10a72d4: and w8, w0, #1
// 0x10a72d8: strb w8, [x19, #0x94]
// 0x10a72dc: adrp x8, #0x1e8e000
// 0x10a72e0: ldr x8, [x8, #0x3f0]
// 0x10a72e4: mov x1, xzr
// 0x10a72e8: ldr x0, [x8]
// 0x10a72ec: bl #0x1036390
// 0x10a72f0: and w8, w0, #1
// 0x10a72f4: strb w8, [x19, #0x95]
// 0x10a72f8: adrp x20, #0x1e8e000
// 0x10a72fc: ldr x20, [x20, #0x4d0]
// 0x10a7300: mov x1, xzr
// 0x10a7304: ldr x0, [x20]
// 0x10a7308: bl #0x1036390
// 0x10a730c: and w8, w0, #1
// 0x10a7310: strb w8, [x19, #0x96]
// 0x10a7314: ldr x0, [x20]
// 0x10a7318: mov x1, xzr
// 0x10a731c: bl #0x1036634
// 0x10a7320: and w8, w0, #1
// 0x10a7324: strb w8, [x19, #0x97]
// 0x10a7328: ldr x0, [x20]
// 0x10a732c: mov x1, xzr
// 0x10a7330: bl #0x10368e4
// 0x10a7334: and w8, w0, #1
// 0x10a7338: strb w8, [x19, #0x98]
// 0x10a733c: adrp x20, #0x1e8e000
// 0x10a7340: ldr x20, [x20, #0x3c0]
// 0x10a7344: mov x1, xzr
// 0x10a7348: ldr x0, [x20]
// 0x10a734c: bl #0x1036390
// 0x10a7350: and w8, w0, #1
// 0x10a7354: strb w8, [x19, #0x99]
// 0x10a7358: ldr x0, [x20]
// 0x10a735c: mov x1, xzr
// 0x10a7360: bl #0x1036634
// 0x10a7364: and w8, w0, #1
// 0x10a7368: strb w8, [x19, #0x9a]
// 0x10a736c: adrp x8, #0x1e8e000
// 0x10a7370: ldr x8, [x8, #0x3f8]
// 0x10a7374: mov x1, xzr
// 0x10a7378: ldr x0, [x8]
// 0x10a737c: bl #0x1036390
// 0x10a7380: and w8, w0, #1
// 0x10a7384: strb w8, [x19, #0x9b]
// 0x10a7388: adrp x8, #0x1e8e000
// 0x10a738c: ldr x8, [x8, #0x448]
// 0x10a7390: mov x1, xzr
// 0x10a7394: ldr x0, [x8]
// 0x10a7398: bl #0x1036634
// 0x10a739c: and w8, w0, #1
// 0x10a73a0: strb w8, [x19, #0x9d]
// 0x10a73a4: adrp x8, #0x1e8e000
// 0x10a73a8: ldr x8, [x8, #0x450]
// 0x10a73ac: mov x1, xzr
// 0x10a73b0: ldr x0, [x8]
// 0x10a73b4: bl #0x1036634
// 0x10a73b8: and w8, w0, #1
// 0x10a73bc: strb w8, [x19, #0x9e]
// 0x10a73c0: adrp x8, #0x1e8e000
// 0x10a73c4: ldr x8, [x8, #0x438]
// 0x10a73c8: mov x1, xzr
// 0x10a73cc: ldr x0, [x8]
// 0x10a73d0: bl #0x1036634
// 0x10a73d4: and w8, w0, #1
// 0x10a73d8: strb w8, [x19, #0x9f]
// 0x10a73dc: adrp x8, #0x1e8e000
// 0x10a73e0: ldr x8, [x8, #0x488]
// 0x10a73e4: mov x1, xzr
// 0x10a73e8: ldr x0, [x8]
// 0x10a73ec: bl #0x1036634
// 0x10a73f0: and w8, w0, #1
// 0x10a73f4: strb w8, [x19, #0xa0]
// 0x10a73f8: adrp x8, #0x1e8e000
// 0x10a73fc: ldr x8, [x8, #0x420]
// 0x10a7400: mov x1, xzr
// 0x10a7404: ldr x0, [x8]
// 0x10a7408: bl #0x1036634
// 0x10a740c: and w8, w0, #1
// 0x10a7410: strb w8, [x19, #0xa1]
// 0x10a7414: adrp x8, #0x1e8e000
// 0x10a7418: ldr x8, [x8, #0x4f8]
// 0x10a741c: mov x1, xzr
// 0x10a7420: ldr x0, [x8]
// 0x10a7424: bl #0x1036634
// 0x10a7428: and w8, w0, #1
// 0x10a742c: strb w8, [x19, #0x9c]
// 0x10a7430: adrp x8, #0x1e8e000
// 0x10a7434: ldr x8, [x8, #0x468]
// 0x10a7438: mov x1, xzr
// 0x10a743c: ldr x0, [x8]
// 0x10a7440: bl #0x1036634
// 0x10a7444: and w8, w0, #1
// 0x10a7448: strb w8, [x19, #0xa5]
// 0x10a744c: adrp x8, #0x1e8e000
// 0x10a7450: ldr x8, [x8, #0x480]
// 0x10a7454: mov x1, xzr
// 0x10a7458: ldr x0, [x8]
// 0x10a745c: bl #0x1036634
// 0x10a7460: and w8, w0, #1
// 0x10a7464: strb w8, [x19, #0xa6]
// 0x10a7468: adrp x8, #0x1e8e000
// 0x10a746c: ldr x8, [x8, #0x478]
// 0x10a7470: mov x1, xzr
// 0x10a7474: ldr x0, [x8]
// 0x10a7478: bl #0x1036634
// 0x10a747c: and w8, w0, #1
// 0x10a7480: strb w8, [x19, #0xa7]
// 0x10a7484: adrp x8, #0x1e8e000
// 0x10a7488: ldr x8, [x8, #0x430]
// 0x10a748c: mov x1, xzr
// 0x10a7490: ldr x0, [x8]
// 0x10a7494: bl #0x1036634
// 0x10a7498: and w8, w0, #1
// 0x10a749c: strb w8, [x19, #0xa8]
// 0x10a74a0: adrp x8, #0x1e8e000
// 0x10a74a4: ldr x8, [x8, #0x4b0]
// 0x10a74a8: mov x1, xzr
// 0x10a74ac: ldr x0, [x8]
// 0x10a74b0: bl #0x1036634
// 0x10a74b4: and w8, w0, #1
// 0x10a74b8: strb w8, [x19, #0xa9]
// 0x10a74bc: adrp x8, #0x1e8e000
// 0x10a74c0: ldr x8, [x8, #0x4c0]
// 0x10a74c4: mov x1, xzr
// 0x10a74c8: ldr x0, [x8]
// 0x10a74cc: bl #0x1036634
// 0x10a74d0: and w8, w0, #1
// 0x10a74d4: strb w8, [x19, #0xaa]
// 0x10a74d8: adrp x8, #0x1e8e000
// 0x10a74dc: ldr x8, [x8, #0x400]
// 0x10a74e0: mov x1, xzr
// 0x10a74e4: ldr x0, [x8]
// 0x10a74e8: bl #0x1036634
// 0x10a74ec: and w8, w0, #1
// 0x10a74f0: strb w8, [x19, #0xab]
// 0x10a74f4: adrp x8, #0x1e8e000
// 0x10a74f8: ldr x8, [x8, #0x4a8]
// 0x10a74fc: mov x1, xzr
// 0x10a7500: ldr x0, [x8]
// 0x10a7504: bl #0x1036634
// 0x10a7508: and w8, w0, #1
// 0x10a750c: strb w8, [x19, #0xac]
// 0x10a7510: adrp x8, #0x1e8e000
// 0x10a7514: ldr x8, [x8, #0x460]
// 0x10a7518: mov x1, xzr
// 0x10a751c: ldr x0, [x8]
// 0x10a7520: bl #0x1036634
// 0x10a7524: and w8, w0, #1
// 0x10a7528: strb w8, [x19, #0xad]
// 0x10a752c: adrp x8, #0x1e8e000
// 0x10a7530: ldr x8, [x8, #0x4d8]
// 0x10a7534: mov x1, xzr
// 0x10a7538: ldr x0, [x8]
// 0x10a753c: bl #0x1036634
// 0x10a7540: and w8, w0, #1
// 0x10a7544: strb w8, [x19, #0xae]
// 0x10a7548: adrp x8, #0x1e8e000
// 0x10a754c: ldr x8, [x8, #0x408]
// 0x10a7550: mov x1, xzr
// 0x10a7554: ldr x0, [x8]
// 0x10a7558: bl #0x1036634
// 0x10a755c: and w8, w0, #1
// 0x10a7560: strb w8, [x19, #0xaf]
// 0x10a7564: adrp x8, #0x1e8e000
// 0x10a7568: ldr x8, [x8, #0x490]
// 0x10a756c: mov x1, xzr
// 0x10a7570: ldr x0, [x8]
// 0x10a7574: bl #0x1036634
// 0x10a7578: and w8, w0, #1
// 0x10a757c: strb w8, [x19, #0xb0]
// 0x10a7580: adrp x8, #0x1e8e000
// 0x10a7584: ldr x8, [x8, #0x4c8]
// 0x10a7588: mov x1, xzr
// 0x10a758c: ldr x0, [x8]
// 0x10a7590: bl #0x1036634
// 0x10a7594: and w8, w0, #1
// 0x10a7598: strb w8, [x19, #0xb1]
// 0x10a759c: adrp x8, #0x1e8e000
// 0x10a75a0: ldr x8, [x8, #0x3d0]
// 0x10a75a4: mov x1, xzr
// 0x10a75a8: ldr x0, [x8]
// 0x10a75ac: bl #0x1036634
// 0x10a75b0: and w8, w0, #1
// 0x10a75b4: strb w8, [x19, #0xb2]
// 0x10a75b8: adrp x8, #0x1e8e000
// 0x10a75bc: ldr x8, [x8, #0x3e0]
// 0x10a75c0: mov x1, xzr
// 0x10a75c4: ldr x0, [x8]
// 0x10a75c8: bl #0x1036634
// 0x10a75cc: and w8, w0, #1
// 0x10a75d0: strb w8, [x19, #0xb3]
// 0x10a75d4: adrp x8, #0x1e8e000
// 0x10a75d8: ldr x8, [x8, #0x458]
// 0x10a75dc: mov x1, xzr
// 0x10a75e0: ldr x0, [x8]
// 0x10a75e4: bl #0x1036634
// 0x10a75e8: and w8, w0, #1
// 0x10a75ec: strb w8, [x19, #0xb4]
// 0x10a75f0: b #0x10a6864
// 0x10a75f4: bl #0xf7db74
```

## `InputControl.AccelerateInput` — RVA `0xca75f8`

- Decompiled symbol: `InputControl_AccelerateInput`
- Metadata signature: `private float AccelerateInput(float input) { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
int InputControl_AccelerateInput(void)
{
    return Time__get_smoothDeltaTime(0);
}
```

## `InputControl.OnOffMehtod` — RVA `0xca7640`

- Decompiled symbol: `InputControl_OnOffMehtod`
- Metadata signature: `public void OnOffMehtod() { }`
- Native interval: `116` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputControl_Recovered` matched 2 offsets against `InputControl` metadata (confidence 1.00).

```c
typedef struct InputControl_Recovered {
    char padding_0[104];
    unsigned long long Sourcebutton;
    char onoff;
} InputControl_Recovered;

void InputControl_OnOffMehtod(struct_0 *ptr)
{
    unsigned int v0;  // w9
    unsigned int v1;  // w8
    unsigned long long v2;  // x0

    v0 = ptr->field_70;
    v1 = v0 ^ 1;
    ptr->field_70 = v1;
    if (!v0)
    {
        v2 = ptr->field_68;
        if (!v2)
            sub_f7db74(v2);
        v2 = Selectable__get_image(v2, 0);
        if (!v2)
            sub_f7db74(v2);
        Image__set_overrideSprite();
        if (ptr->field_70)
            return;
    }
    else if (v1)
    {
        return;
    }
    v2 = ptr->field_68;
    if (!v2)
        sub_f7db74(v2);
    v2 = Selectable__get_image(v2, 0);
    if (v2)
    {
        Image__set_overrideSprite();
        return;
    }
    sub_f7db74(v2);
}
```

## `InputControl.ctor` — RVA `0xca76b4`

- Decompiled symbol: `InputControl_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[200];
    unsigned int field_c8;
} struct_0;

long long InputControl_ctor(struct_0 *ptr)
{
    ptr->field_c8 = 1045220557;
}
```
