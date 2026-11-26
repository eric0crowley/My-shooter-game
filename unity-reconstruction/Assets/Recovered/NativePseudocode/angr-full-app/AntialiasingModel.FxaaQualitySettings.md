# Native pseudocode: AntialiasingModel.FxaaQualitySettings

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AntialiasingModel.FxaaQualitySettings.cctor` — RVA `0xcdae9c`

- Decompiled symbol: `AntialiasingModel_FxaaQualitySettings_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `272` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    unsigned long long field_20;
    unsigned int field_28;
    unsigned long long field_2c;
    unsigned int field_34;
    unsigned long long field_38;
    unsigned int field_40;
    unsigned long long field_44;
    unsigned int field_4c;
    unsigned long long field_50;
    unsigned int field_58;
} struct_3;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    unsigned long long field_20;
    unsigned int field_28;
    unsigned long long field_2c;
    unsigned int field_34;
    unsigned long long field_38;
    unsigned int field_40;
    unsigned long long field_44;
    unsigned int field_4c;
    unsigned long long field_50;
    unsigned int field_58;
} struct_0;

typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_1;

extern long long g_1eee4b8;
extern struct_1 *g_1ef2bd8;
extern char g_1fab605;

void AntialiasingModel_FxaaQualitySettings_cctor(void)
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
    if (!(g_1fab605 & 1))
    {
        sub_f7d92c(&g_1eee4b8);
        sub_f7d92c(&g_1ef2bd8);
        g_1fab605 = 1;
    }
    p = sub_f7d9d4(g_1eee4b8, 5);
    if (p)
    {
        flag = p->field_18;
        ptr = p;
        if (flag)
        {
            ptr->field_20 = 0x3eaa7efa00000000;
            ptr->field_28 = 1034590513;
            if (flag != 1)
            {
                *((unsigned long long *)&(&ptr->field_28)[1]) = 0x3e8000003e800000;
                *((unsigned int *)((char *)&ptr->field_2c + 4)) = 1034590513;
                if (flag > 2)
                {
                    *((unsigned long long *)&ptr->field_34) = 0x3e29fbe73f400000;
                    *((unsigned int *)&ptr->field_38) = 1034590513;
                    if (flag != 3)
                    {
                        (&ptr->field_40)[1] = 0x3d800000;
                        *((unsigned long long *)((char *)&ptr->field_38 + 4)) = 0x3e0000003f800000;
                        if (flag > 4)
                        {
                            ptr->field_44 = 0x3d8106253f800000;
                            ptr->field_4c = 1023383332;
                            g_1ef2bd8->field_b8->field_0 = ptr;
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
