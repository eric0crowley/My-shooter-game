# Native pseudocode: GunActivator

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GunActivator.Update` — RVA `0xc68044`

- Decompiled symbol: `GunActivator_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `340` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GunActivator_Recovered` matched 3 offsets against `GunActivator` metadata (confidence 1.00).

```c
typedef struct GunActivator_Recovered {
    char padding_0[32];
    struct struct_2 *gunList;
    long long buttonName;
    unsigned int key;
} GunActivator_Recovered;

typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

typedef struct struct_4 {
    char padding_0[64];
    char field_40;
} struct_4;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed00;
extern struct_1 *g_1ef0c58;
extern char g_1fab314;

long long GunActivator_Update(struct_3 *ptr)
{
    unsigned long v0;  // x0
    unsigned long long v1;  // x20
    struct_2 *p;  // x8
    unsigned long long v3;  // x22
    unsigned int v4;  // w24
    unsigned long v5;  // x9
    struct_4 *addr;  // x21
    unsigned long v7;  // x0

    if (!(g_1fab314 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        g_1fab314 = 1;
    }
    if (ptr->field_30)
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        v0 = CF2Input__GetKey(ptr->field_30, 0);
        if (!(v0 & 1))
            goto LABEL_10680bc;
        v1 = 1;
    }
    else
    {
LABEL_10680bc:
        v0 = String__IsNullOrEmpty(ptr->field_28, 0);
        if (((char)v0 & 1))
        {
            v1 = 0;
        }
        else
        {
            if (!g_1eeed00->field_e0)
                sub_f7da5c(g_1eeed00);
            v0 = CF2Input__GetButton(ptr->field_28, 0);
            v1 = v0 & 4294967295;
        }
    }
    p = ptr->field_20;
    if (p)
    {
        v3 = 0;
        v4 = (unsigned int)v1 & 1;
        do
        {
            v5 = p->field_18;
            if ((v5 & 4294967295) <= v3)
                return v0;
            if (v5 <= v3)
                sub_f7db7c();
            addr = *((long long *)&p[1].padding_0[4 + 8 * v3]);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (!(Object__op_Inequality(addr, 0, 0) & 1))
                continue;
            if (!addr)
                break;
            if (addr->field_40 != v4)
            {
                addr->field_40 = v4;
                if (((char)v1 & 1))
                    v0 = Gun__FireBullet(addr);
            }
        } while ((p = (struct_2 *)ptr->field_20, v3 += 1, p));
    }
    v7 = sub_f7db74();
    return sub_f7db74();
}
```

## `GunActivator.ctor` — RVA `0xc68198`

- Decompiled symbol: `GunActivator_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

extern long long g_1f0a440;
extern char g_1fab315;

void GunActivator_ctor(struct_0 *ptr)
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
    if (!(g_1fab315 & 1))
    {
        sub_f7d92c(&g_1f0a440);
        g_1fab315 = 1;
    }
    ptr->field_28 = g_1f0a440;
    sub_f7d8d0((struct struct_0 *)&ptr->field_28, g_1f0a440);
    MonoBehaviour__ctor();
    return;
}
```
