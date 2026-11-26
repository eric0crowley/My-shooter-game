# Native pseudocode: MotionBlurComponent.ReconstructionFilter

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MotionBlurComponent.ReconstructionFilter.ctor` — RVA `0xcd56d4`

- Decompiled symbol: `MotionBlurComponent_ReconstructionFilter_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `56` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MotionBlurComponent_ReconstructionFilter_Recovered` matched 2 offsets against `MotionBlurComponent.ReconstructionFilter` metadata (confidence 1.00).

```c
typedef struct MotionBlurComponent_ReconstructionFilter_Recovered {
    char padding_0[16];
    unsigned long long m_VectorRTFormat;
    unsigned int m_PackedRTFormat;
} MotionBlurComponent_ReconstructionFilter_Recovered;

int MotionBlurComponent_ReconstructionFilter_ctor(struct_0 *ptr)
{
    unsigned long long v0;  // x0

    ptr->field_10 = 34359738381;
    Object__ctor();
    v0 = SystemInfo__SupportsRenderTextureFormat(*((int *)((char *)&ptr->field_10 + 4)), 0);
    if (!((char)v0 & 1))
        *((unsigned int *)((char *)&ptr->field_10 + 4)) = 0;
    return v0;
}
```

## `MotionBlurComponent.ReconstructionFilter.IsSupported` — RVA `0xcd58ac`

- Decompiled symbol: `MotionBlurComponent_ReconstructionFilter_IsSupported`
- Metadata signature: `public bool IsSupported() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
void MotionBlurComponent_ReconstructionFilter_IsSupported(void)
{
    SystemInfo__get_supportsMotionVectors();
    return;
}
```

## `MotionBlurComponent.ReconstructionFilter.ProcessImage` — RVA `0xcd6044`

- Decompiled symbol: `MotionBlurComponent_ReconstructionFilter_ProcessImage`
- Metadata signature: `public void ProcessImage(PostProcessingContext context, CommandBuffer cb, ref MotionBlurModel.Settings settings, RenderTargetIdentifier source, RenderTargetIdentifier destination, Material material) { }`
- Native interval: `2320` bytes
- Result: `pseudocode`

```c
extern long long g_1ef3510;
extern char g_1fab5e7;

long long MotionBlurComponent_ReconstructionFilter_ProcessImage(unsigned long a0, long long a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5, unsigned long a6)
{
    unsigned long long v14;  // d8
    unsigned long long v15;  // x30
    unsigned long long v24;  // x20
    unsigned long long v25;  // x19
    unsigned long long v16;  // x28
    unsigned long long v17;  // x27
    unsigned long long v18;  // x26
    unsigned long long v19;  // x25
    unsigned long long v20;  // x24
    unsigned long long v21;  // x23
    unsigned long long v22;  // x22
    unsigned long long v23;  // x21
    unsigned long long v0;  // [bp-0x70]
    char *v1;  // [bp-0x60]
    unsigned long long v2;  // [bp-0x58]
    unsigned long long v3;  // [bp-0x50]
    unsigned long long v4;  // [bp-0x48]
    unsigned long long v5;  // [bp-0x40]
    unsigned long long v6;  // [bp-0x38]
    unsigned long long v7;  // [bp-0x30]
    unsigned long long v8;  // [bp-0x28]
    unsigned long long v9;  // [bp-0x20]
    unsigned long long v10;  // [bp-0x18]
    unsigned long long v11;  // [bp-0x10]
    unsigned long long v12;  // [bp-0x8]
    char v13;  // [bp+0x0]

    v0 = v14;
    v1 = &v13;
    v2 = v15;
    v3 = v16;
    v4 = v17;
    v5 = v18;
    v6 = v19;
    v7 = v20;
    v8 = v21;
    v9 = v22;
    v10 = v23;
    v11 = v24;
    v12 = v25;
    if (!(g_1fab5e7 & 1))
    {
        sub_f7d92c(&g_1ef3510);
        g_1fab5e7 = 1;
    }
    if (a1)
        PostProcessingContext__get_height(a1, 0); /* do not return */
    sub_f7db74();
}
```

## `MotionBlurComponent.ReconstructionFilter.CheckTextureFormatSupport` — RVA `0xcd748c`

- Decompiled symbol: `MotionBlurComponent_ReconstructionFilter_CheckTextureFormatSupport`
- Metadata signature: `private void CheckTextureFormatSupport() { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

int MotionBlurComponent_ReconstructionFilter_CheckTextureFormatSupport(struct_0 *ptr)
{
    unsigned long long v0;  // x0

    v0 = SystemInfo__SupportsRenderTextureFormat(ptr->field_14, 0);
    if (!((char)v0 & 1))
        ptr->field_14 = 0;
    return v0;
}
```
