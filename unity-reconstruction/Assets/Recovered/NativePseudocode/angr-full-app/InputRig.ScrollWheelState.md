# Native pseudocode: InputRig.ScrollWheelState

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InputRig.ScrollWheelState.ctor` — RVA `0xc42fa0`

- Decompiled symbol: `InputRig_ScrollWheelState_ctor`
- Metadata signature: `public void .ctor(InputRig rig) { }`
- Native interval: `244` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

extern long long g_1f0c398;
extern long long g_1f0c3a0;
extern char g_1fab20c;

long long InputRig_ScrollWheelState_ctor(struct_0 *ptr, long long a1)
{
    unsigned long long v7;  // x30
    unsigned long long v8;  // x24
    unsigned long long v9;  // x23
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    long long v14;  // x0
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]
    unsigned long long v5;  // [bp-0x10]
    unsigned long long v6;  // [bp-0x8]

    v0 = v7;
    v1 = v8;
    v2 = v9;
    v3 = v10;
    v4 = v11;
    v5 = v12;
    v6 = v13;
    if (!(g_1fab20c & 1))
    {
        sub_f7d92c("5Q");
        sub_f7d92c(&g_1f0c3a0);
        sub_f7d92c(&g_1f0c398);
        g_1fab20c = 1;
    }
    Object__ctor(ptr, 0);
    ptr->field_10 = a1;
    sub_f7d8d0((struct struct_0 *)&ptr->field_10, a1);
    v14 = sub_f7db70(g_1ef1560);
    ScrollDeltaBinding__ctor(v14, g_1f0c398, 1, 0, 0); /* do not return */
}
```

## `InputRig.ScrollWheelState.Reset` — RVA `0xc43094`

- Decompiled symbol: `InputRig_ScrollWheelState_Reset`
- Metadata signature: `public void Reset() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long InputRig_ScrollWheelState_Reset(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `InputRig.ScrollWheelState.Update` — RVA `0xc43098`

- Decompiled symbol: `InputRig_ScrollWheelState_Update`
- Metadata signature: `public void Update() { }`
- Native interval: `484` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x1043098: sub sp, sp, #0x50
// 0x104309c: str d10, [sp, #0x10]
// 0x10430a0: stp d9, d8, [sp, #0x18]
// 0x10430a4: str x30, [sp, #0x28]
// 0x10430a8: stp x22, x21, [sp, #0x30]
// 0x10430ac: stp x20, x19, [sp, #0x40]
// 0x10430b0: mov x19, x0
// 0x10430b4: mov x0, xzr
// 0x10430b8: bl #0x1bc7a14
// 0x10430bc: adrp x21, #0x1fab000
// 0x10430c0: ldrb w8, [x21, #0x242]
// 0x10430c4: ldr x20, [x19, #0x18]
// 0x10430c8: mov v9.16b, v0.16b
// 0x10430cc: mov v8.16b, v1.16b
// 0x10430d0: cbnz w8, #0x10430e8
// 0x10430d4: adrp x0, #0x1e8c000
// 0x10430d8: ldr x0, [x0, #0xa60]
// 0x10430dc: bl #0xf7d92c
// 0x10430e0: mov w8, #1
// 0x10430e4: strb w8, [x21, #0x242]
// 0x10430e8: adrp x22, #0x1e8c000
// 0x10430ec: ldr x22, [x22, #0xa60]
// 0x10430f0: ldr x0, [x22]
// 0x10430f4: ldr w8, [x0, #0xe0]
// 0x10430f8: cbnz w8, #0x1043100
// 0x10430fc: bl #0xf7da5c
// 0x1043100: fcvt d10, s9
// 0x1043104: add x0, sp, #8
// 0x1043108: mov v0.16b, v10.16b
// 0x104310c: bl #0x1db0c60
// 0x1043110: fcmp s9, #0.0
// 0x1043114: b.ge #0x1043130
// 0x1043118: fmov d1, #-0.50000000
// 0x104311c: fcmp d0, d1
// 0x1043120: b.ne #0x1043158
// 0x1043124: ldr d0, [sp, #8]
// 0x1043128: fmov d1, #-1.00000000
// 0x104312c: b #0x1043144
// 0x1043130: fmov d1, #0.50000000
// 0x1043134: fcmp d0, d1
// 0x1043138: b.ne #0x1043164
// 0x104313c: ldr d0, [sp, #8]
// 0x1043140: fmov d1, #1.00000000
// 0x1043144: fcvtzs x8, d0
// 0x1043148: fadd d1, d0, d1
// 0x104314c: tst x8, #1
// 0x1043150: fcsel d0, d0, d1, eq
// 0x1043154: b #0x104316c
// 0x1043158: fadd d0, d10, d1
// 0x104315c: frintp d0, d0
// 0x1043160: b #0x104316c
// 0x1043164: fadd d0, d10, d1
// 0x1043168: frintm d0, d0
// 0x104316c: cbz x20, #0x1043278
// 0x1043170: ldr x2, [x19, #0x10]
// 0x1043174: mov x8, #0x7ff0000000000000
// 0x1043178: fmov d1, x8
// 0x104317c: fcvtzs w9, d0
// 0x1043180: fcmp d0, d1
// 0x1043184: mov w8, #-0x80000000
// 0x1043188: csel w1, w8, w9, eq
// 0x104318c: mov x0, x20
// 0x1043190: mov x3, xzr
// 0x1043194: bl #0x105e7e8
// 0x1043198: ldrb w8, [x21, #0x242]
// 0x104319c: ldr x20, [x19, #0x20]
// 0x10431a0: cbnz w8, #0x10431b8
// 0x10431a4: adrp x0, #0x1e8c000
// 0x10431a8: ldr x0, [x0, #0xa60]
// 0x10431ac: bl #0xf7d92c
// 0x10431b0: mov w8, #1
// 0x10431b4: strb w8, [x21, #0x242]
// 0x10431b8: ldr x0, [x22]
// 0x10431bc: ldr w8, [x0, #0xe0]
// 0x10431c0: cbnz w8, #0x10431c8
// 0x10431c4: bl #0xf7da5c
// 0x10431c8: fcvt d9, s8
// 0x10431cc: add x0, sp, #8
// 0x10431d0: mov v0.16b, v9.16b
// 0x10431d4: bl #0x1db0c60
// 0x10431d8: fcmp s8, #0.0
// 0x10431dc: b.ge #0x10431f8
// 0x10431e0: fmov d1, #-0.50000000
// 0x10431e4: fcmp d0, d1
// 0x10431e8: b.ne #0x1043220
// 0x10431ec: ldr d0, [sp, #8]
// 0x10431f0: fmov d1, #-1.00000000
// 0x10431f4: b #0x104320c
// 0x10431f8: fmov d1, #0.50000000
// 0x10431fc: fcmp d0, d1
// 0x1043200: b.ne #0x104322c
// 0x1043204: ldr d0, [sp, #8]
// 0x1043208: fmov d1, #1.00000000
// 0x104320c: fcvtzs x8, d0
// 0x1043210: fadd d1, d0, d1
// 0x1043214: tst x8, #1
// 0x1043218: fcsel d0, d0, d1, eq
// 0x104321c: b #0x1043234
// 0x1043220: fadd d0, d9, d1
// 0x1043224: frintp d0, d0
// 0x1043228: b #0x1043234
// 0x104322c: fadd d0, d9, d1
// 0x1043230: frintm d0, d0
// 0x1043234: cbz x20, #0x1043278
// 0x1043238: ldr x2, [x19, #0x10]
// 0x104323c: mov x8, #0x7ff0000000000000
// 0x1043240: mov x0, x20
// 0x1043244: ldp x20, x19, [sp, #0x40]
// 0x1043248: ldp x22, x21, [sp, #0x30]
// 0x104324c: ldr x30, [sp, #0x28]
// 0x1043250: ldp d9, d8, [sp, #0x18]
// 0x1043254: ldr d10, [sp, #0x10]
// 0x1043258: fmov d1, x8
// 0x104325c: fcvtzs w9, d0
// 0x1043260: fcmp d0, d1
// 0x1043264: mov w8, #-0x80000000
// 0x1043268: csel w1, w8, w9, eq
// 0x104326c: mov x3, xzr
// 0x1043270: add sp, sp, #0x50
// 0x1043274: b #0x105e7e8
// 0x1043278: bl #0xf7db74
```

## `InputRig.ScrollWheelState.GetDelta` — RVA `0xc4327c`

- Decompiled symbol: `InputRig_ScrollWheelState_GetDelta`
- Metadata signature: `public Vector2 GetDelta() { }`
- Native interval: `220` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_ScrollWheelState_Recovered` matched 3 offsets against `InputRig.ScrollWheelState` metadata (confidence 1.00).

```c
typedef struct struct_6 {
    char padding_0[16];
    char field_10;
} struct_6;

typedef struct InputRig_ScrollWheelState_Recovered {
    char padding_0[16];
    long long rig;
    struct struct_2 *horzScrollDeltaBinding;
    struct struct_4 *vertScrollDeltaBinding;
} InputRig_ScrollWheelState_Recovered;

typedef struct struct_2 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    char field_10;
} struct_1;

typedef struct struct_4 {
    char padding_0[32];
    struct struct_3 *field_20;
} struct_4;

typedef struct struct_3 {
    char padding_0[16];
    char field_10;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab20d;

struct_6 * InputRig_ScrollWheelState_GetDelta(struct_5 *idx)
{
    struct_6 *v0;  // x0
    struct_3 *v1;  // x0
    unsigned long long v2;  // x0

    if (!(g_1fab20d & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab20d = 1;
    }
    Input__get_mouseScrollDelta(0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(idx->field_10, 0, 0);
    if (((char)v0 & 1))
        return v0;
    if (idx->field_18 && idx->field_18->field_20)
    {
        if (idx->field_18->field_20->field_10)
            AxisBinding__GetAxis();
        if (idx->field_20)
        {
            v1 = idx->field_20->field_20;
            if (v1)
            {
                if (v1->field_10)
                {
                    v2 = AxisBinding__GetAxis();
                    return AxisBinding__GetAxis();
                }
                return v1;
            }
        }
    }
    sub_f7db74();
}
```

## `InputRig.ScrollWheelState.IsBoundToAxis` — RVA `0xc43358`

- Decompiled symbol: `InputRig_ScrollWheelState_IsBoundToAxis`
- Metadata signature: `public bool IsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

long long InputRig_ScrollWheelState_IsBoundToAxis(struct_0 *a0, unsigned long a1, unsigned long a2)
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
    if (a0->field_18)
        InputBindingBase__IsBoundToAxis(a0->field_18); /* do not return */
    sub_f7db74(0);
}
```

## `InputRig.ScrollWheelState.IsBoundToKey` — RVA `0xc433b4`

- Decompiled symbol: `InputRig_ScrollWheelState_IsBoundToKey`
- Metadata signature: `public bool IsBoundToKey(KeyCode key, InputRig rig) { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    long long field_18;
} struct_0;

long long InputRig_ScrollWheelState_IsBoundToKey(struct_0 *a0, unsigned long a1, unsigned long a2)
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
    if (a0->field_18)
        InputBindingBase__IsBoundToKey(a0->field_18); /* do not return */
    sub_f7db74(0);
}
```

## `InputRig.ScrollWheelState.IsEmulatingTouches` — RVA `0xc43410`

- Decompiled symbol: `InputRig_ScrollWheelState_IsEmulatingTouches`
- Metadata signature: `public bool IsEmulatingTouches() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int InputRig_ScrollWheelState_IsEmulatingTouches(void)
{
    return 0;
}
```

## `InputRig.ScrollWheelState.IsEmulatingMousePosition` — RVA `0xc43418`

- Decompiled symbol: `InputRig_ScrollWheelState_IsEmulatingMousePosition`
- Metadata signature: `public bool IsEmulatingMousePosition() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int InputRig_ScrollWheelState_IsEmulatingMousePosition(void)
{
    return 0;
}
```

## `InputRig.ScrollWheelState.GetSubBindingDescriptions` — RVA `0xc43420`

- Decompiled symbol: `InputRig_ScrollWheelState_GetSubBindingDescriptions`
- Metadata signature: `public void GetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1f0ab40;
extern long long g_1f0f9c0;
extern char g_1fab20e;

long long InputRig_ScrollWheelState_GetSubBindingDescriptions(struct_0 *a0, long long a1, long long a2, long long a3)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]
    unsigned long long v5;  // [bp-0x8]

    v0 = v6;
    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    if (!(g_1fab20e & 1))
    {
        sub_f7d92c(&g_1f0f9c0);
        sub_f7d92c(&g_1f0ab40);
        g_1fab20e = 1;
    }
    if (a1)
        BindingDescriptionList__Add(a1, a0->field_20, g_1f0f9c0, a3, a2, 0); /* do not return */
    sub_f7db74();
}
```
