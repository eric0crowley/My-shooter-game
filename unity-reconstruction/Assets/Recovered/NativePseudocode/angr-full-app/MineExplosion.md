# Native pseudocode: MineExplosion

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MineExplosion.ApplyDamage` — RVA `0xc97094`

- Decompiled symbol: `MineExplosion_ApplyDamage`
- Metadata signature: `public void ApplyDamage(float damage) { }`
- Native interval: `180` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MineExplosion_Recovered` matched 3 offsets against `MineExplosion` metadata (confidence 1.00).

```c
typedef struct MineExplosion_Recovered {
    char padding_0[76];
    char isRadiusCollider;
    char padding_4d[11];
    long long myTransform;
    char padding_60[2];
    char detonated;
} MineExplosion_Recovered;

extern long long g_1efd138;
extern char g_1fab489;

struct_0 * MineExplosion_ApplyDamage(struct_0 *ptr)
{
    struct_0 *v0;  // x0
    struct_0 *v1;  // x0
    struct_0 *v2;  // x0
    unsigned long v3;  // x0
    long long v5;  // x0

    v0 = ptr;
    if (!(g_1fab489 & 1))
    {
        v1 = sub_f7d92c(&g_1efd138);
        g_1fab489 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (ptr->field_4c)
        return v2;
    if (ptr->field_62)
        return v2;
    v3 = ptr->field_58;
    ptr->field_62 = 1;
    if (v3)
    {
        v3 = sub_1231e2c(v3, g_1efd138);
        if (v3)
        {
            Collider__set_enabled();
            MonoBehaviour__StartCoroutine(ptr, MineExplosion__Detonate(ptr), 0);
            MineExplosion__DetectDestroyed(ptr);
            v5 = MonoBehaviour__StartCoroutine();
            return MonoBehaviour__StartCoroutine();
        }
    }
    sub_f7db74(v3);
}
```

## `MineExplosion.Start` — RVA `0xc97190`

- Decompiled symbol: `MineExplosion_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `348` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MineExplosion_Recovered` matched 5 offsets against `MineExplosion` metadata (confidence 1.00).

```c
typedef struct struct_1 {
    char padding_0[40];
    long long field_28;
} struct_1;

typedef struct struct_2 {
    char padding_0[136];
    long long field_88;
} struct_2;

typedef struct MineExplosion_Recovered {
    char padding_0[32];
    long long WeaponEffectsComponent;
    char padding_28[32];
    unsigned int radius;
    char isRadiusCollider;
    char padding_4d[11];
    long long myTransform;
    char padding_60[104];
    unsigned int randomSpawnChance;
} MineExplosion_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcf38;
extern long long g_1efd138;
extern long long g_1efebb8;
extern char g_1fab484;

int MineExplosion_Start(struct_3 *ptr)
{
    struct_1 *v0;  // x0
    struct_2 *ptr3;  // x0
    unsigned long v10;  // 4129
    long long v2;  // x1
    struct_3 *p;  // x0
    long long v4;  // x0
    struct_3 *addr;  // x20
    struct_3 *v6;  // x20
    unsigned int v7;  // s0
    unsigned int v8;  // w0
    unsigned int v9;  // s1

    if (!(g_1fab484 & 1))
    {
        sub_f7d92c(&g_1efd138);
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1ef0c58);
        g_1fab484 = 1;
    }
    if (Camera__get_main(0) && (v0 = (struct_1 *)sub_1231bc8(), v0 && v0->field_28 && (ptr3 = (struct_2 *)sub_1249224(v0->field_28, g_1efebb8), ptr3)))
    {
        v2 = ptr3->field_88;
        p = ptr;
        p->field_20 = v2;
        sub_f7d8d0((struct MineExplosion_Recovered *)&p->field_20, v2);
        v4 = Component__get_transform(ptr, 0);
        addr = ptr;
        addr->field_58 = v4;
        v6 = &addr->field_58;
        sub_f7d8d0(v6, v4);
        if (v6->padding_0[12])
        {
LABEL_1097284:
            v8 = Random__get_value(0);
            v9 = ptr->field_c8;
            v10 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v7, v9)) >> 5 & 3 | (unsigned long long)(CmpF(v7, v9) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7, v9)) >> 5 & 3 | (unsigned long long)(CmpF(v7, v9) & 1)) & ((unsigned long long)(char)(CmpF(v7, v9)) >> 5 & 3 | (unsigned long long)(CmpF(v7, v9) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v10)
                return v8;
            if (*((long long *)&v6->padding_0[0]))
            {
                Component__get_gameObject(*((long long *)&v6->padding_0[0]), 0);
                if (g_1ef0c58->field_e0)
                    return Object__Destroy();
                sub_f7da5c(g_1ef0c58);
                return Object__Destroy();
            }
        }
        else if (*((long long *)&v6->padding_0[0]) && sub_1231e2c(*((long long *)&v6->padding_0[0]), g_1efd138))
        {
            SphereCollider__get_radius();
            ptr->field_48 = v7;
            MineExplosion__AlignToGround();
            goto LABEL_1097284;
        }
    }
    sub_f7db74();
}
```

## `MineExplosion.AlignToGround` — RVA `0xc972ec`

- Decompiled symbol: `MineExplosion_AlignToGround`
- Metadata signature: `private void AlignToGround() { }`
- Native interval: `428` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[88];
    long long field_58;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0e48;
extern long long g_1ef22e8;
extern char g_1fab32c;
extern char g_1fab485;

long long MineExplosion_AlignToGround(struct_1 *ptr, unsigned long a1)
{
    long long v0;  // x0
    struct_1 *v1;  // x20
    unsigned int v2;  // w0
    long long v3;  // x0
    long long v4;  // x21
    unsigned long long v5;  // x0

    if (!(g_1fab485 & 1))
    {
        sub_f7d92c(&g_1ef0e48);
        g_1fab485 = 1;
    }
    v0 = ptr->field_58;
    if (v0)
    {
        Transform__get_position(v0, 0);
        v0 = Component__get_transform(ptr, 0);
        if (v0)
        {
            Transform__get_up();
            v1 = &ptr[1].padding_0[48];
            v2 = LayerMask__get_value(&ptr->padding_0[84], 0);
            if (!g_1ef0e48->field_e0)
                sub_f7da5c(g_1ef0e48);
            v3 = Physics__Raycast(v1, v2, 0);
            if (!((char)v3 & 1))
                return v3;
            v4 = ptr->field_58;
            if (!g_1fab32c)
            {
                sub_f7d92c(&g_1ef22e8);
                g_1fab32c = 1;
            }
            RaycastHit__get_normal(v1, 0);
            v0 = Quaternion__FromToRotation(0);
            if (v4)
            {
                Transform__set_rotation(v4, 0);
                v0 = RaycastHit__get_point(v1, 0);
                if (ptr->field_58)
                {
                    v5 = Transform__set_position();
                    return Transform__set_position();
                }
            }
        }
    }
    sub_f7db74(v0);
}
```

## `MineExplosion.OnTriggerEnter` — RVA `0xc97498`

- Decompiled symbol: `MineExplosion_OnTriggerEnter`
- Metadata signature: `private void OnTriggerEnter(Collider col) { }`
- Native interval: `496` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MineExplosion_Recovered` matched 3 offsets against `MineExplosion` metadata (confidence 1.00).

```c
typedef struct MineExplosion_Recovered {
    char padding_0[76];
    char isRadiusCollider;
    char padding_4d[11];
    long long myTransform;
    char padding_60[2];
    char detonated;
} MineExplosion_Recovered;

typedef struct struct_1 {
    char padding_0[97];
    char field_61;
} struct_1;

typedef struct struct_2 {
    char padding_0[98];
    char field_62;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efd020;
extern long long g_1efd0a0;
extern long long g_1f09a90;
extern char g_1fab486;

struct_3 * MineExplosion_OnTriggerEnter(struct_3 *ptr, long long a1)
{
    struct_3 *v0;  // x0
    struct_3 *v1;  // x0
    struct_3 *v2;  // x0
    struct_3 *v3;  // x0
    struct_3 *v4;  // x0
    long long v5;  // x0
    unsigned long v6;  // x0
    struct_1 *p;  // x0
    struct_2 *addr;  // x0
    long long v9;  // x0

    v0 = ptr;
    if (!(g_1fab486 & 1))
    {
        sub_f7d92c(&g_1efd020);
        sub_f7d92c(&g_1efd0a0);
        sub_f7d92c(&g_1ef0c58);
        v1 = sub_f7d92c(&g_1f09a90);
        g_1fab486 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (!ptr->field_4c)
        return v2;
    if (a1)
    {
        v3 = Collider__get_isTrigger(a1, 0);
        if (((char)v3 & 1))
            return v3;
        if (Component__get_gameObject(a1, 0))
        {
            v4 = GameObject__get_layer();
            if ((unsigned int)v4 == 11)
            {
LABEL_1097588:
                if (ptr->field_62)
                    return v4;
                v6 = ptr->field_58;
                ptr->field_62 = 1;
                if (v6 && Transform__get_parent(v6, 0) && Component__get_transform())
                {
                    p = sub_1231bc8();
                    if (p)
                    {
                        p->field_61 = 1;
                        if (ptr->field_58 && Transform__get_parent(ptr->field_58, 0) && Component__get_transform())
                        {
                            addr = sub_1231bc8();
                            if (addr)
                            {
                                addr->field_62 = 1;
                                if (ptr->field_58 && sub_1231bc8(ptr->field_58, g_1efd0a0))
                                {
                                    Collider__set_enabled();
                                    if (ptr->field_58 && Transform__get_parent(ptr->field_58, 0) && Component__get_transform() && sub_1231bc8())
                                    {
                                        v9 = MonoBehaviour__StartCoroutine();
                                        return MonoBehaviour__StartCoroutine();
                                    }
                                }
                            }
                        }
                    }
                }
            }
            else if (Component__get_gameObject(a1, 0))
            {
                v4 = GameObject__get_layer();
                if ((unsigned int)v4 != 13)
                {
                    v5 = Collider__get_attachedRigidbody(a1, 0);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    v4 = Object__op_Inequality(v5, 0, 0);
                    if (!((char)v4 & 1))
                        return v4;
                }
                goto LABEL_1097588;
            }
        }
    }
    sub_f7db74();
}
```

## `MineExplosion.DetectDestroyed` — RVA `0xc97688`

- Decompiled symbol: `MineExplosion_DetectDestroyed`
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

extern long long g_1ef34b8;
extern char g_1fab487;

struct_0 * MineExplosion_DetectDestroyed(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab487 & 1))
    {
        sub_f7d92c(&g_1ef34b8);
        g_1fab487 = 1;
    }
    v0 = sub_f7db70(g_1ef34b8);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `MineExplosion.<DetectDestroyed>d__22.ctor` — RVA `0xc976f4`

- Decompiled symbol: `MineExplosion_DetectDestroyed_d__22_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void MineExplosion_DetectDestroyed_d__22_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `MineExplosion.Detonate` — RVA `0xc9771c`

- Decompiled symbol: `MineExplosion_Detonate`
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

extern long long g_1ef34c0;
extern char g_1fab488;

struct_0 * MineExplosion_Detonate(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab488 & 1))
    {
        sub_f7d92c(&g_1ef34c0);
        g_1fab488 = 1;
    }
    v0 = sub_f7db70(g_1ef34c0);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `MineExplosion.<Detonate>d__23.ctor` — RVA `0xc97788`

- Decompiled symbol: `MineExplosion_Detonate_d__23_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void MineExplosion_Detonate_d__23_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `MineExplosion.ctor` — RVA `0xc977b0`

- Decompiled symbol: `MineExplosion_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `36` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MineExplosion_Recovered` matched 3 offsets against `MineExplosion` metadata (confidence 1.00).

```c
typedef struct MineExplosion_Recovered {
    char padding_0[40];
    unsigned long long explosionDamage;
    unsigned int blastForce;
    char padding_34[148];
    unsigned int randomSpawnChance;
} MineExplosion_Recovered;

long long MineExplosion_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_30 = 0x41700000;
    ptr->field_28 = 0x3e4ccccd43480000;
    ptr->field_c8 = 0x3f800000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```

## `MineExplosion.<DetectDestroyed>d__22.Dispose` — RVA `0xc977d4`

- Decompiled symbol: `MineExplosion_DetectDestroyed_d__22_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long MineExplosion_DetectDestroyed_d__22_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `MineExplosion.<DetectDestroyed>d__22.MoveNext` — RVA `0xc977d8`

- Decompiled symbol: `MineExplosion_DetectDestroyed_d__22_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `736` bytes
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
    char padding_0[76];
    char field_4c;
    char padding_4d[11];
    long long field_58;
    char field_60;
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
extern long long g_1efcf18;
extern long long g_1efedb0;
extern long long g_1efedb8;
extern char g_1fab48a;

unsigned int MineExplosion_DetectDestroyed_d__22_MoveNext(struct_4 *ptr)
{
    struct_3 *v0;  // x19
    long long v1;  // x19
    struct_5 *addr;  // x20
    unsigned int v11;  // w22
    struct_6 *ptr4;  // x21
    long long v13;  // x0
    struct_4 *ptr5;  // x20
    struct_5 *p;  // x0
    unsigned int v4;  // w8
    struct_5 *ptr3;  // x20
    unsigned int v6;  // w22
    unsigned long long v7[10];  // x24
    unsigned long v8;  // x0
    unsigned int v9;  // w8

    if (!(g_1fab48a & 1))
    {
        sub_f7d92c("s.");
        sub_f7d92c(&g_1efcf18);
        sub_f7d92c(&g_1efedb0);
        sub_f7d92c(&g_1efedb8);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef2440);
        sub_f7d92c("s%");
        g_1fab48a = 1;
    }
    if (1 < ptr->field_10)
    {
LABEL_1097a98:
        return 0;
    }
    v0 = ptr->field_20;
    ptr->field_10 = 4294967295;
    if (v0)
    {
        if (v0->field_4c || !v0->field_60)
        {
LABEL_1097878:
            v1 = sub_f7db70(g_1ef2440);
            WaitForSeconds__ctor(v1, 0);
            ptr->field_18 = v1;
            ptr5 = &ptr->field_18;
            sub_f7d8d0(ptr5, v1);
            *((unsigned int *)&ptr5->padding_0[8]) = 1;
            return 1;
        }
        if (sub_1231bc8(v0, g_1efcf18))
        {
            if ((AudioSource__get_isPlaying() & 1))
                goto LABEL_1097878;
            if (Component__get_gameObject(v0, 0) && (p = (struct_5 *)(unsigned long long)sub_1249ec4(), p))
            {
                v4 = p->field_18;
                ptr3 = p;
                if (p->field_18 >= 1)
                {
                    v6 = 0;
                    do
                    {
                        if (v4 <= v6)
                            sub_f7db7c(p);
                        v7 = *((long long *)&ptr3[1].padding_0[4 + 8 * v6]);
                        if (!v7)
                            sub_f7db7c(sub_f7db74());
                        if (!g_1eeea08->field_b8->field_0)
                            sub_f7db7c(sub_f7db74());
                        v8 = Component__get_transform(g_1eeea08->field_b8->field_0, 0);
                        if (!v7[9])
                            sub_f7db7c(sub_f7db74());
                        Transform__set_parent(v7[9], v8, 0);
                        if (!v7[8])
                            goto LABEL_1097ab0;
                    } while ((p = (struct_5 *)GameObject__SetActive(v7[8], 0, 0), v4 = (unsigned int)ptr3->field_18, v6 += 1, v6 < v4));
                }
                else if (Component__get_gameObject(v0, 0) && (p = (struct_5 *)(unsigned long long)sub_1249ec4(), p))
                {
                    v9 = p->field_18;
                    addr = p;
                    if (v9 >= 1)
                    {
                        v11 = 0;
                        do
                        {
                            if (v9 <= v11)
                                sub_f7db7c(p);
                            ptr4 = *((long long *)&addr[1].padding_0[4 + 8 * v11]);
                            if (!ptr4)
                                sub_f7db7c(sub_f7db74());
                            if (!Component__get_transform(ptr4, 0))
                                sub_f7db7c(sub_f7db74());
                            Transform__set_parent();
                            if (!ptr4->field_20)
                                sub_f7db7c(sub_f7db74());
                            Rigidbody__set_isKinematic(ptr4->field_20, 0, 0);
                            if (!ptr4->field_78 || !((Collider__set_isTrigger(ptr4->field_78, 0, 0), Component__get_gameObject(ptr4, 0))))
                                goto LABEL_1097ab0;
                        } while ((p = (struct_5 *)(unsigned long long)GameObject__set_tag(), ptr4->field_31 = 1, v9 = (unsigned int)addr->field_18, v11 += 1, v11 < v9));
                    }
                    else if (v0->field_58)
                    {
                        v13 = Component__get_gameObject(v0->field_58, 0);
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        Object__Destroy(v13, 0);
                        goto LABEL_1097a98;
                    }
                }
            }
        }
    }
LABEL_1097ab0:
    sub_f7db7c(sub_f7db74());
}
```

## `MineExplosion.<DetectDestroyed>d__22.get_Current` — RVA `0xc97ab8`

- Decompiled symbol: `MineExplosion_DetectDestroyed_d__22_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long MineExplosion_DetectDestroyed_d__22_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `MineExplosion.<DetectDestroyed>d__22.Reset` — RVA `0xc97ac0`

- Decompiled symbol: `MineExplosion_DetectDestroyed_d__22_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f048f0;

void MineExplosion_DetectDestroyed_d__22_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f048f0));
}
```

## `MineExplosion.<DetectDestroyed>d__22.get_Current` — RVA `0xc97af8`

- Decompiled symbol: `MineExplosion_DetectDestroyed_d__22_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long MineExplosion_DetectDestroyed_d__22_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `MineExplosion.<Detonate>d__23.Dispose` — RVA `0xc97b00`

- Decompiled symbol: `MineExplosion_Detonate_d__23_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long MineExplosion_Detonate_d__23_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `MineExplosion.<Detonate>d__23.MoveNext` — RVA `0xc97b04`

- Decompiled symbol: `MineExplosion_Detonate_d__23_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `3112` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[32];
    unsigned long long field_20;
    char padding_28[24];
    unsigned long long field_40;
    char padding_48[8];
    unsigned int field_50;
    char padding_54[4];
    void* field_58;
    char field_60;
    char field_61;
    char padding_62[2];
    char field_64;
} struct_3;

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
extern long long g_1efcf18;
extern long long g_1efcf20;
extern long long g_1efcf70;
extern long long g_1efd018;
extern long long g_1efd080;
extern long long g_1efeb30;
extern long long g_1efeb48;
extern long long g_1efeb90;
extern long long g_1efebb0;
extern long long g_1efebb8;
extern long long g_1efec38;
extern long long g_1efec58;
extern char g_1fab2c9;
extern char g_1fab48b;

unsigned int MineExplosion_Detonate_d__23_MoveNext(void* addr)
{
    void* v2;  // x0
    void* v3;  // x0
    void* ptr4;  // x20
    unsigned int v13;  // w0
    unsigned int v14;  // w8
    void* ptr3;  // x20
    unsigned long long idx;  // x22
    unsigned long v17;  // x28
    void* ptr;  // x21
    long long v19;  // x19
    unsigned int v20;  // w0
    long long v21;  // x0
    void* ptr5;  // x0
    long long v22;  // x19
    long long v23;  // x0
    long long v24;  // x0
    long long v25;  // x0
    long long v26;  // x0
    long long v27;  // x0
    long long v28;  // x0
    long long v29;  // x24
    long long v30;  // x0
    long long v31;  // x24
    unsigned int flag;  // w8
    long long v32;  // x0
    long long v33;  // x24
    struct_3 *p;  // x23
    long long v7;  // x19
    void* ptr6;  // x20
    long long v9;  // x21
    unsigned int v10;  // w8
    long long v11;  // x19
    char *v0;  // [bp-0x60]
    char v1;  // [bp+0x0]

    v0 = &v1;
    v2 = addr;
    if (!(g_1fab48b & 1))
    {
        sub_f7d92c(&g_1efcf18);
        sub_f7d92c(&g_1efcf20);
        sub_f7d92c(&g_1efcf70);
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
        v3 = sub_f7d92c(&g_1ef2440);
        g_1fab48b = 1;
        v2 = v3;
    }
    flag = (int)addr[16];
    p = (long long)addr[32];
    if (flag == 2)
    {
        *((unsigned int *)&addr[16]) = 4294967295;
        if (p)
            goto LABEL_1097dc4;
    }
    else if (flag != 1)
    {
        if (flag)
            return 0;
        *((unsigned int *)&addr[16]) = 4294967295;
        if (p)
        {
            if (!p->field_61)
                goto LABEL_1097ce8;
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (!((char)Object__op_Implicit(p->field_40, 0) & 1))
            {
LABEL_1097c8c:
                v7 = sub_f7db70(g_1ef2440);
                WaitForSeconds__ctor(v7, 0);
                *((long long *)&addr[24]) = v7;
                ptr6 = addr + 24;
                sub_f7d8d0(ptr6, v7);
                *((unsigned int *)&ptr6[8]) = 1;
                return 1;
            }
            ptr5 = sub_1231bc8(p, g_1efcf18);
            if (ptr5)
            {
                AudioSource__set_clip();
                ptr5 = sub_1231bc8(p, g_1efcf18);
                if (ptr5)
                {
                    AudioSource__Play();
                    goto LABEL_1097c8c;
                }
            }
        }
    }
    else
    {
        *((unsigned int *)&addr[16]) = 4294967295;
        if (p)
        {
LABEL_1097ce8:
            ptr5 = p->field_58;
            if (ptr5 && (ptr5 = (void*)(unsigned long long)Transform__get_position(ptr5, 0), p->field_20 && (WeaponEffects__ExplosionEffect(p->field_20), ptr5 = p->field_58, ptr5 && (ptr5 = (void*)sub_1231bc8(ptr5, g_1efd018), ptr5))))
            {
                Renderer__set_enabled();
                ptr5 = sub_1231bc8(p, g_1efcf18);
                if (ptr5)
                {
                    AudioSource__set_clip();
                    v9 = sub_1231bc8(p, g_1efcf18);
                    Time__get_timeScale(0);
                    Time__get_timeScale(0);
                    ptr5 = Random__Range(0);
                    if (v9)
                    {
                        AudioSource__set_pitch(v9, 0);
                        ptr5 = sub_1231bc8(p, g_1efcf18);
                        if (ptr5)
                        {
                            AudioSource__Play();
                            v10 = p->field_61;
                            p->field_60 = 1;
                            if (!v10)
                            {
                                v11 = sub_f7db70(g_1ef2440);
                                WaitForSeconds__ctor(v11, 0);
                                *((long long *)&addr[24]) = v11;
                                ptr4 = addr + 24;
                                sub_f7d8d0(ptr4, v11);
                                *((unsigned int *)&ptr4[8]) = 2;
                                return 1;
                            }
LABEL_1097dc4:
                            ptr5 = p->field_58;
                            if (ptr5)
                            {
                                Transform__get_position(ptr5, 0);
                                v13 = LayerMask__op_Implicit(p->field_50, 0);
                                if (!g_1ef0e48->field_e0)
                                    sub_f7da5c(g_1ef0e48);
                                ptr5 = Physics__OverlapSphere(v13, 0);
                                if (ptr5)
                                {
                                    v14 = (int)ptr5[24];
                                    ptr3 = ptr5;
                                    if (v14 < 1)
                                        return 0;
                                    idx = 0;
                                    v17 = &p->field_64;
                                    ptr = ptr3 + 32;
                                    while (true)
                                    {
                                        if (v14 <= (unsigned int)idx)
                                            sub_f7db7c(ptr5);
                                        ptr5 = *((long long *)((char *)ptr + 8 * idx));
                                        if (!ptr5)
                                            break;
                                        v19 = Component__get_transform(ptr5, 0);
                                        if (!g_1ef0c58->field_e0)
                                            sub_f7da5c(g_1ef0c58);
                                        ptr5 = Object__op_Inequality(v19, p->field_58, 0);
                                        if (((char)ptr5 & 1))
                                        {
                                            if (!v19 || !((Transform__get_position(v19, 0), ptr5 = p->field_58, ptr5)))
                                                break;
                                            Transform__get_position(ptr5, 0);
                                            v20 = LayerMask__op_Implicit(p->field_50, 0);
                                            if (!g_1ef0e48->field_e0)
                                                sub_f7da5c(g_1ef0e48);
                                            ptr5 = Physics__Linecast(v17, v20, 0);
                                            if (((char)ptr5 & 1))
                                            {
                                                ptr5 = RaycastHit__get_collider(v17, 0);
                                                if (!p->field_58)
                                                    break;
                                                v21 = sub_1231bc8(p->field_58, g_1efcf70);
                                                if (!g_1ef0c58->field_e0)
                                                    sub_f7da5c(g_1ef0c58);
                                                ptr5 = Object__op_Equality(ptr5, v21, 0);
                                                ptr = ptr;
                                                ptr3 = ptr3;
                                                p = p;
                                                if (((char)ptr5 & 1))
                                                {
                                                    if ((int)ptr3[24] <= (unsigned int)idx)
                                                        sub_f7db7c(ptr5);
                                                    ptr5 = *((long long *)((char *)ptr + 8 * idx));
                                                    if (!ptr5 || !((v22 = v19, ptr5 = (void*)sub_1231bc8(ptr5, g_1efcf70), sub_1231bc8(ptr5, g_1efcf70) && (ptr5 = (void*)Component__get_gameObject(), Component__get_gameObject()))))
                                                        break;
                                                    ptr5 = GameObject__get_layer();
                                                    if ((unsigned int)ptr5 == 13)
                                                    {
                                                        if ((int)ptr3[24] <= (unsigned int)idx)
                                                            sub_f7db7c(ptr5);
                                                        ptr5 = *((long long *)((char *)ptr + 8 * idx));
                                                        if (!ptr5 || !((ptr5 = (void*)sub_1231bc8(ptr5, g_1efcf70), sub_1231bc8(ptr5, g_1efcf70) && (ptr5 = (void*)Component__get_gameObject(), Component__get_gameObject()))))
                                                            break;
                                                        v28 = sub_1249224();
                                                        if (!g_1ef0c58->field_e0)
                                                            sub_f7da5c(g_1ef0c58);
                                                        ptr5 = Object__op_Implicit(v28, 0);
                                                        if (((char)ptr5 & 1))
                                                        {
                                                            if ((int)ptr3[24] <= (unsigned int)idx)
                                                                sub_f7db7c(ptr5);
                                                            ptr5 = *((long long *)((char *)ptr + 8 * idx));
                                                            if (!ptr5 || !((ptr5 = (void*)sub_1231bc8(ptr5, g_1efcf70), sub_1231bc8(ptr5, g_1efcf70) && (ptr5 = (void*)Component__get_gameObject(), Component__get_gameObject()))))
                                                                break;
                                                            v29 = sub_1249224();
                                                            if (!g_1fab2c9)
                                                            {
                                                                sub_f7d92c(&g_1ef22e8);
                                                                g_1fab2c9 = 1;
                                                            }
                                                            ptr5 = p->field_58;
                                                            if (!ptr5 || !((ptr5 = (void*)(unsigned long long)Transform__get_position(ptr5, 0), v29)))
                                                                break;
                                                            ptr5 = CharacterDamage__ApplyDamage(v29, 0, 0, 1, 0, 0);
                                                        }
                                                        if ((int)ptr3[24] <= (unsigned int)idx)
                                                            sub_f7db7c(ptr5);
                                                        ptr5 = *((long long *)((char *)ptr + 8 * idx));
                                                        if (!ptr5 || !((ptr5 = (void*)sub_1231bc8(ptr5, g_1efcf70), sub_1231bc8(ptr5, g_1efcf70) && (ptr5 = (void*)Component__get_gameObject(), Component__get_gameObject()))))
                                                            break;
                                                        v30 = sub_1249224();
                                                        if (!g_1ef0c58->field_e0)
                                                            sub_f7da5c(g_1ef0c58);
                                                        ptr5 = Object__op_Implicit(v30, 0);
                                                        if (((char)ptr5 & 1))
                                                        {
                                                            if ((int)ptr3[24] <= (unsigned int)idx)
                                                                sub_f7db7c(ptr5);
                                                            ptr5 = *((long long *)((char *)ptr + 8 * idx));
                                                            if (!ptr5 || !((ptr5 = (void*)sub_1231bc8(ptr5, g_1efcf70), sub_1231bc8(ptr5, g_1efcf70) && (ptr5 = (void*)Component__get_gameObject(), Component__get_gameObject()))))
                                                                break;
                                                            v31 = sub_1249224();
                                                            if (!g_1fab2c9)
                                                            {
                                                                sub_f7d92c(&g_1ef22e8);
                                                                g_1fab2c9 = 1;
                                                            }
                                                            ptr5 = p->field_58;
                                                            if (!ptr5 || !((ptr5 = (void*)(unsigned long long)Transform__get_position(ptr5, 0), v31)))
                                                                break;
                                                            LocationDamage__ApplyDamage(v31, 0, 0, 1, 0);
                                                        }
                                                    }
                                                    else if ((unsigned int)ptr5 == 11)
                                                    {
                                                        if ((int)ptr3[24] <= (unsigned int)idx)
                                                            sub_f7db7c(ptr5);
                                                        ptr5 = *((long long *)((char *)ptr + 8 * idx));
                                                        if (!ptr5 || !((ptr5 = (void*)sub_1231bc8(ptr5, g_1efcf70), sub_1231bc8(ptr5, g_1efcf70) && (ptr5 = (void*)Component__get_gameObject(), Component__get_gameObject()))))
                                                            break;
                                                        v27 = sub_1249224();
                                                        if (!g_1ef0c58->field_e0)
                                                            sub_f7da5c(g_1ef0c58);
                                                        ptr5 = Object__op_Implicit(v27, 0);
                                                        if (((char)ptr5 & 1))
                                                        {
                                                            if ((int)ptr3[24] <= (unsigned int)idx)
                                                                sub_f7db7c(ptr5);
                                                            ptr5 = *((long long *)((char *)ptr + 8 * idx));
                                                            if (!ptr5 || !((ptr5 = (void*)sub_1231bc8(ptr5, g_1efcf70), sub_1231bc8(ptr5, g_1efcf70) && (ptr5 = (void*)Component__get_gameObject(), Component__get_gameObject() && (ptr5 = (void*)sub_1249224(), sub_1249224())))))
                                                                break;
                                                            FPSPlayer__ApplyDamage();
                                                        }
                                                    }
                                                    else if (!(unsigned int)ptr5)
                                                    {
                                                        if ((int)ptr3[24] <= (unsigned int)idx)
                                                            sub_f7db7c(ptr5);
                                                        ptr5 = *((long long *)((char *)ptr + 8 * idx));
                                                        if (!ptr5 || !((ptr5 = (void*)sub_1231bc8(ptr5, g_1efcf70), sub_1231bc8(ptr5, g_1efcf70) && (ptr5 = (void*)Component__get_gameObject(), Component__get_gameObject()))))
                                                            break;
                                                        v23 = sub_1249224();
                                                        if (!g_1ef0c58->field_e0)
                                                            sub_f7da5c(g_1ef0c58);
                                                        ptr5 = Object__op_Implicit(v23, 0);
                                                        if ((int)ptr3[24] <= (unsigned int)idx)
                                                            sub_f7db7c(ptr5);
                                                        ptr5 = *((long long *)((char *)ptr + 8 * idx));
                                                        if (!ptr5 || !((ptr5 = (void*)sub_1231bc8(ptr5, g_1efcf70), sub_1231bc8(ptr5, g_1efcf70) && (ptr5 = (void*)Component__get_gameObject(), Component__get_gameObject()))))
                                                            break;
                                                        if (((char)ptr5 & 1))
                                                        {
                                                            ptr5 = sub_1249224();
                                                            if (!ptr5)
                                                                break;
                                                            BreakableObject__ApplyDamage(ptr5);
                                                        }
                                                        else
                                                        {
                                                            v24 = sub_1249224();
                                                            if (!g_1ef0c58->field_e0)
                                                                sub_f7da5c(g_1ef0c58);
                                                            ptr5 = Object__op_Implicit(v24, 0);
                                                            if ((int)ptr3[24] <= (unsigned int)idx)
                                                                sub_f7db7c(ptr5);
                                                            ptr5 = *((long long *)((char *)ptr + 8 * idx));
                                                            if (!ptr5 || !((ptr5 = (void*)sub_1231bc8(ptr5, g_1efcf70), sub_1231bc8(ptr5, g_1efcf70) && (ptr5 = (void*)Component__get_gameObject(), Component__get_gameObject()))))
                                                                break;
                                                            if (((char)ptr5 & 1))
                                                            {
                                                                ptr5 = sub_1249224();
                                                                if (ptr5)
                                                                    ExplosiveObject__ApplyDamage(ptr5);
                                                                break;
                                                            }
                                                            else
                                                            {
                                                                v25 = sub_1249224();
                                                                if (!g_1ef0c58->field_e0)
                                                                    sub_f7da5c(g_1ef0c58);
                                                                ptr5 = Object__op_Implicit(v25, 0);
                                                                if ((int)ptr3[24] <= (unsigned int)idx)
                                                                    sub_f7db7c(ptr5);
                                                                ptr5 = *((long long *)((char *)ptr + 8 * idx));
                                                                if (!ptr5 || !((ptr5 = (void*)sub_1231bc8(ptr5, g_1efcf70), sub_1231bc8(ptr5, g_1efcf70) && (ptr5 = (void*)Component__get_gameObject(), Component__get_gameObject()))))
                                                                    break;
                                                                if (((char)ptr5 & 1))
                                                                {
                                                                    ptr5 = sub_1249224();
                                                                    if (!ptr5)
                                                                        break;
                                                                    MineExplosion__ApplyDamage(ptr5);
                                                                }
                                                                else
                                                                {
                                                                    v26 = sub_1249224();
                                                                    if (!g_1ef0c58->field_e0)
                                                                        sub_f7da5c(g_1ef0c58);
                                                                    ptr5 = Object__op_Implicit(v26, 0);
                                                                    if (((char)ptr5 & 1))
                                                                    {
                                                                        if ((int)ptr3[24] <= (unsigned int)idx)
                                                                            sub_f7db7c(ptr5);
                                                                        ptr5 = *((long long *)((char *)ptr + 8 * idx));
                                                                        if (!ptr5 || !((ptr5 = (void*)sub_1231bc8(ptr5, g_1efcf70), sub_1231bc8(ptr5, g_1efcf70) && (ptr5 = (void*)Component__get_gameObject(), Component__get_gameObject() && (ptr5 = (void*)sub_1249224(), ptr5)))))
                                                                            break;
                                                                        AppleFall__ApplyDamage(ptr5);
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                    v32 = sub_1231bc8(v22, g_1efd080);
                                                    if (!g_1ef0c58->field_e0)
                                                        sub_f7da5c(g_1ef0c58);
                                                    ptr5 = Object__op_Implicit(v32, 0);
                                                    if (((char)ptr5 & 1))
                                                    {
                                                        v33 = sub_1231bc8(v22, g_1efd080);
                                                        ptr5 = sub_1231bc8(v22, g_1efd080);
                                                        if (!ptr5 || !((Rigidbody__get_mass(), ptr5 = p->field_58, ptr5 && (ptr5 = (void*)(unsigned long long)Transform__get_position(ptr5, 0), v33))))
                                                            break;
                                                        ptr5 = Rigidbody__AddExplosionForce(v33, 1, 0);
                                                    }
                                                }
                                            }
                                        }
                                        if ((unsigned int)idx >= (int)ptr3[24] - 1)
                                        {
                                            ptr5 = p->field_58;
                                            if (!ptr5 || !((ptr5 = (void*)sub_1231bc8(ptr5, g_1efcf20), sub_1231bc8(ptr5, g_1efcf20))))
                                                break;
                                            ptr5 = Collider__set_enabled();
                                        }
                                        v14 = (int)ptr3[24];
                                        idx += 1;
                                        if ((unsigned int)idx >= v14)
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
    sub_f7db7c(sub_f7db74(ptr5));
}
```

## `MineExplosion.<Detonate>d__23.get_Current` — RVA `0xc9872c`

- Decompiled symbol: `MineExplosion_Detonate_d__23_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long MineExplosion_Detonate_d__23_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `MineExplosion.<Detonate>d__23.Reset` — RVA `0xc98734`

- Decompiled symbol: `MineExplosion_Detonate_d__23_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f048f8;

void MineExplosion_Detonate_d__23_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f048f8));
}
```

## `MineExplosion.<Detonate>d__23.get_Current` — RVA `0xc9876c`

- Decompiled symbol: `MineExplosion_Detonate_d__23_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long MineExplosion_Detonate_d__23_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
