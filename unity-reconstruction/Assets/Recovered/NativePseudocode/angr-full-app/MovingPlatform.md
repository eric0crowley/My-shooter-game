# Native pseudocode: MovingPlatform

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MovingPlatform.Start` — RVA `0xc98cb8`

- Decompiled symbol: `MovingPlatform_Start`
- Metadata signature: `private IEnumerator Start() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern char g_1fab490;

struct_0 * MovingPlatform_Start(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab490 & 1))
    {
        sub_f7d92c("=m");
        g_1fab490 = 1;
    }
    v0 = sub_f7db70(g_1ef3578);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `MovingPlatform.<Start>d__5.ctor` — RVA `0xc98d24`

- Decompiled symbol: `MovingPlatform_Start_d__5_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void MovingPlatform_Start_d__5_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `MovingPlatform.OnCollisionEnter` — RVA `0xc98d4c`

- Decompiled symbol: `MovingPlatform_OnCollisionEnter`
- Metadata signature: `private void OnCollisionEnter(Collision collision) { }`
- Native interval: `292` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[196];
    unsigned int field_c4;
} struct_3;

typedef struct struct_1 {
    char padding_0[48];
    struct struct_0 *field_30;
} struct_1;

typedef struct struct_2 {
    char padding_0[40];
    void* field_28;
} struct_2;

typedef struct struct_0 {
    char padding_0[40];
    void* field_28;
} struct_0;

extern struct_2 *g_1ef0c58;
extern long long g_1efecc8;
extern char g_1fab491;

long long MovingPlatform_OnCollisionEnter(unsigned long a0, long long a1)
{
    unsigned long v0;  // x0
    long long v1;  // x0
    unsigned long v2;  // x0
    struct_3 *v3;  // x0
    long long v4;  // x0
    struct_2 *v5;  // x0

    if (!(g_1fab491 & 1))
    {
        sub_f7d92c("s.");
        sub_f7d92c(&g_1efecc8);
        sub_f7d92c(&g_1ef0c58);
        g_1fab491 = 1;
    }
    if (a1 && Collision__get_gameObject(a1, 0))
    {
        v0 = GameObject__get_layer();
        if ((unsigned int)v0 != 12)
        {
            return v0;
        }
        else if (Collision__get_gameObject(a1, 0))
        {
            v1 = sub_1249224();
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v2 = Object__op_Implicit(v1, 0);
            if (!((char)v2 & 1))
            {
                return v2;
            }
            else if (Collision__get_gameObject(a1, 0))
            {
                v3 = sub_1249224();
                if (v3)
                {
                    v4 = Collision__get_gameObject(a1, 0);
                    if (g_1eeea08->field_b8->field_0)
                    {
                        v5 = AzuObjectPool__RecyclePooledObj(g_1eeea08->field_b8->field_0, v3->field_c4, v4);
                        return AzuObjectPool__RecyclePooledObj(g_1eeea08->field_b8->field_0, v3->field_c4, v4);
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `MovingPlatform.ctor` — RVA `0xc98e70`

- Decompiled symbol: `MovingPlatform_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    unsigned long long field_30;
} struct_0;

long long MovingPlatform_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_30 = 0x3f8000003f800000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```

## `MovingPlatform.<Start>d__5.Dispose` — RVA `0xc98e80`

- Decompiled symbol: `MovingPlatform_Start_d__5_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long MovingPlatform_Start_d__5_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `MovingPlatform.<Start>d__5.MoveNext` — RVA `0xc98e84`

- Decompiled symbol: `MovingPlatform_Start_d__5_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `312` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    unsigned long long field_18;
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
    long long field_28;
    char padding_30[4];
    unsigned int field_34;
    long long field_38;
} struct_0;

unsigned int MovingPlatform_Start_d__5_MoveNext(struct_1 *ptr)
{
    struct_0 *addr;  // x20
    long long v1;  // x1
    struct_0 *p;  // x0
    unsigned int v3;  // s0
    unsigned int v4;  // s2
    unsigned long v5;  // 4125
    unsigned long v6;  // 4125
    struct_1 *ptr3;  // x19

    addr = ptr->field_20;
    if (ptr->field_10 != 1)
    {
        if (ptr->field_10)
            return 0;
        ptr->field_10 = 4294967295;
        if (addr)
        {
            v1 = Component__get_transform(addr, 0);
            p = addr;
            p->field_38 = v1;
            sub_f7d8d0((struct struct_0 *)&p->field_38, v1);
LABEL_1098ee0:
            if (addr->field_38 && (Transform__get_position(addr->field_38, 0), addr->field_28))
            {
                Transform__get_position(addr->field_28, 0);
                v3 = 0x3f800000;
                v5 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v4, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v4) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v4) & 1)) & ((unsigned long long)(char)(CmpF(v4, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v4) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v5)
                {
LABEL_1098f40:
                    addr->field_34 = v3;
LABEL_1098f44:
                    Time__get_deltaTime(0);
                    if (addr->field_38)
                    {
                        Transform__Translate(addr->field_38, 0, 0);
                        ptr->field_18 = 0;
                        ptr3 = &ptr->field_18;
                        sub_f7d8d0(ptr3, 0);
                        *((unsigned int *)&ptr3->padding_0[8]) = 1;
                        return 1;
                    }
                }
                else if (addr->field_38 && (Transform__get_position(addr->field_38, 0), addr->field_20))
                {
                    Transform__get_position(addr->field_20, 0);
                    v3 = 0xbf800000;
                    v6 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v4, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v4) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v4) & 1)) & ((unsigned long long)(char)(CmpF(v4, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v4) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if ((char)v6)
                        goto LABEL_1098f44;
                    goto LABEL_1098f40;
                }
            }
        }
    }
    else
    {
        ptr->field_10 = 4294967295;
        if (addr)
            goto LABEL_1098ee0;
    }
    sub_f7db74();
}
```

## `MovingPlatform.<Start>d__5.get_Current` — RVA `0xc98fbc`

- Decompiled symbol: `MovingPlatform_Start_d__5_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long MovingPlatform_Start_d__5_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `MovingPlatform.<Start>d__5.Reset` — RVA `0xc98fc4`

- Decompiled symbol: `MovingPlatform_Start_d__5_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f049a0;

void MovingPlatform_Start_d__5_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f049a0));
}
```

## `MovingPlatform.<Start>d__5.get_Current` — RVA `0xc98ffc`

- Decompiled symbol: `MovingPlatform_Start_d__5_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long MovingPlatform_Start_d__5_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
