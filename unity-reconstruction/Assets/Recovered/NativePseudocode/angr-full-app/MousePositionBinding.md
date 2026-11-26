# Native pseudocode: MousePositionBinding

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MousePositionBinding.ctor` — RVA `0xc5e2e8`

- Decompiled symbol: `MousePositionBinding_ctor`
- Metadata signature: `public void .ctor(InputBindingBase parent) { }`
- Native interval: `64` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    long long field_18;
    unsigned int field_20;
} struct_0;

long long MousePositionBinding_ctor(struct_0 *p, long long a1)
{
    struct_0 *ptr;  // x20
    unsigned long v1;  // x0

    Object__ctor();
    p->field_18 = a1;
    ptr = &p->field_18;
    ptr->padding_0[8] = 0;
    v1 = sub_f7d8d0(ptr, a1);
    ptr->padding_0[8] = 0;
    *((unsigned int *)&ptr->padding_0[8]) = 0;
    return v1;
}
```

## `MousePositionBinding.ctor` — RVA `0xc5e328`

- Decompiled symbol: `MousePositionBinding_ctor`
- Metadata signature: `public void .ctor(int prio, bool enabled, InputBindingBase parent) { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    long long field_18;
    unsigned int field_20;
} struct_0;

long long MousePositionBinding_ctor(struct_0 *p, unsigned int a1, char a2, long long a3)
{
    struct_0 *ptr;  // x21
    unsigned long v1;  // x0

    Object__ctor();
    p->field_18 = a3;
    ptr = &p->field_18;
    ptr->padding_0[8] = 0;
    v1 = sub_f7d8d0(ptr, a3);
    ptr->padding_0[8] = a2 & 1;
    *((unsigned int *)&ptr->padding_0[8]) = a1;
    return v1;
}
```

## `MousePositionBinding.CopyFrom` — RVA `0xc5e378`

- Decompiled symbol: `MousePositionBinding_CopyFrom`
- Metadata signature: `public void CopyFrom(MousePositionBinding b) { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    struct struct_1 *field_18;
    unsigned int field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    unsigned int field_20;
} struct_0;

struct_1 * MousePositionBinding_CopyFrom(struct_1 *p, struct_0 *addr)
{
    unsigned int v0;  // w8
    struct_1 *ptr;  // x9

    if (!addr)
        return p;
    v0 = addr->field_10;
    p->field_10 = v0;
    if (!v0)
        return p;
    ptr = p;
    do
    {
        ptr->field_10 = 1;
        ptr = ptr->field_18;
    } while (ptr->field_18);
    p->field_20 = addr->field_20;
    return p;
}
```

## `MousePositionBinding.SyncPos` — RVA `0xc5e3a8`

- Decompiled symbol: `MousePositionBinding_SyncPos`
- Metadata signature: `public void SyncPos(Vector2 pos, InputRig rig) { }`
- Native interval: `176` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    int field_20;
} struct_1;

typedef struct struct_2 {
    char padding_0[280];
    struct struct_0 *field_118;
} struct_2;

typedef struct struct_0 {
    char padding_0[48];
    unsigned int field_30;
    unsigned int field_34;
    int field_38;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2d7;

struct_1 * MousePositionBinding_SyncPos(struct_1 *a0, struct_2 *a1)
{
    struct_1 *v0;  // x0
    struct_1 *v1;  // x0
    struct_1 *v2;  // x0
    struct_1 *v3;  // x0
    struct_0 *v4;  // x0

    v0 = a0;
    if (!(g_1fab2d7 & 1))
    {
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab2d7 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (!a0->field_10)
        return v2;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v3 = Object__op_Equality(a1, 0, 0);
    if (((char)v3 & 1))
        return v3;
    if (a1 && a1->field_118)
    {
        v4 = InputRig_MouseConfig__SetPosition(a1->field_118, a0->field_20);
        return InputRig_MouseConfig__SetPosition(a1->field_118, a0->field_20);
    }
    sub_f7db74();
}
```

## `MousePositionBinding.OnIsEmulatingMousePosition` — RVA `0xc5e458`

- Decompiled symbol: `MousePositionBinding_OnIsEmulatingMousePosition`
- Metadata signature: `protected override bool OnIsEmulatingMousePosition() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    char field_10;
} struct_0;

long long MousePositionBinding_OnIsEmulatingMousePosition(struct_0 *a0)
{
    return a0->field_10;
}
```
