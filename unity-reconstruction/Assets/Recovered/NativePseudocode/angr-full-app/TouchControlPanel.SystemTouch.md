# Native pseudocode: TouchControlPanel.SystemTouch

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchControlPanel.SystemTouch.ctor` — RVA `0xc53dd0`

- Decompiled symbol: `TouchControlPanel_SystemTouch_ctor`
- Metadata signature: `public void .ctor(TouchControlPanel panel) { }`
- Native interval: `112` bytes
- Result: `pseudocode`

```c
extern char g_1fab272;

long long TouchControlPanel_SystemTouch_ctor(void* ptr)
{
    unsigned long v0;  // x20
    void* p;  // x19
    unsigned long v2;  // x0

    if (!(g_1fab272 & 1))
    {
        sub_f7d92c("%Y");
        g_1fab272 = 1;
    }
    Object__ctor(ptr, 0);
    v0 = sub_f7db70(g_1ef1e38);
    TouchObject__ctor(v0);
    *((unsigned long *)&ptr[16]) = v0;
    p = ptr + 16;
    v2 = sub_f7d8d0(p, v0);
    *((unsigned long long *)&p[8]) = 0;
    return v2;
}
```

## `TouchControlPanel.SystemTouch.WakeUp` — RVA `0xc54c20`

- Decompiled symbol: `TouchControlPanel_SystemTouch_WakeUp`
- Metadata signature: `public void WakeUp() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[28];
    unsigned int field_1c;
} struct_0;

struct_0 * TouchControlPanel_SystemTouch_WakeUp(struct_0 *ptr)
{
    ptr->field_1c = 0;
    return ptr;
}
```

## `TouchControlPanel.SystemTouch.Update` — RVA `0xc54d50`

- Decompiled symbol: `TouchControlPanel_SystemTouch_Update`
- Metadata signature: `public void Update() { }`
- Native interval: `160` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchControlPanel_SystemTouch_Recovered` matched 2 offsets against `TouchControlPanel.SystemTouch` metadata (confidence 1.00).

```c
typedef struct TouchControlPanel_SystemTouch_Recovered {
    char padding_0[16];
    struct struct_0 *touch;
    char padding_18[4];
    unsigned int elapsedSinceLastAction;
} TouchControlPanel_SystemTouch_Recovered;

typedef struct struct_2 {
    char padding_0[16];
    char field_10;
} struct_2;

typedef struct struct_0 {
    char padding_0[16];
    char field_10;
} struct_0;

struct_1 * TouchControlPanel_SystemTouch_Update(struct_1 *ptr)
{
    struct_1 *v0;  // x0
    unsigned int v1;  // s0
    unsigned int v2;  // s0
    unsigned long v3;  // 4142
    struct_1 *v4;  // x0
    struct_1 *v5;  // x0
    struct_1 *v6;  // x0
    struct_1 *v7;  // x0
    unsigned int v8;  // x2
    long long v9;  // x0

    if (ptr->field_10)
    {
        if (ptr->field_10->field_10)
        {
            v0 = Time__get_unscaledDeltaTime(0);
            v2 = ptr->field_1c + v1;
            ptr->field_1c = v2;
            v3 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v2, 0x40000000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0x40000000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, 0x40000000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0x40000000) & 1)) & ((unsigned long long)(char)(CmpF(v2, 0x40000000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0x40000000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v3)
                return v0;
            v4 = Input__GetMouseButton(0, 0);
            if (((char)v4 & 1))
                return v4;
            v5 = Input__GetMouseButton(1, 0);
            if (((char)v5 & 1))
                return v5;
            v6 = Input__GetMouseButton(2, 0);
            if (((char)v6 & 1))
                return v6;
            v7 = Input__get_touchCount(0);
            if ((unsigned int)v7)
            {
                return v7;
            }
            else if (ptr->field_10)
            {
                v9 = TouchObject__End(ptr->field_10, 1, v8);
                return TouchObject__End(ptr->field_10, 1, v8);
            }
        }
        else
        {
            return ptr;
        }
    }
    sub_f7db74();
}
```
