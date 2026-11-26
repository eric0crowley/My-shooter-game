# Native pseudocode: FoliageRustle

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `FoliageRustle.Start` — RVA `0xc998e4`

- Decompiled symbol: `FoliageRustle_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `340` bytes
- Result: `pseudocode`

```c
extern long long g_1efcfb0;
extern long long g_1efea78;
extern char g_1fab49a;

void FoliageRustle_Start(long long *ptr)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    long long v6;  // x0
    long long v7[6];  // x20
    long long v8;  // x0
    long long v9[6];  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab49a & 1))
    {
        sub_f7d92c(&g_1efcfb0);
        sub_f7d92c(&g_1efea78);
        g_1fab49a = 1;
    }
    if (Camera__get_main(0) && Component__get_transform() && Transform__get_parent() && Component__get_transform())
    {
        v6 = sub_1231bc8();
        ptr[5] = v6;
        v7 = ptr + 5;
        sub_f7d8d0(v7, v6);
        if (Component__get_transform(ptr, 0) && Component__get_gameObject())
        {
            v8 = sub_124913c();
            ptr[4] = v8;
            v9 = ptr + 4;
            sub_f7d8d0(v9, v8);
            if (v9[0])
            {
                AudioSource__set_spatialBlend(v9[0], 0);
                if (v7[0] && v9[0])
                {
                    AudioSource__set_volume(v9[0], 0);
                    if (v9[0])
                    {
                        AudioSource__set_pitch(v9[0], 0);
                        if (v9[0])
                        {
                            AudioSource__set_dopplerLevel(v9[0], 0);
                            if (v9[0])
                                AudioSource__set_maxDistance(v9[0], 0);
                        }
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `FoliageRustle.OnTriggerEnter` — RVA `0xc99a38`

- Decompiled symbol: `FoliageRustle_OnTriggerEnter`
- Metadata signature: `private void OnTriggerEnter(Collider col) { }`
- Native interval: `244` bytes
- Result: `pseudocode`
- Heuristic layout hint: `FoliageRustle_Recovered` matched 2 offsets against `FoliageRustle` metadata (confidence 1.00).

```c
typedef struct FoliageRustle_Recovered {
    char padding_0[32];
    long long rustleFx;
    struct struct_0 *FootstepsComponent;
} FoliageRustle_Recovered;

typedef struct struct_0 {
    char padding_0[360];
    void* field_168;
} struct_0;

void FoliageRustle_OnTriggerEnter(struct_1 *idx, long long a1)
{
    void* v0;  // x21
    unsigned long v1;  // x0

    if (idx->field_28 && idx->field_28->field_168)
    {
        if (!(long long)idx->field_28->field_168[24])
            return;
        if (a1 && Component__get_gameObject(a1, 0))
        {
            if (GameObject__get_layer() == 11)
            {
LABEL_1099aa4:
                if (idx->field_28)
                {
                    v0 = idx->field_28->field_168;
                    if (v0)
                    {
                        v1 = Random__Range(0, (int)v0[24], 0);
                        if ((int)v0[24] <= (unsigned int)v1)
                            sub_f7db7c(v1);
                        if (idx->field_20)
                        {
                            AudioSource__set_clip(idx->field_20, *((long long *)(32 + (char *)v0 + 8 * (v1 & 4294967295))), 0);
                            if (idx->field_20)
                            {
                                AudioSource__get_clip(idx->field_20, 0);
                                AudioSource__PlayOneShot();
                                return;
                            }
                        }
                    }
                }
            }
            else if (Component__get_gameObject(a1, 0))
            {
                if (GameObject__get_layer() != 13)
                    return;
                goto LABEL_1099aa4;
            }
        }
    }
    v1 = sub_f7db74();
    sub_f7db7c(v1);
}
```

## `FoliageRustle.ctor` — RVA `0xc99b2c`

- Decompiled symbol: `FoliageRustle_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long FoliageRustle_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
