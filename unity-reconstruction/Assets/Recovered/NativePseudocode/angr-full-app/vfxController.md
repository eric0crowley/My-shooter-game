# Native pseudocode: vfxController

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `vfxController.Start` — RVA `0xc76308`

- Decompiled symbol: `vfxController_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[88];
    uint128_t field_58;
} struct_0;

struct_0 * vfxController_Start(struct_0 *ptr)
{
    *((uint128_t *)&(&ptr->padding_0)[1]) = 0x1000000030000000000000000;
    return ptr;
}
```

## `vfxController.ChangedStarImage` — RVA `0xc76318`

- Decompiled symbol: `vfxController_ChangedStarImage`
- Metadata signature: `public void ChangedStarImage(int i) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[88];
    unsigned int field_58;
} struct_0;

long long vfxController_ChangedStarImage(struct_0 *ptr, unsigned int a1)
{
    unsigned long long v0;  // x0

    ptr->field_58 = a1;
    v0 = vfxController__PlayStarFX();
    return vfxController__PlayStarFX();
}
```

## `vfxController.PlayStarFX` — RVA `0xc76320`

- Decompiled symbol: `vfxController_PlayStarFX`
- Metadata signature: `public void PlayStarFX() { }`
- Native interval: `508` bytes
- Result: `pseudocode`
- Heuristic layout hint: `vfxController_Recovered` matched 4 offsets against `vfxController` metadata (confidence 1.00).

```c
typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct vfxController_Recovered {
    char padding_0[72];
    struct struct_2 *DesStarFxObjs;
    unsigned long long bgFxPrefabs;
    unsigned int currentStarImage;
    char padding_5c[8];
    unsigned int currentBgFx;
} vfxController_Recovered;

typedef struct struct_2 {
    char padding_0[24];
    int field_18;
} struct_2;

typedef struct struct_4 {
    char padding_0[32];
    long long field_20;
} struct_4;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1f00238;
extern long long g_1f09d48;
extern char g_1fab3a7;
extern char g_85226e;

long long vfxController_PlayStarFX(struct_3 *ptr)
{
    struct_1 *v0;  // x0
    struct_3 *addr;  // x20
    unsigned long v2;  // x0
    struct_2 *p;  // x22
    int v4;  // w8
    int i;  // w23
    struct_4 *v6;  // x8
    long long v7;  // x0
    unsigned long v8;  // x8
    unsigned long long v9;  // x9

    if (!(g_1fab3a7 & 1))
    {
        sub_f7d92c(&g_1f00238);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f09d48);
        sub_f7d92c("'c");
        g_1fab3a7 = 1;
    }
    v0 = GameObject__FindGameObjectsWithTag(g_1f09d48, 0);
    ptr->field_48 = v0;
    addr = &ptr->field_48;
    v2 = sub_f7d8d0(addr, v0);
    p = *((long long *)&addr->padding_0[0]);
    if (p)
    {
        v4 = p->field_18;
        if (p->field_18 >= 1)
        {
            i = 0;
            do
            {
                if (v4 <= i)
                    goto LABEL_1076514;
                v6 = &p->padding_0[8 * i];
                if (!v6->field_20)
                    sub_f7db74();
                v7 = GameObject__get_gameObject(v6->field_20, 0);
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v2 = Object__Destroy(v7, 0);
                v4 = p->field_18;
                i += 1;
            } while (i < v4);
        }
        v8 = ptr->field_64;
        if ((unsigned int)v8)
        {
            v9 = ptr->field_50;
            if (v9)
            {
                if (*((int *)(v9 + 24)) > (unsigned int)v8)
                {
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    v2 = sub_1129f50(*((long long *)(v9 + v8 * 8 + 32)), g_1f00238);
                    goto LABEL_1076454;
                }
                else
                {
LABEL_1076514:
                    sub_f7db7c();
                }
            }
        }
        else
        {
LABEL_1076454:
            if (4 < ptr->field_58)
                return v2;
            goto sub_1076478 + (&g_85226e)[ptr->field_58] * 4;
        }
    }
    sub_f7db74();
}
```

## `vfxController.ChangedStarFX` — RVA `0xc7651c`

- Decompiled symbol: `vfxController_ChangedStarFX`
- Metadata signature: `public void ChangedStarFX(int i) { }`
- Native interval: `8` bytes
- Result: `pseudocode`
- Heuristic layout hint: `vfxController_Recovered` matched 4 offsets against `vfxController` metadata (confidence 1.00).

```c
typedef struct vfxController_Recovered {
    char padding_0[72];
    struct struct_2 *DesStarFxObjs;
    unsigned long long bgFxPrefabs;
    unsigned int currentStarImage;
    char padding_5c[8];
    unsigned int currentBgFx;
} vfxController_Recovered;

typedef struct struct_2 {
    char padding_0[24];
    int field_18;
} struct_2;

long long vfxController_ChangedStarFX(struct_3 *ptr, unsigned int a1)
{
    long long v0;  // x0

    *((unsigned int *)&ptr->padding_5c[0]) = a1;
    v0 = vfxController__PlayStarFX(ptr);
    return vfxController__PlayStarFX(ptr);
}
```

## `vfxController.ChangedLevel` — RVA `0xc76524`

- Decompiled symbol: `vfxController_ChangedLevel`
- Metadata signature: `public void ChangedLevel(int i) { }`
- Native interval: `8` bytes
- Result: `pseudocode`
- Heuristic layout hint: `vfxController_Recovered` matched 4 offsets against `vfxController` metadata (confidence 1.00).

```c
typedef struct vfxController_Recovered {
    char padding_0[72];
    struct struct_2 *DesStarFxObjs;
    unsigned long long bgFxPrefabs;
    unsigned int currentStarImage;
    char padding_5c[8];
    unsigned int currentBgFx;
} vfxController_Recovered;

typedef struct struct_2 {
    char padding_0[24];
    int field_18;
} struct_2;

long long vfxController_ChangedLevel(struct_3 *ptr, unsigned int a1)
{
    long long v0;  // x0

    *((unsigned int *)&ptr->padding_5c[4]) = a1;
    v0 = vfxController__PlayStarFX(ptr);
    return vfxController__PlayStarFX(ptr);
}
```

## `vfxController.ChangedBgFx` — RVA `0xc7652c`

- Decompiled symbol: `vfxController_ChangedBgFx`
- Metadata signature: `public void ChangedBgFx(int i) { }`
- Native interval: `8` bytes
- Result: `pseudocode`
- Heuristic layout hint: `vfxController_Recovered` matched 4 offsets against `vfxController` metadata (confidence 1.00).

```c
typedef struct vfxController_Recovered {
    char padding_0[72];
    struct struct_2 *DesStarFxObjs;
    unsigned long long bgFxPrefabs;
    unsigned int currentStarImage;
    char padding_5c[8];
    unsigned int currentBgFx;
} vfxController_Recovered;

typedef struct struct_2 {
    char padding_0[24];
    int field_18;
} struct_2;

long long vfxController_ChangedBgFx(struct_3 *ptr, unsigned int a1)
{
    long long v0;  // x0

    ptr->field_64 = a1;
    v0 = vfxController__PlayStarFX(ptr);
    return vfxController__PlayStarFX(ptr);
}
```

## `vfxController.ctor` — RVA `0xc76534`

- Decompiled symbol: `vfxController_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long vfxController_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
