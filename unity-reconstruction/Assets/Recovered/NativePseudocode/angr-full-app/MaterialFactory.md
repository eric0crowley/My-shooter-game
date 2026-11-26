# Native pseudocode: MaterialFactory

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MaterialFactory.ctor` — RVA `0xcdf364`

- Decompiled symbol: `MaterialFactory_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

extern long long g_1eec670;
extern long long g_1ef5900;
extern char g_1fab629;

void MaterialFactory_ctor(struct_0 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x0
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x20]
    unsigned long long v2;  // [bp-0x18]
    unsigned long long v3;  // [bp-0x10]
    unsigned long long v4;  // [bp-0x8]

    v0 = v5;
    v1 = v6;
    v2 = v7;
    v3 = v8;
    v4 = v9;
    if (!(g_1fab629 & 1))
    {
        sub_f7d92c(&g_1ef5900);
        sub_f7d92c(&g_1eec670);
        g_1fab629 = 1;
    }
    Object__ctor(ptr, 0);
    v10 = sub_f7db70(g_1eec670);
    sub_12b0eec(v10, g_1ef5900);
    ptr->field_10 = v10;
    sub_f7d8d0();
    return;
}
```

## `MaterialFactory.Get` — RVA `0xcdf3ec`

- Decompiled symbol: `MaterialFactory_Get`
- Metadata signature: `public Material Get(string shaderName) { }`
- Native interval: `500` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    unsigned long long field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eee8a8;
extern struct_0 *g_1ef0c58;
extern long long g_1ef5908;
extern long long g_1ef5920;
extern long long g_1eff8f0;
extern long long g_1f075e0;
extern long long g_1f0cff0;
extern long long g_1f0d9e8;
extern char g_1fab62a;

long long MaterialFactory_Get(struct_1 *ptr, long long a1)
{
    unsigned long long v1;  // x0
    long long v2;  // x22
    unsigned long v3;  // x21
    long long v4;  // x0
    long long v5;  // x0
    long long v6;  // x0
    unsigned long v0;  // [bp-0x28]

    if (!(g_1fab62a & 1))
    {
        sub_f7d92c(&g_1ef5908);
        sub_f7d92c(&g_1ef5920);
        sub_f7d92c("7F");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f075e0);
        sub_f7d92c(&g_1f0cff0);
        g_1fab62a = 1;
    }
    v0 = 0;
    v1 = ptr->field_10;
    if (v1)
    {
        if (((char)sub_12b29e0(v1, a1, &v0, g_1ef5920) & 1))
            return v0;
        v2 = Shader__Find(a1, 0);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if ((Object__op_Equality(v2, 0, 0) & 1))
            goto LABEL_10df58c;
        v3 = sub_f7db70(g_1ef07c0);
        v1 = Material__ctor(v3, v2, 0);
        if (a1)
        {
            v4 = String__Substring(a1, String__LastIndexOf(a1, g_1f075e0, 0) + 1, 0);
            v1 = String__Format(g_1f0cff0, v4, 0);
            if (v3)
            {
                Object__set_name(v3, v1, 0);
                Object__set_hideFlags(v3, 52, 0);
                v0 = v3;
                v1 = ptr->field_10;
                if (v1)
                {
                    sub_12b11d4(v1, a1, v3, g_1ef5908);
                    return v0;
                }
            }
        }
    }
    sub_f7db74(v1);
LABEL_10df58c:
    v5 = String__Format(sub_f7d940(&g_1f0d9e8), a1, 0);
    v6 = sub_f7db70(sub_f7d940(&g_1eee8a8));
    ArgumentException__ctor(v6, v5, 0);
    sub_f7da4c(v6, sub_f7d940(&g_1eff8f0));
}
```

## `MaterialFactory.Dispose` — RVA `0xcdf5e0`

- Decompiled symbol: `MaterialFactory_Dispose`
- Metadata signature: `public void Dispose() { }`
- Native interval: `216` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

extern long long g_1ef5910;
extern long long g_1ef5918;
extern long long g_1ef67f0;
extern long long g_1ef67f8;
extern long long g_1ef70e8;
extern char g_1fab62b;

long long MaterialFactory_Dispose(struct_0 *ptr)
{
    unsigned long long v3;  // x0
    unsigned long long v4;  // x0
    int choice;  // [bp-0x50]
    uint128_t flag2;  // [bp-0x40]
    unsigned long long flag;  // [bp-0x30]

    if (!(g_1fab62b & 1))
    {
        sub_f7d92c(&g_1ef5910);
        sub_f7d92c(&g_1ef5918);
        sub_f7d92c(&g_1ef67f0);
        sub_f7d92c(&g_1ef67f8);
        sub_f7d92c(&g_1ef70e8);
        g_1fab62b = 1;
    }
    flag = 0;
    choice = 0;
    flag2 = 0;
    v3 = ptr->field_10;
    if (v3)
    {
        sub_12b1604(v3, g_1ef5918);
        while (((char)sub_1329144(&choice, g_1ef67f0) & 1))
        {
            GraphicsUtils__Destroy(*((unsigned long long *)((void*)&flag2 + 8)));
        }
        v3 = ptr->field_10;
        if (v3)
        {
            v4 = sub_12b135c(v3, g_1ef5910);
            return sub_12b135c(v3, g_1ef5910);
        }
    }
    sub_f7db74(v3);
}
```
