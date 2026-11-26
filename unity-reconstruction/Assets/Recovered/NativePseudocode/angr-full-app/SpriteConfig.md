# Native pseudocode: SpriteConfig

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SpriteConfig.ctor` — RVA `0xc6344c`

- Decompiled symbol: `SpriteConfig_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `76` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SpriteConfig_Recovered` matched 6 offsets against `SpriteConfig` metadata (confidence 1.00).

```c
typedef struct SpriteConfig_Recovered {
    char padding_0[16];
    char enabled;
    char padding_11[15];
    uint128_t color;
    unsigned long long scale;
    char padding_38[11];
    char oneShotState;
    uint128_t duration;
    unsigned long long rotationTransitionFactor;
} SpriteConfig_Recovered;

void SpriteConfig_ctor(struct_0 *ptr)
{
    Object__ctor();
    ptr->field_10 = 1;
    *((unsigned long long *)&ptr->field_20) = 0x3f8000003f800000 CONCAT 0x3f8000003f800000;
    *((unsigned long long *)((char *)&ptr->field_44 + 4)) = 0x3f8000003f800000;
    ptr->field_30 = 0x3f800000;
    *((uint128_t *)&(&ptr->field_43)[1]) = 84405977751994456057500319505265249485;
    ptr->field_43 = 0;
    return;
}
```

## `SpriteConfig.ctor` — RVA `0xc63498`

- Decompiled symbol: `SpriteConfig_ctor`
- Metadata signature: `public void .ctor(Sprite sprite, Color color) { }`
- Native interval: `144` bytes
- Result: `pseudocode`

```c
long long SpriteConfig_ctor(void* p, long long a1)
{
    void* ptr;  // x20
    unsigned long v1;  // x0
    unsigned int v2;  // s0
    unsigned int v3;  // s1
    unsigned int v4;  // s2
    unsigned int v5;  // s3

    Object__ctor();
    *((long long *)&p[24]) = a1;
    ptr = p + 24;
    *((char *)&ptr[8]) = 1;
    *((unsigned long long *)&ptr[8]) = 0x3f8000003f800000 CONCAT 0x3f8000003f800000;
    *((unsigned long long *)&ptr[60]) = 0x3f8000003f800000;
    *((unsigned long long *)&ptr[24]) = 0x3f800000;
    *((uint128_t *)&ptr[44]) = 84405977751994456057500319505265249485;
    *((char *)&ptr[43]) = 0;
    v1 = sub_f7d8d0(ptr, a1);
    *((unsigned int *)&ptr[8]) = v2;
    *((unsigned int *)&ptr[12]) = v3;
    *((unsigned int *)&ptr[16]) = v4;
    *((unsigned int *)&ptr[20]) = v5;
    return v1;
}
```

## `SpriteConfig.ctor` — RVA `0xc63528`

- Decompiled symbol: `SpriteConfig_ctor`
- Metadata signature: `public void .ctor(bool enabled, bool oneShot, float scale) { }`
- Native interval: `108` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SpriteConfig_Recovered` matched 7 offsets against `SpriteConfig` metadata (confidence 1.00).

```c
typedef struct SpriteConfig_Recovered {
    char padding_0[16];
    char enabled;
    char padding_11[15];
    uint128_t color;
    unsigned int scale;
    unsigned int rotation;
    char padding_38[8];
    unsigned int resetOffset;
    uint128_t duration;
    unsigned long long rotationTransitionFactor;
} SpriteConfig_Recovered;

extern char g_1010101;

void SpriteConfig_ctor(struct_0 *ptr, char a1, unsigned int a2)
{
    unsigned int v0;  // s0

    Object__ctor();
    ptr->field_34 = 0;
    ptr->field_30 = v0;
    ptr->field_10 = a1 & 1;
    *((unsigned long long *)&ptr->field_20) = 0x3f8000003f800000 CONCAT 0x3f8000003f800000;
    *((unsigned long long *)((char *)&ptr->field_44 + 4)) = 0x3f8000003f800000;
    *((uint128_t *)&(&ptr->field_40)[1]) = 84405977751994456057500319505265249485;
    *((unsigned long *)&ptr->field_40) = &g_1010101 * (a2 & 1);
    return;
}
```
