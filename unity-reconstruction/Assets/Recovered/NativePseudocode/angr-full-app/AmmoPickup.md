# Native pseudocode: AmmoPickup

> Metadata source-path string: `Assets/RFPSP/Scripts/Items/AmmoPickup.cs`. This is a path string from the APK metadata, not recovered source text.

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AmmoPickup.Start` — RVA `0xc92bac`

- Decompiled symbol: `AmmoPickup_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `556` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AmmoPickup_Recovered` matched 5 offsets against `AmmoPickup` metadata (confidence 1.00).

```c
typedef struct AmmoPickup_Recovered {
    char padding_0[32];
    long long weaponObj;
    long long WeaponBehaviorComponent;
    struct struct_9 *PlayerWeaponsComponent;
    long long myTransform;
    unsigned int weaponNumber;
} AmmoPickup_Recovered;

typedef struct struct_1 {
    char padding_0[48];
    long long field_30;
} struct_1;

typedef struct struct_5 {
    char padding_0[144];
    struct struct_3 *field_90;
    char padding_98[80];
    struct struct_4 *field_e8;
} struct_5;

typedef struct struct_9 {
    char padding_0[144];
    struct struct_7 *field_90;
    char padding_98[80];
    struct struct_8 *field_e8;
} struct_9;

typedef struct struct_7 {
    char padding_0[96];
    struct struct_6 *field_60;
} struct_7;

typedef struct struct_6 {
    char padding_0[568];
    long long field_238;
} struct_6;

typedef struct struct_8 {
    char padding_0[24];
    int field_18;
} struct_8;

typedef struct struct_3 {
    char padding_0[96];
    struct struct_2 *field_60;
} struct_3;

typedef struct struct_4 {
    char padding_0[24];
    unsigned int field_18;
} struct_4;

typedef struct struct_2 {
    char padding_0[568];
    unsigned long long field_238;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0e48;
extern long long g_1efcf38;
extern long long g_1efcf70;
extern long long g_1efed18;
extern long long g_1efed60;
extern char g_1fab45d;

long long AmmoPickup_Start(struct_10 *ptr5)
{
    long long v0;  // x1
    struct_10 *p;  // x0
    unsigned long v10;  // x0
    struct_9 *ptr6;  // x8
    unsigned long long idx;  // x23
    struct_8 *v13;  // x8
    int v14;  // w24
    struct_8 *ptr7;  // x8
    unsigned long v16;  // x1
    long long v17;  // x0
    unsigned long v18;  // x0
    struct_1 *ptr8;  // x0
    long long v3;  // x1
    struct_10 *addr;  // x20
    struct_10 *ptr4;  // x20
    struct_5 *v6;  // x0
    struct_10 *ptr3;  // x21
    struct_10 *ptr;  // x21
    unsigned long v9;  // x0

    if (!(g_1fab45d & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efcf70);
        sub_f7d92c(&g_1efed60);
        sub_f7d92c(&g_1efed18);
        sub_f7d92c(&g_1ef0e48);
        g_1fab45d = 1;
    }
    v0 = Component__get_transform(ptr5, 0);
    p = ptr5;
    p->field_38 = v0;
    sub_f7d8d0(&p->field_38, v0);
    if (Camera__get_main(0) && Component__get_transform())
    {
        ptr8 = sub_1231bc8();
        if (ptr8)
        {
            v3 = ptr8->field_30;
            addr = ptr5;
            addr->field_20 = v3;
            ptr4 = &addr->field_20;
            sub_f7d8d0(ptr4, v3);
            if (*((long long *)&ptr4->padding_0[0]))
            {
                v6 = sub_1249488(*((long long *)&ptr4->padding_0[0]), g_1efed60);
                ptr3 = ptr5;
                ptr3->field_30 = v6;
                ptr = &ptr3->field_30;
                sub_f7d8d0(ptr, v6);
                if (*((long long *)&ptr->padding_0[8]))
                {
                    v9 = sub_1231bc8(*((long long *)&ptr->padding_0[8]), g_1efcf70);
                    if (*((long long *)&ptr->padding_0[0]) && *((long long *)(*((long long *)&ptr->padding_0[0]) + 144)) && *((long long *)(*((long long *)(*((long long *)&ptr->padding_0[0]) + 144)) + 96)))
                    {
                        if (!g_1ef0e48->field_e0)
                            sub_f7da5c(g_1ef0e48);
                        v10 = Physics__IgnoreCollision(v9, *((long long *)(*((long long *)(*((long long *)(*((long long *)&ptr->padding_0[0]) + 144)) + 96)) + 568)), 1, 0);
                        ptr6 = *((long long *)&ptr->padding_0[0]);
                        if (*((long long *)&ptr->padding_0[0]))
                        {
                            idx = 4;
                            while (true)
                            {
                                v13 = ptr6->field_e8;
                                if (!v13)
                                    break;
                                v14 = idx - 4;
                                if (v13->field_18 <= v14)
                                    return v10;
                                if (v13->field_18 <= v14)
                                    sub_f7db7c();
                                if (!*((long long *)&v13->padding_0[8 * idx]) || !((v10 = (unsigned long)sub_1249224(*((long long *)&v13->padding_0[8 * idx]), g_1efed18), v10)))
                                    break;
                                if (*((int *)(v10 + 292)) != ptr5->field_40)
                                {
                                    ptr6 = *((long long *)&ptr->padding_0[0]);
                                    idx += 1;
                                    if (!ptr6)
                                        break;
                                }
                                else
                                {
                                    if (!*((long long *)&ptr->padding_0[0]) || !((ptr7 = (struct_8 *)*((long long *)(*((long long *)&ptr->padding_0[0]) + 232)), ptr7)))
                                        break;
                                    if (ptr7->field_18 > v14)
                                    {
                                        v16 = *((long long *)&ptr7->padding_0[8 * idx]);
                                        *((unsigned long *)&ptr4->padding_0[0]) = v16;
                                        sub_f7d8d0(ptr4, v16);
                                        if (*((long long *)&ptr4->padding_0[0]))
                                        {
                                            ptr5->field_28 = sub_1249224(*((long long *)&ptr4->padding_0[0]), g_1efed18);
                                            v17 = sub_f7d8d0();
                                            return sub_f7d8d0();
                                        }
                                        break;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    v18 = sub_f7db74();
    return sub_f7db74();
}
```

## `AmmoPickup.PickUpItem` — RVA `0xc92dd8`

- Decompiled symbol: `AmmoPickup_PickUpItem`
- Metadata signature: `public void PickUpItem() { }`
- Native interval: `548` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AmmoPickup_Recovered` matched 8 offsets against `AmmoPickup` metadata (confidence 1.00).

```c
typedef struct AmmoPickup_Recovered {
    char padding_0[40];
    struct struct_3 *WeaponBehaviorComponent;
    long long PlayerWeaponsComponent;
    long long myTransform;
    char padding_40[4];
    unsigned int objectPoolIndex;
    char removeOnUse;
    char padding_49[7];
    long long pickupSound;
    long long fullSound;
    unsigned int ammoToAdd;
} AmmoPickup_Recovered;

typedef struct struct_3 {
    char padding_0[288];
    char field_120;
    char padding_121[3];
    unsigned int field_124;
    int field_128;
    char padding_12c[202];
    char field_1f6;
    char field_1f7;
} struct_3;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

extern struct_2 *g_1ef0c58;
extern char g_1fab45e;

long long AmmoPickup_PickUpItem(struct_4 *ptr)
{
    struct_3 *p;  // x8
    int v1;  // w9
    int v2;  // w10
    unsigned long v3;  // x0
    struct_3 *addr;  // x8
    long long v5;  // x20
    unsigned long long v6;  // x0
    unsigned long v7;  // x0
    unsigned long long v8;  // x0

    if (!(g_1fab45e & 1))
    {
        sub_f7d92c("s.");
        sub_f7d92c(&g_1ef0c58);
        g_1fab45e = 1;
    }
    p = ptr->field_28;
    if (p)
    {
        v1 = *((int *)&p->padding_12c[12]);
        if (v1 > p->field_128)
        {
            v2 = ptr->field_60 + p->field_128;
            if (v1 >= v2)
                v1 = v2;
            p->field_128 = v1;
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v3 = Object__op_Implicit(ptr->field_50, 0);
            if (!((char)v3 & 1))
            {
LABEL_1092e9c:
                addr = ptr->field_28;
                if (addr)
                {
                    if (!addr->field_1f6 && !addr->field_120 && !addr->field_1f7)
                    {
                        addr->field_120 = 1;
                        v5 = ptr->field_30;
                        if (v5)
                        {
                            v3 = MonoBehaviour__StartCoroutine(v5, PlayerWeapons__SelectWeapon(v5, addr->field_124, 0, 0, 0), 0);
                            goto LABEL_1092ef4;
                        }
                    }
                    else
                    {
LABEL_1092ef4:
                        if (!ptr->field_48)
                            return v3;
                        AmmoPickup__FreePooledObjects();
                        if (ptr->field_44)
                        {
                            if (ptr->field_38)
                                Component__get_gameObject(ptr->field_38, 0);
                        }
                        else
                        {
                            Component__get_gameObject(ptr, 0);
                            if (!g_1ef0c58->field_e0)
                                sub_f7da5c(g_1ef0c58);
                            v6 = Object__Destroy();
                            return Object__Destroy();
                        }
                    }
                }
            }
            else if (ptr->field_38)
            {
                Transform__get_position(ptr->field_38, 0);
                v3 = PlayAudioAtPos__PlayClipAt(ptr->field_50);
                goto LABEL_1092e9c;
            }
        }
        else
        {
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v7 = Object__op_Implicit(ptr->field_58, 0);
            if (!((char)v7 & 1))
            {
                return v7;
            }
            else if (ptr->field_38)
            {
                Transform__get_position(ptr->field_38, 0);
                v8 = PlayAudioAtPos__PlayClipAt();
                return PlayAudioAtPos__PlayClipAt();
            }
        }
    }
    sub_f7db74();
}
```

## `AmmoPickup.FreePooledObjects` — RVA `0xc92ffc`

- Decompiled symbol: `AmmoPickup_FreePooledObjects`
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
extern char g_1fab45f;

void AmmoPickup_FreePooledObjects(long long a0)
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

    if (!(g_1fab45f & 1))
    {
        sub_f7d92c("s.");
        sub_f7d92c(&g_1efedb0);
        sub_f7d92c(&g_1efedb8);
        sub_f7d92c("s%");
        g_1fab45f = 1;
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
                    goto LABEL_10931e4;
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
LABEL_10931e4:
    sub_f7db7c(sub_f7db74());
}
```

## `AmmoPickup.ctor` — RVA `0xc932fc`

- Decompiled symbol: `AmmoPickup_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `20` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AmmoPickup_Recovered` matched 2 offsets against `AmmoPickup` metadata (confidence 1.00).

```c
typedef struct AmmoPickup_Recovered {
    char padding_0[72];
    char removeOnUse;
    char padding_49[23];
    unsigned int ammoToAdd;
} AmmoPickup_Recovered;

long long AmmoPickup_ctor(struct_0 *ptr)
{
    ptr->field_48 = 1;
    ptr->field_60 = 1;
}
```
