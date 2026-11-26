# Native pseudocode: EdgeClimbTrigger

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `EdgeClimbTrigger.Start` — RVA `0xc95184`

- Decompiled symbol: `EdgeClimbTrigger_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned long long field_28;
} struct_0;

typedef struct struct_1 {
    char padding_0[40];
    unsigned long long field_28;
} struct_1;

extern long long g_1efcf38;
extern char g_1fab473;

void EdgeClimbTrigger_Start(struct_1 *ptr, unsigned long a1)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_0 *index;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab473 & 1))
    {
        sub_f7d92c(&g_1efcf38);
        g_1fab473 = 1;
    }
    if (Camera__get_main(0) && Component__get_transform())
    {
        index = sub_1231bc8();
        if (index)
        {
            ptr->field_28 = index->field_28;
            sub_f7d8d0();
            return;
        }
    }
    sub_f7db74();
}
```

## `EdgeClimbTrigger.OnTriggerStay` — RVA `0xc951f8`

- Decompiled symbol: `EdgeClimbTrigger_OnTriggerStay`
- Metadata signature: `private void OnTriggerStay(Collider other) { }`
- Native interval: `260` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

typedef struct struct_1 {
    char padding_0[196];
    unsigned int field_c4;
    char padding_c8[352];
    char field_228;
    char padding_229[108];
    unsigned short field_295;
    char padding_297[18];
    char field_2a9;
} struct_1;

extern long long g_1efebc0;
extern long long g_1efeca8;
extern long long g_1f0cf98;
extern char g_1fab474;

void EdgeClimbTrigger_OnTriggerStay(struct_0 *a0, long long a1)
{
    long long v0;  // x0
    struct_1 *v1;  // x0
    struct_1 *ptr;  // x20

    if (!(g_1fab474 & 1))
    {
        sub_f7d92c(&g_1efebc0);
        sub_f7d92c(&g_1efeca8);
        sub_f7d92c(&g_1f0cf98);
        g_1fab474 = 1;
    }
    if (a1 && Component__get_gameObject(a1, 0))
    {
        v0 = GameObject__get_tag();
        if (!((char)String__op_Equality(v0, g_1f0cf98, 0) & 1))
        {
            return;
        }
        else if (a0->field_28)
        {
            v1 = sub_1249224(a0->field_28, g_1efebc0);
            if (a0->field_28)
            {
                ptr = v1;
                if (sub_1249224(a0->field_28, g_1efeca8))
                {
                    Rigidbody__AddForce();
                    if (ptr)
                    {
                        *((unsigned short *)&(&ptr->padding_229)[1]) = 257;
                        ptr->field_c4 = 0x3f800000;
                        ptr->field_228 = 1;
                        ptr->padding_297[17] = 0;
                        return;
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `EdgeClimbTrigger.OnTriggerExit` — RVA `0xc952fc`

- Decompiled symbol: `EdgeClimbTrigger_OnTriggerExit`
- Metadata signature: `private void OnTriggerExit(Collider other) { }`
- Native interval: `244` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

typedef struct struct_1 {
    char padding_0[661];
    unsigned short field_295;
} struct_1;

extern long long g_1efeb40;
extern long long g_1efebc0;
extern long long g_1f0cf98;
extern char g_1fab475;

void EdgeClimbTrigger_OnTriggerExit(struct_0 *a0, long long a1)
{
    long long v0;  // x0
    struct_1 *ptr;  // x0

    if (!(g_1fab475 & 1))
    {
        sub_f7d92c(&g_1efeb40);
        sub_f7d92c(&g_1efebc0);
        sub_f7d92c(&g_1f0cf98);
        g_1fab475 = 1;
    }
    if (a1 && Component__get_gameObject(a1, 0))
    {
        v0 = GameObject__get_tag();
        if (!((char)String__op_Equality(v0, g_1f0cf98, 0) & 1))
        {
            return;
        }
        else if (a0->field_28)
        {
            ptr = sub_1249224(a0->field_28, g_1efebc0);
            if (ptr)
            {
                *((unsigned short *)&(&ptr->padding_0)[1]) = 0;
                if (Component__get_transform(a0, 0) && Component__get_gameObject() && sub_1249224())
                {
                    Collider__set_enabled();
                    return;
                }
            }
        }
    }
    sub_f7db74();
}
```

## `EdgeClimbTrigger.ctor` — RVA `0xc953f0`

- Decompiled symbol: `EdgeClimbTrigger_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned int field_20;
} struct_0;

long long EdgeClimbTrigger_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_20 = 1050253722;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
