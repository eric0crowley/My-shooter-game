# Native pseudocode: bl_MMExampleManager

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_MMExampleManager.get_GetActiveMiniMap` — RVA `0xccaf58`

- Decompiled symbol: `bl_MMExampleManager_get_GetActiveMiniMap`
- Metadata signature: `public bl_MiniMap get_GetActiveMiniMap() { }`
- Native interval: `112` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MMExampleManager_Recovered` matched 2 offsets against `bl_MMExampleManager` metadata (confidence 1.00).

```c
typedef struct bl_MMExampleManager_Recovered {
    char padding_0[32];
    unsigned int MapID;
    char padding_24[4];
    unsigned long long Maps;
} bl_MMExampleManager_Recovered;

extern long long g_1efed78;
extern char g_1fab588;

void bl_MMExampleManager_get_GetActiveMiniMap(struct_0 *ptr)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_0 *v6;  // x0
    struct_0 *v7;  // x0
    struct_0 *v8;  // x0
    unsigned long v9;  // x8
    unsigned long v10;  // x9
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    v6 = ptr;
    if (!(g_1fab588 & 1))
    {
        v7 = sub_f7d92c(&g_1efed78);
        g_1fab588 = 1;
        v6 = v7;
    }
    v8 = v6;
    v9 = ptr->field_28;
    if (v9)
    {
        v10 = ptr->field_20;
        if (*((int *)(v9 + 24)) <= (unsigned int)v10)
            goto LABEL_10cafc4;
        if (*((long long *)(v9 + v10 * 8 + 32)))
        {
            sub_1249488();
            return;
        }
    }
    v8 = sub_f7db74();
LABEL_10cafc4:
    sub_f7db7c(v8);
}
```

## `bl_MMExampleManager.Awake` — RVA `0xccb260`

- Decompiled symbol: `bl_MMExampleManager_Awake`
- Metadata signature: `private void Awake() { }`
- Native interval: `88` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MMExampleManager_Recovered` matched 2 offsets against `bl_MMExampleManager` metadata (confidence 1.00).

```c
typedef struct bl_MMExampleManager_Recovered {
    char padding_0[32];
    unsigned int MapID;
    char padding_24[4];
    struct struct_0 *Maps;
} bl_MMExampleManager_Recovered;

typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
    long long field_20;
} struct_0;

extern long long g_1f0bf10;
extern char g_1fab585;

void bl_MMExampleManager_Awake(struct_1 *p)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    struct_1 *v7;  // x19
    struct_1 *ptr;  // x19
    unsigned long long cur[5];  // x8
    unsigned long long v10;  // x20
    unsigned int v11;  // w9
    unsigned long v12;  // x10
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    struct_1 *v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab585 & 1))
    {
        sub_f7d92c(&g_1f0bf10);
        g_1fab585 = 1;
    }
    p->field_20 = PlayerPrefs__GetInt(g_1f0bf10, 0, 0);
    ptr = v3;
    v3 = ptr;
    cur = p->field_28;
    if (cur)
    {
        ptr = p;
        v10 = 0;
        while (true)
        {
            v11 = cur[3];
            if (v11 > (unsigned int)v10)
                break;
            if (v11 <= (unsigned int)v10)
                goto LABEL_10cb338;
            cur = &cur[v10];
            if (!cur[4] || (GameObject__SetActive(cur[4], 0, 0), cur = (unsigned long long [5])ptr->field_28, v10 += 1, !cur))
                break;
        }
    }
    while (true)
    {
        sub_f7db74();
        v12 = ptr->field_20;
        if (v11 <= (unsigned int)v12)
            break;
        cur = &cur[v12];
        if (cur[4])
        {
            GameObject__SetActive();
            return;
        }
    }
LABEL_10cb338:
    sub_f7db7c();
}
```

## `bl_MMExampleManager.ApplyMap` — RVA `0xccb2b8`

- Decompiled symbol: `bl_MMExampleManager_ApplyMap`
- Metadata signature: `private void ApplyMap() { }`
- Native interval: `132` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x10cb2b8: str x30, [sp, #-0x20]!
// 0x10cb2bc: stp x20, x19, [sp, #0x10]
// 0x10cb2c0: ldr x8, [x0, #0x28]
// 0x10cb2c4: cbz x8, #0x10cb308
// 0x10cb2c8: mov x19, x0
// 0x10cb2cc: mov x20, xzr
// 0x10cb2d0: ldr x9, [x8, #0x18]
// 0x10cb2d4: cmp w20, w9
// 0x10cb2d8: b.ge #0x10cb30c
// 0x10cb2dc: cmp w20, w9
// 0x10cb2e0: b.hs #0x10cb338
// 0x10cb2e4: add x8, x8, x20, lsl #3
// 0x10cb2e8: ldr x0, [x8, #0x20]
// 0x10cb2ec: cbz x0, #0x10cb308
// 0x10cb2f0: mov w1, wzr
// 0x10cb2f4: mov x2, xzr
// 0x10cb2f8: bl #0x1b94cd0
// 0x10cb2fc: ldr x8, [x19, #0x28]
// 0x10cb300: add x20, x20, #1
// 0x10cb304: cbnz x8, #0x10cb2d0
// 0x10cb308: bl #0xf7db74
// 0x10cb30c: ldrsw x10, [x19, #0x20]
// 0x10cb310: cmp w10, w9
// 0x10cb314: b.hs #0x10cb338
// 0x10cb318: add x8, x8, x10, lsl #3
// 0x10cb31c: ldr x0, [x8, #0x20]
// 0x10cb320: cbz x0, #0x10cb308
// 0x10cb324: ldp x20, x19, [sp, #0x10]
// 0x10cb328: mov w1, #1
// 0x10cb32c: mov x2, xzr
// 0x10cb330: ldr x30, [sp], #0x20
// 0x10cb334: b #0x1b94cd0
// 0x10cb338: bl #0xf7db7c
```

## `bl_MMExampleManager.Update` — RVA `0xccb33c`

- Decompiled symbol: `bl_MMExampleManager_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `44` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MMExampleManager_Recovered` matched 3 offsets against `bl_MMExampleManager` metadata (confidence 1.00).

```c
typedef struct bl_MMExampleManager_Recovered {
    char padding_0[32];
    unsigned int MapID;
    char padding_24[4];
    unsigned long long Maps;
    char Rotation;
} bl_MMExampleManager_Recovered;

typedef struct struct_1 {
    char padding_0[32];
    long long field_20;
} struct_1;

typedef struct struct_3 {
    char field_0;
} struct_3;

typedef struct struct_2 {
    char padding_0[184];
    struct struct_3 *field_b8;
} struct_2;

extern struct_2 *g_1ef2b00;
extern long long g_1efed78;
extern char g_1fab559;
extern char g_1fab586;

char [429] bl_MMExampleManager_Update(struct_0 *a0)
{
    unsigned long long v4;  // x30
    char v5[429];  // x0
    char v14[429];  // x0
    char v15;  // x19
    char p[429];  // x20
    struct_0 *v6;  // x0
    unsigned long long v7;  // x22
    unsigned long long v8;  // x21
    unsigned long long v9;  // x20
    struct_0 *ptr;  // x19
    unsigned long long v11;  // x8
    unsigned long v12;  // x9
    struct_1 *v13;  // x8
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x20]
    unsigned long long v2;  // [bp-0x18]
    unsigned long long v3;  // [bp-0x10]

    v3 = v4;
    v5 = Input__GetKeyDown(114, 0);
    if (!((char)v5 & 1))
        return v5;
    v6 = a0;
    v0 = v3;
    v1 = v7;
    v2 = v8;
    v3 = v9;
    ptr = v6;
    if (!(g_1fab586 & 1))
    {
        v6 = sub_f7d92c(&g_1efed78);
        g_1fab586 = 1;
    }
    v11 = ptr->field_28;
    ptr->field_30 = ptr->field_30 ^ 1;
    if (v11)
    {
        v12 = ptr->field_20;
        if (*((int *)(v11 + 24)) <= (unsigned int)v12)
            sub_f7db7c(v6);
        v13 = v11 + v12 * 8;
        if (v13->field_20)
        {
            v14 = sub_1249488(v13->field_20, g_1efed78);
            if (v14)
            {
                v15 = ptr->field_30;
                p = v14;
                if (!(g_1fab559 & 1))
                {
                    v14 = sub_f7d92c(&g_1ef2b00);
                    g_1fab559 = 1;
                }
                if (g_1ef2b00->field_b8->field_0)
                    return v14;
                p[117] = v15;
                p[428] = v15;
                return v14;
            }
        }
    }
    v6 = sub_f7db74();
    sub_f7db7c(v6);
}
```

## `bl_MMExampleManager.ChangeRotation` — RVA `0xccb368`

- Decompiled symbol: `bl_MMExampleManager_ChangeRotation`
- Metadata signature: `private void ChangeRotation() { }`
- Native interval: `212` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: CFGFast did not recover a function at the metadata RVA

```c
// 0x10cb368: str x30, [sp, #-0x30]!
// 0x10cb36c: stp x22, x21, [sp, #0x10]
// 0x10cb370: stp x20, x19, [sp, #0x20]
// 0x10cb374: adrp x20, #0x1fab000
// 0x10cb378: ldrb w8, [x20, #0x586]
// 0x10cb37c: mov x19, x0
// 0x10cb380: tbnz w8, #0, #0x10cb398
// 0x10cb384: adrp x0, #0x1e8e000
// 0x10cb388: ldr x0, [x0, #0xb60]
// 0x10cb38c: bl #0xf7d92c
// 0x10cb390: mov w8, #1
// 0x10cb394: strb w8, [x20, #0x586]
// 0x10cb398: ldrb w9, [x19, #0x30]
// 0x10cb39c: ldr x8, [x19, #0x28]
// 0x10cb3a0: eor w9, w9, #1
// 0x10cb3a4: strb w9, [x19, #0x30]
// 0x10cb3a8: cbz x8, #0x10cb434
// 0x10cb3ac: ldrsw x9, [x19, #0x20]
// 0x10cb3b0: ldr w10, [x8, #0x18]
// 0x10cb3b4: cmp w9, w10
// 0x10cb3b8: b.hs #0x10cb438
// 0x10cb3bc: add x8, x8, x9, lsl #3
// 0x10cb3c0: ldr x0, [x8, #0x20]
// 0x10cb3c4: cbz x0, #0x10cb434
// 0x10cb3c8: adrp x8, #0x1e8e000
// 0x10cb3cc: ldr x8, [x8, #0xb60]
// 0x10cb3d0: ldr x1, [x8]
// 0x10cb3d4: bl #0x1249488
// 0x10cb3d8: cbz x0, #0x10cb434
// 0x10cb3dc: adrp x21, #0x1fab000
// 0x10cb3e0: adrp x22, #0x1e8e000
// 0x10cb3e4: ldrb w8, [x21, #0x559]
// 0x10cb3e8: ldrb w19, [x19, #0x30]
// 0x10cb3ec: ldr x22, [x22, #0xa08]
// 0x10cb3f0: mov x20, x0
// 0x10cb3f4: tbnz w8, #0, #0x10cb40c
// 0x10cb3f8: adrp x0, #0x1e8e000
// 0x10cb3fc: ldr x0, [x0, #0xa08]
// 0x10cb400: bl #0xf7d92c
// 0x10cb404: mov w8, #1
// 0x10cb408: strb w8, [x21, #0x559]
// 0x10cb40c: ldr x8, [x22]
// 0x10cb410: ldr x8, [x8, #0xb8]
// 0x10cb414: ldrb w8, [x8]
// 0x10cb418: cbnz w8, #0x10cb424
// 0x10cb41c: strb w19, [x20, #0x75]
// 0x10cb420: strb w19, [x20, #0x1ac]
// 0x10cb424: ldp x20, x19, [sp, #0x20]
// 0x10cb428: ldp x22, x21, [sp, #0x10]
// 0x10cb42c: ldr x30, [sp], #0x30
// 0x10cb430: ret
// 0x10cb434: bl #0xf7db74
// 0x10cb438: bl #0xf7db7c
```

## `bl_MMExampleManager.ChangeMap` — RVA `0xccb43c`

- Decompiled symbol: `bl_MMExampleManager_ChangeMap`
- Metadata signature: `public void ChangeMap(int i) { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eee870;
extern long long g_1f0bf10;
extern char g_1fab587;

void bl_MMExampleManager_ChangeMap(unsigned long a0, unsigned int a1)
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
    if (!(g_1fab587 & 1))
    {
        sub_f7d92c(&g_1eee870);
        sub_f7d92c(&g_1f0bf10);
        g_1fab587 = 1;
    }
    PlayerPrefs__SetInt(g_1f0bf10, a1, 0);
    if (!g_1eee870->field_e0)
        sub_f7da5c(g_1eee870);
    Application__get_loadedLevel(0);
    Application__LoadLevel();
    return;
}
```

## `bl_MMExampleManager.ctor` — RVA `0xccb4c4`

- Decompiled symbol: `bl_MMExampleManager_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `24` bytes
- Result: `pseudocode`
- Heuristic layout hint: `bl_MMExampleManager_Recovered` matched 2 offsets against `bl_MMExampleManager` metadata (confidence 1.00).

```c
typedef struct bl_MMExampleManager_Recovered {
    char padding_0[32];
    unsigned int MapID;
    char padding_24[12];
    char Rotation;
} bl_MMExampleManager_Recovered;

long long bl_MMExampleManager_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_20 = 2;
    ptr->field_30 = 1;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
