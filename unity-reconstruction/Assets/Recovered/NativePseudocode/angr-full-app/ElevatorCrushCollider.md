# Native pseudocode: ElevatorCrushCollider

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ElevatorCrushCollider.OnTriggerEnter` — RVA `0xc98774`

- Decompiled symbol: `ElevatorCrushCollider_OnTriggerEnter`
- Metadata signature: `private void OnTriggerEnter(Collider col) { }`
- Native interval: `332` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ElevatorCrushCollider_Recovered` matched 3 offsets against `ElevatorCrushCollider` metadata (confidence 1.00).

```c
typedef struct struct_1 {
    char padding_0[528];
    unsigned int field_210;
} struct_1;

typedef struct ElevatorCrushCollider_Recovered {
    char padding_0[32];
    long long squishSnd;
    char fxPlayed;
    char padding_29[3];
    unsigned int crushTime;
} ElevatorCrushCollider_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcf98;
extern long long g_1f0cf98;
extern char g_1fab48c;

long long ElevatorCrushCollider_OnTriggerEnter(struct_2 *ptr, long long a1)
{
    long long v0;  // x0
    long long v1;  // x0
    struct_1 *index;  // x20
    long long v3;  // x0
    long long v4;  // x0

    if (!(g_1fab48c & 1))
    {
        sub_f7d92c(&g_1efcf98);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0cf98);
        g_1fab48c = 1;
    }
    if (a1 && Component__get_gameObject(a1, 0))
    {
        v0 = GameObject__get_tag();
        v1 = String__op_Equality(v0, g_1f0cf98, 0);
        if (!((char)v1 & 1))
            return v1;
        index = sub_1231bc8(a1, g_1efcf98);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v3 = Object__op_Implicit(index, 0);
        if (!((char)v3 & 1))
        {
            return v3;
        }
        else if (ptr->field_28)
        {
            return v3;
        }
        else if (index)
        {
            FPSPlayer__ApplyDamage(index, 0, 0, 0);
            if (Component__get_transform(index, 0))
            {
                Transform__get_position();
                PlayAudioAtPos__PlayClipAt(ptr->field_20, 0);
                v4 = Time__get_time(0);
                ptr->field_2c = index->field_210 + 0x3f800000;
                ptr->field_28 = 1;
                return v4;
            }
        }
    }
    sub_f7db74();
}
```

## `ElevatorCrushCollider.OnTriggerExit` — RVA `0xc988c0`

- Decompiled symbol: `ElevatorCrushCollider_OnTriggerExit`
- Metadata signature: `private void OnTriggerExit(Collider col) { }`
- Native interval: `156` bytes
- Result: `pseudocode`
- Heuristic layout hint: `ElevatorCrushCollider_Recovered` matched 2 offsets against `ElevatorCrushCollider` metadata (confidence 1.00).

```c
typedef struct ElevatorCrushCollider_Recovered {
    char padding_0[40];
    char fxPlayed;
    char padding_29[3];
    unsigned int crushTime;
} ElevatorCrushCollider_Recovered;

extern long long g_1f0cf98;
extern char g_1fab48d;

int ElevatorCrushCollider_OnTriggerExit(struct_0 *ptr, long long a1)
{
    long long v0;  // x0
    unsigned long long v1;  // x0
    unsigned int v2;  // s1
    unsigned int v3;  // s0
    unsigned long v4;  // 4138

    if (!(g_1fab48d & 1))
    {
        sub_f7d92c(&g_1f0cf98);
        g_1fab48d = 1;
    }
    if (a1 && Component__get_gameObject(a1, 0))
    {
        v0 = GameObject__get_tag();
        v1 = String__op_Equality(v0, g_1f0cf98, 0);
        if (((char)v1 & 1))
        {
            v1 = Time__get_time(0);
            v2 = ptr->field_2c + 0x3f800000;
            v4 = arm64g_calculate_condition(80, (((((unsigned long long)(char)(CmpF(v2, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v3) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v2, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v3) & 1)) & ((unsigned long long)(char)(CmpF(v2, v3)) >> 5 & 3 | (unsigned long long)(CmpF(v2, v3) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
            if (!((char)v4))
                ptr->field_28 = 0;
        }
        return v1;
    }
    sub_f7db74();
}
```

## `ElevatorCrushCollider.ctor` — RVA `0xc9895c`

- Decompiled symbol: `ElevatorCrushCollider_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long ElevatorCrushCollider_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
