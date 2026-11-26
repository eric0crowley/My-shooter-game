# Native pseudocode: SpecularLighting

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SpecularLighting.Start` — RVA `0xce33f8`

- Decompiled symbol: `SpecularLighting_Start`
- Metadata signature: `public void Start() { }`
- Native interval: `296` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[40];
    struct struct_2 *field_28;
} struct_1;

typedef struct struct_3 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_3;

typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_0;

typedef struct struct_5 {
    char padding_0[304];
    char field_130;
} struct_5;

typedef struct struct_4 {
    char padding_0[224];
    unsigned int field_e0;
} struct_4;

extern long long g_1eebbf8;
extern struct_4 *g_1ef1f08;
extern struct_5 *g_1ef2470;
extern char g_1fab64d;

void SpecularLighting_Start(struct_1 *a0)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long v15;  // x10
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    struct_1 *cur;  // x19
    long long v11;  // x20
    long long v12;  // x0
    struct_3 **v13;  // x8
    unsigned long v14;  // x9
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
    cur = a0;
    if (!(g_1fab64d & 1))
    {
        sub_f7d92c(&g_1ef1f08);
        sub_f7d92c(&g_1eebbf8);
        sub_f7d92c(&g_1ef2470);
        g_1fab64d = 1;
    }
    v11 = Component__get_gameObject(cur, 0);
    if (!g_1ef1f08->field_e0)
        sub_f7da5c(g_1ef1f08);
    v12 = Type__GetTypeFromHandle(g_1eebbf8, 0);
    if (v11)
    {
        v13 = GameObject__GetComponent(v11, v12, 0);
        if (v13)
        {
            v14 = g_1ef2470->field_130;
            if (*(v13)->field_130 >= (unsigned int)v14 && !((v15 = (unsigned long)(v14 - 1), *((long long *)(*(v13)->field_c8 + v15 * 8)) != g_1ef2470 || (cur->field_28 = (struct struct_2 *)v13, cur += 40, (unsigned int)*(v13)->field_130 < (unsigned int)v14 || *((long long *)(*(v13)->field_c8 + v15 * 8)) != g_1ef2470))))
                goto LABEL_10e3504;
            sub_f7df10(v13);
        }
        cur->field_28 = v13;
LABEL_10e3504:
        sub_f7d8d0();
        return;
    }
    sub_f7db74();
}
```

## `SpecularLighting.Update` — RVA `0xce3520`

- Decompiled symbol: `SpecularLighting_Update`
- Metadata signature: `public void Update() { }`
- Native interval: `536` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SpecularLighting_Recovered` matched 2 offsets against `SpecularLighting` metadata (confidence 1.00).

```c
typedef struct SpecularLighting_Recovered {
    char padding_0[32];
    long long specularLight;
    struct struct_4 *m_WaterBase;
} SpecularLighting_Recovered;

typedef struct struct_7 {
    struct struct_6 *field_0;
    char padding_8[24];
    unsigned long long field_20;
} struct_7;

typedef struct struct_4 {
    struct struct_3 *field_0;
    char padding_8[24];
    long long field_20;
} struct_4;

typedef struct struct_6 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_6;

typedef struct struct_3 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_2 {
    char padding_0[304];
    char field_130;
} struct_2;

extern long long g_1eebbf8;
extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef1f08;
extern struct_2 *g_1ef2470;
extern char g_1fab64e;

long long SpecularLighting_Update(struct_5 *a0)
{
    struct_5 *ptr;  // x20
    long long v1;  // x21
    long long v2;  // x0
    struct_7 *v3;  // x8
    unsigned long v4;  // x9
    unsigned long v5;  // x10
    long long v6;  // x0
    long long v7;  // x0
    unsigned long long v8;  // x0

    if (!(g_1fab64e & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef1f08);
        sub_f7d92c(&g_1eebbf8);
        sub_f7d92c(&g_1ef2470);
        sub_f7d92c("?*");
        g_1fab64e = 1;
    }
    ptr = &a0->field_28;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Implicit(a0->field_28, 0) & 1))
    {
        v1 = Component__get_gameObject(a0, 0);
        if (!g_1ef1f08->field_e0)
            sub_f7da5c(g_1ef1f08);
        v2 = Type__GetTypeFromHandle(g_1eebbf8, 0);
        if (!v1)
            sub_f7db74();
        v3 = GameObject__GetComponent(v1, v2, 0);
        if (v3)
        {
            v4 = g_1ef2470->field_130;
            if (v3->field_0->field_130 >= (unsigned int)v4 && !((v5 = (unsigned long)(v4 - 1), *((long long *)(v3->field_0->field_c8 + v5 * 8)) != g_1ef2470 || (*((struct_7 **)&ptr->padding_0[0]) = v3, (unsigned int)v3->field_0->field_130 < (unsigned int)v4 || *((long long *)(v3->field_0->field_c8 + v5 * 8)) != g_1ef2470))))
                goto LABEL_10e3674;
            sub_f7df10(v3);
        }
        *((struct_7 **)&ptr->padding_0[0]) = v3;
LABEL_10e3674:
        sub_f7d8d0(ptr, v3);
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v6 = Object__op_Implicit(a0->field_20, 0);
    if (!((char)v6 & 1))
        return v6;
    if (*((long long *)&ptr->padding_0[0]))
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v7 = Object__op_Implicit(*((long long *)(*((long long *)&ptr->padding_0[0]) + 32)), 0);
        if (!((char)v7 & 1))
        {
            return v7;
        }
        else if (*((long long *)&ptr->padding_0[0]) && a0->field_20 && Component__get_transform(a0->field_20, 0))
        {
            Transform__get_forward();
            if (*((long long *)(*((long long *)&ptr->padding_0[0]) + 32)))
            {
                v8 = Material__SetVector();
                return Material__SetVector();
            }
        }
    }
    sub_f7db74();
}
```

## `SpecularLighting.ctor` — RVA `0xce3738`

- Decompiled symbol: `SpecularLighting_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long SpecularLighting_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
