# Native pseudocode: ArrowObject

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ArrowObject.Start` — RVA `0xcacce4`

- Decompiled symbol: `ArrowObject_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

typedef struct struct_1 {
    char padding_0[72];
    long long field_48;
} struct_1;

extern long long g_1efcf38;
extern long long g_1efcf98;
extern char g_1fab4c6;

void ArrowObject_Start(struct_1 *ptr)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_0 *v6;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab4c6 & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efcf98);
        g_1fab4c6 = 1;
    }
    if (Camera__get_main(0) && Component__get_transform())
    {
        v6 = sub_1231bc8();
        if (v6 && v6->field_28 && GameObject__get_transform(v6->field_28, 0))
        {
            ptr->field_48 = sub_1231bc8();
            sub_f7d8d0();
            return;
        }
    }
    sub_f7db74();
}
```

## `ArrowObject.InitializeProjectile` — RVA `0xcacd88`

- Decompiled symbol: `ArrowObject_InitializeProjectile`
- Metadata signature: `public void InitializeProjectile() { }`
- Native interval: `584` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ArrowObject_Recovered` matched 8 offsets against `ArrowObject` metadata (confidence 0.80).

```c
typedef struct ArrowObject_Recovered {
    struct ArrowObject_Recovered *field_0;
    char padding_8[24];
    struct ArrowObject_Recovered *myRigidbody;
    struct ArrowObject_Recovered *myMeshRenderer;
    unsigned short hit;
    char padding_32[30];
    struct ArrowObject_Recovered *AmmoPickupComponent;
    char padding_58[4];
    unsigned int startTime;
    char padding_60[24];
    long long myBoxCol;
    long long emptyObject;
    char padding_88[12];
    unsigned int initialColSize;
    char padding_98[32];
    struct struct_1 *field_b8;
} ArrowObject_Recovered;

typedef struct struct_1 {
    long long field_0;
} struct_1;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

extern char g_10acfd0;
extern struct_2 *g_1ef0c58;
extern long long g_1efcf00;
extern long long g_1efcf20;
extern long long g_1efd018;
extern long long g_1efd080;
extern struct_0 g_1fab000;
extern char g_1fab4c7;
extern char g_1fab4c8;

long long ArrowObject_InitializeProjectile(struct_0 *a0)
{
    unsigned long long v4;  // x22
    struct_0 *p;  // x21
    struct_0 *ptr3;  // x21
    struct_0 *v15;  // x0
    struct_0 *ptr4;  // x22
    struct_0 *ptr7;  // x22
    struct_0 *v18;  // x0
    struct_0 *v19;  // x19
    long long v20;  // x0
    unsigned long v21;  // x0
    unsigned long v22;  // x20
    unsigned long v23;  // x0
    struct_0 *ptr;  // x19
    unsigned long long v24;  // x0
    struct_0 *v7;  // x0
    struct_0 *ptr5;  // x20
    struct_0 *addr;  // x20
    unsigned long v10;  // x0
    struct_0 *v11;  // x0
    struct_0 *ptr6;  // x20
    long long v13;  // x0
    unsigned long v0;  // [bp-0x20], Other Possible Types: unsigned long long
    struct_0 *v1;  // [bp-0x18]
    struct_0 *v2;  // [bp-0x10]
    struct_0 *v3;  // [bp-0x8]

    v0 = v4;
    p = &g_1fab000.field_0;
    ptr = a0;
    if (!(g_1fab4c7 & 1))
    {
        sub_f7d92c("s.");
        sub_f7d92c(&g_1efcf00);
        sub_f7d92c(&g_1efcf20);
        sub_f7d92c(&g_1efd018);
        sub_f7d92c(&g_1efd080);
        sub_f7d92c("M%");
        g_1fab4c7 = 1;
    }
    ptr->field_30 = 0;
    v7 = sub_1231bc8(ptr, g_1efcf00);
    ptr5 = ptr;
    ptr5->field_50 = v7;
    addr = &ptr5->field_50;
    sub_f7d8d0(addr, v7);
    v10 = addr->field_0;
    if (v10)
    {
        Behaviour__set_enabled(v10, 0, 0);
        v11 = sub_1231bc8(ptr, g_1efd080);
        ptr6 = ptr;
        ptr6->field_20 = v11;
        addr = &ptr6->field_20;
        sub_f7d8d0(addr, v11);
        v13 = sub_1231bc8(ptr, g_1efcf20);
        ptr3 = ptr;
        ptr3->field_78 = v13;
        p = &ptr3->field_78;
        sub_f7d8d0(p, v13);
        v15 = sub_1231bc8(ptr, g_1efd018);
        ptr4 = ptr;
        ptr4->field_28 = v15;
        ptr7 = &ptr4->field_28;
        sub_f7d8d0(ptr7, v15);
        v10 = ptr7->field_0;
        if (v10 && !((Renderer__set_enabled(v10, 0, 0), v10 = (unsigned long)p->field_0, !v10)))
        {
            BoxCollider__set_size(v10, 0);
            Time__get_time(0);
            v10 = ptr->field_20;
            ptr->field_5c = ptr->field_94;
            if (v10 && !((Rigidbody__set_isKinematic(v10, 0, 0), v10 = (unsigned long)addr->field_0, !v10 || (Rigidbody__set_interpolation(v10, 1, 0), v10 = (unsigned long)p->field_0, !v10))))
            {
                Collider__set_isTrigger(v10, 1, 0);
                v10 = Component__get_transform(ptr, 0);
                if (v10 && !((v10 = (unsigned long)Component__get_gameObject(), !v10)))
                {
                    addr = "s.";
                    GameObject__set_tag();
                    v10 = Component__get_transform(ptr, 0);
                    if (g_1eeea08.field_0->field_b8->field_0 && !((addr = (struct_0 *)v10, v10 = (unsigned long)Component__get_transform(g_1eeea08.field_0->field_b8->field_0, 0), !addr)))
                    {
                        Transform__set_parent(addr, v10, 0);
                        v10 = Component__get_transform(ptr, 0);
                        if (v10)
                        {
                            Transform__set_localScale();
                            v18 = ptr;
                            addr = v2;
                            ptr = v3;
                            p = v1;
                            goto LABEL_10acfd0;
                        }
                    }
                }
            }
        }
    }
    vvar_234{r256|8b} = (int)&g_10acfd0;
    v18 = sub_f7db74(v10);
LABEL_10acfd0:
    v0 = vvar_40{r256|8b};
    v1 = p;
    v2 = addr;
    v3 = ptr;
    v19 = v18;
    if (!(g_1fab4c8 & 1))
    {
        sub_f7d92c("s.");
        sub_f7d92c(&g_1ef0c58);
        g_1fab4c8 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v20 = Object__op_Inequality(v19->field_80, 0, 0);
    if (!((char)v20 & 1))
        return v20;
    v21 = Component__get_transform(v19, 0);
    if (g_1eeea08.field_0->field_b8->field_0)
    {
        v22 = v21;
        v23 = Component__get_transform(g_1eeea08.field_0->field_b8->field_0, 0);
        if (v22)
        {
            Transform__set_parent(v22, v23, 0);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v24 = Object__DestroyImmediate();
            return Object__DestroyImmediate();
        }
    }
    sub_f7db74();
}
```

## `ArrowObject.DeleteEmptyObj` — RVA `0xcacfd0`

- Decompiled symbol: `ArrowObject_DeleteEmptyObj`
- Metadata signature: `public void DeleteEmptyObj() { }`
- Native interval: `232` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x10acfd0: stp x30, x21, [sp, #-0x20]!
// 0x10acfd4: stp x20, x19, [sp, #0x10]
// 0x10acfd8: adrp x20, #0x1fab000
// 0x10acfdc: adrp x21, #0x1e8c000
// 0x10acfe0: ldrb w8, [x20, #0x4c8]
// 0x10acfe4: ldr x21, [x21, #0xd8]
// 0x10acfe8: mov x19, x0
// 0x10acfec: tbnz w8, #0, #0x10ad010
// 0x10acff0: adrp x0, #0x1e8e000
// 0x10acff4: ldr x0, [x0, #0x30]
// 0x10acff8: bl #0xf7d92c
// 0x10acffc: adrp x0, #0x1e8c000
// 0x10ad000: ldr x0, [x0, #0xd8]
// 0x10ad004: bl #0xf7d92c
// 0x10ad008: mov w8, #1
// 0x10ad00c: strb w8, [x20, #0x4c8]
// 0x10ad010: ldr x0, [x21]
// 0x10ad014: ldr x20, [x19, #0x80]
// 0x10ad018: ldr w8, [x0, #0xe0]
// 0x10ad01c: cbnz w8, #0x10ad024
// 0x10ad020: bl #0xf7da5c
// 0x10ad024: mov x0, x20
// 0x10ad028: mov x1, xzr
// 0x10ad02c: mov x2, xzr
// 0x10ad030: bl #0x1b94ac8
// 0x10ad034: tbz w0, #0, #0x10ad0a8
// 0x10ad038: adrp x20, #0x1e8e000
// 0x10ad03c: ldr x20, [x20, #0x30]
// 0x10ad040: mov x0, x19
// 0x10ad044: mov x1, xzr
// 0x10ad048: bl #0x1b92154
// 0x10ad04c: ldr x8, [x20]
// 0x10ad050: ldr x8, [x8, #0xb8]
// 0x10ad054: ldr x8, [x8]
// 0x10ad058: cbz x8, #0x10ad0b4
// 0x10ad05c: mov x20, x0
// 0x10ad060: mov x0, x8
// 0x10ad064: mov x1, xzr
// 0x10ad068: bl #0x1b92154
// 0x10ad06c: cbz x20, #0x10ad0b4
// 0x10ad070: mov x1, x0
// 0x10ad074: mov x0, x20
// 0x10ad078: mov x2, xzr
// 0x10ad07c: bl #0x1b9dcb4
// 0x10ad080: ldr x0, [x21]
// 0x10ad084: ldr x19, [x19, #0x80]
// 0x10ad088: ldr w8, [x0, #0xe0]
// 0x10ad08c: cbnz w8, #0x10ad094
// 0x10ad090: bl #0xf7da5c
// 0x10ad094: mov x0, x19
// 0x10ad098: ldp x20, x19, [sp, #0x10]
// 0x10ad09c: mov x1, xzr
// 0x10ad0a0: ldp x30, x21, [sp], #0x20
// 0x10ad0a4: b #0x1b98adc
// 0x10ad0a8: ldp x20, x19, [sp, #0x10]
// 0x10ad0ac: ldp x30, x21, [sp], #0x20
// 0x10ad0b0: ret
// 0x10ad0b4: bl #0xf7db74
```

## `ArrowObject.OnDrawGizmos` — RVA `0xcad0b8`

- Decompiled symbol: `ArrowObject_OnDrawGizmos`
- Metadata signature: `private void OnDrawGizmos() { }`
- Native interval: `328` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[160];
    char field_a0;
} struct_0;

void ArrowObject_OnDrawGizmos(struct_0 *a0)
{
    if (!a0->field_a0)
        return;
    Gizmos__set_color(0);
    if (Component__get_transform(a0, 0))
    {
        Transform__get_position();
        Gizmos__DrawSphere(0);
        Gizmos__set_color(0);
        if (Component__get_transform(a0, 0))
        {
            Transform__get_position();
            if (Component__get_transform(a0, 0))
            {
                Transform__get_forward();
                Gizmos__DrawSphere(0);
                Gizmos__set_color(0);
                RaycastHit__get_point((struct struct_0 *)&a0[1].padding_0[3], 0);
                Gizmos__DrawSphere();
                return;
            }
        }
    }
    sub_f7db74();
}
```

## `ArrowObject.Update` — RVA `0xcad200`

- Decompiled symbol: `ArrowObject_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `992` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ArrowObject_Recovered` matched 13 offsets against `ArrowObject` metadata (confidence 1.00).

```c
typedef struct struct_4 {
    char padding_0[224];
    unsigned int field_e0;
} struct_4;

typedef struct ArrowObject_Recovered {
    char padding_0[32];
    long long myRigidbody;
    long long myMeshRenderer;
    char hit;
    char falling;
    char padding_32[38];
    unsigned int hitTime;
    unsigned int startTime;
    char padding_60[4];
    unsigned int waitDuration;
    unsigned int objectPoolIndex;
    char padding_6c[4];
    long long hitCol;
    long long myBoxCol;
    long long emptyObject;
    char padding_88[76];
    unsigned int rayMask;
    char padding_d8[4];
    unsigned int visibleDelay;
} ArrowObject_Recovered;

typedef struct struct_5 {
    char padding_0[224];
    unsigned int field_e0;
} struct_5;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_1 *g_1ef0c58;
extern struct_2 *g_1ef0e48;
extern char g_1fab3df;
extern char g_1fab4c9;

struct_4 * ArrowObject_Update(struct_3 *ptr)
{
    unsigned int v0;  // s1
    unsigned int v1;  // s0
    unsigned int v10;  // w0
    struct_4 *v11;  // x0
    struct_5 *v12;  // x0
    unsigned int v13;  // s0
    unsigned long v14;  // 4205
    unsigned long v15;  // x0
    unsigned long long v17;  // x0
    unsigned long v2;  // 4138
    unsigned long v3;  // x0
    unsigned int v4;  // s1
    unsigned long v5;  // 4138
    unsigned long v6;  // x20
    struct_4 *v7;  // x0
    struct_4 *v8;  // x0
    struct_4 *v9;  // x0

    if (!(g_1fab4c9 & 1))
    {
        sub_f7d92c("s.");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef0e48);
        sub_f7d92c("s%");
        g_1fab4c9 = 1;
    }
    Time__get_time(0);
    v0 = ptr->field_5c + ptr->field_dc;
    v2 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) & ((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v2))
    {
        v3 = ptr->field_28;
        if (v3)
        {
            Renderer__set_enabled(v3, 1, 0);
            goto LABEL_10ad294;
        }
    }
    else
    {
LABEL_10ad294:
        if (ptr->field_30)
        {
            Time__get_time(0);
            v4 = ptr->field_58 + ptr->field_64;
            v5 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v4, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v1) & 1)) & ((unsigned long long)(char)(CmpF(v4, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v5))
            {
                v3 = Component__get_transform(ptr, 0);
                if (*((long long *)g_1eeea08->field_b8) && (v6 = v3, v3 = (unsigned long)Component__get_transform(*((long long *)g_1eeea08->field_b8), 0), v6))
                {
                    Transform__set_parent(v6, v3, 0);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    Object__DestroyImmediate(ptr->field_80, 0);
                    v3 = Component__get_transform(ptr, 0);
                    if (v3 && (v3 = (unsigned long)Component__get_gameObject(), *((long long *)g_1eeea08->field_b8)))
                    {
                        AzuObjectPool__RecyclePooledObj(*((long long *)g_1eeea08->field_b8), ptr->field_68, v3);
                        goto LABEL_10ad368;
                    }
                }
            }
            else
            {
LABEL_10ad368:
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v7 = Object__op_Implicit(ptr->field_70, 0);
                if (!((char)v7 & 1))
                    return v7;
                v3 = ptr->field_70;
                if (v3)
                {
                    v8 = Collider__get_enabled(v3, 0);
                    if (((char)v8 & 1))
                        return v8;
                    v3 = ptr->field_20;
                    if (v3)
                    {
                        Rigidbody__set_isKinematic(v3, 0, 0);
                        v3 = ptr->field_20;
                        if (v3)
                        {
                            Rigidbody__set_interpolation(v3, 1, 0);
                            v3 = ptr->field_78;
                            if (v3)
                            {
                                Collider__set_isTrigger(v3, 0, 0);
                                v3 = Component__get_transform(ptr, 0);
                                if (v3)
                                {
                                    v3 = Component__get_gameObject();
                                    if (v3)
                                    {
                                        v9 = GameObject__set_tag();
                                        ptr->field_31 = 1;
                                        return v9;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        else
        {
            v3 = Component__get_transform(ptr, 0);
            if (v3)
            {
                Transform__get_position();
                v3 = Component__get_transform(ptr, 0);
                if (v3)
                {
                    Transform__get_forward();
                    v10 = LayerMask__op_Implicit(ptr->field_d4, 0);
                    if (!g_1ef0e48->field_e0)
                        sub_f7da5c(g_1ef0e48);
                    v11 = Physics__Raycast(&ptr->padding_88[28], v10, 1, 0);
                    if (((char)v11 & 1))
                        v11 = ArrowObject__HitTarget();
                    if (ptr->field_31)
                        return v11;
                    v3 = ptr->field_20;
                    if (v3)
                    {
                        Rigidbody__get_velocity(v3, 0);
                        if (!g_1fab3df)
                        {
                            sub_f7d92c("_F");
                            g_1fab3df = 1;
                        }
                        v12 = g_1ef07e8;
                        if (!g_1ef07e8->field_e0)
                            v12 = sub_f7da5c(g_1ef07e8);
                        v13 = [D] unsupported_Iop_SqrtF32();
                        v14 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v13, 1008981770)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 1008981770) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v13, 1008981770)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 1008981770) & 1)) & ((unsigned long long)(char)(CmpF(v13, 1008981770)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 1008981770) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v14)
                            return v12;
                        v15 = Component__get_transform(ptr, 0);
                        v3 = v15;
                        if (ptr->field_20)
                        {
                            Rigidbody__get_velocity(ptr->field_20, 0);
                            v3 = Quaternion__LookRotation(0);
                            if (v15)
                            {
                                v17 = Transform__set_rotation();
                                return Transform__set_rotation();
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v3);
}
```

## `ArrowObject.HitTarget` — RVA `0xcad5e0`

- Decompiled symbol: `ArrowObject_HitTarget`
- Metadata signature: `private void HitTarget() { }`
- Native interval: `3332` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ArrowObject_Recovered` matched 2 offsets against `ArrowObject` metadata (confidence 1.00).

```c
typedef struct ArrowObject_Recovered {
    char padding_0[96];
    struct struct_9 *startState;
    char padding_68[32];
    unsigned long long scale;
} ArrowObject_Recovered;

typedef struct struct_7 {
    char padding_0[568];
    unsigned long long field_238;
} struct_7;

typedef struct struct_3 {
    char padding_0[32];
    long long field_20;
} struct_3;

typedef struct struct_9 {
    char padding_0[568];
    unsigned long long field_238;
} struct_9;

typedef struct struct_6 {
    unsigned int field_0;
} struct_6;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_5 {
    char padding_0[184];
    struct struct_6 *field_b8;
} struct_5;

extern long long g_1eefaf0;
extern struct_0 *g_1ef0c58;
extern struct_5 *g_1ef22e8;
extern unsigned long long g_1efd080;
extern long long g_1efeb10;
extern long long g_1efeb30;
extern long long g_1efeb38;
extern long long g_1efeb48;
extern long long g_1efeb90;
extern long long g_1efebb0;
extern long long g_1efec38;
extern long long g_1efec58;
extern char g_1fab2c8;
extern char g_1fab2c9;
extern char g_1fab4ca;

void* ArrowObject_HitTarget(void* ptr)
{
    void* v1;  // x0
    void* v2;  // x0
    void* ptr3;  // x21
    unsigned int v12;  // s0
    long long v13;  // x22
    long long v14;  // x0
    long long v15;  // x0
    long long v16;  // x0
    long long v17;  // x0
    unsigned long v18;  // x0
    unsigned long v19;  // x8
    unsigned long v20;  // x1
    void* v3;  // x0
    unsigned long v21;  // x0
    long long v22;  // x0
    long long v23;  // x0
    long long v24;  // x22
    long long v25;  // x23
    void* p;  // x22
    void* v27;  // x22
    long long v28;  // x23
    long long v29;  // x0
    long long v30;  // x23
    void* v4;  // x20
    long long v31;  // x0
    long long v32;  // x23
    unsigned long v33;  // x0
    unsigned long v34;  // x0
    unsigned long v35;  // x23
    long long v36;  // x0
    long long v37;  // x0
    long long v39;  // x0
    unsigned int v40;  // w0
    unsigned long v5;  // x0
    unsigned long v41;  // x0
    long long v42;  // x0
    unsigned int v43;  // w0
    long long v44;  // x0
    unsigned int v45;  // w0
    unsigned long v46;  // x0
    long long v47;  // x0
    unsigned long v48;  // x0
    long long v49;  // x0
    unsigned long v50;  // x0
    void* v6;  // x0
    long long v51;  // x0
    long long v52;  // x22
    unsigned long v53;  // x0
    long long v54;  // x0
    struct_3 *v55;  // x0
    long long v56;  // x22
    unsigned long v57;  // x0
    unsigned long v58;  // x0
    unsigned long v59;  // x22
    long long v7;  // x0
    unsigned int v60;  // s2
    unsigned long v61;  // 4205
    unsigned int v62;  // s0
    void* v63;  // x0
    void* v8;  // x0
    unsigned long v9;  // x0
    void* addr;  // x21
    unsigned int v0;  // [bp-0x34]

    v1 = ptr;
    if (!(g_1fab4ca & 1))
    {
        sub_f7d92c(&g_1efd080);
        sub_f7d92c(&g_1efeb10);
        sub_f7d92c(&g_1efeb30);
        sub_f7d92c(&g_1efeb38);
        sub_f7d92c(&g_1efeb48);
        sub_f7d92c(&g_1efeb90);
        sub_f7d92c(&g_1efebb0);
        sub_f7d92c(&g_1efec38);
        sub_f7d92c(&g_1efec58);
        sub_f7d92c(&g_1eefaf0);
        sub_f7d92c(&g_1ef0c58);
        v2 = sub_f7d92c("s%");
        g_1fab4ca = 1;
        v1 = v2;
    }
    v3 = v1;
    if ((char)ptr[48])
        return v3;
    v4 = ptr + 164;
    v5 = RaycastHit__get_collider(v4, 0);
    if ((long long)ptr[72] && *((long long *)((long long)ptr[72] + 96)))
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v6 = Object__op_Inequality(v5, *((long long *)(*((long long *)((long long)ptr[72] + 96)) + 568)), 0);
        if (!((char)v6 & 1))
            return v6;
        if (RaycastHit__get_collider(v4, 0) && Component__get_gameObject())
        {
            v7 = sub_1249224();
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v8 = Object__op_Implicit(v7, 0);
            if (((char)v8 & 1))
                return v8;
            v9 = RaycastHit__get_collider(v4, 0);
            addr = ptr;
            *((unsigned long *)&addr[112]) = v9;
            ptr3 = addr + 112;
            sub_f7d8d0(ptr3, v9);
            if ((long long)ptr3[80] && (Rigidbody__set_isKinematic((long long)ptr3[80], 1, 0), (long long)ptr[32] && (Rigidbody__set_interpolation((long long)ptr[32], 0, 0), Component__get_transform(ptr, 0) && Component__get_gameObject() && (GameObject__set_tag(), (long long)ptr[120] && (v12 = (int)ptr[148] * 2, BoxCollider__set_size((long long)ptr[120], 0), (long long)ptr[80])))))
            {
                Behaviour__set_enabled((long long)ptr[80], 1, 0);
                v13 = Component__get_transform(ptr, 0);
                RaycastHit__get_point(v4, 0);
                if (v13 && (Transform__set_position(v13, 0), *((long long *)ptr3)))
                {
                    v14 = sub_1231bc8(*((long long *)ptr3), g_1efd080);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (((char)Object__op_Implicit(v14, 0) & 1))
                    {
LABEL_10ad908:
                        if (*((long long *)ptr3))
                        {
                            v17 = sub_1231bc8(*((long long *)ptr3), g_1efd080);
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            v18 = Object__op_Implicit(v17, 0);
                            v19 = *((long long *)ptr3);
                            if (v19)
                            {
                                if (((char)v18 & 1))
                                {
                                    v20 = g_1efd080;
                                    v21 = v19;
                                }
                                if (Component__get_transform(v19, 0))
                                {
                                    v22 = Transform__get_parent();
                                    if (!g_1ef0c58->field_e0)
                                        sub_f7da5c(g_1ef0c58);
                                    if (((char)Object__op_Inequality(v22, 0, 0) & 1))
                                    {
                                        if (*((long long *)ptr3) && Component__get_transform(*((long long *)ptr3), 0) && Transform__get_parent())
                                        {
                                            v23 = sub_1231bc8();
                                            if (!g_1ef0c58->field_e0)
                                                sub_f7da5c(g_1ef0c58);
                                            if (!(Object__op_Implicit(v23, 0) & 1))
                                                goto LABEL_10ada54;
                                            if (*((long long *)ptr3) && Component__get_transform(*((long long *)ptr3), 0) && (v21 = (unsigned long)Transform__get_parent(), Transform__get_parent()) && (v20 = (unsigned long)g_1efd080, v24 = sub_1231bc8(v21, v20), Component__get_transform(ptr, 0) && (Transform__get_forward(), v24)))
                                            {
                                                Rigidbody__AddForce(v24, 1, 0);
                                                goto LABEL_10ada54;
                                            }
                                        }
                                    }
                                    else
                                    {
LABEL_10ada54:
                                        v25 = sub_f7db70(g_1eefaf0);
                                        GameObject__ctor(v25, 0);
                                        p = ptr;
                                        *((long long *)&p[128]) = v25;
                                        v27 = p + 128;
                                        sub_f7d8d0(v27, v25);
                                        if (*((long long *)v27))
                                        {
                                            v28 = GameObject__get_transform(*((long long *)v27), 0);
                                            RaycastHit__get_point(v4, 0);
                                            if (v28 && (Transform__set_position(v28, 0), *((long long *)v27) && (v29 = (long long)(unsigned long long)GameObject__get_transform(*((long long *)v27), 0), *((long long *)ptr3) && (v30 = (long long)(unsigned long long)GameObject__get_transform(*((long long *)v27), 0), Component__get_transform(*((long long *)ptr3), 0) && (Transform__get_rotation(), v30 && (Transform__set_rotation(v30, 0), *((long long *)v27) && (v31 = (long long)(unsigned long long)GameObject__get_transform(*((long long *)v27), 0), *((long long *)ptr3) && (v32 = (long long)(unsigned long long)GameObject__get_transform(*((long long *)v27), 0), v33 = (unsigned long)Component__get_transform(*((long long *)ptr3), 0), v32))))))))
                                            {
                                                Transform__set_parent(v32, Component__get_transform(*((long long *)ptr3), 0), 0);
                                                v34 = Component__get_transform(ptr, 0);
                                                if ((long long)ptr[128] && (v35 = v34, v36 = (long long)(unsigned long long)GameObject__get_transform((long long)ptr[128], 0), v35 && (Transform__set_parent(v35, (unsigned long long)GameObject__get_transform((long long)ptr[128], 0), 0), *((long long *)v27))))
                                                {
                                                    v37 = GameObject__get_gameObject(*((long long *)v27), 0);
                                                    if (!g_1ef0c58->field_e0)
                                                        sub_f7da5c(g_1ef0c58);
                                                    v12 = (int)ptr[100] + 0x3f800000;
                                                    Object__Destroy(v37, 0);
LABEL_10adbac:
                                                    if (*((long long *)ptr3) && Component__get_gameObject(*((long long *)ptr3), 0))
                                                    {
                                                        switch ((unsigned int)GameObject__get_layer())
                                                        {
                                                        case 13:
                                                            if (*((long long *)ptr3) && Component__get_gameObject(*((long long *)ptr3), 0))
                                                            {
                                                                v51 = sub_1249224();
                                                                if (!g_1ef0c58->field_e0)
                                                                    sub_f7da5c(g_1ef0c58);
                                                                if (((char)Object__op_Implicit(v51, 0) & 1))
                                                                {
                                                                    if (*((long long *)ptr3) && Component__get_gameObject(*((long long *)ptr3), 0) && sub_1249224())
                                                                    {
                                                                        if (!(Behaviour__get_enabled() & 1))
                                                                            goto LABEL_10addbc;
                                                                        if (*((long long *)ptr3) && Component__get_gameObject(*((long long *)ptr3), 0) && (v52 = sub_1249224(), Component__get_transform(ptr, 0) && (Transform__get_forward(), (unsigned long long)Camera__get_main(0) && Component__get_transform())))
                                                                        {
                                                                            Transform__get_position();
                                                                            v53 = Component__get_transform(ptr, 0);
                                                                            if (v52 && (v12 = (unsigned int)((int)ptr[52] + (int)ptr[64]), CharacterDamage__ApplyDamage(v52, v53, 1, 0, 0, 0), (long long)ptr[72]))
                                                                            {
                                                                                FPSPlayer__UpdateHitTime((long long)ptr[72], 0);
                                                                                goto LABEL_10addbc;
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                                else
                                                                {
LABEL_10addbc:
                                                                    if (*((long long *)ptr3) && Component__get_gameObject(*((long long *)ptr3), 0))
                                                                    {
                                                                        v54 = sub_1249224();
                                                                        if (!g_1ef0c58->field_e0)
                                                                            sub_f7da5c(g_1ef0c58);
                                                                        if (((char)Object__op_Implicit(v54, 0) & 1))
                                                                        {
                                                                            if (*((long long *)ptr3) && Component__get_gameObject(*((long long *)ptr3), 0) && (v55 = (struct_3 *)sub_1249224(), v55 && v55->field_20))
                                                                            {
                                                                                if (!(Behaviour__get_enabled(v55->field_20, 0) & 1))
                                                                                    goto LABEL_10adf08;
                                                                                if (*((long long *)ptr3) && Component__get_gameObject(*((long long *)ptr3), 0) && (v56 = sub_1249224(), Component__get_transform(ptr, 0) && (Transform__get_forward(), (unsigned long long)Camera__get_main(0) && Component__get_transform())))
                                                                                {
                                                                                    Transform__get_position();
                                                                                    v57 = Component__get_transform(ptr, 0);
                                                                                    if (v56 && (v12 = (unsigned int)((int)ptr[52] + (int)ptr[64]), LocationDamage__ApplyDamage(v56, v57, 1, 0, 0), (long long)ptr[72]))
                                                                                    {
                                                                                        FPSPlayer__UpdateHitTime((long long)ptr[72], 0);
                                                                                        goto LABEL_10adf08;
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                        else
                                                                        {
LABEL_10adf08:
                                                                            v58 = Component__get_transform(ptr, 0);
                                                                            if ((long long)ptr[112] && (v59 = v58, Component__get_transform((long long)ptr[112], 0) && (Transform__get_position(), v0 = v12, *((long long *)ptr3) && Component__get_transform(*((long long *)ptr3), 0))))
                                                                            {
                                                                                Transform__get_position();
                                                                                RaycastHit__get_point(v4, 0);
                                                                                if (!g_1fab2c8)
                                                                                {
                                                                                    sub_f7d92c("_F");
                                                                                    g_1fab2c8 = 1;
                                                                                }
                                                                                if (!g_1ef07e8->field_e0)
                                                                                    sub_f7da5c(g_1ef07e8);
                                                                                v60 = [D] unsupported_Iop_SqrtF32();
                                                                                v61 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v60, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v60, 925353388) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v60, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v60, 925353388) & 1)) & ((unsigned long long)(char)(CmpF(v60, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v60, 925353388) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                                                if (!((char)v61))
                                                                                {
                                                                                    v62 = (v12 - v12) / v60;
                                                                                }
                                                                                else
                                                                                {
                                                                                    if (!g_1fab2c9)
                                                                                    {
                                                                                        sub_f7d92c(&g_1ef22e8);
                                                                                        g_1fab2c9 = 1;
                                                                                    }
                                                                                    v62 = g_1ef22e8->field_b8->field_0;
                                                                                }
                                                                                if (v59)
                                                                                {
                                                                                    v12 = v0 - v62 * 1041865114;
                                                                                    Transform__set_position(v59, 0);
                                                                                    goto LABEL_10ae158;
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                            break;
                                                        case 1:
                                                            if (*((long long *)ptr3) && Component__get_gameObject(*((long long *)ptr3), 0))
                                                            {
                                                                v49 = sub_1249224();
                                                                if (!g_1ef0c58->field_e0)
                                                                    sub_f7da5c(g_1ef0c58);
                                                                if (!(Object__op_Implicit(v49, 0) & 1))
                                                                    goto LABEL_10ae158;
                                                                if (*((long long *)ptr3) && Component__get_gameObject(*((long long *)ptr3), 0))
                                                                    goto LABEL_10ae0b8;
                                                                break;
                                                            }
                                                            break;
                                                        case 0:
                                                            if (*((long long *)ptr3) && Component__get_gameObject(*((long long *)ptr3), 0))
                                                            {
                                                                v39 = sub_1249224();
                                                                if (!g_1ef0c58->field_e0)
                                                                    sub_f7da5c(g_1ef0c58);
                                                                v40 = Object__op_Implicit(v39, 0);
                                                                if (*((long long *)ptr3) && Component__get_gameObject(*((long long *)ptr3), 0))
                                                                {
                                                                    if (((char)v40 & 1))
                                                                    {
                                                                        v41 = sub_1249224();
                                                                        if (v41)
                                                                        {
                                                                            v12 = (int)ptr[64] + (int)ptr[52];
                                                                            AppleFall__ApplyDamage(v41);
                                                                        }
                                                                    }
                                                                    else
                                                                    {
                                                                        v42 = sub_1249224();
                                                                        if (!g_1ef0c58->field_e0)
                                                                            sub_f7da5c(g_1ef0c58);
                                                                        v43 = Object__op_Implicit(v42, 0);
                                                                        if (*((long long *)ptr3) && Component__get_gameObject(*((long long *)ptr3), 0))
                                                                        {
                                                                            if (((char)v43 & 1))
                                                                            {
LABEL_10ae0b8:
                                                                                v50 = sub_1249224();
                                                                                if (v50)
                                                                                {
                                                                                    v12 = (int)ptr[64] + (int)ptr[52];
                                                                                    BreakableObject__ApplyDamage(v50);
                                                                                }
                                                                            }
                                                                            else
                                                                            {
                                                                                v44 = sub_1249224();
                                                                                if (!g_1ef0c58->field_e0)
                                                                                    sub_f7da5c(g_1ef0c58);
                                                                                v45 = Object__op_Implicit(v44, 0);
                                                                                if (*((long long *)ptr3) && Component__get_gameObject(*((long long *)ptr3), 0))
                                                                                {
                                                                                    if (((char)v45 & 1))
                                                                                    {
                                                                                        v46 = sub_1249224();
                                                                                        if (v46)
                                                                                            ExplosiveObject__ApplyDamage(v46);
                                                                                    }
                                                                                    else
                                                                                    {
                                                                                        v47 = sub_1249224();
                                                                                        if (!g_1ef0c58->field_e0)
                                                                                            sub_f7da5c(g_1ef0c58);
                                                                                        if (!(Object__op_Implicit(v47, 0) & 1))
                                                                                            goto LABEL_10ae158;
                                                                                        if (*((long long *)ptr3) && Component__get_gameObject(*((long long *)ptr3), 0) && (v48 = (unsigned long)sub_1249224(), v48) && (v12 = (unsigned int)((int)ptr[64] + (int)ptr[52]), MineExplosion__ApplyDamage(v48), (long long)ptr[72]))
                                                                                        {
                                                                                            FPSPlayer__UpdateHitTime((long long)ptr[72], 0);
                                                                                            goto LABEL_10ae158;
                                                                                        }
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                            break;
                                                        default:
LABEL_10ae158:
                                                            if ((long long)ptr[72])
                                                            {
                                                                RaycastHit__get_point(v4, 0);
                                                                RaycastHit__get_normal(v4, 0);
                                                                if (*((long long *)((long long)ptr[72] + 136)))
                                                                {
                                                                    WeaponEffects__ImpactEffects(*((long long *)((long long)ptr[72] + 136)), *((long long *)ptr3), 0, 1);
                                                                    v63 = Time__get_time(0);
                                                                    *((unsigned int *)&ptr[88]) = v12;
                                                                    *((char *)&ptr[48]) = 1;
                                                                    return v63;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                    else if (*((long long *)ptr3) && Component__get_transform(*((long long *)ptr3), 0))
                    {
                        v15 = Transform__get_parent();
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        if (!(Object__op_Inequality(v15, 0, 0) & 1))
                            goto LABEL_10adbac;
                        if (*((long long *)ptr3) && Component__get_transform(*((long long *)ptr3), 0) && Transform__get_parent())
                        {
                            v16 = sub_1231bc8();
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            if ((Object__op_Implicit(v16, 0) & 1))
                                goto LABEL_10ad908;
                            goto LABEL_10adbac;
                        }
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `ArrowObject.ctor` — RVA `0xcae2e4`

- Decompiled symbol: `ArrowObject_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `48` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ArrowObject_Recovered` matched 4 offsets against `ArrowObject` metadata (confidence 1.00).

```c
typedef struct ArrowObject_Recovered {
    char padding_0[52];
    unsigned long long damage;
    unsigned int force;
    char padding_40[36];
    unsigned int waitDuration;
    char padding_68[104];
    unsigned int hitCheckDist;
} ArrowObject_Recovered;

long long ArrowObject_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    *((unsigned int *)((char *)&ptr->field_34 + 4)) = 0x40400000;
    *((unsigned int *)&ptr->padding_40[32]) = 0x41f00000;
    *((unsigned long long *)&(&ptr->padding_0)[1]) = 0x41a0000042480000;
    *((unsigned int *)&ptr->padding_68[100]) = 1053609165;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
