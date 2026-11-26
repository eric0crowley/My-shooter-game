# Native pseudocode: InnerMap

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InnerMap.get_InnerMapRect` — RVA `0xc7a160`

- Decompiled symbol: `InnerMap_get_InnerMapRect`
- Metadata signature: `public RectTransform get_InnerMapRect() { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    long long field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efd060;
extern char g_1fab3cf;

long long InnerMap_get_InnerMapRect(struct_1 *ptr)
{
    long long v0;  // x0

    if (!(g_1fab3cf & 1))
    {
        sub_f7d92c(&g_1efd060);
        sub_f7d92c(&g_1ef0c58);
        g_1fab3cf = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Implicit(ptr->field_20, 0) & 1))
    {
        v0 = sub_1231bc8(ptr, g_1efd060);
        ptr->field_20 = v0;
        sub_f7d8d0((struct struct_1 *)&ptr->field_20, v0);
    }
    return ptr->field_20;
}
```

## `InnerMap.getMapRadius` — RVA `0xc7a204`

- Decompiled symbol: `InnerMap_getMapRadius`
- Metadata signature: `public float getMapRadius() { }`
- Native interval: `144` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x107a204: stp x30, x21, [sp, #-0x20]!
// 0x107a208: stp x20, x19, [sp, #0x10]
// 0x107a20c: adrp x19, #0x1fab000
// 0x107a210: adrp x21, #0x1e8d000
// 0x107a214: ldrb w8, [x19, #0x3d0]
// 0x107a218: ldr x21, [x21, #0xb90]
// 0x107a21c: mov x20, x0
// 0x107a220: tbnz w8, #0, #0x107a238
// 0x107a224: adrp x0, #0x1e8d000
// 0x107a228: ldr x0, [x0, #0xb90]
// 0x107a22c: bl #0xf7d92c
// 0x107a230: mov w8, #1
// 0x107a234: strb w8, [x19, #0x3d0]
// 0x107a238: ldr x0, [x21]
// 0x107a23c: mov w1, #4
// 0x107a240: bl #0xf7d9d4
// 0x107a244: mov x19, x0
// 0x107a248: mov x0, x20
// 0x107a24c: bl #0x107a160
// 0x107a250: cbz x0, #0x107a28c
// 0x107a254: mov x1, x19
// 0x107a258: mov x2, xzr
// 0x107a25c: bl #0x1b9cedc
// 0x107a260: cbz x19, #0x107a28c
// 0x107a264: ldr w8, [x19, #0x18]
// 0x107a268: cbz w8, #0x107a290
// 0x107a26c: ldp s0, s1, [x19, #0x20]
// 0x107a270: ldp x20, x19, [sp, #0x10]
// 0x107a274: fabs s0, s0
// 0x107a278: fabs s1, s1
// 0x107a27c: fcmp s0, s1
// 0x107a280: fcsel s0, s0, s1, mi
// 0x107a284: ldp x30, x21, [sp], #0x20
// 0x107a288: ret
// 0x107a28c: bl #0xf7db74
// 0x107a290: bl #0xf7db7c
```

## `InnerMap.ctor` — RVA `0xc7a294`

- Decompiled symbol: `InnerMap_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long InnerMap_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
