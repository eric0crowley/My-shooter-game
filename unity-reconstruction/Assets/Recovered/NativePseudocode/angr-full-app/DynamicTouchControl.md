# Native pseudocode: DynamicTouchControl

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DynamicTouchControl.Pressed` — RVA `0xc44b14`

- Decompiled symbol: `DynamicTouchControl_Pressed`
- Metadata signature: `public bool Pressed() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[224];
    struct struct_0 *field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[28];
    char field_1c;
} struct_0;

long long DynamicTouchControl_Pressed(struct_1 *a0)
{
    if (a0->field_e0)
        return a0->field_e0->field_1c;
    sub_f7db74();
}
```

## `DynamicTouchControl.GetDynamicRegion` — RVA `0xc471f4`

- Decompiled symbol: `DynamicTouchControl_GetDynamicRegion`
- Metadata signature: `public DynamicRegion GetDynamicRegion() { }`
- Native interval: `24` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DynamicTouchControl_Recovered` matched 2 offsets against `DynamicTouchControl` metadata (confidence 1.00).

```c
typedef struct DynamicTouchControl_Recovered {
    char padding_0[192];
    unsigned long long targetDynamicRegion;
    char linkedToDynamicRegion;
} DynamicTouchControl_Recovered;

unsigned long long DynamicTouchControl_GetDynamicRegion(struct_0 *a0)
{
    if (!a0->field_c8)
        return 0;
    return a0->field_c0;
}
```

## `DynamicTouchControl.OnLinkToDynamicRegion` — RVA `0xc4720c`

- Decompiled symbol: `DynamicTouchControl_OnLinkToDynamicRegion`
- Metadata signature: `public void OnLinkToDynamicRegion(DynamicRegion dynRegion) { }`
- Native interval: `172` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DynamicTouchControl_Recovered` matched 2 offsets against `DynamicTouchControl` metadata (confidence 1.00).

```c
typedef struct DynamicTouchControl_Recovered {
    char padding_0[192];
    long long targetDynamicRegion;
    char linkedToDynamicRegion;
} DynamicTouchControl_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab231;

long long DynamicTouchControl_OnLinkToDynamicRegion(struct_1 *ptr, long long a1)
{
    long long v0;  // x0

    if (!(g_1fab231 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab231 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(a1, 0, 0) & 1))
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v0 = Object__op_Equality(a1, ptr->field_c0, 0);
    }
    else if (ptr)
    {
        v0 = 0;
    }
    else
    {
        sub_f7db74();
    }
    ptr->field_c8 = (char)v0 & 1;
    return v0;
}
```

## `DynamicTouchControl.get_TouchStateScreen` — RVA `0xc475c4`

- Decompiled symbol: `DynamicTouchControl_get_TouchStateScreen`
- Metadata signature: `public TouchGestureBasicState get_TouchStateScreen() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[216];
    unsigned long long field_d8;
} struct_0;

long long DynamicTouchControl_get_TouchStateScreen(struct_0 *a0)
{
    return a0->field_d8;
}
```

## `DynamicTouchControl.get_TouchStateOriented` — RVA `0xc475cc`

- Decompiled symbol: `DynamicTouchControl_get_TouchStateOriented`
- Metadata signature: `public TouchGestureBasicState get_TouchStateOriented() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[208];
    unsigned long long field_d0;
} struct_0;

long long DynamicTouchControl_get_TouchStateOriented(struct_0 *a0)
{
    return a0->field_d0;
}
```

## `DynamicTouchControl.get_TouchStateWorld` — RVA `0xc475d4`

- Decompiled symbol: `DynamicTouchControl_get_TouchStateWorld`
- Metadata signature: `public TouchGestureBasicState get_TouchStateWorld() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned long long field_e0;
} struct_0;

long long DynamicTouchControl_get_TouchStateWorld(struct_0 *a0)
{
    return a0->field_e0;
}
```

## `DynamicTouchControl.ctor` — RVA `0xc475dc`

- Decompiled symbol: `DynamicTouchControl_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `316` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DynamicTouchControl_Recovered` matched 6 offsets against `DynamicTouchControl` metadata (confidence 1.00).

```c
typedef struct DynamicTouchControl_Recovered {
    char padding_0[136];
    char fadeOutWhenReleased;
    char padding_89[7];
    unsigned long long fadeInDuration;
    unsigned int fadeOutDuration;
    unsigned short centerOnDirectTouch;
    char padding_9e[2];
    unsigned short clampInsideRegion;
    char padding_a2[22];
    unsigned int originSmoothTime;
} DynamicTouchControl_Recovered;

extern long long g_1ef1e08;
extern char g_1fab22f;

long long DynamicTouchControl_ctor(struct_0 *ptr)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]
    unsigned long long v5;  // [bp-0x8]

    v0 = v6;
    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    if (!(g_1fab22f & 1))
    {
        sub_f7d92c(&g_1ef1e08);
        g_1fab22f = 1;
    }
    ptr->field_88 = 1;
    ptr->field_98 = 0x3f000000;
    ptr->field_9c = 257;
    ptr->field_a0 = 257;
    ptr->field_90 = 4539628425434680525;
    ptr->field_b8 = 0x3f000000;
    TouchControl__ctor(ptr, 0); /* do not return */
}
```

## `DynamicTouchControl.OnInitControl` — RVA `0xc47718`

- Decompiled symbol: `DynamicTouchControl_OnInitControl`
- Metadata signature: `protected override void OnInitControl() { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
long long DynamicTouchControl_OnInitControl(long long a0)
{
    unsigned long long v0;  // x0

    DynamicTouchControl__SetTargetDynamicRegion();
    DynamicTouchControl__SetTouchSmoothing(a0);
    v0 = DynamicTouchControl__StoreDefaultPos(a0);
    return DynamicTouchControl__StoreDefaultPos(a0);
}
```

## `DynamicTouchControl.SetTargetDynamicRegion` — RVA `0xc47740`

- Decompiled symbol: `DynamicTouchControl_SetTargetDynamicRegion`
- Metadata signature: `public void SetTargetDynamicRegion(DynamicRegion targetDynamicRegion) { }`
- Native interval: `176` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab230;

long long DynamicTouchControl_SetTargetDynamicRegion(void* ptr, unsigned long a1)
{
    long long v0;  // x0
    long long v1;  // x0
    long long v2;  // x0

    if (!(g_1fab230 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab230 = 1;
    }
    *((unsigned long *)&ptr[192]) = a1;
    sub_f7d8d0(ptr + 192, a1);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Inequality(a1, 0, 0);
    if (!((char)v0 & 1))
        return v0;
    if (a1)
    {
        v1 = ComponentBase__CanBeUsed(a1, 0);
        if (!((char)v1 & 1))
            return v1;
        v2 = DynamicRegion__SetTargetControl(a1, ptr);
        return DynamicRegion__SetTargetControl(a1, ptr);
    }
    sub_f7db74();
}
```

## `DynamicTouchControl.SetTouchSmoothing` — RVA `0xc477f0`

- Decompiled symbol: `DynamicTouchControl_SetTouchSmoothing`
- Metadata signature: `public void SetTouchSmoothing(float smTime) { }`
- Native interval: `88` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DynamicTouchControl_Recovered` matched 4 offsets against `DynamicTouchControl` metadata (confidence 1.00).

```c
typedef struct DynamicTouchControl_Recovered {
    char padding_0[180];
    unsigned int touchSmoothing;
    char padding_b8[24];
    struct struct_0 *touchStateOriented;
    struct struct_1 *touchStateScreen;
    struct struct_2 *touchStateWorld;
} DynamicTouchControl_Recovered;

typedef struct struct_2 {
    char padding_0[164];
    unsigned int field_a4;
} struct_2;

typedef struct struct_0 {
    char padding_0[164];
    unsigned int field_a4;
} struct_0;

typedef struct struct_1 {
    char padding_0[164];
    unsigned int field_a4;
} struct_1;

void DynamicTouchControl_SetTouchSmoothing(struct_3 *ptr)
{
    struct_2 *p;  // x8
    unsigned int v1;  // s1
    unsigned int flag;  // s0
    unsigned int v3;  // s0
    unsigned long v4;  // 4142
    unsigned int v5;  // s0
    unsigned int v6;  // s0

    p = ptr->field_e0;
    v1 = [D] unsupported_Iop_ZeroHI96ofV128();
    flag = 0;
    v4 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v4)
        v5 = v1;
    else
        v5 = flag;
    ptr->field_b4 = v5;
    if (p)
    {
        v6 = v5 * 1036831949;
        p->field_a4 = v6;
        if (ptr->field_d0)
        {
            ptr->field_d0->field_a4 = v6;
            if (ptr->field_d8)
            {
                ptr->field_d8->field_a4 = v6;
                return;
            }
        }
    }
    sub_f7db74();
}
```

## `DynamicTouchControl.StoreDefaultPos` — RVA `0xc47848`

- Decompiled symbol: `DynamicTouchControl_StoreDefaultPos`
- Metadata signature: `protected void StoreDefaultPos() { }`
- Native interval: `752` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[240];
    long long field_f0;
    char padding_f8[64];
    long long field_138;
    unsigned int field_140;
    unsigned int field_144;
    unsigned int field_148;
    unsigned int field_14c;
    unsigned int field_150;
    unsigned int field_154;
    unsigned int field_158;
    unsigned int field_15c;
    unsigned int field_160;
    unsigned int field_164;
    unsigned int field_168;
    unsigned int field_16c;
    unsigned int field_170;
} struct_2;

typedef struct struct_4 {
    struct struct_3 *field_0;
    char padding_8[16];
    unsigned int field_18;
    char padding_1c[4];
    char field_20;
} struct_4;

typedef struct struct_3 {
    char padding_0[64];
    long long field_40;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern long long g_1eee3d8;
extern long long g_1eefaf0;
extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef1f08;
extern long long g_1efd060;
extern long long g_1efec98;
extern long long g_1f105c0;
extern char g_1fab233;

unsigned long long DynamicTouchControl_StoreDefaultPos(struct_2 *ptr)
{
    unsigned long long v0;  // x0
    struct_2 *p;  // x20
    long long v10;  // x0
    long long v11;  // x21
    long long v12;  // x0
    long long v13;  // x22
    long long v14;  // x0
    long long v15;  // x0
    struct_2 *v16;  // x20
    unsigned int v17;  // s0
    unsigned int v18;  // s1
    unsigned int v19;  // s2
    long long v2;  // x0
    unsigned long long v20;  // x0
    long long v3;  // x0
    struct_4 *v4;  // x22
    unsigned long v5;  // x0
    unsigned long v6;  // x23
    struct_4 *addr;  // x0
    long long v8;  // x0
    long long v9;  // x23

    if (!(g_1fab233 & 1))
    {
        sub_f7d92c(&g_1efd060);
        sub_f7d92c(&g_1efec98);
        sub_f7d92c(&g_1eefaf0);
        sub_f7d92c(")B");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1eee3d8);
        sub_f7d92c(&g_1ef1f08);
        sub_f7d92c(&g_1f105c0);
        g_1fab233 = 1;
    }
    v0 = CFUtils__get_editorStopped(0);
    if (((char)v0 & 1))
        return v0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    p = &ptr->field_138;
    if (((char)Object__op_Equality(ptr->field_138, 0, 0) & 1))
    {
        v2 = Object__get_name(ptr, 0);
        v3 = String__Concat(v2, g_1f105c0, 0);
        v4 = sub_f7d9d4(g_1eee3d8, 1);
        if (!g_1ef1f08->field_e0)
            sub_f7da5c(g_1ef1f08);
        v5 = Type__GetTypeFromHandle(g_1eeb600, 0);
        if (!v4)
            goto LABEL_1047b24;
        v6 = v5;
        if (v5 && (v5 = (unsigned long)sub_f7da60(v6, v4->field_0->field_40), !v5))
            goto LABEL_1047b2c;
        if (!v4->field_18)
            goto LABEL_1047b28;
        addr = v4;
        *((unsigned long *)&addr->field_20) = v6;
        sub_f7d8d0((struct struct_4 *)&addr->field_20, v6);
        v8 = sub_f7db70(g_1eefaf0);
        v9 = v8;
        GameObject__ctor(v8, v3, v4, 0);
        *((long long *)&p->padding_0[0]) = v9;
        sub_f7d8d0(p, v9);
    }
    v10 = sub_1231bc8(ptr, g_1efd060);
    if (ptr->field_138)
    {
        v11 = v10;
        v12 = GameObject__get_transform(ptr->field_138, 0);
        if (v11)
        {
            v13 = v12;
            v14 = Transform__get_parent(v11, 0);
            if (v13)
            {
                Transform__SetParent(v13, v14, 0, 0);
                if (*((long long *)&p->padding_0[0]))
                {
                    v15 = sub_1249224(*((long long *)&p->padding_0[0]), g_1efec98);
                    ptr->field_f0 = v15;
                    v16 = &ptr->field_f0;
                    sub_f7d8d0(v16, v15);
                    if (*((long long *)&v16->padding_0[72]))
                    {
                        Object__set_hideFlags(*((long long *)&v16->padding_0[72]), 61, 0);
                        RectTransform__get_anchorMin(v11, 0);
                        ptr->field_148 = v17;
                        ptr->field_14c = v18;
                        RectTransform__get_anchorMax(v11, 0);
                        ptr->field_140 = v17;
                        ptr->field_144 = v18;
                        RectTransform__get_offsetMin(v11, 0);
                        ptr->field_150 = v17;
                        ptr->field_154 = v18;
                        RectTransform__get_offsetMax(v11, 0);
                        ptr->field_158 = v17;
                        ptr->field_15c = v18;
                        RectTransform__get_anchoredPosition3D(v11, 0);
                        ptr->field_168 = v17;
                        ptr->field_16c = v18;
                        ptr->field_170 = v19;
                        RectTransform__get_pivot(v11, 0);
                        ptr->field_160 = v17;
                        ptr->field_164 = v18;
                        v20 = DynamicTouchControl__SetupInitialRectPosition(ptr);
                        return DynamicTouchControl__SetupInitialRectPosition(ptr);
                    }
                }
            }
        }
    }
LABEL_1047b24:
    v5 = sub_f7db74();
LABEL_1047b28:
    v5 = sub_f7db7c(v5);
LABEL_1047b2c:
    sub_f7da4c(sub_f7db98(v5), 0);
}
```

## `DynamicTouchControl.ResetControl` — RVA `0xc47b38`

- Decompiled symbol: `DynamicTouchControl_ResetControl`
- Metadata signature: `public override void ResetControl() { }`
- Native interval: `112` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DynamicTouchControl_Recovered` matched 8 offsets against `DynamicTouchControl` metadata (confidence 1.00).

```c
typedef struct DynamicTouchControl_Recovered {
    char padding_0[136];
    char fadeOutWhenReleased;
    char padding_89[143];
    char dynamicIsFadingOut;
    char dynamicAlphaAnimOn;
    char dynamicWaitingToFadeOut;
    char padding_11b[5];
    unsigned int dynamicAlphaAnimElapsed;
    char padding_124[4];
    unsigned int dynamicAlphaCur;
    unsigned int dynamicAlphaStart;
    unsigned int dynamicAlphaTarget;
} DynamicTouchControl_Recovered;

struct_0 * DynamicTouchControl_ResetControl(struct_0 *ptr)
{
    if (!ptr->field_88)
    {
        ptr->field_118 = 0;
        ptr->field_11a = 0;
        ptr->field_128 = 0x3f800000;
        ptr->field_12c = 0x3f800000;
        ptr->field_130 = 0x3f800000;
        ptr->field_120 = 0;
        ptr->field_119 = 0;
        return ptr;
    }
    DynamicTouchControl__IsInDynamicMode(ptr); /* do not return */
}
```

## `DynamicTouchControl.CanFadeOut` — RVA `0xc47ba8`

- Decompiled symbol: `DynamicTouchControl_CanFadeOut`
- Metadata signature: `private bool CanFadeOut() { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[136];
    char field_88;
} struct_0;

unsigned int DynamicTouchControl_CanFadeOut(struct_0 *a0)
{
    if (!a0->field_88)
        return 0;
    DynamicTouchControl__IsInDynamicMode(); /* do not return */
}
```

## `DynamicTouchControl.DynamicFadeOut` — RVA `0xc47bbc`

- Decompiled symbol: `DynamicTouchControl_DynamicFadeOut`
- Metadata signature: `private void DynamicFadeOut(bool animate) { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
void* DynamicTouchControl_DynamicFadeOut(void* ptr, unsigned long a1)
{
    unsigned int v0;  // s0

    if (!((char)a1 & 1))
    {
        v0 = (int)ptr[140];
        *((char *)&ptr[282]) = 0;
        *((unsigned long long *)&ptr[288]) = 0;
        *((unsigned short *)&ptr[280]) = 1;
        *((unsigned int *)&ptr[296]) = v0;
        *((unsigned int *)&ptr[300]) = v0;
        *((unsigned int *)&ptr[304]) = v0;
        return ptr;
    }
    else if ((char)ptr[280])
    {
        return ptr;
    }
    else
    {
        *((char *)&ptr[280]) = 1;
        *((char *)&ptr[282]) = 1;
        *((unsigned int *)&ptr[292]) = 0;
        return ptr;
    }
}
```

## `DynamicTouchControl.DynamicWakeUp` — RVA `0xc47c04`

- Decompiled symbol: `DynamicTouchControl_DynamicWakeUp`
- Metadata signature: `private void DynamicWakeUp(bool animate) { }`
- Native interval: `88` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DynamicTouchControl_Recovered` matched 9 offsets against `DynamicTouchControl` metadata (confidence 1.00).

```c
typedef struct DynamicTouchControl_Recovered {
    char padding_0[144];
    unsigned int fadeInDuration;
    char padding_94[132];
    char dynamicIsFadingOut;
    char dynamicAlphaAnimOn;
    char dynamicWaitingToFadeOut;
    char padding_11b[1];
    unsigned int dynamicAlphaAnimDur;
    unsigned int dynamicAlphaAnimElapsed;
    char padding_124[4];
    unsigned int dynamicAlphaCur;
    unsigned int dynamicAlphaStart;
    unsigned int dynamicAlphaTarget;
} DynamicTouchControl_Recovered;

struct_0 * DynamicTouchControl_DynamicWakeUp(struct_0 *ptr, unsigned long a1)
{
    unsigned int v0;  // s1
    unsigned long v1;  // 4133
    unsigned int v2;  // s0
    char v3;  // x8

    ptr->field_118 = 0;
    ptr->field_11a = 0;
    if (((char)a1 & 1) && !((v0 = ptr->field_90, v1 = (unsigned long)arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v0, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 981668463) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 981668463) & 1)) & ((unsigned long long)(char)(CmpF(v0, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 981668463) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), (char)v1)))
    {
        v2 = ptr->field_128;
        ptr->field_11c = v0;
        v3 = 1;
    }
    else
    {
        v3 = 0;
        v2 = 0x3f800000;
        ptr->field_128 = 0x3f800000;
    }
    ptr->field_12c = v2;
    ptr->field_120 = 0;
    ptr->field_130 = 0x3f800000;
    ptr->field_119 = v3;
    return ptr;
}
```

## `DynamicTouchControl.InvalidateHierarchy` — RVA `0xc47c5c`

- Decompiled symbol: `DynamicTouchControl_InvalidateHierarchy`
- Metadata signature: `public override void InvalidateHierarchy() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[240];
    long long field_f0;
    char padding_f8[64];
    long long field_138;
    unsigned int field_140;
    unsigned int field_144;
    unsigned int field_148;
    unsigned int field_14c;
    unsigned int field_150;
    unsigned int field_154;
    unsigned int field_158;
    unsigned int field_15c;
    unsigned int field_160;
    unsigned int field_164;
    unsigned int field_168;
    unsigned int field_16c;
    unsigned int field_170;
} struct_2;

unsigned long long DynamicTouchControl_InvalidateHierarchy(struct_2 *a0)
{
    unsigned long long v0;  // x0

    TouchControl__InvalidateHierarchy();
    v0 = DynamicTouchControl__StoreDefaultPos(a0);
    return DynamicTouchControl__StoreDefaultPos(a0);
}
```

## `DynamicTouchControl.JustPressed` — RVA `0xc47c78`

- Decompiled symbol: `DynamicTouchControl_JustPressed`
- Metadata signature: `public bool JustPressed() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    long long field_e0;
} struct_0;

long long DynamicTouchControl_JustPressed(struct_0 *a0)
{
    unsigned long v0;  // x0

    if (a0->field_e0)
    {
        v0 = TouchGestureBasicState__JustPressedRaw(a0->field_e0, 0);
        return TouchGestureBasicState__JustPressedRaw(a0->field_e0, 0);
    }
    sub_f7db74(0);
}
```

## `DynamicTouchControl.JustReleased` — RVA `0xc47c94`

- Decompiled symbol: `DynamicTouchControl_JustReleased`
- Metadata signature: `public bool JustReleased() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    long long field_e0;
} struct_0;

long long DynamicTouchControl_JustReleased(struct_0 *a0)
{
    unsigned long v0;  // x0

    if (a0->field_e0)
    {
        v0 = TouchGestureBasicState__JustReleasedRaw(a0->field_e0, 0);
        return TouchGestureBasicState__JustReleasedRaw(a0->field_e0, 0);
    }
    sub_f7db74(0);
}
```

## `DynamicTouchControl.IsTouchPressureSensitive` — RVA `0xc47cb0`

- Decompiled symbol: `DynamicTouchControl_IsTouchPressureSensitive`
- Metadata signature: `public bool IsTouchPressureSensitive() { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[224];
    struct struct_0 *field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[28];
    char field_1c;
} struct_0;

unsigned long long DynamicTouchControl_IsTouchPressureSensitive(struct_1 *a0)
{
    unsigned long long v0;  // x0

    if (a0->field_e0)
    {
        if (a0->field_e0->field_1c)
        {
            v0 = TouchGestureBasicState__IsPressureSensitive();
            return TouchGestureBasicState__IsPressureSensitive();
        }
        return 0;
    }
    sub_f7db74(0);
}
```

## `DynamicTouchControl.GetTouchPressure` — RVA `0xc47ce0`

- Decompiled symbol: `DynamicTouchControl_GetTouchPressure`
- Metadata signature: `public float GetTouchPressure() { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[28];
    char field_1c;
} struct_2;

typedef struct struct_1 {
    char padding_0[224];
    struct struct_0 *field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[28];
    char field_1c;
} struct_0;

struct_2 * DynamicTouchControl_GetTouchPressure(struct_1 *ptr)
{
    struct_0 *v0;  // x0
    unsigned long long v1;  // x0

    v0 = ptr->field_e0;
    if (v0)
    {
        if (v0->field_1c)
        {
            v1 = TouchGestureBasicState__GetPressure();
            return TouchGestureBasicState__GetPressure();
        }
        return v0;
    }
    sub_f7db74(0);
}
```

## `DynamicTouchControl.IsInDynamicMode` — RVA `0xc47d10`

- Decompiled symbol: `DynamicTouchControl_IsInDynamicMode`
- Metadata signature: `public bool IsInDynamicMode() { }`
- Native interval: `112` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[200];
    char field_c8;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab232;

void DynamicTouchControl_IsInDynamicMode(struct_1 *a0)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab232 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab232 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    Object__op_Inequality();
    return;
}
```

## `DynamicTouchControl.GetDynamicAlpha` — RVA `0xc47d80`

- Decompiled symbol: `DynamicTouchControl_GetDynamicAlpha`
- Metadata signature: `public float GetDynamicAlpha() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long DynamicTouchControl_GetDynamicAlpha(unsigned long a0)
{
    return a0;
}
```

## `DynamicTouchControl.GetAlpha` — RVA `0xc47d88`

- Decompiled symbol: `DynamicTouchControl_GetAlpha`
- Metadata signature: `public override float GetAlpha() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
long long DynamicTouchControl_GetAlpha(unsigned long a0)
{
    return a0;
}
```

## `DynamicTouchControl.SetDynamicAlpha` — RVA `0xc47d98`

- Decompiled symbol: `DynamicTouchControl_SetDynamicAlpha`
- Metadata signature: `private void SetDynamicAlpha(float alpha, float animDur) { }`
- Native interval: `64` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DynamicTouchControl_Recovered` matched 6 offsets against `DynamicTouchControl` metadata (confidence 1.00).

```c
typedef struct DynamicTouchControl_Recovered {
    char padding_0[281];
    char dynamicAlphaAnimOn;
    char padding_11a[2];
    unsigned int dynamicAlphaAnimDur;
    unsigned int dynamicAlphaAnimElapsed;
    char padding_124[4];
    unsigned int dynamicAlphaCur;
    unsigned int dynamicAlphaStart;
    unsigned int dynamicAlphaTarget;
} DynamicTouchControl_Recovered;

struct_0 * DynamicTouchControl_SetDynamicAlpha(struct_0 *ptr)
{
    unsigned int v0;  // s1
    unsigned long v1;  // 4129
    unsigned int v2;  // s2
    char v3;  // x8
    unsigned int v4;  // s0

    v1 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v0, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 981668463) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 981668463) & 1)) & ((unsigned long long)(char)(CmpF(v0, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v0, 981668463) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v1))
    {
        v2 = ptr->field_128;
        ptr->field_11c = v0;
        v3 = 1;
    }
    else
    {
        v3 = 0;
        v2 = v4;
        ptr->field_128 = v4;
    }
    ptr->field_12c = v2;
    ptr->field_130 = v4;
    ptr->field_120 = 0;
    ptr->field_119 = v3;
    return ptr;
}
```

## `DynamicTouchControl.UpdateDynamicAlpha` — RVA `0xc47dd8`

- Decompiled symbol: `DynamicTouchControl_UpdateDynamicAlpha`
- Metadata signature: `private void UpdateDynamicAlpha() { }`
- Native interval: `244` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DynamicTouchControl_Recovered` matched 12 offsets against `DynamicTouchControl` metadata (confidence 1.00).

```c
typedef struct DynamicTouchControl_Recovered {
    char padding_0[140];
    unsigned int fadeOutTargetAlpha;
    char padding_90[4];
    unsigned int fadeOutDelay;
    unsigned int fadeOutDuration;
    char padding_9c[124];
    char dynamicIsFadingOut;
    char dynamicAlphaAnimOn;
    char dynamicWaitingToFadeOut;
    char padding_11b[1];
    unsigned int dynamicAlphaAnimDur;
    unsigned int dynamicAlphaAnimElapsed;
    unsigned int dynamicFadeOutDelayElapsed;
    unsigned int dynamicAlphaCur;
    unsigned int dynamicAlphaStart;
    unsigned int dynamicAlphaTarget;
} DynamicTouchControl_Recovered;

int DynamicTouchControl_UpdateDynamicAlpha(struct_0 *ptr)
{
    struct_0 *v0;  // x0
    struct_0 *v1;  // x0
    struct_0 *v10;  // x0
    unsigned int v11;  // s1
    unsigned int v12;  // s0
    unsigned long v13;  // 4146
    unsigned int v14;  // s2
    unsigned int v15;  // s0
    unsigned long v16;  // 4141
    unsigned int v17;  // s1
    char v18;  // x8
    unsigned int v19;  // s1
    unsigned int v2;  // s1
    unsigned int v20;  // s1
    unsigned int v3;  // s0
    unsigned int v4;  // s0
    unsigned long v5;  // 4146
    unsigned int v6;  // s0
    unsigned int v7;  // s1
    unsigned int v8;  // s0
    unsigned long v9;  // 4154

    v0 = ptr;
    if (v0->field_119)
    {
        v1 = CFUtils__get_realDeltaTime(0);
        v2 = ptr->field_11c;
        v4 = ptr->field_120 + v3;
        ptr->field_120 = v4;
        v5 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v4, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v2) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v2) & 1)) & ((unsigned long long)(char)(CmpF(v4, v2)) >> 5 & 3 | (unsigned long long)(CmpF(v4, v2) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v5))
        {
            v6 = ptr->field_130;
            ptr->field_119 = 0;
        }
        else
        {
            v7 = [D] unsupported_Iop_ZeroHI96ofV128();
            v8 = 0;
            v9 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v4 / v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4 / v2, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4 / v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4 / v2, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v4 / v2, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4 / v2, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v9)
                v8 = v7;
            v6 = ptr->field_12c + v8 * (ptr->field_130 - ptr->field_12c);
        }
        ptr->field_128 = v6;
        v0 = v1;
    }
    v10 = v0;
    if (ptr->field_118 && ptr->field_11a)
    {
        v10 = CFUtils__get_realDeltaTime(0);
        v11 = ptr->field_94;
        v12 = ptr->field_124 + v6;
        ptr->field_124 = v12;
        v13 = arm64g_calculate_condition(176, (((((unsigned long long)(char)(CmpF(v12, v11)) >> 5 & 3 | (unsigned long long)(CmpF(v12, v11) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v12, v11)) >> 5 & 3 | (unsigned long long)(CmpF(v12, v11) & 1)) & ((unsigned long long)(char)(CmpF(v12, v11)) >> 5 & 3 | (unsigned long long)(CmpF(v12, v11) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v13))
        {
            v14 = ptr->field_98;
            v15 = ptr->field_8c;
            ptr->field_11a = 0;
            v16 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v14, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v14, 981668463) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v14, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v14, 981668463) & 1)) & ((unsigned long long)(char)(CmpF(v14, 981668463)) >> 5 & 3 | (unsigned long long)(CmpF(v14, 981668463) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v16))
            {
                v17 = ptr->field_128;
                ptr->field_11c = v14;
                v18 = 1;
                v19 = v17;
            }
            else
            {
                v18 = 0;
                v20 = v15;
                ptr->field_128 = v20;
                v19 = v20;
            }
            ptr->field_12c = v19;
            ptr->field_130 = v20;
            ptr->field_120 = 0;
            ptr->field_119 = v18;
        }
    }
    return *((unsigned int *)&v10);
}
```

## `DynamicTouchControl.SetWorldPos` — RVA `0xc47ecc`

- Decompiled symbol: `DynamicTouchControl_SetWorldPos`
- Metadata signature: `public override void SetWorldPos(Vector2 pos2D) { }`
- Native interval: `60` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[240];
    long long field_f0;
    char padding_f8[64];
    long long field_138;
    unsigned int field_140;
    unsigned int field_144;
    unsigned int field_148;
    unsigned int field_14c;
    unsigned int field_150;
    unsigned int field_154;
    unsigned int field_158;
    unsigned int field_15c;
    unsigned int field_160;
    unsigned int field_164;
    unsigned int field_168;
    unsigned int field_16c;
    unsigned int field_170;
} struct_2;

unsigned long long DynamicTouchControl_SetWorldPos(struct_2 *ptr)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1
    struct_2 *p;  // x9
    unsigned long long v3;  // x0

    *((unsigned int *)&ptr->padding_f8[0]) = v0;
    *((unsigned int *)&ptr->padding_f8[4]) = v1;
    *((unsigned int *)&ptr->padding_f8[8]) = 0;
    TouchControl__SetWorldPosRaw();
    p = &ptr->padding_f8[12];
    *((long long *)&p->padding_0[0]) = *((long long *)&ptr->padding_f8[0]);
    *((int *)&p->padding_0[8]) = *((int *)&ptr->padding_f8[8]);
    ptr->padding_f8[24] = 0;
    v3 = DynamicTouchControl__StoreDefaultPos(ptr);
    return DynamicTouchControl__StoreDefaultPos(ptr);
}
```

## `DynamicTouchControl.SetOriginPos` — RVA `0xc47f08`

- Decompiled symbol: `DynamicTouchControl_SetOriginPos`
- Metadata signature: `protected void SetOriginPos(Vector3 pos, bool animate) { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
void DynamicTouchControl_SetOriginPos(void* ptr, unsigned long a1)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1
    unsigned int v2;  // s2
    void* p;  // x10

    *((unsigned int *)&ptr[248]) = v0;
    *((unsigned int *)&ptr[252]) = v1;
    *((unsigned int *)&ptr[0x100]) = v2;
    if (!((char)a1 & 1))
    {
        TouchControl__SetWorldPosRaw();
        p = ptr + 260;
        *((long long *)p) = (long long)ptr[248];
        *((int *)&p[8]) = (int)ptr[0x100];
        *((char *)&ptr[272]) = 0;
        return;
    }
    TouchControl__GetWorldPos(); /* do not return */
}
```

## `DynamicTouchControl.SetOriginPos` — RVA `0xc47f68`

- Decompiled symbol: `DynamicTouchControl_SetOriginPos`
- Metadata signature: `protected void SetOriginPos(Vector3 pos) { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
void DynamicTouchControl_SetOriginPos(unsigned int *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned int v4;  // s0
    unsigned int v5;  // s1
    unsigned int v6;  // s2
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    ptr[62] = v4;
    ptr[63] = v5;
    ptr[64] = v6;
    TouchControl__GetWorldPos(); /* do not return */
}
```

## `DynamicTouchControl.GetOriginOffset` — RVA `0xc47fa0`

- Decompiled symbol: `DynamicTouchControl_GetOriginOffset`
- Metadata signature: `protected Vector2 GetOriginOffset() { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
void DynamicTouchControl_GetOriginOffset(unsigned long a0)
{
    if (Component__get_transform())
    {
        Transform__get_position();
        return;
    }
    sub_f7db74();
}
```

## `DynamicTouchControl.UpdateOriginAnimation` — RVA `0xc47fd4`

- Decompiled symbol: `DynamicTouchControl_UpdateOriginAnimation`
- Metadata signature: `protected void UpdateOriginAnimation() { }`
- Native interval: `160` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DynamicTouchControl_Recovered` matched 3 offsets against `DynamicTouchControl` metadata (confidence 1.00).

```c
typedef struct DynamicTouchControl_Recovered {
    char padding_0[184];
    unsigned int originSmoothTime;
    char padding_bc[84];
    char originAnimOn;
    char padding_111[3];
    unsigned int originAnimElapsed;
} DynamicTouchControl_Recovered;

struct_0 * DynamicTouchControl_UpdateOriginAnimation(struct_0 *ptr)
{
    unsigned int v0;  // s1
    unsigned int v1;  // s0
    unsigned int v2;  // s0
    unsigned int v3;  // s1
    unsigned long v4;  // 4163
    unsigned long v5;  // 4157
    unsigned long long v6;  // x0

    if (!ptr->field_110)
        return ptr;
    CFUtils__get_realDeltaTime(0);
    v0 = ptr->field_b8;
    v2 = ptr->field_114 + v1;
    ptr->field_114 = v2;
    v3 = v0 * 1045220557;
    v4 = arm64g_calculate_condition(160, (((((unsigned long long)(char)(CmpF(v2, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v3) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v3) & 1)) & ((unsigned long long)(char)(CmpF(v2, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v3) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v4))
        v5 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v2 / v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2 / v3, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2 / v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2 / v3, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v2 / v3, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v2 / v3, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    else
        ptr->field_110 = 0;
    v6 = TouchControl__SetWorldPosRaw(ptr, 0);
    return TouchControl__SetWorldPosRaw(ptr, 0);
}
```

## `DynamicTouchControl.SetupInitialRectPosition` — RVA `0xc48074`

- Decompiled symbol: `DynamicTouchControl_SetupInitialRectPosition`
- Metadata signature: `private void SetupInitialRectPosition() { }`
- Native interval: `264` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[240];
    unsigned long long field_f0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab234;

long long DynamicTouchControl_SetupInitialRectPosition(struct_1 *ptr)
{
    long long v0;  // x0
    unsigned long long v1;  // x0

    if (!(g_1fab234 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab234 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(ptr->field_f0, 0, 0);
    if (((char)v0 & 1))
        return v0;
    v1 = ptr->field_f0;
    if (v1)
    {
        RectTransform__set_anchoredPosition3D(v1, 0);
        v1 = ptr->field_f0;
        if (v1)
        {
            RectTransform__set_anchorMin(v1, 0);
            v1 = ptr->field_f0;
            if (v1)
            {
                RectTransform__set_anchorMax(v1, 0);
                v1 = ptr->field_f0;
                if (v1)
                {
                    RectTransform__set_offsetMin(v1, 0);
                    v1 = ptr->field_f0;
                    if (v1)
                    {
                        RectTransform__set_offsetMax(v1, 0);
                        v1 = ptr->field_f0;
                    }
                }
            }
        }
    }
    sub_f7db74(v1);
}
```

## `DynamicTouchControl.GetDefaultPos` — RVA `0xc4817c`

- Decompiled symbol: `DynamicTouchControl_GetDefaultPos`
- Metadata signature: `protected Vector3 GetDefaultPos() { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[240];
    long long field_f0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab235;

void DynamicTouchControl_GetDefaultPos(struct_1 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    long long v8;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab235 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab235 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(ptr->field_f0, 0, 0) & 1))
    {
        v8 = Component__get_transform(ptr, 0);
        if (!v8)
            goto LABEL_1048200;
    }
    else
    {
        v8 = ptr->field_f0;
        if (!v8)
        {
LABEL_1048200:
            sub_f7db74(v8);
        }
    }
    Transform__get_position();
    return;
}
```

## `DynamicTouchControl.OnDestroyControl` — RVA `0xc48204`

- Decompiled symbol: `DynamicTouchControl_OnDestroyControl`
- Metadata signature: `protected override void OnDestroyControl() { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[664];
    struct struct_1 *field_298;
    unsigned long long field_2a0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1ef0c58;
extern char g_1fab236;

void DynamicTouchControl_OnDestroyControl(struct_0 **a0)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    struct_0 **v8;  // x0
    unsigned long v9;  // x1
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab236 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab236 = 1;
    }
    v8 = a0;
    v9 = *(a0)->field_2a0;
    *(a0)->field_298();
}
```

## `DynamicTouchControl.OnUpdateControl` — RVA `0xc482a8`

- Decompiled symbol: `DynamicTouchControl_OnUpdateControl`
- Metadata signature: `protected override void OnUpdateControl() { }`
- Native interval: `1528` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DynamicTouchControl_Recovered` matched 12 offsets against `DynamicTouchControl` metadata (confidence 1.00).

```c
typedef struct DynamicTouchControl_Recovered {
    char padding_0[140];
    unsigned int fadeOutTargetAlpha;
    char padding_90[4];
    unsigned int fadeOutDelay;
    unsigned int fadeOutDuration;
    char padding_9c[124];
    char dynamicIsFadingOut;
    char dynamicAlphaAnimOn;
    char dynamicWaitingToFadeOut;
    char padding_11b[1];
    unsigned int dynamicAlphaAnimDur;
    unsigned int dynamicAlphaAnimElapsed;
    unsigned int dynamicFadeOutDelayElapsed;
    unsigned int dynamicAlphaCur;
    unsigned int dynamicAlphaStart;
    unsigned int dynamicAlphaTarget;
} DynamicTouchControl_Recovered;

typedef struct struct_1 {
    char padding_0[392];
    struct struct_2 *field_188;
    unsigned long long field_190;
} struct_1;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

extern struct_0 *g_1ef0c58;
extern char g_1fab237;

void DynamicTouchControl_OnUpdateControl(struct_0 *ptr, unsigned long a1, unsigned long long a2, unsigned long a3)
{
    unsigned long long v10;  // d12
    unsigned long long v11;  // d11
    unsigned long v20;  // x1
    unsigned long long v12;  // d10
    unsigned long long v13;  // d9
    unsigned long long v14;  // d8
    unsigned long long v15;  // x30
    unsigned long long v16;  // x21
    unsigned long long v17;  // x20
    unsigned long long v18;  // x19
    struct_1 **v19;  // x0
    unsigned long long v0;  // [bp-0x50]
    char flag;  // [bp-0x44]
    unsigned long long v2;  // [bp-0x40]
    unsigned long long v3;  // [bp-0x38]
    unsigned long long v4;  // [bp-0x30]
    unsigned long long v5;  // [bp-0x28]
    unsigned long long v6;  // [bp-0x20]
    unsigned long long v7;  // [bp-0x18]
    unsigned long long v8;  // [bp-0x10]
    unsigned long long v9;  // [bp-0x8]

    v0 = v10;
    v2 = v11;
    v3 = v12;
    v4 = v13;
    v5 = v14;
    v6 = v15;
    v7 = v16;
    v8 = v17;
    v9 = v18;
    if (!(g_1fab237 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab237 = 1;
    }
    flag = 0;
    if (*((long long *)&ptr->padding_9c[76]))
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        a2 = 0;
        if (((char)Object__op_Inequality(*((long long *)&ptr->padding_0[88]), 0, 0) & 1))
        {
            v19 = *((long long *)&ptr->padding_0[88]);
            if (!v19)
                goto LABEL_104889c;
            InputRig__WakeTouchControlsUp(v19);
        }
    }
    DynamicTouchControl__UpdateDynamicAlpha(ptr);
    v19 = *((long long *)&ptr->padding_9c[68]);
    if (v19)
    {
        v20 = *(v19)->field_190;
        *(v19)->field_188();
    }
LABEL_104889c:
    sub_f7db74(v19);
}
```

## `DynamicTouchControl.OnTouchStart` — RVA `0xc488a0`

- Decompiled symbol: `DynamicTouchControl_OnTouchStart`
- Metadata signature: `public override bool OnTouchStart(TouchObject touch, TouchControl sender, TouchControl.TouchStartType touchStartType) { }`
- Native interval: `548` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[232];
    long long field_e8;
} struct_0;

extern long long g_1ef0c58;
extern char g_1fab238;

unsigned long long DynamicTouchControl_OnTouchStart(struct_0 *a0, long long a1, unsigned long a2, unsigned int a3)
{
    unsigned long long v2;  // d15
    unsigned long long v3;  // d14
    struct_0 *ptr;  // x22
    long long v5;  // x0
    unsigned long v6;  // cc_dep1
    unsigned long v7;  // 4105
    unsigned long v8;  // 4105
    unsigned long long v0;  // [bp-0x80]
    unsigned long long v1;  // [bp-0x78]

    v0 = v2;
    v1 = v3;
    if (!(g_1fab238 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab238 = 1;
    }
    ptr = &a0->field_e8;
    if (!a0->field_e8)
    {
        *((long long *)&ptr->padding_0[0]) = a1;
        sub_f7d8d0(ptr, a1);
        v5 = *((long long *)&ptr->padding_0[0]);
        if (v5)
        {
            v5 = TouchObject__AddControl(v5, a0, 0);
            if (a1)
            {
                v6 = a3;
                if (!a3)
                {
                    v7 = arm64g_calculate_condition(3, v6, 0, 0);
                    if (!((char)v7))
                        goto LABEL_104893e;
LABEL_104893d:
                }
                else
                {
                    v8 = arm64g_calculate_condition(3, v6, 0, 0);
                    if ((char)v8)
                        goto LABEL_104893d;
LABEL_104893e:
                }
                TouchControl__ScreenToOrientedPos(); /* do not return */
            }
        }
        sub_f7db74(v5);
    }
    else if (a0->field_e8)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `DynamicTouchControl.OnTouchEnd` — RVA `0xc48ac4`

- Decompiled symbol: `DynamicTouchControl_OnTouchEnd`
- Metadata signature: `public override bool OnTouchEnd(TouchObject touch, TouchControl.TouchEndType touchEndType) { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
long long DynamicTouchControl_OnTouchEnd(unsigned long long *ptr, unsigned long long a1, unsigned int a2)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    unsigned long long v10;  // x22
    unsigned long v11;  // x0
    unsigned int v12;  // w8
    unsigned int v13;  // w9
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
    v10 = ptr[29];
    if (a1 == v10 && v10)
    {
        ptr[29] = 0;
        sub_f7d8d0();
        v11 = ptr[28];
        if (ptr[28])
        {
            TouchGestureBasicState__OnTouchEnd();
            v11 = ptr[27];
            if (v11)
            {
                TouchGestureBasicState__OnTouchEnd();
                v11 = ptr[26];
                if (v11)
                {
                    TouchGestureBasicState__OnTouchEnd();
                    goto LABEL_1048b40;
                }
            }
        }
        sub_f7db74(v11);
    }
    else
    {
LABEL_1048b40:
        if (!v10)
            v12 = 0;
        else
            v12 = 1;
        if (a1 != v10)
            v13 = 0;
        else
            v13 = 1;
        return v13 & v12;
    }
}
```

## `DynamicTouchControl.OnTouchMove` — RVA `0xc48b68`

- Decompiled symbol: `DynamicTouchControl_OnTouchMove`
- Metadata signature: `public override bool OnTouchMove(TouchObject touch) { }`
- Native interval: `200` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[232];
    struct struct_0 *field_e8;
} struct_1;

typedef struct struct_0 {
    char padding_0[48];
    long long field_30;
} struct_0;

long long DynamicTouchControl_OnTouchMove(struct_1 *ptr, struct_0 *a1)
{
    unsigned long long v8;  // d11
    unsigned long long v9;  // d10
    unsigned int v18;  // w9
    unsigned long long v10;  // d9
    unsigned long long v11;  // d8
    unsigned long long v12;  // x30
    unsigned long long v13;  // x21
    unsigned long long v14;  // x20
    unsigned long long v15;  // x19
    struct_0 *v16;  // x21
    unsigned int v17;  // w8
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x38]
    unsigned long long v2;  // [bp-0x30]
    unsigned long long v3;  // [bp-0x28]
    unsigned long long v4;  // [bp-0x20]
    unsigned long long v5;  // [bp-0x18]
    unsigned long long v6;  // [bp-0x10]
    unsigned long long v7;  // [bp-0x8]

    v0 = v8;
    v1 = v9;
    v2 = v10;
    v3 = v11;
    v4 = v12;
    v5 = v13;
    v6 = v14;
    v7 = v15;
    v16 = ptr->field_e8;
    if (a1 == v16 && v16)
    {
        if (a1)
        {
            TouchControl__ScreenToWorldPos();
            TouchControl__ScreenToOrientedPos(ptr, a1->field_30, 0); /* do not return */
        }
        sub_f7db74();
    }
    if (!v16)
        v17 = 0;
    else
        v17 = 1;
    if (a1 != v16)
        v18 = 0;
    else
        v18 = 1;
    return v18 & v17;
}
```

## `DynamicTouchControl.OnTouchPressureChange` — RVA `0xc48c30`

- Decompiled symbol: `DynamicTouchControl_OnTouchPressureChange`
- Metadata signature: `public override bool OnTouchPressureChange(TouchObject touch) { }`
- Native interval: `132` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DynamicTouchControl_Recovered` matched 4 offsets against `DynamicTouchControl` metadata (confidence 1.00).

```c
typedef struct DynamicTouchControl_Recovered {
    char padding_0[208];
    long long touchStateOriented;
    long long touchStateScreen;
    long long touchStateWorld;
    unsigned long long touchObj;
} DynamicTouchControl_Recovered;

long long DynamicTouchControl_OnTouchPressureChange(struct_0 *ptr, unsigned long long a1)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v8;  // x21
    unsigned int v9;  // w8
    unsigned int v10;  // w9
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    v8 = ptr->field_e8;
    if (a1 == v8 && v8)
    {
        if (a1 && ptr->field_e0 && (TouchGestureBasicState__OnTouchPressureChange(ptr->field_e0, 0), ptr->field_d8 && (TouchGestureBasicState__OnTouchPressureChange(ptr->field_d8, 0), ptr->field_d0)))
            TouchGestureBasicState__OnTouchPressureChange(ptr->field_d0, 0);
        else
            sub_f7db74();
    }
    if (!v8)
        v9 = 0;
    else
        v9 = 1;
    if (a1 != v8)
        v10 = 0;
    else
        v10 = 1;
    return v10 & v9;
}
```

## `DynamicTouchControl.ReleaseAllTouches` — RVA `0xc48cb4`

- Decompiled symbol: `DynamicTouchControl_ReleaseAllTouches`
- Metadata signature: `public override void ReleaseAllTouches() { }`
- Native interval: `128` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DynamicTouchControl_Recovered` matched 4 offsets against `DynamicTouchControl` metadata (confidence 1.00).

```c
typedef struct DynamicTouchControl_Recovered {
    char padding_0[208];
    unsigned long long touchStateOriented;
    unsigned long long touchStateScreen;
    unsigned long long touchStateWorld;
    long long touchObj;
} DynamicTouchControl_Recovered;

long long DynamicTouchControl_ReleaseAllTouches(struct_0 *ptr)
{
    unsigned long v0;  // x0
    unsigned long long v1;  // x0

    if (ptr->field_e8)
    {
        TouchObject__ReleaseControl(ptr->field_e8, ptr, 1, 0);
        ptr->field_e8 = 0;
        sub_f7d8d0((struct DynamicTouchControl_Recovered *)&ptr->field_e8, 0);
    }
    v0 = ptr->field_e0;
    if (v0)
    {
        TouchGestureBasicState__OnTouchEnd(v0, 1, 0);
        v0 = ptr->field_d0;
        if (v0)
        {
            TouchGestureBasicState__OnTouchEnd(v0, 1, 0);
            v0 = ptr->field_d8;
            if (v0)
            {
                v1 = TouchGestureBasicState__OnTouchEnd();
                return TouchGestureBasicState__OnTouchEnd();
            }
        }
    }
    sub_f7db74(v0);
}
```

## `DynamicTouchControl.CanBeTouchedDirectly` — RVA `0xc48d34`

- Decompiled symbol: `DynamicTouchControl_CanBeTouchedDirectly`
- Metadata signature: `public override bool CanBeTouchedDirectly(TouchObject touchObj) { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[232];
    unsigned long long field_e8;
} struct_0;

unsigned long long DynamicTouchControl_CanBeTouchedDirectly(struct_0 *a0)
{
    unsigned long long v0;  // x0

    if (!((char)TouchControl__CanBeTouchedDirectly() & 1))
        return 0;
    if (a0->field_e8)
        v0 = 0;
    else
        v0 = 1;
    return v0;
}
```

## `DynamicTouchControl.CanBeSwipedOverFromNothing` — RVA `0xc48d64`

- Decompiled symbol: `DynamicTouchControl_CanBeSwipedOverFromNothing`
- Metadata signature: `public override bool CanBeSwipedOverFromNothing(TouchObject touchObj) { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[232];
    unsigned long long field_e8;
} struct_0;

unsigned long long DynamicTouchControl_CanBeSwipedOverFromNothing(struct_0 *a0)
{
    unsigned long long v0;  // x0

    if (!((char)TouchControl__CanBeSwipedOverFromNothingDefault() & 1))
    {
        return 0;
    }
    else if (a0->field_e8)
    {
        return 0;
    }
    else
    {
        v0 = TouchControl__IsActiveAndVisible(a0, 0);
        return TouchControl__IsActiveAndVisible(a0, 0);
    }
}
```

## `DynamicTouchControl.CanBeSwipedOverFromRestrictedList` — RVA `0xc48d9c`

- Decompiled symbol: `DynamicTouchControl_CanBeSwipedOverFromRestrictedList`
- Metadata signature: `public override bool CanBeSwipedOverFromRestrictedList(TouchObject touchObj) { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[232];
    unsigned long long field_e8;
} struct_0;

unsigned long long DynamicTouchControl_CanBeSwipedOverFromRestrictedList(struct_0 *a0)
{
    unsigned long long v0;  // x0

    if (!((char)TouchControl__CanBeSwipedOverFromRestrictedListDefault() & 1))
    {
        return 0;
    }
    else if (a0->field_e8)
    {
        return 0;
    }
    else
    {
        v0 = TouchControl__IsActiveAndVisible(a0, 0);
        return TouchControl__IsActiveAndVisible(a0, 0);
    }
}
```

## `DynamicTouchControl.CanSwipeOverOthers` — RVA `0xc48dd4`

- Decompiled symbol: `DynamicTouchControl_CanSwipeOverOthers`
- Metadata signature: `public override bool CanSwipeOverOthers(TouchObject touchObj) { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
long long DynamicTouchControl_CanSwipeOverOthers(unsigned long a0, unsigned long a1)
{
    unsigned long long v0;  // x0

    v0 = TouchControl__CanSwipeOverOthersDefault();
    return TouchControl__CanSwipeOverOthersDefault();
}
```

## `DynamicTouchControl.CanBeActivatedByDynamicRegion` — RVA `0xc48de4`

- Decompiled symbol: `DynamicTouchControl_CanBeActivatedByDynamicRegion`
- Metadata signature: `public virtual bool CanBeActivatedByDynamicRegion() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[232];
    unsigned long long field_e8;
} struct_0;

unsigned int DynamicTouchControl_CanBeActivatedByDynamicRegion(struct_0 *a0)
{
    if (!a0->field_e8)
        return TouchControl__IsActive();
    return 0;
}
```

## `DynamicTouchControl.CanBeActivatedByOtherControl` — RVA `0xc48dfc`

- Decompiled symbol: `DynamicTouchControl_CanBeActivatedByOtherControl`
- Metadata signature: `public override bool CanBeActivatedByOtherControl(TouchControl c, TouchObject touchObj) { }`
- Native interval: `48` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[232];
    unsigned long long field_e8;
} struct_0;

unsigned long long DynamicTouchControl_CanBeActivatedByOtherControl(struct_0 *a0)
{
    unsigned long long v0;  // x0

    if (!((char)TouchControl__CanBeActivatedByOtherControl() & 1))
        return 0;
    if (a0->field_e8)
        v0 = 0;
    else
        v0 = 1;
    return v0;
}
```
