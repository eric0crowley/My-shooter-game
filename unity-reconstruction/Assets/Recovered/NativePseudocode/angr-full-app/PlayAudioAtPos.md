# Native pseudocode: PlayAudioAtPos

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `PlayAudioAtPos.PlayClipAt` — RVA `0xc8d260`

- Decompiled symbol: `PlayAudioAtPos_PlayClipAt`
- Metadata signature: `public static AudioSource PlayClipAt(AudioClip clip, Vector3 pos, float vol, float blend = 1.0, float pitch = 1.0, float minDist = 1.0, float maxDist = 500.0) { }`
- Native interval: `412` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    long long field_20;
} struct_0;

extern long long g_1efece0;
extern char g_1fab2cb;
extern char g_1fab43c;

long long PlayAudioAtPos_PlayClipAt(long long a0, unsigned long a1)
{
    unsigned long long v0;  // x20
    struct_0 *ptr;  // x0
    long long v2;  // x21
    struct_0 *v3;  // x20

    if (!(g_1fab43c & 1))
    {
        sub_f7d92c("s.");
        sub_f7d92c(&g_1efece0);
        g_1fab43c = 1;
    }
    v0 = g_1eeea08->field_b8->field_0;
    if (!g_1fab2cb)
    {
        sub_f7d92c("-M");
        g_1fab2cb = 1;
    }
    if (v0 && AzuObjectPool__SpawnPooledObj())
    {
        ptr = sub_1249224();
        if (ptr)
        {
            v2 = ptr->field_20;
            v3 = ptr;
            if (v2)
            {
                AudioSource__set_clip(v2, a0, 0);
                AudioSource__set_spatialBlend(v2, 0);
                AudioSource__set_minDistance(v2, 0);
                AudioSource__set_maxDistance(v2, 0);
                AudioSource__set_volume(v2, 0);
                AudioSource__set_pitch(v2, 0);
                AudioSource__Play(v2, 0);
                MonoBehaviour__StartCoroutine(v3, TempAudioTimer__DeactivateTimer(v3), 0);
                return v2;
            }
        }
    }
    sub_f7db74();
}
```
