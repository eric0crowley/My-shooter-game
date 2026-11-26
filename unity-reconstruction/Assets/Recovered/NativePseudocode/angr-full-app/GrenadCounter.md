# Native pseudocode: GrenadCounter

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GrenadCounter.OnEnabled` — RVA `0xcc2340`

- Decompiled symbol: `GrenadCounter_OnEnabled`
- Metadata signature: `private void OnEnabled() { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[40];
    struct struct_0 *field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[296];
    unsigned int field_128;
} struct_0;

extern long long g_1f0a7f0;
extern char g_1fab519;

unsigned long long GrenadCounter_OnEnabled(struct_1 *idx)
{
    unsigned long long v0;  // x0

    if (!(g_1fab519 & 1))
    {
        sub_f7d92c(&g_1f0a7f0);
        g_1fab519 = 1;
    }
    v0 = PlayerPrefs__GetInt(g_1f0a7f0, 0);
    if (idx->field_28)
    {
        idx->field_28->field_128 = v0;
        return v0;
    }
    sub_f7db74();
}
```

## `GrenadCounter.Start` — RVA `0xcc239c`

- Decompiled symbol: `GrenadCounter_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `280` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GrenadCounter_Recovered` matched 2 offsets against `GrenadCounter` metadata (confidence 1.00).

```c
typedef struct GrenadCounter_Recovered {
    char padding_0[32];
    struct struct_3 *GrenadeAmmo;
    unsigned long long WB;
} GrenadCounter_Recovered;

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

extern long long g_1eefbf0;
extern long long g_1efcfc0;
extern long long g_1f065a0;
extern long long g_1f0a7f0;
extern char g_1fab51a;

void GrenadCounter_Start(struct_2 *ptr)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x22
    unsigned long long v16;  // x1
    unsigned long long v17;  // x2
    struct_0 **v18;  // x0
    unsigned long long v8;  // x21
    unsigned long long v9;  // x20
    unsigned long long v10;  // x19
    struct_0 **v11;  // x20
    unsigned long v12;  // x0
    long long v13;  // x0
    unsigned long long flag;  // x3
    unsigned long long v15;  // x0
    unsigned long long v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x24]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]
    unsigned long long v5;  // [bp-0x8]

    v0 = v6;
    v2 = v7;
    v3 = v8;
    v4 = v9;
    v5 = v10;
    if (!(g_1fab51a & 1))
    {
        sub_f7d92c(&g_1efcfc0);
        sub_f7d92c(&g_1eefbf0);
        sub_f7d92c(&g_1f0a7f0);
        sub_f7d92c(&g_1f065a0);
        g_1fab51a = 1;
    }
    v11 = ptr->field_20;
    v1 = PlayerPrefs__GetInt(g_1f0a7f0, 0);
    v12 = Int32__ToString(&v1, 0);
    if (ptr->field_28)
    {
        v13 = Int32__ToString(ptr->field_28 + 312, 0);
        flag = 0;
        v15 = String__Concat(v12, g_1f065a0, v13, 0);
        if (v11)
        {
            v16 = v15;
            v17 = *(v11)->field_5f0;
            v18 = v11;
            *(v11)->field_5e8();
        }
    }
    sub_f7db74();
}
```

## `GrenadCounter.UpdateAmmoUI` — RVA `0xcc24b4`

- Decompiled symbol: `GrenadCounter_UpdateAmmoUI`
- Metadata signature: `public void UpdateAmmoUI() { }`
- Native interval: `204` bytes
- Result: `pseudocode`
- Heuristic layout hint: `GrenadCounter_Recovered` matched 2 offsets against `GrenadCounter` metadata (confidence 1.00).

```c
typedef struct GrenadCounter_Recovered {
    char padding_0[32];
    struct struct_3 *GrenadeAmmo;
    unsigned long long WB;
} GrenadCounter_Recovered;

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

extern long long g_1f065a0;
extern long long g_1f0a7f0;
extern char g_1fab51b;

void GrenadCounter_UpdateAmmoUI(struct_2 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x21
    struct_0 **v15;  // x0
    unsigned long long v16;  // x2
    unsigned long long v7;  // x20
    unsigned long long v8;  // x19
    struct_0 **v9;  // x19
    unsigned long v10;  // x0
    long long v11;  // x0
    unsigned long long flag;  // x3
    unsigned long long v13;  // x0
    unsigned long long v14;  // x1
    unsigned int v0;  // [bp-0x24]
    unsigned long long v1;  // [bp-0x20]
    unsigned long long v2;  // [bp-0x18]
    unsigned long long v3;  // [bp-0x10]
    unsigned long long v4;  // [bp-0x8]

    v1 = v5;
    v2 = v6;
    v3 = v7;
    v4 = v8;
    if (!(g_1fab51b & 1))
    {
        sub_f7d92c(&g_1f0a7f0);
        sub_f7d92c(&g_1f065a0);
        g_1fab51b = 1;
    }
    v9 = ptr->field_20;
    v0 = PlayerPrefs__GetInt(g_1f0a7f0, 0) - 1;
    v10 = Int32__ToString(&v0, 0);
    if (ptr->field_28)
    {
        v11 = Int32__ToString(ptr->field_28 + 312, 0);
        flag = 0;
        v13 = String__Concat(v10, g_1f065a0, v11, 0);
        if (v9)
        {
            v14 = v13;
            v15 = v9;
            v16 = *(v9)->field_5f0;
            *(v9)->field_5e8();
        }
    }
    sub_f7db74();
}
```

## `GrenadCounter.Update` — RVA `0xcc2580`

- Decompiled symbol: `GrenadCounter_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
extern long long g_1f0a7f0;
extern char g_1fab51c;

void GrenadCounter_Update(unsigned long long *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long v8;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab51c & 1))
    {
        sub_f7d92c(&g_1f0a7f0);
        g_1fab51c = 1;
    }
    if (PlayerPrefs__GetInt(g_1f0a7f0, 0) > 0)
    {
        v8 = ptr[7];
        if (!v8 || !((GameObject__SetActive(v8, 0, 0), v8 = (unsigned long)ptr[6], v8)))
            goto LABEL_10c2618;
    }
    else
    {
        v8 = ptr[6];
        if (!v8 || !((GameObject__SetActive(v8, 0, 0), v8 = (unsigned long)ptr[7], v8)))
        {
LABEL_10c2618:
            sub_f7db74(v8);
        }
    }
    GameObject__SetActive();
    return;
}
```

## `GrenadCounter.ctor` — RVA `0xcc261c`

- Decompiled symbol: `GrenadCounter_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long GrenadCounter_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
