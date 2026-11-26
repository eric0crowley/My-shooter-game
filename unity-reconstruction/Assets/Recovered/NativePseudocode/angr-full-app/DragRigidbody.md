# Native pseudocode: DragRigidbody

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DragRigidbody.Start` — RVA `0xc8ac8c`

- Decompiled symbol: `DragRigidbody_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `300` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DragRigidbody_Recovered` matched 6 offsets against `DragRigidbody` metadata (confidence 1.00).

```c
typedef struct DragRigidbody_Recovered {
    char padding_0[32];
    struct struct_1 *FPSWalkerComponent;
    char padding_28[8];
    long long FPSPlayerComponent;
    long long InputComponent;
    char padding_40[20];
    unsigned int reachDistance;
    unsigned int reachDistanceAmt;
    char padding_5c[68];
    long long mainCamTransform;
} DragRigidbody_Recovered;

typedef struct struct_0 {
    char padding_0[568];
    unsigned long long field_238;
    char padding_240[412];
    unsigned int field_3dc;
} struct_0;

typedef struct struct_1 {
    char padding_0[568];
    long long field_238;
    char padding_240[412];
    unsigned int field_3dc;
} struct_1;

extern long long g_1efcf98;
extern long long g_1efcfa0;
extern long long g_1efcfd8;
extern char g_1fab435;

unsigned long long DragRigidbody_Start(struct_2 *ptr4)
{
    struct_0 *v0;  // x1
    struct_2 *ptr;  // x0
    unsigned long long v10;  // x0
    unsigned int v11;  // s0
    long long v2;  // x1
    struct_2 *p;  // x0
    long long v4;  // x1
    struct_2 *addr;  // x0
    long long v6;  // x0
    struct_2 *ptr3;  // x20
    struct_2 *ptr5;  // x20
    struct_0 *pos;  // x8

    if (!(g_1fab435 & 1))
    {
        sub_f7d92c(&g_1efcf98);
        sub_f7d92c(&g_1efcfa0);
        sub_f7d92c(&g_1efcfd8);
        g_1fab435 = 1;
    }
    v0 = sub_1231bc8(ptr4, g_1efcfa0);
    ptr = ptr4;
    ptr->field_20 = v0;
    sub_f7d8d0((struct DragRigidbody_Recovered *)&ptr->field_20, v0);
    v2 = sub_1231bc8(ptr4, g_1efcf98);
    p = ptr4;
    p->field_30 = v2;
    sub_f7d8d0((struct DragRigidbody_Recovered *)&p->field_30, v2);
    v4 = sub_1231bc8(ptr4, g_1efcfd8);
    addr = ptr4;
    addr->field_38 = v4;
    sub_f7d8d0((struct DragRigidbody_Recovered *)&addr->field_38, v4);
    if (Camera__get_main(0))
    {
        v6 = Component__get_transform();
        ptr3 = ptr4;
        ptr3->field_a0 = v6;
        ptr5 = &ptr3->field_a0;
        sub_f7d8d0(ptr5, v6);
        pos = *((long long *)&ptr5->padding_5c[36]);
        if (pos && pos->field_238)
        {
            v10 = CapsuleCollider__get_height(pos->field_238, 0);
            ptr4->field_58 = *((int *)&ptr5->padding_40[12]) / (0x3f800000 - pos->field_3dc / v11);
            return v10;
        }
    }
    sub_f7db74();
}
```

## `DragRigidbody.Update` — RVA `0xc8adb8`

- Decompiled symbol: `DragRigidbody_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `1532` bytes
- Result: `pseudocode`

```c
typedef struct struct_13 {
    char padding_0[150];
    char field_96;
} struct_13;

typedef struct struct_12 {
    char padding_0[120];
    struct struct_11 *field_78;
    char padding_80[24];
    struct struct_9 *field_98;
    char padding_a0[364];
    unsigned int field_20c;
    char padding_210[164];
    unsigned int field_2b4;
    unsigned int field_2b8;
    char padding_2bc[1];
    char field_2bd;
    char padding_2be[18];
    char field_2d0;
} struct_12;

typedef struct struct_9 {
    char padding_0[262];
    char field_106;
} struct_9;

typedef struct struct_10 {
    char padding_0[1068];
    unsigned long long field_42c;
    unsigned int field_434;
} struct_10;

typedef struct struct_11 {
    char padding_0[1068];
    unsigned long long field_42c;
    unsigned int field_434;
} struct_11;

typedef struct struct_4 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
} struct_4;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_3 {
    char padding_0[184];
    struct struct_4 *field_b8;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eefaf0;
extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef0e48;
extern struct_3 *g_1ef22e8;
extern long long g_1efeaf0;
extern long long g_1efeaf8;
extern long long g_1f0d688;
extern char g_1fab2c8;
extern char g_1fab2c9;
extern char g_1fab436;

void* DragRigidbody_Update(void* ptr)
{
    void* v3;  // x0
    void* v4;  // x0
    unsigned int v13;  // s0
    unsigned long v14;  // 4129
    unsigned int v15;  // s3
    unsigned int v16;  // s2
    unsigned long v17;  // 4205
    unsigned int v18;  // s0
    unsigned int v19;  // s1
    unsigned int v20;  // s2
    unsigned int v21;  // s2
    unsigned int addr[3];  // x8
    void* v5;  // x0
    unsigned long ptr5;  // x8
    unsigned long v24;  // x8
    unsigned int v25;  // w0
    void* v26;  // x0
    long long v27;  // x0
    void* v28;  // x0
    void* v29;  // x0
    void* p;  // x21
    long long v31;  // x20
    long long v32;  // x20
    void* v6;  // x0
    long long v33;  // x0
    long long v34;  // x0
    long long v35;  // x20
    long long v36;  // x20
    long long v37;  // x0
    long long v38;  // x22
    unsigned long v39;  // x0
    struct_12 *ptr3;  // x8
    unsigned int v7;  // s1
    unsigned long v8;  // 4142
    void* v9;  // x0
    unsigned int v10;  // s1
    unsigned long v11;  // 4138
    struct_12 *ptr4;  // x8
    int choice;  // [bp-0xa0]
    uint128_t flag2;  // [bp-0x90]
    uint128_t flag;  // [bp-0x84]

    v3 = ptr;
    if (!(g_1fab436 & 1))
    {
        sub_f7d92c(&g_1efeaf0);
        sub_f7d92c(&g_1efeaf8);
        sub_f7d92c(&g_1eefaf0);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef0e48);
        v4 = sub_f7d92c(&g_1f0d688);
        g_1fab436 = 1;
        v3 = v4;
    }
    v5 = v3;
    flag = 0;
    choice = 0;
    flag2 = 0;
    if ((long long)ptr[56])
    {
        if (!*((char *)((long long)ptr[56] + 150)))
            return v5;
        if ((long long)ptr[48])
        {
            v6 = Time__get_time(0);
            v7 = *((int *)((long long)ptr[48] + 692)) + 1050253722;
            v8 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v7, 0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7, 0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0) & 1)) & ((unsigned long long)(char)(CmpF(v7, 0)) >> 5 & 3 | (unsigned long long)(CmpF(v7, 0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v8)
                return v6;
            if ((long long)ptr[48])
            {
                v9 = Time__get_time(0);
                v10 = *((int *)((long long)ptr[48] + 696)) + 1050253722;
                v11 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v10, 0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v10, 0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0) & 1)) & ((unsigned long long)(char)(CmpF(v10, 0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v11)
                    return v9;
                if ((char)ptr[120])
                    return v9;
                ptr4 = (long long)ptr[48];
                if (ptr4)
                {
                    if (ptr4->field_2bd)
                        return v9;
                    if (ptr4->field_2d0)
                        return v9;
                    v13 = ptr4->field_20c;
                    v14 = arm64g_calculate_condition(144, (((((unsigned long long)(char)(CmpF(v13, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v13, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v13, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v13, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if ((char)v14)
                        return v9;
                    if (ptr4->field_98)
                    {
                        if (ptr4->field_98->field_106)
                        {
                            if ((long long)ptr[160] && (Transform__get_position((long long)ptr[160], 0), (long long)ptr[160] && (Transform__get_forward((long long)ptr[160], 0), (long long)ptr[160])))
                            {
                                v15 = (int)ptr[88];
                                Transform__get_position((long long)ptr[160], 0);
                                if (!g_1fab2c8)
                                {
                                    sub_f7d92c("_F");
                                    g_1fab2c8 = 1;
                                }
                                if (!g_1ef07e8->field_e0)
                                    sub_f7da5c(g_1ef07e8);
                                v16 = [D] unsupported_Iop_SqrtF32();
                                v17 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v16, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v16, 925353388) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v16, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v16, 925353388) & 1)) & ((unsigned long long)(char)(CmpF(v16, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v16, 925353388) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                if (!((char)v17))
                                {
                                    v18 = (v13 + v13 * v15 - v13 * v15) / v16;
                                    v19 = (v10 + v10 * v15 - v10 * v15) / v16;
                                    v21 = (v20 + v20 * v15 - v20 * v15) / v16;
                                }
                                else
                                {
                                    if (!g_1fab2c9)
                                    {
                                        sub_f7d92c(&g_1ef22e8);
                                        g_1fab2c9 = 1;
                                    }
                                    addr = g_1ef22e8->field_b8;
                                    v18 = addr[0];
                                    v19 = addr[1];
                                    v21 = addr[2];
                                }
                                *((unsigned int *)&ptr[124]) = v18;
                                *((unsigned int *)&ptr[128]) = v19;
                                *((unsigned int *)&ptr[132]) = v21;
                                goto LABEL_108b018;
                            }
                        }
                        else
                        {
                            if (ptr4->field_78)
                            {
                                ptr5 = &(&ptr4->field_78->padding_0)[1];
                                v24 = *((long long *)ptr5);
                                *((int *)&ptr[132]) = *((int *)(ptr5 + 8));
                                *((unsigned long *)&ptr[124]) = v24;
LABEL_108b018:
                                if ((long long)ptr[160] && (Transform__get_position((long long)ptr[160], 0), (long long)ptr[48] && *((long long *)((long long)ptr[48] + 152))))
                                {
                                    v25 = LayerMask__op_Implicit((int)ptr[152], 0);
                                    if (!g_1ef0e48->field_e0)
                                        sub_f7da5c(g_1ef0e48);
                                    v26 = Physics__Raycast(&choice, v25, 0);
                                    if (((char)v26 & 1))
                                    {
                                        v27 = RaycastHit__get_rigidbody(&choice, 0);
                                        if (!g_1ef0c58->field_e0)
                                            sub_f7da5c(g_1ef0c58);
                                        v28 = Object__op_Implicit(v27, 0);
                                        if (!((char)v28 & 1))
                                            return v28;
                                        if (RaycastHit__get_rigidbody(&choice, 0))
                                        {
                                            v29 = Rigidbody__get_isKinematic();
                                            if (((char)v29 & 1))
                                                return v29;
                                            if ((long long)ptr[48])
                                            {
                                                if (*((char *)((long long)ptr[48] + 701)))
                                                    return v29;
                                                p = ptr + 104;
                                                if (!g_1ef0c58->field_e0)
                                                    sub_f7da5c(g_1ef0c58);
                                                if (!((char)Object__op_Implicit((long long)ptr[104], 0) & 1))
                                                {
                                                    v31 = sub_f7db70(g_1eefaf0);
                                                    GameObject__ctor(v31, g_1f0d688, 0);
                                                    if (v31)
                                                    {
                                                        v32 = sub_124913c(v31, g_1efeaf0);
                                                        v33 = sub_124913c(v31, g_1efeaf8);
                                                        *((long long *)p) = v33;
                                                        sub_f7d8d0(p, v33);
                                                        if (v32)
                                                        {
                                                            Rigidbody__set_isKinematic(v32, 1, 0);
                                                            goto LABEL_108b1c0;
                                                        }
                                                    }
                                                }
                                                else
                                                {
LABEL_108b1c0:
                                                    v34 = RaycastHit__get_rigidbody(&choice, 0);
                                                    if (*((long long *)p) && (Joint__set_connectedBody(*((long long *)p), v34, 0), *((long long *)p)))
                                                    {
                                                        v35 = Component__get_transform(*((long long *)p), 0);
                                                        RaycastHit__get_point(&choice, 0);
                                                        if (v35)
                                                        {
                                                            Transform__set_position(v35, 0);
                                                            if ((char)ptr[96])
                                                            {
                                                                v36 = Component__get_transform(ptr, 0);
                                                                if (RaycastHit__get_rigidbody(&choice, 0) && !((Rigidbody__get_centerOfMass(), !v36 || (Transform__TransformDirection(v36, 0), !(unsigned long long)RaycastHit__get_rigidbody(&choice, 0) || !Component__get_transform() || (Transform__get_position(), !*((long long *)p) || !Component__get_transform(*((long long *)p), 0) || (Transform__InverseTransformPoint(), v37 = *((long long *)p), !v37))))))
                                                                    goto LABEL_108b344;
                                                            }
                                                            else
                                                            {
                                                                v38 = *((long long *)p);
                                                                if (!g_1fab2c9)
                                                                {
                                                                    sub_f7d92c(&g_1ef22e8);
                                                                    g_1fab2c9 = 1;
                                                                }
                                                                if (v38)
                                                                {
                                                                    v37 = v38;
LABEL_108b344:
                                                                    Joint__set_anchor(v37, 0);
                                                                    if (*((long long *)p))
                                                                    {
                                                                        SpringJoint__set_spring(*((long long *)p), 0);
                                                                        if ((long long)ptr[104])
                                                                        {
                                                                            SpringJoint__set_damper((long long)ptr[104], 0);
                                                                            if ((long long)ptr[104])
                                                                            {
                                                                                SpringJoint__set_maxDistance((long long)ptr[104], 0);
                                                                                RaycastHit__get_distance(&choice, 0);
                                                                                v39 = MonoBehaviour__StartCoroutine(ptr, DragRigidbody__DragObject(), 0);
                                                                                return MonoBehaviour__StartCoroutine(ptr, DragRigidbody__DragObject(), 0);
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
                                    else
                                    {
                                        ptr3 = (long long)ptr[48];
                                        if (ptr3)
                                        {
                                            ptr3->field_2bd = 1;
                                            ptr3->field_2b8 = 0xc1000000;
                                            return v26;
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
    sub_f7db74();
}
```

## `DragRigidbody.DragObject` — RVA `0xc8b3b4`

- Decompiled symbol: `DragRigidbody_DragObject`
- Metadata signature: `private IEnumerator DragObject(float distance) { }`
- Native interval: `124` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DragRigidbody_Recovered` matched 2 offsets against `DragRigidbody` metadata (confidence 0.67).

```c
typedef struct DragRigidbody_Recovered {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long FPSWalkerComponent;
    unsigned int IronsightsComponent;
} DragRigidbody_Recovered;

extern char g_1fab437;

struct_0 * DragRigidbody_DragObject(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0
    unsigned int v2;  // s0

    if (!(g_1fab437 & 1))
    {
        sub_f7d92c("ch");
        g_1fab437 = 1;
    }
    v0 = sub_f7db70(g_1ef2fb0);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct DragRigidbody_Recovered *)&ptr->field_20, a0);
    ptr->field_28 = v2;
    return ptr;
}
```

## `DragRigidbody.<DragObject>d__24.ctor` — RVA `0xc8b430`

- Decompiled symbol: `DragRigidbody_DragObject_d__24_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void DragRigidbody_DragObject_d__24_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `DragRigidbody.OnCollisionStay` — RVA `0xc8b458`

- Decompiled symbol: `DragRigidbody_OnCollisionStay`
- Metadata signature: `private void OnCollisionStay(Collision col) { }`
- Native interval: `316` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DragRigidbody_Recovered` matched 2 offsets against `DragRigidbody` metadata (confidence 1.00).

```c
typedef struct DragRigidbody_Recovered {
    char padding_0[104];
    struct DragRigidbody_Recovered *springJoint;
    char padding_70[36];
    char dropOnPlayerCollision;
} DragRigidbody_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efeca8;
extern char g_1fab438;

struct_1 * DragRigidbody_OnCollisionStay(struct_1 *ptr, long long a1)
{
    struct_1 *v0;  // x0
    struct_1 *v1;  // x0
    struct_1 *v2;  // x0
    struct_1 *v3;  // x0
    struct_1 *v4;  // x0
    long long v5;  // x0
    long long v6;  // x0
    struct_1 *v7;  // x0
    unsigned long long v8;  // x0

    v0 = ptr;
    if (!(g_1fab438 & 1))
    {
        sub_f7d92c(&g_1efeca8);
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab438 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (!ptr->field_94)
        return v2;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v3 = Object__op_Implicit(ptr->field_68, 0);
    if (!((char)v3 & 1))
        return v3;
    v4 = ptr->field_68;
    if (v4)
    {
        v5 = Joint__get_connectedBody(v4, 0);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v4 = Object__op_Implicit(v5, 0);
        if (!((char)v4 & 1))
        {
            return v4;
        }
        else if (a1)
        {
            v4 = Collision__get_gameObject(a1, 0);
            if (v4)
            {
                v4 = sub_1249224();
                if (ptr->field_68)
                {
                    v6 = Joint__get_connectedBody(ptr->field_68, 0);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    v7 = Object__op_Equality(v4, v6, 0);
                    if (!((char)v7 & 1))
                        return v7;
                    v8 = DragRigidbody__DropObject(ptr);
                    return DragRigidbody__DropObject(ptr);
                }
            }
        }
    }
    sub_f7db74(v4);
}
```

## `DragRigidbody.DropObject` — RVA `0xc8b594`

- Decompiled symbol: `DragRigidbody_DropObject`
- Metadata signature: `private void DropObject() { }`
- Native interval: `140` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DragRigidbody_Recovered` matched 3 offsets against `DragRigidbody` metadata (confidence 1.00).

```c
typedef struct DragRigidbody_Recovered {
    char padding_0[32];
    struct struct_0 *FPSWalkerComponent;
    char padding_28[64];
    long long springJoint;
    char padding_70[8];
    char dragState;
} DragRigidbody_Recovered;

typedef struct struct_0 {
    char padding_0[408];
    char field_198;
    char padding_199[3];
    unsigned int field_19c;
} struct_0;

unsigned long long DragRigidbody_DropObject(struct_1 *ptr)
{
    struct_0 *p;  // x20
    unsigned int v1;  // s0
    unsigned long long v2;  // x0

    p = ptr->field_20;
    if (p)
    {
        p->field_198 = 0;
        Time__get_time(0);
        p->field_19c = v1;
        if (ptr->field_68 && Joint__get_connectedBody(ptr->field_68, 0))
        {
            Rigidbody__set_drag();
            if (ptr->field_68 && Joint__get_connectedBody(ptr->field_68, 0))
            {
                Rigidbody__set_angularDrag();
                if (ptr->field_68)
                {
                    v2 = Joint__set_connectedBody(ptr->field_68, 0, 0);
                    ptr->field_78 = 0;
                    return v2;
                }
            }
        }
    }
    sub_f7db74();
}
```

## `DragRigidbody.ctor` — RVA `0xc8b620`

- Decompiled symbol: `DragRigidbody_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `68` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DragRigidbody_Recovered` matched 4 offsets against `DragRigidbody` metadata (confidence 1.00).

```c
typedef struct DragRigidbody_Recovered {
    char padding_0[64];
    uint128_t spring;
    char padding_50[4];
    unsigned int reachDistance;
    char padding_58[4];
    unsigned int throwForce;
    char padding_60[56];
    unsigned int layersToDrag;
} DragRigidbody_Recovered;

void DragRigidbody_ctor(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    ptr->field_54 = 0x40200000;
    ptr->field_40 = 0x40a00000412000003f80000042960000;
    ptr->field_5c = 0x40e00000;
    ptr->field_98 = LayerMask__op_Implicit(0, 0);
    MonoBehaviour__ctor();
    return;
}
```

## `DragRigidbody.<DragObject>d__24.Dispose` — RVA `0xc8b664`

- Decompiled symbol: `DragRigidbody_DragObject_d__24_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long DragRigidbody_DragObject_d__24_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `DragRigidbody.<DragObject>d__24.MoveNext` — RVA `0xc8b668`

- Decompiled symbol: `DragRigidbody_DragObject_d__24_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `2048` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x108b668: sub sp, sp, #0x90
// 0x108b66c: stp d13, d12, [sp, #0x20]
// 0x108b670: stp d11, d10, [sp, #0x30]
// 0x108b674: stp d9, d8, [sp, #0x40]
// 0x108b678: stp x30, x25, [sp, #0x50]
// 0x108b67c: stp x24, x23, [sp, #0x60]
// 0x108b680: stp x22, x21, [sp, #0x70]
// 0x108b684: stp x20, x19, [sp, #0x80]
// 0x108b688: adrp x19, #0x1fab000
// 0x108b68c: ldrb w8, [x19, #0x439]
// 0x108b690: mov x20, x0
// 0x108b694: tbnz w8, #0, #0x108b6b8
// 0x108b698: adrp x0, #0x1e8d000
// 0x108b69c: ldr x0, [x0, #0x248]
// 0x108b6a0: bl #0xf7d92c
// 0x108b6a4: adrp x0, #0x1e8c000
// 0x108b6a8: ldr x0, [x0, #0xd8]
// 0x108b6ac: bl #0xf7d92c
// 0x108b6b0: mov w8, #1
// 0x108b6b4: strb w8, [x19, #0x439]
// 0x108b6b8: stp xzr, xzr, [sp, #8]
// 0x108b6bc: str xzr, [sp, #0x18]
// 0x108b6c0: ldr w8, [x20, #0x10]
// 0x108b6c4: adrp x22, #0x1e8c000
// 0x108b6c8: ldr x19, [x20, #0x20]
// 0x108b6cc: ldr x22, [x22, #0xd8]
// 0x108b6d0: cmp w8, #1
// 0x108b6d4: b.eq #0x108b8b4
// 0x108b6d8: cbnz w8, #0x108ba54
// 0x108b6dc: mov w8, #-1
// 0x108b6e0: str w8, [x20, #0x10]
// 0x108b6e4: cbz x19, #0x108be64
// 0x108b6e8: ldrb w8, [x19, #0x78]
// 0x108b6ec: cbnz w8, #0x108b738
// 0x108b6f0: ldr x0, [x19, #0x68]
// 0x108b6f4: cbz x0, #0x108be64
// 0x108b6f8: mov x1, xzr
// 0x108b6fc: bl #0x1bd009c
// 0x108b700: cbz x0, #0x108be64
// 0x108b704: mov x1, xzr
// 0x108b708: bl #0x1bcf0c8
// 0x108b70c: ldr x0, [x19, #0x68]
// 0x108b710: str s0, [x19, #0x70]
// 0x108b714: cbz x0, #0x108be64
// 0x108b718: mov x1, xzr
// 0x108b71c: bl #0x1bd009c
// 0x108b720: cbz x0, #0x108be64
// 0x108b724: mov x1, xzr
// 0x108b728: bl #0x1bcf150
// 0x108b72c: mov w8, #1
// 0x108b730: str s0, [x19, #0x74]
// 0x108b734: strb w8, [x19, #0x78]
// 0x108b738: ldr x0, [x19, #0x68]
// 0x108b73c: cbz x0, #0x108be64
// 0x108b740: mov x1, xzr
// 0x108b744: bl #0x1bd009c
// 0x108b748: cbz x0, #0x108be64
// 0x108b74c: mov x1, xzr
// 0x108b750: bl #0x1bcf214
// 0x108b754: tbnz w0, #0, #0x108b870
// 0x108b758: ldr x0, [x19, #0x68]
// 0x108b75c: cbz x0, #0x108be64
// 0x108b760: mov x1, xzr
// 0x108b764: bl #0x1bd009c
// 0x108b768: cbz x0, #0x108be64
// 0x108b76c: adrp x23, #0x1e8d000
// 0x108b770: ldr x23, [x23, #0x248]
// 0x108b774: ldr x1, [x23]
// 0x108b778: bl #0x1231bc8
// 0x108b77c: ldr x8, [x22]
// 0x108b780: mov x21, x0
// 0x108b784: ldr w9, [x8, #0xe0]
// 0x108b788: cbnz w9, #0x108b794
// 0x108b78c: mov x0, x8
// 0x108b790: bl #0xf7da5c
// 0x108b794: mov x0, x21
// 0x108b798: mov x1, xzr
// 0x108b79c: bl #0x1b98274
// 0x108b7a0: tbz w0, #0, #0x108b850
// 0x108b7a4: ldr x0, [x19, #0x68]
// 0x108b7a8: cbz x0, #0x108be64
// 0x108b7ac: mov x1, xzr
// 0x108b7b0: bl #0x1bd009c
// 0x108b7b4: cbz x0, #0x108be64
// 0x108b7b8: ldr x1, [x23]
// 0x108b7bc: bl #0x1231bc8
// 0x108b7c0: cbz x0, #0x108be64
// 0x108b7c4: mov x1, xzr
// 0x108b7c8: bl #0x1b91624
// 0x108b7cc: tbz w0, #0, #0x108b850
// 0x108b7d0: ldr x0, [x19, #0x68]
// 0x108b7d4: cbz x0, #0x108be64
// 0x108b7d8: mov x1, xzr
// 0x108b7dc: bl #0x1bd009c
// 0x108b7e0: cbz x0, #0x108be64
// 0x108b7e4: ldr x1, [x23]
// 0x108b7e8: bl #0x1231bc8
// 0x108b7ec: mov x21, x0
// 0x108b7f0: mov x0, xzr
// 0x108b7f4: bl #0x1b9ae58
// 0x108b7f8: mov x0, xzr
// 0x108b7fc: mov v8.16b, v0.16b
// 0x108b800: bl #0x1b9ae58
// 0x108b804: mov v1.16b, v0.16b
// 0x108b808: fmov s0, #0.75000000
// 0x108b80c: fmul s0, s8, s0
// 0x108b810: mov x0, xzr
// 0x108b814: bl #0x1b9012c
// 0x108b818: cbz x21, #0x108be64
// 0x108b81c: mov x0, x21
// 0x108b820: mov x1, xzr
// 0x108b824: bl #0x1b6a500
// 0x108b828: ldr x0, [x19, #0x68]
// 0x108b82c: cbz x0, #0x108be64
// 0x108b830: mov x1, xzr
// 0x108b834: bl #0x1bd009c
// 0x108b838: cbz x0, #0x108be64
// 0x108b83c: ldr x1, [x23]
// 0x108b840: bl #0x1231bc8
// 0x108b844: cbz x0, #0x108be64
// 0x108b848: mov x1, xzr
// 0x108b84c: bl #0x1b6a5cc
// 0x108b850: ldr x0, [x19, #0x68]
// 0x108b854: cbz x0, #0x108be64
// 0x108b858: mov x1, xzr
// 0x108b85c: bl #0x1bd009c
// 0x108b860: cbz x0, #0x108be64
// 0x108b864: mov w1, #1
// 0x108b868: mov x2, xzr
// 0x108b86c: bl #0x1bcf250
// 0x108b870: ldr x0, [x19, #0x68]
// 0x108b874: cbz x0, #0x108be64
// 0x108b878: mov x1, xzr
// 0x108b87c: bl #0x1bd009c
// 0x108b880: cbz x0, #0x108be64
// 0x108b884: ldr s0, [x19, #0x48]
// 0x108b888: mov x1, xzr
// 0x108b88c: bl #0x1bcf104
// 0x108b890: ldr x0, [x19, #0x68]
// 0x108b894: cbz x0, #0x108be64
// 0x108b898: mov x1, xzr
// 0x108b89c: bl #0x1bd009c
// 0x108b8a0: cbz x0, #0x108be64
// 0x108b8a4: ldr s0, [x19, #0x4c]
// 0x108b8a8: mov x1, xzr
// 0x108b8ac: bl #0x1bcf18c
// 0x108b8b0: b #0x108b8c0
// 0x108b8b4: mov w8, #-1
// 0x108b8b8: str w8, [x20, #0x10]
// 0x108b8bc: cbz x19, #0x108be64
// 0x108b8c0: ldr x8, [x19, #0x38]
// 0x108b8c4: cbz x8, #0x108be64
// 0x108b8c8: ldrb w8, [x8, #0x96]
// 0x108b8cc: cbz w8, #0x108bdc8
// 0x108b8d0: ldr x8, [x19, #0x30]
// 0x108b8d4: cbz x8, #0x108be64
// 0x108b8d8: ldr s8, [x8, #0x2b4]
// 0x108b8dc: mov x0, xzr
// 0x108b8e0: bl #0x1b9ad30
// 0x108b8e4: adrp x8, #0x832000
// 0x108b8e8: ldr s1, [x8, #0x550]
// 0x108b8ec: fadd s1, s8, s1
// 0x108b8f0: fcmp s1, s0
// 0x108b8f4: b.pl #0x108bdc8
// 0x108b8f8: ldr x0, [x19, #0x68]
// 0x108b8fc: cbz x0, #0x108be64
// 0x108b900: mov x1, xzr
// 0x108b904: bl #0x1bd009c
// 0x108b908: ldr x8, [x22]
// 0x108b90c: mov x21, x0
// 0x108b910: ldr w9, [x8, #0xe0]
// 0x108b914: cbnz w9, #0x108b920
// 0x108b918: mov x0, x8
// 0x108b91c: bl #0xf7da5c
// 0x108b920: mov x0, x21
// 0x108b924: mov x1, xzr
// 0x108b928: bl #0x1b98274
// 0x108b92c: tbz w0, #0, #0x108bdc8
// 0x108b930: ldr x8, [x19, #0x30]
// 0x108b934: cbz x8, #0x108be64
// 0x108b938: ldrb w9, [x8, #0x2d0]
// 0x108b93c: cbnz w9, #0x108bdc8
// 0x108b940: ldr s0, [x8, #0x20c]
// 0x108b944: fcmp s0, #0.0
// 0x108b948: b.lt #0x108bdc8
// 0x108b94c: ldr x9, [x8, #0x98]
// 0x108b950: cbz x9, #0x108be64
// 0x108b954: adrp x23, #0x1e8c000
// 0x108b958: ldrb w9, [x9, #0x106]
// 0x108b95c: ldr x23, [x23, #0xa60]
// 0x108b960: adrp x24, #0x1fab000
// 0x108b964: adrp x21, #0x832000
// 0x108b968: cbz w9, #0x108ba5c
// 0x108b96c: ldr x0, [x19, #0xa0]
// 0x108b970: cbz x0, #0x108be64
// 0x108b974: mov x1, xzr
// 0x108b978: bl #0x1b9d508
// 0x108b97c: ldr x0, [x19, #0xa0]
// 0x108b980: cbz x0, #0x108be64
// 0x108b984: mov x1, xzr
// 0x108b988: mov v8.16b, v0.16b
// 0x108b98c: mov v9.16b, v1.16b
// 0x108b990: mov v10.16b, v2.16b
// 0x108b994: bl #0x1b9d9b8
// 0x108b998: ldr x8, [x19, #0x30]
// 0x108b99c: cbz x8, #0x108be64
// 0x108b9a0: ldr x8, [x8, #0x98]
// 0x108b9a4: cbz x8, #0x108be64
// 0x108b9a8: ldr x0, [x19, #0xa0]
// 0x108b9ac: cbz x0, #0x108be64
// 0x108b9b0: ldr s3, [x19, #0x58]
// 0x108b9b4: ldr s4, [x8, #0x1a8]
// 0x108b9b8: mov x1, xzr
// 0x108b9bc: fadd s3, s3, s4
// 0x108b9c0: fmul s2, s2, s3
// 0x108b9c4: fmul s1, s1, s3
// 0x108b9c8: fmul s0, s0, s3
// 0x108b9cc: fadd s11, s10, s2
// 0x108b9d0: fadd s12, s9, s1
// 0x108b9d4: fadd s13, s8, s0
// 0x108b9d8: bl #0x1b9d508
// 0x108b9dc: ldrb w8, [x24, #0x2c8]
// 0x108b9e0: mov v8.16b, v0.16b
// 0x108b9e4: mov v9.16b, v1.16b
// 0x108b9e8: mov v10.16b, v2.16b
// 0x108b9ec: cbnz w8, #0x108ba04
// 0x108b9f0: adrp x0, #0x1e8c000
// 0x108b9f4: ldr x0, [x0, #0xa60]
// 0x108b9f8: bl #0xf7d92c
// 0x108b9fc: mov w8, #1
// 0x108ba00: strb w8, [x24, #0x2c8]
// 0x108ba04: ldr x0, [x23]
// 0x108ba08: fsub s13, s13, s8
// 0x108ba0c: fsub s9, s12, s9
// 0x108ba10: fsub s8, s11, s10
// 0x108ba14: ldr w8, [x0, #0xe0]
// 0x108ba18: cbnz w8, #0x108ba20
// 0x108ba1c: bl #0xf7da5c
// 0x108ba20: fmul s0, s13, s13
// 0x108ba24: fmul s1, s9, s9
// 0x108ba28: ldr s3, [x21, #0x41c]
// 0x108ba2c: fadd s0, s0, s1
// 0x108ba30: fmul s1, s8, s8
// 0x108ba34: fadd s0, s1, s0
// 0x108ba38: fsqrt s2, s0
// 0x108ba3c: fcmp s2, s3
// 0x108ba40: b.le #0x108ba7c
// 0x108ba44: fdiv s0, s13, s2
// 0x108ba48: fdiv s1, s9, s2
// 0x108ba4c: fdiv s2, s8, s2
// 0x108ba50: b #0x108bab4
// 0x108ba54: mov w19, wzr
// 0x108ba58: b #0x108be3c
// 0x108ba5c: ldr x8, [x8, #0x78]
// 0x108ba60: cbz x8, #0x108be64
// 0x108ba64: add x8, x8, #0x42c
// 0x108ba68: ldr w9, [x8, #8]
// 0x108ba6c: ldr x8, [x8]
// 0x108ba70: str w9, [x19, #0x90]
// 0x108ba74: str x8, [x19, #0x88]
// 0x108ba78: b #0x108babc
// 0x108ba7c: adrp x25, #0x1fab000
// 0x108ba80: ldrb w8, [x25, #0x2c9]
// 0x108ba84: cbnz w8, #0x108ba9c
// 0x108ba88: adrp x0, #0x1e8c000
// 0x108ba8c: ldr x0, [x0, #0x1e8]
// 0x108ba90: bl #0xf7d92c
// 0x108ba94: mov w8, #1
// 0x108ba98: strb w8, [x25, #0x2c9]
// 0x108ba9c: adrp x8, #0x1e8c000
// 0x108baa0: ldr x8, [x8, #0x1e8]
// 0x108baa4: ldr x8, [x8]
// 0x108baa8: ldr x8, [x8, #0xb8]
// 0x108baac: ldp s0, s1, [x8]
// 0x108bab0: ldr s2, [x8, #8]
// 0x108bab4: stp s0, s1, [x19, #0x88]
// 0x108bab8: str s2, [x19, #0x90]
// 0x108babc: ldr x0, [x19, #0xa0]
// 0x108bac0: cbz x0, #0x108be64
// 0x108bac4: mov x1, xzr
// 0x108bac8: bl #0x1b9d508
// 0x108bacc: ldr d8, [x19, #0x88]
// 0x108bad0: ldrb w8, [x24, #0x2c8]
// 0x108bad4: ldr s9, [x19, #0x90]
// 0x108bad8: stp s0, s1, [sp, #8]
// 0x108badc: str s2, [sp, #0x10]
// 0x108bae0: cbnz w8, #0x108baf8
// 0x108bae4: adrp x0, #0x1e8c000
// 0x108bae8: ldr x0, [x0, #0xa60]
// 0x108baec: bl #0xf7d92c
// 0x108baf0: mov w8, #1
// 0x108baf4: strb w8, [x24, #0x2c8]
// 0x108baf8: ldr x0, [x23]
// 0x108bafc: ldr w8, [x0, #0xe0]
// 0x108bb00: cbnz w8, #0x108bb08
// 0x108bb04: bl #0xf7da5c
// 0x108bb08: fmul v0.2s, v8.2s, v8.2s
// 0x108bb0c: ldr s2, [x21, #0x41c]
// 0x108bb10: faddp s0, v0.2s
// 0x108bb14: fmul s1, s9, s9
// 0x108bb18: fadd s0, s1, s0
// 0x108bb1c: fsqrt s1, s0
// 0x108bb20: fcmp s1, s2
// 0x108bb24: b.le #0x108bb38
// 0x108bb28: dup v0.2s, v1.s[0]
// 0x108bb2c: fdiv v0.2s, v8.2s, v0.2s
// 0x108bb30: fdiv s1, s9, s1
// 0x108bb34: b #0x108bb70
// 0x108bb38: adrp x21, #0x1fab000
// 0x108bb3c: ldrb w8, [x21, #0x2c9]
// 0x108bb40: cbnz w8, #0x108bb58
// 0x108bb44: adrp x0, #0x1e8c000
// 0x108bb48: ldr x0, [x0, #0x1e8]
// 0x108bb4c: bl #0xf7d92c
// 0x108bb50: mov w8, #1
// 0x108bb54: strb w8, [x21, #0x2c9]
// 0x108bb58: adrp x8, #0x1e8c000
// 0x108bb5c: ldr x8, [x8, #0x1e8]
// 0x108bb60: ldr x8, [x8]
// 0x108bb64: ldr x8, [x8, #0xb8]
// 0x108bb68: ldr d0, [x8]
// 0x108bb6c: ldr s1, [x8, #8]
// 0x108bb70: stur d0, [sp, #0x14]
// 0x108bb74: str s1, [sp, #0x1c]
// 0x108bb78: ldr x0, [x19, #0x68]
// 0x108bb7c: cbz x0, #0x108be64
// 0x108bb80: mov x1, xzr
// 0x108bb84: bl #0x1b92154
// 0x108bb88: ldr s0, [x20, #0x28]
// 0x108bb8c: mov x21, x0
// 0x108bb90: add x0, sp, #8
// 0x108bb94: mov x1, xzr
// 0x108bb98: bl #0x1b754fc
// 0x108bb9c: cbz x21, #0x108be64
// 0x108bba0: mov x0, x21
// 0x108bba4: mov x1, xzr
// 0x108bba8: bl #0x1b9d5a8
// 0x108bbac: ldr x8, [x19, #0x38]
// 0x108bbb0: cbz x8, #0x108be64
// 0x108bbb4: ldr x0, [x19, #0x68]
// 0x108bbb8: cbz x0, #0x108be64
// 0x108bbbc: ldrb w21, [x8, #0x8a]
// 0x108bbc0: mov x1, xzr
// 0x108bbc4: bl #0x1bd009c
// 0x108bbc8: cbz x0, #0x108be64
// 0x108bbcc: mov x1, xzr
// 0x108bbd0: cbz w21, #0x108bc60
// 0x108bbd4: bl #0x1bcf1d8
// 0x108bbd8: ldr s12, [x19, #0x5c]
// 0x108bbdc: fmov s1, #1.00000000
// 0x108bbe0: fcmp s0, s1
// 0x108bbe4: fmov s8, #0.50000000
// 0x108bbe8: b.mi #0x108bc0c
// 0x108bbec: ldr x0, [x19, #0x68]
// 0x108bbf0: cbz x0, #0x108be64
// 0x108bbf4: mov x1, xzr
// 0x108bbf8: bl #0x1bd009c
// 0x108bbfc: cbz x0, #0x108be64
// 0x108bc00: mov x1, xzr
// 0x108bc04: bl #0x1bcf1d8
// 0x108bc08: mov v8.16b, v0.16b
// 0x108bc0c: ldr x8, [x19, #0x30]
// 0x108bc10: cbz x8, #0x108be64
// 0x108bc14: ldr x8, [x8, #0x98]
// 0x108bc18: cbz x8, #0x108be64
// 0x108bc1c: ldr x0, [x19, #0x68]
// 0x108bc20: cbz x0, #0x108be64
// 0x108bc24: ldrb w21, [x8, #0x106]
// 0x108bc28: mov x1, xzr
// 0x108bc2c: bl #0x1bd009c
// 0x108bc30: mov x20, x0
// 0x108bc34: cbz w21, #0x108bd44
// 0x108bc38: ldr x0, [x19, #0xa0]
// 0x108bc3c: cbz x0, #0x108be64
// 0x108bc40: mov x1, xzr
// 0x108bc44: bl #0x1b9d9b8
// 0x108bc48: ldr x0, [x19, #0x68]
// 0x108bc4c: cbz x0, #0x108be64
// 0x108bc50: mov v9.16b, v0.16b
// 0x108bc54: mov v10.16b, v1.16b
// 0x108bc58: mov v11.16b, v2.16b
// 0x108bc5c: b #0x108bd68
// 0x108bc60: bl #0x1b92154
// 0x108bc64: cbz x0, #0x108be64
// 0x108bc68: mov x1, xzr
// 0x108bc6c: bl #0x1b9d508
// 0x108bc70: ldr x0, [x19, #0xa0]
// 0x108bc74: cbz x0, #0x108be64
// 0x108bc78: mov x1, xzr
// 0x108bc7c: mov v8.16b, v0.16b
// 0x108bc80: mov v9.16b, v1.16b
// 0x108bc84: mov v10.16b, v2.16b
// 0x108bc88: bl #0x1b9d508
// 0x108bc8c: adrp x21, #0x1fab000
// 0x108bc90: ldrb w8, [x21, #0x3e0]
// 0x108bc94: mov v11.16b, v0.16b
// 0x108bc98: mov v12.16b, v1.16b
// 0x108bc9c: mov v13.16b, v2.16b
// 0x108bca0: cbnz w8, #0x108bcb8
// 0x108bca4: adrp x0, #0x1e8c000
// 0x108bca8: ldr x0, [x0, #0xa60]
// 0x108bcac: bl #0xf7d92c
// 0x108bcb0: mov w8, #1
// 0x108bcb4: strb w8, [x21, #0x3e0]
// 0x108bcb8: ldr x0, [x23]
// 0x108bcbc: ldr w8, [x0, #0xe0]
// 0x108bcc0: cbnz w8, #0x108bcc8
// 0x108bcc4: bl #0xf7da5c
// 0x108bcc8: ldr x8, [x19, #0x30]
// 0x108bccc: cbz x8, #0x108be64
// 0x108bcd0: ldr x8, [x8, #0x98]
// 0x108bcd4: cbz x8, #0x108be64
// 0x108bcd8: ldr s3, [x19, #0x58]
// 0x108bcdc: ldr s4, [x8, #0x1a8]
// 0x108bce0: adrp x8, #0x832000
// 0x108bce4: fsub s0, s8, s11
// 0x108bce8: fsub s1, s9, s12
// 0x108bcec: ldr s5, [x8, #0x380]
// 0x108bcf0: fsub s2, s10, s13
// 0x108bcf4: fmul s0, s0, s0
// 0x108bcf8: fmul s1, s1, s1
// 0x108bcfc: fmul s2, s2, s2
// 0x108bd00: fadd s0, s0, s1
// 0x108bd04: fadd s0, s2, s0
// 0x108bd08: fadd s1, s3, s4
// 0x108bd0c: fsqrt s0, s0
// 0x108bd10: fmul s1, s1, s5
// 0x108bd14: fcmp s0, s1
// 0x108bd18: b.pl #0x108bdc8
// 0x108bd1c: ldr x8, [x19, #0x20]
// 0x108bd20: cbz x8, #0x108be64
// 0x108bd24: mov w19, #1
// 0x108bd28: strb w19, [x8, #0x198]
// 0x108bd2c: str xzr, [x20, #0x18]!
// 0x108bd30: mov x0, x20
// 0x108bd34: mov x1, xzr
// 0x108bd38: bl #0xf7d8d0
// 0x108bd3c: stur w19, [x20, #-8]
// 0x108bd40: b #0x108be3c
// 0x108bd44: ldr x8, [x19, #0x30]
// 0x108bd48: cbz x8, #0x108be64
// 0x108bd4c: ldr x8, [x8, #0x78]
// 0x108bd50: cbz x8, #0x108be64
// 0x108bd54: ldr x0, [x19, #0x68]
// 0x108bd58: cbz x0, #0x108be64
// 0x108bd5c: ldr s9, [x8, #0x42c]
// 0x108bd60: ldr s10, [x8, #0x430]
// 0x108bd64: ldr s11, [x8, #0x434]
// 0x108bd68: mov x1, xzr
// 0x108bd6c: bl #0x1b92154
// 0x108bd70: cbz x0, #0x108be64
// 0x108bd74: mov x1, xzr
// 0x108bd78: bl #0x1b9d508
// 0x108bd7c: cbz x20, #0x108be64
// 0x108bd80: mov v3.16b, v0.16b
// 0x108bd84: fmul s0, s12, s8
// 0x108bd88: mov v4.16b, v1.16b
// 0x108bd8c: mov v5.16b, v2.16b
// 0x108bd90: fmul s2, s0, s11
// 0x108bd94: fmul s1, s0, s10
// 0x108bd98: fmul s0, s0, s9
// 0x108bd9c: mov w1, #1
// 0x108bda0: mov x0, x20
// 0x108bda4: mov x2, xzr
// 0x108bda8: bl #0x1bcf728
// 0x108bdac: ldr x8, [x19, #0x30]
// 0x108bdb0: cbz x8, #0x108be64
// 0x108bdb4: ldr x20, [x8, #0x78]
// 0x108bdb8: mov x0, xzr
// 0x108bdbc: bl #0x1b9ad30
// 0x108bdc0: cbz x20, #0x108be64
// 0x108bdc4: str s0, [x20, #0x1fc]
// 0x108bdc8: ldr x0, [x19, #0x68]
// 0x108bdcc: cbz x0, #0x108be64
// 0x108bdd0: mov x1, xzr
// 0x108bdd4: bl #0x1bd009c
// 0x108bdd8: ldr x8, [x22]
// 0x108bddc: mov x20, x0
// 0x108bde0: ldr w9, [x8, #0xe0]
// 0x108bde4: cbnz w9, #0x108bdf0
// 0x108bde8: mov x0, x8
// 0x108bdec: bl #0xf7da5c
// 0x108bdf0: mov x0, x20
// 0x108bdf4: mov x1, xzr
// 0x108bdf8: bl #0x1b98274
// 0x108bdfc: tbz w0, #0, #0x108be0c
// 0x108be00: mov x0, x19
// 0x108be04: bl #0x108b594
// 0x108be08: b #0x108be24
// 0x108be0c: ldr x20, [x19, #0x20]
// 0x108be10: cbz x20, #0x108be64
// 0x108be14: mov x0, xzr
// 0x108be18: strb wzr, [x20, #0x198]
// 0x108be1c: bl #0x1b9ad30
// 0x108be20: str s0, [x20, #0x19c]
// 0x108be24: ldr x8, [x19, #0x30]
// 0x108be28: strb wzr, [x19, #0x78]
// 0x108be2c: cbz x8, #0x108be64
// 0x108be30: mov w19, wzr
// 0x108be34: mov w9, #1
// 0x108be38: strb w9, [x8, #0x2bd]
// 0x108be3c: mov w0, w19
// 0x108be40: ldp x20, x19, [sp, #0x80]
// 0x108be44: ldp x22, x21, [sp, #0x70]
// 0x108be48: ldp x24, x23, [sp, #0x60]
// 0x108be4c: ldp x30, x25, [sp, #0x50]
// 0x108be50: ldp d9, d8, [sp, #0x40]
// 0x108be54: ldp d11, d10, [sp, #0x30]
// 0x108be58: ldp d13, d12, [sp, #0x20]
// 0x108be5c: add sp, sp, #0x90
// 0x108be60: ret
// 0x108be64: bl #0xf7db74
```

## `DragRigidbody.<DragObject>d__24.get_Current` — RVA `0xc8be68`

- Decompiled symbol: `DragRigidbody_DragObject_d__24_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long DragRigidbody_DragObject_d__24_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `DragRigidbody.<DragObject>d__24.Reset` — RVA `0xc8be70`

- Decompiled symbol: `DragRigidbody_DragObject_d__24_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f044d0;

void DragRigidbody_DragObject_d__24_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f044d0));
}
```

## `DragRigidbody.<DragObject>d__24.get_Current` — RVA `0xc8bea8`

- Decompiled symbol: `DragRigidbody_DragObject_d__24_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long DragRigidbody_DragObject_d__24_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
