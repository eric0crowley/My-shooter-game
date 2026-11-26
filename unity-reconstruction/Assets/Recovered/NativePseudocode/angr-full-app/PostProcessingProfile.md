# Native pseudocode: PostProcessingProfile

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `PostProcessingProfile.ctor` — RVA `0xcde56c`

- Decompiled symbol: `PostProcessingProfile_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `924` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PostProcessingProfile_Recovered` matched 3 offsets against `PostProcessingProfile` metadata (confidence 0.75).

```c
typedef struct PostProcessingProfile_Recovered {
    char padding_0[20];
    unsigned int field_14;
    char padding_18[8];
    uint128_t debugViews;
    unsigned long long antialiasing;
    unsigned int ambientOcclusion;
} PostProcessingProfile_Recovered;

extern long long g_1eee748;
extern long long g_1eee818;
extern long long g_1eeebe0;
extern long long g_1eeec98;
extern long long g_1eef5e8;
extern long long g_1ef0a10;
extern long long g_1ef1538;
extern long long g_1ef21e0;
extern long long g_1ef2390;
extern char g_1fab622;

long long PostProcessingProfile_ctor(unsigned long a0)
{
    unsigned long long v13;  // x30
    unsigned long long v14;  // x28
    unsigned long long v23;  // x19
    unsigned long long v15;  // x27
    unsigned long long v16;  // x26
    unsigned long long v17;  // x25
    unsigned long long v18;  // x24
    unsigned long long v19;  // x23
    unsigned long long v20;  // x22
    unsigned long long v21;  // x21
    unsigned long long v22;  // x20
    char *v0;  // [bp-0x60]
    unsigned long long v1;  // [bp-0x58]
    unsigned long long v2;  // [bp-0x50]
    unsigned long long v3;  // [bp-0x48]
    unsigned long long v4;  // [bp-0x40]
    unsigned long long v5;  // [bp-0x38]
    unsigned long long v6;  // [bp-0x30]
    unsigned long long v7;  // [bp-0x28]
    unsigned long long v8;  // [bp-0x20]
    unsigned long long v9;  // [bp-0x18]
    unsigned long long v10;  // [bp-0x10]
    unsigned long long v11;  // [bp-0x8]
    char v12;  // [bp+0x0]

    v0 = &v12;
    v1 = v13;
    v2 = v14;
    v3 = v15;
    v4 = v16;
    v5 = v17;
    v6 = v18;
    v7 = v19;
    v8 = v20;
    v9 = v21;
    v10 = v22;
    v11 = v23;
    if (!(g_1fab622 & 1))
    {
        sub_f7d92c(&g_1eee748);
        sub_f7d92c(&g_1eee818);
        sub_f7d92c(&g_1eeebe0);
        sub_f7d92c(&g_1eeec98);
        sub_f7d92c("I2");
        sub_f7d92c("#3");
        sub_f7d92c("E7");
        sub_f7d92c(&g_1eef5e8);
        sub_f7d92c("i:");
        sub_f7d92c("[;");
        sub_f7d92c("S=");
        sub_f7d92c(&g_1ef0a10);
        sub_f7d92c(&g_1ef1538);
        sub_f7d92c(&g_1ef21e0);
        sub_f7d92c(&g_1ef2390);
        g_1fab622 = 1;
    }
    BuiltinDebugViewsModel__ctor(sub_f7db70(g_1eeec98)); /* do not return */
}
```
