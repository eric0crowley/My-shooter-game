# Native pseudocode: CharacterAction

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `CharacterAction.OnEnable` — RVA `0xc65d20`

- Decompiled symbol: `CharacterAction_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[56];
    long long field_38;
} struct_0;

extern long long g_1efcf08;
extern char g_1fab2fc;

void CharacterAction_OnEnable(struct_0 *ptr)
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
    if (!(g_1fab2fc & 1))
    {
        sub_f7d92c(&g_1efcf08);
        g_1fab2fc = 1;
    }
    ptr->field_38 = sub_1231bc8(ptr, g_1efcf08);
    sub_f7d8d0();
    return;
}
```

## `CharacterAction.Update` — RVA `0xc65d78`

- Decompiled symbol: `CharacterAction_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[376];
    unsigned long long field_178;
} struct_2;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed00;
extern struct_1 *g_1ef0c58;
extern char g_1fab2fd;
extern char g_1fab2fe;

long long CharacterAction_Update(long long *ptr)
{
    long long v1;  // x0
    long long v2;  // x0
    unsigned long long v3;  // x21
    long long v4;  // x0
    long long v5;  // x0
    struct_2 **v6;  // x20
    long long v7;  // x0
    unsigned long long v0;  // [bp-0x18]

    if (!(g_1fab2fd & 1))
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab2fd = 1;
    }
    v1 = String__IsNullOrEmpty(ptr[5], 0);
    if (((char)v1 & 1))
        return v1;
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    v2 = CF2Input__GetButtonDown(ptr[5], 0);
    if (!((char)v2 & 1))
        return v2;
    v0 = v3;
    if (!(g_1fab2fe & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab2fe = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v4 = Object__op_Equality(ptr[4], 0, 0);
    if (((char)v4 & 1))
    {
        return v4;
    }
    else if (ptr[4])
    {
        v6 = LevelData__FindInteractiveObjectFor();
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v7 = Object__op_Inequality(v6, 0, 0);
        if (!((char)v7 & 1))
            return v7;
        v5 = String__IsNullOrEmpty(ptr[6], 0);
        if (!((char)v5 & 1))
        {
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v5 = Object__op_Inequality(ptr[7], 0, 0);
            if (((char)v5 & 1))
            {
                v5 = ptr[7];
                if (!v5)
                    sub_f7db74(v5);
                v5 = Animator__SetTrigger(v5, ptr[6], 0);
            }
        }
        if (!v6)
            sub_f7db74(v5);
        goto *(v6)->field_178;
    }
    else
    {
        sub_f7db74(ptr[4]);
    }
}
```

## `CharacterAction.PerformAction` — RVA `0xc65dfc`

- Decompiled symbol: `CharacterAction_PerformAction`
- Metadata signature: `public void PerformAction() { }`
- Native interval: `276` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x1065dfc: stp x30, x21, [sp, #-0x20]!
// 0x1065e00: stp x20, x19, [sp, #0x10]
// 0x1065e04: adrp x20, #0x1fab000
// 0x1065e08: adrp x21, #0x1e8c000
// 0x1065e0c: ldrb w8, [x20, #0x2fe]
// 0x1065e10: ldr x21, [x21, #0xd8]
// 0x1065e14: mov x19, x0
// 0x1065e18: tbnz w8, #0, #0x1065e30
// 0x1065e1c: adrp x0, #0x1e8c000
// 0x1065e20: ldr x0, [x0, #0xd8]
// 0x1065e24: bl #0xf7d92c
// 0x1065e28: mov w8, #1
// 0x1065e2c: strb w8, [x20, #0x2fe]
// 0x1065e30: ldr x0, [x21]
// 0x1065e34: ldr x20, [x19, #0x20]
// 0x1065e38: ldr w8, [x0, #0xe0]
// 0x1065e3c: cbnz w8, #0x1065e44
// 0x1065e40: bl #0xf7da5c
// 0x1065e44: mov x0, x20
// 0x1065e48: mov x1, xzr
// 0x1065e4c: mov x2, xzr
// 0x1065e50: bl #0x1b9568c
// 0x1065e54: tbnz w0, #0, #0x1065f00
// 0x1065e58: ldr x0, [x19, #0x20]
// 0x1065e5c: cbz x0, #0x1065f0c
// 0x1065e60: mov x1, x19
// 0x1065e64: bl #0x1065f10
// 0x1065e68: ldr x8, [x21]
// 0x1065e6c: mov x20, x0
// 0x1065e70: ldr w9, [x8, #0xe0]
// 0x1065e74: cbnz w9, #0x1065e80
// 0x1065e78: mov x0, x8
// 0x1065e7c: bl #0xf7da5c
// 0x1065e80: mov x0, x20
// 0x1065e84: mov x1, xzr
// 0x1065e88: mov x2, xzr
// 0x1065e8c: bl #0x1b94ac8
// 0x1065e90: tbz w0, #0, #0x1065f00
// 0x1065e94: ldr x0, [x19, #0x30]
// 0x1065e98: mov x1, xzr
// 0x1065e9c: bl #0x17f6920
// 0x1065ea0: tbnz w0, #0, #0x1065ee0
// 0x1065ea4: ldr x0, [x21]
// 0x1065ea8: ldr x21, [x19, #0x38]
// 0x1065eac: ldr w8, [x0, #0xe0]
// 0x1065eb0: cbnz w8, #0x1065eb8
// 0x1065eb4: bl #0xf7da5c
// 0x1065eb8: mov x0, x21
// 0x1065ebc: mov x1, xzr
// 0x1065ec0: mov x2, xzr
// 0x1065ec4: bl #0x1b94ac8
// 0x1065ec8: tbz w0, #0, #0x1065ee0
// 0x1065ecc: ldr x0, [x19, #0x38]
// 0x1065ed0: cbz x0, #0x1065f0c
// 0x1065ed4: ldr x1, [x19, #0x30]
// 0x1065ed8: mov x2, xzr
// 0x1065edc: bl #0x1b67884
// 0x1065ee0: cbz x20, #0x1065f0c
// 0x1065ee4: ldr x8, [x20]
// 0x1065ee8: mov x0, x20
// 0x1065eec: mov x1, x19
// 0x1065ef0: ldp x20, x19, [sp, #0x10]
// 0x1065ef4: ldp x3, x2, [x8, #0x178]
// 0x1065ef8: ldp x30, x21, [sp], #0x20
// 0x1065efc: br x3
// 0x1065f00: ldp x20, x19, [sp, #0x10]
// 0x1065f04: ldp x30, x21, [sp], #0x20
// 0x1065f08: ret
// 0x1065f0c: bl #0xf7db74
```

## `CharacterAction.ctor` — RVA `0xc660d0`

- Decompiled symbol: `CharacterAction_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
extern long long g_1f08380;
extern char g_1fab2ff;

void CharacterAction_ctor(long long *a0)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    long long ptr[7];  // x0
    long long p[7];  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab2ff & 1))
    {
        sub_f7d92c(&g_1f08380);
        g_1fab2ff = 1;
    }
    ptr = a0;
    ptr[5] = g_1f08380;
    sub_f7d8d0((long long [7])&ptr[5], g_1f08380);
    p = a0;
    p[6] = g_1f08380;
    sub_f7d8d0((long long [7])&p[6], g_1f08380);
    MonoBehaviour__ctor();
    return;
}
```
