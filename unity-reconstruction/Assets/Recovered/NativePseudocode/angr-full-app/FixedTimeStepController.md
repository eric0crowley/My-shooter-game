# Native pseudocode: FixedTimeStepController

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `FixedTimeStepController.ctor` — RVA `0xc5b188`

- Decompiled symbol: `FixedTimeStepController_ctor`
- Metadata signature: `public void .ctor(int framesPerSecond) { }`
- Native interval: `72` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FixedTimeStepController_Recovered` matched 4 offsets against `FixedTimeStepController` metadata (confidence 1.00).

```c
typedef struct FixedTimeStepController_Recovered {
    char padding_0[16];
    unsigned int fixedTime;
    unsigned int fixedDeltaTime;
    unsigned int fixedDeltaTimeCombined;
    char padding_1c[4];
    unsigned long long totalFrameCount;
} FixedTimeStepController_Recovered;

void FixedTimeStepController_ctor(struct_0 *ptr, int a1)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    int v6;  // w19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    v6 = a1;
    Object__ctor();
    if (1 >= v6)
        v6 = 1;
    ptr->field_10 = 0;
    ptr->field_20 = 0;
    ptr->field_14 = 0x3f800000 / v6;
    ptr->field_18 = 0;
    return;
}
```

## `FixedTimeStepController.SetFPS` — RVA `0xc5b1d0`

- Decompiled symbol: `FixedTimeStepController_SetFPS`
- Metadata signature: `public void SetFPS(int framesPerSecond) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

struct_0 * FixedTimeStepController_SetFPS(struct_0 *ptr, int a1)
{
    if (1 >= a1)
        a1 = 1;
    ptr->field_14 = 0x3f800000 / a1;
    return ptr;
}
```

## `FixedTimeStepController.Reset` — RVA `0xc5b1ec`

- Decompiled symbol: `FixedTimeStepController_Reset`
- Metadata signature: `public void Reset() { }`
- Native interval: `16` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FixedTimeStepController_Recovered` matched 3 offsets against `FixedTimeStepController` metadata (confidence 1.00).

```c
typedef struct FixedTimeStepController_Recovered {
    char padding_0[16];
    unsigned int fixedTime;
    char padding_14[4];
    unsigned int fixedDeltaTimeCombined;
    char padding_1c[4];
    unsigned long long totalFrameCount;
} FixedTimeStepController_Recovered;

struct_0 * FixedTimeStepController_Reset(struct_0 *ptr)
{
    ptr->field_10 = 0;
    ptr->field_20 = 0;
    ptr->field_18 = 0;
    return ptr;
}
```

## `FixedTimeStepController.GetDeltaTime` — RVA `0xc5b1fc`

- Decompiled symbol: `FixedTimeStepController_GetDeltaTime`
- Metadata signature: `public float GetDeltaTime() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long FixedTimeStepController_GetDeltaTime(unsigned long a0)
{
    return a0;
}
```

## `FixedTimeStepController.GetDeltaTimeCombined` — RVA `0xc5b204`

- Decompiled symbol: `FixedTimeStepController_GetDeltaTimeCombined`
- Metadata signature: `public float GetDeltaTimeCombined() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long FixedTimeStepController_GetDeltaTimeCombined(unsigned long a0)
{
    return a0;
}
```

## `FixedTimeStepController.GetFrameCount` — RVA `0xc5b20c`

- Decompiled symbol: `FixedTimeStepController_GetFrameCount`
- Metadata signature: `public int GetFrameCount() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned int field_20;
} struct_0;

int FixedTimeStepController_GetFrameCount(struct_0 *a0)
{
    return a0->field_20;
}
```

## `FixedTimeStepController.GetFrameSteps` — RVA `0xc5b214`

- Decompiled symbol: `FixedTimeStepController_GetFrameSteps`
- Metadata signature: `public int GetFrameSteps() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[36];
    unsigned int field_24;
} struct_0;

int FixedTimeStepController_GetFrameSteps(struct_0 *a0)
{
    return a0->field_24;
}
```

## `FixedTimeStepController.GetTime` — RVA `0xc5b21c`

- Decompiled symbol: `FixedTimeStepController_GetTime`
- Metadata signature: `public float GetTime() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long FixedTimeStepController_GetTime(unsigned long a0)
{
    return a0;
}
```

## `FixedTimeStepController.Update` — RVA `0xc5b224`

- Decompiled symbol: `FixedTimeStepController_Update`
- Metadata signature: `public void Update(float deltaTime) { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1eef940;
extern char g_1fab2aa;

unsigned int [10] FixedTimeStepController_Update(unsigned int *ptr)
{
    unsigned int v0;  // s1
    unsigned int v1;  // w8
    unsigned int v2;  // s0
    unsigned int v3;  // s0
    unsigned long v4;  // 4183
    unsigned int v5;  // s2
    unsigned long v6;  // 4157
    unsigned int v7[10];  // x0
    unsigned int v8[10];  // x0

    v0 = ptr[5];
    v1 = 0;
    v3 = ptr[7] + v2;
    ptr[6] = 0;
    ptr[7] = v3;
    ptr[9] = 0;
    v4 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v3, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v0) & 1)) & ((unsigned long long)(char)(CmpF(v3, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v4))
    {
        v1 = 0;
        v5 = 0;
        do
        {
            v3 -= v0;
            v5 += v0;
            v1 += 1;
            v6 = arm64g_calculate_condition(192, (((((unsigned long long)(char)(CmpF(v3, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v0) & 1)) & ((unsigned long long)(char)(CmpF(v3, v0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, v0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        } while ((char)v6);
        ptr[9] = v1;
        ptr[6] = v5;
        ptr[7] = v3;
    }
    ptr[8] = v1 + ptr[8];
    v7 = ptr;
    if (!(g_1fab2aa & 1))
    {
        v8 = sub_f7d92c(&g_1eef940);
        g_1fab2aa = 1;
        v0 = ptr[5];
        v7 = v8;
    }
    g_1eef940->field_b8->field_0 = v0;
    return v7;
}
```

## `FixedTimeStepController.SetStaticData` — RVA `0xc5b2c8`

- Decompiled symbol: `FixedTimeStepController_SetStaticData`
- Metadata signature: `public void SetStaticData() { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_1;

extern struct_1 *g_1eef940;
extern char g_1fab2aa;

struct_0 * FixedTimeStepController_SetStaticData(struct_0 *idx)
{
    struct_0 *v0;  // x0
    struct_0 *v1;  // x0

    v0 = idx;
    if (!(g_1fab2aa & 1))
    {
        v1 = sub_f7d92c(&g_1eef940);
        g_1fab2aa = 1;
        v0 = v1;
    }
    g_1eef940->field_b8->field_0 = idx->field_14;
    return v0;
}
```

## `FixedTimeStepController.Execute` — RVA `0xc5b318`

- Decompiled symbol: `FixedTimeStepController_Execute`
- Metadata signature: `public void Execute(Action updateCallback) { }`
- Native interval: `160` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FixedTimeStepController_Recovered` matched 2 offsets against `FixedTimeStepController` metadata (confidence 1.00).

```c
typedef struct FixedTimeStepController_Recovered {
    char padding_0[20];
    unsigned int fixedDeltaTime;
    char padding_18[12];
    int frameSteps;
} FixedTimeStepController_Recovered;

typedef struct struct_3 {
    char padding_0[24];
    struct struct_4 *field_18;
    char padding_20[8];
    unsigned long long field_28;
    char padding_30[16];
    unsigned long long field_40;
} struct_3;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_1;

extern struct_1 *g_1eef940;
extern char g_1fab2aa;

struct_0 * FixedTimeStepController_Execute(struct_0 *ptr, struct_3 *p)
{
    unsigned int v0;  // w8
    struct_0 *v1;  // x0
    struct_0 *v2;  // x0
    struct_0 *v3;  // x0
    unsigned long long v4;  // x0
    unsigned long long v5;  // x1

    v0 = ptr->field_24;
    if (v0 < 1)
        return ptr;
    v1 = ptr;
    if (!(g_1fab2aa & 1))
    {
        v2 = sub_f7d92c(&g_1eef940);
        g_1fab2aa = 1;
        v0 = ptr->field_24;
        v1 = v2;
    }
    v3 = v1;
    g_1eef940->field_b8->field_0 = ptr->field_14;
    if (v0 < 1)
    {
        return v3;
    }
    else if (p)
    {
        v4 = p->field_40;
        v5 = p->field_28;
        p->field_18();
    }
    else
    {
        sub_f7db74();
    }
}
```
