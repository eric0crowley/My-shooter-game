# Native pseudocode: MovingElevator

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MovingElevator.Start` — RVA `0xc98964`

- Decompiled symbol: `MovingElevator_Start`
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

extern char g_1fab48e;

struct_0 * MovingElevator_Start(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab48e & 1))
    {
        sub_f7d92c(";m");
        g_1fab48e = 1;
    }
    v0 = sub_f7db70(g_1ef3570);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `MovingElevator.<Start>d__5.ctor` — RVA `0xc989d0`

- Decompiled symbol: `MovingElevator_Start_d__5_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void MovingElevator_Start_d__5_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `MovingElevator.OnCollisionEnter` — RVA `0xc989f8`

- Decompiled symbol: `MovingElevator_OnCollisionEnter`
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
extern char g_1fab48f;

long long MovingElevator_OnCollisionEnter(unsigned long a0, long long a1)
{
    unsigned long v0;  // x0
    long long v1;  // x0
    unsigned long v2;  // x0
    struct_3 *v3;  // x0
    long long v4;  // x0
    struct_2 *v5;  // x0

    if (!(g_1fab48f & 1))
    {
        sub_f7d92c("s.");
        sub_f7d92c(&g_1efecc8);
        sub_f7d92c(&g_1ef0c58);
        g_1fab48f = 1;
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

## `MovingElevator.ctor` — RVA `0xc98b1c`

- Decompiled symbol: `MovingElevator_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[52];
    unsigned long long field_34;
} struct_0;

long long MovingElevator_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    *((unsigned long long *)&(&ptr->padding_0)[1]) = 0x3f8000003f800000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```

## `MovingElevator.<Start>d__5.Dispose` — RVA `0xc98b2c`

- Decompiled symbol: `MovingElevator_Start_d__5_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long MovingElevator_Start_d__5_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `MovingElevator.<Start>d__5.MoveNext` — RVA `0xc98b30`

- Decompiled symbol: `MovingElevator_Start_d__5_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `320` bytes
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
    unsigned int field_28;
    unsigned int field_2c;
    unsigned int field_30;
    char padding_34[4];
    unsigned int field_38;
    char padding_3c[4];
    long long field_40;
} struct_0;

unsigned int MovingElevator_Start_d__5_MoveNext(struct_1 *p)
{
    struct_0 *ptr;  // x20
    long long v1;  // x1
    struct_1 *ptr3;  // x19
    struct_0 *addr;  // x0
    unsigned int v3;  // s0
    unsigned int v4;  // s1
    unsigned int v5;  // s2
    unsigned int v6;  // s0
    unsigned int v7;  // s0
    unsigned long v8;  // 4129
    unsigned long v9;  // 4125

    ptr = p->field_20;
    if (p->field_10 != 1)
    {
        if (p->field_10)
            return 0;
        p->field_10 = 4294967295;
        if (ptr)
        {
            v1 = Component__get_transform(ptr, 0);
            addr = ptr;
            addr->field_40 = v1;
            sub_f7d8d0((struct struct_0 *)&addr->field_40, v1);
            if (Component__get_transform(ptr, 0) && (Transform__get_position(), ptr->field_28 = v3, ptr->field_2c = v4, ptr->field_30 = v5, ptr->field_40))
            {
                Transform__get_position(ptr->field_40, 0);
                v6 = ptr->field_2c;
                v7 = 0xbf800000;
                v8 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v4, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v6) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v6) & 1)) & ((unsigned long long)(char)(CmpF(v4, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v6) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v8)
                {
LABEL_1098bfc:
                    ptr->field_38 = v7;
LABEL_1098c00:
                    Time__get_deltaTime(0);
                    if (ptr->field_40)
                    {
                        Transform__Translate(ptr->field_40, 0, 0);
                        p->field_18 = 0;
                        ptr3 = &p->field_18;
                        sub_f7d8d0(ptr3, 0);
                        *((unsigned int *)&ptr3->padding_0[8]) = 1;
                        return 1;
                    }
                }
                else if (ptr->field_40 && (Transform__get_position(ptr->field_40, 0), ptr->field_20))
                {
                    Transform__get_position(ptr->field_20, 0);
                    v7 = 0x3f800000;
                    v9 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v4, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v4) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v4) & 1)) & ((unsigned long long)(char)(CmpF(v4, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v4) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if ((char)v9)
                        goto LABEL_1098c00;
                    goto LABEL_1098bfc;
                }
            }
        }
    }
    else
    {
        p->field_10 = 4294967295;
    }
    sub_f7db74();
}
```

## `MovingElevator.<Start>d__5.get_Current` — RVA `0xc98c70`

- Decompiled symbol: `MovingElevator_Start_d__5_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long MovingElevator_Start_d__5_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `MovingElevator.<Start>d__5.Reset` — RVA `0xc98c78`

- Decompiled symbol: `MovingElevator_Start_d__5_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04998;

void MovingElevator_Start_d__5_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f04998));
}
```

## `MovingElevator.<Start>d__5.get_Current` — RVA `0xc98cb0`

- Decompiled symbol: `MovingElevator_Start_d__5_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long MovingElevator_Start_d__5_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
