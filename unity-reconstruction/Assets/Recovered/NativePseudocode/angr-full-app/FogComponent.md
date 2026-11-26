# Native pseudocode: FogComponent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `FogComponent.get_active` — RVA `0xcd46c8`

- Decompiled symbol: `FogComponent_get_active`
- Metadata signature: `public override bool get_active() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    struct struct_0 *field_10;
    struct struct_1 *field_18;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    char field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

extern long long g_1efa100;
extern char g_1fab5d3;

unsigned long long FogComponent_get_active(struct_2 *a0)
{
    unsigned long long v0;  // x0

    if (!(g_1fab5d3 & 1))
    {
        sub_f7d92c(&g_1efa100);
        g_1fab5d3 = 1;
    }
    if (a0->field_18)
    {
        if (!a0->field_18->field_10)
        {
            return 0;
        }
        else if (a0->field_10)
        {
            if (!((char)PostProcessingContext__get_isGBufferAvailable(a0->field_10, 0) & 1))
            {
                return 0;
            }
            else if (!((char)RenderSettings__get_fog(0) & 1))
            {
                return 0;
            }
            else if (a0->field_10)
            {
                if (a0->field_10->field_30)
                    v0 = 0;
                else
                    v0 = 1;
                return v0;
            }
        }
    }
    sub_f7db74();
}
```

## `FogComponent.GetName` — RVA `0xcd4750`

- Decompiled symbol: `FogComponent_GetName`
- Metadata signature: `public override string GetName() { }`
- Native interval: `64` bytes
- Result: `pseudocode`

```c
extern unsigned long long g_1f0a488;
extern char g_1fab5d4;

long long FogComponent_GetName(void)
{
    if (!(g_1fab5d4 & 1))
    {
        sub_f7d92c(&g_1f0a488);
        g_1fab5d4 = 1;
    }
    return g_1f0a488;
}
```

## `FogComponent.GetCameraFlags` — RVA `0xcd4790`

- Decompiled symbol: `FogComponent_GetCameraFlags`
- Metadata signature: `public override DepthTextureMode GetCameraFlags() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int FogComponent_GetCameraFlags(void)
{
    return 1;
}
```

## `FogComponent.GetCameraEvent` — RVA `0xcd4798`

- Decompiled symbol: `FogComponent_GetCameraEvent`
- Metadata signature: `public override CameraEvent GetCameraEvent() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned int FogComponent_GetCameraEvent(void)
{
    return 13;
}
```

## `FogComponent.PopulateCommandBuffer` — RVA `0xcd47a0`

- Decompiled symbol: `FogComponent_PopulateCommandBuffer`
- Metadata signature: `public override void PopulateCommandBuffer(CommandBuffer cb) { }`
- Native interval: `1140` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[16];
    struct struct_2 *field_10;
    unsigned long long field_18;
} struct_3;

typedef struct struct_2 {
    char padding_0[32];
    long long field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_1;

typedef struct struct_5 {
    long long field_0;
} struct_5;

typedef struct struct_4 {
    struct struct_5 *field_0;
    unsigned long long field_8;
    unsigned long long field_10;
    unsigned long long field_18;
} struct_4;

extern struct_4 g_1db6f18;
extern struct_0 *g_1ef3150;
extern long long g_1efa100;
extern long long g_1f0a250;
extern long long g_1f0a258;
extern long long g_1f0a260;
extern long long g_1f0aa80;
extern char g_1fab5d5;

long long FogComponent_PopulateCommandBuffer(struct_3 *a0, unsigned long a1)
{
    unsigned long long v32;  // d11
    unsigned long long v33;  // d10
    unsigned long long v42;  // x20
    unsigned long long v43;  // x19
    long long v44;  // x0
    long long v45;  // x20
    unsigned int v46;  // w0
    struct_0 *v47;  // x0
    unsigned int v48;  // w8
    unsigned long long v34;  // d9
    unsigned long long v35;  // d8
    unsigned long long v36;  // x30
    unsigned long long v37;  // x25
    unsigned long long v38;  // x24
    unsigned long long v39;  // x23
    unsigned long long v40;  // x22
    unsigned long long v41;  // x21
    uint128_t flag16;  // [bp-0x190]
    uint128_t flag17;  // [bp-0x180]
    unsigned long long flag5;  // [bp-0x170]
    uint128_t flag14;  // [bp-0x160]
    uint128_t flag15;  // [bp-0x150]
    unsigned long long flag4;  // [bp-0x140]
    uint128_t flag12;  // [bp-0x130]
    uint128_t flag13;  // [bp-0x120]
    unsigned long long flag3;  // [bp-0x110]
    uint128_t flag10;  // [bp-0x100]
    uint128_t flag11;  // [bp-0xf0]
    unsigned long long flag2;  // [bp-0xe0]
    uint128_t flag8;  // [bp-0xd0]
    uint128_t flag9;  // [bp-0xc0]
    unsigned long long choice;  // [bp-0xb0]
    uint128_t flag6;  // [bp-0xa0]
    uint128_t flag7;  // [bp-0x90]
    unsigned long long flag;  // [bp-0x80]
    unsigned long long v18;  // [bp-0x70]
    unsigned long long v19;  // [bp-0x68]
    unsigned long long v20;  // [bp-0x60]
    unsigned long long v21;  // [bp-0x58]
    char *v22;  // [bp-0x50]
    unsigned long long v23;  // [bp-0x40]
    unsigned long long v24;  // [bp-0x38]
    unsigned long long v25;  // [bp-0x30]
    unsigned long long v26;  // [bp-0x28]
    unsigned long long v27;  // [bp-0x20]
    unsigned long long v28;  // [bp-0x18]
    unsigned long long v29;  // [bp-0x10]
    unsigned long long v30;  // [bp-0x8]
    char v31;  // [bp+0x0]

    v18 = v32;
    v19 = v33;
    v20 = v34;
    v21 = v35;
    v22 = &v31;
    v23 = v36;
    v24 = v37;
    v25 = v38;
    v26 = v39;
    v27 = v40;
    v28 = v41;
    v29 = v42;
    v30 = v43;
    if (!(g_1fab5d5 & 1))
    {
        sub_f7d92c(&g_1efa100);
        sub_f7d92c(&g_1ef3150);
        sub_f7d92c(&g_1f0aa80);
        sub_f7d92c(&g_1f0a258);
        sub_f7d92c(&g_1f0a250);
        sub_f7d92c(&g_1f0a260);
        g_1fab5d5 = 1;
    }
    flag = 0;
    choice = 0;
    flag2 = 0;
    flag3 = 0;
    flag4 = 0;
    flag5 = 0;
    flag6 = 0;
    flag7 = 0;
    flag8 = 0;
    flag9 = 0;
    flag10 = 0;
    flag11 = 0;
    flag12 = 0;
    flag13 = 0;
    flag14 = 0;
    flag15 = 0;
    flag16 = 0;
    flag17 = 0;
    if (a0->field_18 && a0->field_10 && a0->field_10->field_20)
    {
        v44 = MaterialFactory__Get(a0->field_10->field_20, g_1f0aa80, 0);
        if (v44)
        {
            v45 = v44;
            Material__set_shaderKeywords();
            v46 = GraphicsUtils__get_isLinearColorSpace(0);
            RenderSettings__get_fogColor(0);
            if (((char)v46 & 1))
            {
                Mathf__GammaToLinearSpace(0);
                Mathf__GammaToLinearSpace(0);
                Mathf__GammaToLinearSpace(0);
            }
            v47 = g_1ef3150;
            if (!g_1ef3150->field_e0)
            {
                sub_f7da5c(g_1ef3150);
                v47 = g_1ef3150;
            }
            Material__SetColor(v45, v47->field_b8->field_0, 0);
            RenderSettings__get_fogDensity(0);
            Material__SetFloat(v45, g_1ef3150->field_b8->field_4, 0);
            RenderSettings__get_fogStartDistance(0);
            Material__SetFloat(v45, g_1ef3150->field_b8->field_8, 0);
            RenderSettings__get_fogEndDistance(0);
            Material__SetFloat(v45, g_1ef3150->field_b8->field_c, 0);
            v48 = RenderSettings__get_fogMode(0) - 1;
            if (2 >= v48)
                Material__EnableKeyword(v45, (&g_1db6f18.field_0)[v48]->field_0, 0);
            if (a0->field_10)
                PostProcessingContext__get_isHdr(a0->field_10, 0); /* do not return */
        }
    }
    sub_f7db74();
}
```

## `FogComponent.ctor` — RVA `0xcd4c14`

- Decompiled symbol: `FogComponent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
extern long long g_1efa050;
extern char g_1fab5d6;

void FogComponent_ctor(unsigned long a0)
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
    if (!(g_1fab5d6 & 1))
    {
        sub_f7d92c(&g_1efa050);
        g_1fab5d6 = 1;
    }
    sub_15689ec();
    return;
}
```
