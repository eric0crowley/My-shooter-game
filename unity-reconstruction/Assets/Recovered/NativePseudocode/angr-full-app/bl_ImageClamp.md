# Native pseudocode: bl_ImageClamp

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_ImageClamp.Awake` — RVA `0xc781c8`

- Decompiled symbol: `bl_ImageClamp_Awake`
- Metadata signature: `private void Awake() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

extern long long g_1efd058;
extern char g_1fab3b4;

void bl_ImageClamp_Awake(struct_0 *ptr)
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
    if (!(g_1fab3b4 & 1))
    {
        sub_f7d92c(&g_1efd058);
        g_1fab3b4 = 1;
    }
    ptr->field_28 = sub_1231bc8(ptr, g_1efd058);
    sub_f7d8d0();
    return;
}
```

## `bl_ImageClamp.Update` — RVA `0xc78220`

- Decompiled symbol: `bl_ImageClamp_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `188` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_ImageClamp_Recovered` matched 2 offsets against `bl_ImageClamp` metadata (confidence 1.00).

```c
typedef struct bl_ImageClamp_Recovered {
    char padding_0[32];
    unsigned int m_Direction;
    char padding_24[4];
    unsigned long long m_Image;
} bl_ImageClamp_Recovered;

void bl_ImageClamp_Update(struct_0 *ptr)
{
    unsigned long long v7;  // d11
    unsigned long long v8;  // d10
    unsigned long long v9;  // d9
    unsigned long long v10;  // d8
    unsigned long long v11;  // x30
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    unsigned int flag;  // w20
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x38]
    unsigned long long v2;  // [bp-0x30]
    unsigned long long v3;  // [bp-0x28]
    unsigned long long v4;  // [bp-0x20]
    unsigned long long v5;  // [bp-0x10]
    unsigned long long v6;  // [bp-0x8]

    v0 = v7;
    v1 = v8;
    v2 = v9;
    v3 = v10;
    v4 = v11;
    v5 = v12;
    v6 = v13;
    if (ptr->field_28)
    {
        flag = ptr->field_20;
        if (!flag)
        {
            Time__get_deltaTime(0);
        }
        else if (flag == 1)
        {
            Time__get_deltaTime(0);
        }
        else
        {
            Time__get_deltaTime(0);
        }
    }
    sub_f7db74();
}
```

## `bl_ImageClamp.ctor` — RVA `0xc782dc`

- Decompiled symbol: `bl_ImageClamp_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned int field_20;
} struct_0;

long long bl_ImageClamp_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_20 = 1;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
