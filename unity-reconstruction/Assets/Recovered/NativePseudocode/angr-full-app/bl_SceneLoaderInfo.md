# Native pseudocode: bl_SceneLoaderInfo

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_SceneLoaderInfo.ctor` — RVA `0xce81c0`

- Decompiled symbol: `bl_SceneLoaderInfo_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `184` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_SceneLoaderInfo_Recovered` matched 5 offsets against `bl_SceneLoaderInfo` metadata (confidence 1.00).

```c
typedef struct bl_SceneLoaderInfo_Recovered {
    char padding_0[16];
    long long SceneName;
    long long DisplayName;
    long long Description;
    unsigned int SkipType;
    char padding_2c[4];
    unsigned int FakeLoadingTime;
} bl_SceneLoaderInfo_Recovered;

extern long long g_1f06220;
extern long long g_1f09b20;
extern long long g_1f0d7f8;
extern char g_1fab66c;

void bl_SceneLoaderInfo_ctor(struct_0 *ptr)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    struct_0 *p;  // x0
    struct_0 *addr;  // x0
    struct_0 *ptr3;  // x0
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]
    unsigned long long v5;  // [bp-0x8]

    v0 = v6;
    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    if (!(g_1fab66c & 1))
    {
        sub_f7d92c(&g_1f0d7f8);
        sub_f7d92c(&g_1f06220);
        sub_f7d92c(&g_1f09b20);
        g_1fab66c = 1;
    }
    p = ptr;
    p->field_10 = g_1f0d7f8;
    sub_f7d8d0((struct bl_SceneLoaderInfo_Recovered *)&p->field_10, g_1f0d7f8);
    addr = ptr;
    addr->field_18 = g_1f09b20;
    sub_f7d8d0((struct bl_SceneLoaderInfo_Recovered *)&addr->field_18, g_1f09b20);
    ptr3 = ptr;
    ptr3->field_20 = g_1f06220;
    sub_f7d8d0((struct bl_SceneLoaderInfo_Recovered *)&ptr3->field_20, g_1f06220);
    ptr->field_28 = 3;
    ptr->field_30 = 0x40000000;
    Object__ctor();
    return;
}
```
