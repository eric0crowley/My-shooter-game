# Native pseudocode: EmuTouchBinding

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `EmuTouchBinding.ctor` — RVA `0xc5d500`

- Decompiled symbol: `EmuTouchBinding_ctor`
- Metadata signature: `public void .ctor(InputBindingBase parent) { }`
- Native interval: `68` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    long long field_18;
    unsigned int field_20;
} struct_0;

long long EmuTouchBinding_ctor(struct_0 *p, long long a1)
{
    struct_0 *ptr;  // x20
    unsigned long v1;  // x0

    Object__ctor();
    p->field_18 = a1;
    ptr = &p->field_18;
    ptr->padding_0[8] = 0;
    v1 = sub_f7d8d0(ptr, a1);
    ptr->padding_0[8] = 0;
    *((unsigned int *)&ptr->padding_0[8]) = 4294967295;
    return v1;
}
```

## `EmuTouchBinding.CopyFrom` — RVA `0xc5d578`

- Decompiled symbol: `EmuTouchBinding_CopyFrom`
- Metadata signature: `public void CopyFrom(EmuTouchBinding b) { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    struct struct_1 *field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    char field_10;
} struct_0;

struct_1 * EmuTouchBinding_CopyFrom(struct_1 *cur, struct_0 *ptr)
{
    unsigned int v0;  // w8

    if (!ptr)
        return cur;
    v0 = ptr->field_10;
    cur->field_10 = v0;
    if (!v0)
        return cur;
    do
    {
        cur->field_10 = 1;
        cur = cur->field_18;
    } while (cur);
    return cur;
}
```

## `EmuTouchBinding.SyncState` — RVA `0xc5d5b4`

- Decompiled symbol: `EmuTouchBinding_SyncState`
- Metadata signature: `public void SyncState(TouchGestureBasicState touchState, InputRig rig) { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    char field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[28];
    char field_1c;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2ce;

struct_1 * EmuTouchBinding_SyncState(struct_1 *a0, struct_0 *a1, unsigned long a2)
{
    struct_1 *v0;  // x0
    struct_1 *v1;  // x0
    struct_1 *v2;  // x0
    struct_1 *v3;  // x0
    void* v4;  // x0

    v0 = a0;
    if (!(g_1fab2ce & 1))
    {
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab2ce = 1;
        v0 = v1;
    }
    v2 = v0;
    if (!a0->field_10)
        return v2;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v3 = Object__op_Equality(a2, 0, 0);
    if (((char)v3 & 1))
        return v3;
    if (a2)
    {
        v4 = InputRig__SyncEmuTouch(a2, a1, &a0[1].padding_0[15]);
        return InputRig__SyncEmuTouch(a2, a1, &a0[1].padding_0[15]);
    }
    sub_f7db74();
}
```

## `EmuTouchBinding.OnIsEmulatingTouches` — RVA `0xc5d658`

- Decompiled symbol: `EmuTouchBinding_OnIsEmulatingTouches`
- Metadata signature: `protected override bool OnIsEmulatingTouches() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    char field_10;
} struct_0;

long long EmuTouchBinding_OnIsEmulatingTouches(struct_0 *a0)
{
    return a0->field_10;
}
```
