# Native pseudocode: AntialiasingModel.FxaaConsoleSettings

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AntialiasingModel.FxaaConsoleSettings.cctor` — RVA `0xcdafac`

- Decompiled symbol: `AntialiasingModel_FxaaConsoleSettings_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `228` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    uint128_t field_20;
    uint128_t field_30;
    uint128_t field_40;
    uint128_t field_50;
    uint128_t field_60;
} struct_3;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    uint128_t field_20;
    uint128_t field_30;
    uint128_t field_40;
    uint128_t field_50;
    uint128_t field_60;
} struct_0;

typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_1;

extern long long g_1eee4b0;
extern struct_1 *g_1ef2bd0;
extern char g_1fab606;

void AntialiasingModel_FxaaConsoleSettings_cctor(void)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_3 *p;  // x0
    unsigned int flag;  // w8
    struct_3 *ptr;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab606 & 1))
    {
        sub_f7d92c(&g_1eee4b0);
        sub_f7d92c(&g_1ef2bd0);
        g_1fab606 = 1;
    }
    p = sub_f7d9d4(g_1eee4b0, 5);
    if (p)
    {
        flag = p->field_18;
        ptr = p;
        if (flag)
        {
            ptr->field_20 = 81694352611761604162050630799969547715;
            if (flag != 1)
            {
                ptr->field_30 = 81694352611606861657139958265607157187;
                if (flag > 2)
                {
                    ptr->field_40 = 0x3d4ccccd3e000000410000003f000000;
                    if (flag != 3)
                    {
                        ptr->field_50 = 0x3d23d70a3e000000408000003f000000;
                        if (flag > 4)
                        {
                            ptr->field_60 = 0x3d23d70a3e000000400000003f000000;
                            g_1ef2bd0->field_b8->field_0 = ptr;
                            sub_f7d8d0();
                            return;
                        }
                    }
                }
            }
        }
        sub_f7db7c();
    }
    sub_f7db74();
}
```
