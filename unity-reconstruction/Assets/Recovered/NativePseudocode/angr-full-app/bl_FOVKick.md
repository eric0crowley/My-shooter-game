# Native pseudocode: bl_FOVKick

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_FOVKick.Setup` — RVA `0xcdff2c`

- Decompiled symbol: `bl_FOVKick_Setup`
- Metadata signature: `public void Setup(Camera camera) { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
void bl_FOVKick_Setup(unsigned long a0, unsigned long a1)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    bl_FOVKick__CheckStatus();
}
```

## `bl_FOVKick.CheckStatus` — RVA `0xcdff74`

- Decompiled symbol: `bl_FOVKick_CheckStatus`
- Metadata signature: `private void CheckStatus(Camera camera) { }`
- Native interval: `224` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[40];
    unsigned long long field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eef838;
extern struct_0 *g_1ef0c58;
extern long long g_1f03f28;
extern long long g_1f0a270;
extern long long g_1f0a278;
extern char g_1fab632;

long long bl_FOVKick_CheckStatus(struct_1 *a0, long long a1)
{
    long long v0;  // x0
    long long v1;  // x19
    long long v2;  // x0

    if (!(g_1fab632 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab632 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(a1, 0, 0);
    if (!((char)v0 & 1))
    {
        if (a0->field_28)
            return v0;
        v1 = sub_f7db70(sub_f7d940(&g_1eef838));
        v2 = &g_1f0a270;
    }
    else
    {
        v1 = sub_f7db70(sub_f7d940(&g_1eef838));
        v2 = &g_1f0a278;
    }
    Exception__ctor(v1, sub_f7d940(v2), 0);
    sub_f7da4c(v1, sub_f7d940(&g_1f03f28));
}
```

## `bl_FOVKick.ChangeCamera` — RVA `0xce0054`

- Decompiled symbol: `bl_FOVKick_ChangeCamera`
- Metadata signature: `public void ChangeCamera(Camera camera) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

long long bl_FOVKick_ChangeCamera(struct_0 *ptr, unsigned long a1)
{
    long long v0;  // x0

    ptr->field_10 = a1;
    v0 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `bl_FOVKick.FOVKickUp` — RVA `0xce005c`

- Decompiled symbol: `bl_FOVKick_FOVKickUp`
- Metadata signature: `public IEnumerator FOVKickUp() { }`
- Native interval: `108` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_FOVKick_Recovered` matched 2 offsets against `bl_FOVKick` metadata (confidence 1.00).

```c
typedef struct bl_FOVKick_Recovered {
    char padding_0[16];
    unsigned int Camera;
    char padding_14[12];
    long long TimeToIncrease;
} bl_FOVKick_Recovered;

extern long long g_1ef4140;
extern char g_1fab633;

struct_0 * bl_FOVKick_FOVKickUp(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab633 & 1))
    {
        sub_f7d92c(&g_1ef4140);
        g_1fab633 = 1;
    }
    v0 = sub_f7db70(g_1ef4140);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct bl_FOVKick_Recovered *)&ptr->field_20, a0);
    return ptr;
}
```

## `bl_FOVKick.<FOVKickUp>d__9.ctor` — RVA `0xce00c8`

- Decompiled symbol: `bl_FOVKick_FOVKickUp_d__9_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void bl_FOVKick_FOVKickUp_d__9_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `bl_FOVKick.FOVKickDown` — RVA `0xce00f0`

- Decompiled symbol: `bl_FOVKick_FOVKickDown`
- Metadata signature: `public IEnumerator FOVKickDown() { }`
- Native interval: `108` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_FOVKick_Recovered` matched 2 offsets against `bl_FOVKick` metadata (confidence 1.00).

```c
typedef struct bl_FOVKick_Recovered {
    char padding_0[16];
    unsigned int Camera;
    char padding_14[12];
    long long TimeToIncrease;
} bl_FOVKick_Recovered;

extern long long g_1ef4138;
extern char g_1fab634;

struct_0 * bl_FOVKick_FOVKickDown(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab634 & 1))
    {
        sub_f7d92c(&g_1ef4138);
        g_1fab634 = 1;
    }
    v0 = sub_f7db70(g_1ef4138);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct bl_FOVKick_Recovered *)&ptr->field_20, a0);
    return ptr;
}
```

## `bl_FOVKick.<FOVKickDown>d__10.ctor` — RVA `0xce015c`

- Decompiled symbol: `bl_FOVKick_FOVKickDown_d__10_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void bl_FOVKick_FOVKickDown_d__10_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `bl_FOVKick.ctor` — RVA `0xce0184`

- Decompiled symbol: `bl_FOVKick_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `28` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_FOVKick_Recovered` matched 2 offsets against `bl_FOVKick` metadata (confidence 1.00).

```c
typedef struct bl_FOVKick_Recovered {
    char padding_0[28];
    unsigned long long FOVIncrease;
    unsigned int TimeToDecrease;
} bl_FOVKick_Recovered;

long long bl_FOVKick_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    *((unsigned int *)((char *)&ptr->field_1c + 4)) = 0x3f800000;
    *((unsigned long long *)&(&ptr->padding_0)[1]) = 0x3f80000040400000;
    v0 = Object__ctor();
    return Object__ctor();
}
```

## `bl_FOVKick.<FOVKickDown>d__10.Dispose` — RVA `0xce01a0`

- Decompiled symbol: `bl_FOVKick_FOVKickDown_d__10_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long bl_FOVKick_FOVKickDown_d__10_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `bl_FOVKick.<FOVKickDown>d__10.MoveNext` — RVA `0xce01a4`

- Decompiled symbol: `bl_FOVKick_FOVKickDown_d__10_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `324` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10e01a4: str d8, [sp, #-0x30]!
// 0x10e01a8: stp x30, x21, [sp, #0x10]
// 0x10e01ac: stp x20, x19, [sp, #0x20]
// 0x10e01b0: adrp x20, #0x1fab000
// 0x10e01b4: ldrb w8, [x20, #0x635]
// 0x10e01b8: mov x19, x0
// 0x10e01bc: tbnz w8, #0, #0x10e01d4
// 0x10e01c0: adrp x0, #0x1e8d000
// 0x10e01c4: ldr x0, [x0, #0xa80]
// 0x10e01c8: bl #0xf7d92c
// 0x10e01cc: mov w8, #1
// 0x10e01d0: strb w8, [x20, #0x635]
// 0x10e01d4: ldr w8, [x19, #0x10]
// 0x10e01d8: ldr x21, [x19, #0x20]
// 0x10e01dc: cmp w8, #1
// 0x10e01e0: b.eq #0x10e021c
// 0x10e01e4: cbnz w8, #0x10e02d0
// 0x10e01e8: mov w8, #-1
// 0x10e01ec: str w8, [x19, #0x10]
// 0x10e01f0: cbz x21, #0x10e02e4
// 0x10e01f4: ldr x0, [x21, #0x10]
// 0x10e01f8: cbz x0, #0x10e02e4
// 0x10e01fc: mov x1, xzr
// 0x10e0200: bl #0x1b6e71c
// 0x10e0204: ldp s1, s2, [x21, #0x18]
// 0x10e0208: fsub s0, s0, s1
// 0x10e020c: fdiv s0, s0, s2
// 0x10e0210: fabs s0, s0
// 0x10e0214: str s0, [x19, #0x28]
// 0x10e0218: b #0x10e022c
// 0x10e021c: mov w8, #-1
// 0x10e0220: str w8, [x19, #0x10]
// 0x10e0224: cbz x21, #0x10e02e4
// 0x10e0228: ldr s0, [x19, #0x28]
// 0x10e022c: ldr x20, [x21, #0x10]
// 0x10e0230: ldr s8, [x21, #0x18]
// 0x10e0234: fcmp s0, #0.0
// 0x10e0238: b.le #0x10e02bc
// 0x10e023c: ldr x0, [x21, #0x28]
// 0x10e0240: cbz x0, #0x10e02e4
// 0x10e0244: ldr s1, [x21, #0x24]
// 0x10e0248: mov x1, xzr
// 0x10e024c: fdiv s0, s0, s1
// 0x10e0250: bl #0x1b6cda8
// 0x10e0254: cbz x20, #0x10e02e4
// 0x10e0258: ldr s1, [x21, #0x1c]
// 0x10e025c: mov x0, x20
// 0x10e0260: mov x1, xzr
// 0x10e0264: fmul s0, s0, s1
// 0x10e0268: fadd s0, s8, s0
// 0x10e026c: bl #0x1b6e758
// 0x10e0270: ldr s8, [x19, #0x28]
// 0x10e0274: mov x0, xzr
// 0x10e0278: bl #0x1b89b60
// 0x10e027c: fsub s0, s8, s0
// 0x10e0280: str s0, [x19, #0x28]
// 0x10e0284: adrp x8, #0x1e8d000
// 0x10e0288: ldr x8, [x8, #0xa80]
// 0x10e028c: ldr x0, [x8]
// 0x10e0290: bl #0xf7db70
// 0x10e0294: mov x1, xzr
// 0x10e0298: mov x20, x0
// 0x10e029c: bl #0x1b99af0
// 0x10e02a0: str x20, [x19, #0x18]!
// 0x10e02a4: mov x0, x19
// 0x10e02a8: mov x1, x20
// 0x10e02ac: bl #0xf7d8d0
// 0x10e02b0: mov w0, #1
// 0x10e02b4: stur w0, [x19, #-8]
// 0x10e02b8: b #0x10e02d4
// 0x10e02bc: cbz x20, #0x10e02e4
// 0x10e02c0: mov x0, x20
// 0x10e02c4: mov v0.16b, v8.16b
// 0x10e02c8: mov x1, xzr
// 0x10e02cc: bl #0x1b6e758
// 0x10e02d0: mov w0, wzr
// 0x10e02d4: ldp x20, x19, [sp, #0x20]
// 0x10e02d8: ldp x30, x21, [sp, #0x10]
// 0x10e02dc: ldr d8, [sp], #0x30
// 0x10e02e0: ret
// 0x10e02e4: bl #0xf7db74
```

## `bl_FOVKick.<FOVKickDown>d__10.get_Current` — RVA `0xce02e8`

- Decompiled symbol: `bl_FOVKick_FOVKickDown_d__10_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_FOVKick_FOVKickDown_d__10_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_FOVKick.<FOVKickDown>d__10.Reset` — RVA `0xce02f0`

- Decompiled symbol: `bl_FOVKick_FOVKickDown_d__10_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f054b8;

void bl_FOVKick_FOVKickDown_d__10_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f054b8));
}
```

## `bl_FOVKick.<FOVKickDown>d__10.get_Current` — RVA `0xce0328`

- Decompiled symbol: `bl_FOVKick_FOVKickDown_d__10_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_FOVKick_FOVKickDown_d__10_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_FOVKick.<FOVKickUp>d__9.Dispose` — RVA `0xce0330`

- Decompiled symbol: `bl_FOVKick_FOVKickUp_d__9_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long bl_FOVKick_FOVKickUp_d__9_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `bl_FOVKick.<FOVKickUp>d__9.MoveNext` — RVA `0xce0334`

- Decompiled symbol: `bl_FOVKick_FOVKickUp_d__9_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `304` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10e0334: str d8, [sp, #-0x30]!
// 0x10e0338: stp x30, x21, [sp, #0x10]
// 0x10e033c: stp x20, x19, [sp, #0x20]
// 0x10e0340: adrp x20, #0x1fab000
// 0x10e0344: ldrb w8, [x20, #0x636]
// 0x10e0348: mov x19, x0
// 0x10e034c: tbnz w8, #0, #0x10e0364
// 0x10e0350: adrp x0, #0x1e8d000
// 0x10e0354: ldr x0, [x0, #0xa80]
// 0x10e0358: bl #0xf7d92c
// 0x10e035c: mov w8, #1
// 0x10e0360: strb w8, [x20, #0x636]
// 0x10e0364: ldr w8, [x19, #0x10]
// 0x10e0368: ldr x21, [x19, #0x20]
// 0x10e036c: cmp w8, #1
// 0x10e0370: b.eq #0x10e03ac
// 0x10e0374: cbnz w8, #0x10e044c
// 0x10e0378: mov w8, #-1
// 0x10e037c: str w8, [x19, #0x10]
// 0x10e0380: cbz x21, #0x10e0460
// 0x10e0384: ldr x0, [x21, #0x10]
// 0x10e0388: cbz x0, #0x10e0460
// 0x10e038c: mov x1, xzr
// 0x10e0390: bl #0x1b6e71c
// 0x10e0394: ldp s1, s2, [x21, #0x18]
// 0x10e0398: fsub s0, s0, s1
// 0x10e039c: fdiv s0, s0, s2
// 0x10e03a0: fabs s0, s0
// 0x10e03a4: str s0, [x19, #0x28]
// 0x10e03a8: b #0x10e03bc
// 0x10e03ac: mov w8, #-1
// 0x10e03b0: str w8, [x19, #0x10]
// 0x10e03b4: cbz x21, #0x10e0460
// 0x10e03b8: ldr s0, [x19, #0x28]
// 0x10e03bc: ldr s1, [x21, #0x20]
// 0x10e03c0: fcmp s0, s1
// 0x10e03c4: b.pl #0x10e044c
// 0x10e03c8: ldr x0, [x21, #0x28]
// 0x10e03cc: cbz x0, #0x10e0460
// 0x10e03d0: ldr x20, [x21, #0x10]
// 0x10e03d4: ldr s8, [x21, #0x18]
// 0x10e03d8: fdiv s0, s0, s1
// 0x10e03dc: mov x1, xzr
// 0x10e03e0: bl #0x1b6cda8
// 0x10e03e4: cbz x20, #0x10e0460
// 0x10e03e8: ldr s1, [x21, #0x1c]
// 0x10e03ec: mov x0, x20
// 0x10e03f0: mov x1, xzr
// 0x10e03f4: fmul s0, s0, s1
// 0x10e03f8: fadd s0, s8, s0
// 0x10e03fc: bl #0x1b6e758
// 0x10e0400: ldr s8, [x19, #0x28]
// 0x10e0404: mov x0, xzr
// 0x10e0408: bl #0x1b89b60
// 0x10e040c: fadd s0, s8, s0
// 0x10e0410: str s0, [x19, #0x28]
// 0x10e0414: adrp x8, #0x1e8d000
// 0x10e0418: ldr x8, [x8, #0xa80]
// 0x10e041c: ldr x0, [x8]
// 0x10e0420: bl #0xf7db70
// 0x10e0424: mov x1, xzr
// 0x10e0428: mov x20, x0
// 0x10e042c: bl #0x1b99af0
// 0x10e0430: str x20, [x19, #0x18]!
// 0x10e0434: mov x0, x19
// 0x10e0438: mov x1, x20
// 0x10e043c: bl #0xf7d8d0
// 0x10e0440: mov w0, #1
// 0x10e0444: stur w0, [x19, #-8]
// 0x10e0448: b #0x10e0450
// 0x10e044c: mov w0, wzr
// 0x10e0450: ldp x20, x19, [sp, #0x20]
// 0x10e0454: ldp x30, x21, [sp, #0x10]
// 0x10e0458: ldr d8, [sp], #0x30
// 0x10e045c: ret
// 0x10e0460: bl #0xf7db74
```

## `bl_FOVKick.<FOVKickUp>d__9.get_Current` — RVA `0xce0464`

- Decompiled symbol: `bl_FOVKick_FOVKickUp_d__9_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_FOVKick_FOVKickUp_d__9_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_FOVKick.<FOVKickUp>d__9.Reset` — RVA `0xce046c`

- Decompiled symbol: `bl_FOVKick_FOVKickUp_d__9_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f054c0;

void bl_FOVKick_FOVKickUp_d__9_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f054c0));
}
```

## `bl_FOVKick.<FOVKickUp>d__9.get_Current` — RVA `0xce04a4`

- Decompiled symbol: `bl_FOVKick_FOVKickUp_d__9_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_FOVKick_FOVKickUp_d__9_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
