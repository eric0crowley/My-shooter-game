# Native pseudocode: WeaponSpawn

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `WeaponSpawn.Start` — RVA `0xc94f74`

- Decompiled symbol: `WeaponSpawn_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[56];
    unsigned int field_38;
} struct_0;

struct_0 * WeaponSpawn_Start(struct_0 *ptr)
{
    ptr->field_38 = 0;
    return ptr;
}
```

## `WeaponSpawn.Update` — RVA `0xc94f7c`

- Decompiled symbol: `WeaponSpawn_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `216` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponSpawn_Recovered` matched 3 offsets against `WeaponSpawn` metadata (confidence 1.00).

```c
typedef struct WeaponSpawn_Recovered {
    char padding_0[40];
    unsigned int spawnTime;
    char padding_2c[4];
    long long gunInstance;
    unsigned int timeLeft;
} WeaponSpawn_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab471;

long long WeaponSpawn_Update(struct_1 *ptr)
{
    unsigned int v0;  // s1
    unsigned int v1;  // s0
    unsigned long v2;  // 4137
    unsigned long v3;  // 4129
    long long v4;  // x0
    long long v5;  // x0

    if (!(g_1fab471 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab471 = 1;
    }
    v0 = ptr->field_38;
    v1 = ptr->field_28;
    v2 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) & ((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v2))
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Implicit(ptr->field_30, 0) & 1))
        {
            v1 = ptr->field_28;
            goto LABEL_1094fec;
        }
        else
        {
            v1 = ptr->field_38;
            v3 = arm64g_calculate_condition(128, (((((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v3))
            {
                ptr->field_38 = 0;
                WeaponSpawn__Spawn(ptr);
            }
        }
    }
    else
    {
LABEL_1094fec:
        ptr->field_38 = v1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v4 = Object__op_Implicit(ptr->field_30, 0);
    if (((char)v4 & 1))
        return v4;
    v5 = Time__get_deltaTime(0);
    ptr->field_38 = ptr->field_38 - v1;
    return v5;
}
```

## `WeaponSpawn.Spawn` — RVA `0xc95054`

- Decompiled symbol: `WeaponSpawn_Spawn`
- Metadata signature: `private void Spawn() { }`
- Native interval: `288` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponSpawn_Recovered` matched 4 offsets against `WeaponSpawn` metadata (confidence 1.00).

```c
typedef struct WeaponSpawn_Recovered {
    char padding_0[32];
    long long gunPrefab;
    unsigned int spawnTime;
    char padding_2c[4];
    long long gunInstance;
    unsigned int timeLeft;
} WeaponSpawn_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1f00260;
extern char g_1fab472;

long long WeaponSpawn_Spawn(struct_1 *ptr)
{
    long long v0;  // x0
    struct_1 *p;  // x19
    unsigned long v2;  // x0

    if (!(g_1fab472 & 1))
    {
        sub_f7d92c(&g_1f00260);
        sub_f7d92c(&g_1ef0c58);
        g_1fab472 = 1;
    }
    if (Component__get_transform(ptr, 0))
    {
        Transform__get_position();
        if (Component__get_transform(ptr, 0))
        {
            Transform__get_rotation();
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v0 = sub_112a1ac(ptr->field_20, g_1f00260);
            ptr->field_30 = v0;
            p = &ptr->field_30;
            v2 = sub_f7d8d0(p, v0);
            *((int *)&p->padding_0[8]) = *((int *)&p->padding_0[8]);
            return v2;
        }
    }
    sub_f7db74();
}
```

## `WeaponSpawn.ctor` — RVA `0xc95174`

- Decompiled symbol: `WeaponSpawn_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned int field_28;
} struct_0;

long long WeaponSpawn_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_28 = 0x41f00000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
