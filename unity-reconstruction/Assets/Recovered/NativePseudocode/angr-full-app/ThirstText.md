# Native pseudocode: ThirstText

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ThirstText.Start` — RVA `0xc926e4`

- Decompiled symbol: `ThirstText_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `140` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[56];
    struct struct_3 *field_38;
} struct_2;

typedef struct struct_4 {
    char padding_0[680];
    struct struct_5 *field_2a8;
    unsigned long long field_2b0;
} struct_4;

typedef struct struct_0 {
    char padding_0[680];
    struct struct_1 *field_2a8;
    unsigned long long field_2b0;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_5 {
    unsigned long long field_0;
} struct_5;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1efd0b0;
extern char g_1fab457;

void ThirstText_Start(struct_2 *p)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    struct_4 **v8;  // x0
    struct_2 *ptr;  // x20
    struct_0 **v10;  // x0
    unsigned long long v11;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab457 & 1))
    {
        sub_f7d92c(&g_1efd0b0);
        g_1fab457 = 1;
    }
    v8 = sub_1231bc8(p, g_1efd0b0);
    p->field_38 = v8;
    ptr = &p->field_38;
    sub_f7d8d0(ptr, v8);
    v10 = *((long long *)&ptr->padding_0[0]);
    if (!*((long long *)&ptr->padding_0[0]))
        sub_f7db74(0);
    v11 = *((long long *)(*((long long *)*((long long *)&ptr->padding_0[0])) + 688));
    (*((long long *)(*((long long *)*((long long *)&ptr->padding_0[0])) + 680)))();
}
```

## `ThirstText.Update` — RVA `0xc92770`

- Decompiled symbol: `ThirstText_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `156` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ThirstText_Recovered` matched 3 offsets against `ThirstText` metadata (confidence 1.00).

```c
typedef struct ThirstText_Recovered {
    char padding_0[32];
    unsigned int thirstGui;
    unsigned int oldThirstGui;
    char padding_28[16];
    struct struct_3 *uiTextComponent;
} ThirstText_Recovered;

typedef struct struct_0 {
    char padding_0[1512];
    struct struct_1 *field_5e8;
    unsigned long long field_5f0;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern char g_1fab458;

struct_2 * ThirstText_Update(struct_2 *ptr)
{
    unsigned int v0;  // s0
    struct_2 *p;  // x0
    unsigned long long v10;  // x2
    unsigned int v2;  // s1
    unsigned int v3;  // 4105
    unsigned long v4;  // 4122
    struct_0 **v5;  // x20
    long long v6;  // x0
    unsigned long long v7;  // x0
    unsigned long long v8;  // x1
    struct_0 **v9;  // x0

    if (!(g_1fab458 & 1))
    {
        sub_f7d92c("w\"");
        g_1fab458 = 1;
    }
    v0 = ptr->field_20;
    p = &ptr->field_20;
    v2 = *((int *)&p->padding_0[4]);
    v3 = CmpF(v0, v2);
    v4 = (((CmpF(v0, v2) >> 5 & 3 | CmpF(v0, v2) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1;
    if ((char)((v4 - ((CmpF(v0, v2) >> 5 & 3 | CmpF(v0, v2) & 1) & (v3 >> 5 & 3 | CmpF(v0, v2) & 1) >> 1 & 1)) * 0x10000000 >> 30))
        return p;
    v5 = ptr->field_38;
    v6 = Single__ToString(p, 0);
    v7 = String__Concat(g_1f0ebd8, v6, 0);
    if (!v5)
        sub_f7db74();
    v8 = v7;
    v9 = v5;
    v10 = *(v5)->field_5f0;
    *(v5)->field_5e8();
}
```

## `ThirstText.ctor` — RVA `0xc9280c`

- Decompiled symbol: `ThirstText_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[36];
    unsigned int field_24;
} struct_0;

long long ThirstText_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_24 = 0xc4000000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
