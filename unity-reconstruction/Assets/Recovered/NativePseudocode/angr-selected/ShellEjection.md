# Native pseudocode: ShellEjection

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ShellEjection.Start` — RVA `0xcb5064`

- Decompiled symbol: `ShellEjection_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long ShellEjection_Start(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `ShellEjection.InitializeShell` — RVA `0xcb5068`

- Decompiled symbol: `ShellEjection_InitializeShell`
- Metadata signature: `public void InitializeShell() { }`
- Native interval: `708` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ShellEjection_Recovered` matched 2 offsets against `ShellEjection` metadata (confidence 1.00).

```c
typedef struct struct_0 {
    char padding_0[96];
    struct ShellEjection_Recovered *field_60;
} struct_0;

typedef struct struct_3 {
    char padding_0[1648];
    unsigned long long field_670;
    unsigned int field_678;
} struct_3;

typedef struct ShellEjection_Recovered {
    char padding_0[96];
    unsigned long long gunObjTransform;
    unsigned long long lerpShell;
} ShellEjection_Recovered;

extern long long g_1ef22e8;
extern long long g_1efcf38;
extern char g_1fab2c9;
extern char g_1fab32c;
extern char g_1fab3e1;
extern char g_1fab4dc;

void ShellEjection_InitializeShell(void* ptr)
{
    unsigned long long v9;  // d10
    unsigned long long v10;  // d9
    unsigned long long v19[14];  // x1
    void* p;  // x20
    void* v21;  // x20
    long long v22;  // x1
    void* addr;  // x20
    void* v24;  // x20
    unsigned long v25;  // x1
    void* ptr3;  // x20
    void* v27;  // x20
    long long v28;  // x0
    unsigned long long v11;  // d8
    void* ptr4;  // x21
    void* v30;  // x21
    unsigned long v31;  // x1
    struct_3 *ptr5;  // x8
    unsigned long v33;  // d0
    unsigned long v34;  // x20
    unsigned long v35;  // 4125
    unsigned long v36;  // x20
    unsigned long v37;  // x20
    unsigned long long v12;  // x30
    unsigned long long v13;  // x23
    unsigned long long v14;  // x22
    unsigned long long v15;  // x21
    unsigned long long v16;  // x20
    unsigned long long v17;  // x19
    struct_0 *ptr6;  // x0
    unsigned long long v0;  // [bp-0x50]
    unsigned long long v1;  // [bp-0x40]
    unsigned long long v2;  // [bp-0x38]
    unsigned long long v3;  // [bp-0x30]
    unsigned long long v4;  // [bp-0x28]
    unsigned long long v5;  // [bp-0x20]
    unsigned long long v6;  // [bp-0x18]
    unsigned long long v7;  // [bp-0x10]
    unsigned long long v8;  // [bp-0x8]

    v0 = v9;
    v1 = v10;
    v2 = v11;
    v3 = v12;
    v4 = v13;
    v5 = v14;
    v6 = v15;
    v7 = v16;
    v8 = v17;
    if (!(g_1fab4dc & 1))
    {
        sub_f7d92c(&g_1efcf38);
        g_1fab4dc = 1;
    }
    if (Camera__get_main(0) && Component__get_transform())
    {
        ptr6 = sub_1231bc8();
        if (ptr6)
        {
            v19 = ptr6->field_60;
            p = ptr;
            *((unsigned long long *[14])&p[32]) = v19;
            v21 = p + 32;
            sub_f7d8d0(v21, v19);
            if (*((long long *)v21))
            {
                v22 = *((long long *)(*((long long *)v21) + 104));
                addr = ptr;
                *((long long *)&addr[48]) = v22;
                v24 = addr + 48;
                sub_f7d8d0(v24, v22);
                if ((long long)v24[16])
                {
                    v25 = *((long long *)((long long)v24[16] + 96));
                    ptr3 = ptr;
                    *((unsigned long *)&ptr3[40]) = v25;
                    v27 = ptr3 + 40;
                    sub_f7d8d0(v27, v25);
                    v28 = Component__get_transform(ptr, 0);
                    ptr4 = ptr;
                    *((long long *)&ptr4[144]) = v28;
                    v30 = ptr4 + 144;
                    sub_f7d8d0(v30, v28);
                    if ((long long)v30[112])
                    {
                        v31 = *((long long *)((long long)v30[112] + 96));
                        *((unsigned long *)&ptr[40]) = v31;
                        sub_f7d8d0(v27, v31);
                        ptr5 = (long long)ptr[56];
                        *((unsigned short *)&ptr[168]) = 257;
                        if (ptr5)
                        {
                            v33 = ptr5->field_670;
                            *((unsigned long *)&ptr[172]) = v33;
                            *((unsigned int *)&ptr[184]) = ptr5->field_678;
                            Time__get_time(0);
                            *((unsigned int *)&ptr[188]) = v33;
                            Time__get_time(0);
                            v34 = (long long)ptr[64];
                            *((unsigned int *)&ptr[180]) = (unsigned int)v33 + (int)ptr[184];
                            if (!g_1fab2c9)
                            {
                                sub_f7d92c(&g_1ef22e8);
                                g_1fab2c9 = 1;
                            }
                            if (v34)
                            {
                                Rigidbody__set_angularVelocity(v34, 0);
                                if ((long long)ptr[64])
                                {
                                    Rigidbody__set_maxAngularVelocity((long long)ptr[64], 0);
                                    Random__get_value(0);
                                    v35 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(0x447a0000, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(0x447a0000, 0x3f000000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(0x447a0000, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(0x447a0000, 0x3f000000) & 1)) & ((unsigned long long)(char)(CmpF(0x447a0000, 0x3f000000)) >> 5 & 3 | (unsigned long long)(CmpF(0x447a0000, 0x3f000000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                    if (!((char)v35))
                                        *((int *)&ptr[172]) = -((int)ptr[172]);
                                    v36 = (long long)ptr[64];
                                    if (!g_1fab32c)
                                    {
                                        sub_f7d92c(&g_1ef22e8);
                                        g_1fab32c = 1;
                                    }
                                    Random__Range(0);
                                    if (v36)
                                    {
                                        Rigidbody__AddRelativeTorque(v36, 1, 0);
                                        v37 = (long long)ptr[64];
                                        if (!g_1fab3e1)
                                        {
                                            sub_f7d92c(&g_1ef22e8);
                                            g_1fab3e1 = 1;
                                        }
                                        Random__Range(0);
                                        if (v37)
                                        {
                                            Rigidbody__AddRelativeTorque(v37, 1, 0);
                                            ShellEjection__CalcShellPos();
                                            MonoBehaviour__StartCoroutine();
                                            return;
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


## `ShellEjection.CalcShellPos` — RVA `0xcb532c`

- Decompiled symbol: `ShellEjection_CalcShellPos`
- Metadata signature: `private IEnumerator CalcShellPos() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef39b0;
extern char g_1fab4de;

struct_0 * ShellEjection_CalcShellPos(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab4de & 1))
    {
        sub_f7d92c(&g_1ef39b0);
        g_1fab4de = 1;
    }
    v0 = sub_f7db70(g_1ef39b0);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `ShellEjection.Update` — RVA `0xcb5398`

- Decompiled symbol: `ShellEjection_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `156` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ShellEjection_Recovered` matched 2 offsets against `ShellEjection` metadata (confidence 1.00).

```c
typedef struct ShellEjection_Recovered {
    char padding_0[56];
    unsigned long long WeaponBehaviorComponent;
    char padding_40[116];
    unsigned int shellRemovalTime;
} ShellEjection_Recovered;

extern char g_1fab4dd;

int ShellEjection_Update(struct_2 *ptr, unsigned long a1)
{
    unsigned int v0;  // w0
    unsigned int v1;  // s1
    unsigned int v2;  // s0
    unsigned long v3;  // 4129

    if (!(g_1fab4dd & 1))
    {
        sub_f7d92c("s.");
        g_1fab4dd = 1;
    }
    v0 = Time__get_time(0);
    v1 = ptr->field_b4;
    v3 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v2, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v1) & 1)) & ((unsigned long long)(char)(CmpF(v2, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v3)
        return v0;
    if (ptr->field_38)
        Component__get_gameObject(ptr, 0);
    sub_f7db74();
}
```


## `ShellEjection.<CalcShellPos>d__29.ctor` — RVA `0xcb5434`

- Decompiled symbol: `ShellEjection_CalcShellPos_d__29_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void ShellEjection_CalcShellPos_d__29_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `ShellEjection.OnCollisionEnter` — RVA `0xcb545c`

- Decompiled symbol: `ShellEjection_OnCollisionEnter`
- Metadata signature: `private void OnCollisionEnter(Collision collision) { }`
- Native interval: `148` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ShellEjection_Recovered` matched 3 offsets against `ShellEjection` metadata (confidence 1.00).

```c
typedef struct ShellEjection_Recovered {
    char padding_0[144];
    long long myTransform;
    char padding_98[8];
    void* shellSounds;
    char padding_a8[1];
    char soundState;
} ShellEjection_Recovered;

struct_0 * ShellEjection_OnCollisionEnter(struct_0 *ptr)
{
    void* v0;  // x20
    struct_0 *v1;  // x0
    unsigned long v2;  // x0

    if (!ptr->field_a9)
        return ptr;
    v0 = ptr->field_a0;
    if (v0)
    {
        v1 = ptr;
        if ((long long)v0[24])
        {
            v2 = Random__Range(0);
            if ((int)v0[24] <= (unsigned int)v2)
            {
                sub_f7db7c(v2);
            }
            else if (ptr->field_90)
            {
                Transform__get_position(ptr->field_90, 0);
                v1 = PlayAudioAtPos__PlayClipAt(*((long long *)(32 + (char *)v0 + 8 * (v2 & 4294967295))), 0);
            }
            else
            {
                sub_f7db74();
                sub_f7db7c(v2);
            }
        }
        ptr->field_a9 = 0;
        return v1;
    }
    v2 = sub_f7db74();
    sub_f7db7c(v2);
}
```


## `ShellEjection.ctor` — RVA `0xcb54f0`

- Decompiled symbol: `ShellEjection_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[168];
    unsigned short field_a8;
} struct_0;

long long ShellEjection_ctor(struct_0 *ptr)
{
    ptr->field_a8 = 257;
}
```


## `ShellEjection.<CalcShellPos>d__29.Dispose` — RVA `0xcb5500`

- Decompiled symbol: `ShellEjection_CalcShellPos_d__29_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long ShellEjection_CalcShellPos_d__29_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `ShellEjection.<CalcShellPos>d__29.MoveNext` — RVA `0xcb5504`

- Decompiled symbol: `ShellEjection_CalcShellPos_d__29_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `608` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    unsigned long long field_18;
    struct struct_2 *field_20;
} struct_4;

typedef struct struct_2 {
    char padding_0[32];
    struct struct_0 *field_20;
    struct struct_3 *field_28;
    struct struct_1 *field_30;
    char padding_38[8];
    unsigned long long field_40;
    long long field_48;
    char padding_50[64];
    long long field_90;
    char padding_98[16];
    char field_a8;
    char padding_a9[19];
    unsigned int field_bc;
    char padding_c0[8];
    char field_c8;
} struct_2;

typedef struct struct_1 {
    char padding_0[296];
    char field_128;
    char padding_129[95];
    unsigned int field_188;
    unsigned int field_18c;
    unsigned int field_190;
} struct_1;

typedef struct struct_0 {
    char padding_0[676];
    char field_2a4;
} struct_0;

typedef struct struct_3 {
    char padding_0[160];
    char field_a0;
    char padding_a1[527];
    char field_2b0;
    char field_2b1;
    char padding_2b2[16];
    char field_2c2;
    char padding_2c3[25];
    char field_2dc;
    char padding_2dd[11];
    char field_2e8;
} struct_3;

unsigned int ShellEjection_CalcShellPos_d__29_MoveNext(struct_4 *p)
{
    struct_2 *ptr;  // x20
    unsigned int v1;  // s1
    unsigned long v8;  // 4138
    unsigned int v9;  // s8
    unsigned int v10;  // s9
    unsigned long v11;  // 4138
    unsigned int v12;  // s8
    unsigned int v13;  // s9
    unsigned long v14;  // 4138
    char v15[745];  // x8
    char v16[745];  // x8
    unsigned int v17;  // s0
    struct_4 *addr;  // x19
    unsigned long v2;  // 4138
    unsigned int v3;  // s8
    unsigned int v4;  // s9
    unsigned long v5;  // 4138
    unsigned long long v6;  // x0
    unsigned int v7;  // s1

    if (1 < p->field_10)
        return 0;
    ptr = p->field_20;
    p->field_10 = 4294967295;
    if (ptr && ptr->field_28)
    {
        if (!ptr->field_28->field_a0)
        {
            if (!ptr->field_a8)
            {
LABEL_10b5714:
                p->field_18 = 0;
                addr = &p->field_18;
                sub_f7d8d0(addr, 0);
                *((unsigned int *)&addr->padding_0[8]) = 1;
                return 1;
            }
            if (ptr->field_30)
            {
                Time__get_time(0);
                v7 = ptr->field_bc + ptr->field_30->field_188;
                v8 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v7, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v7, v17) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v7, v17) & 1)) & ((unsigned long long)(char)(CmpF(v7, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v7, v17) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if (!((char)v8))
                {
                    if (ptr->field_20)
                    {
                        if (ptr->field_20->field_2a4)
                            goto LABEL_10b562c;
                        goto LABEL_10b569c;
                    }
                }
                else
                {
LABEL_10b562c:
                    if (ptr->field_30)
                    {
                        v9 = ptr->field_bc;
                        v10 = ptr->field_30->field_190;
                        Time__get_time(0);
                        v11 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v9 + v10, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v9 + v10, v17) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v9 + v10, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v9 + v10, v17) & 1)) & ((unsigned long long)(char)(CmpF(v9 + v10, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v9 + v10, v17) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v11))
                        {
                            if (ptr->field_20)
                            {
                                if (!ptr->field_20->field_2a4)
                                    goto LABEL_10b5660;
                                goto LABEL_10b569c;
                            }
                        }
                        else
                        {
LABEL_10b5660:
                            if (ptr->field_30)
                            {
                                v12 = ptr->field_bc;
                                v13 = ptr->field_30->field_18c;
                                Time__get_time(0);
                                v14 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v12 + v13, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v12 + v13, v17) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v12 + v13, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v12 + v13, v17) & 1)) & ((unsigned long long)(char)(CmpF(v12 + v13, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v12 + v13, v17) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                                if ((char)v14 || !ptr->field_c8)
                                {
                                    if (ptr->field_30)
                                    {
                                        if (ptr->field_30->field_128)
                                            goto LABEL_10b569c;
                                        v15 = ptr->field_28;
                                        if (v15)
                                        {
                                            if ((!v15[689] || v15[706]) && (!v15[732] || !v15[744]))
                                                goto LABEL_10b5714;
                                            goto LABEL_10b569c;
                                        }
                                    }
                                }
                                else
                                {
LABEL_10b569c:
                                    if (ptr->field_48)
                                    {
                                        Rigidbody__get_velocity(ptr->field_48, 0);
                                        if (ptr->field_90)
                                        {
                                            Transform__set_parent(ptr->field_90, 0, 0);
                                            v16 = ptr->field_28;
                                            if (v16)
                                            {
                                                if (v16[689] || v16[688] || !v16[744])
                                                {
                                                    ptr->field_a8 = 0;
                                                    return 0;
                                                }
                                                v6 = ptr->field_40;
                                                if (ptr->field_40)
                                                {
                                                    Rigidbody__AddForce(v6, 2, 0);
                                                    ptr->field_a8 = 0;
                                                    return 0;
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
        else if (ptr->field_30)
        {
            Time__get_time(0);
            v1 = ptr->field_bc + ptr->field_30->field_188;
            v2 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v1, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v17) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v17) & 1)) & ((unsigned long long)(char)(CmpF(v1, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v17) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v2)
            {
LABEL_10b5574:
                if (ptr->field_30)
                {
                    v3 = ptr->field_bc;
                    v4 = ptr->field_30->field_190;
                    Time__get_time(0);
                    v5 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v3 + v4, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v3 + v4, v17) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3 + v4, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v3 + v4, v17) & 1)) & ((unsigned long long)(char)(CmpF(v3 + v4, v17)) >> 5 & 3 | (unsigned long long)(CmpF(v3 + v4, v17) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if ((char)v5)
                    {
                        p->field_18 = 0;
                        addr = &p->field_18;
                        sub_f7d8d0(addr, 0);
                        *((unsigned int *)&addr->padding_0[8]) = 1;
                        return 1;
                    }
                    if (ptr->field_20)
                    {
                        if (!ptr->field_20->field_2a4)
                        {
                            p->field_18 = 0;
                            addr = &p->field_18;
                            sub_f7d8d0(addr, 0);
                            *((unsigned int *)&addr->padding_0[8]) = 1;
                            return 1;
                        }
LABEL_10b55a8:
                        if (ptr->field_90)
                        {
                            Transform__set_parent(ptr->field_90, 0, 0);
                            if (ptr->field_48)
                            {
                                Rigidbody__get_velocity(ptr->field_48, 0);
                                if (ptr->field_40)
                                {
                                    Rigidbody__AddForce(ptr->field_40, 2, 0);
                                    ptr->field_a8 = 0;
                                    return 0;
                                }
                            }
                        }
                    }
                }
            }
            else if (ptr->field_20)
            {
                if (!ptr->field_20->field_2a4)
                    goto LABEL_10b55a8;
                goto LABEL_10b5574;
            }
        }
    }
    sub_f7db74();
}
```


## `ShellEjection.<CalcShellPos>d__29.get_Current` — RVA `0xcb5764`

- Decompiled symbol: `ShellEjection_CalcShellPos_d__29_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long ShellEjection_CalcShellPos_d__29_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `ShellEjection.<CalcShellPos>d__29.Reset` — RVA `0xcb576c`

- Decompiled symbol: `ShellEjection_CalcShellPos_d__29_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04cf8;

void ShellEjection_CalcShellPos_d__29_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04cf8));
}
```


## `ShellEjection.<CalcShellPos>d__29.get_Current` — RVA `0xcb57a4`

- Decompiled symbol: `ShellEjection_CalcShellPos_d__29_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long ShellEjection_CalcShellPos_d__29_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
