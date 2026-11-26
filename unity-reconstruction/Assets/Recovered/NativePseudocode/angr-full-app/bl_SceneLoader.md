# Native pseudocode: bl_SceneLoader

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_SceneLoader.get_sceneAsyncOp` — RVA `0xc76814`

- Decompiled symbol: `bl_SceneLoader_get_sceneAsyncOp`
- Metadata signature: `public AsyncOperation get_sceneAsyncOp() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[160];
    unsigned long long field_a0;
} struct_0;

long long bl_SceneLoader_get_sceneAsyncOp(struct_0 *a0)
{
    return a0->field_a0;
}
```

## `bl_SceneLoader.set_sceneAsyncOp` — RVA `0xc7681c`

- Decompiled symbol: `bl_SceneLoader_set_sceneAsyncOp`
- Metadata signature: `public void set_sceneAsyncOp(AsyncOperation value) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[160];
    unsigned long long field_a0;
} struct_0;

long long bl_SceneLoader_set_sceneAsyncOp(struct_0 *ptr, unsigned long a1)
{
    long long v0;  // x0

    ptr->field_a0 = a1;
    v0 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `bl_SceneLoader.Awake` — RVA `0xc76824`

- Decompiled symbol: `bl_SceneLoader_Awake`
- Metadata signature: `private void Awake() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
void bl_SceneLoader_Awake(unsigned long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    bl_SceneLoader__AsynLoadData();
    MonoBehaviour__StartCoroutine();
    return;
}
```

## `bl_SceneLoader.AsynLoadData` — RVA `0xc76844`

- Decompiled symbol: `bl_SceneLoader_AsynLoadData`
- Metadata signature: `private IEnumerator AsynLoadData() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef4198;
extern char g_1fab3ac;

struct_0 * bl_SceneLoader_AsynLoadData(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab3ac & 1))
    {
        sub_f7d92c(&g_1ef4198);
        g_1fab3ac = 1;
    }
    v0 = sub_f7db70(g_1ef4198);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `bl_SceneLoader.<AsynLoadData>d__38.ctor` — RVA `0xc768b0`

- Decompiled symbol: `bl_SceneLoader_AsynLoadData_d__38_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void bl_SceneLoader_AsynLoadData_d__38_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `bl_SceneLoader.Init` — RVA `0xc768d8`

- Decompiled symbol: `bl_SceneLoader_Init`
- Metadata signature: `private void Init() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[152];
    long long field_98;
} struct_0;

void bl_SceneLoader_Init(struct_0 *ptr, unsigned long a1)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr->field_98;
    if (ptr->field_98)
    {
        bl_LoadingScreenUI__Init();
        v4 = Component__get_transform(ptr, 0);
    }
    sub_f7db74(v4);
}
```

## `bl_SceneLoader.Update` — RVA `0xc76c5c`

- Decompiled symbol: `bl_SceneLoader_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `68` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_SceneLoader_Recovered` matched 3 offsets against `bl_SceneLoader` metadata (confidence 1.00).

```c
typedef struct bl_SceneLoader_Recovered {
    char padding_0[152];
    long long ScreenUI;
    unsigned long long k__BackingField;
    char padding_a8[8];
    char isOperationStarted;
} bl_SceneLoader_Recovered;

struct_0 * bl_SceneLoader_Update(struct_0 *a0)
{
    unsigned long long v0;  // x0

    if (!a0->field_b0)
    {
        return a0;
    }
    else if (a0->field_a0)
    {
        bl_SceneLoader__UpdateProgress(a0);
        if (a0->field_98)
        {
            bl_LoadingScreenUI__LoadingRotator(a0->field_98);
            v0 = bl_SceneLoader__SkipWithKey(a0);
            return bl_SceneLoader__SkipWithKey(a0);
        }
        sub_f7db74(0);
    }
    else
    {
        return a0;
    }
}
```

## `bl_SceneLoader.UpdateProgress` — RVA `0xc76ca0`

- Decompiled symbol: `bl_SceneLoader_UpdateProgress`
- Metadata signature: `private void UpdateProgress() { }`
- Native interval: `432` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_SceneLoader_Recovered` matched 9 offsets against `bl_SceneLoader` metadata (confidence 1.00).

```c
typedef struct bl_SceneLoader_Recovered {
    char padding_0[32];
    unsigned int SkipType;
    unsigned int SceneSmoothLoad;
    char padding_28[8];
    char useTimeScale;
    char padding_31[43];
    unsigned int RoundBarProgress;
    char padding_60[56];
    long long ScreenUI;
    long long k__BackingField;
    char padding_a8[9];
    char FinishLoad;
    char padding_b2[2];
    unsigned int smoothValue;
    char padding_b8[8];
    struct struct_1 *CurrentLoadLevel;
} bl_SceneLoader_Recovered;

typedef struct struct_1 {
    char padding_0[40];
    unsigned int field_28;
    unsigned int field_2c;
} struct_1;

long long bl_SceneLoader_UpdateProgress(struct_0 *ptr)
{
    unsigned int p[12];  // x8
    unsigned int v2;  // s0
    unsigned int v11;  // s1
    unsigned long v12;  // 4154
    unsigned int v13;  // s0
    unsigned int v14;  // s0
    unsigned long v15;  // 4133
    unsigned int v16;  // s1
    unsigned long v17;  // 4133
    unsigned int v18;  // s8
    unsigned long v19;  // d0
    unsigned long v20;  // 4125
    unsigned long v3;  // 4129
    unsigned long long v21;  // 4102
    unsigned long long v22;  // d0
    unsigned long long v23;  // 4102
    unsigned long v24;  // 4137
    unsigned long long v25;  // x0
    unsigned int v4;  // w8
    unsigned int v5;  // s0
    unsigned int flag;  // s1
    unsigned int v7;  // s9
    unsigned int choice;  // s3
    long long v9;  // x0
    unsigned int v10;  // s0
    char v0;  // [bp-0x28]

    p = ptr->field_c0;
    if (p)
    {
        if (p[11])
        {
            v2 = ptr->field_b4;
            v3 = arm64g_calculate_condition(160, (((((unsigned long long)(char)(CmpF(v2, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v2, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v2, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v3)
                goto LABEL_1076d84;
            goto LABEL_1076d94;
        }
        else
        {
            v4 = p[10];
            if (!p[10])
            {
                v4 = ptr->field_20;
                if (!ptr->field_20)
                    v4 = 4;
            }
            if (ptr->field_a0)
            {
                v5 = 1036831949;
                flag = 0;
                if (v4 == 3)
                    v7 = flag;
                else
                    v7 = v5;
                AsyncOperation__get_progress();
                if (ptr->field_30)
                    Time__get_deltaTime(0);
                else
                    Time__get_unscaledDeltaTime(0);
                choice = 0;
                v9 = ptr->field_a0;
                v10 = 1036831949 * ptr->field_24;
                v11 = [D] unsupported_Iop_ZeroHI96ofV128();
                v12 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v10, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v10, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                if ((char)v12)
                    v13 = v11;
                else
                    v13 = choice;
                ptr->field_b4 = ptr->field_b4 + (v7 + 1036831949 - ptr->field_b4) * v13;
                if (v9)
                {
                    if (((char)AsyncOperation__get_isDone(v9, 0) & 1) || (v14 = ptr->field_b4, v15 = (unsigned long)arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v14, 1065185444)) >> 5 & 3 | (unsigned long long)(CmpF(v14, 1065185444) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v14, 1065185444)) >> 5 & 3 | (unsigned long long)(CmpF(v14, 1065185444) & 1)) & ((unsigned long long)(char)(CmpF(v14, 1065185444)) >> 5 & 3 | (unsigned long long)(CmpF(v14, 1065185444) & 1)) >> 1 & 1)) * 0x10000000, 0, 0), !((char)v15)))
                    {
LABEL_1076d84:
                        if (!ptr->field_b1)
                            bl_SceneLoader__OnFinish(ptr);
                    }
LABEL_1076d94:
                    v16 = ptr->field_5c;
                    v17 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v16, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v16, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v16, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v16, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v16, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v16, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                    if (!((char)v17))
                    {
                        v18 = ptr->field_b4 / v16;
                        v19 = v18;
                        modf(&v0);
                        v20 = arm64g_calculate_condition(160, (((((unsigned long long)(char)(CmpF(v18, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v18, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v18, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v18, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v18, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v18, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                        if (!((char)v20))
                        {
                            v21 = (((CmpF(v19, 0xbfe0000000000000) >> 5 & 3 | CmpF(v19, 0xbfe0000000000000) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v19, 0xbfe0000000000000) >> 5 & 3 | CmpF(v19, 0xbfe0000000000000) & 1) & (CmpF(v19, 0xbfe0000000000000) >> 5 & 3 | CmpF(v19, 0xbfe0000000000000) & 1) >> 1 & 1);
                            if ((char)(v21 * 0x10000000 >> 30))
                            {
                                v22 = v0;
                                goto LABEL_1076de8;
                            }
                        }
                        else
                        {
                            v23 = (((CmpF(v19, 0x3fe0000000000000) >> 5 & 3 | CmpF(v19, 0x3fe0000000000000) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v19, 0x3fe0000000000000) >> 5 & 3 | CmpF(v19, 0x3fe0000000000000) & 1) & (CmpF(v19, 0x3fe0000000000000) >> 5 & 3 | CmpF(v19, 0x3fe0000000000000) & 1) >> 1 & 1);
                            if ((char)(v23 * 0x10000000 >> 30))
                            {
                                v22 = v0;
LABEL_1076de8:
                                v24 = arm64g_calculate_condition(10, (unsigned long long)v22 & 1, 0, 0);
                            }
                        }
                    }
                    if (ptr->field_98)
                    {
                        v25 = bl_LoadingScreenUI__UpdateLoadProgress(ptr->field_98);
                        return bl_LoadingScreenUI__UpdateLoadProgress(ptr->field_98);
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `bl_SceneLoader.SkipWithKey` — RVA `0xc76e54`

- Decompiled symbol: `bl_SceneLoader_SkipWithKey`
- Metadata signature: `private void SkipWithKey() { }`
- Native interval: `56` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_SceneLoader_Recovered` matched 2 offsets against `bl_SceneLoader` metadata (confidence 1.00).

```c
typedef struct bl_SceneLoader_Recovered {
    char padding_0[152];
    long long ScreenUI;
    char padding_a0[24];
    char canSkipWithKey;
} bl_SceneLoader_Recovered;

struct_0 * bl_SceneLoader_SkipWithKey(struct_0 *a0)
{
    struct_0 *v0;  // x0

    if (!a0->field_b8)
        return a0;
    v0 = Input__get_anyKeyDown(0);
    if (!((char)v0 & 1))
        return v0;
    if (a0->field_98)
        bl_LoadingScreenUI__TransitionToScene(a0->field_98); /* do not return */
    sub_f7db74(0);
}
```

## `bl_SceneLoader.get_GetSkipType` — RVA `0xc76e8c`

- Decompiled symbol: `bl_SceneLoader_get_GetSkipType`
- Metadata signature: `public SceneSkipType get_GetSkipType() { }`
- Native interval: `44` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_SceneLoader_Recovered` matched 2 offsets against `bl_SceneLoader` metadata (confidence 1.00).

```c
typedef struct bl_SceneLoader_Recovered {
    char padding_0[32];
    unsigned int SkipType;
    char padding_24[156];
    struct struct_0 *CurrentLoadLevel;
} bl_SceneLoader_Recovered;

typedef struct struct_0 {
    char padding_0[40];
    unsigned int field_28;
} struct_0;

unsigned long long bl_SceneLoader_get_GetSkipType(struct_1 *a0)
{
    if (a0->field_c0 && a0->field_c0->field_28)
        return a0->field_c0->field_28;
    if (a0->field_20)
        return a0->field_20;
    return 4;
}
```

## `bl_SceneLoader.get_DeltaTime` — RVA `0xc76eb8`

- Decompiled symbol: `bl_SceneLoader_get_DeltaTime`
- Metadata signature: `public float get_DeltaTime() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

void bl_SceneLoader_get_DeltaTime(struct_0 *a0)
{
    if (!a0->field_30)
    {
        Time__get_unscaledDeltaTime();
        return;
    }
    Time__get_deltaTime();
    return;
}
```

## `bl_SceneLoader.OnFinish` — RVA `0xc76ed0`

- Decompiled symbol: `bl_SceneLoader_OnFinish`
- Metadata signature: `private void OnFinish() { }`
- Native interval: `252` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_SceneLoader_Recovered` matched 7 offsets against `bl_SceneLoader` metadata (confidence 1.00).

```c
typedef struct bl_SceneLoader_Recovered {
    char padding_0[32];
    unsigned int SkipType;
    char padding_24[92];
    long long FinishSound;
    char padding_88[8];
    long long onLoaded;
    unsigned long long ScreenUI;
    char padding_a0[17];
    char FinishLoad;
    char padding_b2[6];
    char canSkipWithKey;
    char padding_b9[7];
    struct struct_1 *CurrentLoadLevel;
} bl_SceneLoader_Recovered;

typedef struct struct_1 {
    char padding_0[40];
    unsigned int field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab3ad;

long long bl_SceneLoader_OnFinish(struct_2 *ptr)
{
    long long v0;  // x0
    unsigned int v1;  // w8
    unsigned long long v2;  // x0
    unsigned long long v3;  // x0

    if (!(g_1fab3ad & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab3ad = 1;
    }
    v0 = ptr->field_90;
    ptr->field_b1 = 1;
    if (v0)
        UnityEvent__Invoke(v0, 0);
    if (ptr->field_c0 && !((v1 = ptr->field_c0->field_28, !v1)) || !((v1 = ptr->field_20, !v1)))
    {
        if (2 > v1 - 2)
        {
            v2 = ptr->field_98;
            if (v2)
                bl_LoadingScreenUI__TransitionToScene(v2); /* do not return */
        }
        else
        {
            if (v1 != 4)
                goto LABEL_1076f58;
            goto LABEL_1076f50;
        }
    }
    else
    {
LABEL_1076f50:
        ptr->field_b8 = 1;
LABEL_1076f58:
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Inequality(ptr->field_80, 0, 0) & 1))
        {
            v2 = Component__get_transform(ptr, 0);
            if (v2)
            {
                Transform__get_position();
                AudioSource__PlayClipAtPoint(ptr->field_80, 0);
                goto LABEL_1076fb4;
            }
        }
        else
        {
LABEL_1076fb4:
            v2 = ptr->field_98;
            if (v2)
            {
                v3 = bl_LoadingScreenUI__OnFinish(v2);
                return bl_LoadingScreenUI__OnFinish(v2);
            }
        }
    }
    sub_f7db74(v2);
}
```

## `bl_SceneLoader.ShowCustomProgress` — RVA `0xc77140`

- Decompiled symbol: `bl_SceneLoader_ShowCustomProgress`
- Metadata signature: `public void ShowCustomProgress(float value) { }`
- Native interval: `204` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_SceneLoader_Recovered` matched 4 offsets against `bl_SceneLoader` metadata (confidence 1.00).

```c
typedef struct struct_0 {
    char padding_0[88];
    unsigned int field_58;
    unsigned int field_5c;
    char padding_60[56];
    struct bl_SceneLoader_Recovered *field_98;
    char padding_a0[20];
    unsigned int field_b4;
} struct_0;

typedef struct bl_SceneLoader_Recovered {
    char padding_0[48];
    struct struct_7 *useTimeScale;
    char padding_38[16];
    struct struct_8 *RandomTips;
    struct struct_8 *FadeTipsSpeed;
    char padding_58[88];
    struct struct_5 *isOperationStarted;
} bl_SceneLoader_Recovered;

typedef struct struct_7 {
    struct struct_1 *field_0;
} struct_7;

typedef struct struct_8 {
    struct struct_3 *field_0;
} struct_8;

typedef struct struct_5 {
    char padding_0[104];
    long long field_68;
} struct_5;

typedef struct struct_1 {
    char padding_0[1512];
    struct struct_2 *field_5e8;
    unsigned long long field_5f0;
} struct_1;

typedef struct struct_3 {
    char padding_0[1064];
    struct struct_4 *field_428;
    unsigned long long field_430;
} struct_3;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_4 {
    unsigned long long field_0;
} struct_4;

long long bl_SceneLoader_ShowCustomProgress(struct_0 *ptr)
{
    unsigned int v1;  // s1
    unsigned long v2;  // 4190
    unsigned int v3;  // s0
    unsigned int v4;  // s9
    unsigned long v5;  // d0
    unsigned long v6;  // 4125
    unsigned long long v7;  // 4102
    unsigned long long v8;  // 4102
    unsigned long v9;  // 4137
    long long v10;  // x0
    char v0;  // [bp-0x28], Other Possible Types: unsigned long long

    v1 = ptr->field_5c;
    v2 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v1, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v2))
    {
        v4 = (ptr->field_b4 * ptr->field_58 + v3) / v1;
        v5 = v4;
        modf(&v0);
        v6 = arm64g_calculate_condition(160, (((((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if (!((char)v6))
        {
            v7 = (((CmpF(v5, 0xbfe0000000000000) >> 5 & 3 | CmpF(v5, 0xbfe0000000000000) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v5, 0xbfe0000000000000) >> 5 & 3 | CmpF(v5, 0xbfe0000000000000) & 1) & (CmpF(v5, 0xbfe0000000000000) >> 5 & 3 | CmpF(v5, 0xbfe0000000000000) & 1) >> 1 & 1);
            if ((char)(v7 * 0x10000000 >> 30))
                goto LABEL_10771b0;
        }
        else
        {
            v8 = (((CmpF(v5, 0x3fe0000000000000) >> 5 & 3 | CmpF(v5, 0x3fe0000000000000) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v5, 0x3fe0000000000000) >> 5 & 3 | CmpF(v5, 0x3fe0000000000000) & 1) & (CmpF(v5, 0x3fe0000000000000) >> 5 & 3 | CmpF(v5, 0x3fe0000000000000) & 1) >> 1 & 1);
            if ((char)(v8 * 0x10000000 >> 30))
            {
LABEL_10771b0:
                v9 = arm64g_calculate_condition(10, (unsigned long long)v0 & 1, 0, 0);
            }
        }
    }
    if (ptr->field_98)
    {
        v10 = bl_LoadingScreenUI__UpdateLoadProgress(ptr->field_98);
        return bl_LoadingScreenUI__UpdateLoadProgress(ptr->field_98);
    }
    sub_f7db74(0);
}
```

## `bl_SceneLoader.TransitionToScene` — RVA `0xc7720c`

- Decompiled symbol: `bl_SceneLoader_TransitionToScene`
- Metadata signature: `public void TransitionToScene() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[152];
    long long field_98;
} struct_0;

long long bl_SceneLoader_TransitionToScene(struct_0 *a0)
{
    if (a0->field_98)
        bl_LoadingScreenUI__TransitionToScene(a0->field_98); /* do not return */
    sub_f7db74(0);
}
```

## `bl_SceneLoader.LoadLevel` — RVA `0xc773b8`

- Decompiled symbol: `bl_SceneLoader_LoadLevel`
- Metadata signature: `public void LoadLevel(string level) { }`
- Native interval: `172` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_SceneLoader_Recovered` matched 3 offsets against `bl_SceneLoader` metadata (confidence 1.00).

```c
typedef struct bl_SceneLoader_Recovered {
    char padding_0[152];
    long long ScreenUI;
    char padding_a0[8];
    long long Manager;
    char padding_b0[16];
    struct struct_0 *CurrentLoadLevel;
} bl_SceneLoader_Recovered;

typedef struct struct_2 {
    char padding_0[16];
    unsigned long long field_10;
    char padding_18[20];
    unsigned int field_2c;
} struct_2;

typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
    char padding_18[20];
    unsigned int field_2c;
} struct_0;

long long bl_SceneLoader_LoadLevel(struct_1 *ptr, unsigned long a1)
{
    unsigned long v0;  // x0
    struct_2 *v1;  // x0
    struct_1 *v2;  // x20
    unsigned long v3;  // x0
    long long v4;  // x0

    v0 = ptr->field_a8;
    if (v0)
    {
        v1 = bl_SceneLoaderManager__GetSceneInfo(v0);
        ptr->field_c0 = v1;
        v2 = &ptr->field_c0;
        v3 = sub_f7d8d0(v2, v1);
        if (!*((long long *)&v2->padding_0[0]))
            return v3;
        v0 = ptr->field_98;
        if (ptr->field_98)
        {
            v0 = bl_LoadingScreenUI__SetupUIForScene();
            if (*((long long *)&v2->padding_0[0]))
            {
                v0 = MonoBehaviour__StartCoroutine(ptr, bl_SceneLoader__DoAsyncOperation(ptr, *((long long *)(*((long long *)&v2->padding_0[0]) + 16))), 0);
                if (ptr->field_c0)
                {
                    if (ptr->field_c0->field_2c == 1)
                    {
                        bl_SceneLoader__StartFakeLoading(ptr);
                        v4 = MonoBehaviour__StartCoroutine();
                        return MonoBehaviour__StartCoroutine();
                    }
                    return v0;
                }
            }
        }
    }
    sub_f7db74(v0);
}
```

## `bl_SceneLoader.DoAsyncOperation` — RVA `0xc77880`

- Decompiled symbol: `bl_SceneLoader_DoAsyncOperation`
- Metadata signature: `private IEnumerator DoAsyncOperation(string level) { }`
- Native interval: `136` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_SceneLoader_Recovered` matched 2 offsets against `bl_SceneLoader` metadata (confidence 0.67).

```c
typedef struct bl_SceneLoader_Recovered {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long SkipType;
    long long FadeInSpeed;
} bl_SceneLoader_Recovered;

extern long long g_1ef41a0;
extern char g_1fab3ae;

struct_0 * bl_SceneLoader_DoAsyncOperation(long long a0, long long a1)
{
    struct_0 *v0;  // x21
    struct_0 *ptr;  // x0
    struct_0 *p;  // x0

    if (!(g_1fab3ae & 1))
    {
        sub_f7d92c(&g_1ef41a0);
        g_1fab3ae = 1;
    }
    v0 = sub_f7db70(g_1ef41a0);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct bl_SceneLoader_Recovered *)&ptr->field_20, a0);
    p = ptr;
    p->field_28 = a1;
    sub_f7d8d0((struct bl_SceneLoader_Recovered *)&p->field_28, a1);
    return p;
}
```

## `bl_SceneLoader.StartFakeLoading` — RVA `0xc77908`

- Decompiled symbol: `bl_SceneLoader_StartFakeLoading`
- Metadata signature: `private IEnumerator StartFakeLoading() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef41a8;
extern char g_1fab3af;

struct_0 * bl_SceneLoader_StartFakeLoading(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab3af & 1))
    {
        sub_f7d92c(&g_1ef41a8);
        g_1fab3af = 1;
    }
    v0 = sub_f7db70(g_1ef41a8);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `bl_SceneLoader.ResetLoadScreen` — RVA `0xc77974`

- Decompiled symbol: `bl_SceneLoader_ResetLoadScreen`
- Metadata signature: `public bl_SceneLoader ResetLoadScreen() { }`
- Native interval: `44` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_SceneLoader_Recovered` matched 4 offsets against `bl_SceneLoader` metadata (confidence 1.00).

```c
typedef struct bl_SceneLoader_Recovered {
    char padding_0[160];
    unsigned long long k__BackingField;
    char padding_a8[8];
    char isOperationStarted;
    char FinishLoad;
    char padding_b2[2];
    unsigned int smoothValue;
} bl_SceneLoader_Recovered;

struct_0 * bl_SceneLoader_ResetLoadScreen(struct_0 *ptr)
{
    ptr->field_b0 = 0;
    ptr->field_a0 = 0;
    sub_f7d8d0((struct bl_SceneLoader_Recovered *)&ptr->field_a0, 0);
    ptr->field_b4 = 0;
    ptr->field_b1 = 0;
    return ptr;
}
```

## `bl_SceneLoader.Hide` — RVA `0xc779a0`

- Decompiled symbol: `bl_SceneLoader_Hide`
- Metadata signature: `public bl_SceneLoader Hide() { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[152];
    unsigned long long field_98;
} struct_0;

long long bl_SceneLoader_Hide(struct_0 *a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    if (a0->field_98)
        bl_LoadingScreenUI__ResetUI(); /* do not return */
    sub_f7db74(0);
}
```

## `bl_SceneLoader.<DoAsyncOperation>d__49.ctor` — RVA `0xc77a48`

- Decompiled symbol: `bl_SceneLoader_DoAsyncOperation_d__49_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void bl_SceneLoader_DoAsyncOperation_d__49_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `bl_SceneLoader.<StartFakeLoading>d__50.ctor` — RVA `0xc77a70`

- Decompiled symbol: `bl_SceneLoader_StartFakeLoading_d__50_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void bl_SceneLoader_StartFakeLoading_d__50_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `bl_SceneLoader.GetActiveLoader` — RVA `0xc77a98`

- Decompiled symbol: `bl_SceneLoader_GetActiveLoader`
- Metadata signature: `public static bl_SceneLoader GetActiveLoader() { }`
- Native interval: `268` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_0 *g_1eef458;
extern struct_1 *g_1ef0c58;
extern long long g_1f00230;
extern long long g_1f09b68;
extern char g_1fab3b0;

unsigned long long bl_SceneLoader_GetActiveLoader(void)
{
    unsigned long long ptr[5];  // x0
    unsigned long long v1;  // x8

    if (!(g_1fab3b0 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1f00230);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("S\"");
        sub_f7d92c(&g_1f09b68);
        g_1fab3b0 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    ptr = sub_1129ea4(g_1f00230);
    if (ptr)
    {
        v1 = ptr[3];
        if (v1)
        {
            if ((unsigned int)v1 >= 2)
            {
                if (!g_1eef458->field_e0)
                    sub_f7da5c(g_1eef458);
                Debug__LogWarning(g_1f0eb48, 0);
                v1 = ptr[3];
            }
            if ((unsigned int)v1)
                return ptr[4];
            sub_f7db7c();
        }
    }
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__LogWarning(g_1f09b68, 0);
    return 0;
}
```

## `bl_SceneLoader.ctor` — RVA `0xc77ba4`

- Decompiled symbol: `bl_SceneLoader_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `468` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_SceneLoader_Recovered` matched 13 offsets against `bl_SceneLoader` metadata (confidence 1.00).

```c
typedef struct bl_SceneLoader_Recovered {
    char padding_0[32];
    unsigned int SkipType;
    unsigned long long SceneSmoothLoad;
    unsigned int FadeOutSpeed;
    char padding_30[1];
    unsigned short useBackgrounds;
    char padding_33[1];
    unsigned long long TimePerBackground;
    unsigned int TimeBetweenBackground;
    long long StartFadeInCurve;
    char padding_48[4];
    unsigned long long TimePerTip;
    char padding_54[4];
    unsigned int mainLoadScale;
    char padding_5c[4];
    unsigned int LoadingCircleSpeed;
    char padding_64[4];
    long long LoadingTextFormat;
    unsigned long long AudioVolume;
    unsigned int FinishSoundVolume;
} bl_SceneLoader_Recovered;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    char field_20[28];
    char field_2c;
    char padding_2d[15];
    char field_3c[28];
    char field_48;
} struct_1;

extern long long g_1eee230;
extern char g_1fab3b1;

long long bl_SceneLoader_ctor(struct_0 *ptr)
{
    struct_1 *p;  // x20
    long long v9;  // x21
    struct_0 *addr;  // x0
    struct_0 *ptr3;  // x0
    unsigned long v12;  // x0
    int v0;  // [bp-0xb0]
    char v1;  // [bp-0xa4]
    int v2;  // [bp-0x90]
    unsigned long long choice;  // [bp-0x80]
    unsigned int flag;  // [bp-0x78]
    int v5;  // [bp-0x70]
    unsigned long flag2;  // [bp-0x50]
    int v7;  // [bp-0x48]

    if (!(g_1fab3b1 & 1))
    {
        sub_f7d92c("W,");
        sub_f7d92c(&g_1eee230);
        sub_f7d92c(")?");
        g_1fab3b1 = 1;
    }
    ptr->field_20 = 1;
    *((unsigned int *)((char *)&ptr->field_24 + 4)) = 0x40000000;
    *((unsigned short *)((char *)&ptr->field_2c + 1)) = 257;
    *((unsigned long *)&(&ptr->field_20)[1]) = 0x4000000040400000;
    *((unsigned long *)&ptr->padding_30) = 0x4000000040a00000;
    *((unsigned int *)&(&ptr->padding_33)[4]) = 0x3f000000;
    p = sub_f7d9d4(g_1eee230, 2);
    flag2 = 0;
    *((unsigned long long *)&v7) = 0;
    *((unsigned int *)&(&v7)[16]) = 0;
    *((unsigned long long *)&(&v7)[8]) = 0;
    Keyframe__ctor(&flag2, 0);
    if (p)
    {
        memcpy(&v5, &flag2, 16);
        *((uint128_t *)&(&v5)[12]) = *((uint128_t *)(&v7 + 4));
        if (p->field_18)
        {
            *((uint128_t *)&p->field_20[12]) = *((uint128_t *)(&v5 + 12));
            *((uint128_t *)&p->field_20[0]) = *((uint128_t *)&v5);
            *((unsigned long long *)&v2) = 0;
            *((unsigned long long *)&(&v2)[8]) = 0;
            flag = 0;
            choice = 0;
            Keyframe__ctor(&v2, 0);
            memcpy(&v1, &v2 - 12, 16);
            v0 = v2;
            if (p->field_18 > 1)
            {
                *((uint128_t *)&p->padding_2d[11]) = *((uint128_t *)(&v0 + 12));
                *((uint128_t *)&p->field_2c) = *((uint128_t *)&v0);
                v9 = sub_f7db70(g_1eee7c8);
                AnimationCurve__ctor(v9, p, 0);
                addr = ptr;
                addr->field_34 = v9;
                sub_f7d8d0((struct bl_SceneLoader_Recovered *)&addr->field_34, v9);
                *((unsigned long *)&(&ptr->field_3c)[1]) = 0x4000000040a00000;
                *((unsigned int *)&ptr->padding_48[0]) = 0x3f800000;
                *((unsigned int *)&ptr->field_4c) = 0x43960000;
                ptr3 = ptr;
                *((long long *)&ptr3->padding_54) = g_1f15e90;
                sub_f7d8d0((struct bl_SceneLoader_Recovered *)&ptr3->padding_54, g_1f15e90);
                *((unsigned long *)&ptr->padding_5c) = 0x3f0000003f800000;
                *((unsigned int *)&ptr->padding_64[0]) = 0x3f000000;
                v12 = MonoBehaviour__ctor(ptr, 0);
                return MonoBehaviour__ctor(ptr, 0);
            }
        }
        sub_f7db7c();
    }
    sub_f7db74();
}
```

## `bl_SceneLoader.<AsynLoadData>d__38.Dispose` — RVA `0xc77d80`

- Decompiled symbol: `bl_SceneLoader_AsynLoadData_d__38_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long bl_SceneLoader_AsynLoadData_d__38_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `bl_SceneLoader.<AsynLoadData>d__38.MoveNext` — RVA `0xc77d84`

- Decompiled symbol: `bl_SceneLoader_AsynLoadData_d__38_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `248` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_2 {
    char padding_0[168];
    unsigned long long field_a8;
} struct_2;

typedef struct struct_0 {
    char padding_0[168];
    long long field_a8;
} struct_0;

extern long long g_1ef2430;
extern char g_1fab3b2;

unsigned int bl_SceneLoader_AsynLoadData_d__38_MoveNext(struct_1 *ptr)
{
    unsigned int flag;  // w8
    long long v1;  // x1
    struct_1 *p;  // x0
    long long v3;  // x20
    struct_1 *addr;  // x0
    struct_2 *v5;  // x20
    long long v6;  // x0
    long long v7;  // x1
    struct_2 *ptr3;  // x0

    if (!(g_1fab3b2 & 1))
    {
        sub_f7d92c(&g_1ef2430);
        g_1fab3b2 = 1;
    }
    flag = ptr->field_10;
    if (flag != 2)
    {
        if (flag == 1)
        {
            ptr->field_10 = 4294967295;
            v3 = sub_f7db70(g_1ef2430);
            WaitForEndOfFrame__ctor(v3, 0);
            addr = ptr;
            addr->field_18 = v3;
            sub_f7d8d0((struct struct_1 *)&addr->field_18, v3);
            ptr->field_10 = 2;
            return 1;
        }
        else if (!flag)
        {
            ptr->field_10 = 4294967295;
            v1 = bl_SceneLoaderManager__AsyncLoadData(0);
            p = ptr;
            p->field_18 = v1;
            sub_f7d8d0((struct struct_1 *)&p->field_18, v1);
            ptr->field_10 = 1;
            return 1;
        }
        else
        {
            return 0;
        }
    }
    v5 = ptr->field_20;
    ptr->field_10 = 4294967295;
    v6 = bl_SceneLoaderManager__get_Instance(0);
    if (v5)
    {
        v7 = v6;
        ptr3 = v5;
        ptr3->field_a8 = v7;
        sub_f7d8d0((struct struct_2 *)&ptr3->field_a8, v7);
        bl_SceneLoader__Init(v5, v7); /* do not return */
    }
    sub_f7db74();
}
```

## `bl_SceneLoader.<AsynLoadData>d__38.get_Current` — RVA `0xc77e7c`

- Decompiled symbol: `bl_SceneLoader_AsynLoadData_d__38_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_SceneLoader_AsynLoadData_d__38_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_SceneLoader.<AsynLoadData>d__38.Reset` — RVA `0xc77e84`

- Decompiled symbol: `bl_SceneLoader_AsynLoadData_d__38_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05518;

void bl_SceneLoader_AsynLoadData_d__38_Reset(void)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = sub_f7db70(sub_f7d940(&g_1ef0bd8));
    NotSupportedException__ctor(v4, 0);
    sub_f7da4c(v4, sub_f7d940(&g_1f05518));
}
```

## `bl_SceneLoader.<AsynLoadData>d__38.get_Current` — RVA `0xc77ebc`

- Decompiled symbol: `bl_SceneLoader_AsynLoadData_d__38_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_SceneLoader_AsynLoadData_d__38_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_SceneLoader.<DoAsyncOperation>d__49.Dispose` — RVA `0xc77ec4`

- Decompiled symbol: `bl_SceneLoader_DoAsyncOperation_d__49_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long bl_SceneLoader_DoAsyncOperation_d__49_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `bl_SceneLoader.<DoAsyncOperation>d__49.MoveNext` — RVA `0xc77ec8`

- Decompiled symbol: `bl_SceneLoader_DoAsyncOperation_d__49_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `392` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    unsigned long long field_18;
    struct struct_1 *field_20;
    unsigned int field_28;
    char padding_2c[4];
    unsigned int field_30;
} struct_2;

typedef struct struct_1 {
    char padding_0[40];
    unsigned int field_28;
    char padding_2c[4];
    char field_30;
    char padding_31[15];
    long long field_40;
    char padding_48[80];
    struct struct_0 *field_98;
} struct_1;

typedef struct struct_0 {
    char padding_0[144];
    long long field_90;
} struct_0;

unsigned int bl_SceneLoader_DoAsyncOperation_d__49_MoveNext(struct_2 *ptr)
{
    unsigned int flag;  // w8
    unsigned int v1;  // w20
    struct_1 *index;  // x21
    unsigned int v3;  // s8
    unsigned int v4;  // s0
    unsigned long v5;  // 4135
    unsigned int v6;  // w8

    flag = ptr->field_10;
    v1 = 0;
    if (flag != 2)
    {
        index = ptr->field_20;
        if (flag == 1)
        {
            v3 = ptr->field_30;
            v4 = 0x3f800000;
            ptr->field_10 = 4294967295;
            v5 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v3, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v3, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v3, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v3, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v5)
                bl_SceneLoaderUtils__LoadLevelAsync(*((long long *)&ptr->field_28)); /* do not return */
        }
        else if (!flag)
        {
            v3 = 0;
            ptr->field_30 = 0;
            ptr->field_10 = 4294967295;
        }
        else
        {
            return 0;
        }
        if (!index)
            sub_f7db74();
        if (index->field_30)
            Time__get_deltaTime(0);
        else
            Time__get_unscaledDeltaTime(0);
        ptr->field_30 = v3 + v4 * index->field_28;
        if (!index->field_40)
            sub_f7db74();
        AnimationCurve__Evaluate(index->field_40, 0);
        if (!index->field_98)
        {
            sub_f7db74();
        }
        else if (index->field_98->field_90)
        {
            CanvasGroup__set_alpha(index->field_98->field_90, 0);
            ptr->field_18 = 0;
            sub_f7d8d0((struct struct_2 *)&ptr->field_18, 0);
            v6 = 1;
            v1 = 1;
        }
        else
        {
            sub_f7db74();
        }
    }
    else
    {
        v6 = 4294967295;
    }
    ptr->field_10 = v6;
    return v1;
}
```

## `bl_SceneLoader.<DoAsyncOperation>d__49.get_Current` — RVA `0xc78050`

- Decompiled symbol: `bl_SceneLoader_DoAsyncOperation_d__49_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_SceneLoader_DoAsyncOperation_d__49_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_SceneLoader.<DoAsyncOperation>d__49.Reset` — RVA `0xc78058`

- Decompiled symbol: `bl_SceneLoader_DoAsyncOperation_d__49_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05520;

void bl_SceneLoader_DoAsyncOperation_d__49_Reset(void)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = sub_f7db70(sub_f7d940(&g_1ef0bd8));
    NotSupportedException__ctor(v4, 0);
    sub_f7da4c(v4, sub_f7d940(&g_1f05520));
}
```

## `bl_SceneLoader.<DoAsyncOperation>d__49.get_Current` — RVA `0xc78090`

- Decompiled symbol: `bl_SceneLoader_DoAsyncOperation_d__49_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_SceneLoader_DoAsyncOperation_d__49_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_SceneLoader.<StartFakeLoading>d__50.Dispose` — RVA `0xc78098`

- Decompiled symbol: `bl_SceneLoader_StartFakeLoading_d__50_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long bl_SceneLoader_StartFakeLoading_d__50_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `bl_SceneLoader.<StartFakeLoading>d__50.MoveNext` — RVA `0xc7809c`

- Decompiled symbol: `bl_SceneLoader_StartFakeLoading_d__50_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `228` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_1 {
    char padding_0[180];
    unsigned int field_b4;
    char padding_b8[8];
    struct struct_0 *field_c0;
} struct_1;

typedef struct struct_0 {
    char padding_0[48];
    unsigned int field_30;
} struct_0;

extern long long g_1ef2430;
extern char g_1fab3b3;

unsigned int bl_SceneLoader_StartFakeLoading_d__50_MoveNext(struct_2 *ptr)
{
    struct_1 *p;  // x20
    unsigned int v1;  // s8
    unsigned long v2;  // 4129
    long long v3;  // x20
    struct_2 *addr;  // x19

    if (!(g_1fab3b3 & 1))
    {
        sub_f7d92c(&g_1ef2430);
        g_1fab3b3 = 1;
    }
    p = ptr->field_20;
    if (ptr->field_10 != 1)
    {
        if (ptr->field_10)
            return 0;
        ptr->field_10 = 4294967295;
        if (p)
        {
            p->field_b4 = 0;
LABEL_1078100:
            v1 = p->field_b4;
            v2 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v1, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v1, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v1, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v1, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v2)
                return 0;
            Time__get_deltaTime(0);
            if (p->field_c0)
            {
                p->field_b4 = v1 + 0x3f800000 / p->field_c0->field_30;
                v3 = sub_f7db70(g_1ef2430);
                WaitForEndOfFrame__ctor(v3, 0);
                ptr->field_18 = v3;
                addr = &ptr->field_18;
                sub_f7d8d0(addr, v3);
                *((unsigned int *)&addr->padding_0[8]) = 1;
                return 1;
            }
        }
    }
    else
    {
        ptr->field_10 = 4294967295;
        if (p)
            goto LABEL_1078100;
    }
    sub_f7db74();
}
```

## `bl_SceneLoader.<StartFakeLoading>d__50.get_Current` — RVA `0xc78180`

- Decompiled symbol: `bl_SceneLoader_StartFakeLoading_d__50_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_SceneLoader_StartFakeLoading_d__50_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_SceneLoader.<StartFakeLoading>d__50.Reset` — RVA `0xc78188`

- Decompiled symbol: `bl_SceneLoader_StartFakeLoading_d__50_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05528;

void bl_SceneLoader_StartFakeLoading_d__50_Reset(void)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = sub_f7db70(sub_f7d940(&g_1ef0bd8));
    NotSupportedException__ctor(v4, 0);
    sub_f7da4c(v4, sub_f7d940(&g_1f05528));
}
```

## `bl_SceneLoader.<StartFakeLoading>d__50.get_Current` — RVA `0xc781c0`

- Decompiled symbol: `bl_SceneLoader_StartFakeLoading_d__50_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_SceneLoader_StartFakeLoading_d__50_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
