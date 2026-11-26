# Native pseudocode: UiParticles

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `UiParticles.get_ParticleSystem` — RVA `0xccc604`

- Decompiled symbol: `UiParticles_get_ParticleSystem`
- Metadata signature: `public ParticleSystem get_ParticleSystem() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[216];
    unsigned long long field_d8;
} struct_0;

long long UiParticles_get_ParticleSystem(struct_0 *a0)
{
    return a0->field_d8;
}
```

## `UiParticles.set_ParticleSystem` — RVA `0xccc60c`

- Decompiled symbol: `UiParticles_set_ParticleSystem`
- Metadata signature: `public void set_ParticleSystem(ParticleSystem value) { }`
- Native interval: `128` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[728];
    unsigned long long field_2d8;
} struct_0;

extern long long g_1f01250;
extern char g_1fab592;

unsigned long long UiParticles_set_ParticleSystem(struct_0 **a0, long long a1)
{
    unsigned long long v0;  // x0

    if (!(g_1fab592 & 1))
    {
        sub_f7d92c(&g_1f01250);
        g_1fab592 = 1;
    }
    v0 = sub_11398ec(a0 + 27, a1, g_1f01250);
    if (!((char)v0 & 1))
        return v0;
    goto *(a0)->field_2d8;
}
```

## `UiParticles.get_mainTexture` — RVA `0xccc68c`

- Decompiled symbol: `UiParticles_get_mainTexture`
- Metadata signature: `public override Texture get_mainTexture() { }`
- Native interval: `296` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[824];
    struct struct_1 *field_338;
    unsigned long long field_340;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1ef0c58;
extern char g_1fab593;

void UiParticles_get_mainTexture(struct_0 **a0)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    struct_0 **v8;  // x0
    unsigned long v9;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab593 & 1))
    {
        sub_f7d92c("W=");
        sub_f7d92c(&g_1ef0c58);
        g_1fab593 = 1;
    }
    v8 = a0;
    v9 = *(a0)->field_340;
    *(a0)->field_338();
}
```

## `UiParticles.get_RenderMode` — RVA `0xccc7b4`

- Decompiled symbol: `UiParticles_get_RenderMode`
- Metadata signature: `public UiParticleRenderMode get_RenderMode() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

int UiParticles_get_RenderMode(struct_0 *a0)
{
    return a0->field_e0;
}
```

## `UiParticles.set_RenderMode` — RVA `0xccc7bc`

- Decompiled symbol: `UiParticles_set_RenderMode`
- Metadata signature: `public void set_RenderMode(UiParticleRenderMode value) { }`
- Native interval: `128` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[728];
    unsigned long long field_2d8;
} struct_0;

extern long long g_1f01258;
extern char g_1fab594;

unsigned long long UiParticles_set_RenderMode(struct_0 **a0, unsigned int a1)
{
    unsigned long long v0;  // x0

    if (!(g_1fab594 & 1))
    {
        sub_f7d92c(&g_1f01258);
        g_1fab594 = 1;
    }
    v0 = sub_1139948(a0 + 28, a1, g_1f01258);
    if (!((char)v0 & 1))
        return v0;
    goto *(a0)->field_2d8;
}
```

## `UiParticles.Awake` — RVA `0xccc83c`

- Decompiled symbol: `UiParticles_Awake`
- Metadata signature: `protected override void Awake() { }`
- Native interval: `304` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efd040;
extern long long g_1efd048;
extern char g_1fab595;

void UiParticles_Awake(long long *p)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    long long v12;  // x0
    long long ptr[31];  // x22
    long long v14;  // x21
    long long v15;  // x0
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
    if (!(g_1fab595 & 1))
    {
        sub_f7d92c(&g_1efd048);
        sub_f7d92c(&g_1efd040);
        sub_f7d92c(&g_1ef0c58);
        g_1fab595 = 1;
    }
    v12 = sub_1231bc8(p, g_1efd040);
    ptr = p + 4;
    v14 = sub_1231bc8(p, g_1efd048);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(p[4], 0, 0) & 1))
    {
        if (!v14)
            goto LABEL_10cc968;
        v15 = Renderer__get_sharedMaterial(v14, 0);
        ptr[0] = v15;
        sub_f7d8d0(ptr, v15);
    }
    else if (!v14)
    {
LABEL_10cc968:
        sub_f7db74();
    }
    if (ParticleSystemRenderer__get_renderMode(v14, 0) == 1)
        UiParticles__set_RenderMode(p, 1);
    UIBehaviour__Awake(p, 0);
    UiParticles__set_ParticleSystem(p, v12);
    p[30] = v14;
    sub_f7d8d0();
    return;
}
```

## `UiParticles.SetMaterialDirty` — RVA `0xccc96c`

- Decompiled symbol: `UiParticles_SetMaterialDirty`
- Metadata signature: `public override void SetMaterialDirty() { }`
- Native interval: `148` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[240];
    long long field_f0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab596;

long long UiParticles_SetMaterialDirty(struct_1 *a0)
{
    long long v0;  // x0
    unsigned long long v1;  // x0

    if (!(g_1fab596 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab596 = 1;
    }
    Graphic__SetMaterialDirty(a0, 0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Inequality(a0->field_f0, 0, 0);
    if (!((char)v0 & 1))
        return v0;
    if (a0->field_f0)
    {
        v1 = Renderer__set_sharedMaterial();
        return Renderer__set_sharedMaterial();
    }
    sub_f7db74(0);
}
```

## `UiParticles.OnPopulateMesh` — RVA `0xccca00`

- Decompiled symbol: `UiParticles_OnPopulateMesh`
- Metadata signature: `protected override void OnPopulateMesh(VertexHelper toFill) { }`
- Native interval: `152` bytes
- Result: `pseudocode`
- Heuristic layout hint: `UiParticles_Recovered` matched 2 offsets against `UiParticles` metadata (confidence 1.00).

```c
typedef struct UiParticles_Recovered {
    char padding_0[216];
    long long m_ParticleSystem;
    char padding_e0[24];
    struct struct_1 *m_Particles;
} UiParticles_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab597;

long long UiParticles_OnPopulateMesh(struct_2 *ptr, long long a1)
{
    unsigned long long v2;  // x23
    long long v3;  // x0
    unsigned int v4;  // w21
    unsigned long v5;  // x22
    struct_1 *v6;  // x8
    char v0;  // [bp-0xb8]
    unsigned long long v1;  // [bp-0x28]

    if (!(g_1fab597 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab597 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Equality(ptr->field_d8, 0, 0) & 1))
    {
        v1 = v2;
        UiParticles__InitParticlesBuffer(ptr, a1);
        v3 = ptr->field_d8;
        if (v3)
        {
            v3 = ParticleSystem__GetParticles(v3, ptr->field_f8, 0);
            if (a1)
            {
                v4 = v3;
                v3 = VertexHelper__Clear(a1, 0);
                if (v4 < 1)
                    return v3;
                v5 = 0;
                while (true)
                {
                    v6 = ptr->field_f8;
                    if (!v6)
                        break;
                    if (v6->field_18 <= v5)
                        sub_f7db7c(v3);
                    memmove(&v0, (struct struct_1 *)&v6->padding_0[v2], 132);
                    v3 = UiParticles__DrawParticleBillboard(ptr, &v0, a1);
                    v5 += 1;
                    if (v4 == v5)
                        return v3;
                }
            }
        }
        v3 = sub_f7db74(v3);
        sub_f7db7c(v3);
    }
}
```

## `UiParticles.GenerateParticlesBillboards` — RVA `0xccca98`

- Decompiled symbol: `UiParticles_GenerateParticlesBillboards`
- Metadata signature: `private void GenerateParticlesBillboards(VertexHelper vh) { }`
- Native interval: `184` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x10cca98: sub sp, sp, #0xc0
// 0x10cca9c: stp x30, x23, [sp, #0x90]
// 0x10ccaa0: stp x22, x21, [sp, #0xa0]
// 0x10ccaa4: stp x20, x19, [sp, #0xb0]
// 0x10ccaa8: mov x19, x1
// 0x10ccaac: mov x20, x0
// 0x10ccab0: bl #0x10ccc7c
// 0x10ccab4: ldr x0, [x20, #0xd8]
// 0x10ccab8: cbz x0, #0x10ccb48
// 0x10ccabc: ldr x1, [x20, #0xf8]
// 0x10ccac0: mov x2, xzr
// 0x10ccac4: bl #0x1bc99d8
// 0x10ccac8: cbz x19, #0x10ccb48
// 0x10ccacc: mov w21, w0
// 0x10ccad0: mov x0, x19
// 0x10ccad4: mov x1, xzr
// 0x10ccad8: bl #0x1d8544c
// 0x10ccadc: cmp w21, #1
// 0x10ccae0: b.lt #0x10ccb34
// 0x10ccae4: mov x22, xzr
// 0x10ccae8: mov w21, w21
// 0x10ccaec: mov w23, #0x20
// 0x10ccaf0: ldr x8, [x20, #0xf8]
// 0x10ccaf4: cbz x8, #0x10ccb48
// 0x10ccaf8: ldr w9, [x8, #0x18]
// 0x10ccafc: cmp x22, x9
// 0x10ccb00: b.hs #0x10ccb4c
// 0x10ccb04: add x1, x8, x23
// 0x10ccb08: add x0, sp, #8
// 0x10ccb0c: mov w2, #0x84
// 0x10ccb10: bl #0x1db0cd0
// 0x10ccb14: add x1, sp, #8
// 0x10ccb18: mov x0, x20
// 0x10ccb1c: mov x2, x19
// 0x10ccb20: bl #0x10ccd44
// 0x10ccb24: add x22, x22, #1
// 0x10ccb28: cmp x21, x22
// 0x10ccb2c: add x23, x23, #0x84
// 0x10ccb30: b.ne #0x10ccaf0
// 0x10ccb34: ldp x20, x19, [sp, #0xb0]
// 0x10ccb38: ldp x22, x21, [sp, #0xa0]
// 0x10ccb3c: ldp x30, x23, [sp, #0x90]
// 0x10ccb40: add sp, sp, #0xc0
// 0x10ccb44: ret
// 0x10ccb48: bl #0xf7db74
// 0x10ccb4c: bl #0xf7db7c
```

## `UiParticles.Update` — RVA `0xcccb50`

- Decompiled symbol: `UiParticles_Update`
- Metadata signature: `protected virtual void Update() { }`
- Native interval: `300` bytes
- Result: `pseudocode`
- Heuristic layout hint: `UiParticles_Recovered` matched 3 offsets against `UiParticles` metadata (confidence 0.75).

```c
typedef struct UiParticles_Recovered {
    struct struct_1 *field_0;
    char padding_8[208];
    long long m_ParticleSystem;
    char padding_e0[12];
    char m_IgnoreTimescale;
    char padding_ed[3];
    long long m_ParticleSystemRenderer;
} UiParticles_Recovered;

typedef struct struct_1 {
    char padding_0[760];
    struct struct_2 *field_2f8;
    unsigned long long field_300;
} struct_1;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab598;

long long UiParticles_Update(struct_3 *ptr)
{
    unsigned long long v0;  // x2
    unsigned long v1;  // x0
    long long v2;  // x0
    unsigned long long v3;  // x3
    struct_3 *v4;  // x0
    unsigned long v5;  // x1
    long long v6;  // x0
    long long v7;  // x0
    unsigned long long v8;  // x0

    if (!(g_1fab598 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab598 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = 0;
    v1 = Object__op_Inequality(ptr->field_d8, 0, 0);
    if (ptr->field_ec)
    {
        if (!(v1 & 1))
            goto LABEL_10ccc0c;
        v2 = Time__get_unscaledDeltaTime(0);
        if (ptr->field_d8)
        {
            v0 = 0;
            v3 = 0;
            ParticleSystem__Simulate(ptr->field_d8, 1, 0, 0);
            v4 = ptr;
            v5 = ptr->field_0->field_300;
            ptr->field_0->field_2f8();
        }
    }
    else
    {
        if (((char)v1 & 1))
        {
            v2 = ptr->field_d8;
            if (!v2)
            {
                sub_f7db74(v2);
            }
            else if (((char)ParticleSystem__get_isPlaying(v2, 0) & 1))
            {
                v0 = 0;
                v4 = ptr;
                v5 = ptr->field_0->field_300;
                ptr->field_0->field_2f8();
            }
        }
LABEL_10ccc0c:
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v6 = Object__op_Inequality(ptr->field_f0, 0, 0);
        if (!((char)v6 & 1))
            return v6;
        v2 = ptr->field_f0;
        if (v2)
        {
            v7 = Renderer__get_enabled(v2, 0);
            if (!((char)v7 & 1))
                return v7;
            v2 = ptr->field_f0;
            if (v2)
            {
                v8 = Renderer__set_enabled();
                return Renderer__set_enabled();
            }
        }
    }
    sub_f7db74(v2);
}
```

## `UiParticles.InitParticlesBuffer` — RVA `0xcccc7c`

- Decompiled symbol: `UiParticles_InitParticlesBuffer`
- Metadata signature: `private void InitParticlesBuffer() { }`
- Native interval: `200` bytes
- Result: `pseudocode`
- Heuristic layout hint: `UiParticles_Recovered` matched 2 offsets against `UiParticles` metadata (confidence 1.00).

```c
typedef struct UiParticles_Recovered {
    char padding_0[216];
    unsigned long long m_ParticleSystem;
    char padding_e0[24];
    struct struct_0 *m_Particles;
} UiParticles_Recovered;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

extern long long g_1eee540;
extern char g_1fab599;

long long UiParticles_InitParticlesBuffer(struct_1 *ptr, unsigned long a1, unsigned long a2)
{
    struct_1 *p;  // x19
    unsigned long long v2;  // x0
    unsigned long v3;  // x0
    unsigned int v4;  // w0
    struct_2 *v5;  // x0
    unsigned long v6;  // x0
    unsigned long long v0;  // [bp-0x28], Other Possible Types: unsigned long

    if (!(g_1fab599 & 1))
    {
        sub_f7d92c(&g_1eee540);
        g_1fab599 = 1;
    }
    v0 = 0;
    p = &ptr->field_f8;
    if (ptr->field_f8)
    {
        v2 = ptr->field_d8;
        if (!v2)
            sub_f7db74(v2);
        v0 = ParticleSystem__get_main(v2, 0);
        v3 = ParticleSystem_MainModule__get_maxParticles(&v0, 0);
        if ((unsigned int)v3 <= ptr->field_f8->field_18)
            return v3;
    }
    v2 = ptr->field_d8;
    if (v2)
    {
        v0 = ParticleSystem__get_main(v2, 0);
        v4 = ParticleSystem_MainModule__get_maxParticles(&v0, 0);
        v5 = sub_f7d9d4(g_1eee540, v4);
        *((struct_2 **)&p->padding_0[0]) = v5;
        v6 = sub_f7d8d0(p, v5);
        return sub_f7d8d0(p, v5);
    }
    sub_f7db74(v2);
}
```

## `UiParticles.DrawParticleBillboard` — RVA `0xcccd44`

- Decompiled symbol: `UiParticles_DrawParticleBillboard`
- Metadata signature: `private void DrawParticleBillboard(ParticleSystem.Particle particle, VertexHelper vh) { }`
- Native interval: `1160` bytes
- Result: `pseudocode`
- Heuristic layout hint: `UiParticles_Recovered` matched 2 offsets against `UiParticles` metadata (confidence 1.00).

```c
typedef struct UiParticles_Recovered {
    char padding_0[216];
    struct struct_0 *m_ParticleSystem;
    unsigned int m_RenderMode;
} UiParticles_Recovered;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

extern long long g_1eee408;
extern char g_1fab59a;

long long UiParticles_DrawParticleBillboard(struct_1 *p, long long ptr, long long a2, unsigned long a3)
{
    uint128_t v25;  // q1
    uint128_t v26;  // q9
    unsigned int v35;  // s14
    unsigned int v36;  // s0
    unsigned int v37;  // s0
    unsigned int v38;  // s0
    struct_2 *v39;  // x0
    unsigned int v40;  // w22
    struct_2 *v41;  // x0
    struct_2 *v42;  // x23
    struct_2 *v43;  // x0
    unsigned long long v44;  // x20
    uint128_t v27;  // q2
    unsigned int v45;  // w20
    unsigned long long v46;  // x0
    uint128_t v28;  // q10
    unsigned int v29;  // s0
    unsigned int v30;  // s0
    uint128_t v31;  // q1
    uint128_t v32;  // q2
    struct_0 *v33;  // x0
    unsigned int v34;  // s13
    unsigned int v0;  // [bp-0x1f0]
    unsigned int v1;  // [bp-0x1ec]
    unsigned int v2;  // [bp-0x1e8]
    unsigned int v3;  // [bp-0x1e4]
    unsigned int v4;  // [bp-0x1e0]
    unsigned int v5;  // [bp-0x1dc]
    unsigned int v6;  // [bp-0x1d8]
    unsigned int v7;  // [bp-0x1d4]
    unsigned int v8;  // [bp-0x1d0]
    unsigned int v9;  // [bp-0x1cc]
    unsigned int v10;  // [bp-0x1c8]
    unsigned int v11;  // [bp-0x1c4]
    char v12;  // [bp-0x1c0]
    char v13;  // [bp-0x138]
    unsigned long v14;  // [bp-0xb0], Other Possible Types: unsigned long long
    unsigned long v15;  // [bp-0xa8]
    unsigned int v16;  // [bp-0xa0]
    unsigned int v17;  // [bp-0x9c]
    unsigned int v18;  // [bp-0x98]
    unsigned int v19;  // [bp-0x90]
    unsigned int v20;  // [bp-0x8c]
    unsigned int v21;  // [bp-0x88]
    unsigned int v22;  // [bp-0x84]
    char *v23;  // [bp-0x40]
    char v24;  // [bp+0x0]

    v23 = &v24;
    if (!(g_1fab59a & 1))
    {
        sub_f7d92c(&g_1eee408);
        g_1fab59a = 1;
    }
    v14 = 0;
    ParticleSystem_Particle__get_position(ptr, 0);
    v26 = v25;
    v28 = v27;
    ParticleSystem_Particle__get_rotation3D(ptr, 0);
    v30 = v29 * 1016003125;
    v31 = (unsigned int)v25 * 1016003125;
    v32 = (unsigned int)v27 * 1016003125;
    Quaternion__Internal_FromEulerRad(0);
    v19 = v30;
    v20 = v31;
    v21 = v32;
    v22 = 1016003125;
    v33 = p->field_d8;
    if (v33)
    {
        v34 = v31;
        v35 = v32;
        v15 = ParticleSystem__get_main(v33, 0);
        if ((int)ParticleSystem_MainModule__get_simulationSpace(&v15, 0) != 1)
        {
            v8 = v29;
            v37 = v30;
            goto LABEL_10cce58;
        }
        v33 = Graphic__get_rectTransform(p, 0);
        if (v33)
        {
            v36 = v29;
            v31 = v26;
            v32 = v28;
            Transform__InverseTransformPoint();
            v26 = v31;
            v28 = v32;
            v8 = v36;
            v37 = v36;
LABEL_10cce58:
            v38 = v37;
            ParticleSystem_Particle__get_startLifetime(ptr, 0);
            ParticleSystem_Particle__get_remainingLifetime(ptr, 0);
            ParticleSystem_Particle__get_startLifetime(ptr, 0);
            ParticleSystem_Particle__GetCurrentSize3D(ptr, p->field_d8, 0);
            v16 = v38;
            v17 = v31;
            v18 = v32;
            v9 = v28;
            v10 = v26;
            v11 = v38 - v38;
            if (p->field_e0 == 1)
            {
                memcpy(&v13, ptr, 132);
                UiParticles__GetStrechedBillboardsSizeAndRotation();
                v30 = v19;
                v34 = v20;
                v35 = v21;
            }
            Quaternion__op_Multiply(0);
            v6 = v34;
            v7 = v30;
            v5 = v35;
            Quaternion__op_Multiply(0);
            v3 = v34;
            v4 = v30;
            v2 = v35;
            Quaternion__op_Multiply(0);
            v1 = v35;
            Quaternion__op_Multiply(0);
            v39 = ParticleSystem_Particle__GetCurrentColor(ptr, p->field_d8, 0);
            v33 = v39;
            if (a2)
            {
                v0 = v30;
                v40 = VertexHelper__get_currentVertCount(a2, 0);
                v41 = sub_f7d9d4(g_1eee408, 4);
                v33 = v41;
                if (p->field_d8)
                {
                    v42 = v41;
                    v14 = ParticleSystem__get_textureSheetAnimation(p->field_d8, 0);
                    if (((char)ParticleSystem_TextureSheetAnimationModule__get_enabled(&v14, 0) & 1))
                    {
                        memcpy(&v12, ptr, 132);
                        v43 = UiParticles__EvaluateTexturesheetUVs(p, &v12, v42);
                    }
                    else
                    {
                        v43 = UiParticles__EvaluateQuadUVs();
                    }
                    v33 = v43;
                    if (v42)
                    {
                        if (!v42->field_18)
                            sub_f7db7c(v43);
                        v44 = v39 & 4294967295;
                        v43 = VertexHelper__AddVert(a2, v44, 0);
                        if (v42->field_18 > 1)
                        {
                            v43 = VertexHelper__AddVert(a2, v44, 0);
                            if (v42->field_18 > 2)
                            {
                                v43 = VertexHelper__AddVert(a2, v44, 0);
                                if (v42->field_18 > 3)
                                {
                                    VertexHelper__AddVert(a2, v44, 0);
                                    v45 = v40 + 2;
                                    VertexHelper__AddTriangle(a2, v40, v40 + 1, v45, 0);
                                    v46 = VertexHelper__AddTriangle(a2, v45, v40 + 3, v40, 0);
                                    return VertexHelper__AddTriangle(a2, v45, v40 + 3, v40, 0);
                                }
                            }
                        }
                        goto LABEL_10cd1c8;
                    }
                }
            }
        }
    }
    v43 = sub_f7db74(v33);
LABEL_10cd1c8:
    sub_f7db7c(v43);
}
```

## `UiParticles.GetStrechedBillboardsSizeAndRotation` — RVA `0xccd1cc`

- Decompiled symbol: `UiParticles_GetStrechedBillboardsSizeAndRotation`
- Metadata signature: `private void GetStrechedBillboardsSizeAndRotation(ParticleSystem.Particle particle, float timeAlive01, ref Vector3 size3D, out Quaternion rotation) { }`
- Native interval: `844` bytes
- Result: `pseudocode`
- Heuristic layout hint: `UiParticles_Recovered` matched 3 offsets against `UiParticles` metadata (confidence 1.00).

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct UiParticles_Recovered {
    char padding_0[216];
    unsigned long long m_ParticleSystem;
    char padding_e0[4];
    unsigned int m_StretchedSpeedScale;
    unsigned int m_StretchedLenghScale;
} UiParticles_Recovered;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_3 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    char padding_c[12];
    unsigned int field_18;
    unsigned int field_1c;
    unsigned int field_20;
} struct_3;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_3 *field_b8;
} struct_2;

extern struct_2 *g_1ef22e8;
extern char g_1fab2c9;
extern char g_1fab32c;
extern char g_1fab3df;
extern char g_1fab3e2;

struct_0 * UiParticles_GetStrechedBillboardsSizeAndRotation(struct_4 *p, long long a1, unsigned int *ptr, unsigned int *addr)
{
    unsigned int v6;  // s0
    unsigned long long v7;  // x0
    unsigned int v16;  // s11
    unsigned int v17;  // s15
    unsigned int v18;  // s14
    unsigned int v19;  // s0
    unsigned int v20;  // s1
    unsigned long v21;  // 4153
    struct_1 *v22;  // x0
    unsigned int v23;  // s2
    unsigned int v24;  // s3
    unsigned int v25;  // s1
    unsigned int ptr3[9];  // x8
    unsigned int v26;  // s0
    unsigned int v27;  // s1
    unsigned long v28;  // 4221
    unsigned int v29;  // s10
    unsigned long v30;  // 4136
    unsigned int v31;  // s10
    unsigned int v32;  // s11
    unsigned int v33;  // s9
    unsigned int v34;  // s12
    struct_1 *v35;  // x0
    unsigned int v9;  // s11
    unsigned int v36;  // s0
    unsigned int v10;  // s10
    unsigned int v11;  // s9
    unsigned int v12;  // s0
    uint128_t v13;  // q1
    unsigned int ptr4[9];  // x8
    unsigned int v15;  // s9
    unsigned int v0;  // [bp-0xc4]
    char v1;  // [bp-0xc0]
    uint128_t v2;  // [bp-0xb0]
    uint128_t flag;  // [bp-0xa0], Other Possible Types: char
    uint128_t v4;  // [bp-0x90]
    unsigned long long v5;  // [bp-0x78], Other Possible Types: unsigned long

    v6 = 0;
    v5 = 0;
    flag = 0;
    v4 = 0;
    if (!g_1fab2c9)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab2c9 = 1;
    }
    v7 = p->field_d8;
    if (v7)
    {
        ptr3 = g_1ef22e8->field_b8;
        v9 = ptr3[1];
        v10 = ptr3[2];
        v11 = ptr3[0];
        v5 = ParticleSystem__get_velocityOverLifetime(v7, 0);
        if (((char)ParticleSystem_VelocityOverLifetimeModule__get_enabled(&v5, 0) & 1))
        {
            v7 = p->field_d8;
            if (v7)
            {
                v5 = ParticleSystem__get_velocityOverLifetime(v7, 0);
                ParticleSystem_VelocityOverLifetimeModule__get_x(&v5, 0);
                memcpy(&flag, &v1, 16);
                v4 = v2;
                ParticleSystem_MinMaxCurve__Evaluate(&flag, 0);
                v7 = p->field_d8;
                if (v7)
                {
                    v11 = v12;
                    v5 = ParticleSystem__get_velocityOverLifetime(v7, 0);
                    ParticleSystem_VelocityOverLifetimeModule__get_y(&v5, 0);
                    memcpy(&flag, &v1, 16);
                    v4 = v2;
                    ParticleSystem_MinMaxCurve__Evaluate(&flag, 0);
                    v7 = p->field_d8;
                    if (v7)
                    {
                        v9 = v12;
                        v5 = ParticleSystem__get_velocityOverLifetime(v7, 0);
                        ParticleSystem_VelocityOverLifetimeModule__get_z(&v5, 0);
                        v13 = v2;
                        memcpy(&flag, &v1, 16);
                        v4 = v13;
                        v6 = v12;
                        ParticleSystem_MinMaxCurve__Evaluate(&flag, 0);
                        v10 = v6;
                        goto LABEL_10cd328;
                    }
                }
            }
        }
        else
        {
LABEL_10cd328:
            v0 = v10;
            ParticleSystem_Particle__get_velocity(a1, 0);
            if (!g_1fab32c)
            {
                sub_f7d92c(&g_1ef22e8);
                g_1fab32c = 1;
            }
            ptr4 = g_1ef22e8->field_b8;
            v15 = v11 + v6;
            v16 = ptr4[6];
            v17 = ptr4[7];
            v18 = ptr4[8];
            if (!g_1fab3e2)
            {
                sub_f7d92c("_F");
                g_1fab3e2 = 1;
            }
            if (!g_1ef07e8->field_e0)
                sub_f7da5c(g_1ef07e8);
            v19 = [D] unsupported_Iop_SqrtF32();
            v20 = 0;
            v21 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v19, 646978941)) >> 5 & 3 | (unsigned long long)(CmpF(v19, 646978941) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v19, 646978941)) >> 5 & 3 | (unsigned long long)(CmpF(v19, 646978941) & 1)) & ((unsigned long long)(char)(CmpF(v19, 646978941)) >> 5 & 3 | (unsigned long long)(CmpF(v19, 646978941) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v21))
            {
                v22 = g_1ef07e8;
                v24 = (v0 + v23) * v18;
                v25 = v15 * v16 + (v9 + (unsigned int)v13) * v17;
                v26 = (v24 + v15 * v16 + (v9 + (unsigned int)v13) * v17) / v19;
                v27 = [D] unsupported_Iop_ZeroHI96ofV128();
                v28 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v26, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF(v26, 0xbf800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((v24 + v25) / v19, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF((v24 + v25) / v19, 0xbf800000) & 1)) & ((unsigned long long)(char)(CmpF(v26, 0xbf800000)) >> 5 & 3 | (unsigned long long)(CmpF((v24 + v25) / v19, 0xbf800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v28)
                    v29 = v27;
                else
                    v29 = 0xbf800000;
                if (!g_1ef07e8->field_e0)
                    v22 = sub_f7da5c(g_1ef07e8);
                acos(v22);
                v20 = v29 * 1113927393;
            }
            v30 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v15, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v15, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v15, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v15, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v15, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v15, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v30))
                v20 = -(v20);
            Quaternion__Internal_FromEulerRad();
            *(addr) = 0;
            addr[1] = 0;
            addr[2] = v20 * 1016003125;
            addr[3] = v24;
            v31 = *(ptr);
            v32 = ptr[2];
            v33 = ptr[1] * p->field_e8;
            ptr[1] = v33;
            v34 = p->field_e4;
            if (!g_1fab3df)
            {
                sub_f7d92c("_F");
                g_1fab3df = 1;
            }
            v35 = g_1ef07e8;
            if (!g_1ef07e8->field_e0)
                v35 = sub_f7da5c(g_1ef07e8);
            v36 = [D] unsupported_Iop_SqrtF32();
            *(ptr) = v31;
            ptr[1] = v33 + v36 * v34;
            ptr[2] = v32;
            return v35;
        }
    }
    sub_f7db74(v7);
}
```

## `UiParticles.EvaluateQuadUVs` — RVA `0xccd518`

- Decompiled symbol: `UiParticles_EvaluateQuadUVs`
- Metadata signature: `private void EvaluateQuadUVs(Vector2[] uvs) { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    unsigned long long field_20;
    unsigned long long field_28;
    unsigned long long field_30;
    unsigned long long field_38;
} struct_0;

void UiParticles_EvaluateQuadUVs(unsigned long a0, struct_0 *ptr)
{
    unsigned int flag;  // w8

    if (ptr)
    {
        flag = ptr->field_18;
        if (flag)
        {
            ptr->field_20 = 0;
            if (flag != 1)
            {
                ptr->field_28 = 0x3f80000000000000;
                if (flag > 2)
                {
                    ptr->field_30 = 0x3f8000003f800000;
                    if (flag != 3)
                    {
                        ptr->field_38 = 0x3f800000;
                        return;
                    }
                }
            }
        }
        sub_f7db7c();
    }
    sub_f7db74();
}
```

## `UiParticles.EvaluateTexturesheetUVs` — RVA `0xccd574`

- Decompiled symbol: `UiParticles_EvaluateTexturesheetUVs`
- Metadata signature: `private void EvaluateTexturesheetUVs(ParticleSystem.Particle particle, float timeAlive, Vector2[] uvs) { }`
- Native interval: `688` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x10cd574: sub sp, sp, #0x90
// 0x10cd578: stp d9, d8, [sp, #0x40]
// 0x10cd57c: str x30, [sp, #0x50]
// 0x10cd580: stp x24, x23, [sp, #0x60]
// 0x10cd584: stp x22, x21, [sp, #0x70]
// 0x10cd588: stp x20, x19, [sp, #0x80]
// 0x10cd58c: mov v8.16b, v0.16b
// 0x10cd590: movi v0.2d, #0000000000000000
// 0x10cd594: stp q0, q0, [sp, #0x20]
// 0x10cd598: ldr x0, [x0, #0xd8]
// 0x10cd59c: cbz x0, #0x10cd820
// 0x10cd5a0: mov x20, x1
// 0x10cd5a4: mov x1, xzr
// 0x10cd5a8: mov x19, x2
// 0x10cd5ac: bl #0x1bc9d04
// 0x10cd5b0: str x0, [sp, #0x58]
// 0x10cd5b4: mov x0, x20
// 0x10cd5b8: mov x1, xzr
// 0x10cd5bc: bl #0x1bca450
// 0x10cd5c0: add x0, sp, #0x58
// 0x10cd5c4: mov x1, xzr
// 0x10cd5c8: mov v9.16b, v0.16b
// 0x10cd5cc: bl #0x1bca338
// 0x10cd5d0: scvtf s0, w0
// 0x10cd5d4: fdiv s9, s9, s0
// 0x10cd5d8: mov v0.16b, v8.16b
// 0x10cd5dc: mov v1.16b, v9.16b
// 0x10cd5e0: bl #0x1db0cb0
// 0x10cd5e4: add x0, sp, #0x58
// 0x10cd5e8: mov x1, xzr
// 0x10cd5ec: fdiv s8, s0, s9
// 0x10cd5f0: bl #0x1bca168
// 0x10cd5f4: mov w21, w0
// 0x10cd5f8: add x0, sp, #0x58
// 0x10cd5fc: mov x1, xzr
// 0x10cd600: bl #0x1bca0f0
// 0x10cd604: mov w22, w0
// 0x10cd608: mov x8, sp
// 0x10cd60c: add x0, sp, #0x58
// 0x10cd610: mov x1, xzr
// 0x10cd614: bl #0x1bca294
// 0x10cd618: ldp q0, q1, [sp]
// 0x10cd61c: add x0, sp, #0x20
// 0x10cd620: mov x1, xzr
// 0x10cd624: stp q0, q1, [sp, #0x20]
// 0x10cd628: mov v0.16b, v8.16b
// 0x10cd62c: bl #0x1bca510
// 0x10cd630: add x0, sp, #0x58
// 0x10cd634: mov x1, xzr
// 0x10cd638: mov v8.16b, v0.16b
// 0x10cd63c: bl #0x1bca1e0
// 0x10cd640: cmp w0, #1
// 0x10cd644: b.eq #0x10cd67c
// 0x10cd648: fmov s9, wzr
// 0x10cd64c: cbnz w0, #0x10cd728
// 0x10cd650: mul w8, w22, w21
// 0x10cd654: scvtf s0, w8
// 0x10cd658: fmul s0, s8, s0
// 0x10cd65c: frintm s0, s0
// 0x10cd660: fcmp s0, #0.0
// 0x10cd664: b.mi #0x10cd728
// 0x10cd668: sub w8, w8, #1
// 0x10cd66c: scvtf s1, w8
// 0x10cd670: fcmp s0, s1
// 0x10cd674: fcsel s9, s1, s0, gt
// 0x10cd678: b #0x10cd728
// 0x10cd67c: add x0, sp, #0x58
// 0x10cd680: mov x1, xzr
// 0x10cd684: bl #0x1bca0f0
// 0x10cd688: scvtf s0, w0
// 0x10cd68c: fmul s0, s8, s0
// 0x10cd690: add x0, sp, #0x58
// 0x10cd694: mov x1, xzr
// 0x10cd698: frintm s8, s0
// 0x10cd69c: bl #0x1bca0f0
// 0x10cd6a0: sub w8, w0, #1
// 0x10cd6a4: scvtf s0, w8
// 0x10cd6a8: fcmp s8, s0
// 0x10cd6ac: fcsel s0, s0, s8, gt
// 0x10cd6b0: fcmp s8, #0.0
// 0x10cd6b4: fmov s1, wzr
// 0x10cd6b8: add x0, sp, #0x58
// 0x10cd6bc: mov x1, xzr
// 0x10cd6c0: fcsel s8, s0, s1, pl
// 0x10cd6c4: bl #0x1bca3b0
// 0x10cd6c8: mov w21, w0
// 0x10cd6cc: add x0, sp, #0x58
// 0x10cd6d0: mov x1, xzr
// 0x10cd6d4: bl #0x1bc9ff4
// 0x10cd6d8: tbz w0, #0, #0x10cd710
// 0x10cd6dc: mov x0, x20
// 0x10cd6e0: mov x1, xzr
// 0x10cd6e4: bl #0x1bca458
// 0x10cd6e8: mov x1, xzr
// 0x10cd6ec: bl #0x1b900f0
// 0x10cd6f0: add x0, sp, #0x58
// 0x10cd6f4: mov x1, xzr
// 0x10cd6f8: bl #0x1bca168
// 0x10cd6fc: mov w1, w0
// 0x10cd700: mov w0, wzr
// 0x10cd704: mov x2, xzr
// 0x10cd708: bl #0x1b9016c
// 0x10cd70c: mov w21, w0
// 0x10cd710: add x0, sp, #0x58
// 0x10cd714: mov x1, xzr
// 0x10cd718: bl #0x1bca0f0
// 0x10cd71c: mul w8, w0, w21
// 0x10cd720: scvtf s0, w8
// 0x10cd724: fadd s9, s8, s0
// 0x10cd728: add x0, sp, #0x58
// 0x10cd72c: mov x1, xzr
// 0x10cd730: bl #0x1bca0f0
// 0x10cd734: mov w8, #0x7f800000
// 0x10cd738: fmov s0, w8
// 0x10cd73c: mov w20, w0
// 0x10cd740: fcvtzs w9, s9
// 0x10cd744: fcmp s9, s0
// 0x10cd748: mov w8, #-0x80000000
// 0x10cd74c: add x0, sp, #0x58
// 0x10cd750: mov x1, xzr
// 0x10cd754: csel w24, w8, w9, eq
// 0x10cd758: bl #0x1bca0f0
// 0x10cd75c: mov w21, w0
// 0x10cd760: add x0, sp, #0x58
// 0x10cd764: mov x1, xzr
// 0x10cd768: bl #0x1bca0f0
// 0x10cd76c: mov w22, w0
// 0x10cd770: add x0, sp, #0x58
// 0x10cd774: mov x1, xzr
// 0x10cd778: bl #0x1bca168
// 0x10cd77c: mov w23, w0
// 0x10cd780: add x0, sp, #0x58
// 0x10cd784: mov x1, xzr
// 0x10cd788: bl #0x1bca168
// 0x10cd78c: cbz x19, #0x10cd820
// 0x10cd790: ldr w8, [x19, #0x18]
// 0x10cd794: cbz w8, #0x10cd81c
// 0x10cd798: sdiv w9, w24, w20
// 0x10cd79c: sdiv w10, w24, w21
// 0x10cd7a0: scvtf s0, w22
// 0x10cd7a4: fmov s2, #1.00000000
// 0x10cd7a8: msub w9, w9, w20, w24
// 0x10cd7ac: mvn w10, w10
// 0x10cd7b0: scvtf s3, w23
// 0x10cd7b4: fdiv s1, s2, s0
// 0x10cd7b8: add w10, w0, w10
// 0x10cd7bc: scvtf s0, w9
// 0x10cd7c0: fdiv s3, s2, s3
// 0x10cd7c4: fmul s2, s1, s0
// 0x10cd7c8: scvtf s0, w10
// 0x10cd7cc: cmp w8, #1
// 0x10cd7d0: fmul s0, s3, s0
// 0x10cd7d4: stp s2, s0, [x19, #0x20]
// 0x10cd7d8: b.eq #0x10cd81c
// 0x10cd7dc: fadd s3, s3, s0
// 0x10cd7e0: cmp w8, #2
// 0x10cd7e4: stp s2, s3, [x19, #0x28]
// 0x10cd7e8: b.ls #0x10cd81c
// 0x10cd7ec: fadd s1, s1, s2
// 0x10cd7f0: cmp w8, #3
// 0x10cd7f4: stp s1, s3, [x19, #0x30]
// 0x10cd7f8: b.eq #0x10cd81c
// 0x10cd7fc: stp s1, s0, [x19, #0x38]
// 0x10cd800: ldp x20, x19, [sp, #0x80]
// 0x10cd804: ldp x22, x21, [sp, #0x70]
// 0x10cd808: ldp x24, x23, [sp, #0x60]
// 0x10cd80c: ldr x30, [sp, #0x50]
// 0x10cd810: ldp d9, d8, [sp, #0x40]
// 0x10cd814: add sp, sp, #0x90
// 0x10cd818: ret
// 0x10cd81c: bl #0xf7db7c
// 0x10cd820: bl #0xf7db74
```

## `UiParticles.ctor` — RVA `0xccd824`

- Decompiled symbol: `UiParticles_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[228];
    unsigned long long field_e4;
} struct_0;

long long UiParticles_ctor(struct_0 *ptr)
{
    *((unsigned long long *)&(&ptr->padding_0)[1]) = 0x3f8000003f800000;
}
```
