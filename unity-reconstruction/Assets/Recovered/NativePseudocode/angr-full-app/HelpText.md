# Native pseudocode: HelpText

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `HelpText.Start` — RVA `0xc91400`

- Decompiled symbol: `HelpText_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `308` bytes
- Result: `pseudocode`
- Heuristic layout hint: `HelpText_Recovered` matched 2 offsets against `HelpText` metadata (confidence 1.00).

```c
typedef struct HelpText_Recovered {
    char padding_0[72];
    long long playerObj;
    struct struct_5 *uiTextComponent;
} HelpText_Recovered;

typedef struct struct_0 {
    char padding_0[1512];
    struct struct_1 *field_5e8;
    unsigned long long field_5f0;
} struct_0;

typedef struct struct_6 {
    char padding_0[40];
    long long field_28;
} struct_6;

typedef struct struct_2 {
    char padding_0[1512];
    struct struct_3 *field_5e8;
    unsigned long long field_5f0;
} struct_2;

typedef struct struct_5 {
    struct struct_2 *field_0;
} struct_5;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

typedef struct struct_3 {
    unsigned long long field_0;
} struct_3;

extern long long g_1efcf38;
extern long long g_1efd0b0;
extern unsigned long long g_1f0d058;
extern char g_1fab451;

void HelpText_Start(struct_4 *a0)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    struct_4 *v14;  // x21
    struct_2 **v15;  // x0
    unsigned long long v16;  // x2
    unsigned long long v17;  // x1
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    struct_0 **v8;  // x0
    struct_4 *p;  // x20
    struct_4 *ptr;  // x20
    struct_6 *addr;  // x0
    long long v12;  // x1
    struct_4 *ptr3;  // x21
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab451 & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efd0b0);
        sub_f7d92c(&g_1f0d058);
        g_1fab451 = 1;
    }
    v8 = sub_1231bc8(a0, g_1efd0b0);
    p = a0;
    p->field_50 = v8;
    ptr = &p->field_50;
    sub_f7d8d0(ptr, v8);
    if (Camera__get_main(0) && Component__get_transform())
    {
        addr = sub_1231bc8();
        if (addr)
        {
            v12 = addr->field_28;
            ptr3 = a0;
            ptr3->field_48 = v12;
            v14 = &ptr3->field_48;
            sub_f7d8d0(v14, v12);
            if (*((long long *)&v14->padding_0[8]))
            {
                Behaviour__set_enabled(*((long long *)&v14->padding_0[8]), 1, 0);
                v15 = *((long long *)&ptr->padding_0[0]);
                if (v15)
                {
                    v16 = *(v15)->field_5f0;
                    v17 = g_1f0d058;
                    *(v15)->field_5e8();
                }
            }
        }
    }
    sub_f7db74();
}
```

## `HelpText.Update` — RVA `0xc91534`

- Decompiled symbol: `HelpText_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `708` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[664];
    struct struct_1 *field_298;
    unsigned long long field_2a0;
} struct_0;

typedef struct struct_3 {
    char padding_0[664];
    struct struct_4 *field_298;
    unsigned long long field_2a0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

extern long long g_1efebc0;
extern long long g_1efec08;
extern long long g_1f0c380;
extern char g_1fab452;

void HelpText_Update(struct_2 **ptr)
{
    unsigned long long v10;  // d13
    unsigned long long v11;  // d12
    struct_0 **v20;  // x0
    struct_3 **v21;  // x0
    unsigned long long v23;  // x1
    unsigned long long v12;  // d11
    unsigned long long v13;  // d10
    unsigned long long v14;  // d9
    unsigned long long v15;  // d8
    unsigned long long v16;  // x30
    unsigned long long v17;  // x21
    unsigned long long v18;  // x20
    unsigned long long v19;  // x19
    unsigned long long v0;  // [bp-0x50]
    unsigned long long v1;  // [bp-0x48]
    unsigned long long v2;  // [bp-0x40]
    unsigned long long v3;  // [bp-0x38]
    unsigned long long v4;  // [bp-0x30]
    unsigned long long v5;  // [bp-0x28]
    unsigned long long v6;  // [bp-0x20]
    unsigned long long v7;  // [bp-0x18]
    unsigned long long v8;  // [bp-0x10]
    unsigned long long v9;  // [bp-0x8]

    v0 = v10;
    v1 = v11;
    v2 = v12;
    v3 = v13;
    v4 = v14;
    v5 = v15;
    v6 = v16;
    v7 = v17;
    v8 = v18;
    v9 = v19;
    if (!(g_1fab452 & 1))
    {
        sub_f7d92c(&g_1efebc0);
        sub_f7d92c(&g_1efec08);
        sub_f7d92c(&g_1f0c380);
        g_1fab452 = 1;
    }
    v20 = ptr[9];
    if (v20)
    {
        v21 = sub_1249224(v20, g_1efebc0);
        v20 = v21;
        if (ptr[9])
        {
            v20 = sub_1249224(ptr[9], g_1efec08);
            if (v21)
            {
                v20 = ptr[10];
                if (v20)
                {
                    v23 = *(v20)->field_2a0;
                    *(v20)->field_298();
                }
            }
        }
    }
    sub_f7db74(v20);
}
```

## `HelpText.ctor` — RVA `0xc917f8`

- Decompiled symbol: `HelpText_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `44` bytes
- Result: `pseudocode`
- Heuristic layout hint: `HelpText_Recovered` matched 4 offsets against `HelpText` metadata (confidence 1.00).

```c
typedef struct HelpText_Recovered {
    char padding_0[48];
    unsigned int horizontalOffset;
    char helpTextState;
    char padding_35[7];
    unsigned short initialHide;
    char padding_3e[6];
    unsigned int fadeTime;
} HelpText_Recovered;

long long HelpText_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_30 = 1026430075;
    ptr->field_34 = 1;
    ptr->field_3c = 257;
    ptr->field_44 = 0x40a00000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
