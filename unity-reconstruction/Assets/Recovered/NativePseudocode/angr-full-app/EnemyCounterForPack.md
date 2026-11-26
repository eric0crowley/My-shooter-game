# Native pseudocode: EnemyCounterForPack

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `EnemyCounterForPack.Start` — RVA `0xc6d448`

- Decompiled symbol: `EnemyCounterForPack_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `32` bytes
- Result: `pseudocode`
- Heuristic layout hint: `EnemyCounterForPack_Recovered` matched 2 offsets against `EnemyCounterForPack` metadata (confidence 1.00).

```c
typedef struct EnemyCounterForPack_Recovered {
    char padding_0[32];
    struct struct_0 *myEnemy;
    char padding_28[16];
    unsigned int countEnemy;
} EnemyCounterForPack_Recovered;

typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

void EnemyCounterForPack_Start(struct_1 *ptr)
{
    if (ptr->field_20)
    {
        ptr->field_38 = ptr->field_20->field_18;
        return;
    }
    sub_f7db74();
}
```

## `EnemyCounterForPack.DestroyMe` — RVA `0xc6d468`

- Decompiled symbol: `EnemyCounterForPack_DestroyMe`
- Metadata signature: `public void DestroyMe() { }`
- Native interval: `232` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab348;

void EnemyCounterForPack_DestroyMe(long long *a0)
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
    if (!(g_1fab348 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab348 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(a0[5], 0, 0) & 1))
    {
        if (a0[5])
            GameObject__SetActive(a0[5], 1, 0);
        else
            sub_f7db74(0);
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Inequality(a0[6], 0, 0) & 1))
    {
        Component__get_gameObject(a0, 0);
        if (!g_1ef0c58->field_e0)
        {
LABEL_106d530:
            sub_f7da5c();
        }
    }
    else if (!(g_1ef0c58->field_e0))
    {
        goto LABEL_106d530;
    }
    Object__Destroy();
    return;
}
```

## `EnemyCounterForPack.ctor` — RVA `0xc6d550`

- Decompiled symbol: `EnemyCounterForPack_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long EnemyCounterForPack_ctor(void)
{
}
```
