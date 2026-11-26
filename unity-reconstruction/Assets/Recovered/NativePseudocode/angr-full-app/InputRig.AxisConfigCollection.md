# Native pseudocode: InputRig.AxisConfigCollection

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InputRig.AxisConfigCollection.ctor` — RVA `0xc41ec0`

- Decompiled symbol: `InputRig_AxisConfigCollection_ctor`
- Metadata signature: `public void .ctor(InputRig rig, int capacity) { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
extern long long g_1ef9848;
extern char g_1fab1ff;

void InputRig_AxisConfigCollection_ctor(unsigned long a0, unsigned long a1, unsigned long a2)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]
    unsigned long long v5;  // [bp-0x8]

    v0 = v6;
    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    if (!(g_1fab1ff & 1))
    {
        sub_f7d92c(&g_1ef9848);
        g_1fab1ff = 1;
    }
}
```

## `InputRig.AxisConfigCollection.Add` — RVA `0xc41f20`

- Decompiled symbol: `InputRig_AxisConfigCollection_Add`
- Metadata signature: `public InputRig.AxisConfig Add(string name, InputRig.AxisType axisType, bool undoable) { }`
- Native interval: `296` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    char padding_8[8];
    long long field_10;
    unsigned long long field_18;
    char padding_20[4];
    unsigned int field_24;
    char field_28;
    char padding_29[11];
    unsigned int field_34;
    char padding_38[12];
    unsigned int field_44;
    char padding_48[12];
    char padding_54[12];
    uint128_t field_54;
    unsigned int field_64;
    char field_68;
    char padding_69[3];
    char padding_78[8];
    uint128_t field_6c;
    unsigned int field_7c;
} struct_1;

typedef struct struct_0 {
    char padding_0[376];
    unsigned long long field_178;
} struct_0;

extern long long g_1ef3320;
extern long long g_1ef90c0;
extern long long g_1ef9850;
extern char g_1fab200;

long long InputRig_AxisConfigCollection_Add(long long a0, long long a1, unsigned long a2)
{
    long long v0;  // x0

    if (!(g_1fab200 & 1))
    {
        sub_f7d92c(&g_1ef3320);
        sub_f7d92c(&g_1ef90c0);
        sub_f7d92c(&g_1ef9850);
        g_1fab200 = 1;
    }
    v0 = sub_1526618(a0, a1, g_1ef9850);
    if (v0)
        return v0;
    InputRig_AxisConfig__ctor(sub_f7db70(g_1ef3320)); /* do not return */
}
```

## `InputRig.AxisConfigCollection.ApplyKeyboardInput` — RVA `0xc42048`

- Decompiled symbol: `InputRig_AxisConfigCollection_ApplyKeyboardInput`
- Metadata signature: `public void ApplyKeyboardInput() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern long long g_1ef90d0;
extern long long g_1ef90d8;
extern char g_1fab201;

struct_2 * InputRig_AxisConfigCollection_ApplyKeyboardInput(struct_1 *ptr)
{
    struct_0 *v0;  // x0
    int v1;  // w20
    unsigned long v2;  // x0

    if (!(g_1fab201 & 1))
    {
        sub_f7d92c(&g_1ef90d0);
        sub_f7d92c(&g_1ef90d8);
        g_1fab201 = 1;
    }
    v0 = ptr->field_10;
    if (v0)
    {
        v1 = 0;
        do
        {
            if (v0->field_18 <= v1)
                return v0;
        } while ((v0 = (struct_0 *)(unsigned long long)sub_14a30c0(), v0 && (InputRig_AxisConfig__ApplyKeyboardInput(v0), v0 = (struct_0 *)ptr->field_10, v1 = (int)(v1 + 1), v0)));
    }
    v2 = sub_f7db74(v0);
    return sub_f7db74(v0);
}
```

## `InputRig.AxisConfigCollection.MuteAllUntilRelease` — RVA `0xc420d0`

- Decompiled symbol: `InputRig_AxisConfigCollection_MuteAllUntilRelease`
- Metadata signature: `public void MuteAllUntilRelease() { }`
- Native interval: `148` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[118];
    char field_92;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
    char padding_1c[118];
    char field_92;
} struct_0;

extern long long g_1ef90d0;
extern long long g_1ef90d8;
extern char g_1fab202;

struct_2 * InputRig_AxisConfigCollection_MuteAllUntilRelease(struct_1 *ptr)
{
    struct_0 *p;  // x0
    int v1;  // w20
    unsigned long v2;  // x0

    if (!(g_1fab202 & 1))
    {
        sub_f7d92c(&g_1ef90d0);
        sub_f7d92c(&g_1ef90d8);
        g_1fab202 = 1;
    }
    p = ptr->field_10;
    if (p)
    {
        v1 = 0;
        do
        {
            if (p->field_18 <= v1)
                return p;
        } while ((p = (struct_0 *)(unsigned long long)sub_14a30c0(), p && (p->field_92 = 1, p = (struct_0 *)ptr->field_10, v1 = (int)(v1 + 1), p)));
    }
    v2 = sub_f7db74(p);
    return sub_f7db74(p);
}
```
