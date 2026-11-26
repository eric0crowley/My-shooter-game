# Native pseudocode: starFxController

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `starFxController.Awake` — RVA `0xc760ec`

- Decompiled symbol: `starFxController_Awake`
- Metadata signature: `private void Awake() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
extern char g_1fab3a5;

void starFxController_Awake(unsigned long a0)
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
    if (!(g_1fab3a5 & 1))
    {
        sub_f7d92c("'c");
        g_1fab3a5 = 1;
    }
    g_1ef2b20->field_b8->field_0 = a0;
    sub_f7d8d0();
    return;
}
```

## `starFxController.Start` — RVA `0xc76144`

- Decompiled symbol: `starFxController_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long starFxController_Start(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = starFxController__Reset();
    return starFxController__Reset();
}
```

## `starFxController.Reset` — RVA `0xc76148`

- Decompiled symbol: `starFxController_Reset`
- Metadata signature: `public void Reset() { }`
- Native interval: `168` bytes
- Result: `pseudocode`
- Heuristic layout hint: `starFxController_Recovered` matched 5 offsets against `starFxController` metadata (confidence 1.00).

```c
typedef struct starFxController_Recovered {
    char padding_0[32];
    struct struct_0 *starFX;
    char padding_28[4];
    unsigned int currentEa;
    unsigned int delay;
    unsigned int currentDelay;
    char isEnd;
} starFxController_Recovered;

typedef struct struct_4 {
    char padding_0[24];
    unsigned int field_18;
} struct_4;

typedef struct struct_2 {
    char padding_0[32];
    long long field_20;
} struct_2;

typedef struct struct_3 {
    char padding_0[32];
    long long field_20;
} struct_3;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

struct_1 * starFxController_Reset(struct_1 *ptr)
{
    unsigned long long v0;  // x20
    struct_1 *v1;  // x0
    struct_1 *v2;  // x0
    struct_4 *v3;  // x8
    struct_2 *v4;  // x8
    unsigned int v5;  // s0
    unsigned long long v6;  // x20
    struct_4 *v7;  // x8
    struct_3 *v8;  // x8

    v0 = 0;
    v1 = ptr;
    while (true)
    {
        v3 = ptr->field_20;
        if (!v3)
            break;
        if (v3->field_18 <= v0)
            sub_f7db7c(v1);
        v4 = &v3->padding_0[8 * v0];
        if (!v4->field_20)
            break;
        v2 = GameObject__SetActive(v4->field_20, 0, 0);
        v0 += 1;
        v1 = v2;
        if (v0 == 3)
        {
            v5 = ptr->field_30;
            v6 = 0;
            ptr->field_2c = 0;
            ptr->field_38 = 0;
            ptr->field_34 = v5;
            while (true)
            {
                v7 = ptr->field_20;
                if (!v7)
                    break;
                if (v7->field_18 <= v6)
                    sub_f7db7c(v2);
                v8 = &v7->padding_0[8 * v6];
                if (!v8->field_20)
                    break;
                v2 = GameObject__SetActive(v8->field_20, 0, 0);
                v6 += 1;
                if (v6 == 3)
                    return v2;
            }
            break;
        }
    }
    sub_f7db7c(sub_f7db74());
}
```

## `starFxController.Update` — RVA `0xc761f0`

- Decompiled symbol: `starFxController_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `272` bytes
- Result: `pseudocode`
- Heuristic layout hint: `starFxController_Recovered` matched 5 offsets against `starFxController` metadata (confidence 1.00).

```c
typedef struct starFxController_Recovered {
    char padding_0[32];
    struct struct_0 *starFX;
    char padding_28[4];
    unsigned int currentEa;
    unsigned int delay;
    unsigned int currentDelay;
    char isEnd;
} starFxController_Recovered;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

extern struct_0 *g_1eeed00;
extern char g_1fab3a6;

struct_1 * starFxController_Update(struct_1 *ptr)
{
    unsigned long v0;  // x0
    unsigned int v1;  // s0
    struct_1 *v10;  // x0
    unsigned int v2;  // s0
    unsigned long v3;  // 4142
    unsigned long v4;  // x8
    unsigned long long v5;  // x8
    unsigned int v6;  // s0
    unsigned long v7;  // x9
    struct_1 *v8;  // x8
    struct_1 *v9;  // x0

    if (!(g_1fab3a6 & 1))
    {
        sub_f7d92c(&g_1eeed00);
        g_1fab3a6 = 1;
    }
    if (!ptr->field_38)
    {
        v0 = Time__get_deltaTime(0);
        v2 = ptr->field_34 - v1;
        ptr->field_34 = v2;
        v3 = arm64g_calculate_condition(128, (((((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v3))
        {
            v4 = ptr->field_2c;
            v5 = v4 * 0x100000000 >> 63 & 0xffffffff00000000 | v4 & 4294967295;
            if ((unsigned int)v5 == ptr->padding_28)
            {
                v6 = ptr->field_30;
                ptr->field_38 = 1;
                ptr->field_2c = 0;
                ptr->field_34 = v6;
            }
            else
            {
                v7 = ptr->field_20;
                ptr->field_34 = ptr->field_30;
                if (!v7)
                {
                    v0 = sub_f7db74();
                    sub_f7db7c(v0);
                }
                else if (*((int *)(v7 + 24)) > (unsigned int)v5)
                {
                    v8 = v7 + v5 * 8;
                    if (!v8->field_20)
                    {
                        sub_f7db74();
                        sub_f7db7c(v0);
                    }
                    GameObject__SetActive(v8->field_20, 1, 0);
                    ptr->field_2c = ptr->field_2c + 1;
                }
                else
                {
                    sub_f7db7c(v0);
                }
            }
        }
    }
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    v9 = CF2Input__GetKeyDown(274, 0);
    if (!((char)v9 & 1))
        return v9;
    v10 = starFxController__Reset(ptr);
    return starFxController__Reset(ptr);
}
```

## `starFxController.ctor` — RVA `0xc76300`

- Decompiled symbol: `starFxController_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long starFxController_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
