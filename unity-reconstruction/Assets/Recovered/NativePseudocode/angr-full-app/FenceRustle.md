# Native pseudocode: FenceRustle

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `FenceRustle.OnTriggerEnter` — RVA `0xc997d0`

- Decompiled symbol: `FenceRustle_OnTriggerEnter`
- Metadata signature: `private void OnTriggerEnter(Collider col) { }`
- Native interval: `260` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FenceRustle_Recovered` matched 2 offsets against `FenceRustle` metadata (confidence 1.00).

```c
typedef struct FenceRustle_Recovered {
    char padding_0[32];
    void* fenceRustles;
    char padding_28[4];
    unsigned int lastRustleTime;
} FenceRustle_Recovered;

int FenceRustle_OnTriggerEnter(struct_0 *ptr, long long a1)
{
    struct_0 *v0;  // x0
    struct_0 *v2;  // x0
    unsigned int v3;  // s0
    unsigned int v4;  // s0
    unsigned long v5;  // 4142
    void* v6;  // x20
    unsigned long v7;  // x0
    struct_0 *v8;  // x0

    if (ptr->field_20)
    {
        v0 = ptr;
        if (!(long long)v0->field_20[24])
            return *((unsigned int *)&v0);
        if (a1 && Component__get_gameObject(a1, 0))
        {
            if (GameObject__get_layer() == 11)
            {
LABEL_1099834:
                v2 = Time__get_time(0);
                v4 = v3 - ptr->field_2c;
                v5 = arm64g_calculate_condition(208, (((((unsigned long long)(char)(CmpF(v4, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0x3f800000) & 1)) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - (((unsigned long long)(char)(CmpF(v4, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0x3f800000) & 1)) & ((unsigned long long)(char)(CmpF(v4, 0x3f800000)) >> 5 & 3 | (unsigned long long)(CmpF(v4, 0x3f800000) & 1)) >> 1 & 1)) * 0x10000000, 0, 0);
                v0 = v2;
                if ((char)v5)
                    return *((unsigned int *)&v0);
                v6 = ptr->field_20;
                if (v6)
                {
                    v7 = Random__Range(0, (int)v6[24], 0);
                    if ((int)v6[24] <= (unsigned int)v7)
                        sub_f7db7c(v7);
                    if (Component__get_transform(ptr, 0))
                    {
                        Transform__get_position();
                        PlayAudioAtPos__PlayClipAt(*((long long *)(32 + (char *)v6 + 8 * (v7 & 4294967295))), 0);
                        v8 = Time__get_time(0);
                        ptr->field_2c = v4;
                        v0 = v8;
                        return *((unsigned int *)&v0);
                    }
                }
            }
            else if (Component__get_gameObject(a1, 0))
            {
                v0 = GameObject__get_layer();
                if ((unsigned int)v0 != 13)
                    return *((unsigned int *)&v0);
                goto LABEL_1099834;
            }
        }
    }
    v7 = sub_f7db74();
    sub_f7db7c(v7);
}
```

## `FenceRustle.ctor` — RVA `0xc998d4`

- Decompiled symbol: `FenceRustle_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned int field_28;
} struct_0;

long long FenceRustle_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_28 = 0x3f800000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
