# Native pseudocode: Randomly_Customize_NPC

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `Randomly_Customize_NPC.Start` — RVA `0xc727d4`

- Decompiled symbol: `Randomly_Customize_NPC_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `356` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Randomly_Customize_NPC_Recovered` matched 7 offsets against `Randomly_Customize_NPC` metadata (confidence 1.00).

```c
typedef struct Randomly_Customize_NPC_Recovered {
    char padding_0[32];
    long long Face_Obj;
    long long cap_Obj;
    long long Helmet_Obj;
    long long Mask_Obj;
    long long Body;
    long long Helmet;
    struct struct_0 *UniformMat;
} Randomly_Customize_NPC_Recovered;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

extern char g_85226a;

unsigned long long Randomly_Customize_NPC_Start(struct_1 *ptr)
{
    long long v0;  // x0
    struct_0 *v1;  // x8
    unsigned long long v2;  // x20
    unsigned long long v3;  // x21
    struct_0 *v4;  // x8
    unsigned long long v5;  // x0

    if (ptr->field_50)
    {
        v0 = Random__RandomRange(0, ptr->field_50->field_18, 0);
        v1 = ptr->field_50;
        if (v1)
        {
            v2 = v0 & 4294967295;
            if (v1->field_18 <= (int)v0)
            {
                sub_f7db7c(v0);
            }
            else if (ptr->field_40)
            {
                v3 = v2 * 0x100000000 >> 63 & 0xffffffff00000000 | v2 & 4294967295;
                v0 = Renderer__set_material(ptr->field_40, *((long long *)&v1[1].padding_0[4 + 8 * v3]), 0);
                v4 = ptr->field_50;
                if (v4)
                {
                    if (v4->field_18 <= (unsigned int)v2)
                    {
                        sub_f7db7c(v0);
                    }
                    else if (ptr->field_48)
                    {
                        Renderer__set_material(ptr->field_48, *((long long *)&v4[1].padding_0[4 + 8 * v3]), 0);
                        Random__RandomRange(0, 4, 0);
                        if (ptr->field_20)
                        {
                            GameObject__SetActive(ptr->field_20, 0, 0);
                            if (ptr->field_28)
                            {
                                GameObject__SetActive(ptr->field_28, 0, 0);
                                if (ptr->field_30)
                                {
                                    GameObject__SetActive(ptr->field_30, 0, 0);
                                    if (ptr->field_38)
                                    {
                                        v5 = GameObject__SetActive(ptr->field_38, 0, 0);
                                        if (3 < Random__RandomRange(0, 4, 0))
                                            return v5;
                                        goto sub_10728e4 + (&g_85226a)[Random__RandomRange(0, 4, 0) & 4294967295] * 4;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db7c(sub_f7db74());
}
```


## `Randomly_Customize_NPC.Preset_1` — RVA `0xc72938`

- Decompiled symbol: `Randomly_Customize_NPC_Preset_1`
- Metadata signature: `private void Preset_1() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
void Randomly_Customize_NPC_Preset_1(long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[4];
    if (v4)
    {
        GameObject__SetActive(v4, 1, 0);
        v4 = ptr[5];
        if (ptr[5])
        {
            GameObject__SetActive();
            return;
        }
    }
    sub_f7db74(v4);
}
```


## `Randomly_Customize_NPC.Preset_2` — RVA `0xc72970`

- Decompiled symbol: `Randomly_Customize_NPC_Preset_2`
- Metadata signature: `private void Preset_2() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
void Randomly_Customize_NPC_Preset_2(long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[4];
    if (v4)
    {
        GameObject__SetActive(v4, 1, 0);
        v4 = ptr[6];
        if (ptr[6])
        {
            GameObject__SetActive();
            return;
        }
    }
    sub_f7db74(v4);
}
```


## `Randomly_Customize_NPC.Preset_3` — RVA `0xc729a8`

- Decompiled symbol: `Randomly_Customize_NPC_Preset_3`
- Metadata signature: `private void Preset_3() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[56];
    unsigned long long field_38;
} struct_0;

void Randomly_Customize_NPC_Preset_3(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a0->field_38)
    {
        GameObject__SetActive();
        return;
    }
    sub_f7db74(0);
}
```


## `Randomly_Customize_NPC.Preset_4` — RVA `0xc729c8`

- Decompiled symbol: `Randomly_Customize_NPC_Preset_4`
- Metadata signature: `private void Preset_4() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
void Randomly_Customize_NPC_Preset_4(unsigned long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[7];
    if (v4)
    {
        GameObject__SetActive(v4, 1, 0);
        v4 = ptr[6];
        if (ptr[6])
        {
            GameObject__SetActive();
            return;
        }
    }
    sub_f7db74(v4);
}
```


## `Randomly_Customize_NPC.ctor` — RVA `0xc72a00`

- Decompiled symbol: `Randomly_Customize_NPC_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long Randomly_Customize_NPC_ctor(void)
{
}
```
