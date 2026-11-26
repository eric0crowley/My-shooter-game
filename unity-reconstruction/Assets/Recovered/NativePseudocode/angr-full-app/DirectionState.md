# Native pseudocode: DirectionState

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DirectionState.ctor` — RVA `0xc5ae6c`

- Decompiled symbol: `DirectionState_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
void DirectionState_ctor(unsigned long long *ptr)
{
    Object__ctor();
    ptr[2] = 0;
    ptr[3] = 0;
    return;
}
```

## `DirectionState.Reset` — RVA `0xc5ae88`

- Decompiled symbol: `DirectionState_Reset`
- Metadata signature: `public void Reset() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
unsigned long long [4] DirectionState_Reset(unsigned long long *ptr)
{
    ptr[2] = 0;
    ptr[3] = 0;
    return ptr;
}
```

## `DirectionState.GetCur` — RVA `0xc5ae90`

- Decompiled symbol: `DirectionState_GetCur`
- Metadata signature: `public Dir GetCur() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

int DirectionState_GetCur(struct_0 *a0)
{
    return a0->field_10;
}
```

## `DirectionState.GetPrev` — RVA `0xc5ae98`

- Decompiled symbol: `DirectionState_GetPrev`
- Metadata signature: `public Dir GetPrev() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

int DirectionState_GetPrev(struct_0 *a0)
{
    return a0->field_14;
}
```

## `DirectionState.GetOriginal` — RVA `0xc5aea0`

- Decompiled symbol: `DirectionState_GetOriginal`
- Metadata signature: `public Dir GetOriginal() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

int DirectionState_GetOriginal(struct_0 *a0)
{
    return a0->field_18;
}
```

## `DirectionState.GetPrevOriginal` — RVA `0xc5aea8`

- Decompiled symbol: `DirectionState_GetPrevOriginal`
- Metadata signature: `public Dir GetPrevOriginal() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[28];
    unsigned int field_1c;
} struct_0;

int DirectionState_GetPrevOriginal(struct_0 *a0)
{
    return a0->field_1c;
}
```

## `DirectionState.JustPressed` — RVA `0xc5aeb0`

- Decompiled symbol: `DirectionState_JustPressed`
- Metadata signature: `public bool JustPressed(Dir dir) { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

unsigned long long DirectionState_JustPressed(struct_0 *a0, unsigned int a1)
{
    if (*((int *)&a0[1].padding_0[0]) == a1)
    {
        return 0;
    }
    else if (a0->field_10 != a1)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `DirectionState.JustReleased` — RVA `0xc5aed4`

- Decompiled symbol: `DirectionState_JustReleased`
- Metadata signature: `public bool JustReleased(Dir dir) { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

unsigned long long DirectionState_JustReleased(struct_0 *a0, unsigned int a1)
{
    if (*((int *)&a0[1].padding_0[0]) != a1)
    {
        return 0;
    }
    else if (a0->field_10 == a1)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `DirectionState.BeginFrame` — RVA `0xc5aef8`

- Decompiled symbol: `DirectionState_BeginFrame`
- Metadata signature: `public void BeginFrame() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
unsigned int [8] DirectionState_BeginFrame(unsigned int *ptr)
{
    unsigned int v0;  // w9

    v0 = ptr[6];
    ptr[5] = ptr[4];
    ptr[7] = v0;
    return ptr;
}
```

## `DirectionState.SetDir` — RVA `0xc5af0c`

- Decompiled symbol: `DirectionState_SetDir`
- Metadata signature: `public void SetDir(Dir dir, DirectionState.OriginalDirResetMode resetMode) { }`
- Native interval: `200` bytes
- Result: `pseudocode`

```c
extern char g_1fab2cd;

unsigned int [57] DirectionState_SetDir(unsigned int *ptr, long long a1, unsigned int a2)
{
    unsigned int v0;  // w8
    unsigned int v1;  // w21
    unsigned int v2[57];  // x0
    unsigned long v3;  // 4121
    unsigned int v4;  // w10
    unsigned int v5;  // w8

    v0 = ptr[5];
    ptr[4] = a1;
    if (v0 == (int)a1)
    {
        return ptr;
    }
    else if (!(int)a1)
    {
        ptr[6] = 0;
        return ptr;
    }
    else if (!v0)
    {
        ptr[6] = a1;
        return ptr;
    }
    else if (a2)
    {
        v1 = CFUtils__DirDeltaAngle(ptr[7], a1);
        if (!g_1fab2cd)
        {
            sub_f7d92c("_F");
            g_1fab2cd = 1;
        }
        v2 = g_1ef07e8;
        if (!g_1ef07e8->field_e0)
            v2 = sub_f7da5c(g_1ef07e8);
        v3 = arm64g_calculate_condition(83, (unsigned long long)v1, 0, 0);
        if ((char)v3)
            v4 = v1;
        else
            v4 = -(v1);
        if (a2 == 2)
            v5 = 135;
        else
            v5 = 180;
        if (a2 == 3)
            v5 = 90;
        if (v4 < v5)
            return v2;
        ptr[6] = ptr[4];
        return v2;
    }
    else
    {
        return ptr;
    }
}
```
