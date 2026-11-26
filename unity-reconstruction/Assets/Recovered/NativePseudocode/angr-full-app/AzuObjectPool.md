# Native pseudocode: AzuObjectPool

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AzuObjectPool.SpawnPooledObj` — RVA `0xc8d3fc`

- Decompiled symbol: `AzuObjectPool_SpawnPooledObj`
- Metadata signature: `public GameObject SpawnPooledObj(int objRegIndex, Vector3 spawnPosition, Quaternion spawnRotation) { }`
- Native interval: `472` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[28];
    unsigned int field_1c;
    char padding_20[8];
    struct struct_3 *field_28;
} struct_4;

typedef struct struct_2 {
    char padding_0[48];
    struct struct_1 *field_30;
} struct_2;

typedef struct struct_1 {
    char padding_0[28];
    unsigned int field_1c;
    char padding_20[8];
    struct struct_0 *field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

extern long long g_1ef7b68;
extern long long g_1ef7b70;
extern long long g_1ef8168;
extern char g_1fab495;

struct_4 * AzuObjectPool_SpawnPooledObj(struct_2 *ptr, unsigned int a1)
{
    struct_1 *v0;  // x0
    struct_4 *v1;  // x0
    struct_4 *v2;  // x0
    struct_1 *v3;  // x21
    struct_4 *v4;  // x0
    struct_4 *v5;  // x0
    struct_1 *v6;  // x0
    struct_4 *p;  // x0
    unsigned int v8;  // w8

    if (!(g_1fab495 & 1))
    {
        sub_f7d92c(&g_1ef7b68);
        sub_f7d92c(&g_1ef8168);
        sub_f7d92c(&g_1ef7b70);
        g_1fab495 = 1;
    }
    v0 = ptr->field_30;
    if (v0)
    {
        v1 = sub_14a30c0(v0, a1, g_1ef8168);
        v0 = v1;
        if (v0)
        {
            v0 = v1;
            if (ptr->field_30)
            {
                v2 = sub_14a30c0(ptr->field_30, a1, g_1ef8168);
                v0 = v2;
                if (v0)
                {
                    v0 = v2;
                    if (v1->field_28)
                    {
                        v0 = sub_14a30c0(v1->field_28, v2->field_1c, g_1ef7b70);
                        if (v0)
                        {
                            v3 = v0;
                            GameObject__SetActive();
                            v0 = GameObject__get_transform(v3, 0);
                            if (v0)
                            {
                                Transform__set_position();
                                v0 = GameObject__get_transform(v3, 0);
                                if (v0)
                                {
                                    Transform__set_rotation();
                                    v0 = ptr->field_30;
                                    if (v0)
                                    {
                                        v4 = sub_14a30c0(v0, a1, g_1ef8168);
                                        v0 = v4;
                                        if (v0)
                                        {
                                            v0 = v4;
                                            if (ptr->field_30)
                                            {
                                                v5 = sub_14a30c0(ptr->field_30, a1, g_1ef8168);
                                                v0 = v5;
                                                if (v0)
                                                {
                                                    v0 = v5;
                                                    if (v0->field_28)
                                                    {
                                                        v6 = ptr->field_30;
                                                        v0 = v6;
                                                        if (v0)
                                                        {
                                                            p = sub_14a30c0(v6, a1, g_1ef8168);
                                                            v0 = p;
                                                            if (v0)
                                                            {
                                                                if (v4->field_1c == v5->field_28->field_18 - 1)
                                                                    v8 = 0;
                                                                else
                                                                    v8 = p->field_1c + 1;
                                                                p->field_1c = v8;
                                                                return v3;
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
    sub_f7db74(v0);
}
```

## `AzuObjectPool.RecyclePooledObj` — RVA `0xc931ec`

- Decompiled symbol: `AzuObjectPool_RecyclePooledObj`
- Metadata signature: `public GameObject RecyclePooledObj(int objRegIndex, GameObject obj) { }`
- Native interval: `272` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[40];
    struct struct_2 *field_28;
} struct_2;

typedef struct struct_1 {
    char padding_0[48];
    struct struct_0 *field_30;
} struct_1;

typedef struct struct_0 {
    char padding_0[40];
    struct struct_0 *field_28;
} struct_0;

extern long long g_1ef7b58;
extern long long g_1ef7b70;
extern long long g_1ef8168;
extern char g_1fab496;

struct_2 * AzuObjectPool_RecyclePooledObj(struct_1 *ptr, unsigned int a1, long long a2)
{
    struct_0 *v0;  // x0
    struct_2 *v1;  // x0
    struct_2 *p;  // x0
    struct_2 *v3;  // x0
    struct_2 *v4;  // x0
    struct_2 *v5;  // x0

    if (!(g_1fab496 & 1))
    {
        sub_f7d92c(&g_1ef7b58);
        sub_f7d92c(&g_1ef8168);
        sub_f7d92c(&g_1ef7b70);
        g_1fab496 = 1;
    }
    v0 = ptr->field_30;
    if (v0)
    {
        v1 = sub_14a30c0(v0, a1, g_1ef8168);
        v0 = v1;
        if (v0)
        {
            v0 = v1;
            if (ptr->field_30)
            {
                p = sub_14a30c0(ptr->field_30, a1, g_1ef8168);
                v0 = p;
                if (v0)
                {
                    v3 = p->field_28;
                    v0 = v3;
                    if (v0)
                    {
                        v4 = sub_14a3dc8(v3, a2, g_1ef7b58);
                        v0 = v4;
                        if (v1->field_28)
                        {
                            v5 = sub_14a30c0(v1->field_28, v4 & 4294967295, g_1ef7b70);
                            v0 = v5;
                            if (v0)
                            {
                                v0 = GameObject__get_transform();
                                if (v0)
                                {
                                    Transform__set_parent();
                                    GameObject__SetActive(v5, 0, 0);
                                    return v5;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74(v0);
}
```

## `AzuObjectPool.Awake` — RVA `0xc9908c`

- Decompiled symbol: `AzuObjectPool_Awake`
- Metadata signature: `private void Awake() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
extern char g_1fab493;

void AzuObjectPool_Awake(unsigned long a0)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab493 & 1))
    {
        sub_f7d92c("s.");
        g_1fab493 = 1;
    }
    g_1eeea08->field_b8->field_0 = a0;
    sub_f7d8d0();
    return;
}
```

## `AzuObjectPool.Start` — RVA `0xc990e4`

- Decompiled symbol: `AzuObjectPool_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `964` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AzuObjectPool_Recovered` matched 3 offsets against `AzuObjectPool` metadata (confidence 1.00).

```c
typedef struct struct_5 {
    char padding_0[24];
    unsigned int field_18;
} struct_5;

typedef struct struct_2 {
    char padding_0[64];
    long long field_40;
} struct_2;

typedef struct AzuObjectPool_Recovered {
    char padding_0[32];
    long long FPSWalkerCapsule;
    long long myTransform;
    struct struct_3 *objRegistry;
} AzuObjectPool_Recovered;

typedef struct struct_3 {
    char padding_0[24];
    int field_18;
} struct_3;

typedef struct struct_6 {
    char padding_0[16];
    long long field_10;
} struct_6;

typedef struct struct_7 {
    char padding_0[16];
    long long field_10;
} struct_7;

typedef struct struct_9 {
    char padding_0[32];
    char field_20;
} struct_9;

typedef struct struct_11 {
    char padding_0[40];
    struct struct_10 *field_28;
} struct_11;

typedef struct struct_10 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_10;

typedef struct struct_8 {
    char padding_0[32];
    long long field_20;
} struct_8;

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
extern long long g_1ef7b48;
extern long long g_1ef8160;
extern long long g_1ef8168;
extern long long g_1efcf38;
extern long long g_1efcf70;
extern long long g_1efeb98;
extern long long g_1f00260;
extern char g_1fab494;

struct_5 * AzuObjectPool_Start(struct_4 *ptr3)
{
    struct_2 *v2;  // x0
    long long v3;  // x0
    long long v12;  // x0
    struct_6 *v13;  // x0
    struct_7 *v14;  // x0
    long long v15;  // x0
    long long v16;  // x23
    struct_9 *v17;  // x0
    long long v18;  // x0
    struct_11 *ptr4;  // x0
    struct_10 *ptr;  // x0
    unsigned long long v21;  // x8
    struct_4 *p;  // x20
    unsigned long v22;  // x10
    struct_8 *ptr5;  // x8
    unsigned long v24;  // x0
    struct_4 *v5;  // x20
    long long v6;  // x0
    struct_4 *addr;  // x21
    struct_4 *ptr6;  // x21
    struct_3 *v9;  // x0
    int v10;  // w22
    int v11;  // w28
    char *v0;  // [bp-0x60]
    char v1;  // [bp+0x0]

    v0 = &v1;
    if (!(g_1fab494 & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efcf70);
        sub_f7d92c(&g_1efeb98);
        sub_f7d92c(&g_1ef7b48);
        sub_f7d92c(&g_1ef8160);
        sub_f7d92c(&g_1ef8168);
        sub_f7d92c(&g_1f00260);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef0e48);
        g_1fab494 = 1;
    }
    if (Camera__get_main(0) && Component__get_transform())
    {
        v2 = sub_1231bc8();
        if (v2 && v2->field_40)
        {
            v3 = sub_1231bc8(v2->field_40, g_1efcf70);
            p = ptr3;
            p->field_20 = v3;
            v5 = &p->field_20;
            sub_f7d8d0(v5, v3);
            v6 = Component__get_transform(ptr3, 0);
            addr = ptr3;
            addr->field_28 = v6;
            ptr6 = &addr->field_28;
            sub_f7d8d0(ptr6, v6);
            v9 = *((long long *)&ptr6->padding_0[8]);
            if (v9)
            {
                v10 = 0;
                while (true)
                {
                    if (v9->field_18 <= v10)
                        return v9;
                    v11 = -1;
                    v12 = sub_14a30c0();
                    if (!v12)
                        break;
                    v11 += 1;
                    if (*((int *)(v12 + 24)) > v11)
                    {
                        if (!ptr3->field_30 || !((v13 = (struct_6 *)sub_14a30c0(ptr3->field_30, (unsigned long long)(unsigned int)v10, g_1ef8168), v13)))
                            break;
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        if (((char)Object__op_Implicit(v13->field_10, 0) & 1))
                        {
                            if (!ptr3->field_30 || !((v14 = (struct_7 *)sub_14a30c0(ptr3->field_30, (unsigned long long)(unsigned int)v10, g_1ef8168), v14 && *((long long *)&ptr6->padding_0[0]) && (Transform__get_position(*((long long *)&ptr6->padding_0[0]), 0), *((long long *)&ptr6->padding_0[0])))))
                                break;
                            Transform__get_rotation(*((long long *)&ptr6->padding_0[0]), 0);
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            v15 = sub_112a1ac(v14->field_10, g_1f00260);
                            if (!ptr3->field_30 || !((v16 = v15, v17 = (struct_9 *)sub_14a30c0(ptr3->field_30, (unsigned long long)(unsigned int)v10, g_1ef8168), v17)))
                                break;
                            if (v17->field_20)
                            {
                                if (!v16)
                                    break;
                                v18 = sub_1249224(v16, g_1efeb98);
                                if (!g_1ef0e48->field_e0)
                                    sub_f7da5c(g_1ef0e48);
                                Physics__IgnoreCollision(v18, *((long long *)&v5->padding_0[0]), 1, 0);
                            }
                            else if (!v16)
                            {
                                break;
                            }
                            GameObject__SetActive(v16, 0, 0);
                            if (!ptr3->field_30 || !((ptr4 = (struct_11 *)sub_14a30c0(ptr3->field_30, (unsigned long long)(unsigned int)v10, g_1ef8168), ptr4 && (ptr = (struct_10 *)ptr4->field_28, ptr && (v21 = ptr->field_10, ptr->field_1c = ptr->field_1c + 1, v21)))))
                                break;
                            v22 = ptr->field_18;
                            if (*((int *)(v21 + 24)) > (unsigned int)v22)
                            {
                                ptr5 = v21 + v22 * 8;
                                ptr->field_18 = (unsigned int)v22 + 1;
                                ptr5->field_20 = v16;
                                sub_f7d8d0((struct struct_8 *)&ptr5->field_20, v16);
                            }
                            else
                            {
                                sub_14a3390();
                            }
                            if (!GameObject__get_transform(v16, 0))
                                break;
                            Transform__set_parent();
                        }
                    }
                    else
                    {
                        v9 = ptr3->field_30;
                        v10 += 1;
                        break;
                    }
                }
            }
        }
    }
    v24 = sub_f7db74();
    return sub_f7db74();
}
```

## `AzuObjectPool.ctor` — RVA `0xc994a8`

- Decompiled symbol: `AzuObjectPool_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    long long field_30;
} struct_0;

extern long long g_1eed748;
extern long long g_1ef8158;
extern char g_1fab497;

void AzuObjectPool_ctor(struct_0 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x20
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x20]
    unsigned long long v2;  // [bp-0x18]
    unsigned long long v3;  // [bp-0x10]
    unsigned long long v4;  // [bp-0x8]

    v0 = v5;
    v1 = v6;
    v2 = v7;
    v3 = v8;
    v4 = v9;
    if (!(g_1fab497 & 1))
    {
        sub_f7d92c(&g_1ef8158);
        sub_f7d92c(&g_1eed748);
        g_1fab497 = 1;
    }
    v10 = sub_f7db70(g_1eed748);
    sub_14a2b64(v10, g_1ef8158);
    ptr->field_30 = v10;
    sub_f7d8d0((struct struct_0 *)&ptr->field_30, v10);
    MonoBehaviour__ctor();
    return;
}
```
