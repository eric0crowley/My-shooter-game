# Native pseudocode: HealthPickup

> Metadata source-path string: `Assets/RFPSP/Scripts/Items/HealthPickup.cs`. This is a path string from the APK metadata, not recovered source text.

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `HealthPickup.Start` — RVA `0xc93f74`

- Decompiled symbol: `HealthPickup_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `296` bytes
- Result: `pseudocode`
- Heuristic layout hint: `HealthPickup_Recovered` matched 2 offsets against `HealthPickup` metadata (confidence 1.00).

```c
typedef struct HealthPickup_Recovered {
    char padding_0[32];
    long long myTransform;
    struct struct_1 *FPSPlayerComponent;
} HealthPickup_Recovered;

typedef struct struct_4 {
    char padding_0[40];
    long long field_28;
} struct_4;

typedef struct struct_3 {
    char padding_0[96];
    unsigned long long field_60;
} struct_3;

typedef struct struct_1 {
    char padding_0[96];
    unsigned long long field_60;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0e48;
extern long long g_1efcf38;
extern long long g_1efcf70;
extern long long g_1efebb8;
extern char g_1fab468;

void HealthPickup_Start(struct_2 *ptr)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    long long v6;  // x1
    struct_4 *v7;  // x0
    struct_3 *v8;  // x0
    struct_2 *v9;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab468 & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efcf70);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1ef0e48);
        g_1fab468 = 1;
    }
    v6 = Component__get_transform(ptr, 0);
    ptr->field_20 = v6;
    sub_f7d8d0(&ptr->field_20, v6);
    if (Camera__get_main(0) && Component__get_transform())
    {
        v7 = sub_1231bc8();
        if (v7 && v7->field_28)
        {
            v8 = sub_1249224(v7->field_28, g_1efebb8);
            ptr->field_28 = v8;
            v9 = &ptr->field_28;
            sub_f7d8d0(v9, v8);
            if (*((long long *)&v9->padding_0[8]))
            {
                sub_1231bc8(*((long long *)&v9->padding_0[8]), g_1efcf70);
                if (*((long long *)&v9->padding_0[0]) && *((long long *)(*((long long *)&v9->padding_0[0]) + 96)))
                {
                    if (!g_1ef0e48->field_e0)
                        sub_f7da5c(g_1ef0e48);
                    Physics__IgnoreCollision();
                    return;
                }
            }
        }
    }
    sub_f7db74();
}
```


## `HealthPickup.PickUpItem` — RVA `0xc9409c`

- Decompiled symbol: `HealthPickup_PickUpItem`
- Metadata signature: `private void PickUpItem(GameObject user) { }`
- Native interval: `432` bytes
- Result: `pseudocode`
- Heuristic layout hint: `HealthPickup_Recovered` matched 5 offsets against `HealthPickup` metadata (confidence 1.00).

```c
typedef struct HealthPickup_Recovered {
    char padding_0[32];
    long long myTransform;
    struct struct_2 *FPSPlayerComponent;
    char padding_30[4];
    char removeOnUse;
    char padding_35[3];
    long long pickupSound;
    long long fullSound;
} HealthPickup_Recovered;

typedef struct struct_2 {
    char padding_0[524];
    unsigned int field_20c;
    unsigned int field_210;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efebb8;
extern char g_1fab469;

long long HealthPickup_PickUpItem(struct_1 *addr, long long a1)
{
    unsigned int v0[133];  // x0
    struct_1 *p;  // x20
    unsigned int ptr[133];  // x0
    unsigned int v3;  // s0
    unsigned int v4;  // s1
    unsigned long v5;  // 4133
    long long v6;  // x0
    unsigned long long v7;  // x0
    long long v8;  // x0
    unsigned long long v9;  // x0

    if (!(g_1fab469 & 1))
    {
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1ef0c58);
        g_1fab469 = 1;
    }
    if (a1)
    {
        v0 = sub_1249224(a1, g_1efebb8);
        addr->field_28 = v0;
        p = &addr->field_28;
        sub_f7d8d0(p, v0);
        ptr = *((long long *)&p->padding_0[0]);
        if (ptr)
        {
            v3 = ptr[131];
            v4 = ptr[132];
            v5 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v3, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v4) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v4) & 1)) & ((unsigned long long)(char)(CmpF(v3, v4)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v4) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v5))
            {
                FPSPlayer__HealPlayer();
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v6 = Object__op_Implicit(addr->field_38, 0);
                if (!((char)v6 & 1))
                {
LABEL_109418c:
                    if (!addr->field_34)
                        return v6;
                    HealthPickup__FreePooledObjects();
                    Component__get_gameObject(addr, 0);
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    v7 = Object__Destroy();
                    return Object__Destroy();
                }
                else if (addr->field_20)
                {
                    Transform__get_position(addr->field_20, 0);
                    v6 = PlayAudioAtPos__PlayClipAt(addr->field_38);
                    goto LABEL_109418c;
                }
            }
            else
            {
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v8 = Object__op_Implicit(addr->field_40, 0);
                if (!((char)v8 & 1))
                {
                    return v8;
                }
                else if (addr->field_20)
                {
                    Transform__get_position(addr->field_20, 0);
                    v9 = PlayAudioAtPos__PlayClipAt();
                    return PlayAudioAtPos__PlayClipAt();
                }
            }
        }
    }
    sub_f7db74();
}
```


## `HealthPickup.FreePooledObjects` — RVA `0xc9424c`

- Decompiled symbol: `HealthPickup_FreePooledObjects`
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
extern char g_1fab46a;

void HealthPickup_FreePooledObjects(long long a0)
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

    if (!(g_1fab46a & 1))
    {
        sub_f7d92c("s.");
        sub_f7d92c(&g_1efedb0);
        sub_f7d92c(&g_1efedb8);
        sub_f7d92c("s%");
        g_1fab46a = 1;
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
                    goto LABEL_1094434;
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
LABEL_1094434:
    sub_f7db7c(sub_f7db74());
}
```


## `HealthPickup.ctor` — RVA `0xc9443c`

- Decompiled symbol: `HealthPickup_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `24` bytes
- Result: `pseudocode`
- Heuristic layout hint: `HealthPickup_Recovered` matched 2 offsets against `HealthPickup` metadata (confidence 1.00).

```c
typedef struct HealthPickup_Recovered {
    char padding_0[48];
    unsigned int healthToAdd;
    char removeOnUse;
} HealthPickup_Recovered;

long long HealthPickup_ctor(struct_0 *ptr)
{
    ptr->field_30 = 0x41c80000;
    ptr->field_34 = 1;
}
```
