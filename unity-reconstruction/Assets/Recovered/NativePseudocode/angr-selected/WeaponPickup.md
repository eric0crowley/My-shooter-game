# Native pseudocode: WeaponPickup

> Metadata source-path string: `Assets/RFPSP/Scripts/Items/WeaponPickup.cs`. This is a path string from the APK metadata, not recovered source text.

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `WeaponPickup.Start` — RVA `0xc94454`

- Decompiled symbol: `WeaponPickup_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `576` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponPickup_Recovered` matched 3 offsets against `WeaponPickup` metadata (confidence 1.00).

```c
typedef struct WeaponPickup_Recovered {
    char padding_0[32];
    long long weaponObj;
    long long myTransform;
    unsigned int weaponNumber;
} WeaponPickup_Recovered;

typedef struct struct_3 {
    char padding_0[48];
    long long field_30;
} struct_3;

typedef struct struct_6 {
    char padding_0[112];
    long long field_70;
    char padding_78[24];
    struct struct_4 *field_90;
    char padding_98[80];
    struct struct_5 *field_e8;
} struct_6;

typedef struct struct_8 {
    char padding_0[24];
    unsigned int field_18;
} struct_8;

typedef struct struct_7 {
    char padding_0[32];
    long long field_20;
} struct_7;

typedef struct struct_5 {
    char padding_0[24];
    int field_18;
} struct_5;

typedef struct struct_4 {
    char padding_0[96];
    unsigned long long field_60;
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
extern long long g_1efcf38;
extern long long g_1efcf70;
extern long long g_1efec90;
extern long long g_1efed18;
extern char g_1fab46b;

long long WeaponPickup_Start(struct_2 *a0)
{
    struct_2 *cur;  // x20
    long long v1;  // x0
    unsigned long long v9;  // x24
    struct_7 *v10;  // x8
    long long v11;  // x0
    struct_5 *v12;  // x8
    unsigned long v13;  // x1
    long long v14;  // x0
    long long v15;  // x0
    unsigned long long v16;  // x0
    struct_2 *p;  // x19
    struct_2 *v3;  // x19
    struct_3 *v4;  // x0
    struct_6 *addr;  // x0
    struct_8 *v6;  // x8
    struct_6 *ptr;  // x21
    long long *v8;  // x22

    cur = a0;
    if (!(g_1fab46b & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efcf70);
        sub_f7d92c(&g_1efec90);
        sub_f7d92c(&g_1efed18);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef0e48);
        g_1fab46b = 1;
    }
    v1 = Component__get_transform(cur, 0);
    p = cur;
    p->field_28 = v1;
    v3 = &p->field_28;
    sub_f7d8d0(v3, v1);
    if (Camera__get_main(0) && Component__get_transform())
    {
        v4 = sub_1231bc8();
        if (v4 && v4->field_30)
        {
            addr = sub_1249224(v4->field_30, g_1efec90);
            if (addr)
            {
                v6 = addr->field_e8;
                ptr = addr;
                if (addr->field_e8)
                {
                    v8 = NULL;
                    while (v6->field_18 > (unsigned int)v8)
                    {
                        if (v6->field_18 <= (unsigned int)v8)
                            goto LABEL_1094690;
                        v10 = &v6->padding_0[8 * (v8 * 0x100000000 >> 63 & 0xffffffff00000000 | v8 & 4294967295)];
                        if (!v10->field_20 || (v11 = sub_1249224(v10->field_20, g_1efed18), v11 && *((int *)(v11 + 292)) != cur->field_30 && !((v6 = (struct_8 *)ptr->field_e8, v8 = (long long *)(unsigned long long)((unsigned int)v8 + 1), !ptr->field_e8)) || (v6 = (struct_8 *)ptr->field_e8, v8 = (long long *)(unsigned long long)((unsigned int)v8 + 1), !ptr->field_e8)) || (v6 = (struct_8 *)ptr->field_e8, v8 = (long long *)(unsigned long long)((unsigned int)v8 + 1), !ptr->field_e8))
                            break;
                    }
                }
            }
        }
    }
    while (true)
    {
        do
        {
            sub_f7db74();
        } while ((v12 = (struct_5 *)ptr->field_e8, !v12));
        if (v12->field_18 <= (unsigned int)v8)
            break;
        v13 = *((long long *)&v12[1].padding_0[4 + 8 * v9]);
        cur->field_20 = v13;
        cur = &cur->field_20;
        sub_f7d8d0(cur, v13);
        if (ptr->field_70)
        {
            v14 = GameObject__get_activeInHierarchy(ptr->field_70, 0);
            if (!((char)v14 & 1))
            {
                return v14;
            }
            else if (*((long long *)&v3->padding_0[0]))
            {
                v8 = &g_1efcf70;
                cur = sub_1231bc8(*((long long *)&v3->padding_0[0]), g_1efcf70);
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v15 = Object__op_Implicit(cur, 0);
                if (!((char)v15 & 1))
                {
                    return v15;
                }
                else if (*((long long *)&v3->padding_0[0]) && (sub_1231bc8(*((long long *)&v3->padding_0[0]), g_1efcf70), ptr->field_90 && ptr->field_90->field_60))
                {
                    if (!g_1ef0e48->field_e0)
                        sub_f7da5c(g_1ef0e48);
                    v16 = Physics__IgnoreCollision();
                    return Physics__IgnoreCollision();
                }
            }
        }
    }
LABEL_1094690:
    sub_f7db7c();
}
```


## `WeaponPickup.DestroyWeapon` — RVA `0xc94694`

- Decompiled symbol: `WeaponPickup_DestroyWeapon`
- Metadata signature: `public IEnumerator DestroyWeapon(float waitTime) { }`
- Native interval: `124` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponPickup_Recovered` matched 2 offsets against `WeaponPickup` metadata (confidence 0.67).

```c
typedef struct WeaponPickup_Recovered {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long weaponObj;
    unsigned int myTransform;
} WeaponPickup_Recovered;

extern long long g_1ef4028;
extern char g_1fab46c;

struct_0 * WeaponPickup_DestroyWeapon(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0
    unsigned int v2;  // s0

    if (!(g_1fab46c & 1))
    {
        sub_f7d92c(&g_1ef4028);
        g_1fab46c = 1;
    }
    v0 = sub_f7db70(g_1ef4028);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    ptr->field_28 = v2;
    return ptr;
}
```


## `WeaponPickup.<DestroyWeapon>d__11.ctor` — RVA `0xc94710`

- Decompiled symbol: `WeaponPickup_DestroyWeapon_d__11_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void WeaponPickup_DestroyWeapon_d__11_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `WeaponPickup.FreePooledObjects` — RVA `0xc94738`

- Decompiled symbol: `WeaponPickup_FreePooledObjects`
- Metadata signature: `private void FreePooledObjects() { }`
- Native interval: `496` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[24];
    int field_18;
} struct_2;

typedef struct struct_3 {
    char padding_0[32];
    unsigned long long field_20;
    char padding_28[9];
    char field_31;
    char padding_32[70];
    unsigned long long field_78;
} struct_3;

extern long long g_1efedb0;
extern long long g_1efedb8;
extern char g_1fab46d;

void WeaponPickup_FreePooledObjects(long long a0)
{
    struct_2 *ptr;  // x0
    unsigned int v1;  // w8
    struct_2 *p;  // x20
    unsigned int v3;  // w22
    unsigned long long v4[10];  // x24
    unsigned long v5;  // x0
    unsigned int v6;  // w8
    struct_2 *addr;  // x19
    unsigned int v8;  // w21
    struct_3 *ptr3;  // x20

    if (!(g_1fab46d & 1))
    {
        sub_f7d92c("s.");
        sub_f7d92c(&g_1efedb0);
        sub_f7d92c(&g_1efedb8);
        sub_f7d92c("s%");
        g_1fab46d = 1;
    }
    if (Component__get_gameObject(a0, 0) && (ptr = (struct_2 *)(unsigned long long)sub_1249ec4(), ptr))
    {
        v1 = ptr->field_18;
        p = ptr;
        if (ptr->field_18 >= 1)
        {
            v3 = 0;
            do
            {
                if (v1 <= v3)
                    sub_f7db7c(ptr);
                v4 = *((long long *)&p[1].padding_0[4 + 8 * v3]);
                if (!v4)
                    sub_f7db7c(sub_f7db74());
                if (!g_1eeea08->field_b8->field_0)
                    sub_f7db7c(sub_f7db74());
                v5 = Component__get_transform(g_1eeea08->field_b8->field_0, 0);
                if (!v4[9])
                    sub_f7db7c(sub_f7db74());
                Transform__set_parent(v4[9], v5, 0);
                if (!v4[8])
                    goto LABEL_1094920;
            } while ((ptr = (struct_2 *)GameObject__SetActive(v4[8], 0, 0), v1 = (unsigned int)p->field_18, v3 += 1, v3 < v1));
        }
        else if (Component__get_gameObject(a0, 0))
        {
            ptr = sub_1249ec4();
            if (ptr)
            {
                v6 = ptr->field_18;
                addr = ptr;
                if (v6 < 1)
                    return;
                v8 = 0;
                while (true)
                {
                    if (v6 <= v8)
                        sub_f7db7c(ptr);
                    ptr3 = *((long long *)&addr[1].padding_0[4 + 8 * v8]);
                    if (!ptr3 || !Component__get_transform(ptr3, 0) || !((Transform__set_parent(), ptr3->field_20 && (Rigidbody__set_isKinematic(ptr3->field_20, 0, 0), ptr3->field_78 && (Collider__set_isTrigger(ptr3->field_78, 0, 0), Component__get_gameObject(ptr3, 0))))))
                        break;
                    ptr = GameObject__set_tag();
                    ptr3->field_31 = 1;
                    v6 = addr->field_18;
                    v8 += 1;
                    if (v8 >= v6)
                        return;
                }
            }
        }
    }
LABEL_1094920:
    sub_f7db7c(sub_f7db74());
}
```


## `WeaponPickup.PickUpItem` — RVA `0xc94928`

- Decompiled symbol: `WeaponPickup_PickUpItem`
- Metadata signature: `private void PickUpItem() { }`
- Native interval: `1040` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponPickup_Recovered` matched 6 offsets against `WeaponPickup` metadata (confidence 1.00).

```c
typedef struct struct_4 {
    char padding_0[152];
    struct struct_5 *field_98;
    char padding_a0[44];
    unsigned int field_cc;
    char padding_d0[12];
    unsigned int field_dc;
    char padding_e0[8];
    unsigned long long field_e8;
} struct_4;

typedef struct WeaponPickup_Recovered {
    char padding_0[32];
    long long weaponObj;
    long long myTransform;
    char padding_30[4];
    unsigned int weaponToDrop;
    char removeOnUse;
    char padding_39[15];
    long long pickupSound;
    struct struct_6 *fullSound;
} WeaponPickup_Recovered;

typedef struct struct_1 {
    char padding_0[48];
    long long field_30;
} struct_1;

typedef struct struct_14 {
    char padding_0[288];
    char field_120;
    char padding_121[1];
    char field_122;
    char field_123;
    unsigned int field_124;
    int field_128;
    char padding_12c[4];
    unsigned int field_130;
    char padding_134[208];
    unsigned int field_204;
    char padding_208[85];
    char field_25d;
} struct_14;

typedef struct struct_2 {
    char padding_0[32];
    long long field_20;
} struct_2;

typedef struct struct_3 {
    char padding_0[32];
    long long field_20;
} struct_3;

typedef struct struct_9 {
    char padding_0[32];
    long long field_20;
} struct_9;

typedef struct struct_10 {
    char padding_0[32];
    long long field_20;
} struct_10;

typedef struct struct_11 {
    char padding_0[32];
    long long field_20;
} struct_11;

typedef struct struct_12 {
    char padding_0[32];
    long long field_20;
} struct_12;

typedef struct struct_13 {
    char padding_0[605];
    char field_25d;
} struct_13;

typedef struct struct_5 {
    char padding_0[290];
    char field_122;
    char padding_123[314];
    char field_25d;
} struct_5;

typedef struct struct_6 {
    char padding_0[152];
    struct struct_7 *field_98;
    char padding_a0[44];
    unsigned int field_cc;
    char padding_d0[12];
    unsigned int field_dc;
    char padding_e0[8];
    unsigned long long field_e8;
} struct_6;

typedef struct struct_7 {
    char padding_0[290];
    char field_122;
    char padding_123[314];
    char field_25d;
} struct_7;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern char g_1094d38;
extern struct_0 *g_1ef0c58;
extern long long g_1efcf38;
extern long long g_1efec90;
extern long long g_1efed18;
extern struct_4 g_1fab000;
extern char g_1fab46e;
extern char g_1fab46f;

long long WeaponPickup_PickUpItem(struct_8 *a0)
{
    struct_4 *ptr;  // x20
    struct_8 *addr;  // x19
    long long v14;  // x0
    unsigned long long v15;  // x0
    char ptr3[606];  // x8
    unsigned long ptr4;  // x8, Other Possible Types: unsigned long long
    unsigned long v18;  // x23
    unsigned long long v19;  // x24
    struct_2 *v20;  // x8
    unsigned long v21;  // x8
    struct_3 *v22;  // x8
    unsigned int v23;  // w9
    struct_1 *v6;  // x0
    unsigned long long v24;  // x24
    unsigned long long v25;  // x25
    struct_9 *v26;  // x8
    unsigned long v27;  // x8
    struct_10 *v28;  // x8
    unsigned long v29;  // x8
    unsigned long v30;  // x9
    struct_11 *v31;  // x8
    unsigned long v32;  // x8
    struct_4 *v7;  // x0
    unsigned long v33;  // x9
    struct_12 *v34;  // x8
    struct_13 *ptr5;  // x0
    unsigned long v36;  // x1
    struct_8 *v38;  // x0
    struct_8 *v39;  // x19
    long long v40;  // x0
    unsigned long long v41;  // x0
    struct_14 *ptr6;  // x0
    struct_14 *p;  // x21
    unsigned int v10;  // w8
    unsigned int v11;  // s0
    unsigned long long v12;  // 4103
    unsigned int v13;  // w9
    unsigned long v0;  // [bp-0x20]
    struct_14 *v1;  // [bp-0x18]
    struct_4 *v2;  // [bp-0x10]
    struct_8 *v3;  // [bp-0x8]

    ptr = &g_1fab000.padding_0[0];
    addr = a0;
    if (!(g_1fab46e & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efec90);
        sub_f7d92c(&g_1efed18);
        sub_f7d92c(&g_1ef0c58);
        g_1fab46e = 1;
    }
    if (Camera__get_main(0) && Component__get_transform() && !((v6 = (struct_1 *)sub_1231bc8(), !v6 || !v6->field_30 || (v7 = (struct_4 *)sub_1249224(v6->field_30, g_1efec90), !addr->field_20 || (ptr = (struct_4 *)sub_1249224(v6->field_30, g_1efec90), ptr6 = (struct_14 *)sub_1249224(addr->field_20, g_1efed18), !ptr || (p = ptr6, !ptr6))))))
    {
        if (p->field_120)
        {
            v10 = *((int *)&p->padding_134[4]);
            if (v10 > p->field_128 && addr->field_38 && !((v11 = p->field_204, v12 = ((((unsigned long long)(char)(CmpF(v11, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v11, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v11, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v11, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v11, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v11, 0.0) & 1)) >> 1 & 1), !((char)(v12 * 0x10000000 >> 30)))))
            {
                v13 = p->field_130 + p->field_128;
                if (v10 >= v13)
                    v10 = v13;
                p->field_128 = v10;
                goto LABEL_1094cfc;
            }
            else
            {
                ptr = addr->field_50;
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v14 = Object__op_Implicit(ptr, 0);
                if (!((char)v14 & 1))
                    return v14;
                if (addr->field_28)
                {
                    Transform__get_position(addr->field_28, 0);
                    v15 = PlayAudioAtPos__PlayClipAt();
                    return PlayAudioAtPos__PlayClipAt();
                }
            }
        }
        else if (*((int *)&ptr->padding_d0[8]) == ptr->field_cc && p->field_123)
        {
            ptr3 = ptr->field_98;
            if (ptr3)
            {
                if (ptr3[290])
                {
                    if (!addr->field_38 || p->field_25d || ptr3[605])
                    {
                        ptr3[288] = 0;
                        ptr3[605] = 0;
LABEL_1094cac:
                        p->field_25d = 1;
                        goto LABEL_1094cb4;
                    }
                    else
                    {
LABEL_1094d20:
                        PlayerWeapons__DropWeapon(ptr);
                        goto LABEL_1094cb4;
                    }
                }
                else
                {
                    if (ptr->field_e8)
                    {
                        v18 = ptr->field_dc;
                        while (*((int *)(ptr4 + 24)) > (unsigned int)v18)
                        {
                            if (*((int *)(ptr4 + 24)) <= (unsigned int)v18)
                                goto LABEL_1094d34;
                            v19 = v18 * 0x100000000 >> 63 & 0xffffffff00000000 | v18 & 4294967295;
                            v20 = ptr4 + v19 * 8;
                            if (!v20->field_20 || !((ptr6 = (struct_14 *)sub_1249224(v20->field_20, g_1efed18), ptr6)))
                                goto LABEL_1094d30;
                            if (ptr6->field_120)
                            {
                                v21 = ptr->field_e8;
                                if (!v21)
                                    goto LABEL_1094d30;
                                if (*((int *)(v21 + 24)) <= (unsigned int)v18)
                                    goto LABEL_1094d34;
                                v22 = v21 + v19 * 8;
                                if (!v22->field_20 || !((ptr6 = (struct_14 *)sub_1249224(v22->field_20, g_1efed18), ptr6)))
                                    goto LABEL_1094d30;
                                if (ptr6->field_122)
                                {
                                    addr->field_34 = v18;
                                    break;
                                }
                            }
                            ptr4 = ptr->field_e8;
                            if (!ptr4)
                                goto LABEL_1094d30;
                            v23 = *((int *)(ptr4 + 24));
                            if ((unsigned int)v18 == v23 - 1 && v23 >= 1)
                            {
                                v24 = 0;
                                while (true)
                                {
                                    if (v23 <= (unsigned int)v24)
                                        goto LABEL_1094d34;
                                    v26 = ptr4 + (v24 * 0x100000000 >> 63 & 0xffffffff00000000 | v24 & 4294967295) * 8;
                                    if (!v26->field_20 || (ptr6 = (struct_14 *)sub_1249224(v26->field_20, g_1efed18), !ptr6))
                                        goto LABEL_1094d30;
                                    if (ptr6->field_120)
                                        break;
LABEL_1094c00:
                                    ptr4 = ptr->field_e8;
                                    if (!ptr4)
                                        goto LABEL_1094d30;
                                    v23 = *((int *)(ptr4 + 24));
                                    v24 = (unsigned int)v24 + 1;
                                    if ((unsigned int)v24 >= v23)
                                        goto LABEL_1094c24;
                                }
                                v27 = ptr->field_e8;
                                if (!v27)
                                    goto LABEL_1094d30;
                                if (*((int *)(v27 + 24)) <= (unsigned int)v24)
                                    goto LABEL_1094d34;
                                v28 = v27 + v25 * 8;
                                if (!v28->field_20 || !((ptr6 = (struct_14 *)sub_1249224(v28->field_20, g_1efed18), ptr6)))
                                    goto LABEL_1094d30;
                                if (!ptr6->field_122)
                                    goto LABEL_1094c00;
                                addr->field_34 = v24;
                                ptr4 = ptr->field_e8;
                            }
LABEL_1094c24:
                            v18 = (unsigned int)v18 + 1;
                            if (!ptr4)
                                goto LABEL_1094d30;
                        }
                        if (addr->field_38 && !p->field_25d)
                            goto LABEL_1094d20;
                        v29 = ptr->field_e8;
                        if (v29)
                        {
                            v30 = addr->field_34;
                            if (*((int *)(v29 + 24)) <= (unsigned int)v30)
                                goto LABEL_1094d34;
                            v31 = v29 + v30 * 8;
                            if (!v31->field_20 || (ptr6 = (struct_14 *)sub_1249224(v31->field_20, g_1efed18), !ptr6 || (ptr6->field_120 = 0, v32 = (unsigned long)ptr->field_e8, !v32)))
                                goto LABEL_1094d30;
                            v33 = addr->field_34;
                            if (*((int *)(v32 + 24)) <= (unsigned int)v33)
                                goto LABEL_1094d34;
                            v34 = v32 + v33 * 8;
                            if (!v34->field_20 || !((ptr5 = (struct_13 *)sub_1249224(v34->field_20, g_1efed18), ptr5)))
                                goto LABEL_1094d30;
                            ptr5->field_25d = 0;
                            goto LABEL_1094cac;
                        }
                    }
                }
            }
        }
        else
        {
LABEL_1094cb4:
            p->field_120 = 1;
            v36 = p->field_124;
            p->field_25d = addr->field_38 ^ 1;
            MonoBehaviour__StartCoroutine(ptr, PlayerWeapons__SelectWeapon(ptr, v36, 0, 0, 0), 0);
            PlayerWeapons__UpdateTotalWeapons(ptr, 0);
LABEL_1094cfc:
            v38 = addr;
            ptr = v2;
            addr = v3;
            p = v1;
            goto LABEL_1094d38;
        }
    }
LABEL_1094d30:
    ptr6 = sub_f7db74();
LABEL_1094d34:
    vvar_714{r256|8b} = (int)&g_1094d38;
    v38 = sub_f7db7c(ptr6);
LABEL_1094d38:
    v0 = vvar_201{r256|8b};
    v1 = p;
    v2 = ptr;
    v3 = addr;
    v39 = v38;
    if (!(g_1fab46f & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab46f = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v40 = Object__op_Implicit(v39->field_48, 0);
    if (((char)v40 & 1))
    {
        if (v39->field_28)
        {
            Transform__get_position(v39->field_28, 0);
            v40 = PlayAudioAtPos__PlayClipAt(v39->field_48);
        }
        else
        {
            sub_f7db74(0);
        }
    }
    if (!v39->field_38)
        return v40;
    WeaponPickup__FreePooledObjects(v39);
    Component__get_gameObject(v39, 0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v41 = Object__Destroy();
    return Object__Destroy();
}
```


## `WeaponPickup.RemovePickup` — RVA `0xc94d38`

- Decompiled symbol: `WeaponPickup_RemovePickup`
- Metadata signature: `private void RemovePickup() { }`
- Native interval: `228` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x1094d38: stp x30, x21, [sp, #-0x20]!
// 0x1094d3c: stp x20, x19, [sp, #0x10]
// 0x1094d40: adrp x20, #0x1fab000
// 0x1094d44: adrp x21, #0x1e8c000
// 0x1094d48: ldrb w8, [x20, #0x46f]
// 0x1094d4c: ldr x21, [x21, #0xd8]
// 0x1094d50: mov x19, x0
// 0x1094d54: tbnz w8, #0, #0x1094d6c
// 0x1094d58: adrp x0, #0x1e8c000
// 0x1094d5c: ldr x0, [x0, #0xd8]
// 0x1094d60: bl #0xf7d92c
// 0x1094d64: mov w8, #1
// 0x1094d68: strb w8, [x20, #0x46f]
// 0x1094d6c: ldr x0, [x21]
// 0x1094d70: ldr x20, [x19, #0x48]
// 0x1094d74: ldr w8, [x0, #0xe0]
// 0x1094d78: cbnz w8, #0x1094d80
// 0x1094d7c: bl #0xf7da5c
// 0x1094d80: mov x0, x20
// 0x1094d84: mov x1, xzr
// 0x1094d88: bl #0x1b98274
// 0x1094d8c: tbz w0, #0, #0x1094dc4
// 0x1094d90: ldr x0, [x19, #0x28]
// 0x1094d94: cbz x0, #0x1094e18
// 0x1094d98: ldr x20, [x19, #0x48]
// 0x1094d9c: mov x1, xzr
// 0x1094da0: bl #0x1b9d508
// 0x1094da4: mov w8, #0x43fa0000
// 0x1094da8: fmov s3, #0.75000000
// 0x1094dac: fmov s4, #1.00000000
// 0x1094db0: fmov s5, #1.00000000
// 0x1094db4: fmov s6, #1.00000000
// 0x1094db8: fmov s7, w8
// 0x1094dbc: mov x0, x20
// 0x1094dc0: bl #0x108d260
// 0x1094dc4: ldrb w8, [x19, #0x38]
// 0x1094dc8: cbz w8, #0x1094e0c
// 0x1094dcc: mov x0, x19
// 0x1094dd0: bl #0x1094738
// 0x1094dd4: mov x0, x19
// 0x1094dd8: mov x1, xzr
// 0x1094ddc: bl #0x1b92190
// 0x1094de0: ldr x8, [x21]
// 0x1094de4: mov x19, x0
// 0x1094de8: ldr w9, [x8, #0xe0]
// 0x1094dec: cbnz w9, #0x1094df8
// 0x1094df0: mov x0, x8
// 0x1094df4: bl #0xf7da5c
// 0x1094df8: mov x0, x19
// 0x1094dfc: ldp x20, x19, [sp, #0x10]
// 0x1094e00: mov x1, xzr
// 0x1094e04: ldp x30, x21, [sp], #0x20
// 0x1094e08: b #0x1b98a20
// 0x1094e0c: ldp x20, x19, [sp, #0x10]
// 0x1094e10: ldp x30, x21, [sp], #0x20
// 0x1094e14: ret
// 0x1094e18: bl #0xf7db74
```


## `WeaponPickup.ctor` — RVA `0xc94e1c`

- Decompiled symbol: `WeaponPickup_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[56];
    char field_38;
} struct_0;

long long WeaponPickup_ctor(struct_0 *ptr)
{
    ptr->field_38 = 1;
}
```


## `WeaponPickup.<DestroyWeapon>d__11.Dispose` — RVA `0xc94e2c`

- Decompiled symbol: `WeaponPickup_DestroyWeapon_d__11_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long WeaponPickup_DestroyWeapon_d__11_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `WeaponPickup.<DestroyWeapon>d__11.MoveNext` — RVA `0xc94e30`

- Decompiled symbol: `WeaponPickup_DestroyWeapon_d__11_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `252` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    unsigned long long field_18;
    struct struct_1 *field_20;
    unsigned int field_28;
} struct_2;

typedef struct struct_1 {
    char padding_0[64];
    unsigned int field_40;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab470;

unsigned int WeaponPickup_DestroyWeapon_d__11_MoveNext(struct_2 *ptr)
{
    struct_1 *p;  // x20
    unsigned int v1;  // s0
    unsigned int v2;  // s1
    unsigned long v3;  // 4138
    long long v4;  // x0
    struct_2 *addr;  // x19

    if (!(g_1fab470 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab470 = 1;
    }
    p = ptr->field_20;
    if (ptr->field_10 == 1)
    {
        ptr->field_10 = 4294967295;
        if (!p)
            sub_f7db74();
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        Time__get_time(0);
        if (!p)
            sub_f7db74();
        p->field_40 = v1;
    }
    else
    {
        return 0;
    }
    Time__get_time(0);
    v2 = p->field_40 + ptr->field_28;
    v3 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v2, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v1) & 1)) & ((unsigned long long)(char)(CmpF(v2, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v3)
    {
        ptr->field_18 = 0;
        addr = &ptr->field_18;
        sub_f7d8d0(addr, 0);
        *((unsigned int *)&addr->padding_0[8]) = 1;
        return 1;
    }
    WeaponPickup__FreePooledObjects(p);
    v4 = Component__get_gameObject(p, 0);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    Object__Destroy(v4, 0);
    return 0;
}
```


## `WeaponPickup.<DestroyWeapon>d__11.get_Current` — RVA `0xc94f2c`

- Decompiled symbol: `WeaponPickup_DestroyWeapon_d__11_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long WeaponPickup_DestroyWeapon_d__11_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `WeaponPickup.<DestroyWeapon>d__11.Reset` — RVA `0xc94f34`

- Decompiled symbol: `WeaponPickup_DestroyWeapon_d__11_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05390;

void WeaponPickup_DestroyWeapon_d__11_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f05390));
}
```


## `WeaponPickup.<DestroyWeapon>d__11.get_Current` — RVA `0xc94f6c`

- Decompiled symbol: `WeaponPickup_DestroyWeapon_d__11_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long WeaponPickup_DestroyWeapon_d__11_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
