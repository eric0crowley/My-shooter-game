# Native pseudocode: bl_CreateItemExample

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_CreateItemExample.Start` — RVA `0xccaedc`

- Decompiled symbol: `bl_CreateItemExample_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `124` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1efd0e8;
extern char g_1fab582;

long long bl_CreateItemExample_Start(struct_0 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    long long v8;  // x0
    struct_0 *v9;  // x20
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab582 & 1))
    {
        sub_f7d92c(&g_1efd0e8);
        g_1fab582 = 1;
    }
    v8 = sub_1231bc8(ptr, g_1efd0e8);
    ptr->field_20 = v8;
    v9 = &ptr->field_20;
    sub_f7d8d0(v9, v8);
    if (*((long long *)&v9->padding_0[0]))
        bl_MMExampleManager__get_GetActiveMiniMap(); /* do not return */
    sub_f7db74(0);
}
```

## `bl_CreateItemExample.Update` — RVA `0xccafc8`

- Decompiled symbol: `bl_CreateItemExample_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `188` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1f0a440;
extern char g_1fab583;

long long bl_CreateItemExample_Update(void* a0)
{
    unsigned long v0;  // x0
    unsigned long v1;  // x0
    unsigned long v2;  // x0

    if (!(g_1fab583 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0a440);
        g_1fab583 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality((long long)a0[40], 0, 0);
    if (((char)v0 & 1))
        return v0;
    if (((char)Input__GetButtonDown(g_1f0a440, 0) & 1))
        bl_CreateItemExample__CreateItem(a0);
    v1 = Input__GetKeyDown(104, 0);
    if (!((char)v1 & 1))
        return v1;
    if ((long long)a0[40])
    {
        v2 = (unsigned long long)bl_MiniMap__DoHitEffect((long long)a0[40]);
        return (unsigned long long)bl_MiniMap__DoHitEffect((long long)a0[40]);
    }
    sub_f7db74(0);
}
```

## `bl_CreateItemExample.CreateItem` — RVA `0xccb084`

- Decompiled symbol: `bl_CreateItemExample_CreateItem`
- Metadata signature: `private void CreateItem() { }`
- Native interval: `468` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    unsigned int field_10;
    unsigned int field_14;
    unsigned int field_18;
    char padding_1c[12];
    uint128_t field_28;
    unsigned int field_38;
    char padding_3c[12];
    unsigned int field_48;
} struct_2;

typedef struct struct_3 {
    char padding_0[40];
    struct struct_3 *field_28;
} struct_3;

typedef struct struct_3 {
    char padding_0[392];
    long long field_188;
} struct_3;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern struct_1 *g_1ef0e48;
extern long long g_1ef2af8;
extern char g_1fab584;

long long bl_CreateItemExample_CreateItem(struct_3 *a0)
{
    long long v19;  // x20
    long long v20;  // x0
    struct_2 *ptr;  // x20
    long long v22;  // x0
    unsigned long long v0;  // [bp-0xd0]
    unsigned long long v1;  // [bp-0xc8]
    unsigned int v2;  // [bp-0xc0]
    unsigned int v3;  // [bp-0xbc]
    unsigned int v4;  // [bp-0xb8]
    unsigned long long v5;  // [bp-0xb4]
    unsigned int v6;  // [bp-0xac]
    unsigned long long v7;  // [bp-0xa8]
    unsigned int v8;  // [bp-0xa8]
    unsigned int v9;  // [bp-0xa4]
    unsigned int v10;  // [bp-0xa0]
    unsigned int v11;  // [bp-0xa0]
    unsigned long long v12;  // [bp-0x9c]
    unsigned int v13;  // [bp-0x94]
    int choice;  // [bp-0x90]
    uint128_t flag2;  // [bp-0x80]
    uint128_t flag;  // [bp-0x74]
    unsigned long long v17;  // [bp-0x60]
    unsigned int v18;  // [bp-0x58]

    if (!(g_1fab584 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef0e48);
        sub_f7d92c(&g_1ef2af8);
        g_1fab584 = 1;
    }
    flag = 0;
    choice = 0;
    flag2 = 0;
    v19 = Camera__get_main(0);
    Input__get_mousePosition(0);
    if (v19)
    {
        Camera__ScreenPointToRay(v19, 0);
        v18 = v13;
        v17 = v12;
        v7 = v17;
        v11 = v18;
        if (!g_1ef0e48->field_e0)
            sub_f7da5c(g_1ef0e48);
        v2 = v8;
        v3 = v9;
        v4 = v10;
        v5 = v7;
        v6 = v11;
        v20 = Physics__Raycast(&v2, &choice, 0);
        if (!((char)v20 & 1))
            return v20;
        RaycastHit__get_point(&choice, 0);
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        v0 = 0x3f800000;
        v1 = 0x3f80000000000000;
        Debug__DrawLine(0);
        RaycastHit__get_point(&choice, 0);
        ptr = sub_f7db70(g_1ef2af8);
        *((unsigned int *)((char *)&ptr->field_28 + 8)) = 1064514355;
        *((uint128_t *)&(&ptr->padding_1c)[1]) = 0x3f8000003f8000003f80000041400000;
        *((unsigned int *)&ptr->padding_3c[4]) = 1;
        Object__ctor(ptr, 0);
        ptr->field_10 = v8;
        ptr->field_14 = v9;
        ptr->field_18 = v10;
        if (a0->field_28)
        {
            v22 = bl_MiniMap__CreateNewItem(a0->field_28, ptr);
            return bl_MiniMap__CreateNewItem(a0->field_28, ptr);
        }
    }
    sub_f7db74();
}
```

## `bl_CreateItemExample.ctor` — RVA `0xccb258`

- Decompiled symbol: `bl_CreateItemExample_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long bl_CreateItemExample_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
