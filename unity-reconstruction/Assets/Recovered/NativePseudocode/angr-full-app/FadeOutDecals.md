# Native pseudocode: FadeOutDecals

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `FadeOutDecals.Awake` — RVA `0xc8e1f8`

- Decompiled symbol: `FadeOutDecals_Awake`
- Metadata signature: `private void Awake() { }`
- Native interval: `204` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FadeOutDecals_Recovered` matched 4 offsets against `FadeOutDecals` metadata (confidence 1.00).

```c
typedef struct FadeOutDecals_Recovered {
    char padding_0[40];
    long long RendererComponent;
    char padding_30[16];
    long long parentObj;
    unsigned long long parentObjTransform;
    long long myTransform;
} FadeOutDecals_Recovered;

extern long long g_1efd070;
extern char g_1fab441;

void FadeOutDecals_Awake(struct_0 *ptr5)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    long long v14;  // x0
    struct_0 *ptr;  // x20
    struct_0 *ptr3;  // x20
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    long long v8;  // x0
    struct_0 *p;  // x20
    struct_0 *ptr4;  // x20
    long long v11;  // x1
    struct_0 *addr;  // x0
    long long v13;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    if (!(g_1fab441 & 1))
    {
        sub_f7d92c(&g_1efd070);
        g_1fab441 = 1;
    }
    v8 = Component__get_transform(ptr5, 0);
    p = ptr5;
    p->field_50 = v8;
    ptr4 = &p->field_50;
    sub_f7d8d0(ptr4, v8);
    v11 = sub_1231bc8(ptr5, g_1efd070);
    addr = ptr5;
    addr->field_28 = v11;
    sub_f7d8d0((struct FadeOutDecals_Recovered *)&addr->field_28, v11);
    v13 = *((long long *)&ptr4->padding_0[0]);
    if (v13)
    {
        v13 = Transform__get_parent(v13, 0);
        if (v13)
        {
            v14 = Component__get_gameObject();
            ptr = ptr5;
            ptr->field_40 = v14;
            ptr3 = &ptr->field_40;
            sub_f7d8d0(ptr3, v14);
            v13 = *((long long *)&ptr3->padding_0[0]);
            if (v13)
            {
                ptr5->field_48 = GameObject__get_transform(v13, 0);
                sub_f7d8d0();
                return;
            }
        }
    }
    sub_f7db74(v13);
}
```

## `FadeOutDecals.InitializeDecal` — RVA `0xc8e2c4`

- Decompiled symbol: `FadeOutDecals_InitializeDecal`
- Metadata signature: `public void InitializeDecal() { }`
- Native interval: `120` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned int field_20;
    unsigned int field_24;
    unsigned long long field_28;
    unsigned int field_30;
    unsigned int field_34;
    unsigned int field_38;
    unsigned int field_3c;
} struct_0;

void FadeOutDecals_InitializeDecal(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v4;  // x0
    unsigned int v5;  // s1
    unsigned int v6;  // s0
    unsigned int v7;  // s0
    unsigned int v8;  // s2
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    Time__get_time(0);
    v4 = ptr->field_28;
    v5 = ptr->field_24;
    v7 = v6 + v5;
    ptr->field_20 = v7;
    if (v4)
    {
        v4 = Renderer__get_material(v4, 0);
        if (v4)
        {
            Material__get_color();
            v4 = ptr->field_28;
            ptr->field_30 = v7;
            ptr->field_34 = v5;
            ptr->field_38 = v8;
            ptr->field_3c = 0x3f800000;
            if (v4)
            {
                v4 = Renderer__get_material(v4, 0);
                if (v4)
                {
                    Material__set_color();
                    return;
                }
            }
        }
    }
    sub_f7db74(v4);
}
```

## `FadeOutDecals.Update` — RVA `0xc8e33c`

- Decompiled symbol: `FadeOutDecals_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `296` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FadeOutDecals_Recovered` matched 5 offsets against `FadeOutDecals` metadata (confidence 0.83).

```c
typedef struct FadeOutDecals_Recovered {
    char padding_0[32];
    unsigned int startTime;
    unsigned int markDuration;
    long long RendererComponent;
    char padding_30[12];
    unsigned int field_3c;
    long long parentObj;
    long long parentObjTransform;
} FadeOutDecals_Recovered;

extern char g_1fab442;

int FadeOutDecals_Update(struct_2 *ptr)
{
    unsigned int v0;  // s8
    unsigned int v1;  // s0
    unsigned int v10;  // s1
    unsigned long v11;  // 4153
    unsigned long v2;  // 4125
    long long v3;  // x0
    unsigned int v4;  // s0
    unsigned int v5;  // s1
    unsigned int v6;  // s0
    unsigned long v7;  // 4140
    unsigned int v8;  // s8
    unsigned int v9;  // w0

    if (!(g_1fab442 & 1))
    {
        sub_f7d92c("s.");
        g_1fab442 = 1;
    }
    v0 = ptr->field_20;
    Time__get_time(0);
    v2 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) & ((unsigned long long)(char)(CmpF(v0, v1)) >> 5 & 3 | (unsigned long long)(CmpF(v0, v1) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if (!((char)v2))
    {
        Time__get_deltaTime(0);
        v3 = ptr->field_28;
        ptr->field_3c = ptr->field_3c - v1;
        if (!v3)
            sub_f7db74(v3);
        v3 = Renderer__get_material(v3, 0);
        if (!v3)
            sub_f7db74(v3);
        Material__set_color();
        v4 = ptr->field_3c;
        v5 = [D] unsupported_Iop_ZeroHI96ofV128();
        v6 = 0;
        v7 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) & ((unsigned long long)(char)(CmpF(v4, 0.0)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0.0) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
        if ((char)v7)
            v6 = v5;
        ptr->field_3c = v6;
    }
    v8 = ptr->field_20;
    v9 = Time__get_time(0);
    v10 = ptr->field_24;
    v11 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v8, v6 - v10)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v6 - v10) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v8, v6 - v10)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v6 - v10) & 1)) & ((unsigned long long)(char)(CmpF(v8, v6 - v10)) >> 5 & 3 | (unsigned long long)(CmpF(v8, v6 - v10) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
    if ((char)v11)
        return v9;
    v3 = g_1eeea08->field_b8->field_0;
    if (v3)
    {
        v3 = Component__get_transform(v3, 0);
        if (ptr->field_48)
        {
            Transform__set_parent(ptr->field_48, v3, 0);
            v3 = ptr->field_40;
            if (v3)
                return GameObject__SetActive();
        }
    }
    sub_f7db74(v3);
}
```

## `FadeOutDecals.ctor` — RVA `0xc8e464`

- Decompiled symbol: `FadeOutDecals_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[36];
    unsigned int field_24;
} struct_0;

long long FadeOutDecals_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_24 = 10;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
