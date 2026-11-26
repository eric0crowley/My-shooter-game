# Native pseudocode: AmmoText

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AmmoText.OnEnable` — RVA `0xc91100`

- Decompiled symbol: `AmmoText_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `100` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AmmoText_Recovered` matched 2 offsets against `AmmoText` metadata (confidence 1.00).

```c
typedef struct AmmoText_Recovered {
    char padding_0[44];
    unsigned long long oldAmmo;
    char padding_34[20];
    long long uiTextComponent;
} AmmoText_Recovered;

extern long long g_1efd0b0;
extern char g_1fab44d;

long long AmmoText_OnEnable(struct_0 *ptr)
{
    long long v0;  // x0
    struct_0 *p;  // x19
    unsigned long v2;  // x0

    if (!(g_1fab44d & 1))
    {
        sub_f7d92c(&g_1efd0b0);
        g_1fab44d = 1;
    }
    v0 = sub_1231bc8(ptr, g_1efd0b0);
    *((long long *)&ptr->padding_34[16]) = v0;
    p = &ptr->padding_34[16];
    v2 = sub_f7d8d0(p, v0);
    *((unsigned long long *)&p->padding_0[28]) = 0xfffffe00fffffe00;
    return v2;
}
```

## `AmmoText.Update` — RVA `0xc91164`

- Decompiled symbol: `AmmoText_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `268` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AmmoText_Recovered` matched 4 offsets against `AmmoText` metadata (confidence 1.00).

```c
typedef struct AmmoText_Recovered {
    char padding_0[32];
    unsigned int ammoGui;
    unsigned int ammoGui2;
    char showMags;
    char padding_29[31];
    struct struct_3 *uiTextComponent;
} AmmoText_Recovered;

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

extern unsigned long long g_1f06220;
extern long long g_1f065a0;
extern char g_1fab44e;

struct_2 * AmmoText_Update(struct_2 *ptr)
{
    struct_0 **v0;  // x20
    long long v1;  // x0
    unsigned long long v10;  // x1
    struct_0 **v11;  // x0
    long long v2;  // x0
    unsigned long long flag;  // x3
    unsigned long long v4;  // x0
    unsigned long long v5;  // x1
    struct_0 **v6;  // x0
    unsigned long long v7;  // x2
    unsigned long v8;  // x0
    unsigned long long v9;  // x2

    if (!(g_1fab44e & 1))
    {
        sub_f7d92c(&g_1f065a0);
        sub_f7d92c(&g_1f06220);
        g_1fab44e = 1;
    }
    if (ptr->field_20 == *((int *)&ptr->padding_29[3]) && ptr->field_24 == *((int *)&ptr->padding_29[7]))
        return &ptr->field_20;
    v0 = ptr->field_48;
    if (ptr->field_28)
    {
        v1 = Int32__ToString();
        v2 = Int32__ToString((struct AmmoText_Recovered *)&ptr->field_24, 0);
        flag = 0;
        v4 = String__Concat(v1, g_1f065a0, v2, 0);
        if (v0)
        {
            v5 = v4;
            v6 = v0;
            v7 = *(v0)->field_5f0;
            *(v0)->field_5e8();
        }
    }
    else
    {
        v8 = Int32__ToString((struct AmmoText_Recovered *)&ptr->field_24, 0);
        if (v0)
        {
            v9 = *(v0)->field_5f0;
            if (!v8)
                v10 = g_1f06220;
            else
                v10 = v8;
            v11 = v0;
            *(v0)->field_5e8();
        }
    }
    sub_f7db74();
}
```

## `AmmoText.ctor` — RVA `0xc91270`

- Decompiled symbol: `AmmoText_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `24` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AmmoText_Recovered` matched 2 offsets against `AmmoText` metadata (confidence 1.00).

```c
typedef struct AmmoText_Recovered {
    char padding_0[40];
    char showMags;
    char padding_29[3];
    unsigned long long oldAmmo;
} AmmoText_Recovered;

long long AmmoText_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_28 = 1;
    *((unsigned long long *)&(&ptr->padding_29)[1]) = 0xfffffe00fffffe00;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
