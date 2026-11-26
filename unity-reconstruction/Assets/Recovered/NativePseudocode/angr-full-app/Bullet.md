# Native pseudocode: Bullet

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `Bullet.OnEnable` — RVA `0xc67958`

- Decompiled symbol: `Bullet_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

extern long long g_1efd080;
extern char g_1fab30f;

void Bullet_OnEnable(struct_0 *ptr)
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
    if (!(g_1fab30f & 1))
    {
        sub_f7d92c(&g_1efd080);
        g_1fab30f = 1;
    }
    ptr->field_28 = sub_1231bc8(ptr, g_1efd080);
    sub_f7d8d0();
    return;
}
```

## `Bullet.Init` — RVA `0xc679b0`

- Decompiled symbol: `Bullet_Init`
- Metadata signature: `public void Init(Gun gun) { }`
- Native interval: `48` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Bullet_Recovered` matched 3 offsets against `Bullet` metadata (confidence 1.00).

```c
typedef struct Bullet_Recovered {
    char padding_0[32];
    unsigned long long gun;
    char padding_28[12];
    unsigned int lifetime;
    char padding_38[12];
    unsigned int speed;
} Bullet_Recovered;

long long Bullet_Init(struct_0 *p, unsigned long a1)
{
    struct_0 *ptr;  // x19
    unsigned long v1;  // x0

    p->field_20 = a1;
    ptr = &p->field_20;
    v1 = sub_f7d8d0(ptr);
    *((unsigned int *)&ptr->padding_0[20]) = 0;
    *((int *)((char *)&ptr->field_20 + 4)) = [D] unsupported_Iop_ZeroHI96ofV128();
    return v1;
}
```

## `Bullet.GetGun` — RVA `0xc679e0`

- Decompiled symbol: `Bullet_GetGun`
- Metadata signature: `public Gun GetGun() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

long long Bullet_GetGun(struct_0 *a0)
{
    return a0->field_20;
}
```

## `Bullet.FixedUpdate` — RVA `0xc679e8`

- Decompiled symbol: `Bullet_FixedUpdate`
- Metadata signature: `private void FixedUpdate() { }`
- Native interval: `452` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Bullet_Recovered` matched 6 offsets against `Bullet` metadata (confidence 1.00).

```c
typedef struct Bullet_Recovered {
    char padding_0[40];
    long long rigidBody;
    unsigned int maxLifetime;
    unsigned int lifetime;
    char padding_38[4];
    unsigned int maxSpeed;
    unsigned int accel;
    unsigned int speed;
} Bullet_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab310;

int Bullet_FixedUpdate(struct_1 *ptr)
{
    unsigned int v0;  // s1
    unsigned int v1;  // s0
    unsigned int v10;  // s0
    unsigned long v11;  // 4146
    unsigned int v2;  // s0
    unsigned long v3;  // 4163
    long long v4;  // x0
    long long v5;  // x20
    unsigned int v6;  // s11
    unsigned int v7;  // s0
    unsigned int v8;  // w0
    unsigned int v9;  // s1

    if (!(g_1fab310 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab310 = 1;
    }
    Time__get_deltaTime(0);
    v0 = ptr->field_3c;
    v2 = ptr->field_44 + v1 * ptr->field_40;
    ptr->field_44 = v2;
    v3 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v2, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v0) & 1)) & ((unsigned long long)(char)(CmpF(v2, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v3))
        ptr->field_44 = v0;
    v4 = Component__get_transform(ptr, 0);
    if (v4)
    {
        v5 = v4;
        Transform__get_position();
        Transform__get_forward(v5, 0);
        Time__get_deltaTime(0);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v6 = v2 + v2 * ptr->field_44 * v2;
        if (!((char)Object__op_Inequality(ptr->field_28, 0, 0) & 1))
        {
            v7 = v6;
            Transform__set_position(v5, 0);
        }
        else if (ptr->field_28)
        {
            v7 = v6;
            Rigidbody__MovePosition(ptr->field_28, 0);
        }
        else
        {
            sub_f7db74();
        }
        v8 = Time__get_deltaTime(0);
        v9 = ptr->field_30;
        v10 = ptr->field_34 + v7;
        ptr->field_34 = v10;
        v11 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v10, v9)) >> 5 & 3 | (unsigned long long)(CmpF(v10, v9) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v10, v9)) >> 5 & 3 | (unsigned long long)(CmpF(v10, v9) & 1)) & ((unsigned long long)(char)(CmpF(v10, v9)) >> 5 & 3 | (unsigned long long)(CmpF(v10, v9) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v11)
            return v8;
        Component__get_gameObject(ptr, 0);
        if (g_1ef0c58->field_e0)
            return Object__Destroy();
        sub_f7da5c(g_1ef0c58);
        return Object__Destroy();
    }
    sub_f7db74();
}
```

## `Bullet.ctor` — RVA `0xc67bac`

- Decompiled symbol: `Bullet_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `36` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Bullet_Recovered` matched 3 offsets against `Bullet` metadata (confidence 1.00).

```c
typedef struct Bullet_Recovered {
    char padding_0[48];
    unsigned int maxLifetime;
    char padding_34[4];
    unsigned long long initialSpeed;
    unsigned int accel;
} Bullet_Recovered;

long long Bullet_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_30 = 0x40a00000;
    ptr->field_38 = 0x41f0000041a00000;
    ptr->field_40 = 0x41a00000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
