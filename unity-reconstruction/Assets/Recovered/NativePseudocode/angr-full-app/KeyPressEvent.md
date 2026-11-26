# Native pseudocode: KeyPressEvent

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `KeyPressEvent.ctor` — RVA `0xc68584`

- Decompiled symbol: `KeyPressEvent_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

extern char g_1fab31a;

void KeyPressEvent_ctor(struct_0 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    long long v8;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab31a & 1))
    {
        sub_f7d92c("c[");
        g_1fab31a = 1;
    }
    MonoBehaviour__ctor(ptr, 0);
    v8 = sub_f7db70(g_1ef2110);
    UnityEvent__ctor(v8, 0);
    ptr->field_28 = v8;
    sub_f7d8d0();
    return;
}
```

## `KeyPressEvent.Update` — RVA `0xc685f0`

- Decompiled symbol: `KeyPressEvent_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `244` bytes
- Result: `pseudocode`
- Heuristic layout hint: `KeyPressEvent_Recovered` matched 3 offsets against `KeyPressEvent` metadata (confidence 1.00).

```c
typedef struct KeyPressEvent_Recovered {
    char padding_0[32];
    unsigned int keyCode;
    unsigned int eventType;
    unsigned long long keyEvent;
} KeyPressEvent_Recovered;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_1 *g_1eeed00;
extern char g_1fab31b;

int KeyPressEvent_Update(struct_0 *ptr)
{
    struct_0 *v0;  // x0
    struct_0 *v1;  // x0
    struct_0 *v2;  // x0
    unsigned int flag;  // w8

    v0 = ptr;
    if (!(g_1fab31b & 1))
    {
        v1 = sub_f7d92c(&g_1eeed00);
        g_1fab31b = 1;
        v0 = v1;
    }
    v2 = v0;
    flag = ptr->field_24;
    if (flag == 2)
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        v2 = CF2Input__GetKey(ptr->field_20, 0);
        if (((char)v2 & 1))
        {
LABEL_1068690:
            if (ptr->field_28)
                return UnityEvent__Invoke();
            sub_f7db74(0);
        }
    }
    else if (flag == 1)
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        v2 = CF2Input__GetKeyUp(ptr->field_20, 0);
        if ((v2 & 1))
            goto LABEL_1068690;
    }
    else if (!flag)
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        v2 = CF2Input__GetKeyDown(ptr->field_20, 0);
        if ((v2 & 1))
            goto LABEL_1068690;
    }
    return *((unsigned int *)&v2);
}
```
