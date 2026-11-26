# Native pseudocode: AudioIgnoreListenerPauseAndVolume

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `AudioIgnoreListenerPauseAndVolume.OnEnable` — RVA `0xc64ac4`

- Decompiled symbol: `AudioIgnoreListenerPauseAndVolume_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `324` bytes
- Result: `pseudocode`
- Heuristic layout hint: `AudioIgnoreListenerPauseAndVolume_Recovered` matched 3 offsets against `AudioIgnoreListenerPauseAndVolume` metadata (confidence 1.00).

```c
typedef struct AudioIgnoreListenerPauseAndVolume_Recovered {
    char padding_0[32];
    void* targetSources;
    char ignoreListenerVolume;
    char ignoreListenerPause;
} AudioIgnoreListenerPauseAndVolume_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efd178;
extern char g_1fab2f0;

struct_1 * AudioIgnoreListenerPauseAndVolume_OnEnable(struct_1 *ptr)
{
    struct_1 *v0;  // x0
    struct_1 *v1;  // x0
    void* v10;  // x8
    unsigned long v11;  // x0
    struct_1 *v2;  // x0
    void* addr;  // x8
    struct_1 *p;  // x20
    void* v5;  // x0
    unsigned long long v6;  // x23
    unsigned long v7;  // x9
    unsigned long long v8;  // x24
    void* v9;  // x8

    v0 = ptr;
    if (!(g_1fab2f0 & 1))
    {
        sub_f7d92c(&g_1efd178);
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab2f0 = 1;
        v0 = v1;
    }
    addr = ptr->field_20;
    p = &ptr->field_20;
    if (!addr || !(long long)addr[24])
    {
        v5 = sub_123226c(ptr, g_1efd178);
        ptr->field_20 = v5;
        v2 = sub_f7d8d0(p, v5);
        addr = ptr->field_20;
        if (!addr)
        {
            v11 = sub_f7db74();
            return sub_f7db74();
        }
    }
    v6 = 4;
    do
    {
        v7 = (int)addr[24];
        v8 = v6 - 4;
        if ((v7 & 4294967295) <= v8)
            return v2;
        if (v7 <= v8)
            sub_f7db7c();
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (!(Object__op_Inequality(*((long long *)((char *)addr + 8 * v6)), 0, 0) & 1))
            continue;
        v9 = *((long long *)&p->padding_0[0]);
        if (!v9)
            break;
        if ((int)v9[24] <= v8)
            sub_f7db7c();
        if (!*((long long *)((char *)v9 + 8 * v6)) || !((AudioSource__set_ignoreListenerPause(*((long long *)((char *)v9 + 8 * v6)), (unsigned long long)ptr->field_29, 0), v10 = ptr->field_20, v10)))
            break;
        if ((int)v10[24] <= v8)
            sub_f7db7c();
        if (!*((long long *)((char *)v10 + 8 * v6)))
            break;
        v2 = AudioSource__set_ignoreListenerVolume(*((long long *)((char *)v10 + 8 * v6)), ptr->field_28, 0);
    } while ((addr = (void*)*((long long *)&p->padding_0[0]), v6 += 1, addr));
    v11 = sub_f7db74();
    return sub_f7db74();
}
```

## `AudioIgnoreListenerPauseAndVolume.ctor` — RVA `0xc64c08`

- Decompiled symbol: `AudioIgnoreListenerPauseAndVolume_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned short field_28;
} struct_0;

long long AudioIgnoreListenerPauseAndVolume_ctor(struct_0 *ptr)
{
    unsigned long long v0;  // x0

    ptr->field_28 = 257;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
