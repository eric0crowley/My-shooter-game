# Native pseudocode: my_AI

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `my_AI.ChangePosition` — RVA `0xc6d3fc`

- Decompiled symbol: `my_AI_ChangePosition`
- Metadata signature: `public void ChangePosition() { }`
- Native interval: `68` bytes
- Result: `pseudocode`
- Heuristic layout hint: `my_AI_Recovered` matched 2 offsets against `my_AI` metadata (confidence 1.00).

```c
typedef struct my_AI_Recovered {
    char padding_0[200];
    unsigned long long myAgent;
    char padding_d0[24];
    long long CurrentPosition;
} my_AI_Recovered;

void my_AI_ChangePosition(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    my_AI__SetNextPoint();
    v4 = ptr->field_e8;
    if (v4)
    {
        v4 = GameObject__get_transform(v4, 0);
        if (v4)
        {
            v4 = Transform__get_position();
            if (ptr->field_c8)
            {
                NavMeshAgent__SetDestination();
                return;
            }
        }
    }
    sub_f7db74(v4);
}
```

## `my_AI.Start` — RVA `0xc6ee18`

- Decompiled symbol: `my_AI_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `400` bytes
- Result: `pseudocode`
- Heuristic layout hint: `my_AI_Recovered` matched 9 offsets against `my_AI` metadata (confidence 1.00).

```c
typedef struct my_AI_Recovered {
    char padding_0[116];
    unsigned int BulletsToPause;
    unsigned int pauseBulletLeft;
    char padding_7c[8];
    unsigned int rateOfShouting;
    unsigned int NextTimeToShout;
    char padding_8c[60];
    long long myAgent;
    char padding_d0[16];
    struct struct_1 *nextPos;
    long long CurrentPosition;
    unsigned int nextPosPointer;
    char padding_f4[76];
    long long thisManId;
} my_AI_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efd088;
extern long long g_1efd110;
extern char g_1fab357;

int my_AI_Start(struct_2 *ptr)
{
    long long v0;  // x1
    long long v1;  // x0
    long long v2;  // x0
    struct_1 *v3;  // x8
    unsigned long v4;  // x1
    struct_2 *v5;  // x20
    unsigned int v6;  // w0

    if (!(g_1fab357 & 1))
    {
        sub_f7d92c(&g_1efd088);
        sub_f7d92c(&g_1efd110);
        sub_f7d92c(&g_1ef0c58);
        g_1fab357 = 1;
    }
    v0 = sub_1231bc8(ptr, g_1efd088);
    ptr->field_140 = v0;
    sub_f7d8d0(&ptr->field_140, v0);
    if (Component__get_transform(ptr, 0))
    {
        v1 = sub_1231bc8();
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!((char)Object__op_Implicit(v1, 0) & 1))
        {
LABEL_106eee4:
            if (ptr->field_e0)
            {
                v2 = Random__Range(0, ptr->field_e0->field_18, 0);
                v3 = ptr->field_e0;
                ptr->field_f0 = v2;
                if (v3)
                {
                    if (v3->field_18 > (int)v2)
                    {
                        v4 = *((long long *)&v3[1].padding_0[4 + 8 * (v2 & 4294967295)]);
                        ptr->field_e8 = v4;
                        v5 = &ptr->field_e8;
                        sub_f7d8d0(v5, v4);
                        if (*((long long *)&v5->padding_0[0]) && GameObject__get_transform(*((long long *)&v5->padding_0[0]), 0))
                        {
                            Transform__get_position();
                            if (*((long long *)&v5->padding_0[32]))
                            {
                                NavMeshAgent__SetDestination(*((long long *)&v5->padding_0[32]), 0);
                                ptr->field_78 = ptr->field_74;
                                Random__Range(0);
                                ptr->field_84 = 0;
                                v6 = Time__get_time(0);
                                ptr->field_88 = 0 + 0x41a00000 / ptr->field_84;
                                return v6;
                            }
                        }
                    }
                    else
                    {
                        sub_f7db7c(v2);
                    }
                }
            }
        }
        else if (ptr->field_c8)
        {
            NavMeshAgent__set_speed(ptr->field_c8, 0);
            goto LABEL_106eee4;
        }
    }
    v2 = sub_f7db74();
    sub_f7db7c(v2);
}
```

## `my_AI.Update` — RVA `0xc6efa8`

- Decompiled symbol: `my_AI_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `712` bytes
- Result: `pseudocode`
- Heuristic layout hint: `my_AI_Recovered` matched 19 offsets against `my_AI` metadata (confidence 1.00).

```c
typedef struct my_AI_Recovered {
    char padding_0[32];
    unsigned int DeadAnim;
    unsigned int isDeadAnim;
    unsigned int startMovingAnim;
    unsigned int justRun;
    char padding_30[32];
    unsigned int Petroling;
    unsigned int walkSpeed;
    unsigned int runSpeed;
    unsigned int awareDist;
    char padding_60[36];
    unsigned int rateOfShouting;
    unsigned int NextTimeToShout;
    char padding_8c[52];
    long long myAnimator;
    long long myAgent;
    long long targetPlayer;
    char padding_d8[29];
    char startMoving;
    char padding_f6[1];
    char isJustRunning;
    char padding_f8[8];
    char isDead;
    char padding_101[47];
    struct struct_1 *shoutClip;
    char padding_138[16];
    char isPetrolling;
    char petrollingTrigger;
} my_AI_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    unsigned long long field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efed50;
extern char g_1fab358;

long long my_AI_Update(struct_2 *ptr)
{
    long long v0;  // x0
    unsigned int v1;  // w0
    unsigned long long v10;  // x0
    unsigned long long v2;  // x0
    unsigned int v3;  // s0
    unsigned long v4;  // 4125
    unsigned int v5;  // s0
    unsigned long v6;  // 4125
    long long v7;  // x0
    unsigned int v8;  // s1
    unsigned long v9;  // 4129

    if (!(g_1fab358 & 1))
    {
        sub_f7d92c(&g_1efed50);
        sub_f7d92c(&g_1ef0c58);
        g_1fab358 = 1;
    }
    my_AI__GettingPlayerDistance(ptr, ptr->field_d0);
    if (!ptr->field_100)
    {
        v2 = Input__GetKey(323, 0);
        v3 = ptr->field_5c;
        if (((char)v2 & 1) && !((v4 = (unsigned long)arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v3, 0x40a00000)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0x40a00000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, 0x40a00000)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0x40a00000) & 1)) & ((unsigned long long)(char)(CmpF(v3, 0x40a00000)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0x40a00000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), (char)v4)) || !((v6 = (unsigned long)arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v5, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v3) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v5, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v3) & 1)) & ((unsigned long long)(char)(CmpF(v5, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v5, v3) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), (char)v6 || ptr->field_f5)))
        {
            if (ptr->field_c0 && (Animator__SetBool(ptr->field_c0, (unsigned long long)ptr->field_50, 0, 0), v7 = ptr->field_c0, ptr->field_148 = 0, v7 && (Animator__SetBool(v7, (unsigned long long)ptr->field_28, 1, 0), ptr->field_c8)))
            {
                v3 = ptr->field_58;
                NavMeshAgent__set_speed(ptr->field_c8, 0);
                ptr->field_f5 = 1;
                goto LABEL_106f19c;
            }
        }
        else
        {
            if (!ptr->field_148 || ptr->field_149)
                goto LABEL_106f19c;
            if (ptr->field_c8 && (v3 = ptr->field_54, NavMeshAgent__set_speed(ptr->field_c8, 0), ptr->field_c0))
            {
                Animator__SetBool(ptr->field_c0, ptr->field_50, 1, 0);
                ptr->field_149 = 1;
LABEL_106f19c:
                if (ptr->field_f7)
                {
                    if (ptr->field_c8 && (v3 = ptr->field_58, NavMeshAgent__set_speed(ptr->field_c8, 0), ptr->field_c0))
                    {
                        Animator__SetBool(ptr->field_c0, ptr->field_2c, 1, 0);
                        goto LABEL_106f1f4;
                    }
                }
                else
                {
                    if (ptr->field_c0)
                    {
                        Animator__SetBool(ptr->field_c0, ptr->field_2c, 0, 0);
                        my_AI__DetectPlayer(ptr);
LABEL_106f1f4:
                        Time__get_time(0);
                        v8 = ptr->field_88;
                        v9 = arm64g_calculate_condition(176, (((((unsigned long long)(char)(CmpF(v3, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v8) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v8) & 1)) & ((unsigned long long)(char)(CmpF(v3, v8)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v8) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v9)
                        {
                            v10 = my_AI__ForTDM(ptr);
                            return my_AI__ForTDM(ptr);
                        }
                        if (ptr->field_130)
                        {
                            if (ptr->field_130->field_18)
                            {
                                if (ptr->field_f5)
                                {
                                    Random__Range(0);
                                    ptr->field_84 = 0;
                                    Time__get_time(0);
                                    ptr->field_88 = 0 + 0x41a00000 / ptr->field_84;
                                    my_AI__doShout(ptr); /* do not return */
                                }
                                v10 = my_AI__ForTDM(ptr);
                                return my_AI__ForTDM(ptr);
                            }
                            else
                            {
                                v10 = my_AI__ForTDM(ptr);
                                return my_AI__ForTDM(ptr);
                            }
                        }
                    }
                }
            }
        }
    }
    else if (Component__get_gameObject(ptr, 0))
    {
        v0 = sub_1249224();
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!((char)Object__op_Implicit(v0, 0) & 1))
        {
LABEL_106f070:
            if (ptr->field_c8)
            {
                NavMeshAgent__set_speed(ptr->field_c8, 0);
                v1 = Random__Range(1, 5, 0);
                if (ptr->field_c0)
                {
                    Animator__SetInteger(ptr->field_c0, ptr->field_20, v1, 0);
                    if (ptr->field_c0)
                    {
                        Animator__SetBool(ptr->field_c0, ptr->field_24, 1, 0);
                        v10 = my_AI__ForTDM(ptr);
                        return my_AI__ForTDM(ptr);
                    }
                }
            }
        }
        else if (Component__get_gameObject(ptr, 0) && sub_1249224())
        {
            Behaviour__set_enabled();
            goto LABEL_106f070;
        }
    }
    sub_f7db74();
}
```

## `my_AI.GettingPlayerDistance` — RVA `0xc6f270`

- Decompiled symbol: `my_AI_GettingPlayerDistance`
- Metadata signature: `public float GettingPlayerDistance(Transform _target) { }`
- Native interval: `312` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab35f;
extern char g_1fab3df;

struct_1 * my_AI_GettingPlayerDistance(long long a0, long long a1)
{
    struct_1 *v0;  // x0
    struct_2 *v1;  // x0

    if (!(g_1fab35f & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab35f = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Implicit(a1, 0);
    if (!((char)v0 & 1))
        return v0;
    if (a1 && Component__get_transform(a1, 0))
    {
        Transform__get_position();
        if (Component__get_transform(a0, 0))
        {
            Transform__get_position();
            if (!g_1fab3df)
            {
                sub_f7d92c("_F");
                g_1fab3df = 1;
            }
            v1 = g_1ef07e8;
            if (!g_1ef07e8->field_e0)
                v1 = sub_f7da5c(g_1ef07e8);
            return v1;
        }
    }
    sub_f7db74();
}
```

## `my_AI.DetectPlayer` — RVA `0xc6f3a8`

- Decompiled symbol: `my_AI_DetectPlayer`
- Metadata signature: `private void DetectPlayer() { }`
- Native interval: `828` bytes
- Result: `pseudocode`
- Heuristic layout hint: `my_AI_Recovered` matched 16 offsets against `my_AI` metadata (confidence 1.00).

```c
typedef struct my_AI_Recovered {
    char padding_0[48];
    unsigned int isShootingAnim;
    char padding_34[44];
    unsigned int shootRange;
    unsigned int magCapacity;
    char padding_68[4];
    unsigned int rateOfFire;
    unsigned int NextTimeToFire;
    unsigned int BulletsToPause;
    unsigned int pauseBulletLeft;
    unsigned int PauseTime;
    char padding_80[24];
    unsigned long long ShootPoint;
    char padding_a0[32];
    unsigned long long myAnimator;
    char padding_c8[8];
    unsigned long long targetPlayer;
    char padding_d8[28];
    char inCover;
    char padding_f5[1];
    char isShooting;
    char padding_f7[17];
    unsigned long long myAudioSource;
    long long fireBrustClip;
    char padding_118[56];
    unsigned long long FireLight;
} my_AI_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab35b;

struct_1 * my_AI_DetectPlayer(struct_1 *ptr)
{
    struct_1 *v0;  // x0
    struct_1 *v1;  // x0
    unsigned int v10;  // s0
    unsigned long v11;  // 4142
    unsigned int v12;  // s2
    unsigned long v13;  // 4163
    unsigned int v14;  // s0
    unsigned long v15;  // 4129
    unsigned int v16;  // s0
    struct_1 *v17;  // x0
    unsigned int v18;  // s9
    struct_1 *v19;  // x0
    struct_1 *v2;  // x0
    unsigned long v20;  // 4125
    unsigned long long v21;  // x0
    long long v22;  // x0
    long long v23;  // x0
    struct_1 *v3;  // x0
    unsigned long v4;  // x0
    unsigned long v5;  // x20
    struct_1 *v6;  // x0
    unsigned int v7;  // s1
    unsigned long v8;  // 4129
    unsigned int v9;  // s0

    v0 = ptr;
    if (!(g_1fab35b & 1))
    {
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab35b = 1;
        v0 = v1;
    }
    v2 = v0;
    if (!ptr->field_f6)
        return v2;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v3 = Object__op_Implicit(ptr->field_d0, 0);
    if (!((char)v3 & 1))
        return v3;
    v4 = ptr->field_d0;
    if (v4 && (v4 = (unsigned long)Component__get_transform(v4, 0), v4))
    {
        Transform__get_position();
        v4 = Component__get_transform(ptr, 0);
        if (v4 && (Transform__get_position(), v4 = (unsigned long)ptr->field_d0, v4 && (v4 = (unsigned long)Component__get_transform(v4, 0), v4)))
        {
            Transform__get_position();
            v4 = Component__get_transform(ptr, 0);
            if (v4 && (Transform__LookAt(), v4 = (unsigned long)ptr->field_98, v4 && (v4 = (unsigned long)(unsigned long long)GameObject__get_transform(v4, 0), ptr->field_d0 && (v5 = v4, v4 = (unsigned long)Component__get_transform(ptr->field_d0, 0), v5))))
            {
                Transform__LookAt(v5, v4, 0);
                if (ptr->field_f4)
                {
LABEL_106f4d4:
                    v4 = ptr->field_c0;
                    if (v4)
                    {
                        v21 = Animator__SetBool();
                        return Animator__SetBool();
                    }
                }
                else
                {
                    my_AI__GettingPlayerDistance(ptr, ptr->field_d0);
                    v4 = ptr->field_150;
                    if (v4)
                    {
                        Light__set_range(v4, 0);
                        v6 = Time__get_time(0);
                        v7 = ptr->field_70;
                        v8 = arm64g_calculate_condition(176, (((((unsigned long long)(char)(CmpF(0, v7)) >> 5 & 3 | (unsigned long long)(CmpF(0, v7) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(0, v7)) >> 5 & 3 | (unsigned long long)(CmpF(0, v7) & 1)) & ((unsigned long long)(char)(CmpF(0, v7)) >> 5 & 3 | (unsigned long long)(CmpF(0, v7) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v8)
                            return v6;
                        v9 = ptr->field_60 * ptr->field_60;
                        v11 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v10, v9)) >> 5 & 3 | (unsigned long long)(CmpF(v10, v9) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v10, v9)) >> 5 & 3 | (unsigned long long)(CmpF(v10, v9) & 1)) & ((unsigned long long)(char)(CmpF(v10, v9)) >> 5 & 3 | (unsigned long long)(CmpF(v10, v9) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v11)
                            return v6;
                        Time__get_time(0);
                        v12 = ptr->field_64;
                        ptr->field_70 = v9 + 0x3f800000 / ptr->field_6c;
                        v13 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v12, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v12, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v12, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v12, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v12, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v12, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v13))
                        {
                            v14 = ptr->field_78;
                            v15 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v14, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v14, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v14, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v14, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v14, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v14, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if (!((char)v15))
                            {
                                v4 = ptr->field_108;
                                if (v4)
                                {
                                    if (!((char)AudioSource__get_isPlaying(v4, 0) & 1))
                                    {
                                        v4 = ptr->field_108;
                                        if (v4 && (AudioSource__set_volume(v4, 0), v4 = (unsigned long)ptr->field_108, v4 && (AudioSource__set_clip(v4, ptr->field_110, 0), v4 = (unsigned long)ptr->field_108, v4)))
                                        {
                                            AudioSource__Play(v4, 0);
                                            goto LABEL_106f5c4;
                                        }
                                    }
                                    else
                                    {
LABEL_106f5c4:
                                        v4 = ptr->field_c0;
                                        if (v4)
                                        {
                                            Animator__SetBool(v4, ptr->field_30, 1, 0);
                                            my_AI__shoot(ptr);
                                            v16 = ptr->field_78 + 0xbf800000;
                                            ptr->field_78 = v16;
                                            v17 = Time__get_time(0);
                                            ptr->field_7c = v16 + 0x40000000;
                                            return v17;
                                        }
                                    }
                                }
                            }
                            else
                            {
                                Time__get_time(0);
                                v4 = ptr->field_150;
                                if (v4)
                                {
                                    v18 = ptr->field_7c;
                                    v19 = Light__set_range(v4, 0);
                                    v20 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v14, v18)) >> 5 & 3 | (unsigned long long)(CmpF(v14, v18) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v14, v18)) >> 5 & 3 | (unsigned long long)(CmpF(v14, v18) & 1)) & ((unsigned long long)(char)(CmpF(v14, v18)) >> 5 & 3 | (unsigned long long)(CmpF(v14, v18) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                    if (!((char)v20))
                                    {
                                        ptr->field_78 = ptr->field_74;
                                        return v19;
                                    }
                                    v4 = ptr->field_108;
                                    if (v4)
                                    {
                                        AudioSource__Stop(v4, 0);
                                        goto LABEL_106f4d4;
                                    }
                                }
                            }
                        }
                        else
                        {
                            v4 = ptr->field_108;
                            if (v4)
                            {
                                v22 = AudioSource__get_clip(v4, 0);
                                if (!g_1ef0c58->field_e0)
                                    sub_f7da5c(g_1ef0c58);
                                if (!((char)Object__op_Equality(v22, ptr->field_110, 0) & 1))
                                {
LABEL_106f65c:
                                    my_AI__doReload(ptr);
                                    v23 = MonoBehaviour__StartCoroutine();
                                    return MonoBehaviour__StartCoroutine();
                                }
                                v4 = ptr->field_108;
                                if (v4)
                                {
                                    AudioSource__Stop(v4, 0);
                                    goto LABEL_106f65c;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v4);
}
```

## `my_AI.doShout` — RVA `0xc6f6e4`

- Decompiled symbol: `my_AI_doShout`
- Metadata signature: `private void doShout() { }`
- Native interval: `108` bytes
- Result: `pseudocode`
- Heuristic layout hint: `my_AI_Recovered` matched 2 offsets against `my_AI` metadata (confidence 1.00).

```c
typedef struct my_AI_Recovered {
    char padding_0[296];
    long long Shouting_AudioSource;
    struct struct_0 *shoutClip;
} my_AI_Recovered;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

void my_AI_doShout(struct_1 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    struct_0 *v5;  // x9
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    if (ptr->field_130 && !((v4 = (long long)(unsigned long long)Random__Range(0, (unsigned long long)ptr->field_130->field_18, 0), v5 = (struct_0 *)ptr->field_130, !v5)))
    {
        if (v5->field_18 <= (int)v4)
            goto LABEL_106f74c;
        if (ptr->field_128)
        {
            AudioSource__set_clip(ptr->field_128, *((long long *)&v5[1].padding_0[4 + 8 * (v4 & 4294967295)]), 0);
            if (ptr->field_128)
            {
                AudioSource__Play();
                return;
            }
        }
    }
    v4 = sub_f7db74();
LABEL_106f74c:
    sub_f7db7c(v4);
}
```

## `my_AI.ForTDM` — RVA `0xc6f750`

- Decompiled symbol: `my_AI_ForTDM`
- Metadata signature: `private void ForTDM() { }`
- Native interval: `532` bytes
- Result: `pseudocode`
- Heuristic layout hint: `my_AI_Recovered` matched 5 offsets against `my_AI` metadata (confidence 1.00).

```c
typedef struct my_AI_Recovered {
    char padding_0[208];
    long long targetPlayer;
    char padding_d8[31];
    char isJustRunning;
    char padding_f8[64];
    unsigned int layermask;
    char padding_13c[4];
    struct struct_2 *thisManId;
    char padding_148[2];
    char FoundTarget;
} my_AI_Recovered;

typedef struct struct_2 {
    char padding_0[36];
    unsigned int field_24;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef0e48;
extern long long g_1efd088;
extern char g_1fab359;

long long my_AI_ForTDM(struct_3 *ptr)
{
    unsigned int v3;  // w0
    unsigned long v4;  // x0
    long long v5;  // x0
    unsigned long v6;  // x0
    long long v7;  // x0
    long long v8;  // x0
    struct_3 *p;  // x19
    unsigned long v10;  // x0
    unsigned long v11;  // x0
    unsigned long long v12;  // x0
    int choice;  // [bp-0x90]
    uint128_t flag2;  // [bp-0x80]
    uint128_t flag;  // [bp-0x74]

    if (!(g_1fab359 & 1))
    {
        sub_f7d92c(&g_1efd088);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef0e48);
        g_1fab359 = 1;
    }
    flag = 0;
    choice = 0;
    flag2 = 0;
    if (Component__get_transform(ptr, 0))
    {
        Transform__get_position();
        if (Component__get_transform(ptr, 0))
        {
            Transform__get_forward();
            v3 = LayerMask__op_Implicit(ptr->field_138, 0);
            if (!g_1ef0e48->field_e0)
                sub_f7da5c(g_1ef0e48);
            v4 = Physics__SphereCast(&choice, v3, 0, 0);
            if (!((char)v4 & 1))
            {
                return v4;
            }
            else if (RaycastHit__get_transform(&choice, 0))
            {
                v5 = sub_1231bc8();
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v6 = Object__op_Implicit(v5, 0);
                if (!((char)v6 & 1))
                {
                    return v6;
                }
                else if (RaycastHit__get_transform(&choice, 0))
                {
                    v7 = sub_1231bc8();
                    if (v7 && ptr->field_140)
                    {
                        if (*((int *)(v7 + 32)) == ptr->field_140->field_24)
                        {
                            v8 = RaycastHit__get_transform(&choice, 0);
                            ptr->field_d0 = v8;
                            p = &ptr->field_d0;
                            v10 = sub_f7d8d0(p, v8);
                            p->padding_0[122] = 1;
                            p->padding_0[39] = 0;
                            return v10;
                        }
                        v11 = Random__Range(0, 3, 0);
                        if ((unsigned int)v11 != 2)
                            return v11;
                        ptr->field_14a = 0;
                        ptr->field_f7 = 1;
                        v12 = my_AI__SetNextPoint();
                        return my_AI__SetNextPoint();
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `my_AI.SetNextPoint` — RVA `0xc6f964`

- Decompiled symbol: `my_AI_SetNextPoint`
- Metadata signature: `private void SetNextPoint() { }`
- Native interval: `356` bytes
- Result: `pseudocode`
- Heuristic layout hint: `my_AI_Recovered` matched 9 offsets against `my_AI` metadata (confidence 1.00).

```c
typedef struct my_AI_Recovered {
    char padding_0[76];
    unsigned int walkShoot;
    char padding_50[112];
    long long myAnimator;
    long long myAgent;
    char padding_d0[16];
    unsigned long long nextPos;
    long long CurrentPosition;
    int nextPosPointer;
    char padding_f4[2];
    char isShooting;
    char isJustRunning;
    char padding_f8[80];
    char isPetrolling;
} my_AI_Recovered;

typedef struct struct_1 {
    long long field_0;
} struct_1;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

extern long long g_1db6f08;
extern long long g_1ef0c50;

long long my_AI_SetNextPoint(struct_0 *ptr, long long a1)
{
    long long v0;  // x0
    long long v1;  // x0
    long long v9;  // x0
    unsigned long long v10;  // x0
    struct_2 **ptr;  // x0
    unsigned long long addr;  // x8
    int v3;  // w20
    unsigned long v4;  // x0
    unsigned long v5;  // x1
    unsigned long v6;  // x0
    long long v7;  // x19
    struct_1 **v8;  // x19

    if (!ptr->field_148)
    {
        v0 = ptr->field_c8;
        ptr->field_f7 = 0;
        if (!v0)
            goto LABEL_106fa34;
        a1 = 0;
        NavMeshAgent__set_speed(v0, 0);
        v1 = ptr->field_c0;
        if (!v1)
            goto LABEL_106fa38;
        a1 = ptr->field_4c;
        Animator__SetBool(v1, a1, 1, 0);
        ptr->field_f6 = 1;
    }
    addr = ptr->field_e0;
    if (!addr)
    {
        v4 = sub_f7db74();
LABEL_106fa2c:
        v4 = sub_f7db7c(v4);
LABEL_106fa30:
        v0 = sub_f7db74(v4);
LABEL_106fa34:
        v1 = sub_f7db74(v0);
LABEL_106fa38:
        v7 = sub_f7db74(v1);
        if ((int)a1 == 1)
        {
            v8 = __cxa_begin_catch(v7);
            v9 = sub_f7d940(&g_1ef0c50);
            if (((char)sub_f7dfa0(v9, *(v8)->field_0) & 1))
            {
                v10 = __cxa_end_catch();
                return __cxa_end_catch();
            }
            ptr = __cxa_allocate_exception(8);
            *(ptr) = *(v8);
            v7 = __cxa_throw(ptr, &g_1db6f08, 0);
            __cxa_end_catch(v7, &g_1db6f08, 0);
        }
        sub_e29990(sub_1026098(v7));
    }
    v3 = ptr->field_f0;
    if (2 > *((int *)(addr + 24)))
    {
        v4 = v3;
        goto LABEL_106f9fc;
    }
    while (true)
    {
        a1 = *((int *)(addr + 24));
        v4 = Random__Range(0, a1, 0);
        addr = ptr->field_e0;
        ptr->field_f0 = v4;
        if (v3 != (unsigned int)v4)
        {
LABEL_106f9f8:
            if (!addr)
                goto LABEL_106fa30;
LABEL_106f9fc:
            if (*((int *)(addr + 24)) > (unsigned int)v4)
            {
                v5 = *((long long *)(addr + (v4 & 4294967295) * 8 + 32));
                ptr->field_e8 = v5;
                v6 = sub_f7d8d0(&ptr->field_e8, v5);
                return sub_f7d8d0(&ptr->field_e8, v5);
            }
            goto LABEL_106fa2c;
        }
        else if (!addr)
        {
            v4 = sub_f7db74();
            goto LABEL_106f9f8;
        }
    }
}
```

## `my_AI.OnDrawGizmosSelected` — RVA `0xc6fac8`

- Decompiled symbol: `my_AI_OnDrawGizmosSelected`
- Metadata signature: `private void OnDrawGizmosSelected() { }`
- Native interval: `312` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern char g_1fab35a;

void my_AI_OnDrawGizmosSelected(long long a0)
{
    unsigned long long v10;  // d14
    unsigned long long v11;  // d13
    unsigned long long v12;  // d12
    unsigned long long v13;  // d11
    unsigned long long v14;  // d10
    unsigned long long v15;  // d9
    unsigned long long v16;  // d8
    unsigned long long v17;  // x30
    unsigned long long v18;  // x20
    unsigned long long v19;  // x19
    unsigned long long v0;  // [bp-0x50]
    unsigned long long v1;  // [bp-0x48]
    unsigned long long v2;  // [bp-0x40]
    unsigned long long v3;  // [bp-0x38]
    unsigned long long v4;  // [bp-0x30]
    unsigned long long v5;  // [bp-0x28]
    unsigned long long v6;  // [bp-0x20]
    unsigned long long v7;  // [bp-0x18]
    unsigned long long v8;  // [bp-0x10]
    unsigned long long v9;  // [bp-0x8]

    v0 = v10;
    v1 = v11;
    v2 = v12;
    v3 = v13;
    v4 = v14;
    v5 = v15;
    v6 = v16;
    v7 = v17;
    v8 = v18;
    v9 = v19;
    if (!(g_1fab35a & 1))
    {
        sub_f7d92c(&g_1eef458);
        g_1fab35a = 1;
    }
    Gizmos__set_color(0);
    if (Component__get_transform(a0, 0))
    {
        Transform__get_position();
        if (Component__get_transform(a0, 0))
        {
            Transform__get_position();
            if (Component__get_transform(a0, 0))
            {
                Transform__get_forward();
                if (!g_1eef458->field_e0)
                    sub_f7da5c(g_1eef458);
                Debug__DrawLine(0);
                if (Component__get_transform(a0, 0))
                    Transform__get_position();
            }
        }
    }
    sub_f7db74();
}
```

## `my_AI.shoot` — RVA `0xc6fc00`

- Decompiled symbol: `my_AI_shoot`
- Metadata signature: `private void shoot() { }`
- Native interval: `1664` bytes
- Result: `pseudocode`
- Heuristic layout hint: `my_AI_Recovered` matched 13 offsets against `my_AI` metadata (confidence 1.00).

```c
typedef struct my_AI_Recovered {
    char padding_0[48];
    unsigned int isShootingAnim;
    char padding_34[4];
    unsigned int crouchShoot;
    char padding_3c[40];
    unsigned int magCapacity;
    char padding_68[44];
    unsigned int damage;
    struct struct_4 *ShootPoint;
    struct struct_4 *bullet_Shoot_Effect;
    struct struct_4 *BulletTracer;
    struct struct_4 *bloodHit;
    struct struct_4 *ConcretHit;
    struct struct_4 *myAnimator;
    char padding_c8[8];
    long long targetPlayer;
    char padding_d8[104];
    unsigned long long thisManId;
    char padding_148[8];
    struct struct_4 *FireLight;
} my_AI_Recovered;

typedef struct struct_4 {
    char padding_0[32];
    unsigned int field_20;
} struct_4;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct struct_6 {
    char padding_0[32];
    unsigned int field_20;
} struct_6;

typedef struct struct_0 {
    char padding_0[8];
    char field_8;
} struct_0;

typedef struct struct_3 {
    char padding_0[224];
    unsigned int field_e0;
} struct_3;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

extern struct_1 *g_1ef0750;
extern struct_2 *g_1ef0c58;
extern struct_3 *g_1ef0e48;
extern long long g_1efcf98;
extern long long g_1efd088;
extern long long g_1efd100;
extern long long g_1efebb8;
extern char g_1fab35c;
extern char g_1fab3df;

long long my_AI_shoot(struct_5 *ptr)
{
    struct_4 *v3;  // x0, Other Possible Types: struct_6 *
    unsigned int v4;  // s0
    long long v13;  // x0
    long long v14;  // x20
    long long v15;  // x0
    unsigned int v16;  // w0
    long long v17;  // x20
    long long v18;  // x20
    long long v19;  // x20
    long long v20;  // x20
    long long v21;  // x0
    long long v5;  // x0
    long long v22;  // x0
    unsigned int v23;  // s1
    unsigned long v24;  // 4260
    unsigned long long v25;  // x0
    long long v6;  // x0
    struct_1 *v7;  // x0
    long long v8;  // x1
    unsigned long v9;  // 4134
    unsigned long v10;  // 4128
    long long v11;  // x20
    struct_4 *v12;  // x1
    int choice;  // [bp-0x90]
    uint128_t flag2;  // [bp-0x80]
    uint128_t flag;  // [bp-0x74]

    if (!(g_1fab35c & 1))
    {
        sub_f7d92c(&g_1efcf98);
        sub_f7d92c(&g_1efd088);
        sub_f7d92c(&g_1efd100);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1ef0750);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef0e48);
        sub_f7d92c("11");
        g_1fab35c = 1;
    }
    flag = 0;
    choice = 0;
    flag2 = 0;
    Random__Range(0);
    Random__Range(0);
    v3 = ptr->field_98;
    if (v3 && (v3 = (struct_4 *)(unsigned long long)GameObject__get_transform(v3, 0), v3 && (Transform__get_forward(), v3 = (struct_4 *)ptr->field_c0, v3)))
    {
        if (!((char)Animator__GetBool(v3, ptr->field_38, 0) & 1))
        {
            v3 = ptr->field_c0;
            if (v3)
            {
                Animator__SetTrigger(v3, ptr->field_30, 0);
                goto LABEL_106fd20;
            }
        }
        else
        {
LABEL_106fd20:
            v3 = ptr->field_a0;
            ptr->field_64 = ptr->field_64 + 0xbf800000;
            if (v3 && (ParticleSystem__Play(v3, 0), v3 = (struct_4 *)ptr->field_150, v3 && (Light__set_range(v3, 0), v3 = (struct_4 *)ptr->field_98, v3 && (v3 = (struct_4 *)(unsigned long long)GameObject__get_transform(v3, 0), v3))))
            {
                Transform__get_position();
                if (!g_1ef0e48->field_e0)
                    sub_f7da5c(g_1ef0e48);
                v4 = 0;
                v5 = Physics__Raycast(&choice, 0);
                if (!((char)v5 & 1))
                    return v5;
                v3 = RaycastHit__get_transform(&choice, 0);
                if (v3)
                {
                    v6 = sub_1231bc8();
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (((char)Object__op_Implicit(v6, 0) & 1))
                    {
                        v7 = g_1ef0750;
                        if (!g_1ef0750->field_e0)
                        {
                            sub_f7da5c(g_1ef0750);
                            v7 = g_1ef0750;
                        }
                        if (v7->field_b8->field_8)
                        {
                            v3 = RaycastHit__get_transform(&choice, 0);
                            if (v3 && (v3 = (struct_4 *)sub_1231bc8(), v3 && ptr->field_140))
                            {
                                if (v3->field_20 == *((int *)(ptr->field_140 + 36)))
                                {
                                    v8 = RaycastHit__get_transform(&choice, 0);
                                    ptr->field_d0 = v8;
                                    sub_f7d8d0(&ptr->field_d0, v8);
                                }
                                goto LABEL_106fea4;
                            }
                        }
                        else
                        {
LABEL_106fea4:
                            my_AI__GettingPlayerDistance(ptr, ptr->field_d0);
                            v4 = 0x41400000;
                            v9 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(0, 0x41400000)) >> 5 & 3 | (unsigned long long)(CmpF(0, 0x41400000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(0, 0x41400000)) >> 5 & 3 | (unsigned long long)(CmpF(0, 0x41400000) & 1)) & ((unsigned long long)(char)(CmpF(0, 0x41400000)) >> 5 & 3 | (unsigned long long)(CmpF(0, 0x41400000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if (Random__Range())
                                goto LABEL_1070120;
                            v10 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(0, 0x43480000)) >> 5 & 3 | (unsigned long long)(CmpF(0, 0x43480000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(0, 0x43480000)) >> 5 & 3 | (unsigned long long)(CmpF(0, 0x43480000) & 1)) & ((unsigned long long)(char)(CmpF(0, 0x43480000)) >> 5 & 3 | (unsigned long long)(CmpF(0, 0x43480000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                            if (!((char)v10))
                            {
                                v3 = RaycastHit__get_collider(&choice, 0);
                                if (v3 && (v3 = (struct_4 *)Component__get_gameObject(), v3))
                                {
                                    v11 = sub_1249224();
                                    v3 = Component__get_transform(ptr, 0);
                                    if (v11)
                                    {
                                        v12 = v3;
                                        v4 = ptr->field_94 * 0x40a00000;
                                        v13 = v11;
                                        goto LABEL_107009c;
                                    }
                                }
                            }
                            else
                            {
                                v3 = RaycastHit__get_collider(&choice, 0);
                                if (v3 && (v3 = (struct_4 *)Component__get_gameObject(), v3))
                                {
                                    v14 = sub_1249224();
                                    v3 = Component__get_transform(ptr, 0);
                                    if (v14)
                                    {
                                        v12 = v3;
                                        v13 = v14;
                                        v4 = ptr->field_94;
LABEL_107009c:
                                        FPSPlayer__ApplyDamage(v13, v12, 0, 0);
LABEL_10700a8:
                                        v3 = ptr->field_b0;
                                        if (v3)
                                        {
                                            v19 = Component__get_transform(v3, 0);
                                            v3 = RaycastHit__get_point(&choice, 0);
                                            if (v19 && (Transform__set_position(v19, 0), v3 = (struct_4 *)ptr->field_b0, v3))
                                            {
                                                v20 = Component__get_transform(v3, 0);
                                                RaycastHit__get_normal(&choice, 0);
                                                v3 = Quaternion__LookRotation(0);
                                                if (v20 && (Transform__set_rotation(v20, 0), v3 = (struct_4 *)ptr->field_b0, v3))
                                                {
LABEL_1070118:
                                                    ParticleSystem__Play(v3, 0);
LABEL_1070120:
                                                    v3 = RaycastHit__get_transform(&choice, 0);
                                                    if (v3)
                                                    {
                                                        v21 = Component__get_gameObject();
                                                        if (!g_1ef0c58->field_e0)
                                                            sub_f7da5c(g_1ef0c58);
                                                        v22 = Object__op_Inequality(v21, 0, 0);
                                                        if (!((char)v22 & 1))
                                                            return v22;
                                                        v3 = RaycastHit__get_transform(&choice, 0);
                                                        if (v3)
                                                        {
                                                            Transform__get_position();
                                                            v3 = ptr->field_a8;
                                                            if (v3)
                                                            {
                                                                v3 = Component__get_transform(v3, 0);
                                                                if (v3)
                                                                {
                                                                    Transform__get_position();
                                                                    if (!g_1fab3df)
                                                                    {
                                                                        sub_f7d92c("_F");
                                                                        g_1fab3df = 1;
                                                                    }
                                                                    if (!g_1ef07e8->field_e0)
                                                                        sub_f7da5c(g_1ef07e8);
                                                                    v3 = ptr->field_a8;
                                                                    if (v3)
                                                                    {
                                                                        ParticleSystem__get_startSpeed(v3, 0);
                                                                        v3 = ptr->field_a8;
                                                                        if (v3)
                                                                        {
                                                                            v23 = [D] unsupported_Iop_SqrtF32();
                                                                            v24 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v23 / v4, 0x42480000)) >> 5 & 3 | (unsigned long long)(CmpF(v23 / v4, 0x42480000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v23 / v4, 0x42480000)) >> 5 & 3 | (unsigned long long)(CmpF(v23 / v4, 0x42480000) & 1)) & ((unsigned long long)(char)(CmpF(v23 / v4, 0x42480000)) >> 5 & 3 | (unsigned long long)(CmpF(v23 / v4, 0x42480000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                                                            ParticleSystem__set_startLifetime();
                                                                            v3 = ptr->field_a8;
                                                                            if (v3)
                                                                            {
                                                                                v25 = ParticleSystem__Emit(v3, 1, 0);
                                                                                return ParticleSystem__Emit(v3, 1, 0);
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
                            }
                        }
                    }
                    else
                    {
                        v3 = RaycastHit__get_transform(&choice, 0);
                        if (v3)
                        {
                            v15 = sub_1231bc8();
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            v16 = Object__op_Implicit(v15, 0);
                            v3 = RaycastHit__get_transform(&choice, 0);
                            if (v3)
                            {
                                if (((char)v16 & 1))
                                {
                                    v3 = sub_1231bc8();
                                    if (v3)
                                    {
                                        v4 = ptr->field_94;
                                        getHit__applyDamage(v3, 0, 0);
                                        goto LABEL_10700a8;
                                    }
                                }
                                else
                                {
                                    if ((Component__CompareTag() & 1))
                                        goto LABEL_10700a8;
                                    v3 = ptr->field_b8;
                                    if (v3)
                                    {
                                        v17 = Component__get_transform(v3, 0);
                                        v3 = RaycastHit__get_point(&choice, 0);
                                        if (v17 && (Transform__set_position(v17, 0), v3 = (struct_4 *)ptr->field_b8, v3))
                                        {
                                            v18 = Component__get_transform(v3, 0);
                                            RaycastHit__get_normal(&choice, 0);
                                            v3 = Quaternion__LookRotation(0);
                                            if (v18 && (Transform__set_rotation(v18, 0), v3 = (struct_4 *)ptr->field_b8, v3))
                                                goto LABEL_1070118;
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
    sub_f7db74(v3);
}
```

## `my_AI.doReload` — RVA `0xc70280`

- Decompiled symbol: `my_AI_doReload`
- Metadata signature: `private IEnumerator doReload() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef41d0;
extern char g_1fab35d;

struct_0 * my_AI_doReload(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab35d & 1))
    {
        sub_f7d92c(&g_1ef41d0);
        g_1fab35d = 1;
    }
    v0 = sub_f7db70(g_1ef41d0);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```

## `my_AI.<doReload>d__69.ctor` — RVA `0xc702ec`

- Decompiled symbol: `my_AI_doReload_d__69_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void my_AI_doReload_d__69_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `my_AI.OnTriggerEnter` — RVA `0xc70314`

- Decompiled symbol: `my_AI_OnTriggerEnter`
- Metadata signature: `private IEnumerator OnTriggerEnter(Collider other) { }`
- Native interval: `136` bytes
- Result: `pseudocode`
- Heuristic layout hint: `my_AI_Recovered` matched 2 offsets against `my_AI` metadata (confidence 0.67).

```c
typedef struct my_AI_Recovered {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long DeadAnim;
    long long startMovingAnim;
} my_AI_Recovered;

extern long long g_1ef41c8;
extern char g_1fab35e;

struct_0 * my_AI_OnTriggerEnter(long long a0, long long a1)
{
    struct_0 *v0;  // x21
    struct_0 *ptr;  // x0
    struct_0 *p;  // x0

    if (!(g_1fab35e & 1))
    {
        sub_f7d92c(&g_1ef41c8);
        g_1fab35e = 1;
    }
    v0 = sub_f7db70(g_1ef41c8);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_28 = a0;
    sub_f7d8d0(&ptr->field_28, a0);
    p = ptr;
    p->field_20 = a1;
    sub_f7d8d0(&p->field_20, a1);
    return p;
}
```

## `my_AI.<OnTriggerEnter>d__71.ctor` — RVA `0xc7039c`

- Decompiled symbol: `my_AI_OnTriggerEnter_d__71_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void my_AI_OnTriggerEnter_d__71_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `my_AI.setWalkShoot` — RVA `0xc703c4`

- Decompiled symbol: `my_AI_setWalkShoot`
- Metadata signature: `private void setWalkShoot(bool x) { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long my_AI_setWalkShoot(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `my_AI.Set_Player_As_Target` — RVA `0xc703c8`

- Decompiled symbol: `my_AI_Set_Player_As_Target`
- Metadata signature: `public void Set_Player_As_Target(Transform real_Player) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[208];
    unsigned long long field_d0;
} struct_0;

long long my_AI_Set_Player_As_Target(struct_0 *ptr, unsigned long a1)
{
    long long v0;  // x0

    ptr->field_d0 = a1;
    v0 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `my_AI.checkPetrolling` — RVA `0xc703d0`

- Decompiled symbol: `my_AI_checkPetrolling`
- Metadata signature: `public bool checkPetrolling() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[348];
    char field_15c;
} struct_0;

long long my_AI_checkPetrolling(struct_0 *a0)
{
    return a0->field_15c;
}
```

## `my_AI.ctor` — RVA `0xc703d8`

- Decompiled symbol: `my_AI_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `648` bytes
- Result: `pseudocode`
- Heuristic layout hint: `my_AI_Recovered` matched 23 offsets against `my_AI` metadata (confidence 1.00).

```c
typedef struct my_AI_Recovered {
    char padding_0[32];
    unsigned int DeadAnim;
    unsigned int isDeadAnim;
    unsigned int startMovingAnim;
    unsigned int justRun;
    unsigned int isShootingAnim;
    unsigned int isReloading;
    unsigned int crouchShoot;
    unsigned int takeCover;
    unsigned int CoverL_Lo;
    unsigned int CoverR_Lo;
    unsigned int takeRightCover;
    unsigned int walkShoot;
    unsigned int Petroling;
    uint128_t walkSpeed;
    unsigned long long magCapacity;
    unsigned int rateOfFire;
    char padding_70[4];
    unsigned int BulletsToPause;
    char padding_78[8];
    unsigned long long hitRange;
    char padding_88[4];
    unsigned long long targetAccuracy;
    unsigned int damage;
    char padding_98[96];
    unsigned long long SphareRadius;
    char padding_100[32];
    unsigned int FireSound;
    char padding_124[52];
    unsigned int applySpredValue;
} my_AI_Recovered;

extern long long g_1f09968;
extern long long g_1f0cef8;
extern long long g_1f11c18;
extern long long g_1f131d8;
extern long long g_1f131f8;
extern long long g_1f13208;
extern long long g_1f134a0;
extern long long g_1f15918;
extern char g_1fab360;

void my_AI_ctor(struct_0 *ptr)
{
    unsigned long long v13;  // x30
    unsigned long long v14;  // x28
    unsigned long long v23;  // x19
    unsigned int v24;  // w0
    unsigned long long v15;  // x27
    unsigned long long v16;  // x26
    unsigned long long v17;  // x25
    unsigned long long v18;  // x24
    unsigned long long v19;  // x23
    unsigned long long v20;  // x22
    unsigned long long v21;  // x21
    unsigned long long v22;  // x20
    char *v0;  // [bp-0x60]
    unsigned long long v1;  // [bp-0x58]
    unsigned long long v2;  // [bp-0x50]
    unsigned long long v3;  // [bp-0x48]
    unsigned long long v4;  // [bp-0x40]
    unsigned long long v5;  // [bp-0x38]
    unsigned long long v6;  // [bp-0x30]
    unsigned long long v7;  // [bp-0x28]
    unsigned long long v8;  // [bp-0x20]
    unsigned long long v9;  // [bp-0x18]
    unsigned long long v10;  // [bp-0x10]
    unsigned long long v11;  // [bp-0x8]
    char v12;  // [bp+0x0]

    v0 = &v12;
    v1 = v13;
    v2 = v14;
    v3 = v15;
    v4 = v16;
    v5 = v17;
    v6 = v18;
    v7 = v19;
    v8 = v20;
    v9 = v21;
    v10 = v22;
    v11 = v23;
    if (!(g_1fab360 & 1))
    {
        sub_f7d92c(&g_1f13208);
        sub_f7d92c(&g_1f15918);
        sub_f7d92c(&g_1f11c18);
        sub_f7d92c("g;");
        sub_f7d92c(&g_1f131f8);
        sub_f7d92c(&g_1f09968);
        sub_f7d92c("E\r");
        sub_f7d92c("G\r");
        sub_f7d92c(&g_1f131d8);
        sub_f7d92c(&g_1f0cef8);
        sub_f7d92c(&g_1f134a0);
        sub_f7d92c("e;");
        sub_f7d92c("y:");
        g_1fab360 = 1;
    }
    ptr->field_20 = Animator__StringToHash(g_1f09968, 0);
    ptr->field_24 = Animator__StringToHash(g_1f131d8, 0);
    ptr->field_28 = Animator__StringToHash(g_1f14bd0, 0);
    ptr->field_2c = Animator__StringToHash(g_1f134a0, 0);
    ptr->field_30 = Animator__StringToHash(g_1f13208, 0);
    ptr->field_34 = Animator__StringToHash(g_1f131f8, 0);
    ptr->field_38 = Animator__StringToHash(g_1f11c18, 0);
    ptr->field_3c = Animator__StringToHash(g_1f14f80, 0);
    ptr->field_40 = Animator__StringToHash(g_1f09728, 0);
    ptr->field_44 = Animator__StringToHash(g_1f09730, 0);
    ptr->field_48 = Animator__StringToHash(g_1f14f88, 0);
    ptr->field_4c = Animator__StringToHash(g_1f15918, 0);
    v24 = Animator__StringToHash(g_1f0cef8, 0);
    *((uint128_t *)&(&ptr->field_50)[1]) = 0x41a0000041a0000040d0000040600000;
    *((unsigned int *)((char *)&ptr->field_54 + 12)) = 0x40c00000;
    *((unsigned long long *)&ptr->field_74) = 0x40c0000043480000;
    *((unsigned int *)((char *)&ptr->field_64 + 4)) = 0x41200000;
    *((unsigned int *)((char *)&ptr->field_80 + 4)) = 0x41200000;
    *((unsigned long long *)&(&ptr->padding_78)[1]) = 4294967300;
    *((unsigned long long *)((char *)&ptr->field_54 + 4)) = 0x41f0000041f00000;
    ptr->field_50 = v24;
    *((unsigned int *)&ptr->padding_100[8]) = 0x3f000000;
    *((unsigned long long *)&ptr->padding_98[76]) = 0x42c8000041200000;
    *((unsigned int *)&ptr->padding_124[28]) = 1028443341;
}
```

## `my_AI.<OnTriggerEnter>d__71.Dispose` — RVA `0xc70660`

- Decompiled symbol: `my_AI_OnTriggerEnter_d__71_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long my_AI_OnTriggerEnter_d__71_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `my_AI.<OnTriggerEnter>d__71.MoveNext` — RVA `0xc70664`

- Decompiled symbol: `my_AI_OnTriggerEnter_d__71_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `6120` bytes
- Result: `pseudocode`

```c
extern long long g_1ef2440;
extern long long g_1f134a0;
extern char g_1fab361;
extern unsigned short g_85224c[4];

unsigned int my_AI_OnTriggerEnter_d__71_MoveNext(unsigned long a0)
{
    unsigned int flag;  // [bp-0x28]

    if (!(g_1fab361 & 1))
    {
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c("e:");
        sub_f7d92c("g\r");
        sub_f7d92c("k%");
        sub_f7d92c("g;");
        sub_f7d92c("E\r");
        sub_f7d92c("G\r");
        sub_f7d92c("\t7");
        sub_f7d92c(&g_1f134a0);
        sub_f7d92c("e;");
        g_1fab361 = 1;
    }
    flag = 0;
    if (14 < *((int *)(a0 + 16)))
        return 0;
    goto sub_107072c + g_85224c[*((int *)(a0 + 16))] * 4;
}
```

## `my_AI.<OnTriggerEnter>d__71.get_Current` — RVA `0xc71e4c`

- Decompiled symbol: `my_AI_OnTriggerEnter_d__71_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long my_AI_OnTriggerEnter_d__71_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `my_AI.<OnTriggerEnter>d__71.Reset` — RVA `0xc71e54`

- Decompiled symbol: `my_AI_OnTriggerEnter_d__71_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05550;

void my_AI_OnTriggerEnter_d__71_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f05550));
}
```

## `my_AI.<OnTriggerEnter>d__71.get_Current` — RVA `0xc71e8c`

- Decompiled symbol: `my_AI_OnTriggerEnter_d__71_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long my_AI_OnTriggerEnter_d__71_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `my_AI.<doReload>d__69.Dispose` — RVA `0xc71e94`

- Decompiled symbol: `my_AI_doReload_d__69_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long my_AI_doReload_d__69_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `my_AI.<doReload>d__69.MoveNext` — RVA `0xc71e98`

- Decompiled symbol: `my_AI_doReload_d__69_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `424` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[48];
    unsigned int field_30;
    unsigned int field_34;
    char padding_38[44];
    unsigned int field_64;
    unsigned int field_68;
    char padding_6c[84];
    long long field_c0;
    char padding_c8[64];
    long long field_108;
    char padding_110[8];
    long long field_118;
} struct_0;

extern long long g_1ef2440;
extern char g_1fab362;

unsigned int my_AI_doReload_d__69_MoveNext(struct_1 *ptr)
{
    struct_0 *p;  // x21
    long long v1;  // x20
    long long v3;  // x21
    struct_1 *addr;  // x19
    long long v5;  // x0
    long long v6;  // x19

    if (!(g_1fab362 & 1))
    {
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c("k%");
        g_1fab362 = 1;
    }
    p = ptr->field_20;
    if (ptr->field_10 != 1)
    {
        if (ptr->field_10)
            return 0;
        ptr->field_10 = 4294967295;
        if (p && p->field_108)
        {
            if (((char)AudioSource__get_isPlaying(p->field_108, 0) & 1))
            {
LABEL_1071f28:
                v1 = p->field_c0;
                if (v1)
                {
                    Animator__SetLayerWeight(v1, Animator__GetLayerIndex(v1, g_1f0f7a0, 0) & 4294967295, 0);
                    if (p->field_c0)
                    {
                        Animator__SetBool(p->field_c0, p->field_30, 0, 0);
                        if (p->field_c0)
                        {
                            Animator__SetBool(p->field_c0, p->field_34, 1, 0);
                            v3 = sub_f7db70(g_1ef2440);
                            WaitForSeconds__ctor(v3, 0);
                            ptr->field_18 = v3;
                            addr = &ptr->field_18;
                            sub_f7d8d0(addr, v3);
                            *((unsigned int *)&addr->padding_0[8]) = 1;
                            return 1;
                        }
                    }
                }
            }
            else if (p->field_108 && (AudioSource__set_clip(p->field_108, p->field_118, 0), p->field_108))
            {
                AudioSource__Play(p->field_108, 0);
                goto LABEL_1071f28;
            }
        }
    }
    else
    {
        ptr->field_10 = 4294967295;
        if (p)
        {
            v5 = p->field_c0;
            p->field_64 = p->field_68;
            if (v5)
            {
                Animator__SetBool(v5, p->field_34, 0, 0);
                v6 = p->field_c0;
                if (v6)
                {
                    Animator__SetLayerWeight(v6, Animator__GetLayerIndex(v6, g_1f0f7a0, 0) & 4294967295, 0);
                    return 0;
                }
            }
        }
    }
    sub_f7db74();
}
```

## `my_AI.<doReload>d__69.get_Current` — RVA `0xc72040`

- Decompiled symbol: `my_AI_doReload_d__69_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long my_AI_doReload_d__69_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `my_AI.<doReload>d__69.Reset` — RVA `0xc72048`

- Decompiled symbol: `my_AI_doReload_d__69_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05558;

void my_AI_doReload_d__69_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f05558));
}
```

## `my_AI.<doReload>d__69.get_Current` — RVA `0xc72080`

- Decompiled symbol: `my_AI_doReload_d__69_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long my_AI_doReload_d__69_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
