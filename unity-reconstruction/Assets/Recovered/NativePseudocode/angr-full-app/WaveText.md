# Native pseudocode: WaveText

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `WaveText.OnEnable` — RVA `0xc92a38`

- Decompiled symbol: `WaveText_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `100` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WaveText_Recovered` matched 2 offsets against `WaveText` metadata (confidence 1.00).

```c
typedef struct WaveText_Recovered {
    char padding_0[40];
    unsigned long long oldWave;
    char padding_30[16];
    long long uiTextComponent;
} WaveText_Recovered;

extern long long g_1efd0b0;
extern char g_1fab45b;

long long WaveText_OnEnable(struct_0 *ptr)
{
    long long v0;  // x0
    struct_0 *p;  // x19
    unsigned long v2;  // x0

    if (!(g_1fab45b & 1))
    {
        sub_f7d92c(&g_1efd0b0);
        g_1fab45b = 1;
    }
    v0 = sub_1231bc8(ptr, g_1efd0b0);
    ptr->field_40 = v0;
    p = &ptr->field_40;
    v2 = sub_f7d8d0(p, v0);
    *((unsigned long long *)&p->padding_0[24]) = 0xfffffe00fffffe00;
    return v2;
}
```

## `WaveText.Update` — RVA `0xc92a9c`

- Decompiled symbol: `WaveText_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `256` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WaveText_Recovered` matched 3 offsets against `WaveText` metadata (confidence 1.00).

```c
typedef struct WaveText_Recovered {
    char padding_0[32];
    unsigned int waveGui;
    unsigned int waveGui2;
    char padding_28[24];
    struct struct_3 *uiTextComponent;
} WaveText_Recovered;

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

extern long long g_1f06578;
extern char g_1fab45c;

struct_2 * WaveText_Update(struct_2 *ptr)
{
    struct_2 *v0;  // x0
    struct_0 **v1;  // x20
    long long v2;  // x0
    long long v3;  // x0
    long long v4;  // x3
    unsigned long long flag;  // x4
    unsigned long long v6;  // x0
    unsigned long long v7;  // x1
    struct_0 **v8;  // x0
    unsigned long long v9;  // x2

    if (!(g_1fab45c & 1))
    {
        sub_f7d92c(&g_1f06578);
        sub_f7d92c("Y&");
        g_1fab45c = 1;
    }
    v0 = &ptr->field_20;
    if (ptr->field_20 == *((int *)&v0->padding_0[8]) && ptr->field_24 == *((int *)&ptr->padding_28[4]))
        return v0;
    v1 = ptr->field_40;
    v2 = Int32__ToString(v0, 0);
    v3 = Int32__ToString((struct WaveText_Recovered *)&ptr->field_24, 0);
    v4 = v3;
    flag = 0;
    v6 = String__Concat(g_1f0fb50, v2, g_1f06578, v3, 0);
    if (!v1)
        sub_f7db74();
    v7 = v6;
    v8 = v1;
    v9 = *(v1)->field_5f0;
    *(v1)->field_5e8();
}
```

## `WaveText.ctor` — RVA `0xc92b9c`

- Decompiled symbol: `WaveText_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned long long field_28;
} struct_0;

long long WaveText_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_28 = 0xfffffe00fffffe00;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
