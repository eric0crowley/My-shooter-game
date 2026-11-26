# Native pseudocode: bl_SnapShot

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_SnapShot.get_FolderPath` — RVA `0xccaac4`

- Decompiled symbol: `bl_SnapShot_get_FolderPath`
- Metadata signature: `public static string get_FolderPath() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern char g_1fab57d;

long long bl_SnapShot_get_FolderPath(void)
{
    struct_0 *v0;  // x0

    if (!(g_1fab57d & 1))
    {
        sub_f7d92c("\rc");
        g_1fab57d = 1;
    }
    v0 = g_1ef2b10;
    if (!g_1ef2b10->field_e0)
    {
        sub_f7da5c(g_1ef2b10);
        v0 = g_1ef2b10;
    }
    return v0->field_b8->field_0;
}
```

## `bl_SnapShot.SnapshotName` — RVA `0xccab1c`

- Decompiled symbol: `bl_SnapShot_SnapshotName`
- Metadata signature: `private string SnapshotName(int width, int height) { }`
- Native interval: `596` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eee288;
extern struct_0 *g_1eee870;
extern long long g_1ef0450;
extern long long g_1f0bff8;
extern long long g_1f15da0;
extern char g_1fab57e;

int bl_SnapShot_SnapshotName(unsigned long a0, unsigned long a1, unsigned long a2)
{
    unsigned long long v8;  // x30
    unsigned long long v9;  // x24
    unsigned long long v10;  // x23
    unsigned long long v11;  // x22
    unsigned long long v12;  // x21
    unsigned long long v13;  // x20
    unsigned long long v14;  // x19
    unsigned long long v0;  // [bp-0x40]
    unsigned long long flag;  // [bp-0x38]
    unsigned long long v2;  // [bp-0x30]
    unsigned long long v3;  // [bp-0x28]
    unsigned long long v4;  // [bp-0x20]
    unsigned long long v5;  // [bp-0x18]
    unsigned long long v6;  // [bp-0x10]
    unsigned long long v7;  // [bp-0x8]

    v0 = v8;
    v2 = v9;
    v3 = v10;
    v4 = v11;
    v5 = v12;
    v6 = v13;
    v7 = v14;
    if (!(g_1fab57e & 1))
    {
        sub_f7d92c(&g_1eee870);
        sub_f7d92c("O6");
        sub_f7d92c(&g_1ef0450);
        sub_f7d92c(&g_1eee288);
        sub_f7d92c(&g_1f0bff8);
        sub_f7d92c(&g_1f15da0);
        g_1fab57e = 1;
    }
    flag = 0;
    if (!g_1eee870->field_e0)
        sub_f7da5c(g_1eee870);
    bl_SnapShot__GetFullFolderPath(Application__get_loadedLevelName(0)); /* do not return */
}
```

## `bl_SnapShot.GetFullFolderPath` — RVA `0xccad70`

- Decompiled symbol: `bl_SnapShot_GetFullFolderPath`
- Metadata signature: `private string GetFullFolderPath() { }`
- Native interval: `148` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eee870;
extern char g_1fab57f;

void bl_SnapShot_GetFullFolderPath(void)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab57f & 1))
    {
        sub_f7d92c(&g_1eee870);
        sub_f7d92c("\rc");
        g_1fab57f = 1;
    }
    if (!g_1eee870->field_e0)
        sub_f7da5c(g_1eee870);
    Application__get_dataPath(0);
    if (!g_1ef2b10->field_e0)
        sub_f7da5c(g_1ef2b10);
    String__Concat();
    return;
}
```

## `bl_SnapShot.TakeSnapshot` — RVA `0xccae04`

- Decompiled symbol: `bl_SnapShot_TakeSnapshot`
- Metadata signature: `public void TakeSnapshot() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long bl_SnapShot_TakeSnapshot(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `bl_SnapShot.ctor` — RVA `0xccae08`

- Decompiled symbol: `bl_SnapShot_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `104` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_SnapShot_Recovered` matched 3 offsets against `bl_SnapShot` metadata (confidence 1.00).

```c
typedef struct bl_SnapShot_Recovered {
    char padding_0[32];
    unsigned long long resWidth;
    unsigned int msaa;
    char padding_2c[4];
    long long m_TakeSnapShot;
} bl_SnapShot_Recovered;

extern long long g_1f06220;
extern char g_1fab580;

void bl_SnapShot_ctor(struct_0 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab580 & 1))
    {
        sub_f7d92c(&g_1f06220);
        g_1fab580 = 1;
    }
    ptr->field_20 = 0x80000000800;
    ptr->field_28 = 1;
    ptr->field_30 = g_1f06220;
    sub_f7d8d0((struct bl_SnapShot_Recovered *)&ptr->field_30, g_1f06220);
    MonoBehaviour__ctor();
    return;
}
```

## `bl_SnapShot.cctor` — RVA `0xccae70`

- Decompiled symbol: `bl_SnapShot_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
extern unsigned long long g_1f075f8;
extern char g_1fab581;

void bl_SnapShot_cctor(void)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab581 & 1))
    {
        sub_f7d92c(&g_1f075f8);
        sub_f7d92c("\rc");
        g_1fab581 = 1;
    }
    g_1ef2b10->field_b8->field_0 = g_1f075f8;
    sub_f7d8d0();
    return;
}
```
