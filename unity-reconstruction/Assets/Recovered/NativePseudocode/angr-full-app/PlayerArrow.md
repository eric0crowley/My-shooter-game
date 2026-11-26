# Native pseudocode: PlayerArrow

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `PlayerArrow.Start` — RVA `0xc79e4c`

- Decompiled symbol: `PlayerArrow_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long PlayerArrow_Start(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `PlayerArrow.Update` — RVA `0xc79e50`

- Decompiled symbol: `PlayerArrow_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `592` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    struct struct_1 *field_0;
} struct_3;

typedef struct struct_5 {
    char padding_0[1512];
    struct struct_6 *field_5e8;
    unsigned long long field_5f0;
} struct_5;

typedef struct struct_1 {
    char padding_0[1512];
    struct struct_2 *field_5e8;
    unsigned long long field_5f0;
} struct_1;

typedef struct struct_6 {
    unsigned long long field_0;
} struct_6;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1f07670;
extern long long g_1f138a0;
extern char g_1fab3ce;
extern char g_1fab3e0;

void PlayerArrow_Update(struct_3 **ptr)
{
    struct_5 **v1;  // x0
    struct_5 **v2;  // x20
    long long v4;  // x0
    struct_5 **v5;  // x1
    struct_5 **v6;  // x0
    unsigned long v7;  // x2
    unsigned int v0;  // [bp-0x54]

    if (!(g_1fab3ce & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f138a0);
        sub_f7d92c(&g_1f07670);
        g_1fab3ce = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(ptr[5], 0, 0) & 1))
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!(Object__op_Inequality(ptr[6], 0, 0) & 1))
            goto LABEL_107a040;
        v1 = ptr[6];
        if (v1)
        {
            v1 = Transform__get_position(v1, 0);
            if (ptr[5])
            {
                v1 = Transform__InverseTransformPoint(ptr[5], 0);
                if (ptr[4])
                {
                    atan2f();
                    Transform__set_localEulerAngles(ptr[4], 0);
                    v1 = ptr[5];
                    if (v1)
                    {
                        v2 = ptr[7];
                        Transform__get_position(v1, 0);
                        v1 = ptr[6];
                        if (v1)
                        {
                            Transform__get_position(v1, 0);
                            if (!g_1fab3e0)
                            {
                                sub_f7d92c("_F");
                                g_1fab3e0 = 1;
                            }
                            if (!g_1ef07e8->field_e0)
                                sub_f7da5c(g_1ef07e8);
                            v0 = [D] unsupported_Iop_SqrtF32();
                            v4 = Single__ToString(&v0, g_1f07670, 0);
                            v1 = String__Concat(v4, g_1f138a0, 0);
                            if (v2)
                            {
                                v5 = v1;
                                v6 = v2;
                                v7 = *(v2)->field_5f0;
                                *(v2)->field_5e8();
                            }
                        }
                    }
                }
            }
        }
    }
    else
    {
LABEL_107a040:
        v1 = ptr[4];
        if (v1)
        {
            v1 = Component__get_gameObject(v1, 0);
            if (v1)
            {
                GameObject__SetActive();
                v1 = ptr[7];
                if (v1)
                {
                    v1 = Component__get_gameObject(v1, 0);
                    if (v1)
                    {
                        GameObject__SetActive();
                        return;
                    }
                }
            }
        }
    }
    sub_f7db74(v1);
}
```

## `PlayerArrow.ctor` — RVA `0xc7a0a0`

- Decompiled symbol: `PlayerArrow_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long PlayerArrow_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
