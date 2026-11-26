# Native pseudocode: LevelData

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `LevelData.FindInteractiveObjectFor` — RVA `0xc65f10`

- Decompiled symbol: `LevelData_FindInteractiveObjectFor`
- Metadata signature: `public InteractiveObjectBase FindInteractiveObjectFor(CharacterAction chara) { }`
- Native interval: `448` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

typedef struct struct_3 {
    char padding_0[392];
    struct struct_4 *field_188;
    unsigned long long field_190;
} struct_3;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef7f00;
extern long long g_1ef7f08;
extern unsigned long long g_1fab000;
extern char g_1fab301;

unsigned long long LevelData_FindInteractiveObjectFor(struct_2 *ptr, unsigned long long a1)
{
    unsigned long long v0;  // x21
    struct_1 *v1;  // x0
    int v2;  // w22
    struct_3 **v3;  // x23
    struct_3 **v4;  // x0
    unsigned long long v5;  // x1
    unsigned long v6;  // x2

    v0 = &g_1fab000;
    if (!(g_1fab301 & 1))
    {
        sub_f7d92c(&g_1ef7f00);
        sub_f7d92c(&g_1ef7f08);
        sub_f7d92c(&g_1ef0c58);
        g_1fab301 = 1;
    }
    v1 = ptr->field_20;
    if (v1)
    {
        v0 = 0;
        v2 = 0;
        do
        {
            if (v1->field_18 <= v2)
                return 0;
            v3 = sub_14a30c0();
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (!((char)Object__op_Equality(v3, 0, 0) & 1))
            {
                if (v3)
                {
                    v4 = v3;
                    v5 = a1;
                    v6 = *(v3)->field_190;
                    *(v3)->field_188();
                }
                break;
            }
        } while ((v1 = (struct_1 *)ptr->field_20, v2 = (int)(v2 + 1), v1));
    }
    sub_f7db74(v1);
    return v0;
}
```

## `LevelData.ctor` — RVA `0xc66274`

- Decompiled symbol: `LevelData_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1eed6c8;
extern long long g_1ef7ef8;
extern char g_1fab300;

void LevelData_ctor(struct_0 *ptr)
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
    if (!(g_1fab300 & 1))
    {
        sub_f7d92c(&g_1ef7ef8);
        sub_f7d92c(&g_1eed6c8);
        g_1fab300 = 1;
    }
    MonoBehaviour__ctor(ptr, 0);
    v10 = sub_f7db70(g_1eed6c8);
    sub_14a2b64(v10, g_1ef7ef8);
    ptr->field_20 = v10;
    sub_f7d8d0();
    return;
}
```
