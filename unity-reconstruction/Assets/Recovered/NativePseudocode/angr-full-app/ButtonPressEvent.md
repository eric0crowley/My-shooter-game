# Native pseudocode: ButtonPressEvent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ButtonPressEvent.ctor` — RVA `0xc683e0`

- Decompiled symbol: `ButtonPressEvent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `152` bytes
- Result: `pseudocode`

```c
extern long long g_1f0a440;
extern char g_1fab318;

void ButtonPressEvent_ctor(long long *ptr)
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
    if (!(g_1fab318 & 1))
    {
        sub_f7d92c("c[");
        sub_f7d92c(&g_1f0a440);
        g_1fab318 = 1;
    }
    ptr[4] = g_1f0a440;
    sub_f7d8d0(ptr + 4, g_1f0a440);
    MonoBehaviour__ctor(ptr, 0);
    v10 = sub_f7db70(g_1ef2110);
    UnityEvent__ctor(v10, 0);
    ptr[6] = v10;
    sub_f7d8d0();
    return;
}
```

## `ButtonPressEvent.Update` — RVA `0xc68478`

- Decompiled symbol: `ButtonPressEvent_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `268` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ButtonPressEvent_Recovered` matched 3 offsets against `ButtonPressEvent` metadata (confidence 1.00).

```c
typedef struct ButtonPressEvent_Recovered {
    char padding_0[32];
    long long buttonName;
    char padding_28[4];
    unsigned int eventType;
    unsigned long long buttonEvent;
} ButtonPressEvent_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eeed00;
extern char g_1fab319;

struct_1 * ButtonPressEvent_Update(struct_1 *ptr)
{
    struct_1 *v0;  // x0
    struct_1 *v1;  // x0
    struct_1 *v2;  // x0
    unsigned int flag;  // w8
    struct_1 *v4;  // x0
    struct_1 *v5;  // x0
    struct_1 *v6;  // x0
    unsigned long long v7;  // x0

    v0 = ptr;
    if (!(g_1fab319 & 1))
    {
        v1 = sub_f7d92c(&g_1eeed00);
        g_1fab319 = 1;
        v0 = v1;
    }
    v2 = v0;
    flag = ptr->field_2c;
    if (flag == 2)
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        v6 = CF2Input__GetButton(ptr->field_20, &ptr->padding_28, 0);
        if (!((char)v6 & 1))
            return v6;
    }
    else if (flag == 1)
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        v5 = CF2Input__GetButtonUp(ptr->field_20, &ptr->padding_28, 0);
        if (!((char)v5 & 1))
            return v5;
    }
    else if (!flag)
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        v4 = CF2Input__GetButtonDown(ptr->field_20, &ptr->padding_28, 0);
        if (!((char)v4 & 1))
            return v4;
    }
    else
    {
        return v2;
    }
    if (ptr->field_30)
    {
        v7 = UnityEvent__Invoke();
        return UnityEvent__Invoke();
    }
    sub_f7db74(0);
}
```
