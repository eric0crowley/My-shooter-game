# Native pseudocode: WaveManager

> Metadata source-path string: `Assets/RFPSP/Scripts/AI/WaveManager.cs`. This is a path string from the APK metadata, not recovered source text.

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `WaveManager.StartWave` — RVA `0xc87770`

- Decompiled symbol: `WaveManager_StartWave`
- Metadata signature: `public IEnumerator StartWave() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef3ff0;
extern char g_1fab42b;

struct_0 * WaveManager_StartWave(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab42b & 1))
    {
        sub_f7d92c(&g_1ef3ff0);
        g_1fab42b = 1;
    }
    v0 = sub_f7db70(g_1ef3ff0);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `WaveManager.Start` — RVA `0xc87aa0`

- Decompiled symbol: `WaveManager_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `704` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WaveManager_Recovered` matched 2 offsets against `WaveManager` metadata (confidence 1.00).

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

typedef struct struct_7 {
    char padding_0[32];
    struct struct_8 *field_20;
    char padding_28[24];
    unsigned int field_40;
    unsigned int field_44;
    unsigned int field_48;
    unsigned int field_4c;
    char padding_50[16];
    long long field_60;
    char padding_68[8];
    struct struct_9 *field_70;
    struct struct_4 *field_78;
    struct struct_5 *field_80;
    struct WaveManager_Recovered *field_88;
    uint128_t field_90;
    uint128_t field_a0;
    long long field_b0;
    long long field_b8;
    unsigned int field_c0;
    unsigned int field_c4;
    unsigned int field_c8;
    unsigned int field_cc;
} struct_7;

typedef struct struct_1 {
    char padding_0[32];
    unsigned int field_20;
} struct_1;

typedef struct struct_2 {
    char padding_0[32];
    unsigned int field_20;
    char padding_24[4];
    uint128_t field_28;
} struct_2;

typedef struct struct_3 {
    char padding_0[32];
    unsigned int field_20;
    char padding_24[4];
    uint128_t field_28;
} struct_3;

typedef struct struct_5 {
    char padding_0[32];
    unsigned int field_20;
    char padding_24[4];
    uint128_t field_28;
} struct_5;

typedef struct struct_8 {
    char padding_0[336];
    long long field_150;
    long long field_158;
    long long field_160;
    long long field_168;
} struct_8;

typedef struct struct_9 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
} struct_9;

typedef struct struct_4 {
    char padding_0[32];
    unsigned int field_20;
} struct_4;

typedef struct WaveManager_Recovered {
    char padding_0[32];
    unsigned int FPSPlayerComponent;
    char padding_24[4];
    uint128_t NpcSpawners;
} WaveManager_Recovered;

extern long long g_1efcf38;
extern long long g_1efd0b0;
extern long long g_1efea78;
extern long long g_1efebb8;
extern long long g_1efed08;
extern long long g_1efed10;
extern char g_1fab42a;

void WaveManager_Start(struct_7 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    struct_7 *v14;  // x21
    unsigned int v15[10];  // x0
    struct_7 *ptr5;  // x20
    struct_7 *v17;  // x20
    struct_1 *v18;  // x0
    struct_7 *ptr6;  // x20
    struct_7 *p;  // x20
    unsigned int addr[10];  // x8
    unsigned int v22;  // w10
    struct_1 *ptr3;  // x9
    unsigned long long v6;  // x20
    unsigned int v24;  // w10
    struct_2 *v25;  // x0
    struct_7 *ptr7;  // x20
    struct_7 *v27;  // x20
    struct_3 *v28;  // x0
    struct_7 *ptr8;  // x20
    struct_7 *ptr13;  // x20
    struct_5 *ptr14;  // x0
    struct_3 *ptr4;  // x8
    int v33;  // q0
    unsigned long long v7;  // x19
    unsigned int v34;  // s1
    long long v35;  // x0
    struct_7 *ptr9;  // x20
    struct_7 *v37;  // x20
    long long v38;  // x0
    struct_7 *ptr10;  // x20
    struct_7 *v40;  // x20
    long long v41;  // x0
    struct_0 *v8;  // x0
    unsigned long long v9[46];  // x0
    struct_7 *ptr11;  // x20
    struct_7 *v11;  // x20
    long long v12;  // x0
    struct_7 *ptr12;  // x21
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab42a & 1))
    {
        sub_f7d92c(&g_1efcf38);
        sub_f7d92c(&g_1efd0b0);
        sub_f7d92c(&g_1efea78);
        sub_f7d92c(&g_1efebb8);
        sub_f7d92c(&g_1efed08);
        sub_f7d92c(&g_1efed10);
        g_1fab42a = 1;
    }
    if (Camera__get_main(0))
    {
        v8 = sub_1231bc8();
        if (v8 && v8->field_28)
        {
            v9 = sub_1249224(v8->field_28, g_1efebb8);
            ptr11 = ptr;
            ptr11->field_20 = v9;
            v11 = &ptr11->field_20;
            sub_f7d8d0(v11, v9);
            if (Component__get_gameObject(ptr, 0))
            {
                v12 = sub_124913c();
                ptr12 = ptr;
                ptr12->field_60 = v12;
                v14 = &ptr12->field_60;
                sub_f7d8d0(v14, v12);
                if (*((long long *)&v14->padding_0[0]))
                {
                    AudioSource__set_spatialBlend(*((long long *)&v14->padding_0[0]), 0);
                    if (*((long long *)&v11->padding_0[0]) && *((long long *)(*((long long *)&v11->padding_0[0]) + 336)))
                    {
                        v15 = sub_1249224(*((long long *)(*((long long *)&v11->padding_0[0]) + 336)), g_1efed10);
                        ptr5 = ptr;
                        ptr5->field_70 = v15;
                        v17 = &ptr5->field_70;
                        sub_f7d8d0(v17, v15);
                        if (*((long long *)&v17->padding_50[0]) && *((long long *)(*((long long *)&v17->padding_50[0]) + 344)))
                        {
                            v18 = sub_1249224(*((long long *)(*((long long *)&v17->padding_50[0]) + 344)), g_1efed10);
                            ptr6 = ptr;
                            ptr6->field_78 = v18;
                            p = &ptr6->field_78;
                            sub_f7d8d0(p, v18);
                            addr = *((long long *)&p->padding_0[8]);
                            if (addr)
                            {
                                v22 = *((int *)&p->padding_28[4]);
                                addr[8] = v22;
                                ptr3 = *((long long *)&p->padding_0[0]);
                                if (ptr3)
                                {
                                    ptr3->field_20 = v22;
                                    v24 = ptr->field_44 - ptr->field_48;
                                    addr[9] = v24;
                                    *((unsigned int *)&ptr3[1].padding_0[0]) = v24;
                                    if (ptr->field_20 && ptr->field_20->field_160)
                                    {
                                        v25 = sub_1249224(ptr->field_20->field_160, g_1efed08);
                                        ptr7 = ptr;
                                        ptr7->field_80 = v25;
                                        v27 = &ptr7->field_80;
                                        sub_f7d8d0(v27, v25);
                                        if (v27->field_60 && *((long long *)(v27->field_60 + 360)))
                                        {
                                            v28 = sub_1249224(*((long long *)(v27->field_60 + 360)), g_1efed08);
                                            ptr8 = ptr;
                                            ptr8->field_88 = v28;
                                            ptr13 = &ptr8->field_88;
                                            sub_f7d8d0(ptr13, v28);
                                            ptr14 = *((long long *)&ptr13->padding_0[8]);
                                            if (ptr14)
                                            {
                                                ptr4 = ptr->field_88;
                                                ptr->field_90 = *((int128_t *)&(&ptr14->padding_24)[1]);
                                                if (ptr4)
                                                {
                                                    v33 = (int)*((int128_t *)&(&ptr4->padding_24)[1]);
                                                    v34 = ptr->field_40;
                                                    *((void*)&ptr->field_a0) = v33;
                                                    ptr14->field_20 = v34;
                                                    ptr4->field_20 = v34;
                                                    v35 = sub_1231bc8();
                                                    ptr9 = ptr;
                                                    ptr9->field_b0 = v35;
                                                    v37 = &ptr9->field_b0;
                                                    sub_f7d8d0(v37, v35);
                                                    if (*((long long *)&v37->padding_28[0]))
                                                    {
                                                        v38 = sub_1231bc8(*((long long *)&v37->padding_28[0]), g_1efd0b0);
                                                        ptr10 = ptr;
                                                        ptr10->field_b8 = v38;
                                                        v40 = &ptr10->field_b8;
                                                        sub_f7d8d0(v40, v38);
                                                        if (*((long long *)&v40->padding_0[8]) && Graphic__get_rectTransform(*((long long *)&v40->padding_0[8]), 0))
                                                        {
                                                            RectTransform__get_anchoredPosition();
                                                            v41 = ptr->field_b8;
                                                            ptr->field_c0 = *((unsigned int *)&v33);
                                                            ptr->field_c4 = v34;
                                                            if (v41 && Graphic__get_rectTransform(v41, 0))
                                                            {
                                                                RectTransform__get_anchoredPosition();
                                                                ptr->field_c8 = *((unsigned int *)&v33);
                                                                ptr->field_cc = v34;
                                                                WaveManager__StartWave(ptr);
                                                                MonoBehaviour__StartCoroutine();
                                                                return;
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```


## `WaveManager.FixedUpdate` — RVA `0xc87d60`

- Decompiled symbol: `WaveManager_FixedUpdate`
- Metadata signature: `private void FixedUpdate() { }`
- Native interval: `60` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WaveManager_Recovered` matched 4 offsets against `WaveManager` metadata (confidence 1.00).

```c
typedef struct WaveManager_Recovered {
    char padding_0[68];
    unsigned int NpcsToSpawn;
    unsigned int killedNpcs;
    char padding_4c[36];
    struct struct_0 *WaveText;
    unsigned long long WaveTextShadow;
} WaveManager_Recovered;

typedef struct struct_0 {
    char padding_0[36];
    unsigned int field_24;
} struct_0;

void WaveManager_FixedUpdate(struct_1 *ptr, unsigned long a1)
{
    struct_0 *p;  // x8
    unsigned int v1;  // w9

    p = ptr->field_70;
    if (p)
    {
        v1 = ptr->field_44 - ptr->field_48;
        if (p->field_24 == v1)
            return;
        p->field_24 = v1;
        if (ptr->field_78)
        {
            *((unsigned int *)(ptr->field_78 + 36)) = v1;
            return;
        }
    }
    sub_f7db74();
}
```


## `WaveManager.<StartWave>d__29.ctor` — RVA `0xc87d9c`

- Decompiled symbol: `WaveManager_StartWave_d__29_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void WaveManager_StartWave_d__29_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `WaveManager.FadeWarmupText` — RVA `0xc87dc4`

- Decompiled symbol: `WaveManager_FadeWarmupText`
- Metadata signature: `private IEnumerator FadeWarmupText() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern long long g_1ef3fe8;
extern char g_1fab42c;

struct_0 * WaveManager_FadeWarmupText(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab42c & 1))
    {
        sub_f7d92c(&g_1ef3fe8);
        g_1fab42c = 1;
    }
    v0 = sub_f7db70(g_1ef3fe8);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0(&ptr->field_20, a0);
    return ptr;
}
```


## `WaveManager.<FadeWarmupText>d__30.ctor` — RVA `0xc87e30`

- Decompiled symbol: `WaveManager_FadeWarmupText_d__30_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void WaveManager_FadeWarmupText_d__30_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```


## `WaveManager.ctor` — RVA `0xc87e58`

- Decompiled symbol: `WaveManager_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `148` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WaveManager_Recovered` matched 2 offsets against `WaveManager` metadata (confidence 1.00).

```c
typedef struct WaveManager_Recovered {
    char padding_0[40];
    long long NpcSpawners;
    char padding_30[8];
    unsigned long long warmupTime;
} WaveManager_Recovered;

extern long long g_1eed758;
extern long long g_1ef8188;
extern char g_1fab42d;

void WaveManager_ctor(struct_0 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x20
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
    if (!(g_1fab42d & 1))
    {
        sub_f7d92c(&g_1ef8188);
        sub_f7d92c(&g_1eed758);
        g_1fab42d = 1;
    }
    v10 = sub_f7db70(g_1eed758);
    sub_14a2b64(v10, g_1ef8188);
    ptr->field_28 = v10;
    sub_f7d8d0(&ptr->field_28, v10);
    ptr->field_38 = 0xc400000041f00000;
}
```


## `WaveManager.<FadeWarmupText>d__30.Dispose` — RVA `0xc87eec`

- Decompiled symbol: `WaveManager_FadeWarmupText_d__30_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long WaveManager_FadeWarmupText_d__30_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `WaveManager.<FadeWarmupText>d__30.MoveNext` — RVA `0xc87ef0`

- Decompiled symbol: `WaveManager_FadeWarmupText_d__30_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `388` bytes
- Result: `pseudocode`

```c
typedef struct struct_4 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    struct struct_2 *field_20;
} struct_4;

typedef struct struct_2 {
    char padding_0[156];
    unsigned int field_9c;
    char padding_a0[12];
    unsigned int field_ac;
    struct struct_3 *field_b0;
} struct_2;

typedef struct struct_0 {
    char padding_0[680];
    struct struct_1 *field_2a8;
    unsigned long long field_2b0;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

unsigned int WaveManager_FadeWarmupText_d__30_MoveNext(struct_4 *p)
{
    struct_2 *ptr;  // x20
    unsigned int v1;  // s9
    unsigned int v2;  // s0
    unsigned int v3;  // s0
    struct_0 **v4;  // x0
    unsigned long long v5;  // x1

    if (1 < p->field_10)
        return 0;
    ptr = p->field_20;
    p->field_10 = 4294967295;
    if (ptr)
    {
        Time__get_deltaTime(0);
        v1 = ptr->field_ac;
        v3 = ptr->field_9c - v2;
        ptr->field_9c = v3;
        Time__get_deltaTime(0);
        v4 = ptr->field_b0;
        ptr->field_ac = v1 - v3;
        if (v4)
        {
            v5 = *(v4)->field_2b0;
            *(v4)->field_2a8();
        }
    }
    sub_f7db74();
}
```


## `WaveManager.<FadeWarmupText>d__30.get_Current` — RVA `0xc88074`

- Decompiled symbol: `WaveManager_FadeWarmupText_d__30_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long WaveManager_FadeWarmupText_d__30_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `WaveManager.<FadeWarmupText>d__30.Reset` — RVA `0xc8807c`

- Decompiled symbol: `WaveManager_FadeWarmupText_d__30_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05350;

void WaveManager_FadeWarmupText_d__30_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f05350));
}
```


## `WaveManager.<FadeWarmupText>d__30.get_Current` — RVA `0xc880b4`

- Decompiled symbol: `WaveManager_FadeWarmupText_d__30_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long WaveManager_FadeWarmupText_d__30_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `WaveManager.<StartWave>d__29.Dispose` — RVA `0xc880bc`

- Decompiled symbol: `WaveManager_StartWave_d__29_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long WaveManager_StartWave_d__29_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `WaveManager.<StartWave>d__29.MoveNext` — RVA `0xc880c0`

- Decompiled symbol: `WaveManager_StartWave_d__29_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `1620` bytes
- Result: `pseudocode`

```c
typedef struct struct_10 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    struct struct_7 *field_20;
} struct_10;

typedef struct struct_7 {
    char padding_0[32];
    long long field_20;
    struct struct_1 *field_28;
    unsigned long long field_30;
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
    unsigned int field_44;
    unsigned int field_48;
    int field_4c;
    char padding_50[8];
    long long field_58;
    long long field_60;
    char padding_68[1];
    char field_69;
    char field_6a;
    char padding_6b[5];
    struct struct_2 *field_70;
    struct struct_3 *field_78;
    struct struct_4 *field_80;
    struct struct_8 *field_88;
    char padding_90[12];
    unsigned int field_9c;
    char padding_a0[12];
    unsigned int field_ac;
    struct struct_9 *field_b0;
    long long field_b8;
    uint128_t field_c0;
    uint128_t field_d0;
} struct_7;

typedef struct struct_4 {
    char padding_0[32];
    unsigned int field_20;
    char padding_24[20];
    char field_38;
    char field_39;
} struct_4;

typedef struct struct_2 {
    char padding_0[32];
    int field_20;
} struct_2;

typedef struct struct_3 {
    char padding_0[32];
    int field_20;
} struct_3;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct struct_11 {
    char padding_0[40];
    long long field_28;
    unsigned int field_30;
    char padding_34[56];
    unsigned int field_6c;
    unsigned int field_70;
} struct_11;

typedef struct struct_18 {
    char padding_0[24];
    unsigned int field_18;
} struct_18;

typedef struct struct_21 {
    char padding_0[24];
    unsigned int field_18;
} struct_21;

typedef struct struct_17 {
    char padding_0[24];
    unsigned int field_18;
} struct_17;

typedef struct struct_20 {
    char padding_0[24];
    unsigned int field_18;
} struct_20;

typedef struct struct_12 {
    char padding_0[112];
    unsigned int field_70;
} struct_12;

typedef struct struct_13 {
    char padding_0[120];
    char field_78;
} struct_13;

typedef struct struct_14 {
    char padding_0[116];
    unsigned int field_74;
} struct_14;

typedef struct struct_15 {
    char padding_0[105];
    char field_69;
} struct_15;

typedef struct struct_16 {
    char padding_0[104];
    char field_68;
} struct_16;

typedef struct struct_5 {
    char padding_0[680];
    struct struct_6 *field_2a8;
    unsigned long long field_2b0;
} struct_5;

typedef struct struct_8 {
    char padding_0[56];
    char field_38;
    char field_39;
} struct_8;

typedef struct struct_9 {
    struct struct_5 *field_0;
} struct_9;

typedef struct struct_6 {
    unsigned long long field_0;
} struct_6;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef8190;
extern long long g_1ef8198;
extern char g_1fab42e;

unsigned int WaveManager_StartWave_d__29_MoveNext(struct_10 *addr)
{
    struct_7 *ptr;  // x20
    unsigned int v1;  // s0
    long long v10;  // x21
    struct_1 *v12;  // x0
    unsigned long v13;  // x21
    struct_11 *p;  // x0
    unsigned long long v15;  // x8
    int v16;  // w9
    struct_18 *v17;  // x8
    unsigned long v18;  // x1
    unsigned long long v19;  // x8
    struct_4 *ptr3;  // x8
    int v20;  // w9
    struct_21 *v21;  // x8
    unsigned long long v22;  // x8
    int v23;  // w9
    struct_17 *v24;  // x8
    unsigned long long v25;  // x8
    int v26;  // w9
    struct_20 *v27;  // x8
    struct_12 *idx11;  // x0
    struct_1 *v29;  // x0
    char ptr4[58];  // x9
    struct_13 *ptr5;  // x0
    struct_14 *ptr6;  // x0
    struct_15 *ptr7;  // x0
    struct_16 *ptr8;  // x0
    uint128_t v34;  // q0
    unsigned int v35;  // s8
    unsigned long v37;  // d0
    unsigned long v38;  // 4144
    struct_4 *ptr9;  // x8
    unsigned long long v4;  // x11
    unsigned int v40;  // s0
    unsigned long long flag;  // x2
    struct_5 **v42;  // x0
    unsigned long long v43;  // x1
    int v5;  // w10
    int v6;  // w10
    unsigned long v7;  // 4102
    struct_2 *ptr10;  // x11
    struct_4 *ptr11;  // x9

    if (!(g_1fab42e & 1))
    {
        sub_f7d92c(&g_1ef8190);
        sub_f7d92c(&g_1ef8198);
        sub_f7d92c(&g_1ef0c58);
        g_1fab42e = 1;
    }
    ptr = addr->field_20;
    if (addr->field_10 != 1)
    {
        if (addr->field_10)
            return 0;
        addr->field_10 = 4294967295;
        if (ptr && (v1 = ptr->field_38, ptr3 = (struct_4 *)ptr->field_80, ptr->field_40 = v1, ptr3 && (ptr3->field_20 = v1, ptr4 = (char [58])ptr->field_88, ptr4 && (*((unsigned int *)&ptr4[32]) = v1, v4 = ptr->field_30, ptr->field_44 = 0, ptr->field_48 = 0, v4))))
        {
            v5 = ptr->field_4c;
            if (v5 > *((int *)(v4 + 24)))
            {
                v6 = 1;
            }
            else
            {
                v7 = arm64g_calculate_condition(163, (unsigned long long)(unsigned int)v5, (unsigned long long)(unsigned int)*((int *)(v4 + 24)), 0);
                if (!((char)v7))
                {
                    v6 = v5 + 1;
                }
                else
                {
                    v6 = 1;
                    ptr->field_6a = 1;
                }
            }
            ptr10 = ptr->field_70;
            ptr->field_4c = v6;
            if (ptr10 && (ptr10->field_20 = v6, ptr->field_78))
            {
                ptr->field_78->field_20 = v6;
                ptr->field_9c = 0x3f800000;
                ptr->field_ac = 0x3f800000;
                ptr3->field_38 = 0;
                ptr4[56] = 0;
                if (1 < v6 || ptr->field_6a)
                {
                    Time__get_time(0);
                    ptr11 = ptr->field_80;
                    ptr->field_3c = v1;
                    if (ptr11 && (ptr11->field_39 = 1, ptr->field_88))
                    {
                        ptr->field_88->field_39 = 1;
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        if (!(((char)Object__op_Implicit(ptr->field_58, 0) & 1) && !ptr->field_69))
                        {
LABEL_108841c:
                            if (ptr->field_6a)
                            {
                                ptr->field_6a = 0;
                                goto LABEL_1088428;
                            }
                        }
                        else if (ptr->field_60 && (AudioSource__PlayOneShot(ptr->field_60, ptr->field_58, 0), v10 = ptr->field_20, v10))
                        {
                            MonoBehaviour__StartCoroutine(v10, FPSPlayer__ActivateBulletTime(v10, 0), 0);
                            ptr->field_69 = 1;
                            goto LABEL_108841c;
                        }
                    }
                }
                else
                {
LABEL_1088428:
                    v12 = ptr->field_28;
                    if (v12)
                    {
                        v13 = 0;
                        do
                        {
                            if (v12->field_18 <= v13)
                                goto LABEL_0x1088180;
                            p = sub_14a30c0();
                            v15 = ptr->field_30;
                            if (!v15)
                                break;
                            v16 = ptr->field_4c - 1;
                            if (*((int *)(v15 + 24)) <= v16)
                                goto LABEL_1088710;
                            if (!*((long long *)(v15 + v16 * 8 + 32)) || (v17 = (struct_18 *)*((long long *)(*((long long *)(v15 + (unsigned long long)v16 * 8 + 32)) + 40)), !v17))
                                break;
                            if (v17->field_18 <= v13)
                                goto LABEL_1088710;
                            if (!p || (v18 = (unsigned long)*((long long *)&v17[1].padding_0[4 + 8 * v13]), p->field_28 = (long long)v18, sub_f7d8d0(p + 40, v18), !ptr->field_28 || (p = (struct_11 *)(unsigned long long)sub_14a30c0(ptr->field_28, v13 & 4294967295, g_1ef8198), v19 = ptr->field_30, !v19)))
                                break;
                            v20 = ptr->field_4c - 1;
                            if (*((int *)(v19 + 24)) <= v20)
                                goto LABEL_1088710;
                            if (!*((long long *)(v19 + v20 * 8 + 32)) || (v21 = (struct_21 *)*((long long *)(*((long long *)(v19 + (unsigned long long)v20 * 8 + 32)) + 16)), !v21))
                                break;
                            if (v21->field_18 <= v13)
                                goto LABEL_1088710;
                            if (!p || (p->field_70 = (unsigned int)*((int *)&v21[1].padding_0[4 + 4 * v13]), !ptr->field_28 || (p = (struct_11 *)(unsigned long long)sub_14a30c0(ptr->field_28, v13 & 4294967295, g_1ef8198), v22 = ptr->field_30, !v22)))
                                break;
                            v23 = ptr->field_4c - 1;
                            if (*((int *)(v22 + 24)) <= v23)
                                goto LABEL_1088710;
                            if (!*((long long *)(v22 + v23 * 8 + 32)) || (v24 = (struct_17 *)*((long long *)(*((long long *)(v22 + (unsigned long long)v23 * 8 + 32)) + 24)), !v24))
                                break;
                            if (v24->field_18 <= v13)
                                goto LABEL_1088710;
                            if (!p || (p->field_6c = (unsigned int)*((int *)&v24[1].padding_0[4 + 4 * v13]), !ptr->field_28 || (p = (struct_11 *)(unsigned long long)sub_14a30c0(ptr->field_28, v13 & 4294967295, g_1ef8198), v25 = ptr->field_30, !v25)))
                                break;
                            v26 = ptr->field_4c - 1;
                            if (*((int *)(v25 + 24)) <= v26)
                                goto LABEL_1088710;
                            if (!*((long long *)(v25 + v26 * 8 + 32)) || (v27 = (struct_20 *)*((long long *)(*((long long *)(v25 + (unsigned long long)v26 * 8 + 32)) + 32)), !v27))
                                break;
                            if (v27->field_18 <= v13)
                                goto LABEL_1088710;
                        } while (...);
                    }
                }
            }
        }
    }
    else
    {
        addr->field_10 = 4294967295;
        if (ptr && ptr->field_b0 && Graphic__get_rectTransform(ptr->field_b0, 0) && (RectTransform__set_anchoredPosition(), ptr->field_b8 && (unsigned long long)Graphic__get_rectTransform(ptr->field_b8, 0)))
        {
            RectTransform__set_anchoredPosition();
            v34 = ptr->field_c0;
            v35 = ptr->field_3c;
            ptr->field_d0 = v34;
            Time__get_time(0);
            v37 = (unsigned int)v34;
            v38 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF((unsigned long long)(v35 + 0x4008000000000000), v37)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned long long)(v35 + 0x4008000000000000), v37) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((unsigned long long)(v35 + 0x4008000000000000), v37)) >> 5 & 3 | (unsigned long long)(CmpF((unsigned long long)(v35 + 0x4008000000000000), v37) & 1)) & ((unsigned long long)(char)(CmpF((unsigned long long)(v35 + 0x4008000000000000), v37)) >> 5 & 3 | (unsigned long long)(unsigned int)(CmpF((unsigned long long)(v35 + 0x4008000000000000), v37) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if ((char)v38)
            {
LABEL_1088230:
                if (ptr->field_b0)
                {
                    Behaviour__set_enabled(ptr->field_b0, 1, 0);
                    if (ptr->field_b8)
                    {
                        flag = 0;
                        Behaviour__set_enabled(ptr->field_b8, 1, 0);
                        v42 = ptr->field_b0;
                        if (v42)
                        {
                            v43 = *(v42)->field_2b0;
                            *(v42)->field_2a8();
                        }
                    }
                }
            }
            else if (ptr->field_80 && (ptr->field_80->field_39 = 0, ptr->field_88))
            {
                ptr->field_88->field_39 = 0;
                Time__get_deltaTime(0);
                ptr9 = ptr->field_80;
                v40 = ptr->field_40 - (unsigned int)v37;
                ptr->field_40 = v40;
                if (ptr9 && (ptr9->field_20 = v40, ptr->field_88))
                {
                    *((unsigned int *)&ptr->field_88->padding_0[32]) = v40;
                    goto LABEL_1088230;
                }
            }
        }
    }
    p = sub_f7db74();
LABEL_1088710:
    sub_f7db7c(p);
}
```


## `WaveManager.<StartWave>d__29.get_Current` — RVA `0xc88714`

- Decompiled symbol: `WaveManager_StartWave_d__29_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long WaveManager_StartWave_d__29_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```


## `WaveManager.<StartWave>d__29.Reset` — RVA `0xc8871c`

- Decompiled symbol: `WaveManager_StartWave_d__29_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05358;

void WaveManager_StartWave_d__29_Reset(void)
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
    sub_f7da4c(v4, sub_f7d940(&g_1f05358));
}
```


## `WaveManager.<StartWave>d__29.get_Current` — RVA `0xc88754`

- Decompiled symbol: `WaveManager_StartWave_d__29_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long WaveManager_StartWave_d__29_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
