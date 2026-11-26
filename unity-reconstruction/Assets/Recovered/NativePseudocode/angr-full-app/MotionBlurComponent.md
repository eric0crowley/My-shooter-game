# Native pseudocode: MotionBlurComponent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MotionBlurComponent.get_reconstructionFilter` — RVA `0xcd5668`

- Decompiled symbol: `MotionBlurComponent_get_reconstructionFilter`
- Metadata signature: `public MotionBlurComponent.ReconstructionFilter get_reconstructionFilter() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1ef3508;
extern char g_1fab5e0;

long long MotionBlurComponent_get_reconstructionFilter(struct_0 *a0)
{
    struct_0 *ptr;  // x19
    long long v1;  // x20

    if (!(g_1fab5e0 & 1))
    {
        sub_f7d92c(&g_1ef3508);
        g_1fab5e0 = 1;
    }
    ptr = &a0->field_20;
    if (a0->field_20)
        return a0->field_20;
    v1 = sub_f7db70(g_1ef3508);
    MotionBlurComponent_ReconstructionFilter__ctor(v1);
    *((long long *)&ptr->padding_0[0]) = v1;
    sub_f7d8d0(ptr, v1);
    return *((long long *)&ptr->padding_0[0]);
}
```

## `MotionBlurComponent.get_frameBlendingFilter` — RVA `0xcd570c`

- Decompiled symbol: `MotionBlurComponent_get_frameBlendingFilter`
- Metadata signature: `public MotionBlurComponent.FrameBlendingFilter get_frameBlendingFilter() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned long long field_28;
} struct_0;

extern long long g_1ef3500;
extern char g_1fab5e1;

unsigned long long MotionBlurComponent_get_frameBlendingFilter(struct_0 *a0)
{
    if (!(g_1fab5e1 & 1))
    {
        sub_f7d92c(&g_1ef3500);
        g_1fab5e1 = 1;
    }
    if (a0->field_28)
        return a0->field_28;
    MotionBlurComponent_FrameBlendingFilter__ctor(sub_f7db70(g_1ef3500)); /* do not return */
}
```

## `MotionBlurComponent.get_active` — RVA `0xcd57f0`

- Decompiled symbol: `MotionBlurComponent_get_active`
- Metadata signature: `public override bool get_active() { }`
- Native interval: `188` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

typedef struct struct_1 {
    char padding_0[16];
    char field_10;
    char padding_11[3];
    unsigned int field_14;
    char padding_18[4];
    unsigned int field_1c;
} struct_1;

extern long long g_1efa110;
extern char g_1fab5e2;

unsigned long long MotionBlurComponent_get_active(struct_0 *p)
{
    struct_1 *ptr;  // x8
    unsigned int v1;  // s0
    unsigned int v2;  // s8
    unsigned long v3;  // 4133
    unsigned long v5;  // 4125
    unsigned long v6;  // 4125
    unsigned long long v7;  // x0

    if (!(g_1fab5e2 & 1))
    {
        sub_f7d92c(&g_1efa110);
        g_1fab5e2 = 1;
    }
    ptr = *((long long *)&p->padding_0[24]);
    if (ptr)
    {
        if (!ptr->field_10)
            return 0;
        v1 = ptr->field_14;
        v2 = ptr->field_1c;
        v3 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v3))
        {
            if (!MotionBlurComponent__get_reconstructionFilter(p))
                sub_f7db74();
            v5 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v5 || ((char)SystemInfo__get_supportsMotionVectors(0) & 1))
                goto LABEL_10d586c;
        }
        else
        {
            v6 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v6))
            {
LABEL_10d586c:
                if (SystemInfo__get_graphicsDeviceType(0) != 8)
                {
                    if (*((long long *)&p->padding_0[16]))
                    {
                        if (*((char *)(*((long long *)&p->padding_0[16]) + 48)))
                            v7 = 0;
                        else
                            v7 = 1;
                        return v7;
                    }
                    sub_f7db74();
                }
            }
        }
        return 0;
    }
    sub_f7db74();
}
```

## `MotionBlurComponent.GetName` — RVA `0xcd58b4`

- Decompiled symbol: `MotionBlurComponent_GetName`
- Metadata signature: `public override string GetName() { }`
- Native interval: `64` bytes
- Result: `pseudocode`

```c
extern unsigned long long g_1f0c378;
extern char g_1fab5e3;

long long MotionBlurComponent_GetName(void)
{
    if (!(g_1fab5e3 & 1))
    {
        sub_f7d92c(&g_1f0c378);
        g_1fab5e3 = 1;
    }
    return g_1f0c378;
}
```

## `MotionBlurComponent.ResetHistory` — RVA `0xcd58f4`

- Decompiled symbol: `MotionBlurComponent_ResetHistory`
- Metadata signature: `public void ResetHistory() { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

void MotionBlurComponent_ResetHistory(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    if (ptr->field_28)
        MotionBlurComponent_FrameBlendingFilter__Dispose(ptr->field_28);
    ptr->field_28 = 0;
    sub_f7d8d0();
    return;
}
```

## `MotionBlurComponent.GetCameraFlags` — RVA `0xcd5990`

- Decompiled symbol: `MotionBlurComponent_GetCameraFlags`
- Metadata signature: `public override DepthTextureMode GetCameraFlags() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int MotionBlurComponent_GetCameraFlags(void)
{
    return 5;
}
```

## `MotionBlurComponent.GetCameraEvent` — RVA `0xcd5998`

- Decompiled symbol: `MotionBlurComponent_GetCameraEvent`
- Metadata signature: `public override CameraEvent GetCameraEvent() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int MotionBlurComponent_GetCameraEvent(void)
{
    return 18;
}
```

## `MotionBlurComponent.OnEnable` — RVA `0xcd59a0`

- Decompiled symbol: `MotionBlurComponent_OnEnable`
- Metadata signature: `public override void OnEnable() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

struct_0 * MotionBlurComponent_OnEnable(struct_0 *ptr)
{
    ptr->field_30 = 1;
    return ptr;
}
```

## `MotionBlurComponent.PopulateCommandBuffer` — RVA `0xcd59ac`

- Decompiled symbol: `MotionBlurComponent_PopulateCommandBuffer`
- Metadata signature: `public override void PopulateCommandBuffer(CommandBuffer cb) { }`
- Native interval: `1688` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    struct struct_0 *field_10;
    struct struct_1 *field_18;
    char padding_20[16];
    char field_30;
} struct_2;

typedef struct struct_3 {
    char padding_0[32];
    unsigned long long field_20;
} struct_3;

typedef struct struct_4 {
    char padding_0[20];
    unsigned long long field_14;
    unsigned int field_1c;
} struct_4;

typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

typedef struct struct_1 {
    char padding_0[20];
    unsigned long long field_14;
    unsigned int field_1c;
} struct_1;

extern long long g_1ef3510;
extern long long g_1efa110;
extern long long g_1f0aa50;
extern long long g_1f0aa98;
extern char g_1fab5e4;

struct_2 * MotionBlurComponent_PopulateCommandBuffer(struct_2 *ptr, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5, unsigned long a6)
{
    struct_2 *v4;  // x0
    struct_2 *v5;  // x0
    struct_2 *v6;  // x0
    struct_4 *p;  // x8
    unsigned long v0;  // [bp-0x80]
    unsigned int v1;  // [bp-0x78]
    char *v2;  // [bp-0x60]
    char v3;  // [bp+0x0]

    v2 = &v3;
    v4 = ptr;
    if (!(g_1fab5e4 & 1))
    {
        sub_f7d92c(&g_1efa110);
        sub_f7d92c(&g_1ef3510);
        sub_f7d92c(&g_1f0aa98);
        v5 = sub_f7d92c(&g_1f0aa50);
        g_1fab5e4 = 1;
        v4 = v5;
    }
    v6 = v4;
    if (ptr->field_30)
    {
        ptr->field_30 = 0;
        return v6;
    }
    if (ptr->field_10 && ptr->field_10->field_20)
    {
        MaterialFactory__Get(ptr->field_10->field_20, g_1f0aa98, 0);
        if (ptr->field_10 && ptr->field_10->field_20)
        {
            MaterialFactory__Get(ptr->field_10->field_20, g_1f0aa50, 0);
            p = ptr->field_18;
            if (p)
            {
                v0 = *((long long *)&(&p->padding_0)[1]);
                v1 = *((int *)((char *)&p->field_14 + 4));
                if (ptr->field_10)
                    PostProcessingContext__get_isHdr(ptr->field_10, 0); /* do not return */
            }
        }
    }
    sub_f7db74();
}
```

## `MotionBlurComponent.OnDisable` — RVA `0xcd6f58`

- Decompiled symbol: `MotionBlurComponent_OnDisable`
- Metadata signature: `public override void OnDisable() { }`
- Native interval: `16` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MotionBlurComponent_Recovered` matched 2 offsets against `MotionBlurComponent` metadata (confidence 0.67).

```c
typedef struct struct_1 {
    char padding_0[24];
    struct MotionBlurComponent_Recovered *field_18;
} struct_1;

typedef struct MotionBlurComponent_Recovered {
    char padding_0[24];
    unsigned long long field_18;
    uint128_t m_ReconstructionFilter;
    uint128_t m_FirstFrame;
} MotionBlurComponent_Recovered;

typedef struct MotionBlurComponent_Recovered {
    char padding_0[24];
    unsigned long long field_18;
    uint128_t field_20;
    uint128_t field_30;
} struct_0;

struct_1 * MotionBlurComponent_OnDisable(struct_0 *a0)
{
    struct_1 *v0;  // x0

    if (!a0->field_28)
        return NULL;
    v0 = MotionBlurComponent_FrameBlendingFilter__Dispose(a0->field_28);
    return MotionBlurComponent_FrameBlendingFilter__Dispose(a0->field_28);
}
```

## `MotionBlurComponent.ctor` — RVA `0xcd6f68`

- Decompiled symbol: `MotionBlurComponent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

extern long long g_1efa058;
extern char g_1fab5e5;

void MotionBlurComponent_ctor(struct_0 *ptr)
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
    if (!(g_1fab5e5 & 1))
    {
        sub_f7d92c(&g_1efa058);
        g_1fab5e5 = 1;
    }
    ptr->field_30 = 1;
    sub_15689ec();
    return;
}
```
