# Native pseudocode: RemoveBody

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `RemoveBody.Start` — RVA `0xc87884`

- Decompiled symbol: `RemoveBody_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned int field_20;
} struct_0;

int RemoveBody_Start(struct_0 *ptr)
{
    unsigned int v0;  // w0
    unsigned int v1;  // s0

    v0 = Time__get_time(0);
    ptr->field_20 = v1;
    return v0;
}
```

## `RemoveBody.FixedUpdate` — RVA `0xc878a0`

- Decompiled symbol: `RemoveBody_FixedUpdate`
- Metadata signature: `private void FixedUpdate() { }`
- Native interval: `488` bytes
- Result: `pseudocode`
- Heuristic layout hint: `RemoveBody_Recovered` matched 3 offsets against `RemoveBody` metadata (confidence 1.00).

```c
typedef struct RemoveBody_Recovered {
    char padding_0[32];
    unsigned int startTime;
    unsigned int bodyStayTime;
    struct struct_1 *GunPickup;
} RemoveBody_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

typedef struct struct_5 {
    char padding_0[32];
    struct struct_4 *field_20;
    char padding_28[9];
    char field_31;
    char padding_32[70];
    struct struct_4 *field_78;
} struct_5;

typedef struct struct_4 {
    char padding_0[24];
    unsigned int field_18;
} struct_4;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efedb0;
extern char g_1fab429;

int RemoveBody_FixedUpdate(struct_2 *ptr)
{
    unsigned int v0;  // w0
    unsigned int v1;  // s1
    unsigned int v2;  // s0
    unsigned long v3;  // 4138
    struct_1 *ptr3;  // x0
    int v5;  // w8
    struct_1 *addr;  // x20
    int i;  // w23
    struct_5 *p;  // x21

    if (!(g_1fab429 & 1))
    {
        sub_f7d92c(&g_1efedb0);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("s%");
        g_1fab429 = 1;
    }
    v0 = Time__get_time(0);
    v1 = ptr->field_20 + ptr->field_24;
    v3 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) & ((unsigned long long)(char)(CmpF(v1, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v1, v2) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v3)
        return v0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Implicit(ptr->field_28, 0) & 1))
    {
        ptr3 = ptr->field_28;
        if (!ptr3)
        {
            sub_f7db74(ptr3);
            sub_f7db7c(ptr3);
        }
        ptr3 = GameObject__get_transform(ptr3, 0);
        if (!ptr3)
        {
            sub_f7db74(ptr3);
            sub_f7db7c(ptr3);
        }
        Transform__set_parent();
    }
    ptr3 = Component__get_gameObject(ptr, 0);
    if (ptr3 && (ptr3 = (struct_1 *)(unsigned long long)sub_1249ec4(), ptr3))
    {
        v5 = ptr3->field_18;
        addr = ptr3;
        if (v5 >= 1)
        {
            i = 0;
            do
            {
                if (v5 <= i)
                    sub_f7db7c(ptr3);
                p = *((long long *)&addr[1].padding_0[4 + 8 * i]);
                if (!p)
                {
                    sub_f7db74(ptr3);
                    sub_f7db7c(ptr3);
                }
                ptr3 = Component__get_transform(p, 0);
                if (!ptr3)
                {
                    sub_f7db74(ptr3);
                    sub_f7db7c(ptr3);
                }
                Transform__set_parent();
                ptr3 = p->field_20;
                if (!ptr3)
                {
                    sub_f7db74(ptr3);
                    sub_f7db7c(ptr3);
                }
                Rigidbody__set_isKinematic(ptr3, 0, 0);
                ptr3 = p->field_78;
                if (!ptr3)
                    goto LABEL_1087a80;
                else
                    goto LABEL_10879e8;
LABEL_10879e8:
                Collider__set_isTrigger(ptr3, 0, 0);
                ptr3 = Component__get_gameObject(p, 0);
                if (!ptr3)
                {
                    sub_f7db74(ptr3);
                    sub_f7db7c(ptr3);
                }
                ptr3 = GameObject__set_tag();
                p->field_31 = 1;
                v5 = addr->field_18;
                i += 1;
            } while (i < v5);
            goto LABEL_1087a80;
        }
        Component__get_gameObject(ptr, 0);
        if (g_1ef0c58->field_e0)
            return Object__Destroy();
        sub_f7da5c(g_1ef0c58);
        return Object__Destroy();
    }
LABEL_1087a80:
    ptr3 = sub_f7db74(ptr3);
    sub_f7db7c(ptr3);
}
```

## `RemoveBody.ctor` — RVA `0xc87a88`

- Decompiled symbol: `RemoveBody_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[36];
    unsigned int field_24;
} struct_0;

long long RemoveBody_ctor(struct_0 *ptr)
{
    ptr->field_24 = 0x41700000;
}
```
