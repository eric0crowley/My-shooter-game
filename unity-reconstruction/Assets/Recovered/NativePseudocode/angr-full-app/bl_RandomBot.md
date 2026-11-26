# Native pseudocode: bl_RandomBot

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_RandomBot.FixedUpdate` — RVA `0xccb4dc`

- Decompiled symbol: `bl_RandomBot_FixedUpdate`
- Metadata signature: `private void FixedUpdate() { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
unsigned long long bl_RandomBot_FixedUpdate(long long a0)
{
    unsigned long long v0;  // x0
    unsigned long long v1;  // x0

    if (bl_RandomBot__get_Agent())
    {
        v0 = NavMeshAgent__get_hasPath();
        if (!((char)v0 & 1))
        {
            v1 = bl_RandomBot__RandomBot(a0);
            return bl_RandomBot__RandomBot(a0);
        }
        return v0;
    }
    sub_f7db74();
}
```

## `bl_RandomBot.get_Agent` — RVA `0xccb510`

- Decompiled symbol: `bl_RandomBot_get_Agent`
- Metadata signature: `private NavMeshAgent get_Agent() { }`
- Native interval: `168` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[40];
    long long field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efd038;
extern char g_1fab589;

long long bl_RandomBot_get_Agent(struct_1 *ptr)
{
    long long v0;  // x0

    if (!(g_1fab589 & 1))
    {
        sub_f7d92c(&g_1efd038);
        sub_f7d92c(&g_1ef0c58);
        g_1fab589 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(ptr->field_28, 0, 0) & 1))
    {
        v0 = sub_1231bc8(ptr, g_1efd038);
        ptr->field_28 = v0;
        sub_f7d8d0((struct struct_1 *)&ptr->field_28, v0);
    }
    return ptr->field_28;
}
```

## `bl_RandomBot.RandomBot` — RVA `0xccb5b8`

- Decompiled symbol: `bl_RandomBot_RandomBot`
- Metadata signature: `private void RandomBot() { }`
- Native interval: `208` bytes
- Result: `pseudocode`

```c
long long bl_RandomBot_RandomBot(unsigned long a0)
{
    unsigned long long v3;  // x0
    int choice;  // [bp-0x60]
    uint128_t flag2;  // [bp-0x50]
    unsigned int flag;  // [bp-0x40]

    flag = 0;
    choice = 0;
    flag2 = 0;
    Random__get_insideUnitSphere(0);
    if (Component__get_transform(a0, 0))
    {
        Transform__get_position();
        NavMesh__SamplePosition(&choice, 1, 0);
        NavMeshHit__get_position(&choice, 0);
        if (bl_RandomBot__get_Agent(a0))
        {
            v3 = NavMeshAgent__SetDestination();
            return NavMeshAgent__SetDestination();
        }
    }
    sub_f7db74();
}
```

## `bl_RandomBot.ctor` — RVA `0xccb688`

- Decompiled symbol: `bl_RandomBot_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned int field_20;
} struct_0;

long long bl_RandomBot_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_20 = 0x42480000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
