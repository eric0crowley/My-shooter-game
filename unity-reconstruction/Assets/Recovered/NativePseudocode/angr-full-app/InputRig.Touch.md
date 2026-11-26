# Native pseudocode: InputRig.Touch

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InputRig.Touch.cctor` — RVA `0xc3e9d8`

- Decompiled symbol: `InputRig_Touch_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `152` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    unsigned int field_0;
    char padding_4[68];
    unsigned long long field_48;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_0 *field_b8;
} struct_1;

extern struct_1 *g_1ef3368;
extern char g_1fab1e6;

void InputRig_Touch_cctor(void)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v8;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab1e6 & 1))
    {
        sub_f7d92c("Y*");
        sub_f7d92c(&g_1ef3368);
        g_1fab1e6 = 1;
    }
    memset(g_1ef3368->field_b8, 0, 68);
    g_1ef3368->field_b8->field_0 = 4;
    v8 = sub_f7d9d4(g_1eee528, 0);
    g_1ef3368->field_b8->field_48 = v8;
    sub_f7d8d0();
    return;
}
```

## `InputRig.Touch.ctor` — RVA `0xc3ea70`

- Decompiled symbol: `InputRig_Touch_ctor`
- Metadata signature: `public void .ctor(Touch t) { }`
- Native interval: `168` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_Touch_Recovered` matched 10 offsets against `InputRig.Touch` metadata (confidence 0.77).

```c
typedef struct InputRig_Touch_Recovered {
    unsigned int phase;
    unsigned int deltaTime;
    unsigned int fingerId;
    unsigned int tapCount;
    unsigned int position;
    unsigned int field_14;
    unsigned int rawPosition;
    unsigned int field_1c;
    unsigned int deltaPosition;
    unsigned int field_24;
    uint128_t altitudeAngle;
    unsigned long long radius;
    unsigned int type;
} InputRig_Touch_Recovered;

unsigned long long InputRig_Touch_ctor(struct_0 *ptr, long long a1)
{
    unsigned int v0;  // s0
    unsigned int v1;  // s1
    unsigned long long v2;  // x0

    ptr->field_0 = Touch__get_phase(a1, 0);
    Touch__get_deltaTime(a1, 0);
    ptr->field_4 = v0;
    ptr->field_8 = Touch__get_fingerId(a1, 0);
    ptr->field_c = Touch__get_tapCount(a1, 0);
    Touch__get_position(a1, 0);
    ptr->field_10 = v0;
    ptr->field_14 = v1;
    Touch__get_rawPosition(a1, 0);
    ptr->field_18 = v0;
    ptr->field_1c = v1;
    v2 = Touch__get_deltaPosition(a1, 0);
    ptr->field_20 = v0;
    ptr->field_24 = v1;
    *((unsigned int *)&ptr->field_38) = 0;
    *((uint128_t *)&(&ptr->field_24)[1]) = 0x3f8000003f8000000000000000000000;
    *((unsigned long long *)((char *)&ptr->field_28 + 8)) = 0x3f800000;
    return v2;
}
```

## `InputRig.Touch.TranslateUnityTouches` — RVA `0xc3eb18`

- Decompiled symbol: `InputRig_Touch_TranslateUnityTouches`
- Metadata signature: `public static InputRig.Touch[] TranslateUnityTouches(Touch[] tarr) { }`
- Native interval: `460` bytes
- Result: `pseudocode`
- Heuristic layout hint: `InputRig_Touch_Recovered` matched 10 offsets against `InputRig.Touch` metadata (confidence 0.77).

```c
typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_4 {
    char padding_0[24];
    unsigned long long field_18;
} struct_4;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_1;

typedef struct InputRig_Touch_Recovered {
    unsigned int phase;
    unsigned int deltaTime;
    unsigned int fingerId;
    unsigned int tapCount;
    unsigned int position;
    unsigned int field_14;
    unsigned int rawPosition;
    unsigned int field_1c;
    unsigned int deltaPosition;
    unsigned int field_24;
    char padding_28[8];
    uint128_t altitudeAngle;
    unsigned long long radius;
    unsigned int type;
} InputRig_Touch_Recovered;

typedef struct struct_2 {
    char padding_0[72];
    struct InputRig_Touch_Recovered *field_48;
    struct InputRig_Touch_Recovered *field_50;
} struct_2;

typedef struct InputRig_Touch_Recovered {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

extern struct_1 *g_1ef3368;
extern char g_1fab1e7;

struct_3 * InputRig_Touch_TranslateUnityTouches(struct_4 *a0)
{
    struct_1 *idx;  // x0
    struct_3 *v10;  // x8
    struct_1 *v19;  // x0
    struct_3 *v11;  // x0
    struct_1 *ptr;  // x8
    struct_3 *v13;  // x20
    struct InputRig_Touch_Recovered *p[11];  // x0
    unsigned long v15;  // x22
    unsigned long long v16;  // x23
    struct_1 *off;  // x0
    struct_3 *v18;  // x20
    char v0;  // [bp-0x120]
    char v1;  // [bp-0xd8]
    struct_0 flag3;  // [bp-0x90]
    uint128_t flag4;  // [bp-0x80]
    uint128_t choice;  // [bp-0x70]
    uint128_t flag2;  // [bp-0x60]
    unsigned int flag;  // [bp-0x50]
    char *v7;  // [bp-0x40]
    char v8;  // [bp+0x0]

    v7 = &v8;
    if (!(g_1fab1e7 & 1))
    {
        sub_f7d92c("Y*");
        sub_f7d92c(&g_1ef3368);
        g_1fab1e7 = 1;
    }
    if (a0 && a0->field_18)
    {
        idx = g_1ef3368;
        if (!g_1ef3368->field_e0)
        {
            sub_f7da5c(g_1ef3368);
            idx = g_1ef3368;
        }
        v10 = idx->field_b8->field_50;
        if (idx->field_b8->field_50)
        {
            if (!idx->field_e0 && (sub_f7da5c(), v10 = (struct_3 *)g_1ef3368->field_b8->field_50, !v10))
                goto LABEL_103ece0;
            if ((int)a0->field_18 == v10->field_18)
                goto LABEL_103ec38;
        }
        v11 = sub_f7d9d4(g_1eee528);
        ptr = g_1ef3368;
        v13 = v11;
        if (!g_1ef3368->field_e0)
        {
            sub_f7da5c(g_1ef3368);
            ptr = g_1ef3368;
        }
        p = ptr->field_b8;
        p[10] = v13;
        sub_f7d8d0((struct InputRig_Touch_Recovered *[11])&p[10], v13);
LABEL_103ec38:
        v15 = 0;
        v16 = 32;
        while (true)
        {
            off = g_1ef3368;
            if (!g_1ef3368->field_e0)
            {
                sub_f7da5c(g_1ef3368);
                off = g_1ef3368;
            }
            v18 = off->field_b8->field_50;
            if ((int)a0->field_18 <= v15)
                return v18;
            if ((unsigned int)a0->field_18 > v15)
            {
                memcpy(&v1, (struct struct_4 *)&a0->padding_0[v16], 68);
                flag = 0;
                choice = 0;
                flag2 = 0;
                flag3 = (struct_0)0;
                flag4 = 0;
                InputRig_Touch__ctor(&flag3, &v1);
                if (!v18)
                    break;
                memcpy(&v0, &flag3, 68);
                if (v18->field_18 <= v15)
                    goto LABEL_103ecdc;
                memcpy((struct struct_3 *)&v18->padding_0[v16], &v0, 68);
                v15 += 1;
                v16 += 68;
            }
            else
            {
LABEL_103ecdc:
                sub_f7db7c();
                break;
            }
        }
LABEL_103ece0:
        sub_f7db74();
    }
    v19 = g_1ef3368;
    if (!g_1ef3368->field_e0)
    {
        sub_f7da5c(g_1ef3368);
        v19 = g_1ef3368;
    }
    return v19->field_b8->field_48;
}
```
