# Native pseudocode: SuperTouchZone.EmulatedFingerSystem

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SuperTouchZone.EmulatedFingerSystem.ctor` — RVA `0xc4d108`

- Decompiled symbol: `SuperTouchZone_EmulatedFingerSystem_ctor`
- Metadata signature: `public void .ctor(SuperTouchZone zone) { }`
- Native interval: `308` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_EmulatedFingerSystem_Recovered` matched 2 offsets against `SuperTouchZone.EmulatedFingerSystem` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_EmulatedFingerSystem_Recovered {
    char padding_0[16];
    struct struct_1 *fingers;
    long long zone;
} SuperTouchZone_EmulatedFingerSystem_Recovered;

typedef struct struct_4 {
    struct struct_3 *field_0;
    char padding_8[16];
    unsigned int field_18;
} struct_4;

typedef struct struct_1 {
    struct struct_0 *field_0;
    char padding_8[16];
    unsigned int field_18;
} struct_1;

typedef struct struct_5 {
    char padding_0[80];
    long long field_50;
} struct_5;

typedef struct struct_3 {
    char padding_0[64];
    unsigned long long field_40;
} struct_3;

typedef struct struct_0 {
    char padding_0[64];
    long long field_40;
} struct_0;

extern long long g_1eee570;
extern long long g_1ef3ac0;
extern char g_1fab244;

long long SuperTouchZone_EmulatedFingerSystem_ctor(struct_2 *p, long long a1)
{
    struct_4 *v0;  // x0
    struct_2 *ptr;  // x20
    unsigned long v2;  // x0
    struct_1 *i;  // x24
    unsigned long v4;  // x22
    unsigned long long v5;  // x25
    struct_5 *v6;  // x21
    struct_5 *addr;  // x0
    unsigned long v9;  // x0

    if (!(g_1fab244 & 1))
    {
        sub_f7d92c(&g_1eee570);
        sub_f7d92c(&g_1ef3ac0);
        g_1fab244 = 1;
    }
    Object__ctor(p, 0);
    p->field_18 = a1;
    sub_f7d8d0((struct SuperTouchZone_EmulatedFingerSystem_Recovered *)&p->field_18, a1);
    v0 = sub_f7d9d4(g_1eee570, 3);
    p->field_10 = v0;
    ptr = &p->field_10;
    v2 = sub_f7d8d0(ptr, v0);
    i = *((long long *)&ptr->padding_0[0]);
    if (i)
    {
        v4 = 0;
        v5 = 32;
        do
        {
            if (i->field_18 <= v4)
                return v2;
            v6 = sub_f7db70(g_1ef3ac0);
            TouchObject__ctor(v6);
            addr = v6;
            addr->field_50 = a1;
            sub_f7d8d0((struct struct_5 *)&addr->field_50, a1);
            if (!sub_f7da60(addr, i->field_0->field_40))
            {
                sub_f7da4c(sub_f7db98(), 0);
                sub_f7db7c();
            }
            if (i->field_18 <= v4)
                sub_f7db7c();
            *((struct_5 **)((char *)&(&i[1].field_0)[v4] + 4)) = addr;
            v2 = sub_f7d8d0((struct struct_1 *)((char *)i + v5), addr);
            i = *((long long *)&ptr->padding_0[0]);
            v4 += 1;
            v5 += 8;
        } while (i);
    }
    v9 = sub_f7db74();
    return sub_f7db74();
}
```

## `SuperTouchZone.EmulatedFingerSystem.EndMouseAndTouches` — RVA `0xc4d23c`

- Decompiled symbol: `SuperTouchZone_EmulatedFingerSystem_EndMouseAndTouches`
- Metadata signature: `public void EndMouseAndTouches(bool cancel) { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
long long SuperTouchZone_EmulatedFingerSystem_EndMouseAndTouches(long long *ptr, unsigned int a1)
{
    unsigned long long v0;  // x0

    if (ptr[4])
    {
        TouchObject__ReleaseControl(ptr[4], ptr[3], a1 & 1);
        ptr[4] = 0;
        sub_f7d8d0(ptr + 4, 0);
    }
    v0 = SuperTouchZone_EmulatedFingerSystem__EndTouches(ptr, a1 & 1);
    return SuperTouchZone_EmulatedFingerSystem__EndTouches(ptr, a1 & 1);
}
```

## `SuperTouchZone.EmulatedFingerSystem.EndTouches` — RVA `0xc4d354`

- Decompiled symbol: `SuperTouchZone_EmulatedFingerSystem_EndTouches`
- Metadata signature: `public void EndTouches(bool cancel) { }`
- Native interval: `104` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_EmulatedFingerSystem_Recovered` matched 2 offsets against `SuperTouchZone.EmulatedFingerSystem` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_EmulatedFingerSystem_Recovered {
    char padding_0[16];
    struct struct_0 *fingers;
    char padding_18[24];
    unsigned int curFingerNum;
} SuperTouchZone_EmulatedFingerSystem_Recovered;

typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

struct_1 * SuperTouchZone_EmulatedFingerSystem_EndTouches(struct_1 *ptr, unsigned long a1)
{
    struct_2 *v0;  // x8
    unsigned long long v1;  // x21
    struct_1 *v2;  // x0
    struct_1 *v3;  // x0
    struct_1 *v4;  // x0
    unsigned long v5;  // x0

    v0 = ptr->field_10;
    ptr->field_30 = 0;
    if (v0)
    {
        v1 = 0;
        v2 = ptr;
        do
        {
            v3 = v2;
            if (v0->field_18 <= (unsigned int)v1)
                return v3;
            if (v0->field_18 <= (unsigned int)v1)
                sub_f7db7c();
        } while (*((long long *)&v0[1].padding_0[4 + 8 * v1]) && (v4 = (struct_1 *)(unsigned long long)TouchObject__End(), v0 = (struct_2 *)ptr->field_10, v1 += 1, v2 = (struct_1 *)(unsigned long long)TouchObject__End(), v0));
    }
    v5 = sub_f7db74();
    return sub_f7db74();
}
```

## `SuperTouchZone.EmulatedFingerSystem.OnSystemTouchStart` — RVA `0xc4d4d0`

- Decompiled symbol: `SuperTouchZone_EmulatedFingerSystem_OnSystemTouchStart`
- Metadata signature: `public bool OnSystemTouchStart(TouchObject touchObj, TouchControl sender, TouchControl.TouchStartType touchStartType) { }`
- Native interval: `532` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_EmulatedFingerSystem_Recovered` matched 5 offsets against `SuperTouchZone.EmulatedFingerSystem` metadata (confidence 1.00).

```c
typedef struct SuperTouchZone_EmulatedFingerSystem_Recovered {
    char padding_0[24];
    struct struct_5 *zone;
    struct struct_3 *mouseTouchObj;
    unsigned long long lastMousePos;
    char padding_30[12];
    unsigned int twistCur;
    unsigned int pinchDistCur;
} SuperTouchZone_EmulatedFingerSystem_Recovered;

typedef struct struct_3 {
    struct struct_2 *field_0;
    char padding_8[24];
    unsigned long long field_20;
    char padding_28[40];
    unsigned long long field_50;
} struct_3;

typedef struct struct_7 {
    struct struct_6 *field_0;
    char padding_8[24];
    unsigned long long field_20;
    char padding_28[40];
    long long field_50;
} struct_7;

typedef struct struct_5 {
    char padding_0[440];
    unsigned int field_1b8;
    unsigned int field_1bc;
    unsigned int field_1c0;
    unsigned int field_1c4;
} struct_5;

typedef struct struct_2 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_2;

typedef struct struct_6 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_6;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[304];
    char field_130;
} struct_0;

extern struct_1 *g_1ef0c58;
extern struct_0 *g_1ef3ac0;
extern char g_1fab245;

unsigned int SuperTouchZone_EmulatedFingerSystem_OnSystemTouchStart(struct_4 *ptr, struct_7 *p, long long a2)
{
    unsigned long v0;  // x10
    struct_3 *v1;  // x0
    unsigned long v2;  // 4115
    unsigned long long v3;  // x8
    unsigned int v4;  // w22
    unsigned int v5;  // w0
    unsigned int v6;  // w8

    if (!(g_1fab245 & 1))
    {
        sub_f7d92c(&g_1ef3ac0);
        sub_f7d92c(&g_1ef0c58);
        g_1fab245 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(a2, 0, 0) & 1))
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Inequality(a2, ptr->field_18, 0) & 1))
            return 0;
    }
    if (ptr->field_20)
        return 0;
    if (p)
    {
        v0 = g_1ef3ac0->field_130;
        if (p->field_0->field_130 >= (unsigned int)v0 && *((long long *)(p->field_0->field_c8 + v0 * 8 - 8)) == g_1ef3ac0)
        {
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (((char)Object__op_Equality(p->field_50, ptr->field_18, 0) & 1))
                return 0;
        }
    }
    SuperTouchZone_EmulatedFingerSystem__EndTouches(ptr, 0);
    ptr->field_20 = p;
    sub_f7d8d0((struct SuperTouchZone_EmulatedFingerSystem_Recovered *)&ptr->field_20, p);
    v1 = ptr->field_20;
    if (ptr->field_20 && (v1 = (struct_3 *)TouchObject__AddControl(), ptr->field_18))
    {
        v1 = Input__GetKey(ptr->field_18->field_1b8, 0);
        if (((char)v1 & 1))
        {
LABEL_104d654:
            if (p)
            {
LABEL_104d65c:
                v3 = p->field_20;
                ptr->field_3c = 0;
                ptr->field_28 = v3;
                v4 = Screen__get_width(0);
                v5 = Screen__get_height(0);
                if (v4 < v5)
                    v6 = v4;
                else
                    v6 = v5;
                ptr->field_40 = v6 * 0x3e800000;
                SuperTouchZone_EmulatedFingerSystem__StartTouches();
                return 1;
            }
        }
        else if (ptr->field_18)
        {
            v1 = Input__GetKey(ptr->field_18->field_1bc, 0);
            if ((v1 & 1))
                goto LABEL_104d654;
            if (ptr->field_18)
            {
                v1 = Input__GetKey(ptr->field_18->field_1c0, 0);
                if ((v1 & 1))
                    goto LABEL_104d654;
                if (ptr->field_18)
                {
                    v1 = Input__GetKey(ptr->field_18->field_1c4, 0);
                    v2 = arm64g_calculate_condition(25, (unsigned long long)((unsigned int)v1 & 1), 0, 0);
                    if (p)
                        goto LABEL_104d65c;
                }
            }
        }
    }
    sub_f7db74(v1);
}
```

## `SuperTouchZone.EmulatedFingerSystem.StartTouches` — RVA `0xc4d810`

- Decompiled symbol: `SuperTouchZone_EmulatedFingerSystem_StartTouches`
- Metadata signature: `public void StartTouches(int num, Vector2 center, bool isMouse) { }`
- Native interval: `272` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_EmulatedFingerSystem_Recovered` matched 2 offsets against `SuperTouchZone.EmulatedFingerSystem` metadata (confidence 1.00).

```c
typedef struct struct_4 {
    char padding_0[16];
    struct SuperTouchZone_EmulatedFingerSystem_Recovered *field_10;
    struct struct_5 *field_18;
    char padding_20[16];
    int field_30;
    unsigned int field_34;
    unsigned int field_38;
} struct_4;

typedef struct SuperTouchZone_EmulatedFingerSystem_Recovered {
    char padding_0[24];
    int zone;
    char padding_1c[4];
    struct struct_1 *mouseTouchObj;
} SuperTouchZone_EmulatedFingerSystem_Recovered;

typedef struct struct_2 {
    char padding_0[696];
    struct struct_3 *field_2b8;
    unsigned long long field_2c0;
} struct_2;

typedef struct struct_5 {
    struct struct_2 *field_0;
} struct_5;

typedef struct struct_1 {
    char padding_0[72];
    unsigned int field_48;
    unsigned int field_4c;
} struct_1;

typedef struct struct_3 {
    unsigned long long field_0;
} struct_3;

long long SuperTouchZone_EmulatedFingerSystem_StartTouches(struct_4 *ptr, int a1, unsigned int a2)
{
    unsigned long v0;  // x0
    struct_0 *p;  // x8
    unsigned long long flag;  // x2
    unsigned long long choice;  // x3
    unsigned long long v12;  // x4
    unsigned long v13;  // x0
    int v2;  // w9
    unsigned int v3;  // s0
    unsigned int v4;  // s1
    int v5;  // w23
    unsigned int addr[20];  // x22
    struct_2 **v8;  // x0
    unsigned int v9[20];  // x1

    v0 = SuperTouchZone_EmulatedFingerSystem__EndTouches(ptr, 0);
    p = ptr->field_10;
    if (p)
    {
        v2 = p->field_18;
        ptr->field_34 = v3;
        ptr->field_38 = v4;
        if (v2 < a1)
            v5 = v2;
        else
            v5 = a1;
        ptr->field_30 = v5;
        if (v5 < 1)
        {
            return v0;
        }
        else if (p->field_18 > 0)
        {
            addr = p->field_20;
            SuperTouchZone_EmulatedFingerSystem__GetFingerPos(ptr, 0);
            if (addr)
            {
                addr[18] = v3;
                addr[19] = v4;
                if (ptr->field_18)
                {
                    TouchObject__Start(addr, TouchControl__GetCamera(ptr->field_18), a2 & 1, 0);
                    v8 = ptr->field_18;
                    if (v8)
                    {
                        v9 = addr;
                        flag = 0;
                        choice = 0;
                        v12 = *(v8)->field_2c0;
                        *(v8)->field_2b8();
                    }
                }
            }
        }
        else
        {
            sub_f7db7c();
        }
    }
    v13 = sub_f7db74();
    return sub_f7db74();
}
```

## `SuperTouchZone.EmulatedFingerSystem.OnSystemTouchEnd` — RVA `0xc4d920`

- Decompiled symbol: `SuperTouchZone_EmulatedFingerSystem_OnSystemTouchEnd`
- Metadata signature: `public bool OnSystemTouchEnd(TouchObject touchObj, TouchControl.TouchEndType touchEndType) { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

unsigned int SuperTouchZone_EmulatedFingerSystem_OnSystemTouchEnd(struct_0 *ptr, unsigned long long a1, unsigned int a2)
{
    unsigned int v0;  // w9
    unsigned int v1;  // w8
    unsigned long long v2;  // x1

    if (!ptr->field_20)
        v0 = 0;
    else
        v0 = 1;
    if (ptr->field_20 != a1)
        v1 = 0;
    else
        v1 = 1;
    if ((v0 & v1) == 1)
    {
        ptr->field_20 = 0;
        sub_f7d8d0((struct struct_0 *)&ptr->field_20, 0);
        if (!a2)
            v2 = 0;
        else
            v2 = 1;
        SuperTouchZone_EmulatedFingerSystem__EndTouches(ptr, v2);
    }
    return v0 & v1;
}
```

## `SuperTouchZone.EmulatedFingerSystem.OnSystemTouchMove` — RVA `0xc4d97c`

- Decompiled symbol: `SuperTouchZone_EmulatedFingerSystem_OnSystemTouchMove`
- Metadata signature: `public bool OnSystemTouchMove(TouchObject touchObj) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

unsigned long long SuperTouchZone_EmulatedFingerSystem_OnSystemTouchMove(struct_0 *a0, unsigned long long a1)
{
    if (!a0->field_20)
    {
        return 0;
    }
    else if (a0->field_20 != a1)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `SuperTouchZone.EmulatedFingerSystem.GetFingerPos` — RVA `0xc4d998`

- Decompiled symbol: `SuperTouchZone_EmulatedFingerSystem_GetFingerPos`
- Metadata signature: `private Vector2 GetFingerPos(int fingerId) { }`
- Native interval: `144` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    int field_30;
} struct_0;

struct_0 * SuperTouchZone_EmulatedFingerSystem_GetFingerPos(struct_0 *a0, unsigned long a1)
{
    unsigned long long v2;  // x0
    char v0;  // [bp-0x28]
    char v1;  // [bp-0x24]

    if (a0->field_30 <= 1)
        return a0;
    v2 = sincosf(&v1, &v0);
    return sincosf(&v1, &v0);
}
```

## `SuperTouchZone.EmulatedFingerSystem.Update` — RVA `0xc4dbac`

- Decompiled symbol: `SuperTouchZone_EmulatedFingerSystem_Update`
- Metadata signature: `public void Update() { }`
- Native interval: `1444` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x104dbac: sub sp, sp, #0x90
// 0x104dbb0: str d12, [sp, #0x30]
// 0x104dbb4: stp d11, d10, [sp, #0x38]
// 0x104dbb8: stp d9, d8, [sp, #0x48]
// 0x104dbbc: str x30, [sp, #0x58]
// 0x104dbc0: stp x24, x23, [sp, #0x60]
// 0x104dbc4: stp x22, x21, [sp, #0x70]
// 0x104dbc8: stp x20, x19, [sp, #0x80]
// 0x104dbcc: mov x19, x0
// 0x104dbd0: mov x0, xzr
// 0x104dbd4: bl #0x1b77c10
// 0x104dbd8: mov w20, w0
// 0x104dbdc: mov x0, xzr
// 0x104dbe0: bl #0x1b77c38
// 0x104dbe4: ldr x8, [x19, #0x20]
// 0x104dbe8: cmp w20, w0
// 0x104dbec: csel w9, w20, w0, lt
// 0x104dbf0: scvtf s8, w9
// 0x104dbf4: adrp x24, #0x832000
// 0x104dbf8: adrp x23, #0x832000
// 0x104dbfc: cbz x8, #0x104dc74
// 0x104dc00: ldr d9, [x8, #0x20]
// 0x104dc04: ldr x9, [x8, #0x20]
// 0x104dc08: ldr x8, [x19, #0x18]
// 0x104dc0c: ldr d10, [x19, #0x28]
// 0x104dc10: str x9, [x19, #0x28]
// 0x104dc14: cbz x8, #0x104e0b8
// 0x104dc18: ldr w0, [x8, #0x1bc]
// 0x104dc1c: mov x1, xzr
// 0x104dc20: bl #0x1bc76bc
// 0x104dc24: ldr x8, [x19, #0x18]
// 0x104dc28: cbz x8, #0x104e0b8
// 0x104dc2c: mov w20, w0
// 0x104dc30: ldr w0, [x8, #0x1c0]
// 0x104dc34: mov x1, xzr
// 0x104dc38: bl #0x1bc76bc
// 0x104dc3c: ldr x8, [x19, #0x18]
// 0x104dc40: cbz x8, #0x104e0b8
// 0x104dc44: ldr w9, [x8, #0x1c8]
// 0x104dc48: ldr w10, [x8, #0x1cc]
// 0x104dc4c: ldr w8, [x8, #0x1b8]
// 0x104dc50: mov x1, xzr
// 0x104dc54: cmp w9, w10
// 0x104dc58: cset w9, ne
// 0x104dc5c: and w21, w0, w9
// 0x104dc60: mov w0, w8
// 0x104dc64: bl #0x1bc76bc
// 0x104dc68: tbz w0, #0, #0x104dde4
// 0x104dc6c: mov w8, wzr
// 0x104dc70: b #0x104de04
// 0x104dc74: ldr x8, [x19, #0x18]
// 0x104dc78: cbz x8, #0x104e0b8
// 0x104dc7c: ldr w0, [x8, #0x19c]
// 0x104dc80: mov x1, xzr
// 0x104dc84: bl #0x1bc76bc
// 0x104dc88: ldr x8, [x19, #0x18]
// 0x104dc8c: cbz x8, #0x104e0b8
// 0x104dc90: mov w20, w0
// 0x104dc94: ldr w0, [x8, #0x1a4]
// 0x104dc98: mov x1, xzr
// 0x104dc9c: bl #0x1bc76bc
// 0x104dca0: ldr x8, [x19, #0x18]
// 0x104dca4: cbz x8, #0x104e0b8
// 0x104dca8: mov w21, w0
// 0x104dcac: ldr w0, [x8, #0x198]
// 0x104dcb0: mov x1, xzr
// 0x104dcb4: bl #0x1bc76bc
// 0x104dcb8: ldr x8, [x19, #0x18]
// 0x104dcbc: cbz x8, #0x104e0b8
// 0x104dcc0: and w9, w20, #1
// 0x104dcc4: and w20, w0, #1
// 0x104dcc8: ldr w0, [x8, #0x1a0]
// 0x104dccc: and w8, w21, #1
// 0x104dcd0: sub w8, w9, w8
// 0x104dcd4: mov x1, xzr
// 0x104dcd8: scvtf s9, w8
// 0x104dcdc: bl #0x1bc76bc
// 0x104dce0: and w8, w0, #1
// 0x104dce4: sub w8, w20, w8
// 0x104dce8: scvtf s0, w8
// 0x104dcec: stp s0, s9, [sp, #0x24]
// 0x104dcf0: ldr x8, [x19, #0x18]
// 0x104dcf4: cbz x8, #0x104e0b8
// 0x104dcf8: ldr w0, [x8, #0x1b0]
// 0x104dcfc: mov x1, xzr
// 0x104dd00: bl #0x1bc76bc
// 0x104dd04: ldr x8, [x19, #0x18]
// 0x104dd08: cbz x8, #0x104e0b8
// 0x104dd0c: mov w20, w0
// 0x104dd10: ldr w0, [x8, #0x1b4]
// 0x104dd14: mov x1, xzr
// 0x104dd18: bl #0x1bc76bc
// 0x104dd1c: ldr x8, [x19, #0x18]
// 0x104dd20: cbz x8, #0x104e0b8
// 0x104dd24: mov w22, w0
// 0x104dd28: ldr w0, [x8, #0x1ac]
// 0x104dd2c: mov x1, xzr
// 0x104dd30: bl #0x1bc76bc
// 0x104dd34: ldr x8, [x19, #0x18]
// 0x104dd38: cbz x8, #0x104e0b8
// 0x104dd3c: mov w21, w0
// 0x104dd40: ldr w0, [x8, #0x1a8]
// 0x104dd44: and w9, w22, #1
// 0x104dd48: and w8, w20, #1
// 0x104dd4c: sub w8, w9, w8
// 0x104dd50: mov x1, xzr
// 0x104dd54: scvtf s10, w8
// 0x104dd58: bl #0x1bc76bc
// 0x104dd5c: ldp s3, s2, [sp, #0x24]
// 0x104dd60: ldr w8, [x19, #0x30]
// 0x104dd64: and w9, w0, #1
// 0x104dd68: and w10, w21, #1
// 0x104dd6c: sub w9, w9, w10
// 0x104dd70: fmul s0, s2, s2
// 0x104dd74: fmul s1, s3, s3
// 0x104dd78: scvtf s9, w9
// 0x104dd7c: fadd s0, s0, s1
// 0x104dd80: cbz w8, #0x104dea4
// 0x104dd84: adrp x9, #0x832000
// 0x104dd88: ldr s1, [x9, #0x534]
// 0x104dd8c: str q2, [sp, #0x10]
// 0x104dd90: fabs s2, s9
// 0x104dd94: str q3, [sp]
// 0x104dd98: fcmp s2, s1
// 0x104dd9c: b.pl #0x104df6c
// 0x104dda0: adrp x9, #0x832000
// 0x104dda4: ldr s1, [x9, #0x2e8]
// 0x104dda8: fabs s2, s10
// 0x104ddac: fcmp s2, s1
// 0x104ddb0: b.pl #0x104df6c
// 0x104ddb4: fcmp s0, s1
// 0x104ddb8: b.pl #0x104df6c
// 0x104ddbc: cmp w8, #1
// 0x104ddc0: b.eq #0x104df44
// 0x104ddc4: cmp w8, #2
// 0x104ddc8: b.eq #0x104df54
// 0x104ddcc: cmp w8, #3
// 0x104ddd0: b.ne #0x104e00c
// 0x104ddd4: ldr x8, [x19, #0x18]
// 0x104ddd8: cbz x8, #0x104e0b8
// 0x104dddc: ldr w0, [x8, #0x194]
// 0x104dde0: b #0x104df60
// 0x104dde4: ldr x8, [x19, #0x18]
// 0x104dde8: cbz x8, #0x104e0b8
// 0x104ddec: ldr w0, [x8, #0x1c4]
// 0x104ddf0: mov x1, xzr
// 0x104ddf4: bl #0x1bc76bc
// 0x104ddf8: orr w8, w20, w21
// 0x104ddfc: eor w9, w0, #1
// 0x104de00: and w8, w8, w9
// 0x104de04: fsub v0.2s, v9.2s, v10.2s
// 0x104de08: tbz w20, #0, #0x104de5c
// 0x104de0c: ldr x9, [x19, #0x18]
// 0x104de10: cbz x9, #0x104e0b8
// 0x104de14: ldr w10, [x9, #0x1cc]
// 0x104de18: ldr s1, [x19, #0x3c]
// 0x104de1c: cbz w10, #0x104de30
// 0x104de20: cmp w10, #1
// 0x104de24: b.ne #0x104e108
// 0x104de28: mov s2, v0.s[1]
// 0x104de2c: b #0x104de34
// 0x104de30: mov v2.16b, v0.16b
// 0x104de34: ldr s3, [x9, #0x1dc]
// 0x104de38: fmov s4, #30.00000000
// 0x104de3c: mov w9, #0x42b40000
// 0x104de40: fmul s3, s3, s8
// 0x104de44: fmax s3, s3, s4
// 0x104de48: fmov s4, w9
// 0x104de4c: fdiv s3, s4, s3
// 0x104de50: fmul s2, s2, s3
// 0x104de54: fadd s1, s1, s2
// 0x104de58: str s1, [x19, #0x3c]
// 0x104de5c: cbz w21, #0x104de90
// 0x104de60: ldr x9, [x19, #0x18]
// 0x104de64: cbz x9, #0x104e0b8
// 0x104de68: ldr w9, [x9, #0x1c8]
// 0x104de6c: ldr s1, [x19, #0x40]
// 0x104de70: cbz w9, #0x104de84
// 0x104de74: cmp w9, #1
// 0x104de78: b.ne #0x104e108
// 0x104de7c: mov s2, v0.s[1]
// 0x104de80: b #0x104de88
// 0x104de84: mov v2.16b, v0.16b
// 0x104de88: fadd s1, s1, s2
// 0x104de8c: str s1, [x19, #0x40]
// 0x104de90: tbnz w8, #0, #0x104e018
// 0x104de94: ldur d1, [x19, #0x34]
// 0x104de98: fadd v0.2s, v0.2s, v1.2s
// 0x104de9c: stur d0, [x19, #0x34]
// 0x104dea0: b #0x104e018
// 0x104dea4: adrp x8, #0x832000
// 0x104dea8: ldr s11, [x8, #0x2e8]
// 0x104deac: fcmp s0, s11
// 0x104deb0: b.gt #0x104decc
// 0x104deb4: ldr x8, [x19, #0x18]
// 0x104deb8: cbz x8, #0x104e0b8
// 0x104debc: ldr w0, [x8, #0x18c]
// 0x104dec0: mov x1, xzr
// 0x104dec4: bl #0x1bc76bc
// 0x104dec8: tbz w0, #0, #0x104df00
// 0x104decc: mov w20, #1
// 0x104ded0: ldr x21, [x19, #0x18]
// 0x104ded4: cbz x21, #0x104e0b8
// 0x104ded8: mov x0, x21
// 0x104dedc: bl #0x104da28
// 0x104dee0: mov x1, x0
// 0x104dee4: mov x0, x21
// 0x104dee8: bl #0x104e150
// 0x104deec: mov x0, x19
// 0x104def0: mov w1, w20
// 0x104def4: mov w2, wzr
// 0x104def8: bl #0x104d810
// 0x104defc: b #0x104e018
// 0x104df00: fabs s0, s10
// 0x104df04: fcmp s0, s11
// 0x104df08: mov w20, #2
// 0x104df0c: b.gt #0x104ded0
// 0x104df10: adrp x8, #0x832000
// 0x104df14: ldr s0, [x8, #0x534]
// 0x104df18: fabs s1, s9
// 0x104df1c: fcmp s1, s0
// 0x104df20: b.gt #0x104ded0
// 0x104df24: ldr x8, [x19, #0x18]
// 0x104df28: cbz x8, #0x104e0b8
// 0x104df2c: ldr w0, [x8, #0x190]
// 0x104df30: mov x1, xzr
// 0x104df34: bl #0x1bc76bc
// 0x104df38: tbz w0, #0, #0x104e0e0
// 0x104df3c: mov w20, #2
// 0x104df40: b #0x104ded0
// 0x104df44: ldr x8, [x19, #0x18]
// 0x104df48: cbz x8, #0x104e0b8
// 0x104df4c: ldr w0, [x8, #0x18c]
// 0x104df50: b #0x104df60
// 0x104df54: ldr x8, [x19, #0x18]
// 0x104df58: cbz x8, #0x104e0b8
// 0x104df5c: ldr w0, [x8, #0x190]
// 0x104df60: mov x1, xzr
// 0x104df64: bl #0x1bc76bc
// 0x104df68: tbz w0, #0, #0x104e00c
// 0x104df6c: ldr x8, [x19, #0x18]
// 0x104df70: cbz x8, #0x104e0b8
// 0x104df74: ldur d11, [x19, #0x34]
// 0x104df78: ldr s12, [x8, #0x1d0]
// 0x104df7c: bl #0x104e208
// 0x104df80: fmul s1, s12, s8
// 0x104df84: fmul s0, s1, s0
// 0x104df88: ldp q2, q1, [sp]
// 0x104df8c: ldr x8, [x19, #0x18]
// 0x104df90: mov v1.s[1], v2.s[0]
// 0x104df94: fmul v0.2s, v1.2s, v0.s[0]
// 0x104df98: fadd v0.2s, v11.2s, v0.2s
// 0x104df9c: stur d0, [x19, #0x34]
// 0x104dfa0: cbz x8, #0x104e0b8
// 0x104dfa4: ldr s11, [x19, #0x40]
// 0x104dfa8: ldr s12, [x8, #0x1d4]
// 0x104dfac: bl #0x104e208
// 0x104dfb0: ldr s2, [x24, #0x3b8]
// 0x104dfb4: ldr s3, [x23, #0x3bc]
// 0x104dfb8: fmul s1, s12, s8
// 0x104dfbc: fmul s0, s1, s0
// 0x104dfc0: fmul s0, s0, s10
// 0x104dfc4: ldr x8, [x19, #0x18]
// 0x104dfc8: fadd s0, s11, s0
// 0x104dfcc: fmul s1, s8, s2
// 0x104dfd0: fmul s2, s8, s3
// 0x104dfd4: fcmp s0, s2
// 0x104dfd8: fcsel s2, s2, s0, gt
// 0x104dfdc: fcmp s0, s1
// 0x104dfe0: fcsel s0, s2, s1, pl
// 0x104dfe4: str s0, [x19, #0x40]
// 0x104dfe8: cbz x8, #0x104e0b8
// 0x104dfec: ldr s10, [x19, #0x3c]
// 0x104dff0: ldr s11, [x8, #0x1d8]
// 0x104dff4: bl #0x104e208
// 0x104dff8: fmul s1, s11, s9
// 0x104dffc: fmul s0, s1, s0
// 0x104e000: fadd s0, s10, s0
// 0x104e004: str s0, [x19, #0x3c]
// 0x104e008: b #0x104e018
// 0x104e00c: mov x0, x19
// 0x104e010: mov w1, wzr
// 0x104e014: bl #0x104d354
// 0x104e018: ldr s1, [x23, #0x3bc]
// 0x104e01c: ldr s0, [x24, #0x3b8]
// 0x104e020: ldr s2, [x19, #0x40]
// 0x104e024: ldr x8, [x19, #0x10]
// 0x104e028: fmul s1, s8, s1
// 0x104e02c: fmul s0, s8, s0
// 0x104e030: fcmp s2, s1
// 0x104e034: fcsel s1, s1, s2, gt
// 0x104e038: fcmp s2, s0
// 0x104e03c: fcsel s0, s1, s0, pl
// 0x104e040: str s0, [x19, #0x40]
// 0x104e044: cbz x8, #0x104e0b8
// 0x104e048: mov x20, xzr
// 0x104e04c: ldr w9, [x8, #0x18]
// 0x104e050: cmp w20, w9
// 0x104e054: b.ge #0x104e0bc
// 0x104e058: cmp w20, w9
// 0x104e05c: b.hs #0x104e104
// 0x104e060: add x8, x8, x20, lsl #3
// 0x104e064: ldr x21, [x8, #0x20]
// 0x104e068: mov x0, x19
// 0x104e06c: mov w1, w20
// 0x104e070: bl #0x104d998
// 0x104e074: cbz x21, #0x104e0b8
// 0x104e078: ldrb w8, [x21, #0x10]
// 0x104e07c: mov v8.16b, v0.16b
// 0x104e080: mov v9.16b, v1.16b
// 0x104e084: stp s0, s1, [x21, #0x48]
// 0x104e088: cbz w8, #0x104e0ac
// 0x104e08c: ldr x0, [x19, #0x18]
// 0x104e090: cbz x0, #0x104e0b8
// 0x104e094: bl #0x104da28
// 0x104e098: mov x1, x0
// 0x104e09c: mov x0, x21
// 0x104e0a0: mov v0.16b, v8.16b
// 0x104e0a4: mov v1.16b, v9.16b
// 0x104e0a8: bl #0x104e244
// 0x104e0ac: ldr x8, [x19, #0x10]
// 0x104e0b0: add x20, x20, #1
// 0x104e0b4: cbnz x8, #0x104e04c
// 0x104e0b8: bl #0xf7db74
// 0x104e0bc: ldp x20, x19, [sp, #0x80]
// 0x104e0c0: ldp x22, x21, [sp, #0x70]
// 0x104e0c4: ldp x24, x23, [sp, #0x60]
// 0x104e0c8: ldr x30, [sp, #0x58]
// 0x104e0cc: ldp d9, d8, [sp, #0x48]
// 0x104e0d0: ldp d11, d10, [sp, #0x38]
// 0x104e0d4: ldr d12, [sp, #0x30]
// 0x104e0d8: add sp, sp, #0x90
// 0x104e0dc: ret
// 0x104e0e0: ldr x8, [x19, #0x18]
// 0x104e0e4: cbz x8, #0x104e0b8
// 0x104e0e8: ldr w0, [x8, #0x194]
// 0x104e0ec: mov x1, xzr
// 0x104e0f0: bl #0x1bc76bc
// 0x104e0f4: tst w0, #1
// 0x104e0f8: mov w8, #3
// 0x104e0fc: csel w20, w8, wzr, ne
// 0x104e100: b #0x104ded0
// 0x104e104: bl #0xf7db7c
// 0x104e108: adrp x0, #0x1e8c000
// 0x104e10c: ldr x0, [x0, #0xcc0]
// 0x104e110: bl #0xf7d940
// 0x104e114: bl #0xf7db70
// 0x104e118: mov x19, x0
// 0x104e11c: adrp x0, #0x1e8c000
// 0x104e120: ldr x0, [x0, #0xcc8]
// 0x104e124: bl #0xf7d940
// 0x104e128: mov x1, x0
// 0x104e12c: mov x0, x19
// 0x104e130: mov x2, xzr
// 0x104e134: bl #0x19439c0
// 0x104e138: adrp x0, #0x1e8c000
// 0x104e13c: ldr x0, [x0, #0xcd0]
// 0x104e140: bl #0xf7d940
// 0x104e144: mov x1, x0
// 0x104e148: mov x0, x19
// 0x104e14c: bl #0xf7da4c
```

## `SuperTouchZone.EmulatedFingerSystem.DrawMarkers` — RVA `0xc4e280`

- Decompiled symbol: `SuperTouchZone_EmulatedFingerSystem_DrawMarkers`
- Metadata signature: `public void DrawMarkers() { }`
- Native interval: `1752` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SuperTouchZone_EmulatedFingerSystem_Recovered` matched 3 offsets against `SuperTouchZone.EmulatedFingerSystem` metadata (confidence 1.00).

```c
typedef struct struct_9 {
    char padding_0[224];
    unsigned int field_e0;
} struct_9;

typedef struct SuperTouchZone_EmulatedFingerSystem_Recovered {
    char padding_0[16];
    struct struct_4 *fingers;
    struct struct_6 *zone;
    char padding_20[16];
    int curFingerNum;
} SuperTouchZone_EmulatedFingerSystem_Recovered;

typedef struct struct_4 {
    char padding_0[24];
    int field_18;
} struct_4;

typedef struct struct_6 {
    char padding_0[444];
    unsigned int field_1bc;
    unsigned int field_1c0;
    char padding_1c4[4];
    unsigned int field_1c8;
} struct_6;

typedef struct struct_7 {
    char padding_0[12];
    unsigned long long field_c;
    unsigned int field_14;
} struct_7;

typedef struct struct_8 {
    char padding_0[184];
    struct struct_7 *field_b8;
} struct_8;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern struct_8 *g_1ef22e8;
extern char g_1fab1e1;
extern char g_1fab246;

long long SuperTouchZone_EmulatedFingerSystem_DrawMarkers(struct_5 *ptr)
{
    unsigned long long v36;  // d11
    long long v37;  // x23
    unsigned int v45;  // w0
    unsigned long v46;  // x24
    unsigned int v47;  // w0
    unsigned int v48[115];  // x8
    unsigned int v49;  // w8
    unsigned int v50;  // w27
    unsigned int v52;  // s10
    unsigned long v53;  // 4176
    unsigned int v54;  // s0
    long long v38;  // x22
    unsigned long v55;  // 4146
    struct_4 *v56;  // x8
    int v57;  // w23
    struct_9 **v59;  // x25
    long long v39;  // x20
    long long p[7];  // x8
    long long v41;  // x0
    long long v42;  // x0
    long long v43;  // x0
    uint128_t v44;  // q0
    unsigned long v0;  // [bp-0x290]
    unsigned int v1;  // [bp-0x288]
    unsigned int v2;  // [bp-0x26c]
    unsigned int v3;  // [bp-0x268]
    unsigned int v4;  // [bp-0x264]
    char v13;  // [bp-0x1e0]
    uint128_t v14;  // [bp-0x1d0]
    uint128_t v15;  // [bp-0x1c0]
    uint128_t v16;  // [bp-0x1b0]
    char v17;  // [bp-0x1a0]
    uint128_t v18;  // [bp-0x190]
    uint128_t v19;  // [bp-0x180]
    uint128_t v20;  // [bp-0x170]
    char v21;  // [bp-0x160]
    uint128_t v22;  // [bp-0x150]
    uint128_t v23;  // [bp-0x140]
    uint128_t v24;  // [bp-0x130]
    uint128_t v25;  // [bp-0x120], Other Possible Types: char
    uint128_t v26;  // [bp-0x110]
    uint128_t v27;  // [bp-0x100]
    uint128_t v28;  // [bp-0xf0]
    uint128_t v29;  // [bp-0xe0]
    uint128_t v30;  // [bp-0xd0]
    uint128_t v31;  // [bp-0xc0]
    uint128_t v32;  // [bp-0xb0]
    unsigned long long v33;  // [bp-0x80]
    char *v34;  // [bp-0x60]
    char v35;  // [bp+0x0]

    v33 = v36;
    v34 = &v35;
    if (!(g_1fab246 & 1))
    {
        sub_f7d92c("O<");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("!Y");
        g_1fab246 = 1;
    }
    v31 = 0;
    v32 = 0;
    v29 = 0;
    v30 = 0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v37 = 0;
    v38 = 0;
    v39 = 0;
    if (((char)Object__op_Inequality(g_1ef1e30->field_b8->field_0, 0, 0) & 1))
    {
        p = g_1ef1e30->field_b8->field_0;
        if (p)
        {
            v39 = p[4];
            v38 = p[5];
            v37 = p[6];
        }
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v41 = Object__op_Equality(v39, 0, 0);
    if (((char)v41 & 1))
        return v41;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v42 = Object__op_Equality(v38, 0, 0);
    if (((char)v42 & 1))
        return v42;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v43 = Object__op_Equality(v37, 0, 0);
    if (((char)v43 & 1))
        return v43;
    v59 = "O<";
    if (!g_1eefa78->field_e0)
        sub_f7da5c(g_1eefa78);
    GUI__get_matrix(0);
    v44 = v25;
    v29 = v44;
    v30 = v26;
    v31 = v27;
    v32 = v28;
    GUI__get_color(0);
    v3 = v30;
    v4 = v44;
    v2 = v31;
    if (ptr->field_30 < 2)
    {
LABEL_104e754:
        if (!g_1eefa78->field_e0)
            sub_f7da5c(g_1eefa78);
        GUI__set_color(0);
        v56 = ptr->field_10;
        v57 = 0;
    }
    else if (ptr->field_18 && !((v45 = (unsigned int)(unsigned long long)Input__GetKey((unsigned long long)ptr->field_18->field_1bc, 0), !ptr->field_18 || (v46 = (unsigned long)(unsigned long long)(unsigned int)(unsigned long long)Input__GetKey((unsigned long long)ptr->field_18->field_1bc, 0), v47 = (unsigned int)Input__GetKey(ptr->field_18->field_1c0, 0), v48 = (unsigned int [115])ptr->field_18, !v48))))
    {
        if (v48[114] == v48[1])
            v49 = 0;
        else
            v49 = 1;
        v50 = Input__GetKey(ptr->field_18->field_1c0, 0) & v49;
        if (((unsigned int)v46 & v50) == 1)
        {
            v52 = (unsigned int)v44 * 0x3f000000;
            sinf(Time__get_unscaledTime(0));
            v53 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v52 * 2157060022, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v52 * 2157060022, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v52 * 2157060022, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v52 * 2157060022, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v52 * 2157060022, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v52 * 2157060022, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            v54 = (v52 + 0x3f000000) * 2157060022;
            sinf();
            v55 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v54, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF((v52 + 0x3f000000) * 2157060022, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF((v52 + 0x3f000000) * 2157060022, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF((v52 + 0x3f000000) * 2157060022, 0.0) & 1)) & ((unsigned long long)(char)(CmpF((v52 + 0x3f000000) * 2157060022, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF((v52 + 0x3f000000) * 2157060022, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        }
        Screen__get_height(0);
        if (((char)v46 & 1))
        {
            if (!g_1eefa78->field_e0)
                sub_f7da5c(g_1eefa78);
            GUI__set_color(0);
            if (ptr->field_18)
            {
                Quaternion__Internal_FromEulerRad();
                if (!g_1fab1e1)
                {
                    sub_f7d92c(&g_1ef22e8);
                    g_1fab1e1 = 1;
                }
                v1 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
                v0 = *((long long *)&(&g_1ef22e8->field_b8->padding_0)[1]);
                Matrix4x4__TRS(0);
                memcpy(&v25, &v21, 16);
                v26 = v22;
                v27 = v23;
                v28 = v24;
                if (!g_1eefa78->field_e0)
                    sub_f7da5c(g_1eefa78);
                memcpy(&v17, &v25, 16);
                v18 = v26;
                v19 = v27;
                v20 = v28;
                GUI__set_matrix(&v17, 0);
                GUI__DrawTexture(v37, 2, 0);
                goto LABEL_104e628;
            }
        }
        else
        {
LABEL_104e628:
            if (!v50)
                goto LABEL_104e754;
            if (!g_1eefa78->field_e0)
                sub_f7da5c(g_1eefa78);
            GUI__set_color(0);
            if (ptr->field_18)
            {
                Quaternion__Internal_FromEulerRad();
                if (!g_1fab1e1)
                {
                    sub_f7d92c(&g_1ef22e8);
                    g_1fab1e1 = 1;
                }
                v1 = *((int *)((char *)&g_1ef22e8->field_b8->field_c + 4));
                v0 = *((long long *)&(&g_1ef22e8->field_b8->padding_0)[1]);
                Matrix4x4__TRS(0);
                memcpy(&v25, &v21, 16);
                v26 = v22;
                v27 = v23;
                v28 = v24;
                if (!g_1eefa78->field_e0)
                    sub_f7da5c(g_1eefa78);
                memcpy(&v13, &v25, 16);
                v14 = v26;
                v15 = v27;
                v16 = v28;
                GUI__set_matrix(&v13, 0);
                GUI__DrawTexture(v38, 2, 0);
                goto LABEL_104e754;
            }
        }
    }
}
```

## `SuperTouchZone.EmulatedFingerSystem.GetFingerAngle` — RVA `0xc4e958`

- Decompiled symbol: `SuperTouchZone_EmulatedFingerSystem_GetFingerAngle`
- Metadata signature: `private float GetFingerAngle(int fingerId) { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    int field_30;
} struct_0;

struct_0 * SuperTouchZone_EmulatedFingerSystem_GetFingerAngle(struct_0 *a0, unsigned long a1)
{
    return a0;
}
```
