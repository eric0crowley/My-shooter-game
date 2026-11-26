# Native pseudocode: LocomotionSimpleAgent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `LocomotionSimpleAgent.Start` — RVA `0xc6e208`

- Decompiled symbol: `LocomotionSimpleAgent_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned long long field_28;
} struct_0;

void LocomotionSimpleAgent_Start(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (!a0->field_28)
        sub_f7db74(0);
}
```

## `LocomotionSimpleAgent.Update` — RVA `0xc6e228`

- Decompiled symbol: `LocomotionSimpleAgent_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `1164` bytes
- Result: `pseudocode`
- Heuristic layout hint: `LocomotionSimpleAgent_Recovered` matched 4 offsets against `LocomotionSimpleAgent` metadata (confidence 0.80).

```c
typedef struct LocomotionSimpleAgent_Recovered {
    char padding_0[32];
    struct struct_2 *anim;
    struct struct_2 *agent;
    unsigned long long smoothDeltaPosition;
    unsigned int velocity[2];
    char field_3c;
} LocomotionSimpleAgent_Recovered;

typedef struct struct_2 {
    char padding_0[40];
    unsigned int field_28;
    unsigned int field_2c;
    unsigned int field_30;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efd000;
extern long long g_1f13c88;
extern char g_1fab243;
extern char g_1fab351;
extern char g_1fab3df;

unsigned int [13] LocomotionSimpleAgent_Update(struct_1 *ptr)
{
    unsigned int v2[13];  // x0
    unsigned int v3;  // s2
    unsigned long v12;  // 4129
    unsigned int v14;  // s0
    unsigned long v15;  // 4175
    unsigned long v16;  // 4128
    unsigned int p[13];  // x20
    unsigned int v18;  // s0
    unsigned int addr[13];  // x20
    unsigned int v20;  // s0
    unsigned int v21;  // s1
    unsigned int v4;  // s0
    unsigned int v22;  // s0
    unsigned int v23;  // s8
    unsigned long v24;  // 4125
    unsigned int v5;  // s0
    unsigned int v6;  // s1
    unsigned int v7;  // s12
    unsigned int v8;  // s13
    unsigned int v9;  // s11
    unsigned int v10;  // s1
    unsigned long v11;  // d0
    int v0;  // [bp-0x90]
    int v1;  // [bp-0x80], Other Possible Types: unsigned int

    if (!(g_1fab351 & 1))
    {
        sub_f7d92c(&g_1efd000);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("{=");
        sub_f7d92c("y=");
        sub_f7d92c(&g_1f13c88);
        g_1fab351 = 1;
    }
    v2 = ptr->field_28;
    if (v2 && (NavMeshAgent__get_nextPosition(v2, 0), v2 = (unsigned int [13])ptr->field_28, v2 && (v2 = (unsigned int [13])Component__get_transform(v2, 0), v2 && (Transform__get_position(), v2 = (unsigned int [13])ptr->field_28, v2 && (v1 = v3, v2 = (unsigned int [13])Component__get_transform(v2, 0), v2 && (Transform__get_right(), v2 = (unsigned int [13])ptr->field_28, v2 && (v2 = (unsigned int [13])Component__get_transform(v2, 0), v2)))))))
    {
        v5 = v4 - v4;
        v7 = v6 - v6;
        v8 = v3 - v1;
        v9 = v5;
        v10 = v8 * v3;
        v1 = (int)(v10 + v5 * v4 + v7 * v6);
        Transform__get_forward();
        v0 = (int)(v8 * v3 + v9 * *((unsigned int *)&v1) + v7 * v10);
        Time__get_deltaTime(0);
        v11 = [D] unsupported_Iop_ZeroHI64ofV128();
        ptr->field_30 = v11;
        Time__get_deltaTime(0);
        v12 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF((unsigned int)v11, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v11, 925353388) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((unsigned int)v11, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v11, 925353388) & 1)) & ((unsigned long long)(char)(CmpF((unsigned int)v11, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v11, 925353388) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v12))
        {
            Time__get_deltaTime(0);
            *((long long *)&ptr->field_38[0]) = [D] unsupported_Iop_ZeroHI64ofV128();
        }
        if (!g_1fab243)
        {
            sub_f7d92c("_F");
            g_1fab243 = 1;
        }
        if (!g_1ef07e8->field_e0)
            sub_f7da5c(g_1ef07e8);
        v14 = [D] unsupported_Iop_SqrtF32();
        v15 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v14, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v14, 0x3f000000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v14, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v14, 0x3f000000) & 1)) & ((unsigned long long)(char)(CmpF(v14, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(v14, 0x3f000000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v15)
            goto LABEL_106e464;
        v2 = ptr->field_28;
        if (v2 && (NavMeshAgent__get_remainingDistance(v2, 0), v2 = (unsigned int [13])ptr->field_28, v2))
        {
            NavMeshAgent__get_radius(v2, 0);
            v16 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v14, v14)) >> 5 & 3 | (unsigned long long)(CmpF(v14, v14) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v14, v14)) >> 5 & 3 | (unsigned long long)(CmpF(v14, v14) & 1)) & ((unsigned long long)(char)(CmpF(v14, v14)) >> 5 & 3 | (unsigned long long)(CmpF(v14, v14) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
LABEL_106e464:
            v2 = ptr->field_20;
            if (v2 && (Animator__SetBool(v2, g_1f13c88), v2 = (unsigned int [13])ptr->field_20, v2 && (Animator__SetFloat(v2, g_1f157d0, 0), v2 = (unsigned int [13])ptr->field_20, v2)))
            {
                Animator__SetFloat(v2, g_1f157d8, 0);
                v2 = sub_1231bc8(ptr, g_1efd000);
                if (ptr->field_28 && (p = v2, NavMeshAgent__get_steeringTarget(ptr->field_28, 0), v2 = (unsigned int [13])ptr->field_28, v2 && (v2 = (unsigned int [13])Component__get_transform(v2, 0), v2 && (v2 = (unsigned int [13])(unsigned long long)Transform__get_forward(), p))))
                {
                    v18 = ptr->field_38[1] * 2;
                    p[10] = v18;
                    p[11] = 0x7e000000;
                    p[12] = 2083730228;
                    addr = sub_1231bc8(ptr, g_1efd000);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (((char)Object__op_Implicit(addr, 0) & 1))
                    {
                        v2 = ptr->field_28;
                        if (v2 && (NavMeshAgent__get_steeringTarget(v2, 0), v2 = (unsigned int [13])ptr->field_28, v2 && (v2 = (unsigned int [13])Component__get_transform(v2, 0), v2 && (v2 = (unsigned int [13])(unsigned long long)Transform__get_forward(), addr))))
                        {
                            addr[10] = v18 * 2;
                            addr[11] = 0xfc000000;
                            addr[12] = 4167460456;
                            goto LABEL_106e5c0;
                        }
                    }
                    else
                    {
LABEL_106e5c0:
                        if (!g_1fab3df)
                        {
                            sub_f7d92c("_F");
                            g_1fab3df = 1;
                        }
                        if (!g_1ef07e8->field_e0)
                            sub_f7da5c(g_1ef07e8);
                        v2 = ptr->field_28;
                        if (v2)
                        {
                            v20 = v9 * v9;
                            v21 = v7 * v7;
                            v22 = v8 * v8 + v9 * v9 + v7 * v7;
                            v23 = [D] unsupported_Iop_SqrtF32();
                            v2 = NavMeshAgent__get_radius(v2, 0);
                            v24 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v23, v22)) >> 5 & 3 | (unsigned long long)(CmpF(v23, v8 * v8 + v20 + v21) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v23, v8 * v8 + v9 * v9 + v7 * v7)) >> 5 & 3 | (unsigned long long)(CmpF(v23, v8 * v8 + v9 * v9 + v7 * v7) & 1)) & ((unsigned long long)(char)(CmpF(v23, v8 * v8 + v9 * v9 + v7 * v7)) >> 5 & 3 | (unsigned long long)(CmpF(v23, v8 * v8 + v9 * v9 + v7 * v7) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if ((char)v24)
                            {
                                return v2;
                            }
                            else if (ptr->field_28)
                            {
                                v2 = Component__get_transform(ptr->field_28, 0);
                                if (v2)
                                    Transform__get_position();
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v2);
}
```

## `LocomotionSimpleAgent.OnAnimatorMove` — RVA `0xc6e6b4`

- Decompiled symbol: `LocomotionSimpleAgent_OnAnimatorMove`
- Metadata signature: `private void OnAnimatorMove() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

void LocomotionSimpleAgent_OnAnimatorMove(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long v5;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr->field_28;
    if (v4)
    {
        v5 = Component__get_transform(v4, 0);
        v4 = v5;
        if (ptr->field_28)
        {
            v4 = NavMeshAgent__get_nextPosition(ptr->field_28, 0);
            if (v5)
            {
                Transform__set_position();
                return;
            }
        }
    }
    sub_f7db74(v4);
}
```

## `LocomotionSimpleAgent.ctor` — RVA `0xc6e6fc`

- Decompiled symbol: `LocomotionSimpleAgent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `100` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef22b8;
extern char g_1fab1e0;

void LocomotionSimpleAgent_ctor(unsigned long long *ptr)
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
    if (!g_1fab1e0)
    {
        sub_f7d92c(&g_1ef22b8);
        g_1fab1e0 = 1;
    }
    ptr[6] = g_1ef22b8->field_b8->field_0;
    ptr[7] = g_1ef22b8->field_b8->field_0;
    MonoBehaviour__ctor();
    return;
}
```
