# Native pseudocode: DrinkPickup

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DrinkPickup.Start` — RVA `0xc9356c`

- Decompiled symbol: `DrinkPickup_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `316` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DrinkPickup_Recovered` matched 3 offsets against `DrinkPickup` metadata (confidence 1.00).

```c
typedef struct DrinkPickup_Recovered {
    char padding_0[32];
    long long playerObj;
    long long myTransform;
    char padding_30[32];
    struct struct_2 *FPSPlayerComponent;
} DrinkPickup_Recovered;

typedef struct struct_1 {
    char padding_0[40];
    long long field_28;
} struct_1;

typedef struct struct_4 {
    char padding_0[96];
    unsigned long long field_60;
} struct_4;

typedef struct struct_2 {
    char padding_0[96];
    unsigned long long field_60;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0e48;
extern long long g_1efcf38;
extern long long g_1efcf70;
extern long long g_1efebb8;
extern char g_1fab462;

void DrinkPickup_Start(struct_3 *addr)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    struct_3 *v13;  // x19
    unsigned long long v5;  // x19
    long long v6;  // x1
    struct_3 *ptr;  // x0
    struct_1 *ptr3;  // x0
    long long v9;  // x1
    struct_3 *p;  // x20
    struct_3 *v11;  // x20
    struct_4 *v12;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab462 & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efcf70);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1ef0e48);
        g_1fab462 = 1;
    }
    v6 = Component__get_transform(addr, 0);
    ptr = addr;
    ptr->field_28 = v6;
    sub_f7d8d0(&ptr->field_28, v6);
    if (Camera__get_main(0) && Component__get_transform())
    {
        ptr3 = sub_1231bc8();
        if (ptr3)
        {
            v9 = ptr3->field_28;
            p = addr;
            p->field_20 = v9;
            v11 = &p->field_20;
            sub_f7d8d0(v11, v9);
            if (*((long long *)&v11->padding_0[0]))
            {
                v12 = sub_1249224(*((long long *)&v11->padding_0[0]), g_1efebb8);
                addr->field_50 = v12;
                v13 = &addr->field_50;
                sub_f7d8d0(v13, v12);
                if (v13->field_28)
                {
                    sub_1231bc8(v13->field_28, g_1efcf70);
                    if (*((long long *)&v13->padding_0[0]) && *((long long *)(*((long long *)&v13->padding_0[0]) + 96)))
                    {
                        if (!g_1ef0e48->field_e0)
                            sub_f7da5c(g_1ef0e48);
                        Physics__IgnoreCollision();
                        return;
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `DrinkPickup.PickUpItem` — RVA `0xc936a8`

- Decompiled symbol: `DrinkPickup_PickUpItem`
- Metadata signature: `public void PickUpItem() { }`
- Native interval: `444` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DrinkPickup_Recovered` matched 7 offsets against `DrinkPickup` metadata (confidence 1.00).

```c
typedef struct DrinkPickup_Recovered {
    char padding_0[40];
    struct struct_1 *myTransform;
    char removeOnUse;
    char padding_31[7];
    long long pickupSound;
    long long fullSound;
    unsigned int thirstToRemove;
    unsigned int healthToRestore;
    struct struct_1 *FPSPlayerComponent;
} DrinkPickup_Recovered;

typedef struct struct_3 {
    char padding_0[524];
    unsigned int field_20c;
    unsigned int field_210;
    char padding_214[56];
    char field_24c;
    char padding_24d[11];
    unsigned int field_258;
} struct_3;

typedef struct struct_1 {
    char padding_0[524];
    unsigned int field_20c;
    unsigned int field_210;
    char padding_214[56];
    char field_24c;
    char padding_24d[11];
    unsigned int field_258;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab463;

long long DrinkPickup_PickUpItem(struct_2 *ptr)
{
    struct_3 *p;  // x0
    unsigned int v1;  // s0
    unsigned long long v10;  // x0
    long long v11;  // x0
    unsigned long long v12;  // x0
    unsigned long v2;  // 4133
    unsigned int v3;  // w8
    unsigned int v4;  // s1
    unsigned long v5;  // 4186
    unsigned int v6;  // s2
    unsigned int v7;  // s3
    unsigned long v8;  // 4183
    long long v9;  // x0

    if (!(g_1fab463 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab463 = 1;
    }
    p = ptr->field_50;
    if (p)
    {
        v1 = p->field_258;
        v2 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v2) && p->field_24c)
        {
            v3 = ptr->field_48;
            v4 = v1 - ptr->field_48;
            v5 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1 - v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1 - v3, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v1 - v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1 - v3, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            FPSPlayer__UpdateThirst();
            p = ptr->field_50;
            if (p)
            {
                v6 = p->field_210;
                v7 = p->field_20c + ptr->field_4c;
                v8 = arm64g_calculate_condition(64, (((((unsigned long long)(char)(CmpF(v7, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v7, v6) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v7, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v7, v6) & 1)) & ((unsigned long long)(char)(CmpF(v7, v6)) >> 5 & 3 | (unsigned long long)(CmpF(v7, v6) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                FPSPlayer__HealPlayer();
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v9 = Object__op_Implicit(ptr->field_38, 0);
                if (((char)v9 & 1))
                {
                    p = ptr->field_28;
                    if (p)
                    {
                        Transform__get_position(p, 0);
                        v9 = PlayAudioAtPos__PlayClipAt(ptr->field_38);
                        goto LABEL_10937ac;
                    }
                }
                else
                {
LABEL_10937ac:
                    if (!ptr->field_30)
                        return v9;
                    DrinkPickup__FreePooledObjects();
                    Component__get_gameObject(ptr, 0);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    v10 = Object__Destroy();
                    return Object__Destroy();
                }
            }
        }
        else
        {
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v11 = Object__op_Implicit(ptr->field_40, 0);
            if (!((char)v11 & 1))
                return v11;
            p = ptr->field_28;
            if (p)
            {
                Transform__get_position(p, 0);
                v12 = PlayAudioAtPos__PlayClipAt();
                return PlayAudioAtPos__PlayClipAt();
            }
        }
    }
    sub_f7db74(p);
}
```

## `DrinkPickup.FreePooledObjects` — RVA `0xc93864`

- Decompiled symbol: `DrinkPickup_FreePooledObjects`
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
extern char g_1fab464;

void DrinkPickup_FreePooledObjects(long long a0)
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

    if (!(g_1fab464 & 1))
    {
        sub_f7d92c("s.");
        sub_f7d92c(&g_1efedb0);
        sub_f7d92c(&g_1efedb8);
        sub_f7d92c("s%");
        g_1fab464 = 1;
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
                    goto LABEL_1093a4c;
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
LABEL_1093a4c:
    sub_f7db7c(sub_f7db74());
}
```

## `DrinkPickup.ctor` — RVA `0xc93a54`

- Decompiled symbol: `DrinkPickup_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `28` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DrinkPickup_Recovered` matched 2 offsets against `DrinkPickup` metadata (confidence 1.00).

```c
typedef struct DrinkPickup_Recovered {
    char padding_0[48];
    char removeOnUse;
    char padding_31[23];
    unsigned long long thirstToRemove;
} DrinkPickup_Recovered;

long long DrinkPickup_ctor(struct_0 *ptr)
{
    ptr->field_30 = 1;
    ptr->field_48 = 21474836495;
}
```
