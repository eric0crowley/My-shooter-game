# Native pseudocode: BuiltinDebugViewsComponent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BuiltinDebugViewsComponent.get_active` — RVA `0xccf4d0`

- Decompiled symbol: `BuiltinDebugViewsComponent_get_active`
- Metadata signature: `public override bool get_active() { }`
- Native interval: `84` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

extern long long g_1efa0d0;
extern char g_1fab5a6;

unsigned long long BuiltinDebugViewsComponent_get_active(struct_1 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x20]

    v0 = v1;
    if (!(g_1fab5a6 & 1))
    {
        sub_f7d92c(&g_1efa0d0);
        g_1fab5a6 = 1;
    }
    if (a0->field_18)
    {
        if (3 <= a0->field_18->field_14 - 1)
            return 0;
        return 1;
    }
    sub_f7db74();
}
```

## `BuiltinDebugViewsComponent.GetCameraFlags` — RVA `0xccf524`

- Decompiled symbol: `BuiltinDebugViewsComponent_GetCameraFlags`
- Metadata signature: `public override DepthTextureMode GetCameraFlags() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

extern long long g_1efa0d0;
extern char g_1fab5a7;
extern unsigned int g_852290[4];

unsigned int BuiltinDebugViewsComponent_GetCameraFlags(struct_1 *idx)
{
    unsigned int v0;  // w8

    if (!(g_1fab5a7 & 1))
    {
        sub_f7d92c(&g_1efa0d0);
        g_1fab5a7 = 1;
    }
    if (idx->field_18)
    {
        v0 = idx->field_18->field_14 - 1;
        if (2 < v0)
            return 0;
        return g_852290[v0];
    }
    sub_f7db74();
}
```

## `BuiltinDebugViewsComponent.GetCameraEvent` — RVA `0xccf58c`

- Decompiled symbol: `BuiltinDebugViewsComponent_GetCameraEvent`
- Metadata signature: `public override CameraEvent GetCameraEvent() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

extern long long g_1efa0d0;
extern char g_1fab5a8;

unsigned long long BuiltinDebugViewsComponent_GetCameraEvent(struct_1 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x20]

    v0 = v1;
    if (!(g_1fab5a8 & 1))
    {
        sub_f7d92c(&g_1efa0d0);
        g_1fab5a8 = 1;
    }
    if (a0->field_18)
    {
        if (a0->field_18->field_14 == 3)
            return 18;
        return 12;
    }
    sub_f7db74();
}
```

## `BuiltinDebugViewsComponent.GetName` — RVA `0xccf5e4`

- Decompiled symbol: `BuiltinDebugViewsComponent_GetName`
- Metadata signature: `public override string GetName() { }`
- Native interval: `64` bytes
- Result: `pseudocode`

```c
extern char g_1fab5a9;

long long BuiltinDebugViewsComponent_GetName(void)
{
    if (!(g_1fab5a9 & 1))
    {
        sub_f7d92c("E\n");
        g_1fab5a9 = 1;
    }
    return g_1f08b30;
}
```

## `BuiltinDebugViewsComponent.PopulateCommandBuffer` — RVA `0xccf624`

- Decompiled symbol: `BuiltinDebugViewsComponent_PopulateCommandBuffer`
- Metadata signature: `public override void PopulateCommandBuffer(CommandBuffer cb) { }`
- Native interval: `288` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    struct struct_0 *field_10;
    struct struct_1 *field_18;
} struct_2;

typedef struct struct_1 {
    char padding_0[20];
    unsigned int field_14;
} struct_1;

typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1efa0d0;
extern long long g_1f0aa60;
extern long long g_1f0d760;
extern char g_1fab5aa;

long long BuiltinDebugViewsComponent_PopulateCommandBuffer(struct_2 *idx, long long a1)
{
    unsigned int flag;  // w22
    long long v1;  // x0
    unsigned long long v2;  // x0

    if (!(g_1fab5aa & 1))
    {
        sub_f7d92c(&g_1efa0d0);
        sub_f7d92c(&g_1f0d760);
        sub_f7d92c(&g_1f0aa60);
        g_1fab5aa = 1;
    }
    if (idx->field_18 && idx->field_10 && idx->field_10->field_20)
    {
        flag = idx->field_18->field_14;
        v1 = MaterialFactory__Get(idx->field_10->field_20, g_1f0aa60, 0);
        if (v1)
        {
            Material__set_shaderKeywords();
            if (idx->field_10)
            {
                if (((char)PostProcessingContext__get_isGBufferAvailable(idx->field_10, 0) & 1))
                    Material__EnableKeyword(v1, g_1f0d760, 0);
                if (flag == 3)
                {
                    BuiltinDebugViewsComponent__MotionVectorsPass(idx, a1);
                }
                else if (flag == 2)
                {
                    BuiltinDebugViewsComponent__DepthNormalsPass(idx, a1);
                }
                else if (flag == 1)
                {
                    BuiltinDebugViewsComponent__DepthPass();
                }
                if (idx->field_10)
                {
                    v2 = PostProcessingContext__Interrupt(idx->field_10, 0);
                    return PostProcessingContext__Interrupt(idx->field_10, 0);
                }
            }
        }
    }
    sub_f7db74();
}
```

## `BuiltinDebugViewsComponent.DepthPass` — RVA `0xccf744`

- Decompiled symbol: `BuiltinDebugViewsComponent_DepthPass`
- Metadata signature: `private void DepthPass(CommandBuffer cb) { }`
- Native interval: `280` bytes
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

extern long long g_1efa0d0;
extern long long g_1f0aa60;
extern char g_1fab5ab;

long long BuiltinDebugViewsComponent_DepthPass(struct_3 *a0, long long a1)
{
    long long v6;  // x0
    unsigned long long v7;  // x0
    char v0;  // [bp-0x80]
    uint128_t v1;  // [bp-0x70]
    unsigned long long v2;  // [bp-0x60]
    char v3;  // [bp-0x58]
    uint128_t v4;  // [bp-0x48]
    unsigned long long v5;  // [bp-0x38]

    if (!(g_1fab5ab & 1))
    {
        sub_f7d92c(&g_1efa0d0);
        sub_f7d92c("9f");
        sub_f7d92c(&g_1f0aa60);
        g_1fab5ab = 1;
    }
    if (a0->field_10 && a0->field_10->field_20)
    {
        v6 = MaterialFactory__Get(a0->field_10->field_20, g_1f0aa60, 0);
        if (a0->field_18)
        {
            if (!g_1ef2d28->field_e0)
                sub_f7da5c(g_1ef2d28);
            if (a1)
            {
                CommandBuffer__SetGlobalFloat(a1, g_1ef2d28->field_b8->field_0, 0);
                RenderTargetIdentifier__op_Implicit(2, 0);
                memcpy(&v0, &v3, 16);
                v1 = v4;
                v2 = v5;
                v7 = CommandBuffer__Blit(a1, 0, &v0, v6, 0, 0);
                return CommandBuffer__Blit(a1, 0, &v0, v6, 0, 0);
            }
        }
    }
    sub_f7db74();
}
```

## `BuiltinDebugViewsComponent.DepthNormalsPass` — RVA `0xccf85c`

- Decompiled symbol: `BuiltinDebugViewsComponent_DepthNormalsPass`
- Metadata signature: `private void DepthNormalsPass(CommandBuffer cb) { }`
- Native interval: `196` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1f0aa60;
extern char g_1fab5ac;

long long BuiltinDebugViewsComponent_DepthNormalsPass(struct_1 *a0, long long a1)
{
    long long v9;  // x0
    unsigned long long v10;  // x0
    char v0;  // [bp-0xa0]
    uint128_t v1;  // [bp-0x90]
    unsigned long long v2;  // [bp-0x80]
    char v3;  // [bp-0x78]
    uint128_t v4;  // [bp-0x68]
    unsigned long long v5;  // [bp-0x58]
    char v6;  // [bp-0x50]
    uint128_t v7;  // [bp-0x40]
    unsigned long long v8;  // [bp-0x30]

    if (!(g_1fab5ac & 1))
    {
        sub_f7d92c(&g_1f0aa60);
        g_1fab5ac = 1;
    }
    if (a0->field_10 && a0->field_10->field_20)
    {
        v9 = MaterialFactory__Get(a0->field_10->field_20, g_1f0aa60, 0);
        RenderTargetIdentifier__op_Implicit(2, 0);
        memcpy(&v6, &v3, 16);
        v7 = v4;
        v8 = v5;
        if (a1)
        {
            memcpy(&v0, &v6, 16);
            v1 = v7;
            v2 = v8;
            v10 = CommandBuffer__Blit(a1, 0, &v0, v9, 1, 0);
            return CommandBuffer__Blit(a1, 0, &v0, v9, 1, 0);
        }
    }
    sub_f7db74();
}
```

## `BuiltinDebugViewsComponent.MotionVectorsPass` — RVA `0xccf920`

- Decompiled symbol: `BuiltinDebugViewsComponent_MotionVectorsPass`
- Metadata signature: `private void MotionVectorsPass(CommandBuffer cb) { }`
- Native interval: `1416` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    struct struct_1 *field_10;
    unsigned long long field_18;
} struct_2;

typedef struct struct_1 {
    char padding_0[32];
    long long field_20;
} struct_1;

extern long long g_1efa0d0;
extern long long g_1f0aa60;
extern char g_1fab5ad;

long long BuiltinDebugViewsComponent_MotionVectorsPass(struct_2 *a0, unsigned long a1)
{
    unsigned long long v17;  // d12
    unsigned long long v18;  // d11
    unsigned long long v27;  // x23
    unsigned long long v28;  // x22
    unsigned long long v29;  // x21
    unsigned long long v30;  // x20
    unsigned long long v31;  // x19
    unsigned long long v19;  // d10
    unsigned long long v20;  // d9
    unsigned long long v21;  // d8
    unsigned long long v22;  // x30
    unsigned long long v23;  // x27
    unsigned long long v24;  // x26
    unsigned long long v25;  // x25
    unsigned long long v26;  // x24
    unsigned long long v0;  // [bp-0x80]
    unsigned long long v1;  // [bp-0x78]
    unsigned long long v2;  // [bp-0x70]
    unsigned long long v3;  // [bp-0x68]
    unsigned long long v4;  // [bp-0x60]
    char *v5;  // [bp-0x58]
    unsigned long long v6;  // [bp-0x50]
    unsigned long long v7;  // [bp-0x48]
    unsigned long long v8;  // [bp-0x40]
    unsigned long long v9;  // [bp-0x38]
    unsigned long long v10;  // [bp-0x30]
    unsigned long long v11;  // [bp-0x28]
    unsigned long long v12;  // [bp-0x20]
    unsigned long long v13;  // [bp-0x18]
    unsigned long long v14;  // [bp-0x10]
    unsigned long long v15;  // [bp-0x8]
    char v16;  // [bp+0x0]

    v0 = v17;
    v1 = v18;
    v2 = v19;
    v3 = v20;
    v4 = v21;
    v5 = &v16;
    v6 = v22;
    v7 = v23;
    v8 = v24;
    v9 = v25;
    v10 = v26;
    v11 = v27;
    v12 = v28;
    v13 = v29;
    v14 = v30;
    v15 = v31;
    if (!(g_1fab5ad & 1))
    {
        sub_f7d92c(&g_1efa0d0);
        sub_f7d92c("9f");
        sub_f7d92c(&g_1f0aa60);
        g_1fab5ad = 1;
    }
    if (a0->field_10 && a0->field_10->field_20)
    {
        MaterialFactory__Get(a0->field_10->field_20, g_1f0aa60, 0);
        if (a0->field_18)
        {
            if (!g_1ef2d28->field_e0)
                sub_f7da5c(g_1ef2d28);
            if (a0->field_10)
                PostProcessingContext__get_width(a0->field_10, 0); /* do not return */
        }
    }
    sub_f7db74();
}
```

## `BuiltinDebugViewsComponent.PrepareArrows` — RVA `0xccfea8`

- Decompiled symbol: `BuiltinDebugViewsComponent_PrepareArrows`
- Metadata signature: `private void PrepareArrows() { }`
- Native interval: `268` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[24];
    struct struct_0 *field_18;
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[44];
    unsigned int field_2c;
} struct_0;

typedef struct struct_1 {
    char padding_0[16];
    long long field_10;
    unsigned int field_18;
} struct_1;

typedef struct struct_3 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
} struct_3;

extern long long g_1efa0d0;
extern char g_1fab5ae;

long long BuiltinDebugViewsComponent_PrepareArrows(struct_2 *addr)
{
    unsigned long v0;  // x20
    unsigned int v1;  // w0
    unsigned long p;  // x23
    unsigned long long v11;  // x0
    unsigned long v2;  // x0
    struct_1 *v3;  // x23
    struct_2 *ptr;  // x19
    unsigned long v5;  // x0
    struct_3 *v6;  // x23
    unsigned long v7;  // x0
    unsigned long v8;  // x0
    unsigned int v9;  // w21

    if (!(g_1fab5ae & 1))
    {
        sub_f7d92c("1f");
        sub_f7d92c(&g_1efa0d0);
        g_1fab5ae = 1;
    }
    if (addr->field_18)
    {
        v0 = addr->field_18->field_2c;
        v1 = Screen__get_width(0);
        v2 = Screen__get_height(0);
        v3 = addr->field_20;
        ptr = &addr->field_20;
        v5 = v2;
        if (!v3)
        {
            v6 = sub_f7db70(g_1ef2d20);
            Object__ctor(v6, 0);
            *((struct_3 **)&ptr->padding_0[0]) = v6;
            v7 = sub_f7d8d0(ptr, v6);
            v3 = *((long long *)&ptr->padding_0[0]);
            v5 = v7;
            if (v3)
                goto LABEL_10cff44;
        }
        else
        {
LABEL_10cff44:
            v8 = v5;
            v9 = v0 * v1 / (v2 & 4294967295);
            if (v3->field_18 == v9 && *((int *)&v3[1].padding_0[0]) == (unsigned int)v0)
                return v8;
            p = &v3->field_10;
            GraphicsUtils__Destroy(v3->field_10, 0);
            *((long long *)p) = 0;
            sub_f7d8d0(p, 0);
            if (*((long long *)&ptr->padding_0[0]))
            {
                v11 = BuiltinDebugViewsComponent_ArrowArray__BuildMesh(*((long long *)&ptr->padding_0[0]), v9, v0 & 4294967295);
                return BuiltinDebugViewsComponent_ArrowArray__BuildMesh(*((long long *)&ptr->padding_0[0]), v9, v0 & 4294967295);
            }
        }
    }
    sub_f7db74();
}
```

## `BuiltinDebugViewsComponent.OnDisable` — RVA `0xcd041c`

- Decompiled symbol: `BuiltinDebugViewsComponent_OnDisable`
- Metadata signature: `public override void OnDisable() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

void BuiltinDebugViewsComponent_OnDisable(struct_1 *ptr)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_0 *v6;  // x20
    unsigned long p;  // x20
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    v6 = ptr->field_20;
    if (v6)
    {
        p = &v6->field_10;
        GraphicsUtils__Destroy(v6->field_10, 0);
        *((long long *)p) = 0;
        sub_f7d8d0(p, 0);
    }
    ptr->field_20 = NULL;
    sub_f7d8d0();
    return;
}
```

## `BuiltinDebugViewsComponent.ctor` — RVA `0xcd0464`

- Decompiled symbol: `BuiltinDebugViewsComponent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
extern long long g_1efa048;
extern char g_1fab5af;

void BuiltinDebugViewsComponent_ctor(unsigned long a0)
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
    if (!(g_1fab5af & 1))
    {
        sub_f7d92c(&g_1efa048);
        g_1fab5af = 1;
    }
    sub_15689ec();
    return;
}
```
