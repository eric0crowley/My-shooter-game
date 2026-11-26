# Native pseudocode: TempAudioTimer

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TempAudioTimer.DeactivateTimer` — RVA `0xc8d5d4`

- Decompiled symbol: `TempAudioTimer_DeactivateTimer`
- Metadata signature: `public IEnumerator DeactivateTimer() { }`
- Native interval: `108` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[12];
    long long field_20;
} struct_0;

extern char g_1fab43f;

struct_0 * TempAudioTimer_DeactivateTimer(long long a0)
{
    struct_0 *v0;  // x20
    struct_0 *ptr;  // x0

    if (!(g_1fab43f & 1))
    {
        sub_f7d92c("\tr");
        g_1fab43f = 1;
    }
    v0 = sub_f7db70(g_1ef3b60);
    Object__ctor(v0, 0);
    ptr = v0;
    ptr->field_10 = 0;
    ptr->field_20 = a0;
    sub_f7d8d0((struct struct_0 *)&ptr->field_20, a0);
    return ptr;
}
```

## `TempAudioTimer.Awake` — RVA `0xc8e064`

- Decompiled symbol: `TempAudioTimer_Awake`
- Metadata signature: `private void Awake() { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

void TempAudioTimer_Awake(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    if (Component__get_transform())
    {
        ptr->field_28 = Component__get_gameObject();
        sub_f7d8d0();
        return;
    }
    sub_f7db74();
}
```

## `TempAudioTimer.<DeactivateTimer>d__3.ctor` — RVA `0xc8e098`

- Decompiled symbol: `TempAudioTimer_DeactivateTimer_d__3_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void TempAudioTimer_DeactivateTimer_d__3_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `TempAudioTimer.ctor` — RVA `0xc8e0c0`

- Decompiled symbol: `TempAudioTimer_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long TempAudioTimer_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```

## `TempAudioTimer.<DeactivateTimer>d__3.Dispose` — RVA `0xc8e0c8`

- Decompiled symbol: `TempAudioTimer_DeactivateTimer_d__3_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long TempAudioTimer_DeactivateTimer_d__3_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `TempAudioTimer.<DeactivateTimer>d__3.MoveNext` — RVA `0xc8e0cc`

- Decompiled symbol: `TempAudioTimer_DeactivateTimer_d__3_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `228` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    long long field_18;
    struct struct_1 *field_20;
} struct_0;

typedef struct struct_1 {
    char padding_0[32];
    long long field_20;
    long long field_28;
} struct_1;

extern long long g_1ef2440;
extern char g_1fab440;

unsigned int TempAudioTimer_DeactivateTimer_d__3_MoveNext(struct_0 *ptr)
{
    long long v0[6];  // x8
    long long v1;  // x20
    struct_0 *p;  // x19

    if (!(g_1fab440 & 1))
    {
        sub_f7d92c(&g_1ef2440);
        g_1fab440 = 1;
    }
    v0 = ptr->field_20;
    if (ptr->field_10 == 1)
    {
        ptr->field_10 = 4294967295;
        if (!v0)
            sub_f7db74();
        if (v0[5])
            GameObject__SetActive(v0[5], 0, 0);
        else
            sub_f7db74();
    }
    else if (!ptr->field_10)
    {
        ptr->field_10 = 4294967295;
        if (v0 && v0[4] && AudioSource__get_clip(v0[4], 0))
        {
            AudioClip__get_length();
            v1 = sub_f7db70(g_1ef2440);
            WaitForSeconds__ctor(v1, 0);
            ptr->field_18 = v1;
            p = &ptr->field_18;
            sub_f7d8d0(p, v1);
            *((unsigned int *)&p->padding_0[8]) = 1;
            return 1;
        }
        sub_f7db74();
    }
    return 0;
}
```

## `TempAudioTimer.<DeactivateTimer>d__3.get_Current` — RVA `0xc8e1b0`

- Decompiled symbol: `TempAudioTimer_DeactivateTimer_d__3_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long TempAudioTimer_DeactivateTimer_d__3_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `TempAudioTimer.<DeactivateTimer>d__3.Reset` — RVA `0xc8e1b8`

- Decompiled symbol: `TempAudioTimer_DeactivateTimer_d__3_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f04fe8;

void TempAudioTimer_DeactivateTimer_d__3_Reset(void)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = sub_f7db70(sub_f7d940(&g_1ef0bd8));
    NotSupportedException__ctor(v4, 0);
    sub_f7da4c(v4, sub_f7d940(&g_1f04fe8));
}
```

## `TempAudioTimer.<DeactivateTimer>d__3.get_Current` — RVA `0xc8e1f0`

- Decompiled symbol: `TempAudioTimer_DeactivateTimer_d__3_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long TempAudioTimer_DeactivateTimer_d__3_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
