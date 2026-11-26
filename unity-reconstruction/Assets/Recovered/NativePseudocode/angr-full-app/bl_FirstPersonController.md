# Native pseudocode: bl_FirstPersonController

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_FirstPersonController.Start` — RVA `0xce074c`

- Decompiled symbol: `bl_FirstPersonController_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `308` bytes
- Result: `pseudocode`

```c
extern long long g_1efcf18;
extern long long g_1efcf60;
extern char g_1fab639;

void bl_FirstPersonController_Start(void* ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned int v14;  // s0
    unsigned int v15;  // s1
    unsigned int v16;  // s2
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    long long v8;  // x1
    void* p;  // x0
    unsigned long v10;  // x0
    void* addr;  // x20
    void* ptr3;  // x20
    unsigned long v13;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab639 & 1))
    {
        sub_f7d92c(&g_1efcf18);
        sub_f7d92c(&g_1efcf60);
        g_1fab639 = 1;
    }
    v8 = sub_1231bc8(ptr, g_1efcf60);
    p = ptr;
    *((long long *)&p[184]) = v8;
    sub_f7d8d0(p + 184, v8);
    v10 = Camera__get_main(0);
    addr = ptr;
    *((unsigned long *)&addr[144]) = v10;
    ptr3 = addr + 144;
    sub_f7d8d0(ptr3, v10);
    v13 = *((long long *)ptr3);
    if (v13)
    {
        v13 = Component__get_transform(v13, 0);
        if (v13)
        {
            Transform__get_localPosition();
            v13 = (long long)ptr[80];
            *((unsigned int *)&ptr[200]) = v14;
            *((unsigned int *)&ptr[204]) = v15;
            *((unsigned int *)&ptr[208]) = v16;
            if (v13)
                bl_FOVKick__Setup(v13, (long long)ptr[144]); /* do not return */
        }
    }
    sub_f7db74(v13);
}
```

## `bl_FirstPersonController.Update` — RVA `0xce08d0`

- Decompiled symbol: `bl_FirstPersonController_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `188` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_FirstPersonController_Recovered` matched 5 offsets against `bl_FirstPersonController` metadata (confidence 0.83).

```c
typedef struct bl_FirstPersonController_Recovered {
    char padding_0[104];
    unsigned long long m_JumpBob;
    char padding_70[40];
    char m_Jump;
    char padding_99[19];
    unsigned int field_ac;
    char padding_b0[8];
    unsigned long long m_CharacterController;
    char padding_c0[4];
    char m_PreviouslyGrounded;
    char padding_c5[23];
    char m_Jumping;
} bl_FirstPersonController_Recovered;

unsigned long long bl_FirstPersonController_Update(struct_0 *ptr)
{
    unsigned long v0;  // x0
    unsigned long long v2;  // x0

    bl_FirstPersonController__RotateView();
    if (!ptr->field_98)
        ptr->field_98 = (char)Input__GetKeyDown(32, 0) & 1;
    if (!ptr->field_c4)
    {
        v0 = ptr->field_b8;
        if (!v0)
        {
            sub_f7db74(v0);
        }
        else if (((char)CharacterController__get_isGrounded(v0, 0) & 1))
        {
            v0 = ptr->field_68;
            if (!v0)
                sub_f7db74(v0);
            MonoBehaviour__StartCoroutine(ptr, bl_LerpControlledBob__DoBobCycle(v0), 0);
            bl_FirstPersonController__PlayLandingSound(ptr);
            ptr->field_ac = 0;
            ptr->field_dc = 0;
        }
    }
    v0 = ptr->field_b8;
    if (!v0)
        sub_f7db74(v0);
    if (!((char)CharacterController__get_isGrounded(v0, 0) & 1) && !ptr->field_dc && ptr->field_c4)
        ptr->field_ac = 0;
    v0 = ptr->field_b8;
    if (v0)
    {
        v2 = CharacterController__get_isGrounded(v0, 0);
        ptr->field_c4 = (char)v2 & 1;
        return v2;
    }
    sub_f7db74(v0);
}
```

## `bl_FirstPersonController.RotateView` — RVA `0xce098c`

- Decompiled symbol: `bl_FirstPersonController_RotateView`
- Metadata signature: `private void RotateView() { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
long long bl_FirstPersonController_RotateView(long long *a0)
{
    unsigned long v0;  // x0
    unsigned long v1;  // x0
    unsigned long long v2;  // x0

    v0 = Component__get_transform();
    if (a0[18])
    {
        v1 = Component__get_transform(a0[18], 0);
        if (a0[8])
        {
            v2 = bl_MouseLook__LookRotation(a0[8], v0, v1);
            return bl_MouseLook__LookRotation(a0[8], v0, v1);
        }
    }
    sub_f7db74();
}
```

## `bl_FirstPersonController.PlayLandingSound` — RVA `0xce09dc`

- Decompiled symbol: `bl_FirstPersonController_PlayLandingSound`
- Metadata signature: `private void PlayLandingSound() { }`
- Native interval: `72` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_FirstPersonController_Recovered` matched 4 offsets against `bl_FirstPersonController` metadata (confidence 1.00).

```c
typedef struct bl_FirstPersonController_Recovered {
    char padding_0[136];
    long long m_LandSound;
    char padding_90[68];
    unsigned int m_StepCycle;
    unsigned int m_NextStep;
    char padding_dc[4];
    unsigned long long m_AudioSource;
} bl_FirstPersonController_Recovered;

unsigned long long bl_FirstPersonController_PlayLandingSound(struct_0 *ptr)
{
    unsigned long long v0;  // x0
    unsigned long long v1;  // x0

    v0 = ptr->field_e0;
    if (v0)
    {
        AudioSource__set_clip(v0, ptr->field_88, 0);
        v0 = ptr->field_e0;
        if (v0)
        {
            v1 = AudioSource__Play(v0, 0);
            ptr->field_d8 = ptr->field_d4 + 0x3f000000;
            return v1;
        }
    }
    sub_f7db74(v0);
}
```

## `bl_FirstPersonController.FixedUpdate` — RVA `0xce0a24`

- Decompiled symbol: `bl_FirstPersonController_FixedUpdate`
- Metadata signature: `private void FixedUpdate() { }`
- Native interval: `1060` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_FirstPersonController_Recovered` matched 9 offsets against `bl_FirstPersonController` metadata (confidence 0.75).

```c
typedef struct bl_FirstPersonController_Recovered {
    char padding_0[48];
    unsigned int m_JumpSpeed;
    unsigned int m_StickToGroundForce;
    unsigned int m_GravityMultiplier;
    char padding_3c[92];
    char m_Jump;
    char padding_99[7];
    unsigned int m_Input;
    unsigned int field_a4;
    unsigned int m_MoveDir;
    unsigned int field_ac[2];
    unsigned int field_b0;
    char padding_b4[4];
    long long m_CharacterController;
    unsigned int m_CollisionFlags;
    char padding_c4[24];
    char m_Jumping;
} bl_FirstPersonController_Recovered;

typedef struct struct_3 {
    unsigned int field_0;
    char padding_4[4];
    unsigned int field_8;
    char padding_c[24];
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_3 *field_b8;
} struct_2;

extern struct_0 *g_1ef0e48;
extern struct_2 *g_1ef22e8;
extern char g_1fab2c8;
extern char g_1fab2c9;
extern char g_1fab590;
extern char g_1fab63a;
extern char g_1fab67e;

long long bl_FirstPersonController_FixedUpdate(struct_1 *ptr)
{
    unsigned int v12;  // s14
    unsigned int v13;  // s15
    unsigned long v22;  // 4257
    unsigned int v23;  // s1
    unsigned int v24;  // s1
    unsigned long v25;  // 4205
    unsigned int v26;  // s0
    unsigned int v27;  // s1
    long long v28;  // x0
    unsigned int v29;  // s0
    unsigned int v30;  // w8
    int v31;  // q0
    unsigned int p[12];  // x8
    unsigned long long v32;  // x0
    unsigned int v15;  // s1
    unsigned int v16;  // s2
    unsigned int v17;  // s10
    unsigned int v18;  // s11
    unsigned int v19;  // s2
    unsigned int v20;  // s0
    unsigned int v21;  // s12
    unsigned int v0;  // [bp-0xd4]
    unsigned int v1;  // [bp-0xd0]
    unsigned int v2;  // [bp-0xcc]
    unsigned int v3;  // [bp-0xc8]
    unsigned int v4;  // [bp-0xc4]
    unsigned int v5;  // [bp-0xc0]
    unsigned int flag;  // [bp-0xbc]
    int v7;  // [bp-0xb0], Other Possible Types: unsigned int
    int flag3;  // [bp-0xa0]
    uint128_t flag4;  // [bp-0x90]
    uint128_t flag2;  // [bp-0x84]
    unsigned int choice;  // [bp-0x24]

    if (!(g_1fab63a & 1))
    {
        sub_f7d92c(&g_1ef0e48);
        g_1fab63a = 1;
    }
    choice = 0;
    flag2 = 0;
    flag3 = 0;
    flag4 = 0;
    bl_FirstPersonController__GetInput(ptr, &choice);
    if (Component__get_transform(ptr, 0))
    {
        Transform__get_forward();
        v12 = ptr->field_a4;
        if (Component__get_transform(ptr, 0))
        {
            Transform__get_right();
            v13 = ptr->field_a0;
            if (Component__get_transform(ptr, 0))
            {
                Transform__get_position();
                v7 = 0;
                if (*((long long *)&ptr->padding_b4))
                {
                    CharacterController__get_radius(*((long long *)&ptr->padding_b4), 0);
                    flag = 0;
                    if (!g_1fab590)
                    {
                        sub_f7d92c(&g_1ef22e8);
                        g_1fab590 = 1;
                    }
                    if (*((long long *)&ptr->padding_b4))
                    {
                        p = g_1ef22e8->field_b8;
                        v1 = p[10];
                        v2 = p[9];
                        v0 = p[11];
                        CharacterController__get_height(*((long long *)&ptr->padding_b4), 0);
                        if (!g_1ef0e48->field_e0)
                            sub_f7da5c(g_1ef0e48);
                        v4 = v15 * v12;
                        v5 = v16 * v12;
                        v3 = 0 * v12;
                        Physics__SphereCast(&flag3, 0);
                        RaycastHit__get_normal(&flag3, 0);
                        v17 = v7;
                        if (!g_1fab67e)
                        {
                            sub_f7d92c("aF");
                            g_1fab67e = 1;
                        }
                        v18 = v3 + 0 * v13;
                        v19 = g_1ef07f0->field_b8->field_0;
                        v20 = v16 * v16 + v17 * v17 + v15 * v15;
                        v21 = v5 + v16 * v13;
                        v22 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v20, v19)) >> 5 & 3 | (unsigned long long)(CmpF(v20, v19) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v20, v19)) >> 5 & 3 | (unsigned long long)(CmpF(v20, v19) & 1)) & ((unsigned long long)(char)(CmpF(v20, v19)) >> 5 & 3 | (unsigned long long)(CmpF(v20, v19) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v22))
                        {
                            v23 = v21 * v16 + v18 * v17 + (v4 + v15 * v13) * v15;
                            v18 -= v17 * v23 / v20;
                            v21 -= v16 * v23 / v20;
                        }
                        if (!g_1fab2c8)
                        {
                            sub_f7d92c("_F");
                            g_1fab2c8 = 1;
                        }
                        if (!g_1ef07e8->field_e0)
                            sub_f7da5c(g_1ef07e8);
                        v24 = [D] unsupported_Iop_SqrtF32();
                        v25 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v24, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v24, 925353388) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v24, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v24, 925353388) & 1)) & ((unsigned long long)(char)(CmpF(v24, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v24, 925353388) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v25))
                        {
                            v26 = v18 / v24;
                            v27 = v21 / v24;
                        }
                        else
                        {
                            if (!g_1fab2c9)
                            {
                                sub_f7d92c(&g_1ef22e8);
                                g_1fab2c9 = 1;
                            }
                            v26 = g_1ef22e8->field_b8->field_0;
                            v27 = g_1ef22e8->field_b8->field_8;
                        }
                        v28 = *((long long *)&ptr->padding_b4);
                        v29 = v26 * choice;
                        ptr->field_a8 = v29;
                        ptr->field_ac[1] = v27 * choice;
                        if (v28)
                        {
                            if (((char)CharacterController__get_isGrounded(v28, 0) & 1))
                            {
                                v30 = ptr->field_98;
                                v31 = (int)-(ptr->field_34);
                                ptr->field_ac[0] = *((unsigned int *)&v31);
                                if (v30)
                                {
                                    ptr->field_ac[0] = ptr->field_30;
                                    bl_FirstPersonController__PlayJumpSound(ptr);
                                    v31 = (int)ptr->field_ac[0];
                                    ptr->field_98 = 0;
                                    ptr->padding_c4[16] = 1;
                                }
                            }
                            else
                            {
                                if (!g_1ef0e48->field_e0)
                                    sub_f7da5c(g_1ef0e48);
                                Physics__get_gravity(0);
                                Time__get_fixedDeltaTime(0);
                                v31 = (int)[D] unsupported_Iop_ZeroHI64ofV128();
                                ptr->field_a8 = ptr->field_a8 + v29 * ptr->field_38 * v29;
                                *((unsigned long long *)&ptr->field_ac[0]) = *((unsigned long long *)&v31);
                            }
                            v7 = v31;
                            Time__get_fixedDeltaTime(0);
                            if (*((long long *)&ptr->padding_b4))
                            {
                                *((unsigned int *)&ptr->field_b8) = CharacterController__Move(*((long long *)&ptr->padding_b4), 0);
                                bl_FirstPersonController__ProgressStepCycle(ptr);
                                v32 = bl_FirstPersonController__UpdateCameraPosition(ptr);
                                return bl_FirstPersonController__UpdateCameraPosition(ptr);
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

## `bl_FirstPersonController.GetInput` — RVA `0xce0e48`

- Decompiled symbol: `bl_FirstPersonController_GetInput`
- Metadata signature: `private void GetInput(out float speed) { }`
- Native interval: `520` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_FirstPersonController_Recovered` matched 5 offsets against `bl_FirstPersonController` metadata (confidence 0.71).

```c
typedef struct struct_3 {
    char padding_0[224];
    unsigned int field_e0;
} struct_3;

typedef struct bl_FirstPersonController_Recovered {
    unsigned int field_0;
    char padding_4[28];
    char m_IsWalking;
    char padding_21[39];
    char m_UseFovKick;
    char padding_49[7];
    long long m_FovKick;
    char padding_58[72];
    unsigned int m_Input;
    unsigned int field_a4;
    char padding_a8[16];
    long long m_CharacterController;
} bl_FirstPersonController_Recovered;

typedef struct struct_4 {
    char padding_0[224];
    unsigned int field_e0;
} struct_4;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_1;

extern struct_1 *g_1ef22b8;
extern long long g_1f0ab18;
extern long long g_1f0f998;
extern char g_1fab1e0;
extern char g_1fab243;
extern char g_1fab63b;

struct_3 * bl_FirstPersonController_GetInput(struct_0 *ptr, unsigned int *p)
{
    unsigned int v0;  // w21
    unsigned int v1;  // s0
    unsigned long v9;  // 4186
    struct_3 *v10;  // x0, Other Possible Types: struct_4 *
    unsigned int v11;  // s0
    unsigned long v12;  // 4179
    unsigned long v13;  // x0
    struct_3 *v14;  // x0
    unsigned int v15;  // s0
    unsigned long v18;  // 4190
    unsigned int v2;  // s9
    long long v19;  // x0
    unsigned long long v3;  // x9
    unsigned int v4;  // w8
    unsigned long v5;  // 4128
    unsigned int v6;  // s2
    unsigned long v7;  // d0
    unsigned int v8;  // s1

    if (!(g_1fab63b & 1))
    {
        sub_f7d92c(&g_1f0f998);
        sub_f7d92c(&g_1f0ab18);
        g_1fab63b = 1;
    }
    Input__GetAxis(g_1f0ab18, 0);
    Input__GetAxis(g_1f0f998, 0);
    v0 = ptr->field_20;
    v2 = v1;
    v10 = Input__GetKey(304, 0);
    v3 = 36;
    v4 = ~((unsigned int)v10) & 1;
    v5 = arm64g_calculate_condition(25, (unsigned long long)((unsigned int)v10 & 1), 0, 0);
    if ((char)v5)
        v3 = 40;
    ptr->field_20 = v4;
    v6 = *((int *)((char *)ptr + v3));
    v7 = v1 * v1 + v2 * v2;
    v8 = 0x3f800000;
    *(p) = v6;
    ptr->field_a0 = v1;
    ptr->field_a4 = v2;
    v9 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF((unsigned int)v7, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v7, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((unsigned int)v7, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v7, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF((unsigned int)v7, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v7, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v9))
    {
        if (!g_1fab243)
        {
            sub_f7d92c("_F");
            g_1fab243 = 1;
            v2 = ptr->field_a4;
        }
        v10 = g_1ef07e8;
        if (!g_1ef07e8->field_e0)
            v10 = sub_f7da5c(g_1ef07e8);
        v8 = 925353388;
        v6 = v2 * v2;
        v11 = [D] unsupported_Iop_SqrtF32();
        v12 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v11, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v11, 925353388) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v11, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v11, 925353388) & 1)) & ((unsigned long long)(char)(CmpF(v11, 925353388)) >> 5 & 3 | (unsigned long long)(CmpF(v11, 925353388) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v12))
        {
            v8 = *((long long *)&ptr->field_a0);
            v7 = [D] unsupported_Iop_ZeroHI64ofV128();
        }
        else
        {
            if (!g_1fab1e0)
            {
                v10 = sub_f7d92c(&g_1ef22b8);
                g_1fab1e0 = 1;
            }
            v7 = g_1ef22b8->field_b8->field_0;
        }
        v4 = ptr->field_20;
        *((unsigned long *)&ptr->field_a0) = v7;
    }
    if (v4 == v0)
    {
        return v10;
    }
    else if (ptr->field_48)
    {
        v13 = ptr->field_b8;
        if (v13)
        {
            v14 = CharacterController__get_velocity(v13, 0);
            v15 = (unsigned int)v7 * (unsigned int)v7;
            v18 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v6 * v6 + (unsigned int)v7 * (unsigned int)v7 + v8 * v8, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v6 * v6 + v15 + v8 * v8, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v6 * v6 + (unsigned int)v7 * (unsigned int)v7 + v8 * v8, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v6 * v6 + (unsigned int)v7 * (unsigned int)v7 + v8 * v8, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v6 * v6 + v15 + v8 * v8, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v6 * v6 + (unsigned int)v7 * (unsigned int)v7 + v8 * v8, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v18)
                return v14;
            MonoBehaviour__StopAllCoroutines(ptr, 0);
            v13 = ptr->field_50;
            if (v13)
            {
                if (ptr->field_20)
                    bl_FOVKick__FOVKickDown(v13);
                else
                    bl_FOVKick__FOVKickUp(v13);
                v19 = MonoBehaviour__StartCoroutine();
                return MonoBehaviour__StartCoroutine();
            }
        }
        sub_f7db74(v13);
    }
    else
    {
        return v10;
    }
}
```

## `bl_FirstPersonController.PlayJumpSound` — RVA `0xce1050`

- Decompiled symbol: `bl_FirstPersonController_PlayJumpSound`
- Metadata signature: `private void PlayJumpSound() { }`
- Native interval: `52` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_FirstPersonController_Recovered` matched 2 offsets against `bl_FirstPersonController` metadata (confidence 1.00).

```c
typedef struct bl_FirstPersonController_Recovered {
    char padding_0[128];
    long long m_JumpSound;
    char padding_88[88];
    unsigned long long m_AudioSource;
} bl_FirstPersonController_Recovered;

void bl_FirstPersonController_PlayJumpSound(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr->field_e0;
    if (v4)
    {
        AudioSource__set_clip(v4, ptr->field_80, 0);
        v4 = ptr->field_e0;
        if (ptr->field_e0)
        {
            AudioSource__Play();
            return;
        }
    }
    sub_f7db74(v4);
}
```

## `bl_FirstPersonController.ProgressStepCycle` — RVA `0xce1084`

- Decompiled symbol: `bl_FirstPersonController_ProgressStepCycle`
- Metadata signature: `private void ProgressStepCycle(float speed) { }`
- Native interval: `332` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_FirstPersonController_Recovered` matched 7 offsets against `bl_FirstPersonController` metadata (confidence 0.88).

```c
typedef struct bl_FirstPersonController_Recovered {
    char padding_0[32];
    char m_IsWalking;
    char padding_21[11];
    unsigned int m_RunstepLenghten;
    char padding_30[64];
    unsigned int m_StepInterval;
    char padding_74[44];
    unsigned int m_Input;
    unsigned int field_a4;
    char padding_a8[16];
    unsigned long long m_CharacterController;
    char padding_c0[20];
    unsigned int m_StepCycle;
    unsigned int m_NextStep;
} bl_FirstPersonController_Recovered;

extern char g_1fab3df;

unsigned long long bl_FirstPersonController_ProgressStepCycle(struct_0 *ptr)
{
    unsigned long long v0;  // x0
    unsigned long long v1;  // x0
    unsigned int v10;  // s0
    unsigned long long v11;  // 4103
    unsigned int v12;  // 4099
    unsigned long v13;  // 4115
    unsigned int v14;  // s12
    unsigned int v15;  // s9
    unsigned int v16;  // s10
    unsigned int v17;  // s0
    unsigned int v18;  // s1
    unsigned long v19;  // 4133
    unsigned int v2;  // s0
    unsigned long long v20;  // x0
    unsigned int v4;  // s1
    unsigned int v6;  // s2
    unsigned int v7;  // s1
    unsigned long v9;  // 4190

    v0 = ptr->field_b8;
    if (v0)
    {
        v1 = CharacterController__get_velocity(v0, 0);
        v7 = v6 * v6;
        v9 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v7 + v2 * v2 + v4 * v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7 + v2 * v2 + v4 * v4, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7 + v2 * v2 + v4 * v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7 + v2 * v2 + v4 * v4, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v7 + v2 * v2 + v4 * v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v7 + v2 * v2 + v4 * v4, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v9))
        {
            v10 = ptr->field_a0;
            v11 = (((CmpF(v10, 0.0) >> 5 & 3 | CmpF(v10, 0.0) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v10, 0.0) >> 5 & 3 | CmpF(v10, 0.0) & 1) & (CmpF(v10, 0.0) >> 5 & 3 | CmpF(v10, 0.0) & 1) >> 1 & 1);
            if (!((char)(v11 * 0x10000000 >> 30)) || (v10 = ptr->field_a4, v12 = (unsigned int)(CmpF(v10, 0.0)), v13 = (unsigned long)(((((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1), !((char)((v13 - (((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) & ((unsigned long long)v12 >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) >> 1 & 1)) * 0x10000000 >> 30))))
            {
                v0 = ptr->field_b8;
                if (!v0)
                    sub_f7db74(v0);
                v14 = ptr->field_d4;
                CharacterController__get_velocity(v0, 0);
                if (!g_1fab3df)
                {
                    sub_f7d92c("_F");
                    g_1fab3df = 1;
                }
                if (!g_1ef07e8->field_e0)
                    sub_f7da5c(g_1ef07e8);
                v15 = [D] unsupported_Iop_SqrtF32();
                v16 = 0x3f800000;
                if (!ptr->field_20)
                    v16 = ptr->field_2c;
                v1 = Time__get_fixedDeltaTime(0);
                ptr->field_d4 = v14 + (v6 * v6 + v10 * v10 + v7 * v7) * (v15 + v16 * v2);
            }
        }
        v17 = ptr->field_d4;
        v18 = ptr->field_d8;
        v19 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v17, v18)) >> 5 & 3 | (unsigned long long)(CmpF(v17, v18) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v17, v18)) >> 5 & 3 | (unsigned long long)(CmpF(v17, v18) & 1)) & ((unsigned long long)(char)(CmpF(v17, v18)) >> 5 & 3 | (unsigned long long)(CmpF(v17, v18) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v19)
            return v1;
        ptr->field_d8 = v17 + ptr->field_70;
        v20 = bl_FirstPersonController__PlayFootStepAudio(ptr);
        return bl_FirstPersonController__PlayFootStepAudio(ptr);
    }
    sub_f7db74(v0);
}
```

## `bl_FirstPersonController.UpdateCameraPosition` — RVA `0xce11d0`

- Decompiled symbol: `bl_FirstPersonController_UpdateCameraPosition`
- Metadata signature: `private void UpdateCameraPosition(float speed) { }`
- Native interval: `568` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_FirstPersonController_Recovered` matched 6 offsets against `bl_FirstPersonController` metadata (confidence 1.00).

```c
typedef struct bl_FirstPersonController_Recovered {
    char padding_0[32];
    char m_IsWalking;
    char padding_21[55];
    char m_UseHeadBob;
    char padding_59[7];
    struct struct_0 *m_HeadBob;
    unsigned long long m_JumpBob;
    char padding_70[32];
    struct struct_0 *m_Camera;
    char padding_98[32];
    struct struct_0 *m_CharacterController;
} bl_FirstPersonController_Recovered;

typedef struct struct_3 {
    char padding_0[224];
    unsigned int field_e0;
} struct_3;

typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    unsigned int field_30;
    char padding_34[8];
    unsigned int field_3c;
} struct_0;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern char g_1fab3df;

void bl_FirstPersonController_UpdateCameraPosition(struct_1 *ptr)
{
    struct_3 *v0;  // x0
    unsigned int v1;  // s0
    unsigned long v2;  // 4201
    struct_0 *v3;  // x21
    struct_3 *v4;  // x20

    if (!ptr->field_58)
        return;
    v0 = ptr->field_b8;
    if (v0)
    {
        CharacterController__get_velocity(v0, 0);
        if (!g_1fab3df)
        {
            sub_f7d92c("_F");
            g_1fab3df = 1;
        }
        if (!g_1ef07e8->field_e0)
            sub_f7da5c(g_1ef07e8);
        v1 = [D] unsupported_Iop_SqrtF32();
        v2 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v2))
        {
            v0 = ptr->field_b8;
            if (v0)
            {
                if (!(CharacterController__get_isGrounded(v0, 0) & 1))
                    goto LABEL_10e137c;
                v0 = ptr->field_90;
                if (v0 && (v0 = (struct_3 *)Component__get_transform(v0, 0), ptr->field_b8))
                {
                    v3 = ptr->field_60;
                    v4 = v0;
                    CharacterController__get_velocity(ptr->field_b8, 0);
                    if (!g_1fab3df)
                    {
                        sub_f7d92c("_F");
                        g_1fab3df = 1;
                    }
                    v0 = g_1ef07e8;
                    if (!g_1ef07e8->field_e0)
                        v0 = sub_f7da5c(g_1ef07e8);
                    if (v3 && (v0 = (struct_3 *)(long long)bl_CurveControlledBob__DoHeadBob(v3), v4 && (Transform__set_localPosition(v4, 0), v0 = (struct_3 *)ptr->field_90, v0 && (v0 = (struct_3 *)Component__get_transform(v0, 0), v0 && (Transform__get_localPosition(), v0 = (struct_3 *)ptr->field_90, v0 && (v0 = (struct_3 *)Component__get_transform(v0, 0), v0 && (v0 = (struct_3 *)(unsigned long long)Transform__get_localPosition(), ptr->field_68)))))))
                    {
LABEL_10e1374:
                        v0 = ptr->field_90;
                        if (v0)
                        {
                            v0 = Component__get_transform(v0, 0);
                            if (v0)
                            {
                                Transform__set_localPosition();
                                return;
                            }
                        }
                    }
                }
            }
        }
        else
        {
LABEL_10e137c:
            v0 = ptr->field_90;
            if (v0 && (v0 = (struct_3 *)Component__get_transform(v0, 0), v0 && (v0 = (struct_3 *)(unsigned long long)Transform__get_localPosition(), ptr->field_68)))
                goto LABEL_10e1374;
        }
    }
    sub_f7db74(v0);
}
```

## `bl_FirstPersonController.PlayFootStepAudio` — RVA `0xce1408`

- Decompiled symbol: `bl_FirstPersonController_PlayFootStepAudio`
- Metadata signature: `private void PlayFootStepAudio() { }`
- Native interval: `272` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_FirstPersonController_Recovered` matched 3 offsets against `bl_FirstPersonController` metadata (confidence 1.00).

```c
typedef struct bl_FirstPersonController_Recovered {
    char padding_0[120];
    struct struct_0 *m_FootstepSounds;
    char padding_80[56];
    long long m_CharacterController;
    char padding_c0[32];
    long long m_AudioSource;
} bl_FirstPersonController_Recovered;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    long long field_20;
} struct_0;

typedef struct struct_2 {
    char padding_0[32];
    long long field_20;
} struct_2;

long long bl_FirstPersonController_PlayFootStepAudio(struct_1 *ptr, unsigned long a1, unsigned long a2)
{
    unsigned long v0;  // x0
    struct_0 *v1;  // x8
    unsigned long long v2;  // x20
    unsigned long long v3;  // x22
    unsigned long v4;  // x21
    struct_0 *p;  // x8
    long long v6;  // x1
    struct_2 *addr;  // x0
    struct_0 *ptr3;  // x19
    long long v9;  // x0

    v0 = ptr->field_b8;
    if (v0)
    {
        v0 = CharacterController__get_isGrounded(v0, 0);
        if (!((char)v0 & 1))
        {
            return v0;
        }
        else if (ptr->field_78)
        {
            v0 = Random__Range(1, ptr->field_78->field_18, 0);
            v1 = ptr->field_78;
            if (v1)
            {
                v2 = v0 & 4294967295;
                if (v1->field_18 <= (unsigned int)v0)
                    sub_f7db7c(v0);
                v0 = ptr->field_e0;
                if (v0)
                {
                    v3 = v2 * 0x100000000 >> 63 & 0xffffffff00000000 | v2 & 4294967295;
                    v0 = AudioSource__set_clip(v0, (&v1->field_20)[v3], 0);
                    v4 = ptr->field_e0;
                    if (v4)
                    {
                        v0 = AudioSource__PlayOneShot(v4, AudioSource__get_clip(v4, 0), 0);
                        p = ptr->field_78;
                        if (p)
                        {
                            if (!p->field_18)
                            {
                                sub_f7db7c(v0);
                            }
                            else if (p->field_18 > (unsigned int)v2)
                            {
                                v6 = p->field_20;
                                addr = &p->padding_0[8 * v3];
                                addr->field_20 = v6;
                                sub_f7d8d0((struct struct_2 *)&addr->field_20, v6);
                                v0 = ptr->field_e0;
                                if (v0)
                                {
                                    ptr3 = ptr->field_78;
                                    v0 = AudioSource__get_clip(v0, 0);
                                    if (ptr3)
                                    {
                                        if (ptr3->field_18)
                                        {
                                            ptr3->field_20 = v0;
                                            v9 = sub_f7d8d0();
                                            return sub_f7d8d0();
                                        }
                                        sub_f7db7c(v0);
                                    }
                                }
                            }
                            else
                            {
                                sub_f7db7c(v0);
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db7c(sub_f7db74(v0));
}
```

## `bl_FirstPersonController.OnControllerColliderHit` — RVA `0xce183c`

- Decompiled symbol: `bl_FirstPersonController_OnControllerColliderHit`
- Metadata signature: `private void OnControllerColliderHit(ControllerColliderHit hit) { }`
- Native interval: `292` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_FirstPersonController_Recovered` matched 2 offsets against `bl_FirstPersonController` metadata (confidence 1.00).

```c
typedef struct bl_FirstPersonController_Recovered {
    char padding_0[184];
    long long m_CharacterController;
    unsigned int m_CollisionFlags;
} bl_FirstPersonController_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab63c;

long long bl_FirstPersonController_OnControllerColliderHit(struct_1 *a0, long long a1)
{
    long long v0;  // x0
    long long v1;  // x20
    long long v2;  // x0
    long long v3;  // x0
    unsigned long long v4;  // x0

    if (!(g_1fab63c & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab63c = 1;
    }
    if (a1 && ControllerColliderHit__get_collider(a1, 0))
    {
        v0 = Collider__get_attachedRigidbody();
        if (a0->field_c0 == 4)
            return v0;
        v1 = v0;
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v2 = Object__op_Equality(v1, 0, 0);
        if (((char)v2 & 1))
        {
            return v2;
        }
        else if (v1)
        {
            v3 = Rigidbody__get_isKinematic(v1, 0);
            if (((char)v3 & 1))
            {
                return v3;
            }
            else if (a0->field_b8)
            {
                CharacterController__get_velocity(a0->field_b8, 0);
                ControllerColliderHit__get_point(a1, 0);
                v4 = Rigidbody__AddForceAtPosition();
                return Rigidbody__AddForceAtPosition();
            }
        }
    }
    sub_f7db74();
}
```

## `bl_FirstPersonController.ctor` — RVA `0xce1960`

- Decompiled symbol: `bl_FirstPersonController_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `308` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[28];
    unsigned long long field_1c;
    unsigned int field_24;
} struct_0;

typedef struct struct_2 {
    unsigned long long field_0;
    unsigned int field_8;
} struct_2;

typedef struct struct_3 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_3;

extern struct_3 *g_1ef22e8;
extern long long g_1ef2ae0;
extern long long g_1ef2ae8;
extern long long g_1ef2af0;
extern char g_1fab2c9;
extern char g_1fab63d;

void bl_FirstPersonController_ctor(void* ptr)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    long long v16;  // x20
    void* addr;  // x0
    unsigned int v18;  // s1
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    struct_0 *p;  // x20
    void* ptr3;  // x0
    unsigned long v14;  // x20
    void* ptr4;  // x0
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
    if (!(g_1fab63d & 1))
    {
        sub_f7d92c(&g_1ef2ae0);
        sub_f7d92c(&g_1ef2ae8);
        sub_f7d92c(&g_1ef2af0);
        g_1fab63d = 1;
    }
    p = sub_f7db70(g_1ef2ae8);
    *((unsigned long long *)&(&p->padding_0)[1]) = 0x3f80000040400000;
    *((unsigned int *)((char *)&p->field_1c + 4)) = 0x3f800000;
    Object__ctor(p, 0);
    ptr3 = ptr;
    *((struct_0 **)&ptr3[80]) = p;
    sub_f7d8d0(ptr3 + 80, p);
    v14 = sub_f7db70(g_1ef2ae0);
    bl_CurveControlledBob__ctor(v14);
    ptr4 = ptr;
    *((unsigned long *)&ptr4[96]) = v14;
    sub_f7d8d0(ptr4 + 96, v14);
    v16 = sub_f7db70(g_1ef2af0);
    Object__ctor(v16, 0);
    addr = ptr;
    *((long long *)&addr[104]) = v16;
    sub_f7d8d0(addr + 104, v16);
    if (!g_1fab2c9)
    {
        sub_f7d92c(&g_1ef22e8);
        g_1fab2c9 = 1;
    }
    v18 = g_1ef22e8->field_b8->field_8;
    *((unsigned long long *)&ptr[168]) = g_1ef22e8->field_b8->field_0;
    *((unsigned int *)&ptr[176]) = v18;
    MonoBehaviour__ctor();
    return;
}
```
