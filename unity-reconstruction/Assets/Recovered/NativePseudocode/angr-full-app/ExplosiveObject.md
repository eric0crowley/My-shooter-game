# Native pseudocode: ExplosiveObject

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ExplosiveObject.Start` — RVA `0xc95ddc`

- Decompiled symbol: `ExplosiveObject_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `228` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ExplosiveObject_Recovered` matched 5 offsets against `ExplosiveObject` metadata (confidence 1.00).

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

typedef struct struct_1 {
    char padding_0[136];
    long long field_88;
} struct_1;

typedef struct ExplosiveObject_Recovered {
    char padding_0[32];
    long long WeaponEffectsComponent;
    unsigned int hitPoints;
    unsigned int initialHitPoints;
    char padding_30[32];
    long long myTransform;
    char padding_58[8];
    long long aSource;
} ExplosiveObject_Recovered;

extern long long g_1efcf18;
extern long long g_1efcf38;
extern long long g_1efebb8;
extern char g_1fab47d;

void ExplosiveObject_Start(struct_2 *ptr)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_0 *v6;  // x0
    struct_1 *ptr3;  // x0
    long long v8;  // x1
    struct_2 *p;  // x0
    long long v10;  // x1
    struct_2 *addr;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab47d & 1))
    {
        sub_f7d92c(&g_1efcf18);
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efebb8);
        g_1fab47d = 1;
    }
    if (Camera__get_main(0))
    {
        v6 = sub_1231bc8();
        if (v6 && v6->field_28)
        {
            ptr3 = sub_1249224(v6->field_28, g_1efebb8);
            if (ptr3)
            {
                v8 = ptr3->field_88;
                p = ptr;
                p->field_20 = v8;
                sub_f7d8d0((struct ExplosiveObject_Recovered *)&p->field_20, v8);
                v10 = Component__get_transform(ptr, 0);
                addr = ptr;
                addr->field_50 = v10;
                sub_f7d8d0((struct ExplosiveObject_Recovered *)&addr->field_50, v10);
                ptr->field_2c = ptr->field_28;
                ptr->field_60 = sub_1231bc8(ptr, g_1efcf18);
                sub_f7d8d0();
                return;
            }
        }
    }
    sub_f7db74();
}
```

## `ExplosiveObject.Update` — RVA `0xc95ec0`

- Decompiled symbol: `ExplosiveObject_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long ExplosiveObject_Update(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `ExplosiveObject.DetectDestroyed` — RVA `0xc95ec4`

- Decompiled symbol: `ExplosiveObject_DetectDestroyed`
- Metadata signature: `private IEnumerator DetectDestroyed() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef30b0;
extern char g_1fab47e;

struct_0 * ExplosiveObject_DetectDestroyed(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab47e & 1))
    {
        sub_f7d92c(&g_1ef30b0);
        g_1fab47e = 1;
    }
    v0 = sub_f7db70(g_1ef30b0);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `ExplosiveObject.<DetectDestroyed>d__19.ctor` — RVA `0xc95f30`

- Decompiled symbol: `ExplosiveObject_DetectDestroyed_d__19_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void ExplosiveObject_DetectDestroyed_d__19_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `ExplosiveObject.ResetExplosiveObject` — RVA `0xc95f58`

- Decompiled symbol: `ExplosiveObject_ResetExplosiveObject`
- Metadata signature: `private void ResetExplosiveObject() { }`
- Native interval: `108` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ExplosiveObject_Recovered` matched 4 offsets against `ExplosiveObject` metadata (confidence 1.00).

```c
typedef struct ExplosiveObject_Recovered {
    char padding_0[40];
    unsigned int hitPoints;
    unsigned int initialHitPoints;
    char padding_30[32];
    long long myTransform;
    unsigned short detonated;
} ExplosiveObject_Recovered;

extern long long g_1efd018;
extern char g_1fab47f;

void ExplosiveObject_ResetExplosiveObject(struct_0 *ptr)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned int v6;  // s0
    long long v7;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab47f & 1))
    {
        sub_f7d92c(&g_1efd018);
        g_1fab47f = 1;
    }
    v6 = ptr->field_2c;
    v7 = ptr->field_50;
    ptr->field_58 = 0;
    ptr->field_28 = v6;
    if (v7)
    {
        v7 = sub_1231bc8(v7, g_1efd018);
        if (v7)
        {
            Renderer__set_enabled();
            return;
        }
    }
    sub_f7db74(v7);
}
```

## `ExplosiveObject.Detonate` — RVA `0xc95fc4`

- Decompiled symbol: `ExplosiveObject_Detonate`
- Metadata signature: `private IEnumerator Detonate() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef30b8;
extern char g_1fab480;

struct_0 * ExplosiveObject_Detonate(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab480 & 1))
    {
        sub_f7d92c(&g_1ef30b8);
        g_1fab480 = 1;
    }
    v0 = sub_f7db70(g_1ef30b8);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `ExplosiveObject.<Detonate>d__21.ctor` — RVA `0xc96030`

- Decompiled symbol: `ExplosiveObject_Detonate_d__21_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void ExplosiveObject_Detonate_d__21_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `ExplosiveObject.ApplyDamage` — RVA `0xc96058`

- Decompiled symbol: `ExplosiveObject_ApplyDamage`
- Metadata signature: `public void ApplyDamage(float damage) { }`
- Native interval: `192` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ExplosiveObject_Recovered` matched 2 offsets against `ExplosiveObject` metadata (confidence 1.00).

```c
typedef struct ExplosiveObject_Recovered {
    char padding_0[40];
    unsigned int hitPoints;
    char padding_2c[44];
    char detonated;
} ExplosiveObject_Recovered;

extern long long g_1efeca8;
extern char g_1fab481;

struct_0 * ExplosiveObject_ApplyDamage(struct_0 *ptr)
{
    struct_0 *v0;  // x0
    struct_0 *v1;  // x0
    struct_0 *v2;  // x0
    unsigned int v3;  // s0
    unsigned int v4;  // s0
    unsigned long v5;  // 4146
    long long v6;  // x0

    v0 = ptr;
    if (!(g_1fab481 & 1))
    {
        v1 = sub_f7d92c(&g_1efeca8);
        g_1fab481 = 1;
        v0 = v1;
    }
    v2 = v0;
    v4 = ptr->field_28 - v3;
    ptr->field_28 = v4;
    v5 = arm64g_calculate_condition(128, (((((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v5)
    {
        return v2;
    }
    else if (!ptr->field_58)
    {
        ptr->field_58 = 1;
        if (Component__get_gameObject(ptr, 0) && sub_1249224())
        {
            Rigidbody__set_useGravity();
            ExplosiveObject__Detonate(ptr);
            v6 = MonoBehaviour__StartCoroutine();
            return MonoBehaviour__StartCoroutine();
        }
        sub_f7db74();
    }
    else
    {
        return v2;
    }
}
```

## `ExplosiveObject.ctor` — RVA `0xc96118`

- Decompiled symbol: `ExplosiveObject_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `44` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ExplosiveObject_Recovered` matched 3 offsets against `ExplosiveObject` metadata (confidence 1.00).

```c
typedef struct ExplosiveObject_Recovered {
    char padding_0[44];
    unsigned long long initialHitPoints;
    unsigned int damageDelay;
    char padding_38[4];
    unsigned long long blastForce;
} ExplosiveObject_Recovered;

long long ExplosiveObject_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    *((unsigned int *)((char *)&ptr->field_2c + 4)) = 1045220557;
    *((unsigned long long *)&(&ptr->padding_0)[1]) = 0x4348000042c80000;
    *((unsigned long long *)&ptr->padding_38) = 0x40e0000041700000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```

## `ExplosiveObject.<DetectDestroyed>d__19.Dispose` — RVA `0xc96144`

- Decompiled symbol: `ExplosiveObject_DetectDestroyed_d__19_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long ExplosiveObject_DetectDestroyed_d__19_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `ExplosiveObject.<DetectDestroyed>d__19.MoveNext` — RVA `0xc96148`

- Decompiled symbol: `ExplosiveObject_DetectDestroyed_d__19_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `812` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_3 *field_20;
} struct_4;

typedef struct struct_3 {
    char padding_0[80];
    long long field_50;
    char padding_58[1];
    char field_59;
    char padding_5a[2];
    unsigned int field_5c;
    long long field_60;
} struct_3;

typedef struct struct_5 {
    char padding_0[24];
    int field_18;
} struct_5;

typedef struct struct_6 {
    char padding_0[32];
    unsigned long long field_20;
    char padding_28[9];
    char field_31;
    char padding_32[70];
    unsigned long long field_78;
} struct_6;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

extern struct_2 *g_1ef0c58;
extern long long g_1ef2440;
extern long long g_1efedb0;
extern long long g_1efedb8;
extern char g_1fab482;

unsigned int ExplosiveObject_DetectDestroyed_d__19_MoveNext(struct_4 *ptr)
{
    struct_3 *v0;  // x19
    struct_5 *p;  // x0
    struct_6 *ptr4;  // x21
    long long v11;  // x0
    long long v12;  // x19
    struct_4 *ptr5;  // x20
    unsigned int v2;  // w8
    struct_5 *addr;  // x20
    unsigned int v4;  // w23
    unsigned long long v5[10];  // x21
    unsigned long v6;  // x0
    unsigned int v7;  // w8
    struct_5 *ptr3;  // x20
    unsigned int v9;  // w22

    if (!(g_1fab482 & 1))
    {
        sub_f7d92c("s.");
        sub_f7d92c(&g_1efedb0);
        sub_f7d92c(&g_1efedb8);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c("s%");
        g_1fab482 = 1;
    }
    if (1 < ptr->field_10)
    {
LABEL_1096454:
        return 0;
    }
    v0 = ptr->field_20;
    ptr->field_10 = 4294967295;
    if (v0)
    {
        if (!v0->field_59)
        {
LABEL_10961f0:
            v12 = sub_f7db70(g_1ef2440);
            WaitForSeconds__ctor(v12, 0);
            ptr->field_18 = v12;
            ptr5 = &ptr->field_18;
            sub_f7d8d0(ptr5, v12);
            *((unsigned int *)&ptr5->padding_0[8]) = 1;
            return 1;
        }
        if (v0->field_60)
        {
            if ((AudioSource__get_isPlaying(v0->field_60, 0) & 1))
                goto LABEL_10961f0;
            if (v0->field_5c)
                ExplosiveObject__ResetExplosiveObject(v0); /* do not return */
            if (Component__get_gameObject(v0, 0) && (p = (struct_5 *)(unsigned long long)sub_1249ec4(), p))
            {
                v2 = p->field_18;
                addr = p;
                if (p->field_18 >= 1)
                {
                    v4 = 0;
                    do
                    {
                        if (v2 <= v4)
                            sub_f7db7c(p);
                        v5 = *((long long *)&addr[1].padding_0[4 + 8 * v4]);
                        if (!v5)
                            sub_f7db7c(sub_f7db74());
                        if (!g_1eeea08->field_b8->field_0)
                            sub_f7db7c(sub_f7db74());
                        v6 = Component__get_transform(g_1eeea08->field_b8->field_0, 0);
                        if (!v5[9])
                            sub_f7db7c(sub_f7db74());
                        Transform__set_parent(v5[9], v6, 0);
                        if (!v5[8] || !((GameObject__SetActive(v5[8], 0, 0), Component__get_gameObject(v5, 0))))
                            goto LABEL_109646c;
                    } while ((p = (struct_5 *)GameObject__SetActive(), v2 = (unsigned int)addr->field_18, v4 += 1, v4 < v2));
                }
                else if (Component__get_gameObject(v0, 0) && (p = (struct_5 *)(unsigned long long)sub_1249ec4(), p))
                {
                    v7 = p->field_18;
                    ptr3 = p;
                    if (v7 >= 1)
                    {
                        v9 = 0;
                        do
                        {
                            if (v7 <= v9)
                                sub_f7db7c(p);
                            ptr4 = *((long long *)&ptr3[1].padding_0[4 + 8 * v9]);
                            if (!ptr4)
                                sub_f7db7c(sub_f7db74());
                            if (!Component__get_transform(ptr4, 0))
                                sub_f7db7c(sub_f7db74());
                            Transform__set_parent();
                            if (!ptr4->field_20)
                                sub_f7db7c(sub_f7db74());
                            Rigidbody__set_isKinematic(ptr4->field_20, 0, 0);
                            if (!ptr4->field_78 || !((Collider__set_isTrigger(ptr4->field_78, 0, 0), Component__get_gameObject(ptr4, 0))))
                                goto LABEL_109646c;
                        } while ((p = (struct_5 *)(unsigned long long)GameObject__set_tag(), ptr4->field_31 = 1, v7 = (unsigned int)ptr3->field_18, v9 += 1, v9 < v7));
                    }
                    else if (v0->field_50)
                    {
                        v11 = Component__get_gameObject(v0->field_50, 0);
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        Object__Destroy(v11, 0);
                        goto LABEL_1096454;
                    }
                }
            }
        }
    }
LABEL_109646c:
    sub_f7db7c(sub_f7db74());
}
```

## `ExplosiveObject.<DetectDestroyed>d__19.get_Current` — RVA `0xc96474`

- Decompiled symbol: `ExplosiveObject_DetectDestroyed_d__19_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long ExplosiveObject_DetectDestroyed_d__19_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `ExplosiveObject.<DetectDestroyed>d__19.Reset` — RVA `0xc9647c`

- Decompiled symbol: `ExplosiveObject_DetectDestroyed_d__19_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f045a8;

void ExplosiveObject_DetectDestroyed_d__19_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f045a8));
}
```

## `ExplosiveObject.<DetectDestroyed>d__19.get_Current` — RVA `0xc964b4`

- Decompiled symbol: `ExplosiveObject_DetectDestroyed_d__19_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long ExplosiveObject_DetectDestroyed_d__19_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `ExplosiveObject.<Detonate>d__21.Dispose` — RVA `0xc964bc`

- Decompiled symbol: `ExplosiveObject_Detonate_d__21_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long ExplosiveObject_Detonate_d__21_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `ExplosiveObject.<Detonate>d__21.MoveNext` — RVA `0xc964c0`

- Decompiled symbol: `ExplosiveObject_Detonate_d__21_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `3028` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_2 *field_20;
} struct_3;

typedef struct struct_2 {
    char padding_0[32];
    struct struct_6 *field_20;
    char padding_28[8];
    unsigned int field_30;
    char padding_34[4];
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
    unsigned int field_44;
    char padding_48[8];
    long long field_50;
    char padding_58[1];
    char field_59;
    char padding_5a[2];
    unsigned int field_5c;
    long long field_60;
    long long field_68;
    long long field_70;
} struct_2;

typedef struct struct_6 {
    char padding_0[120];
    struct struct_3 *field_78;
    struct struct_5 *field_80;
} struct_6;

typedef struct struct_5 {
    char padding_0[24];
    int field_18;
    char padding_1c[196];
    unsigned int field_e0;
} struct_5;

typedef struct struct_3 {
    char padding_0[176];
    struct struct_2 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_3;

typedef struct struct_5 {
    char padding_0[176];
    struct struct_4 *field_b0;
    char padding_b8[118];
    unsigned short field_12e;
} struct_5;

typedef struct struct_2 {
    char padding_0[8];
    unsigned int field_8;
} struct_2;

typedef struct struct_4 {
    char padding_0[8];
    unsigned int field_8;
} struct_4;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef0e48;
extern long long g_1ef22e8;
extern long long g_1ef2440;
extern long long g_1efcf70;
extern long long g_1efd010;
extern long long g_1efd018;
extern long long g_1efd080;
extern long long g_1efeb30;
extern long long g_1efeb48;
extern long long g_1efeb90;
extern long long g_1efebb0;
extern long long g_1efebb8;
extern long long g_1efec38;
extern long long g_1efec58;
extern char g_1fab2c8;
extern char g_1fab2c9;
extern char g_1fab3df;
extern char g_1fab483;

unsigned int ExplosiveObject_Detonate_d__21_MoveNext(struct_3 *p)
{
    struct_2 *ptr;  // x19
    long long v9;  // x19
    unsigned long v17;  // x21
    struct_5 *v18;  // x29
    long long v19;  // x0
    uint128_t v20;  // q8
    unsigned int v21;  // s3
    unsigned long v22;  // 4244
    uint128_t v23;  // q14
    long long v24;  // x0
    unsigned int v25;  // s14
    struct_5 *ptr3;  // x0, Other Possible Types: unsigned int [57]
    struct_3 *ptr4;  // x20
    unsigned int v27;  // s3
    unsigned int v28;  // s0
    unsigned int v29;  // s0
    unsigned int v30;  // s1
    unsigned int v31;  // s0
    unsigned long v32;  // 4278
    unsigned long v33;  // 4142
    long long v34;  // x0
    long long v35;  // x0
    long long v36;  // x0
    long long v11;  // x0
    int v37;  // q8
    long long v38;  // x25
    long long v39;  // x0
    long long v40;  // x0
    int v41;  // q8
    long long v42;  // x25
    long long v43;  // x0
    long long v44;  // x0
    unsigned int v45;  // w0
    unsigned long v46;  // x0
    unsigned int v12;  // w0
    long long v47;  // x0
    unsigned int v48;  // w0
    unsigned long v49;  // x0
    long long v50;  // x0
    unsigned int v51;  // w0
    long long v52;  // x0
    long long v53;  // x0
    long long v54;  // x0
    long long v55;  // x25
    unsigned long v56;  // x0
    unsigned int i;  // w8
    struct_5 *addr;  // x20
    uint128_t v15;  // q0
    unsigned long long v16;  // x28
    unsigned long v0;  // [bp-0xe0]
    unsigned int v1;  // [bp-0xd8]
    unsigned int v2;  // [bp-0xd4]
    int choice;  // [bp-0xd0]
    uint128_t flag2;  // [bp-0xc0]
    uint128_t flag;  // [bp-0xb4]
    char *v6;  // [bp-0x60]
    char v7;  // [bp+0x0]

    v6 = &v7;
    if (!(g_1fab483 & 1))
    {
        sub_f7d92c(&g_1efcf70);
        sub_f7d92c(&g_1efd010);
        sub_f7d92c(&g_1efd018);
        sub_f7d92c(&g_1efd080);
        sub_f7d92c(&g_1efeb30);
        sub_f7d92c(&g_1efeb48);
        sub_f7d92c(&g_1efeb90);
        sub_f7d92c(&g_1efebb0);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1efec38);
        sub_f7d92c(&g_1efec58);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef0e48);
        sub_f7d92c(&g_1ef2440);
        g_1fab483 = 1;
    }
    flag = 0;
    choice = 0;
    flag2 = 0;
    ptr = p->field_20;
    if (p->field_10 == 1)
    {
        p->field_10 = 4294967295;
        if (ptr && ptr->field_50 && (Transform__get_position(ptr->field_50, 0), ptr->field_20 && (WeaponEffects__ExplosionEffect(ptr->field_20), ptr->field_50 && sub_1231bc8(ptr->field_50, g_1efd018))))
        {
            Renderer__set_enabled();
            Time__get_timeScale(0);
            Time__get_timeScale(0);
            Random__Range(0);
            if (ptr->field_60 && (AudioSource__set_pitch(ptr->field_60, 0), ptr->field_60 && (AudioSource__Play(ptr->field_60, 0), v11 = ptr->field_50, ptr->field_59 = 1, v11)))
            {
                Transform__get_position(v11, 0);
                v12 = LayerMask__op_Implicit(ptr->field_44, 0);
                if (!g_1ef0e48->field_e0)
                    sub_f7da5c(g_1ef0e48);
                ptr3 = Physics__OverlapSphere(v12, 1, 0);
                if (ptr3)
                {
                    i = ptr3->field_18;
                    addr = ptr3;
                    if (i < 1)
                    {
LABEL_1097040:
                        MonoBehaviour__StartCoroutine(ptr, ExplosiveObject__DetectDestroyed(ptr), 0);
                        return 0;
                    }
                    v0 = &ptr->field_70;
                    v15 = 925353388;
                    v16 = 0;
                    v17 = &ptr->field_68;
                    v18 = &addr->padding_1c[4];
                    v1 = 925353388;
                    do
                    {
                        if (i <= (unsigned int)v16)
                            sub_f7db7c(ptr3);
                        if (!*((long long *)&v18->padding_0[8 * v16]))
                            sub_f7db7c(sub_f7db74());
                        v19 = Component__get_transform(*((long long *)&v18->padding_0[8 * v16]), 0);
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        ptr3 = Object__op_Inequality(v19, ptr->field_50, 0);
                        if (!(ptr3 & 1))
                            continue;
                        if (!ptr->field_50)
                            sub_f7db7c(sub_f7db74());
                        ptr3 = Transform__get_position(ptr->field_50, 0);
                        if (addr->field_18 <= (unsigned int)v16)
                            sub_f7db7c(ptr3);
                        if (!*((long long *)&v18->padding_0[8 * v16]))
                            sub_f7db7c(sub_f7db74());
                        v20 = v15;
                        if (!Component__get_transform(*((long long *)&v18->padding_0[8 * v16]), 0))
                            sub_f7db7c(sub_f7db74());
                        Transform__get_position();
                        if (!ptr->field_50)
                            sub_f7db7c(sub_f7db74());
                        Transform__get_position(ptr->field_50, 0);
                        if (!g_1fab2c8)
                        {
                            v2 = v15;
                            sub_f7d92c("_F");
                            v15 = v2;
                            g_1fab2c8 = 1;
                        }
                        if (!g_1ef07e8->field_e0)
                        {
                            v2 = v15;
                            sub_f7da5c(g_1ef07e8);
                        }
                        v21 = [D] unsupported_Iop_SqrtF32();
                        v22 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v21, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v21, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v21, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v21, v1) & 1)) & ((unsigned long long)(char)(CmpF(v21, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v21, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v22))
                        {
                            v23 = v20;
                        }
                        else
                        {
                            v23 = v20;
                            if (!g_1fab2c9)
                            {
                                sub_f7d92c(&g_1ef22e8);
                                g_1fab2c9 = 1;
                            }
                        }
                        if (!g_1ef0e48->field_e0)
                            sub_f7da5c(g_1ef0e48);
                        v15 = v23;
                        ptr3 = Physics__Raycast(&choice, 0);
                        if (!(ptr3 & 1))
                            continue;
                        if (addr->field_18 <= (unsigned int)v16)
                            sub_f7db7c(ptr3);
                        if (!*((long long *)&v18->padding_0[8 * v16]))
                            sub_f7db7c(sub_f7db74());
                        v24 = sub_1231bc8(*((long long *)&v18->padding_0[8 * v16]), g_1efcf70);
                        ptr->field_68 = v24;
                        sub_f7d8d0(v17, v24);
                        if (!ptr->field_50)
                            sub_f7db7c(sub_f7db74());
                        v25 = ptr->field_30;
                        ptr3 = Transform__get_position(ptr->field_50, 0);
                        if (addr->field_18 <= (unsigned int)v16)
                            sub_f7db7c(ptr3);
                        if (!*((long long *)&v18->padding_0[8 * v16]))
                            sub_f7db7c(sub_f7db74());
                        if (!Component__get_transform(*((long long *)&v18->padding_0[8 * v16]), 0))
                            sub_f7db7c(sub_f7db74());
                        Transform__get_position();
                        if (!g_1fab3df)
                        {
                            sub_f7d92c("_F");
                            g_1fab3df = 1;
                        }
                        ptr3 = g_1ef07e8;
                        if (!g_1ef07e8->field_e0)
                            ptr3 = sub_f7da5c(g_1ef07e8);
                        v27 = ptr->field_40;
                        v28 = [D] unsupported_Iop_SqrtF32();
                        v29 = 0x3f800000 - v28 / ptr->field_40;
                        v30 = [D] unsupported_Iop_ZeroHI96ofV128();
                        v31 = 0;
                        v32 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v29, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v29, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(0x3f800000 - v28 / v27, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 - v28 / v27, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v29, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(0x3f800000 - v28 / v27, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v32)
                            v31 = v30;
                        v15 = v25 * v31;
                        ptr->field_38 = v15;
                        v33 = arm64g_calculate_condition(176, (((((unsigned long long)(char)(CmpF((unsigned int)v15, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v15, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((unsigned int)v15, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v15, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF((unsigned int)v15, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned int)v15, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v33)
                            continue;
                        v34 = RaycastHit__get_collider(&choice, 0);
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        ptr3 = Object__op_Equality(v34, *((long long *)v17), 0);
                        if (!(ptr3 & 1))
                            continue;
                        if (!*((long long *)v17))
                            sub_f7db7c(sub_f7db74());
                        if (!Component__get_gameObject(*((long long *)v17), 0))
                            sub_f7db7c(sub_f7db74());
                        ptr3 = GameObject__get_layer();
                        if ((unsigned int)ptr3)
                        {
                            if ((unsigned int)ptr3 != 11)
                            {
                                if ((unsigned int)ptr3 == 13)
                                {
                                    if (*((long long *)v17))
                                    {
                                        if (Component__get_gameObject(*((long long *)v17), 0))
                                        {
                                            v35 = sub_1249224();
                                            if (!g_1ef0c58->field_e0)
                                                sub_f7da5c(g_1ef0c58);
                                            if (((char)Object__op_Implicit(v35, 0) & 1))
                                            {
                                                if (*((long long *)v17))
                                                {
                                                    if (Component__get_gameObject(*((long long *)v17), 0))
                                                    {
                                                        v36 = sub_1249224();
                                                        v37 = (int)ptr->field_38;
                                                        v38 = v36;
                                                        if (!g_1fab2c9)
                                                        {
                                                            sub_f7d92c(&g_1ef22e8);
                                                            g_1fab2c9 = 1;
                                                        }
                                                        if (!ptr->field_50)
                                                            sub_f7db7c(sub_f7db74());
                                                        Transform__get_position(ptr->field_50, 0);
                                                        if (!v38)
                                                            sub_f7db7c(sub_f7db74());
                                                        v15 = (uint128_t)v37;
                                                        CharacterDamage__ApplyDamage(v38, ptr->field_50, 0, 1, 0, 0);
                                                    }
                                                    else
                                                    {
                                                        sub_f7db7c(sub_f7db74());
                                                    }
                                                }
                                                else
                                                {
                                                    sub_f7db7c(sub_f7db74());
                                                }
                                            }
                                            if (!*((long long *)v17))
                                                sub_f7db7c(sub_f7db74());
                                            if (Component__get_gameObject(*((long long *)v17), 0))
                                            {
                                                v39 = sub_1249224();
                                                if (!g_1ef0c58->field_e0)
                                                    sub_f7da5c(g_1ef0c58);
                                                ptr3 = Object__op_Implicit(v39, 0);
                                                if (((char)ptr3 & 1))
                                                {
                                                    if (*((long long *)v17))
                                                    {
                                                        if (Component__get_gameObject(*((long long *)v17), 0))
                                                        {
                                                            v40 = sub_1249224();
                                                            v41 = (int)ptr->field_38;
                                                            v42 = v40;
                                                            if (!g_1fab2c9)
                                                            {
                                                                sub_f7d92c(&g_1ef22e8);
                                                                g_1fab2c9 = 1;
                                                            }
                                                            if (!ptr->field_50)
                                                                sub_f7db7c(sub_f7db74());
                                                            Transform__get_position(ptr->field_50, 0);
                                                            if (!v42)
                                                                sub_f7db7c(sub_f7db74());
                                                            v15 = (uint128_t)v41;
                                                            ptr3 = LocationDamage__ApplyDamage(v42, ptr->field_50, 0, 1, 0);
                                                        }
                                                        else
                                                        {
                                                            sub_f7db7c(sub_f7db74());
                                                        }
                                                    }
                                                    else
                                                    {
                                                        sub_f7db7c(sub_f7db74());
                                                    }
                                                }
                                            }
                                            else
                                            {
                                                sub_f7db7c(sub_f7db74());
                                            }
                                        }
                                        else
                                        {
                                            sub_f7db7c(sub_f7db74());
                                        }
                                    }
                                    else
                                    {
                                        sub_f7db7c(sub_f7db74());
                                    }
                                }
                            }
                            else
                            {
                                if (*((long long *)v17))
                                {
                                    if (Component__get_gameObject(*((long long *)v17), 0))
                                    {
                                        v43 = sub_1249224();
                                        if (!g_1ef0c58->field_e0)
                                            sub_f7da5c(g_1ef0c58);
                                        ptr3 = Object__op_Implicit(v43, 0);
                                        if (((char)ptr3 & 1))
                                        {
                                            if (*((long long *)v17))
                                            {
                                                if (Component__get_gameObject(*((long long *)v17), 0))
                                                {
                                                    if (sub_1249224())
                                                    {
                                                        v15 = ptr->field_38;
                                                        ptr3 = FPSPlayer__ApplyDamage();
                                                    }
                                                    else
                                                    {
                                                        sub_f7db7c(sub_f7db74());
                                                    }
                                                }
                                                else
                                                {
                                                    sub_f7db7c(sub_f7db74());
                                                }
                                            }
                                            else
                                            {
                                                sub_f7db7c(sub_f7db74());
                                            }
                                        }
                                    }
                                    else
                                    {
                                        sub_f7db7c(sub_f7db74());
                                    }
                                }
                                else
                                {
                                    sub_f7db7c(sub_f7db74());
                                }
                            }
                        }
                        else
                        {
                            if (*((long long *)v17))
                            {
                                if (Component__get_gameObject(*((long long *)v17), 0))
                                {
                                    v44 = sub_1249224();
                                    if (!g_1ef0c58->field_e0)
                                        sub_f7da5c(g_1ef0c58);
                                    v45 = Object__op_Implicit(v44, 0);
                                    if (!*((long long *)v17))
                                        sub_f7db7c(sub_f7db74());
                                    if (Component__get_gameObject(*((long long *)v17), 0))
                                    {
                                        if (((char)v45 & 1))
                                        {
                                            v46 = sub_1249224();
                                            if (!v46)
                                                sub_f7db7c(sub_f7db74());
                                            v15 = ptr->field_38;
                                            ptr3 = BreakableObject__ApplyDamage(v46);
                                        }
                                        else
                                        {
                                            v47 = sub_1249224();
                                            if (!g_1ef0c58->field_e0)
                                                sub_f7da5c(g_1ef0c58);
                                            v48 = Object__op_Implicit(v47, 0);
                                            if (!*((long long *)v17))
                                                sub_f7db7c(sub_f7db74());
                                            if (Component__get_gameObject(*((long long *)v17), 0))
                                            {
                                                if (((char)v48 & 1))
                                                {
                                                    v49 = sub_1249224();
                                                    if (!v49)
                                                        sub_f7db7c(sub_f7db74());
                                                    ptr3 = (unsigned long long)AppleFall__ApplyDamage(v49);
                                                }
                                                else
                                                {
                                                    v50 = sub_1249224();
                                                    if (!g_1ef0c58->field_e0)
                                                        sub_f7da5c(g_1ef0c58);
                                                    v51 = Object__op_Implicit(v50, 0);
                                                    if (!*((long long *)v17))
                                                        sub_f7db7c(sub_f7db74());
                                                    if (Component__get_gameObject(*((long long *)v17), 0))
                                                    {
                                                        if (((char)v51 & 1))
                                                        {
                                                            v56 = sub_1249224();
                                                            if (!v56)
                                                                sub_f7db7c(sub_f7db74());
                                                            ExplosiveObject__ApplyDamage(v56);
                                                        }
                                                        else
                                                        {
                                                            v52 = sub_1249224();
                                                            if (!g_1ef0c58->field_e0)
                                                                sub_f7da5c(g_1ef0c58);
                                                            ptr3 = Object__op_Implicit(v52, 0);
                                                            if (((char)ptr3 & 1))
                                                            {
                                                                if (*((long long *)v17))
                                                                {
                                                                    if (Component__get_gameObject(*((long long *)v17), 0))
                                                                    {
                                                                        if (sub_1249224())
                                                                            ptr3 = MineExplosion__ApplyDamage();
                                                                        else
                                                                            sub_f7db7c(sub_f7db74());
                                                                    }
                                                                    else
                                                                    {
                                                                        sub_f7db7c(sub_f7db74());
                                                                    }
                                                                }
                                                                else
                                                                {
                                                                    sub_f7db7c(sub_f7db74());
                                                                }
                                                            }
                                                        }
                                                    }
                                                    else
                                                    {
                                                        sub_f7db7c(sub_f7db74());
                                                    }
                                                }
                                            }
                                            else
                                            {
                                                sub_f7db7c(sub_f7db74());
                                            }
                                        }
                                    }
                                    else
                                    {
                                        sub_f7db7c(sub_f7db74());
                                    }
                                }
                                else
                                {
                                    sub_f7db7c(sub_f7db74());
                                }
                            }
                            else
                            {
                                sub_f7db7c(sub_f7db74());
                            }
                        }
                        if (addr->field_18 <= (unsigned int)v16)
                            sub_f7db7c(ptr3);
                        if (!*((long long *)&v18->padding_0[8 * v16]))
                            sub_f7db7c(sub_f7db74());
                        if (!Component__get_transform(*((long long *)&v18->padding_0[8 * v16]), 0))
                            sub_f7db7c(sub_f7db74());
                        v53 = sub_1231bc8();
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        ptr3 = Object__op_Implicit(v53, 0);
                        if (!(ptr3 & 1))
                            continue;
                        if (addr->field_18 <= (unsigned int)v16)
                            sub_f7db7c(ptr3);
                        if (!*((long long *)&v18->padding_0[8 * v16]))
                            sub_f7db7c(sub_f7db74());
                        if (!Component__get_transform(*((long long *)&v18->padding_0[8 * v16]), 0))
                            sub_f7db7c(sub_f7db74());
                        v54 = sub_1231bc8();
                        ptr->field_70 = v54;
                        sub_f7d8d0(v0, v54);
                        v55 = ptr->field_70;
                        if (!v55 || !((Rigidbody__get_mass(v55, 0), ptr->field_50)))
                            goto LABEL_109708c;
                        Transform__get_position(ptr->field_50, 0);
                        v15 = ptr->field_3c * (unsigned int)v15;
                        ptr3 = Rigidbody__AddExplosionForce(v55, 1, 0);
                        if ((unsigned int)v16 >= addr->field_18 - 1 && !ptr->field_5c)
                        {
                            if (ptr->field_50)
                            {
                                if (sub_1231bc8(ptr->field_50, g_1efd010))
                                    ptr3 = Collider__set_enabled();
                                else
                                    sub_f7db7c(sub_f7db74());
                            }
                            else
                            {
                                sub_f7db7c(sub_f7db74());
                            }
                        }
                        i = addr->field_18;
                        v16 += 1;
                    } while ((unsigned int)v16 < i);
                    goto LABEL_1097040;
                }
            }
        }
    }
    else if (!p->field_10)
    {
        p->field_10 = 4294967295;
        if (ptr)
        {
            v9 = sub_f7db70(g_1ef2440);
            WaitForSeconds__ctor(v9, 0);
            p->field_18 = v9;
            ptr4 = &p->field_18;
            sub_f7d8d0(ptr4, v9);
            *((unsigned int *)&ptr4->padding_0[8]) = 1;
            return 1;
        }
    }
    else
    {
        return 0;
    }
LABEL_109708c:
    sub_f7db7c(sub_f7db74());
}
```

## `ExplosiveObject.<Detonate>d__21.get_Current` — RVA `0xc97148`

- Decompiled symbol: `ExplosiveObject_Detonate_d__21_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long ExplosiveObject_Detonate_d__21_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `ExplosiveObject.<Detonate>d__21.Reset` — RVA `0xc97150`

- Decompiled symbol: `ExplosiveObject_Detonate_d__21_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f045b0;

void ExplosiveObject_Detonate_d__21_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f045b0));
}
```

## `ExplosiveObject.<Detonate>d__21.get_Current` — RVA `0xc97188`

- Decompiled symbol: `ExplosiveObject_Detonate_d__21_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long ExplosiveObject_Detonate_d__21_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
