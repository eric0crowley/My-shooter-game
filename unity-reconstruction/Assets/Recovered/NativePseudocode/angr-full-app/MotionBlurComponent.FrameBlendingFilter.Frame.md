# Native pseudocode: MotionBlurComponent.FrameBlendingFilter.Frame

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MotionBlurComponent.FrameBlendingFilter.Frame.Release` — RVA `0xcd75b0`

- Decompiled symbol: `MotionBlurComponent_FrameBlendingFilter_Frame_Release`
- Metadata signature: `public void Release() { }`
- Native interval: `208` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab5ed;

void MotionBlurComponent_FrameBlendingFilter_Frame_Release(long long *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
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
    if (!(g_1fab5ed & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab5ed = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(*(ptr), 0, 0) & 1))
        RenderTexture__ReleaseTemporary(*(ptr), 0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(ptr[1], 0, 0) & 1))
        RenderTexture__ReleaseTemporary(ptr[1], 0);
    *(ptr) = 0;
    sub_f7d8d0(ptr, 0);
    ptr[1] = 0;
    sub_f7d8d0();
    return;
}
```

## `MotionBlurComponent.FrameBlendingFilter.Frame.MakeRecord` — RVA `0xcd7680`

- Decompiled symbol: `MotionBlurComponent_FrameBlendingFilter_Frame_MakeRecord`
- Metadata signature: `public void MakeRecord(CommandBuffer cb, RenderTargetIdentifier source, int width, int height, Material material) { }`
- Native interval: `752` bytes
- Result: `pseudocode`

```c
extern long long g_1eee300;
extern long long g_1ef3510;
extern char g_1fab5ee;

void MotionBlurComponent_FrameBlendingFilter_Frame_MakeRecord(long long *a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5)
{
    unsigned long long v10;  // x30
    unsigned long long v11;  // x25
    unsigned long long v12;  // x24
    unsigned long long v13;  // x23
    unsigned long long v14;  // x22
    unsigned long long v15;  // x21
    unsigned long long v16;  // x20
    unsigned long long v17;  // x19
    char *v0;  // [bp-0x50]
    unsigned long long v1;  // [bp-0x40]
    unsigned long long v2;  // [bp-0x38]
    unsigned long long v3;  // [bp-0x30]
    unsigned long long v4;  // [bp-0x28]
    unsigned long long v5;  // [bp-0x20]
    unsigned long long v6;  // [bp-0x18]
    unsigned long long v7;  // [bp-0x10]
    unsigned long long v8;  // [bp-0x8]
    char v9;  // [bp+0x0]

    v0 = &v9;
    v1 = v10;
    v2 = v11;
    v3 = v12;
    v4 = v13;
    v5 = v14;
    v6 = v15;
    v7 = v16;
    v8 = v17;
    if (!(g_1fab5ee & 1))
    {
        sub_f7d92c(&g_1eee300);
        sub_f7d92c(&g_1ef3510);
        g_1fab5ee = 1;
    }
    MotionBlurComponent_FrameBlendingFilter_Frame__Release(a0); /* do not return */
}
```

## `MotionBlurComponent.FrameBlendingFilter.Frame.MakeRecordRaw` — RVA `0xcd7970`

- Decompiled symbol: `MotionBlurComponent_FrameBlendingFilter_Frame_MakeRecordRaw`
- Metadata signature: `public void MakeRecordRaw(CommandBuffer cb, RenderTargetIdentifier source, int width, int height, RenderTextureFormat format) { }`
- Native interval: `368` bytes
- Result: `pseudocode`

```c
extern long long g_1ef3510;
extern char g_1fab5ef;

void MotionBlurComponent_FrameBlendingFilter_Frame_MakeRecordRaw(long long *a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5)
{
    unsigned long long v10;  // x30
    unsigned long long v11;  // x25
    unsigned long long v12;  // x24
    unsigned long long v13;  // x23
    unsigned long long v14;  // x22
    unsigned long long v15;  // x21
    unsigned long long v16;  // x20
    unsigned long long v17;  // x19
    char *v0;  // [bp-0x50]
    unsigned long long v1;  // [bp-0x40]
    unsigned long long v2;  // [bp-0x38]
    unsigned long long v3;  // [bp-0x30]
    unsigned long long v4;  // [bp-0x28]
    unsigned long long v5;  // [bp-0x20]
    unsigned long long v6;  // [bp-0x18]
    unsigned long long v7;  // [bp-0x10]
    unsigned long long v8;  // [bp-0x8]
    char v9;  // [bp+0x0]

    v0 = &v9;
    v1 = v10;
    v2 = v11;
    v3 = v12;
    v4 = v13;
    v5 = v14;
    v6 = v15;
    v7 = v16;
    v8 = v17;
    if (!(g_1fab5ef & 1))
    {
        sub_f7d92c(&g_1ef3510);
        g_1fab5ef = 1;
    }
    MotionBlurComponent_FrameBlendingFilter_Frame__Release(a0); /* do not return */
}
```

## `MotionBlurComponent.FrameBlendingFilter.Frame.CalculateWeight` — RVA `0xcd7b44`

- Decompiled symbol: `MotionBlurComponent_FrameBlendingFilter_Frame_CalculateWeight`
- Metadata signature: `public float CalculateWeight(float strength, float currentTime) { }`
- Native interval: `232` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10d7b44: str d10, [sp, #-0x30]!
// 0x10d7b48: stp d9, d8, [sp, #8]
// 0x10d7b4c: str x30, [sp, #0x18]
// 0x10d7b50: stp x20, x19, [sp, #0x20]
// 0x10d7b54: adrp x20, #0x1fab000
// 0x10d7b58: ldrb w8, [x20, #0x2ca]
// 0x10d7b5c: ldr s10, [x0, #0x10]
// 0x10d7b60: mov v8.16b, v1.16b
// 0x10d7b64: mov x19, x0
// 0x10d7b68: mov v9.16b, v0.16b
// 0x10d7b6c: cbnz w8, #0x10d7b84
// 0x10d7b70: adrp x0, #0x1e8c000
// 0x10d7b74: ldr x0, [x0, #0xd80]
// 0x10d7b78: bl #0xf7d92c
// 0x10d7b7c: mov w8, #1
// 0x10d7b80: strb w8, [x20, #0x2ca]
// 0x10d7b84: adrp x8, #0x1e8c000
// 0x10d7b88: ldr x8, [x8, #0xd80]
// 0x10d7b8c: adrp x9, #0x832000
// 0x10d7b90: ldr s0, [x9, #0x474]
// 0x10d7b94: fabs s1, s10
// 0x10d7b98: ldr x8, [x8]
// 0x10d7b9c: fmov s2, wzr
// 0x10d7ba0: fmaxnm s1, s1, s2
// 0x10d7ba4: fmul s0, s1, s0
// 0x10d7ba8: ldr x8, [x8, #0xb8]
// 0x10d7bac: fmov s1, #8.00000000
// 0x10d7bb0: ldr s3, [x8]
// 0x10d7bb4: fmul s1, s3, s1
// 0x10d7bb8: fcmp s0, s1
// 0x10d7bbc: fcsel s0, s0, s1, gt
// 0x10d7bc0: fabd s1, s2, s10
// 0x10d7bc4: fcmp s1, s0
// 0x10d7bc8: b.mi #0x10d7c14
// 0x10d7bcc: ldr s1, [x19, #0x10]
// 0x10d7bd0: fmov s0, #1.00000000
// 0x10d7bd4: mov w8, #-0x3d800000
// 0x10d7bd8: mov w9, #0x42a00000
// 0x10d7bdc: fmin s0, s9, s0
// 0x10d7be0: fmov s2, w8
// 0x10d7be4: fcmp s9, #0.0
// 0x10d7be8: fmov s3, w9
// 0x10d7bec: fmul s0, s0, s2
// 0x10d7bf0: fsub s1, s1, s8
// 0x10d7bf4: ldp x20, x19, [sp, #0x20]
// 0x10d7bf8: ldr x30, [sp, #0x18]
// 0x10d7bfc: ldp d9, d8, [sp, #8]
// 0x10d7c00: fadd s0, s0, s3
// 0x10d7c04: fcsel s0, s0, s3, pl
// 0x10d7c08: fmul s0, s0, s1
// 0x10d7c0c: ldr d10, [sp], #0x30
// 0x10d7c10: b #0x1db0cf0
// 0x10d7c14: ldp x20, x19, [sp, #0x20]
// 0x10d7c18: ldr x30, [sp, #0x18]
// 0x10d7c1c: ldp d9, d8, [sp, #8]
// 0x10d7c20: fmov s0, wzr
// 0x10d7c24: ldr d10, [sp], #0x30
// 0x10d7c28: ret
```
