# Native pseudocode: InputRig.EmulatedTouchState

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InputRig.EmulatedTouchState.ctor` — RVA `0xc3ece4`

- Decompiled symbol: `InputRig_EmulatedTouchState_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
long long InputRig_EmulatedTouchState_ctor(long long a0)
{
    unsigned long long v0;  // x0

    Object__ctor();
    v0 = InputRig_EmulatedTouchState__Reset(a0);
    return InputRig_EmulatedTouchState__Reset(a0);
}
```

## `InputRig.EmulatedTouchState.Reset` — RVA `0xc3ed00`

- Decompiled symbol: `InputRig_EmulatedTouchState_Reset`
- Metadata signature: `public void Reset() { }`
- Native interval: `48` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_EmulatedTouchState_Recovered` matched 2 offsets against `InputRig.EmulatedTouchState` metadata (confidence 1.00).

```c
typedef struct InputRig_EmulatedTouchState_Recovered {
    char padding_0[24];
    struct struct_3 *touch;
    char padding_20[68];
    char isUsed;
} InputRig_EmulatedTouchState_Recovered;

typedef struct struct_0 {
    char padding_0[376];
    struct struct_1 *field_178;
    unsigned long long field_180;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void InputRig_EmulatedTouchState_Reset(struct_2 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    struct_0 **v4;  // x0
    unsigned long long v5;  // x1
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr->field_18;
    ptr->field_64 = 0;
    if (!v4)
        sub_f7db74(0);
    v5 = *(v4)->field_180;
    *(v4)->field_178();
}
```

## `InputRig.EmulatedTouchState.IsUsed` — RVA `0xc3ed30`

- Decompiled symbol: `InputRig_EmulatedTouchState_IsUsed`
- Metadata signature: `public bool IsUsed() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[100];
    char field_64;
} struct_0;

long long InputRig_EmulatedTouchState_IsUsed(struct_0 *a0)
{
    return a0->field_64;
}
```

## `InputRig.EmulatedTouchState.IsActive` — RVA `0xc3ed38`

- Decompiled symbol: `InputRig_EmulatedTouchState_IsActive`
- Metadata signature: `public bool IsActive() { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    struct struct_0 *field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[28];
    char field_1c;
} struct_0;

long long InputRig_EmulatedTouchState_IsActive(struct_1 *a0)
{
    unsigned long v0;  // x0

    if (a0->field_18)
    {
        if (a0->field_18->field_1c)
            return 1;
        v0 = TouchGestureBasicState__JustReleasedRaw();
        return TouchGestureBasicState__JustReleasedRaw();
    }
    sub_f7db74(0);
}
```

## `InputRig.EmulatedTouchState.Start` — RVA `0xc3ed68`

- Decompiled symbol: `InputRig_EmulatedTouchState_Start`
- Metadata signature: `public void Start(Vector2 pos) { }`
- Native interval: `64` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_EmulatedTouchState_Recovered` matched 2 offsets against `InputRig.EmulatedTouchState` metadata (confidence 1.00).

```c
typedef struct InputRig_EmulatedTouchState_Recovered {
    char padding_0[24];
    long long touch;
    char padding_20[68];
    unsigned short isUsed;
} InputRig_EmulatedTouchState_Recovered;

long long InputRig_EmulatedTouchState_Start(struct_0 *ptr)
{
    long long v0;  // x0
    unsigned long long v1;  // x0

    v0 = ptr->field_18;
    ptr->field_64 = 257;
    if (v0)
    {
        v1 = TouchGestureBasicState__OnTouchStart(v0, 0, 0, 0);
        return TouchGestureBasicState__OnTouchStart(v0, 0, 0, 0);
    }
    sub_f7db74(0);
}
```

## `InputRig.EmulatedTouchState.UpdatePos` — RVA `0xc3eda8`

- Decompiled symbol: `InputRig_EmulatedTouchState_UpdatePos`
- Metadata signature: `public void UpdatePos(Vector2 pos) { }`
- Native interval: `36` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_EmulatedTouchState_Recovered` matched 2 offsets against `InputRig.EmulatedTouchState` metadata (confidence 1.00).

```c
typedef struct InputRig_EmulatedTouchState_Recovered {
    char padding_0[24];
    struct struct_1 *touch;
    char padding_20[69];
    char updatedThisFrame;
} InputRig_EmulatedTouchState_Recovered;

typedef struct struct_1 {
    char padding_0[176];
    unsigned int field_b0;
    unsigned int field_b4;
} struct_1;

void InputRig_EmulatedTouchState_UpdatePos(struct_0 *ptr)
{
    unsigned int p[46];  // x8
    unsigned int v1;  // s0
    unsigned int v2;  // s1

    p = ptr->field_18;
    ptr->field_65 = 1;
    if (p)
    {
        p[44] = v1;
        p[45] = v2;
        return;
    }
    sub_f7db74();
}
```

## `InputRig.EmulatedTouchState.EndTouch` — RVA `0xc3edcc`

- Decompiled symbol: `InputRig_EmulatedTouchState_EndTouch`
- Metadata signature: `public void EndTouch(bool cancel) { }`
- Native interval: `44` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_EmulatedTouchState_Recovered` matched 2 offsets against `InputRig.EmulatedTouchState` metadata (confidence 1.00).

```c
typedef struct InputRig_EmulatedTouchState_Recovered {
    char padding_0[24];
    long long touch;
    char padding_20[68];
    unsigned short isUsed;
} InputRig_EmulatedTouchState_Recovered;

long long InputRig_EmulatedTouchState_EndTouch(struct_0 *ptr, unsigned int a1)
{
    long long v0;  // x0
    unsigned long long v1;  // x0

    v0 = ptr->field_18;
    ptr->field_64 = 0x100;
    if (v0)
    {
        v1 = TouchGestureBasicState__OnTouchEnd(v0, a1 & 1, 0);
        return TouchGestureBasicState__OnTouchEnd(v0, a1 & 1, 0);
    }
    sub_f7db74(0);
}
```

## `InputRig.EmulatedTouchState.ctor` — RVA `0xc3edf8`

- Decompiled symbol: `InputRig_EmulatedTouchState_ctor`
- Metadata signature: `public void .ctor(int fingerId) { }`
- Native interval: `152` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

extern long long g_1ef1e08;
extern char g_1fab1e8;

long long InputRig_EmulatedTouchState_ctor(struct_0 *ptr, unsigned int a1)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x20]
    unsigned long long v2;  // [bp-0x18]
    unsigned long long v3;  // [bp-0x10]
    unsigned long long v4;  // [bp-0x8]

    v0 = v5;
    v1 = v6;
    v2 = v7;
    v3 = v8;
    v4 = v9;
    if (!(g_1fab1e8 & 1))
    {
        sub_f7d92c(&g_1ef1e08);
        g_1fab1e8 = 1;
    }
    Object__ctor(ptr, 0);
    ptr->field_10 = a1;
    TouchGestureBasicState__ctor(sub_f7db70(g_1ef1e08), 0); /* do not return */
}
```

## `InputRig.EmulatedTouchState.SyncOutputTouch` — RVA `0xc3ee90`

- Decompiled symbol: `InputRig_EmulatedTouchState_SyncOutputTouch`
- Metadata signature: `private void SyncOutputTouch() { }`
- Native interval: `200` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    struct struct_0 *field_18;
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    uint128_t field_30;
    unsigned int field_40;
    unsigned int field_44;
} struct_1;

typedef struct struct_0 {
    char padding_0[28];
    char field_1c;
    char padding_1d[23];
    unsigned long long field_34;
} struct_0;

unsigned long long InputRig_EmulatedTouchState_SyncOutputTouch(struct_1 *ptr)
{
    struct_0 *v0;  // x0
    unsigned int v1;  // s0
    unsigned int v2;  // w8
    unsigned int v3;  // s1
    unsigned int v4;  // s1
    unsigned long v6;  // 4174
    int v7;  // q0
    unsigned long long v8;  // x0

    ptr->field_28 = ptr->field_10;
    Time__get_unscaledDeltaTime(0);
    v0 = ptr->field_18;
    ptr->field_24 = v1;
    ptr->field_2c = 0;
    if (v0)
    {
        if (((char)TouchGestureBasicState__JustPressedRaw(v0, 0) & 1))
        {
            v2 = 0;
            goto LABEL_103ef28;
        }
        v0 = ptr->field_18;
        if (v0)
        {
            if (((char)TouchGestureBasicState__JustReleasedRaw(v0, 0) & 1))
            {
                v2 = 3;
                goto LABEL_103ef28;
            }
            else
            {
                v0 = ptr->field_18;
                if (v0)
                {
                    if (v0->field_1c)
                    {
                        TouchGestureBasicState__GetDeltaVecRaw();
                        v4 = v3 * v3;
                        v6 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v1 * v1 + v4, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v1 * v1 + v4, 981668463) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1 * v1 + v4, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v1 * v1 + v4, 981668463) & 1)) & ((unsigned long long)(char)(CmpF(v1 * v1 + v4, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v1 * v1 + v4, 981668463) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if ((char)v6)
                            v2 = 2;
                        else
                            v2 = 1;
                    }
                    else
                    {
                        v2 = 4;
                    }
LABEL_103ef28:
                    v0 = ptr->field_18;
                    ptr->field_20 = v2;
                    if (v0)
                    {
                        v7 = (int)_INSERT(*((long long *)&(&v0->padding_1d)[1]), 8, *((long long *)&(&v0->padding_1d)[1]));
                        *((void*)&ptr->field_30) = v7;
                        v8 = TouchGestureBasicState__GetDeltaVecRaw(v0, 0);
                        ptr->field_40 = *((unsigned int *)&v7);
                        ptr->field_44 = v4;
                        return v8;
                    }
                }
            }
        }
    }
    sub_f7db74(v0);
}
```

## `InputRig.EmulatedTouchState.Update` — RVA `0xc3ef58`

- Decompiled symbol: `InputRig_EmulatedTouchState_Update`
- Metadata signature: `public void Update() { }`
- Native interval: `80` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_EmulatedTouchState_Recovered` matched 2 offsets against `InputRig.EmulatedTouchState` metadata (confidence 1.00).

```c
typedef struct InputRig_EmulatedTouchState_Recovered {
    char padding_0[24];
    long long touch;
    char padding_20[68];
    unsigned short isUsed;
} InputRig_EmulatedTouchState_Recovered;

void InputRig_EmulatedTouchState_Update(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    struct_0 **v4;  // x0
    unsigned long v5;  // x1
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    if ((char)ptr->field_64 && !*((char *)&ptr->field_64 + 1))
        InputRig_EmulatedTouchState__EndTouch(ptr, 0);
    v4 = ptr->field_18;
    if (!ptr->field_18)
        sub_f7db74(0);
    v5 = *((long long *)(*((long long *)ptr->field_18) + 400));
    (*((long long *)(*((long long *)ptr->field_18) + 392)))();
}
```
